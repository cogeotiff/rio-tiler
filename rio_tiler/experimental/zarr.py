"""rio_tiler.experimental.zarr reader: rio-tiler Async reader built on top of zarr-python."""

from __future__ import annotations

import math
import warnings
from collections.abc import Sequence
from typing import Any, cast

import attr
import numpy
import zarr
from affine import Affine
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.transform import array_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds, transform_geom
from rasterio.windows import from_bounds as window_from_bounds

from rio_tiler._warp import warp
from rio_tiler.constants import MAX_ARRAY_SIZE, WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    ExpressionMixingWarning,
    MaxArraySizeError,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.expression import parse_expression
from rio_tiler.io import AsyncBaseReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import (
    CRS_to_uri,
    _get_width_height,
    _missing_size,
    _validate_shape_input,
    cast_to_sequence,
)


def _has_spatial(conventions: list[dict]) -> bool:
    return next(
        (
            True
            for c in conventions
            if c["uuid"] == "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4"
        ),
        False,
    )


def _has_proj(conventions: list[dict]) -> bool:
    return next(
        (
            True
            for c in conventions
            if c["uuid"] == "f17cb550-5864-4468-aeb7-f3180cfb622f"
        ),
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


@attr.s
class Reader(AsyncBaseReader):
    """Rio-tiler Zarr.AsyncArray Reader.

    A pure zarr-python async reader that accepts a zarr AsyncArray
    plus geospatial metadata (transform, crs) as input.

    Attributes:
        input: zarr AsyncArray (2D or 3D with bands-first layout).
        crs: Coordinate reference system.
        transform: Affine transform.
        tms: TileMatrixSet for tile operations.
        options: Reader options including nodata.
        colormap: Optional colormap dictionary.

    Note:
        For 3D arrays, expects bands-first layout (bands, height, width).
        For 2D arrays, treats as single-band (height, width).

    """

    input: zarr.AsyncArray = attr.ib()

    crs: CRS | None = attr.ib(default=None)
    transform: Affine | None = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # Array shape
    nbands: int = attr.ib(init=False)
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    # Array bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    # List of names for the first dimension (e.g time, bands, etc)
    band_names: list[str] | None = attr.ib(default=None)

    colormap: dict | None = attr.ib(default=None)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def __attrs_post_init__(self) -> None:
        """Post init: derive height, width, count from array shape."""
        if self.input.ndim not in (2, 3):
            raise ValueError(
                f"Expected 2D or 3D array, got {self.input.ndim}D with shape {self.input.shape}"
            )

        spatial_dims = ["y", "x", "latitude", "longitude", "lat", "lon"]

        # NOTE: zarr-python says attrs is of type dict[str, JSON]
        attributes = cast(dict[str, Any], self.input.attrs)
        conventions: list[dict] = attributes.get("zarr_conventions", [])

        # Transform
        if not self.transform and _has_spatial(conventions):
            # NOTE: `spatial:dimensions` is the only required attribute for the `spatial` convention
            # but if this ever change we default to list of common spatial dimension names
            spatial_dims = attributes.get("spatial:dimensions", spatial_dims)

            transform_type = attributes.get("spatial:transform_type") or "affine"
            tr = attributes.get("spatial:transform")
            if transform_type == "affine" and tr is not None:
                if attributes.get("spatial:registration", "pixel") == "node":
                    # NOTE: If the registration is "node", we need to adjust the transform to
                    # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                    tr[2] -= tr[0] / 2
                    tr[5] -= tr[4] / 2

                self.transform = Affine(*tr)

        assert self.transform, (
            "Affine transform is required, either as an argument or in `spatial` zarr_conventions"
        )

        # CRS
        if not self.crs and _has_proj(conventions):
            self.crs = _get_proj_crs(attributes)

        assert self.crs, (
            "CRS is required, either as an argument or in `geo-proj` zarr_conventions"
        )

        shape = self.input.shape
        if len(shape) == 2:
            self.nbands = 1
            self.height = shape[0]
            self.width = shape[1]
        elif len(shape) == 3:
            self.nbands = shape[0]
            self.height = shape[1]
            self.width = shape[2]

        self.bounds = array_bounds(self.height, self.width, self.transform)

        dimensions = getattr(self.input.metadata, "dimension_names", [])
        self._dims = [d for d in dimensions if d.lower() not in spatial_dims]

        if self.band_names:
            assert len(self.band_names) == self.nbands, (
                "Length of band_names must match number of bands in the array"
            )

    @property
    def band_descriptions(self) -> list[str]:
        """
        Return list of `band descriptions` in DataArray.

        `Bands` are all dimensions not defined as spatial dims by rioxarray.
        """
        if self.band_names:
            return self.band_names

        return [f"b{ix + 1}" for ix in range(self.nbands)]

    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        nodata = getattr(self.input.metadata, "fill_value", None)
        if nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        attrs: dict[str, Any] = self.input.attrs or {}

        meta: dict[str, Any] = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            "band_metadata": [(f"b{ix + 1}", {}) for ix in range(self.nbands)],
            "band_descriptions": [
                (f"b{ix}", val) for ix, val in enumerate(self.band_descriptions, 1)
            ],
            "dtype": self.input.dtype.name,
            "nodata_type": nodata_type,
            "colorinterp": None,
            # additional info (not in default model)
            "driver": "Zarr",
            "count": self.nbands,
            "width": self.width,
            "height": self.height,
            "dimensions": self._dims,
            "attrs": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in attrs.items()
            },
        }

        if nodata is not None:
            meta.update({"nodata_value": nodata.item()})

        return Info.model_validate(meta)

    async def statistics(
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        indexes: Indexes | None = None,
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
            indexes (int or sequence of int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        nbytes = await self.input.nbytes_stored()
        if nbytes > MAX_ARRAY_SIZE:
            raise MaxArraySizeError(
                f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {self.input.shape} in memory."
            )

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        img = await self._read(indexes=indexes, nodata=nodata)
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
        indexes: Indexes | None = None,
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
            indexes (sequence of int or int, optional): Band indexes.
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
            indexes=indexes,
            expression=expression,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
        )

    async def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
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
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to bounds_crs.
            bounds_crs (rasterio.crs.CRS, optional): CRS of the input bounds. Defaults to WGS84.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (str, optional): Resampling method for reprojection. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        dst_crs = dst_crs or bounds_crs

        # Transform bbox from bounds_crs → dst_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 1. Estimate output dimensions
        if dst_crs != self.crs:
            # Case 1: Reprojection needed
            # - reproject bbox to dataset CRS
            # - compute native output shape in dataset resolution/CRS
            # - compute output shape in output CRS
            dst_bounds = transform_bounds(dst_crs, self.crs, *bbox, densify_pts=21)
            native_src_w = max(
                1, round((dst_bounds[2] - dst_bounds[0]) / abs(self.transform.a))
            )
            native_src_h = max(
                1, round((dst_bounds[3] - dst_bounds[1]) / abs(self.transform.e))
            )
            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, native_src_w, native_src_h, *dst_bounds
            )
        else:
            # Case 2: No reprojection needed
            # - keep output dataset bbox as input bbox
            # - compute output shape in dataset resolution/CRS
            dst_bounds = bbox
            dst_width = max(1, round((bbox[2] - bbox[0]) / abs(self.transform.a)))
            dst_height = max(1, round((bbox[3] - bbox[1]) / abs(self.transform.e)))

        # Case 1: `max_size` is set,
        # compute output shape based on it,
        # respecting aspect ratio of the output bbox (dst_width/dst_height)
        if max_size:
            height, width = _get_width_height(max_size, dst_height, dst_width)

        # Case 2: One of width/height is missing,
        # compute it but keep the aspect ratio from the max output bbox (dst_width/dst_height)
        elif _missing_size(width, height):
            ratio = dst_height / dst_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        # 2. Output shape (in the output CRS)
        height = cast(int, height or dst_height)
        width = cast(int, width or dst_width)

        # 3. Build pixel window from bounds in dataset CRS
        rasterio_win = window_from_bounds(*dst_bounds, transform=self.transform)
        row_off = math.floor(rasterio_win.row_off)
        col_off = math.floor(rasterio_win.col_off)
        win_width = math.ceil(rasterio_win.width) + 1
        win_height = math.ceil(rasterio_win.height) + 1

        # Validate intersection
        col_end = min(self.width, math.ceil(rasterio_win.col_off + rasterio_win.width))
        row_end = min(self.height, math.ceil(rasterio_win.row_off + rasterio_win.height))
        if col_off >= col_end or row_off >= row_end:
            raise ValueError("Input BBOX and dataset bounds do not intersect")

        # Clamp window to array bounds
        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(self.width, col_off + win_width)
        clipped_row_stop = min(self.height, row_off + win_height)

        # 3. Read data from zarr array
        img = await self._read(
            indexes=indexes,
            row_slice=slice(clipped_row_off, clipped_row_stop),
            col_slice=slice(clipped_col_off, clipped_col_stop),
            nodata=nodata,
        )

        # 4. Reproject/resample to output CRS and dimensions
        img = warp(
            img,
            dst_crs=dst_crs,
            dst_bounds=bbox,
            dst_width=width,
            dst_height=height,
            reproject_method=reproject_method,
        )

        if expression:
            img = img.apply_expression(expression)

        return img

    async def preview(
        self,
        indexes: Indexes | None = None,
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
            indexes (sequence of int or int, optional): Band indexes.
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
        nbytes = await self.input.nbytes_stored()
        if nbytes > MAX_ARRAY_SIZE:
            raise MaxArraySizeError(
                f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {self.input.shape} in memory."
            )

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width = self.width
        dst_height = self.height
        if dst_crs and dst_crs != self.crs:
            # Get shape of the dataset in the output CRS
            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, self.width, self.height, *self.bounds
            )

        if max_size:
            height, width = _get_width_height(max_size, dst_height, dst_width)

        elif _missing_size(width, height):
            ratio = dst_height / dst_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        # Shape in the output CRS
        height = height or dst_height
        width = width or dst_width

        # 2. Read data
        img = await self._read(indexes=indexes, nodata=nodata)
        if expression:
            img = img.apply_expression(expression)

        # 3. Reproject if needed
        if dst_crs and dst_crs != self.crs:
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

    async def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.
            nodata: (int or float, optional): Overwrite dataset internal nodata value. Defaults to `None`.

        Returns:
            PointData: Pixel value per bands/assets.

        """
        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

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
            row_slice=slice(y, y + 1),
            col_slice=slice(x, x + 1),
            indexes=indexes,
            nodata=nodata,
        )

        pt = PointData(
            img.array[:, 0, 0],
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
        indexes: Indexes | None = None,
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
            indexes (sequence of int or int, optional): Band indexes.
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
            indexes=indexes,
            expression=expression,
            max_size=max_size,
            height=height,
            width=width,
            nodata=nodata,
            reproject_method=reproject_method,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
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

    async def _read(
        self,
        indexes: Sequence[int] | None = None,
        row_slice: slice | None = None,
        col_slice: slice | None = None,
        nodata: NoData | None = None,
    ) -> ImageData:
        """Read data from zarr AsyncArray.

        Args:
            indexes: Band indexes (1-based). If None, reads all bands.
            row_slice: Row slice for windowed read.
            col_slice: Column slice for windowed read.
            nodata (int or float, optional): Overwrite dataset internal nodata value.

        Returns:
            ImageData: Image data with mask and spatial info.

        """
        row_slice = row_slice or slice(0, self.height)
        col_slice = col_slice or slice(0, self.width)

        if len(self.input.shape) == 2:
            # 2D array: (height, width)
            selection = (row_slice, col_slice)
            if indexes is None:
                indexes = [1]  # Single band

            # Calculate array size in bytes
            read_height = row_slice.stop - row_slice.start
            read_width = col_slice.stop - col_slice.start
            nbytes = len(indexes) * read_height * read_width * self.input.dtype.itemsize
            if nbytes > MAX_ARRAY_SIZE:
                raise MaxArraySizeError(
                    f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {(len(indexes), read_height, read_width)} in memory."
                )

            data = await self.input.getitem(selection)

            # Ensure 3D shape (bands, height, width)
            data = numpy.expand_dims(data, axis=0)  # type: ignore[assignment]

        else:
            # 3D array: (bands, height, width)
            if indexes is None:
                indexes = list(range(1, self.nbands + 1))

            # Calculate array size in bytes
            read_height = row_slice.stop - row_slice.start
            read_width = col_slice.stop - col_slice.start
            nbytes = len(indexes) * read_height * read_width * self.input.dtype.itemsize
            if nbytes > MAX_ARRAY_SIZE:
                raise MaxArraySizeError(
                    f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {(len(indexes), read_height, read_width)} in memory."
                )

            band_indices = [ix - 1 for ix in indexes]

            data = await self.input.get_orthogonal_selection(
                (band_indices, row_slice, col_slice),  # type: ignore[arg-type]
            )

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
        read_height = row_slice.stop - row_slice.start
        read_width = col_slice.stop - col_slice.start
        read_transform = self.transform * Affine.translation(
            col_slice.start, row_slice.start
        )
        read_bounds = array_bounds(read_height, read_width, read_transform)

        bdescr = self.band_descriptions
        band_descriptions = [bdescr[ix - 1] for ix in indexes]

        return ImageData(
            masked_data,
            bounds=read_bounds,
            crs=self.crs,
            band_names=[f"b{idx}" for idx in indexes],
            band_descriptions=band_descriptions,
            nodata=nodata,
        )
