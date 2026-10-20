"""rio_tiler.experimental.zarr reader: rio-tiler Async reader built on top of zarr-python."""

from __future__ import annotations

import asyncio
import datetime
import math
import warnings
from collections.abc import Sequence
from functools import cached_property
from typing import Any, Literal, TypedDict, cast

import attr
import numpy
import zarr
from affine import Affine
from isochron import (
    UTC,
    Duration,
    ISO8601Error,
    format_datetime,
    parse_date,
    parse_datetime,
    parse_duration,
)
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.transform import array_bounds, from_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds, transform_geom
from rasterio.windows import from_bounds as window_from_bounds

from rio_tiler._warp import warp
from rio_tiler.constants import MAX_ARRAY_SIZE, WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    InvalidBounds,
    MaxArraySizeError,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.io import AsyncBaseReader, BaseReader
from rio_tiler.io.base import SpatialMixin
from rio_tiler.models import BandStatistics, Bounds, ImageData, Info, PointData
from rio_tiler.types import BBox, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import (
    CRS_to_uri,
    _get_width_height,
    _validate_shape_input,
    cast_to_sequence,
    estimate_output,
    has_width_or_height,
    output_size,
    run_sync,
)

MULTISCALE_CONVENTION_UUID = "d35379db-88df-4056-af3a-620245f8e347"
SPATIAL_CONVENTION_UUID = "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4"
PROJ_CONVENTION_UUID = "f17cb550-5864-4468-aeb7-f3180cfb622f"
COORDS_CONVENTION_UUID = "6ca4454a-658a-4348-a667-b39ced0e58cb"


def find_convention(conventions: list[dict], uuid: str) -> bool:
    """Check if a specific convention is present in the list of conventions."""
    return next(
        (True for c in conventions if c["uuid"] == uuid),
        False,
    )


def _get_proj_crs(attributes: dict) -> CRS:
    """Get CRS defined by PROJ conventions."""
    proj_string = next(
        (  # type: ignore
            attributes.get(key)
            for key in ["proj:code", "proj:wkt2", "proj:projjson"]
            if key in attributes
        )
    )
    return CRS.from_user_input(proj_string)


def _get_transform(attributes: dict) -> Affine | None:
    transform_type = attributes.get("spatial:transform_type") or "affine"
    tr = attributes.get("spatial:transform")
    if transform_type == "affine" and tr is not None:
        if attributes.get("spatial:registration", "pixel") == "node":
            # NOTE: If the registration is "node", we need to adjust the transform to
            # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
            tr[2] -= tr[0] / 2
            tr[5] -= tr[4] / 2

        return Affine(*tr)

    return None


SelMethod = Literal["nearest", "pad", "ffill", "backfill", "bfill"]


def _to_datetime64(value: Any) -> numpy.datetime64:
    """Convert a datetime-like value (ISO 8601 string, date, datetime) to a UTC naive `datetime64[ns]`."""
    if isinstance(value, numpy.datetime64):
        return value.astype("datetime64[ns]")

    if isinstance(value, str):
        try:
            value = parse_datetime(value)
        except ISO8601Error:
            value = parse_date(value)

    if isinstance(value, datetime.datetime):
        if value.tzinfo is not None:
            value = value.astimezone(UTC).replace(tzinfo=None)

    elif isinstance(value, datetime.date):
        value = datetime.datetime.combine(value, datetime.time())

    else:
        raise ValueError(f"Cannot convert {value!r} to datetime")

    return numpy.datetime64(value, "ns")


def _get_coordinate_values(coordinates: dict) -> numpy.ndarray | None:
    """Return coordinate values from coordinates convention.

    Supports for 2 types:
    - Inline coordinate values — short value vectors embedded directly in the metadata
        (for example, a 4-band spectral axis where allocating a separate array would be wasteful).
    - Implicit regularly spaced values — a compact start / end / step descriptor for axes that are uniformly spaced,
        covering both numeric domains (angles, distances, frequencies, levels) and ISO 8601 time intervals, without enumerating every value.

    Returns:
        numpy.ndarray: numeric, `datetime64[ns]` (temporal) or string values.

    """
    if coordinates["type"] == "interval":
        step: str | int | float = coordinates["step"]
        # Handle numeric interval
        if isinstance(step, (int, float)):
            start: int | float = coordinates["start"]
            stop: int | float = coordinates["stop"]
            size = int(round((stop - start) / step)) + 1
            return start + numpy.arange(size) * step

        # Handle ISO 8601 (temporal) interval
        elif isinstance(step, str):
            start_datetime = parse_datetime(coordinates["start"])
            stop_datetime = parse_datetime(coordinates["stop"])
            step_duration = parse_duration(step)
            if isinstance(step_duration, Duration):
                size = (stop_datetime - start_datetime) // step_duration.to_timedelta(
                    start_datetime
                ) + 1
            else:
                size = ((stop_datetime - start_datetime) // step_duration) + 1

            return numpy.array(
                [
                    _to_datetime64(start_datetime + i * step_duration)  # type: ignore
                    for i in range(size)
                ],
                dtype="datetime64[ns]",
            )

    elif coordinates["type"] == "inline":
        values = numpy.asarray(coordinates["values"])
        if values.dtype.kind in "iuf":
            return values

        # Temporal inline values (ISO 8601 strings)
        try:
            return numpy.array(
                [_to_datetime64(v) for v in values.tolist()], dtype="datetime64[ns]"
            )
        except (ISO8601Error, ValueError, TypeError):
            return values.astype(str)

    else:
        warnings.warn(f"Unsupported coordinate type '{coordinates['type']}'", UserWarning)

    return None


def _format_coordinate_values(values: numpy.ndarray) -> list[Any]:
    """Convert coordinate values to JSON friendly labels (ISO 8601 string for temporal values)."""
    if values.dtype.kind == "M":
        return [
            format_datetime(v.astype("datetime64[us]").item().replace(tzinfo=UTC))
            for v in values
        ]

    return values.tolist()


def _coerce_label(label: Any, values: numpy.ndarray) -> Any:
    """Cast a selection label to the coordinate values type."""
    kind = values.dtype.kind
    if kind == "M":
        return _to_datetime64(label)

    if kind in "iuf":
        return float(label) if isinstance(label, str) else label

    return str(label)


def _sel_label(
    values: numpy.ndarray,
    label: Any,
    method: SelMethod | None = None,
    dim: str = "",
) -> int:
    """Return the position of one label in the coordinate values."""
    label = _coerce_label(label, values)

    if method is None:
        idx = numpy.nonzero(values == label)[0]
        if not idx.size:
            raise KeyError(f"'{label}' not found in '{dim}' coordinates")

        return int(idx[0])

    if values.dtype.kind not in "iufM":
        raise ValueError(
            f"Selection method '{method}' is not supported for non-numeric '{dim}' coordinates"
        )

    order = numpy.argsort(values, kind="stable")
    sorted_values = values[order]
    size = len(sorted_values)

    if method in ["pad", "ffill"]:
        ix = int(numpy.searchsorted(sorted_values, label, side="right")) - 1
        if ix < 0:
            raise KeyError(f"No '{dim}' coordinate value before '{label}'")

    elif method in ["backfill", "bfill"]:
        ix = int(numpy.searchsorted(sorted_values, label, side="left"))
        if ix >= size:
            raise KeyError(f"No '{dim}' coordinate value after '{label}'")

    elif method == "nearest":
        right = min(int(numpy.searchsorted(sorted_values, label, side="left")), size - 1)
        left = max(right - 1, 0)
        # NOTE: like pandas, ties are resolved using the larger value
        ix = (
            left
            if abs(sorted_values[left] - label) < abs(sorted_values[right] - label)
            else right
        )

    else:
        raise ValueError(f"Invalid selection method '{method}'")

    return int(order[ix])


def _sel_indexer(
    values: numpy.ndarray,
    selector: Any,
    method: SelMethod | None = None,
    dim: str = "",
) -> int | numpy.ndarray | slice:
    """Convert a label-based selector to a positional indexer (like `xarray.DataArray.sel`).

    Args:
        values (numpy.ndarray): coordinate values.
        selector (Any): scalar label, sequence of labels or slice of labels (inclusive bounds).
        method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill).
        dim (str, optional): dimension name (for error messages).

    Returns:
        int, numpy.ndarray or slice: positional indexer.

    """
    if isinstance(selector, slice):
        if selector.step is not None:
            raise ValueError("Slice step is not supported for label based selection")

        increasing = bool(numpy.all(values[1:] >= values[:-1]))
        decreasing = bool(numpy.all(values[1:] <= values[:-1]))
        if not (increasing or decreasing):
            raise ValueError(f"Slice selection requires monotonic '{dim}' coordinates")

        inside = numpy.ones(values.shape, dtype=bool)
        if selector.start is not None:
            start = _coerce_label(selector.start, values)
            inside &= (values >= start) if increasing else (values <= start)

        if selector.stop is not None:
            stop = _coerce_label(selector.stop, values)
            inside &= (values <= stop) if increasing else (values >= stop)

        idx = numpy.nonzero(inside)[0]
        if not idx.size:
            raise KeyError(f"Empty selection for '{dim}' slice {selector}")

        return slice(int(idx[0]), int(idx[-1]) + 1)

    if isinstance(selector, (list, tuple, numpy.ndarray)):
        return numpy.array(
            [_sel_label(values, label, method, dim) for label in selector], dtype="int"
        )

    return _sel_label(values, selector, method, dim)


@attr.s
class ArrayMixin(SpatialMixin):
    """Shared attributes/methods for Async/Sync Array Readers."""

    input: zarr.AsyncArray | zarr.Array = attr.ib()

    crs: CRS = attr.ib(default=None)
    transform: Affine = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # Array dimension
    # Example: ["time", "x", "y"]
    dimensions: list[str] = attr.ib(default=None)

    # Dimension
    # https://github.com/zarr-conventions/spatial#spatialdimensions
    # The list in spatial:dimensions itself is ordered by axis role: the first entry
    # names the dimension carrying the logical Y axis; the second entry
    # names the dimension carrying the logical X axis.
    # Example: ["y", "x"]
    spatial_dims: list[str] = attr.ib(default=None)

    # Coordinates
    # https://github.com/christophenoel/zarr-coords
    # Example: {"bands": {"type": "inline", "values": ["b01", "b02"]}}
    coordinates: dict[str, Any] | None = attr.ib(default=None)

    # Array shape
    nbands: int = attr.ib(init=False)
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    # Array bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    def __attrs_post_init__(self) -> None:  # noqa: C901
        """Post init: derive height, width, count from array shape."""
        if self.input.ndim < 2:
            raise ValueError(
                f"Expected >=2D array, got {self.input.ndim}D with shape {self.input.shape}"
            )

        self.dimensions = self.dimensions or list(
            getattr(self.input.metadata, "dimension_names", [])
        )
        assert self.dimensions, (
            "Array dimensions are required, either as an argument or from zarr metadata."
        )
        assert len(self.dimensions) == self.input.ndim, (
            f"Dimensions metadata {len(self.dimensions)} does not match input array dimensions {self.input.ndim}"
        )

        # NOTE: zarr-python says attrs is of type dict[str, JSON]
        attributes = cast(dict[str, Any], self.input.attrs)
        conventions: list[dict] = attributes.get("zarr_conventions", [])

        # Spatial
        # NOTE: The transform is independent of the array's physical axis order:
        # a reader locates the X and Y array positions via dimension_names and
        # supplies the corresponding indices.
        # ref: https://github.com/zarr-conventions/spatial#spatialtransform
        _has_spatial = find_convention(conventions, SPATIAL_CONVENTION_UUID)
        if _has_spatial:
            self.spatial_dims = self.spatial_dims or attributes["spatial:dimensions"]
            self.transform = self.transform or _get_transform(attributes)

        assert self.transform, (
            "Affine transform is required, either as an argument or from `spatial` zarr_conventions."
        )
        assert self.spatial_dims, (
            "Spatial dimensions are required, either as an argument or from `spatial` zarr_conventions."
        )
        assert set(self.spatial_dims).intersection(set(self.dimensions)), (
            f"Incompatible spatial dimension {self.spatial_dims} and array dimensions {self.dimensions}"
        )

        # Proj
        _has_proj = find_convention(conventions, PROJ_CONVENTION_UUID)
        if _has_proj:
            self.crs = self.crs or _get_proj_crs(attributes)

        assert self.crs, (
            "CRS is required, either as an argument or from `proj` zarr_conventions."
        )

        y_index = self.dimensions.index(self.spatial_dims[0])
        x_index = self.dimensions.index(self.spatial_dims[1])
        shape = self.input.shape
        self.height = shape[y_index]
        self.width = shape[x_index]

        # NOTE: number of `bands` is the product of all the non-spatial dimensions
        self.nbands = int(
            numpy.prod(
                [
                    size
                    for size, dim in zip(shape, self.dimensions)
                    if dim not in self.spatial_dims
                ]
            )
        )

        # [xmin, ymin, xmax, ymax]
        self.bounds = array_bounds(self.height, self.width, self.transform)

        # Coordinates
        _has_coords = find_convention(conventions, COORDS_CONVENTION_UUID)
        if _has_coords:
            self.coordinates = self.coordinates or attributes["coords:coordinates"]

        # NOTE: coordinates are optional for non-spatial dimensions, if missing
        # we use the positions as coordinates values.
        if self.coordinates:
            assert set(self.coordinates.keys()).intersection(set(self.dimensions)), (
                f"Incompatible coordinates {list(self.coordinates.keys())} and array dimensions {self.dimensions}"
            )

    @property
    def minzoom(self):
        """Return dataset minzoom.

        NOTE: because a zarr.Array doesn't have overviews, minzoom is the same as maxzoom.
        """
        return self._maxzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self._maxzoom

    @cached_property
    def non_spatial_dims(self) -> list[str]:
        """Return the non-spatial dimensions (in array order)."""
        return [dim for dim in self.dimensions if dim not in self.spatial_dims]

    @cached_property
    def _coordinates(self) -> dict[str, tuple[numpy.ndarray, list[Any]]]:
        """Return coordinate values and labels for each non-spatial dimension.

        - values: derived from the `coordinates` (inline or interval), used for selection.
          Default to the array positions (`0, 1, ..., n - 1`) when not available.
        - labels: inline values as defined in the coordinates, formatted interval values
          or `{dim}{position + 1}` (e.g `time1`) when coordinates are not available.
        """
        coordinates = self.coordinates or {}

        out: dict[str, tuple[numpy.ndarray, list[Any]]] = {}
        for dim in self.non_spatial_dims:
            size = self.input.shape[self.dimensions.index(dim)]

            values: numpy.ndarray | None = None
            if dim in coordinates:
                values = _get_coordinate_values(coordinates[dim])
                if values is not None and len(values) != size:
                    warnings.warn(
                        f"Number of '{dim}' coordinates ({len(values)}) does not match the dimension size ({size}), using positions.",
                        UserWarning,
                    )
                    values = None

            if values is None:
                out[dim] = (numpy.arange(size), [f"{dim}{ix + 1}" for ix in range(size)])

            elif coordinates[dim]["type"] == "inline":
                out[dim] = (values, list(coordinates[dim]["values"]))

            else:
                out[dim] = (values, _format_coordinate_values(values))

        return out

    @property
    def coordinate_values(self) -> dict[str, numpy.ndarray]:
        """Return coordinate values (used for selection) for each non-spatial dimension."""
        return {dim: values for dim, (values, _) in self._coordinates.items()}

    def _get_labels(self, dim: str, idx: int | numpy.ndarray | slice) -> list[Any]:
        """Return labels for a positional selection on a non-spatial dimension."""
        labels = self._coordinates[dim][1]
        if isinstance(idx, int):
            return [labels[idx]]

        if isinstance(idx, slice):
            return labels[idx]

        return [labels[ix] for ix in idx]

    @property
    def dimensions_descriptions(self) -> dict[str, list[Any]]:
        """Return coordinate values (labels) for each non-spatial dimension (empty for 2D arrays)."""
        return {dim: self._get_labels(dim, slice(None)) for dim in self.coordinate_values}

    def _get_selection(
        self,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
    ) -> tuple[
        dict[str, int | numpy.ndarray | slice], dict[str, list[Any]], dict[str, Any]
    ]:
        """Convert label based selection to positional selection for non-spatial dimensions.

        Args:
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`).
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill).

        Returns:
            tuple: positional selection per dimension, labels of the kept dimensions and labels of the scalar selection (dropped dimensions).

        """
        sel = sel or {}
        if invalid := [dim for dim in sel if dim not in self.non_spatial_dims]:
            raise ValueError(
                f"Invalid selection dimension(s) {invalid}, should be one of {self.non_spatial_dims}"
            )

        selection: dict[str, int | numpy.ndarray | slice] = {}
        kept: dict[str, list[Any]] = {}
        scalars: dict[str, Any] = {}
        for dim, values in self.coordinate_values.items():
            idx: int | numpy.ndarray | slice = (
                _sel_indexer(values, sel[dim], sel_method, dim)
                if dim in sel
                else slice(None)
            )
            selection[dim] = idx
            if isinstance(idx, int):
                scalars[dim] = self._get_labels(dim, idx)[0]
            else:
                kept[dim] = self._get_labels(dim, idx)

        return selection, kept, scalars

    def _get_read_selection(
        self,
        *,
        y_slice: slice,
        x_slice: slice,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
    ) -> tuple[
        tuple[int | numpy.ndarray | slice, ...], dict[str, list[Any]], dict[str, Any]
    ]:
        """Build the orthogonal selection for a read and check the output size."""
        selection, kept, scalars = self._get_selection(sel, sel_method)

        read_height = len(range(*y_slice.indices(self.height)))
        read_width = len(range(*x_slice.indices(self.width)))
        shape = (*[len(labels) for labels in kept.values()], read_height, read_width)

        nbytes = int(numpy.prod(shape)) * self.input.dtype.itemsize
        if nbytes > MAX_ARRAY_SIZE:
            raise MaxArraySizeError(
                f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {shape} in memory."
            )

        selection[self.spatial_dims[0]] = y_slice
        selection[self.spatial_dims[1]] = x_slice

        return tuple(selection[dim] for dim in self.dimensions), kept, scalars

    def _to_image(
        self,
        data: numpy.ndarray,
        *,
        y_slice: slice,
        x_slice: slice,
        kept: dict[str, list[Any]],
        scalars: dict[str, Any],
        nodata: NoData | None = None,
    ) -> ImageData:
        """Create ImageData from an orthogonal selection result."""
        # Dimensions selected with a scalar are dropped by the orthogonal selection
        dims = [dim for dim in self.dimensions if dim not in scalars]

        # Make sure data is in form of (*non-spatial dimensions, height, width)
        data = numpy.moveaxis(
            data,
            [dims.index(self.spatial_dims[0]), dims.index(self.spatial_dims[1])],
            [-2, -1],
        )

        # Ensure at least 3D shape
        if data.ndim == 2:
            data = numpy.expand_dims(data, axis=0)

        masked_data = numpy.ma.MaskedArray(data)

        # if data has Nodata then we simply make sure the mask == the nodata
        nodata = (
            nodata
            if nodata is not None
            else getattr(self.input.metadata, "fill_value", None)
        )
        if nodata is not None:
            if numpy.isnan(nodata):
                masked_data.mask = numpy.isnan(masked_data.data)
            else:
                masked_data.mask = masked_data.data == nodata

        # Calculate bounds for the read window
        read_height, read_width = data.shape[-2:]
        y_start, _, _ = y_slice.indices(self.height)
        x_start, _, _ = x_slice.indices(self.width)
        read_transform = self.transform @ Affine.translation(x_start, y_start)
        read_bounds = array_bounds(read_height, read_width, read_transform)

        return ImageData(  # type: ignore
            masked_data,
            bounds=read_bounds,
            crs=self.crs,
            band_descriptions=kept,
            nodata=nodata,
            metadata={"sel": scalars} if scalars else {},
        )

    def _info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        nodata = getattr(self.input.metadata, "fill_value", None)
        if nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        attrs: dict[str, Any] = cast(dict[str, Any], self.input.attrs or {})

        meta: dict[str, Any] = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            "band_metadata": [],
            "band_descriptions": [],
            "dtype": self.input.dtype.name,
            "nodata_type": nodata_type,
            "colorinterp": None,
            # additional info (not in default model)
            "dimensions": self.dimensions,
            "dimensions_count": dict(zip(self.dimensions, self.input.shape)),
            "coordinates": self.coordinates,
            "attrs": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in attrs.items()
            },
        }

        minv, maxv = attrs.get("valid_min"), attrs.get("valid_max")
        if minv is not None and maxv is not None:
            meta["minmax"] = [(minv, maxv)]

        if nodata is not None:
            meta.update({"nodata_value": nodata.item()})

        return Info.model_validate(meta)


###############################################################################
#           AsyncArrayReader class for reading zarr AsyncArray                #
###############################################################################
@attr.s
class AsyncArrayReader(AsyncBaseReader, ArrayMixin):
    """Rio-tiler Zarr.AsyncArray Reader.

    A pure zarr-python async reader that accepts a zarr AsyncArray
    plus geospatial metadata (transform, crs) as input.

    Attributes:
        input: zarr AsyncArray (2D or 3D with bands-first layout).
        crs: Coordinate reference system.
        transform: Affine transform.
        tms: TileMatrixSet for tile operations.

    Note:
        For 3D arrays, expects bands-first layout (bands, height, width).
        For 2D arrays, treats as single-band (height, width).

    """

    input: zarr.AsyncArray = attr.ib()

    crs: CRS = attr.ib(default=None)
    transform: Affine = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # Array dimension
    # Example: ["time", "x", "y"]
    dimensions: list[str] = attr.ib(default=None)

    # Dimension
    # https://github.com/zarr-conventions/spatial#spatialdimensions
    # The list in spatial:dimensions itself is ordered by axis role: the first entry
    # names the dimension carrying the logical Y axis; the second entry
    # names the dimension carrying the logical X axis.
    # Example: ["y", "x"]
    spatial_dims: list[str] = attr.ib(default=None)

    # Coordinates
    # https://github.com/christophenoel/zarr-coords
    # Example: {"bands": {"type": "inline", "values": ["b01", "b02"]}}
    coordinates: dict[str, Any] | None = attr.ib(default=None)

    # Array shape
    nbands: int = attr.ib(init=False)
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    # Array bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        return self._info()

    async def statistics(
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        img = await self._read(sel=sel, sel_method=sel_method, nodata=nodata)
        if expression:
            img = img.apply_expression(expression)

        return img.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    async def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output tile size. Defaults to TMS tilesize.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        matrix = self.tms.matrix(tile_z)
        bbox = cast(
            BBox,
            self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)),
        )

        return await self.part(
            bbox,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            sel=sel,
            sel_method=sel_method,
            expression=expression,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
        )

    async def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to bounds_crs.
            bounds_crs (rasterio.crs.CRS, optional): CRS of the input bounds. Defaults to WGS84.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (str, optional): Resampling method for reprojection. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        dst_crs = dst_crs or bounds_crs

        # 1. Transform output bbox from bounds_crs → output_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 2. Estimate output shape and read window
        height, width, dst_bounds = estimate_output(
            dataset_crs=self.crs,
            dataset_transform=self.transform,  # type: ignore
            output_bounds=bbox,
            output_crs=dst_crs,
            output_height=height,
            output_width=width,
            max_size=max_size,
        )

        # 3. Build pixel window from bounds in dataset CRS
        window = window_from_bounds(*dst_bounds, transform=self.transform)

        # 4. Validate window intersection
        row_off = math.floor(window.row_off)
        col_off = math.floor(window.col_off)
        win_width = math.ceil(window.width) + 1
        win_height = math.ceil(window.height) + 1

        col_end = min(self.width, math.ceil(window.col_off + window.width))
        row_end = min(self.height, math.ceil(window.row_off + window.height))
        if col_off >= col_end or row_off >= row_end:
            raise InvalidBounds("Input BBOX and dataset bounds do not intersect")

        # 5. Clamp window to array bounds
        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(self.width, col_off + win_width)
        clipped_row_stop = min(self.height, row_off + win_height)

        # 6. Read data from zarr array
        img = await self._read(
            y_slice=slice(clipped_row_off, clipped_row_stop),
            x_slice=slice(clipped_col_off, clipped_col_stop),
            sel=sel,
            sel_method=sel_method,
            nodata=nodata,
        )

        # 7. Reproject/resample to output CRS and dimensions
        img = await run_sync(
            warp,
            img,
            dst_crs=dst_crs,
            dst_bounds=bbox,
            dst_width=width,
            dst_height=height,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
        )

        if expression:
            img = img.apply_expression(expression)

        return img

    async def preview(
        self,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        dst_crs: CRS | None = None,
        max_size: int | None = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Args:
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to None (same as input).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            resampling_method (str, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (str, optional): GDAL Resampling method to use when reprojecting. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        dst_crs = dst_crs or self.crs

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width: int = self.width
        dst_height: int = self.height
        if dst_crs != self.crs:
            # Get shape of the dataset in the output CRS
            _, dst_width, dst_height = calculate_default_transform(  # type: ignore
                self.crs, dst_crs, self.width, self.height, *self.bounds
            )

        height, width = output_size(
            dataset_height=dst_height,
            dataset_width=dst_width,
            output_height=height,
            output_width=width,
            max_size=max_size,
        )

        # 2. Read data
        img = await self._read(sel=sel, sel_method=sel_method, nodata=nodata)
        if expression:
            img = img.apply_expression(expression)

        # 3. Reproject if needed
        if dst_crs != self.crs:
            img = await run_sync(
                img.reproject,
                dst_crs=dst_crs,
                reproject_method=reproject_method,
            )

        # 4. Resize
        if width != img.width or height != img.height:
            img = await run_sync(
                img.resize,
                width=width,
                height=height,
                resampling_method=resampling_method,
            )

        return img

    async def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.
            nodata: (int or float, optional): Overwrite dataset internal nodata value. Defaults to `None`.

        Returns:
            PointData: Pixel value per bands/assets.

        """
        coordinates = (lon, lat)
        if coord_crs != self.crs:
            xs, ys = transform_coords(coord_crs, self.crs, [lon], [lat])
            lon, lat = xs[0], ys[0]

        dataset_min_lon, dataset_min_lat, dataset_max_lon, dataset_max_lat = self.bounds
        # check if latitude is inverted
        if dataset_min_lat > dataset_max_lat:
            warnings.warn(
                "BoundingBox of the dataset is inverted (minLat > maxLat).",
                UserWarning,
            )

        dataset_min_lat, dataset_max_lat = (
            min(dataset_min_lat, dataset_max_lat),
            max(dataset_min_lat, dataset_max_lat),
        )
        if not (
            (dataset_min_lon < lon < dataset_max_lon)
            and (dataset_min_lat < lat < dataset_max_lat)
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        y, x = rowcol(self.transform, lon, lat)

        img = await self._read(
            y_slice=slice(y, y + 1),
            x_slice=slice(x, x + 1),
            sel=sel,
            sel_method=sel_method,
            nodata=nodata,
        )

        pt = PointData(
            img.array[..., 0, 0],
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            coordinates=coordinates,
            crs=coord_crs,
            pixel_location=(x, y),
            nodata=img.nodata,
            scales=img.scales,
            offsets=img.offsets,
            metadata=img.metadata,
        )
        if expression:
            pt = pt.apply_expression(expression)

        return pt

    async def feature(
        self,
        shape: dict,
        dst_crs: CRS | None = None,
        shape_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        img = await self.part(
            bbox,
            dst_crs=dst_crs,
            bounds_crs=shape_crs,
            sel=sel,
            sel_method=sel_method,
            expression=expression,
            max_size=max_size,
            height=height,
            width=width,
            nodata=nodata,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        cutline_mask = (
            await run_sync(
                rasterize,
                [shape],
                out_shape=(img.height, img.width),
                transform=img.transform,
                all_touched=True,  # Mandatory for matching masks at different resolutions
                default_value=0,
                fill=1,
                dtype="uint8",
            )
        ).astype("bool")

        img.cutline_mask = cutline_mask
        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img

    async def _read(
        self,
        *,
        y_slice: slice | None = None,
        x_slice: slice | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        nodata: NoData | None = None,
    ) -> ImageData:
        """Read data from zarr AsyncArray.

        Args:
            y_slice: index along the Y-axis dimension (named in self.spatial_dim[0]).
            x_slice: index along the X-axis dimension (named in self.spatial_dim[1])
            sel (dict, optional): label based selection for non-spatial dimensions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill).
            nodata (int or float, optional): Overwrite dataset internal nodata value.

        Returns:
            ImageData: Image data with shape (*non-spatial dimensions, height, width), mask and spatial info.

        """
        y_slice = y_slice or slice(None)
        x_slice = x_slice or slice(None)

        selection, kept, scalars = self._get_read_selection(
            y_slice=y_slice, x_slice=x_slice, sel=sel, sel_method=sel_method
        )
        data = await self.input.get_orthogonal_selection(selection)

        return self._to_image(
            data,  # type: ignore[arg-type]
            y_slice=y_slice,
            x_slice=x_slice,
            kept=kept,
            scalars=scalars,
            nodata=nodata,
        )


###############################################################################
#                 ArrayReader class for reading zarr Array                    #
###############################################################################
@attr.s
class ArrayReader(BaseReader, ArrayMixin):
    """Rio-tiler Zarr.Array Reader.

    A pure zarr-python sync reader that accepts a zarr.Array
    plus geospatial metadata (transform, crs) as input.

    Attributes:
        input: zarr Array (2D or 3D with bands-first layout).
        crs: Coordinate reference system.
        transform: Affine transform.
        tms: TileMatrixSet for tile operations.

    Note:
        For 3D arrays, expects bands-first layout (bands, height, width).
        For 2D arrays, treats as single-band (height, width).

    """

    input: zarr.Array = attr.ib()

    crs: CRS = attr.ib(default=None)
    transform: Affine = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # Array dimension
    # Example: ["time", "x", "y"]
    dimensions: list[str] = attr.ib(default=None)

    # Dimension
    # https://github.com/zarr-conventions/spatial#spatialdimensions
    # The list in spatial:dimensions itself is ordered by axis role: the first entry
    # names the dimension carrying the logical Y axis; the second entry
    # names the dimension carrying the logical X axis.
    # Example: ["y", "x"]
    spatial_dims: list[str] = attr.ib(default=None)

    # Coordinates
    # https://github.com/christophenoel/zarr-coords
    # Example: {"bands": {"type": "inline", "values": ["b01", "b02"]}}
    coordinates: dict[str, Any] | None = attr.ib(default=None)

    # Array shape
    nbands: int = attr.ib(init=False)
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    # Array bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        return self._info()

    def statistics(
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        img = self._read(sel=sel, sel_method=sel_method, nodata=nodata)
        if expression:
            img = img.apply_expression(expression)

        return img.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output tile size. Defaults to TMS tilesize.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        matrix = self.tms.matrix(tile_z)
        bbox = cast(
            BBox,
            self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)),
        )

        return self.part(
            bbox,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            sel=sel,
            sel_method=sel_method,
            expression=expression,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
        )

    def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to bounds_crs.
            bounds_crs (rasterio.crs.CRS, optional): CRS of the input bounds. Defaults to WGS84.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (str, optional): Resampling method for reprojection. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        dst_crs = dst_crs or bounds_crs

        # 1. Transform output bbox from bounds_crs → output_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 2. Estimate output shape and read window
        height, width, dst_bounds = estimate_output(
            dataset_crs=self.crs,
            dataset_transform=self.transform,  # type: ignore
            output_bounds=bbox,
            output_crs=dst_crs,
            output_height=height,
            output_width=width,
            max_size=max_size,
        )

        # 3. Build pixel window from bounds in dataset CRS
        window = window_from_bounds(*dst_bounds, transform=self.transform)

        # 4. Validate window intersection
        row_off = math.floor(window.row_off)
        col_off = math.floor(window.col_off)
        win_width = math.ceil(window.width) + 1
        win_height = math.ceil(window.height) + 1

        col_end = min(self.width, math.ceil(window.col_off + window.width))
        row_end = min(self.height, math.ceil(window.row_off + window.height))
        if col_off >= col_end or row_off >= row_end:
            raise InvalidBounds("Input BBOX and dataset bounds do not intersect")

        # 5. Clamp window to array bounds
        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(self.width, col_off + win_width)
        clipped_row_stop = min(self.height, row_off + win_height)

        # 6. Read data from zarr array
        img = self._read(
            sel=sel,
            sel_method=sel_method,
            y_slice=slice(clipped_row_off, clipped_row_stop),
            x_slice=slice(clipped_col_off, clipped_col_stop),
            nodata=nodata,
        )

        # 7. Reproject/resample to output CRS and dimensions
        img = warp(
            img,
            dst_crs=dst_crs,
            dst_bounds=bbox,
            dst_width=width,
            dst_height=height,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
        )

        if expression:
            img = img.apply_expression(expression)

        return img

    def preview(
        self,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        dst_crs: CRS | None = None,
        max_size: int | None = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Args:
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to None (same as input).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            resampling_method (str, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (str, optional): GDAL Resampling method to use when reprojecting. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        dst_crs = dst_crs or self.crs

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width: int = self.width
        dst_height: int = self.height
        if dst_crs != self.crs:
            # Get shape of the dataset in the output CRS
            _, dst_width, dst_height = calculate_default_transform(  # type: ignore
                self.crs, dst_crs, self.width, self.height, *self.bounds
            )

        height, width = output_size(
            dataset_height=dst_height,
            dataset_width=dst_width,
            output_height=height,
            output_width=width,
            max_size=max_size,
        )

        # 2. Read data
        img = self._read(sel=sel, sel_method=sel_method, nodata=nodata)
        if expression:
            img = img.apply_expression(expression)

        # 3. Reproject if needed
        if dst_crs != self.crs:
            img = img.reproject(
                dst_crs=dst_crs,
                reproject_method=reproject_method,
            )

        # 4. Resize
        if width != img.width or height != img.height:
            img = img.resize(
                width=width,
                height=height,
                resampling_method=resampling_method,
            )

        return img

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.
            nodata: (int or float, optional): Overwrite dataset internal nodata value. Defaults to `None`.

        Returns:
            PointData: Pixel value per bands/assets.

        """
        coordinates = (lon, lat)
        if coord_crs != self.crs:
            xs, ys = transform_coords(coord_crs, self.crs, [lon], [lat])
            lon, lat = xs[0], ys[0]

        dataset_min_lon, dataset_min_lat, dataset_max_lon, dataset_max_lat = self.bounds
        # check if latitude is inverted
        if dataset_min_lat > dataset_max_lat:
            warnings.warn(
                "BoundingBox of the dataset is inverted (minLat > maxLat).",
                UserWarning,
            )

        dataset_min_lat, dataset_max_lat = (
            min(dataset_min_lat, dataset_max_lat),
            max(dataset_min_lat, dataset_max_lat),
        )
        if not (
            (dataset_min_lon < lon < dataset_max_lon)
            and (dataset_min_lat < lat < dataset_max_lat)
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        y, x = rowcol(self.transform, lon, lat)

        img = self._read(
            y_slice=slice(y, y + 1),
            x_slice=slice(x, x + 1),
            sel=sel,
            sel_method=sel_method,
            nodata=nodata,
        )

        pt = PointData(
            img.array[..., 0, 0],
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            coordinates=coordinates,
            crs=coord_crs,
            pixel_location=(x, y),
            nodata=img.nodata,
            scales=img.scales,
            offsets=img.offsets,
            metadata=img.metadata,
        )
        if expression:
            pt = pt.apply_expression(expression)

        return pt

    def feature(
        self,
        shape: dict,
        dst_crs: CRS | None = None,
        shape_crs: CRS = WGS84_CRS,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.
            sel (dict, optional): label based selection for non-spatial dimensions (e.g `{"time": "2025-01-01", "z": [10, 20]}`). Dimensions without coordinates use positions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        img = self.part(
            bbox,
            dst_crs=dst_crs,
            bounds_crs=shape_crs,
            sel=sel,
            sel_method=sel_method,
            expression=expression,
            max_size=max_size,
            height=height,
            width=width,
            nodata=nodata,
            reproject_method=reproject_method,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        cutline_mask = rasterize(
            [shape],
            out_shape=(img.height, img.width),
            transform=img.transform,
            all_touched=True,  # Mandatory for matching masks at different resolutions
            default_value=0,
            fill=1,
            dtype="uint8",
        ).astype("bool")

        img.cutline_mask = cutline_mask
        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img

    def _read(
        self,
        *,
        y_slice: slice | None = None,
        x_slice: slice | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        nodata: NoData | None = None,
    ) -> ImageData:
        """Read data from zarr Array.

        Args:
            y_slice: index along the Y-axis dimension (named in self.spatial_dim[0]).
            x_slice: index along the X-axis dimension (named in self.spatial_dim[1])
            sel (dict, optional): label based selection for non-spatial dimensions.
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill).
            nodata (int or float, optional): Overwrite dataset internal nodata value.

        Returns:
            ImageData: Image data with shape (*non-spatial dimensions, height, width), mask and spatial info.

        """
        y_slice = y_slice or slice(None)
        x_slice = x_slice or slice(None)

        selection, kept, scalars = self._get_read_selection(
            y_slice=y_slice, x_slice=x_slice, sel=sel, sel_method=sel_method
        )
        data = self.input.get_orthogonal_selection(selection)

        return self._to_image(
            data,  # type: ignore[arg-type]
            y_slice=y_slice,
            x_slice=x_slice,
            kept=kept,
            scalars=scalars,
            nodata=nodata,
        )


def _get_zoom(
    tms: TileMatrixSet,
    crs: CRS,
    width: int,
    height: int,
    bounds: BBox,
) -> int:
    """Get MaxZoom for a Group."""
    tms_crs = tms.rasterio_crs
    if crs != tms_crs:
        transform, _, _ = calculate_default_transform(
            crs,
            tms_crs,
            width,
            height,
            *bounds,
        )
    else:
        transform = from_bounds(*bounds, width, height)

    resolution = max(abs(transform[0]), abs(transform[4]))
    return tms.zoom_for_res(resolution)


class ArrayMetadata(TypedDict):
    """Array Metadata."""

    array: zarr.AsyncArray | zarr.Array
    crs: CRS
    transform: Affine
    height: int
    width: int
    spatial_dims: list[str]
    coordinates: dict[str, Any] | None


class GroupMetadata(TypedDict):
    """Group Metadata."""

    crs: CRS | None
    bbox: BBox | None
    transform: Affine | None
    multiscale: bool
    arrays: dict[str, list[ArrayMetadata]]


def calculate_output_transform(
    crs: CRS,
    bounds: BBox,
    height: int,
    width: int,
    out_crs: CRS,
    *,
    out_bounds: BBox | None = None,
    out_max_size: int | None = None,
    out_height: int | None = None,
    out_width: int | None = None,
) -> Affine:
    """Calculate Reprojected Dataset transform."""
    # 1. get the `whole` reprojected dataset transfrom, shape and bounds
    dst_transform, dst_width, dst_height = calculate_default_transform(
        crs,
        out_crs,
        width,
        height,
        *bounds,
    )

    # If no bounds we assume the full dataset bounds
    out_bounds = out_bounds or array_bounds(dst_height, dst_width, dst_transform)

    # output Bounds
    w, s, e, n = out_bounds

    # adjust dataset virtual output shape/transform
    dst_width = max(1, round((e - w) / dst_transform.a))
    dst_height = max(1, round((s - n) / dst_transform.e))

    # Output Transform in Output CRS
    dst_transform = from_bounds(w, s, e, n, dst_width, dst_height)

    # 2. adjust output size based on max_size if
    # - not input width/height
    # - max_size < dst_width and dst_height
    if out_max_size:
        out_height, out_width = _get_width_height(out_max_size, dst_height, dst_width)

    elif out_height or out_width:
        if not out_height or not out_width:
            # get the size's ratio of the reprojected dataset
            ratio = dst_height / dst_width
            if out_width:
                out_height = math.ceil(out_width * ratio)
            else:
                out_width = math.ceil(out_height / ratio)

    out_height = out_height or dst_height
    out_width = out_width or dst_width

    # Get the transform in the Dataset CRS
    transform, _, _ = calculate_default_transform(
        out_crs,
        crs,
        out_width,
        out_height,
        *out_bounds,
    )

    return transform


def get_target_resolution(
    *,
    input_crs: CRS,
    output_crs: CRS,
    input_height: int,
    input_width: int,
    input_transform: Affine,
    output_bounds: BBox | None = None,
    output_max_size: int | None = None,
    output_height: int | None = None,
    output_width: int | None = None,
) -> float:
    """Get Target Resolution."""
    input_bounds = array_bounds(input_height, input_width, input_transform)

    # Get Target expected resolution in Dataset CRS
    # 1. Reprojection
    if output_crs and output_crs != input_crs:
        dst_transform = calculate_output_transform(
            input_crs,
            input_bounds,
            input_height,
            input_width,
            output_crs,
            # bounds is supposed to be in output_crs
            out_bounds=output_bounds,
            out_max_size=output_max_size,
            out_height=output_height,
            out_width=output_width,
        )
        return dst_transform.a

    # 2. No Reprojection
    # If no bounds we assume the full dataset bounds
    bounds = output_bounds or input_bounds
    window = window_from_bounds(*bounds, transform=input_transform)
    if output_max_size:
        output_height, output_width = _get_width_height(
            output_max_size, round(window.height), round(window.width)
        )

    elif has_width_or_height(output_width, output_height):
        ratio = window.height / window.width
        if output_width:
            output_height = math.ceil(output_width * ratio)
        else:
            output_width = math.ceil(output_height / ratio)

    height = output_height or max(1, round(window.height))
    width = output_width or max(1, round(window.width))
    return from_bounds(*bounds, height=height, width=width).a


def get_multiscale_level(
    variable_metadata: list[ArrayMetadata],
    target_res: float,
    zoom_level_strategy: Literal["AUTO", "LOWER", "UPPER"] = "AUTO",
) -> ArrayMetadata:
    """Return the multiscale level corresponding to the desired resolution."""
    ms_resolutions: list[tuple[float, ArrayMetadata]] = [
        (min(abs(ms["transform"][0]), abs(ms["transform"][4])), ms)
        for ms in variable_metadata
    ]

    # Based on aiocogeo:
    # https://github.com/geospatial-jeff/aiocogeo/blob/5a1d32c3f22c883354804168a87abb0a2ea1c328/aiocogeo/partial_reads.py#L113-L147
    percentage = {"AUTO": 50, "LOWER": 100, "UPPER": 0}.get(zoom_level_strategy, 50)

    # Iterate over zoom levels from lowest/coarsest to highest/finest. If the `target_res` is more than `percentage`
    # percent of the way from the zoom level below to the zoom level above, then upsample the zoom level below, else
    # downsample the zoom level above.
    available_resolutions = sorted(ms_resolutions, key=lambda x: x[0], reverse=True)
    if len(available_resolutions) == 1:
        return available_resolutions[0][1]

    for i in range(0, len(available_resolutions) - 1):
        res_current, _ = available_resolutions[i]
        res_higher, _ = available_resolutions[i + 1]
        threshold = res_higher - (res_higher - res_current) * (percentage / 100.0)
        if target_res > threshold or target_res == res_current:
            return available_resolutions[i][1]

    # Default level is the first ms level
    return ms_resolutions[0][1]


class GeoZarrInfo(Bounds):
    """GeoZarr Info."""

    driver: str
    variables: list[dict[str, Any]]
    attributes: dict[str, Any]


@attr.s
class GroupMixin(SpatialMixin):
    """Shared attributes/methods for Async/Sync Group Readers."""

    input: zarr.AsyncGroup | zarr.Group = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    crs: CRS = attr.ib(init=False)
    transform: Affine = attr.ib(init=False, default=None)

    # Group shape
    height: int = attr.ib(init=False, default=None)
    width: int = attr.ib(init=False, default=None)

    # Group bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    # list of availables the groups with variables (used for cache)
    _groups: dict[str, GroupMetadata] = attr.ib(init=False, factory=dict)
    _variables: list[dict[str, Any]] = attr.ib(init=False, default=None)

    _group_var_sep: str = ":"

    def __attrs_post_init__(self) -> None:
        """Post init: derive height, width, count from array shape."""
        attributes = cast(dict[str, Any], self.input.attrs)
        conventions: list[dict] = attributes.get("zarr_conventions", [])

        # Default CRS/Bounds for a Zarr Store
        self.crs = WGS84_CRS
        self.bounds = (-180.0, -90.0, 180.0, 90.0)

        transform: Affine | None = None
        height: int | None = None
        width: int | None = None
        bounds: BBox | None = None
        if find_convention(conventions, SPATIAL_CONVENTION_UUID) and find_convention(
            conventions, PROJ_CONVENTION_UUID
        ):
            # CRS
            crs = _get_proj_crs(attributes)

            if bbox := attributes.get("spatial:bbox"):
                bounds = tuple(bbox)

            # Transform
            # Case 1: Transform at group level
            transform = _get_transform(attributes)

            if spatial_shape := attributes.get("spatial:shape"):
                height, width = spatial_shape[-2:]

            # Case 2: check multiscales for transform and shape
            if find_convention(conventions, MULTISCALE_CONVENTION_UUID):
                # assume the first layout is the highest resolution
                first_res = attributes["multiscales"]["layout"][0]

                if bbox := first_res.get("spatial:bbox"):
                    bounds = bounds or bbox

                transform = transform or _get_transform(first_res)

                if spatial_shape := first_res.get("spatial:shape"):
                    h, w = spatial_shape[-2:]
                    height = height or h
                    width = width or w

            if not bounds and all([width, height, transform]):
                bounds = array_bounds(height, width, transform)

            if bounds:
                self.crs = crs
                self.bounds = bounds
                if transform:
                    self.transform = transform

            if all([height, width]):
                self.height = height
                self.width = width

    @property
    def minzoom(self) -> int:
        """Return dataset minzoom."""
        attributes = cast(dict[str, Any], self.input.attrs)

        conventions: list[dict] = attributes.get("zarr_conventions", [])
        if find_convention(conventions, MULTISCALE_CONVENTION_UUID):
            # NOTE: assume the last layout is the lowest resolution
            last_res = attributes["multiscales"]["layout"][-1]

            # NOTE: assume `spatial:shape` and `spatial:transform` are provided
            # at the layout level (if not present at group level)
            transform = _get_transform(last_res)
            if transform and (spatial_shape := last_res.get("spatial:shape")):
                height, width = spatial_shape[-2:]
                return _get_zoom(
                    tms=self.tms,
                    crs=self.crs,
                    width=width,
                    height=height,
                    bounds=array_bounds(height, width, transform),
                )

        if not self.transform:
            return self.tms.minzoom

        return self.maxzoom

    @property
    def maxzoom(self) -> int:
        """Return dataset maxzoom."""
        attributes = cast(dict[str, Any], self.input.attrs)

        conventions: list[dict] = attributes.get("zarr_conventions", [])
        if find_convention(conventions, MULTISCALE_CONVENTION_UUID):
            # NOTE: assume the first layout is the highest resolution
            first_res = attributes["multiscales"]["layout"][0]

            # NOTE: assume `spatial:shape` and `spatial:transform` are provided
            # at the layout level (if not present at group level)
            transform = _get_transform(first_res)
            if transform and (spatial_shape := first_res.get("spatial:shape")):
                height, width = spatial_shape[-2:]
                return _get_zoom(
                    tms=self.tms,
                    crs=self.crs,
                    width=width,
                    height=height,
                    bounds=array_bounds(height, width, transform),
                )

        # NOTE: By construction we know that if `self.transform` is set
        # self.bounds and self.crs are also comming from the zarr attributes.
        if self.transform:
            w = self.width
            h = self.height
            if not self.width or not self.height:
                w = round((self.bounds[2] - self.bounds[0]) / abs(self.transform.a))
                h = round((self.bounds[3] - self.bounds[1]) / abs(self.transform.e))

            dst_affine = self.transform
            tms_crs = self.tms.rasterio_crs
            if self.crs != tms_crs:
                dst_affine, _, _ = calculate_default_transform(
                    self.crs,
                    self.tms.rasterio_crs,
                    w,
                    h,
                    *self.bounds,
                )
            resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
            return self.tms.zoom_for_res(resolution)

        return self.tms.maxzoom

    def parse_variable(self, variable: str) -> tuple[str | None, str, Any | None]:
        """Parse variable name into group, variable and options."""
        group_name: str | None = None
        if self._group_var_sep in variable:
            group_name, variable = variable.split(self._group_var_sep)[0:2]

        return group_name, variable, None

    def select_variable(
        self,
        variable_metadata: list[ArrayMetadata],
        *,
        # MultiScale Selection
        bounds: BBox | None = None,
        height: int | None = None,
        width: int | None = None,
        max_size: int | None = None,
        dst_crs: CRS | None = None,
    ) -> ArrayMetadata:
        """Get DataArray from xarray Dataset."""
        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' and 'width' set.",
                UserWarning,
                stacklevel=2,
            )
            max_size = None

        # Default variable is the first one (hihhest resolution)
        variable = variable_metadata[0]
        if len(variable_metadata) == 1:
            # NOTE: Only one variable, return it
            return variable

        # NOTE: Select a Multiscale Layer based on output resolution
        if any([height, width, max_size]):
            transform = variable["transform"]
            layout_height = variable["height"]
            layout_width = variable["width"]
            crs = variable["crs"]

            target_res = get_target_resolution(
                input_crs=crs,
                output_crs=dst_crs,
                input_height=layout_height,
                input_width=layout_width,
                input_transform=transform,
                output_bounds=bounds,
                output_max_size=max_size,
                output_height=height,
                output_width=width,
            )

            variable = get_multiscale_level(variable_metadata, target_res)

        return variable


###############################################################################
#          AsyncGroupReader class for reading zarr AsyncGroup                 #
###############################################################################
@attr.s
class AsyncGroupReader(AsyncBaseReader, GroupMixin):
    """Rio-tiler GeoZarr Reader.

    A pure zarr-python async reader that accepts a zarr AsyncGroup (GeoZarr)

    Attributes:
        input: zarr AsyncGroup
        tms: TileMatrixSet for tile operations.

    """

    input: zarr.AsyncGroup = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    crs: CRS = attr.ib(init=False)
    transform: Affine = attr.ib(init=False, default=None)

    # Group shape
    height: int = attr.ib(init=False, default=None)
    width: int = attr.ib(init=False, default=None)

    # Group bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    # list of availables the groups with variables (used for cache)
    _groups: dict[str, GroupMetadata] = attr.ib(init=False, factory=dict)
    _variables: list[dict[str, Any]] = attr.ib(init=False, default=None)

    _group_var_sep: str = ":"

    async def get_bounds(
        self,
        *,
        variables: Sequence[str] | str,
        crs: CRS = WGS84_CRS,
    ) -> BBox:  # noqa: C901
        """Get BBox for variables."""
        variables = cast_to_sequence(variables)

        async def _get_bounds(variable: str) -> BBox:
            group_name, variable, _ = self.parse_variable(variable)

            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            bounds_crs = group_metadata["crs"]
            bbox = group_metadata["bbox"]
            if not bounds_crs or not bbox:
                array_metadata = self.select_variable(array)
                bbox = array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                )
                bounds_crs = array_metadata["crs"]

            if bounds_crs != crs:
                return cast(
                    BBox, transform_bounds(bounds_crs, crs, *bbox, densify_pts=21)
                )

            return bbox

        bounds = await asyncio.gather(*(_get_bounds(variable) for variable in variables))
        minx, miny, maxx, maxy = zip(*bounds)
        return (min(minx), min(miny), max(maxx), max(maxy))

    async def get_minzoom(
        self,
        *,
        variables: Sequence[str] | str,
    ) -> int:
        """Get minzoom for variables."""
        variables = cast_to_sequence(variables)

        async def _get_minzoom(variable: str) -> int:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            # Assume the last array is the lowest resolution
            array_metadata = array[-1]
            return _get_zoom(
                tms=self.tms,
                crs=array_metadata["crs"],
                width=array_metadata["width"],
                height=array_metadata["height"],
                bounds=array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                ),
            )

        zooms = await asyncio.gather(*(_get_minzoom(variable) for variable in variables))
        return min(zooms)

    async def get_maxzoom(
        self,
        *,
        variables: Sequence[str] | str,
    ) -> int:
        """Get maxzoom for variables."""
        variables = cast_to_sequence(variables)

        async def _get_maxzoom(variable: str) -> int:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            # Assume the first array is the highest resolution
            array_metadata = array[0]
            return _get_zoom(
                tms=self.tms,
                crs=array_metadata["crs"],
                width=array_metadata["width"],
                height=array_metadata["height"],
                bounds=array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                ),
            )

        zooms = await asyncio.gather(*(_get_maxzoom(variable) for variable in variables))
        return max(zooms)

    async def list_variables(self) -> list[dict[str, Any]]:
        """List variables in the Zarr store."""
        if self._variables is not None:
            return self._variables

        ms_groups = []
        variables: list[dict[str, Any]] = []

        # 1. Check Root level group
        group_metadata = await self.get_group_metadata()

        # Zarr store is a multiscale group
        if group_metadata["multiscale"]:
            ms_groups.append("__root__")

        # 2. Root has top level arrays
        if arrays := group_metadata["arrays"]:
            variables.extend(
                [
                    {
                        "name": name,
                        "group": None,
                        "long_name": name,
                        "multiscale": group_metadata["multiscale"],
                    }
                    for name, _ in arrays.items()
                ]
            )

        # 3. Check children groups
        else:
            async for group_name, member in self.input.members(max_depth=10):
                if any(group_name.startswith(msg) for msg in ms_groups):
                    continue

                # Check Group for variables
                if isinstance(member, zarr.AsyncGroup):
                    group_metadata = await self.get_group_metadata(group_name)
                    is_multiscale = group_metadata["multiscale"]
                    if is_multiscale:
                        ms_groups.append(group_name)

                    if arrays := group_metadata["arrays"]:
                        variables.extend(
                            [
                                {
                                    "name": name,
                                    "group": group_name,
                                    "long_name": f"{group_name}{self._group_var_sep}{name}",
                                    "multiscale": is_multiscale,
                                }
                                for name, _ in arrays.items()
                            ]
                        )

        self._variables = variables
        return self._variables

    async def get_group_metadata(  # noqa: C901
        self,
        group: str | None = None,
    ) -> GroupMetadata:
        """Find arrays in a Zarr store and extract spatial metadata."""
        group = group or "__root__"

        if group in self._groups:
            return self._groups[group]

        g = self.input if group == "__root__" else await self.input.getitem(group)
        assert isinstance(g, zarr.AsyncGroup), (
            f"Group '{group}' not found in the Zarr store."
        )

        arrays: dict[str, list[ArrayMetadata]] = {}

        root_crs: CRS | None = None
        root_transform: Affine | None = None
        root_bbox: BBox | None = None
        coordinates: dict[str, Any] | None = None
        spatial_dims: list[str] | None = None

        attributes = cast(dict[str, Any], g.attrs)
        conventions = attributes.get("zarr_conventions", [])
        # Top Level spatial/geo metadata
        # 1. Group level metadata (crs, transform)
        if find_convention(conventions, PROJ_CONVENTION_UUID):
            root_crs = _get_proj_crs(attributes)

        if find_convention(conventions, SPATIAL_CONVENTION_UUID):
            spatial_dims = attributes["spatial:dimensions"]
            root_transform = _get_transform(attributes)
            root_bbox = attributes.get("spatial:bbox")

        if find_convention(conventions, COORDS_CONVENTION_UUID):
            coordinates = attributes["coords:coordinates"]

        group_is_multiscale = find_convention(conventions, MULTISCALE_CONVENTION_UUID)
        if group_is_multiscale:
            # NOTE: We assume a group with multiscale should have geo-proj convention
            assert root_crs, (
                f"`proj:code` missing for multiscales group '{g.name}' metadata"
            )

            # 1. Multiscales metadata
            ms_group: dict[str, dict[str, Any]] = {}
            for layout in attributes["multiscales"]["layout"]:
                ms_group[layout["asset"]] = {
                    "transform": _get_transform(layout),
                }

            # 2. list all arrays for each layout
            for group_name, meta in ms_group.items():
                msgroup = await g.getitem(group_name)

                # NOTE: `ms_group` reference group names so we know `getitem` return a group
                msgroup = cast(zarr.AsyncGroup, msgroup)
                async for array in msgroup.array_values():
                    # NOTE: skip non-data arrays
                    # TODO: be smarter
                    if array.ndim < 2:
                        continue

                    array_attributes = cast(dict[str, Any], array.attrs)
                    array_conventions = array_attributes.get("zarr_conventions", [])

                    variable_name = array.name.split("/")[-1]
                    if variable_name not in arrays:
                        arrays[variable_name] = []

                    # NOTE: Transform from the array or the multiscale layout
                    transform = _get_transform(array_attributes) or meta["transform"]
                    assert transform, (
                        f"`spatial:transform` missing for multiscales layout {group_name} (path: '{array.name}')"
                    )

                    array_spatial_dims = (
                        array_attributes.get("spatial:dimensions") or spatial_dims or []
                    )
                    if not array_spatial_dims:
                        # TODO: add warning when spatial:dimensions is not set
                        continue

                    dims = getattr(array.metadata, "dimension_names", [])
                    if not dims:
                        # TODO: add warning when both dimension_names is not set
                        continue

                    y_dim_pos = dims.index(array_spatial_dims[0])
                    x_dim_pos = dims.index(array_spatial_dims[1])
                    height = array.shape[y_dim_pos]
                    width = array.shape[x_dim_pos]

                    array_coordinates = coordinates
                    if find_convention(array_conventions, COORDS_CONVENTION_UUID):
                        array_coordinates = cast(
                            dict[str, Any], array_attributes["coords:coordinates"]
                        )

                    arrays[variable_name].append(
                        {
                            "array": array,
                            "crs": root_crs,
                            "height": height,
                            "width": width,
                            "transform": transform,
                            "spatial_dims": array_spatial_dims,
                            "coordinates": array_coordinates,
                        }
                    )

        else:
            # List arrays in group
            async for array in g.array_values():
                array_crs: CRS | None = None
                array_transform: Affine | None = None

                # NOTE: skip non-data arrays
                # TODO: be smarter
                if array.ndim < 2:
                    continue

                array_attributes = cast(dict[str, Any], array.attrs)
                array_conventions = array_attributes.get("zarr_conventions", [])
                if find_convention(array_conventions, PROJ_CONVENTION_UUID):
                    array_crs = _get_proj_crs(array_attributes)

                if find_convention(array_conventions, SPATIAL_CONVENTION_UUID):
                    array_transform = _get_transform(array_attributes)

                array_crs = array_crs or root_crs
                array_transform = _get_transform(array_attributes) or root_transform
                array_spatial_dims = (
                    array_attributes.get("spatial:dimensions") or spatial_dims or []
                )
                if not array_spatial_dims:
                    # TODO: add warning when spatial:dimensions is not set
                    continue

                dims = getattr(array.metadata, "dimension_names", [])
                if not dims:
                    # TODO: add warning when both dimension_names is not set
                    continue

                y_dim_pos = dims.index(array_spatial_dims[0])
                x_dim_pos = dims.index(array_spatial_dims[1])
                height = array.shape[y_dim_pos]
                width = array.shape[x_dim_pos]

                array_coordinates = coordinates
                if find_convention(array_conventions, COORDS_CONVENTION_UUID):
                    array_coordinates = cast(
                        dict[str, Any], array_attributes["coords:coordinates"]
                    )

                if all([array_crs, array_transform]):
                    array_name = array.name.replace(f"{g.name}/", "").lstrip("/")
                    arrays[array_name] = [
                        {
                            "array": array,
                            "crs": array_crs,
                            "height": height,
                            "width": width,
                            "transform": array_transform,
                            "spatial_dims": array_spatial_dims,
                            "coordinates": array_coordinates,
                        }
                    ]

        self._groups[group] = {
            "crs": root_crs,
            "bbox": root_bbox,
            "transform": root_transform,
            "multiscale": group_is_multiscale,
            "arrays": arrays,
        }

        return self._groups[group]

    async def info(self) -> GeoZarrInfo:  # type: ignore[override]
        """Return Dataset's info.

        Returns:
            GeoZarrInfo: Dataset info.

        """
        availables_variables = await self.list_variables()

        attrs: dict[str, Any] = self.input.attrs or {}

        meta: dict[str, Any] = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            # additional info (not in default model)
            "driver": "GeoZarr",
            "variables": availables_variables,
            "attributes": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in attrs.items()
            },
        }

        return GeoZarrInfo.model_validate(meta)

    async def statistics(  # type: ignore[override]
        self,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        max_size: int | None = 1024,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            variables (list of str or str, optional): list of variables to return value for. Defaults to all variables.
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        img = await self.preview(
            variables=variables,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            max_size=max_size,
            nodata=nodata,
            **kwargs,
        )

        return img.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    async def tile(  # type: ignore[override]
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        tilesize: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        # NOTE: if the top level bbox doesn't exist this, should always return False
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        matrix = self.tms.matrix(tile_z)
        bbox = cast(
            BBox,
            self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)),
        )

        return await self.part(
            bbox,
            variables=variables,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
            **kwargs,
        )

    async def part(  # type: ignore[override]
        self,
        bbox: BBox,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            variables (list of str or str): list of variables to return value for.
            sel (dict, optional): label based selection for non-spatial dimensions, applied to all the variables (e.g `{"time": "2025-01-01"}`).
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        variables = cast_to_sequence(variables)

        dst_crs = dst_crs or bounds_crs

        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        async def _part(variable: str) -> ImageData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(
                array,
                bounds=bbox,
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )
            async with AsyncArrayReader(
                input=cast(zarr.AsyncArray, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return await src.part(
                    bbox,
                    dst_crs=dst_crs,
                    bounds_crs=dst_crs,
                    max_size=max_size,
                    height=height,
                    width=width,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                    reproject_method=reproject_method,
                )

        img_stack = await asyncio.gather(*(_part(variable) for variable in variables))

        img = ImageData.create_from_list(img_stack)
        if not img.is_nd:
            img.band_names = [f"b{ix + 1}" for ix in range(img.count)]

        if expression:
            return img.apply_expression(expression)

        return img

    async def preview(  # type: ignore[override]
        self,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        dst_crs: CRS | None = None,
        max_size: int | None = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        variables = cast_to_sequence(variables)

        async def _preview(variable: str) -> ImageData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(
                array,
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )
            async with AsyncArrayReader(
                input=cast(zarr.AsyncArray, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return await src.preview(
                    max_size=max_size,
                    height=height,
                    width=width,
                    dst_crs=dst_crs,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                    resampling_method=resampling_method,
                    reproject_method=reproject_method,
                    **kwargs,
                )

        img_stack = await asyncio.gather(*(_preview(variable) for variable in variables))

        img = ImageData.create_from_list(img_stack)
        if not img.is_nd:
            img.band_names = [f"b{ix + 1}" for ix in range(img.count)]

        if expression:
            return img.apply_expression(expression)

        return img

    async def point(  # type: ignore[override]
        self,
        lon: float,
        lat: float,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        coord_crs: CRS = WGS84_CRS,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            rio_tiler.models.PointData: PointData instance with data, mask and spatial info.

        """
        variables = cast_to_sequence(variables)

        async def _point(variable: str) -> PointData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = await self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(array)
            async with AsyncArrayReader(
                input=cast(zarr.AsyncArray, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return await src.point(
                    lon,
                    lat,
                    coord_crs=coord_crs,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                )

        point_stack = await asyncio.gather(*(_point(variable) for variable in variables))

        pt = PointData.create_from_list(point_stack)
        if not pt.is_nd:
            pt.band_names = [f"b{ix + 1}" for ix in range(pt.count)]

        if expression:
            return pt.apply_expression(expression)

        return pt

    async def feature(  # type: ignore[override]
        self,
        shape: dict,
        *,
        variables: Sequence[str] | str,
        dst_crs: CRS | None = None,
        shape_crs: CRS = WGS84_CRS,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        img = await self.part(
            bbox,
            variables=variables,
            dst_crs=dst_crs,
            bounds_crs=shape_crs,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            max_size=max_size,
            height=height,
            width=width,
            nodata=nodata,
            reproject_method=reproject_method,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        cutline_mask = (
            await run_sync(
                rasterize,
                [shape],
                out_shape=(img.height, img.width),
                transform=img.transform,
                all_touched=True,  # Mandatory for matching masks at different resolutions
                default_value=0,
                fill=1,
                dtype="uint8",
            )
        ).astype("bool")

        img.cutline_mask = cutline_mask
        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img


###############################################################################
#                 GroupReader class for reading zarr Group                   #
###############################################################################
@attr.s
class GroupReader(BaseReader, GroupMixin):
    """Rio-tiler Zarr.Group Reader.

    A pure zarr-python sync reader that accepts a zarr.Group (GeoZarr)

    Attributes:
        input: zarr Group
        tms: TileMatrixSet for tile operations.

    """

    input: zarr.Group = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    crs: CRS = attr.ib(init=False)
    transform: Affine = attr.ib(init=False, default=None)

    # Group shape
    height: int = attr.ib(init=False, default=None)
    width: int = attr.ib(init=False, default=None)

    # Group bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    # list of availables the groups with variables (used for cache)
    _groups: dict[str, GroupMetadata] = attr.ib(init=False, factory=dict)
    _variables: list[dict[str, Any]] = attr.ib(init=False, default=None)

    _group_var_sep: str = ":"

    def get_bounds(
        self,
        *,
        variables: Sequence[str] | str,
        crs: CRS = WGS84_CRS,
    ) -> BBox:  # noqa: C901
        """Get BBox for variables."""
        variables = cast_to_sequence(variables)

        def _get_bounds(variable: str) -> BBox:
            group_name, variable, _ = self.parse_variable(variable)

            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            bounds_crs = group_metadata["crs"]
            bbox = group_metadata["bbox"]
            if not bounds_crs or not bbox:
                array_metadata = self.select_variable(array)
                bbox = array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                )
                bounds_crs = array_metadata["crs"]

            if bounds_crs != crs:
                return cast(
                    BBox, transform_bounds(bounds_crs, crs, *bbox, densify_pts=21)
                )

            return bbox

        bounds = [_get_bounds(variable) for variable in variables]
        minx, miny, maxx, maxy = zip(*bounds)
        return (min(minx), min(miny), max(maxx), max(maxy))

    def get_minzoom(
        self,
        *,
        variables: Sequence[str] | str,
    ) -> int:
        """Get minzoom for variables."""
        variables = cast_to_sequence(variables)

        def _get_minzoom(variable: str) -> int:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            # Assume the last array is the lowest resolution
            array_metadata = array[-1]
            return _get_zoom(
                tms=self.tms,
                crs=array_metadata["crs"],
                width=array_metadata["width"],
                height=array_metadata["height"],
                bounds=array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                ),
            )

        zooms = [_get_minzoom(variable) for variable in variables]
        return min(zooms)

    def get_maxzoom(
        self,
        *,
        variables: Sequence[str] | str,
    ) -> int:
        """Get maxzoom for variables."""
        variables = cast_to_sequence(variables)

        def _get_maxzoom(variable: str) -> int:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            # Assume the first array is the highest resolution
            array_metadata = array[0]
            return _get_zoom(
                tms=self.tms,
                crs=array_metadata["crs"],
                width=array_metadata["width"],
                height=array_metadata["height"],
                bounds=array_bounds(
                    array_metadata["height"],
                    array_metadata["width"],
                    array_metadata["transform"],
                ),
            )

        zooms = [_get_maxzoom(variable) for variable in variables]
        return max(zooms)

    def list_variables(self) -> list[dict[str, Any]]:
        """List variables in the Zarr store."""
        if self._variables is not None:
            return self._variables

        ms_groups = []
        variables: list[dict[str, Any]] = []

        # 1. Check Root level group
        group_metadata = self.get_group_metadata()

        # Zarr store is a multiscale group
        if group_metadata["multiscale"]:
            ms_groups.append("__root__")

        # 2. Root has top level arrays
        if arrays := group_metadata["arrays"]:
            variables.extend(
                [
                    {
                        "name": name,
                        "group": None,
                        "long_name": name,
                        "multiscale": group_metadata["multiscale"],
                        # "nbands": array[0]["array"].shape[0]
                        # if len(array[0]["array"].shape) == 3
                        # else 1,
                    }
                    for name, array in arrays.items()
                ]
            )

        # 3. Check children groups
        else:
            for group_name, member in self.input.members(max_depth=10):
                if any(group_name.startswith(msg) for msg in ms_groups):
                    continue

                # Check Group for variables
                if isinstance(member, zarr.Group):
                    group_metadata = self.get_group_metadata(group_name)
                    is_multiscale = group_metadata["multiscale"]
                    if is_multiscale:
                        ms_groups.append(group_name)

                    if arrays := group_metadata["arrays"]:
                        variables.extend(
                            [
                                {
                                    "name": name,
                                    "group": group_name,
                                    "long_name": f"{group_name}{self._group_var_sep}{name}",
                                    "multiscale": is_multiscale,
                                    # "nbands": array[0]["array"].shape[0]
                                    # if len(array[0]["array"].shape) == 3
                                    # else 1,
                                }
                                for name, array in arrays.items()
                            ]
                        )

        self._variables = variables
        return self._variables

    def get_group_metadata(  # noqa: C901
        self,
        group: str | None = None,
    ) -> GroupMetadata:
        """Find arrays in a Zarr store and extract spatial metadata."""
        group = group or "__root__"

        if group in self._groups:
            return self._groups[group]

        g = self.input if group == "__root__" else self.input[group]
        assert isinstance(g, zarr.Group), f"Group '{group}' not found in the Zarr store."

        arrays: dict[str, list[ArrayMetadata]] = {}

        root_crs: CRS | None = None
        root_transform: Affine | None = None
        root_bbox: BBox | None = None
        coordinates: dict[str, Any] | None = None
        spatial_dims: list[str] | None = None

        group_attributes = cast(dict[str, Any], g.attrs)
        group_conventions = cast(list[dict], group_attributes.get("zarr_conventions", []))

        # Top Level spatial/geo metadata
        # 1. Group level metadata (crs, transform)
        if find_convention(group_conventions, PROJ_CONVENTION_UUID):
            root_crs = _get_proj_crs(group_attributes)

        if find_convention(group_conventions, SPATIAL_CONVENTION_UUID):
            spatial_dims = group_attributes["spatial:dimensions"]
            root_transform = _get_transform(group_attributes)
            root_bbox = group_attributes.get("spatial:bbox")

        if find_convention(group_conventions, COORDS_CONVENTION_UUID):
            coordinates = group_attributes["coords:coordinates"]

        group_is_multiscale = find_convention(
            group_conventions, MULTISCALE_CONVENTION_UUID
        )
        if group_is_multiscale:
            # NOTE: We assume a group with multiscale should have geo-proj convention
            assert root_crs, (
                f"`proj:code` missing for multiscales group '{g.name}' metadata"
            )

            # 1. Multiscales metadata
            ms_group: dict[str, dict[str, Any]] = {}
            for layout in group_attributes["multiscales"]["layout"]:
                ms_group[layout["asset"]] = {
                    "transform": _get_transform(layout),
                }

            # 2. list all arrays for each layout
            for group_name, meta in ms_group.items():
                msgroup = g[group_name]

                # NOTE: `ms_group` reference group names so we know `getitem` return a group
                msgroup = cast(zarr.Group, msgroup)
                for array in msgroup.array_values():
                    # NOTE: skip non-data arrays
                    # TODO: be smarter
                    if array.ndim < 2:
                        continue

                    variable_name = array.name.split("/")[-1]
                    if variable_name not in arrays:
                        arrays[variable_name] = []

                    array_attributes = cast(dict[str, Any], array.attrs)
                    array_conventions = array_attributes.get("zarr_conventions", [])
                    # NOTE: Transform from the array or the multiscale layout
                    transform = _get_transform(array_attributes) or meta["transform"]
                    assert transform, (
                        f"`spatial:transform` missing for multiscales layout {group_name} (path: '{array.name}')"
                    )

                    array_spatial_dims = (
                        array_attributes.get("spatial:dimensions") or spatial_dims
                    )

                    dims = getattr(array.metadata, "dimension_names", [])
                    if dims:
                        y_dim_pos = dims.index(array_spatial_dims[0])
                        x_dim_pos = dims.index(array_spatial_dims[1])
                        height = array.shape[y_dim_pos]
                        width = array.shape[x_dim_pos]

                    else:
                        # TODO: raise warning when dimension_names is not set
                        height, width = array.shape[-2:]

                    array_coordinates = coordinates
                    if find_convention(array_conventions, COORDS_CONVENTION_UUID):
                        array_coordinates = cast(
                            dict[str, Any], array_attributes["coords:coordinates"]
                        )

                    arrays[variable_name].append(
                        {
                            "array": array,
                            "crs": root_crs,
                            "height": height,
                            "width": width,
                            "transform": transform,
                            "spatial_dims": array_spatial_dims,
                            "coordinates": array_coordinates,
                        }
                    )

        else:
            # List arrays in group
            for array in g.array_values():
                array_crs: CRS | None = None
                array_transform: Affine | None = None

                # NOTE: skip non-data arrays
                # TODO: be smarter
                if array.ndim < 2:
                    continue

                array_attributes = cast(dict[str, Any], array.attrs)
                array_conventions = array_attributes.get("zarr_conventions", [])

                if find_convention(array_conventions, PROJ_CONVENTION_UUID):
                    array_crs = _get_proj_crs(array_attributes)

                if find_convention(array_conventions, SPATIAL_CONVENTION_UUID):
                    array_transform = _get_transform(array_attributes)

                array_crs = array_crs or root_crs
                array_transform = _get_transform(array_attributes) or root_transform
                array_spatial_dims = (
                    array_attributes.get("spatial:dimensions") or spatial_dims
                )

                dims = getattr(array.metadata, "dimension_names", [])
                if dims:
                    y_dim_pos = dims.index(array_spatial_dims[0])
                    x_dim_pos = dims.index(array_spatial_dims[1])
                    height = array.shape[y_dim_pos]
                    width = array.shape[x_dim_pos]
                else:
                    # TODO: raise warning when dimension_names is not set
                    height, width = array.shape[-2:]

                array_coordinates = coordinates
                if find_convention(array_conventions, COORDS_CONVENTION_UUID):
                    array_coordinates = cast(
                        dict[str, Any], array_attributes["coords:coordinates"]
                    )

                if all([array_crs, array_transform]):
                    array_name = array.name.replace(f"{g.name}/", "").lstrip("/")
                    arrays[array_name] = [
                        {
                            "array": array,
                            "crs": array_crs,
                            "height": height,
                            "width": width,
                            "transform": array_transform,
                            "spatial_dims": array_spatial_dims,
                            "coordinates": array_coordinates,
                        }
                    ]

        self._groups[group] = {
            "crs": root_crs,
            "bbox": root_bbox,
            "transform": root_transform,
            "multiscale": group_is_multiscale,
            "arrays": arrays,
        }

        return self._groups[group]

    def info(self) -> GeoZarrInfo:  # type: ignore[override]
        """Return Dataset's info.

        Returns:
            GeoZarrInfo: Dataset info.

        """
        availables_variables = self.list_variables()

        attrs: dict[str, Any] = cast(dict[str, Any], self.input.attrs or {})

        meta: dict[str, Any] = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            # additional info (not in default model)
            "driver": "GeoZarr",
            "variables": availables_variables,
            "attributes": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in attrs.items()
            },
        }

        return GeoZarrInfo.model_validate(meta)

    def statistics(  # type: ignore[override]
        self,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        max_size: int | None = 1024,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            variables (list of str or str, optional): list of variables to return value for. Defaults to all variables.
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        img = self.preview(
            variables=variables,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            max_size=max_size,
            nodata=nodata,
            **kwargs,
        )

        return img.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    def tile(  # type: ignore[override]
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        tilesize: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        # NOTE: if the top level bbox doesn't exist this, should always return False
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        matrix = self.tms.matrix(tile_z)
        bbox = cast(
            BBox,
            self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)),
        )

        return self.part(
            bbox,
            variables=variables,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
            **kwargs,
        )

    def part(  # type: ignore[override]
        self,
        bbox: BBox,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            variables (list of str or str): list of variables to return value for.
            sel (dict, optional): label based selection for non-spatial dimensions, applied to all the variables (e.g `{"time": "2025-01-01"}`).
            sel_method (str, optional): method to use for inexact matches (nearest, pad/ffill, backfill/bfill). Defaults to exact match.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        variables = cast_to_sequence(variables)

        dst_crs = dst_crs or bounds_crs

        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        def _part(variable: str) -> ImageData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(
                array,
                bounds=bbox,
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )
            with ArrayReader(
                input=cast(zarr.Array, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return src.part(
                    bbox,
                    dst_crs=dst_crs,
                    bounds_crs=dst_crs,
                    max_size=max_size,
                    height=height,
                    width=width,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                    reproject_method=reproject_method,
                )

        img = ImageData.create_from_list([_part(variable) for variable in variables])
        if not img.is_nd:
            img.band_names = [f"b{ix + 1}" for ix in range(img.count)]

        if expression:
            return img.apply_expression(expression)

        return img

    def preview(  # type: ignore[override]
        self,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        dst_crs: CRS | None = None,
        max_size: int | None = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        variables = cast_to_sequence(variables)

        def _preview(variable: str) -> ImageData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(
                array,
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )
            with ArrayReader(
                input=cast(zarr.Array, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return src.preview(
                    max_size=max_size,
                    height=height,
                    width=width,
                    dst_crs=dst_crs,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                    resampling_method=resampling_method,
                    reproject_method=reproject_method,
                    **kwargs,
                )

        img = ImageData.create_from_list([_preview(variable) for variable in variables])
        if not img.is_nd:
            img.band_names = [f"b{ix + 1}" for ix in range(img.count)]

        if expression:
            return img.apply_expression(expression)

        return img

    def point(  # type: ignore[override]
        self,
        lon: float,
        lat: float,
        *,
        variables: Sequence[str] | str,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        coord_crs: CRS = WGS84_CRS,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            rio_tiler.models.PointData: PointData instance with data, mask and spatial info.

        """
        variables = cast_to_sequence(variables)

        def _point(variable: str) -> PointData:
            group_name, variable, _ = self.parse_variable(variable)
            group_metadata = self.get_group_metadata(group_name)
            array = group_metadata["arrays"].get(variable)
            if not array:
                raise ValueError(
                    f"Variable '{variable}' not found in '{group_name}' group."
                )

            array_metadata = self.select_variable(array)
            with ArrayReader(
                input=cast(zarr.Array, array_metadata["array"]),
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                coordinates=array_metadata["coordinates"],
                spatial_dims=array_metadata["spatial_dims"],
                tms=self.tms,
            ) as src:
                return src.point(
                    lon,
                    lat,
                    coord_crs=coord_crs,
                    sel=sel,
                    sel_method=sel_method,
                    nodata=nodata,
                )

        pt = PointData.create_from_list([_point(variable) for variable in variables])
        if not pt.is_nd:
            pt.band_names = [f"b{ix + 1}" for ix in range(pt.count)]

        if expression:
            return pt.apply_expression(expression)

        return pt

    def feature(  # type: ignore[override]
        self,
        shape: dict,
        *,
        variables: Sequence[str] | str,
        dst_crs: CRS | None = None,
        shape_crs: CRS = WGS84_CRS,
        expression: str | None = None,
        sel: dict[str, Any] | None = None,
        sel_method: SelMethod | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        img = self.part(
            bbox,
            variables=variables,
            dst_crs=dst_crs,
            bounds_crs=shape_crs,
            expression=expression,
            sel=sel,
            sel_method=sel_method,
            max_size=max_size,
            height=height,
            width=width,
            nodata=nodata,
            reproject_method=reproject_method,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        cutline_mask = rasterize(
            [shape],
            out_shape=(img.height, img.width),
            transform=img.transform,
            all_touched=True,  # Mandatory for matching masks at different resolutions
            default_value=0,
            fill=1,
            dtype="uint8",
        ).astype("bool")

        img.cutline_mask = cutline_mask
        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img


# TODO: remove in 10.0
Reader = AsyncArrayReader
GeoZarrReader = AsyncGroupReader
