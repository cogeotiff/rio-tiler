"""rio_tiler.experimental.zarr reader: rio-tiler Async reader built on top of zarr-python."""

from __future__ import annotations

import asyncio
import math
import warnings
from collections.abc import Sequence
from typing import Any, Literal, TypedDict, cast

import attr
import numpy
import zarr
from affine import Affine
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.errors import NotGeoreferencedWarning
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


def _has_multiscales(conventions: list[dict]) -> bool:
    return next(
        (
            True
            for c in conventions
            if c["uuid"] == "d35379db-88df-4056-af3a-620245f8e347"
        ),
        False,
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
    def minzoom(self):
        """Return dataset minzoom.

        NOTE: because a zarr.Array doesn't have overviews, minzoom is the same as maxzoom.
        """
        return self._maxzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self._maxzoom

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

    array: zarr.AsyncArray
    crs: CRS
    height: int
    width: int
    transform: Affine


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

    elif _missing_size(output_width, output_height):
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


@attr.s
class GeoZarrReader(AsyncBaseReader):
    """Rio-tiler GeoZarr Reader.

    A pure zarr-python async reader that accepts a zarr AsyncGroup (GeoZarr)

    Attributes:
        input: zarr AsyncGroup
        tms: TileMatrixSet for tile operations.
        colormap: Optional colormap dictionary.

    """

    input: zarr.AsyncGroup = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    crs: CRS = attr.ib(init=False)
    transform: Affine = attr.ib(init=False)

    # Group shape
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    # Group bounds (calculated from shape + transform)
    bounds: BBox = attr.ib(init=False)

    multiscales: bool = attr.ib(init=False)

    colormap: dict | None = attr.ib(default=None)

    # list of availables arrays in the group
    _variables: dict[str, list[ArrayMetadata]] = attr.ib(init=False, default=None)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def __attrs_post_init__(self) -> None:
        """Post init: derive height, width, count from array shape."""
        spatial_dims = ["y", "x", "latitude", "longitude", "lat", "lon"]
        spatial_shape: tuple[int, int] | None = None
        transform: Affine | None = None

        # NOTE: zarr-python says attrs is of type dict[str, JSON]
        attributes = cast(dict[str, Any], self.input.attrs)
        conventions: list[dict] = attributes.get("zarr_conventions", [])

        self.multiscales = _has_multiscales(conventions)
        # assert self.multiscales, "GeoZarr convention requires 'multiscales' convention to be present in zarr_conventions"

        self.spatial = _has_spatial(conventions)
        assert self.spatial, (
            "GeoZarr convention requires 'spatial' convention to be present in zarr_conventions"
        )

        self.proj = _has_proj(conventions)
        assert self.proj, (
            "GeoZarr convention requires 'geo-proj' convention to be present in zarr_conventions"
        )

        # CRS
        self.crs = _get_proj_crs(attributes)

        # NOTE: `spatial:dimensions` is the only required attribute for the `spatial` convention
        # but if this ever change we default to list of common spatial dimension names
        spatial_dims = attributes.get("spatial:dimensions", spatial_dims)
        spatial_shape = attributes.get("spatial:shape")

        # Transform
        # Case 1: Transform at group level
        tr = attributes.get("spatial:transform")
        transform_type = attributes.get("spatial:transform_type", "affine")
        if transform_type == "affine" and tr is not None:
            if attributes.get("spatial:registration", "pixel") == "node":
                # NOTE: If the registration is "node", we need to adjust the transform to
                # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                tr[2] -= tr[0] / 2
                tr[5] -= tr[4] / 2

            transform = Affine(*tr)

        # Case 2: No transform at group level, check multiscales for transform and shape
        if not transform and self.multiscales:
            # assume the first layout is the highest resolution
            first_res = attributes["multiscales"]["layout"][0]
            spatial_shape = first_res.get("spatial:shape")

            tr = first_res.get("spatial:transform")
            transform_type = attributes.get("spatial:transform_type", "affine")
            if transform_type == "affine" and tr is not None:
                if attributes.get("spatial:registration", "pixel") == "node":
                    # NOTE: If the registration is "node", we need to adjust the transform to
                    # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                    tr[2] -= tr[0] / 2
                    tr[5] -= tr[4] / 2

                transform = Affine(*tr)

        assert transform, (
            "spatial:transform is required either at group level or in the first layout of multiscales convention"
        )
        self.transform = transform

        # NOTE: we could potentially check for spatial:bbox and derive shape from it
        assert spatial_shape, (
            "spatial:shape is required either at group level or in the first layout of multiscales convention"
        )
        self.height = spatial_shape[0]
        self.width = spatial_shape[1]

        self.bounds = array_bounds(self.height, self.width, self.transform)

    @property
    def minzoom(self):
        """Return dataset minzoom."""
        if self.multiscales:
            attributes = cast(dict[str, Any], self.input.attrs)
            # assume the last layout is the lowest resolution
            last_res = attributes["multiscales"]["layout"][-1]
            shape = last_res.get("spatial:shape")
            transform = last_res.get("spatial:transform")
            if all([transform, shape]):
                return _get_zoom(
                    tms=self.tms,
                    crs=self.crs,
                    width=shape[1],
                    height=shape[0],
                    bounds=array_bounds(shape[0], shape[1], Affine(*transform)),
                )

        return self.maxzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        if self.multiscales:
            attributes = cast(dict[str, Any], self.input.attrs)
            # assume the last layout is the highest resolution
            first_res = attributes["multiscales"]["layout"][0]
            shape = first_res.get("spatial:shape")
            transform = first_res.get("spatial:transform")
            if all([transform, shape]):
                return _get_zoom(
                    tms=self.tms,
                    crs=self.crs,
                    width=shape[1],
                    height=shape[0],
                    bounds=array_bounds(shape[0], shape[1], Affine(*transform)),
                )

        return self._maxzoom

    @property
    async def variables(self) -> dict[str, list[ArrayMetadata]]:  # noqa: C901
        """Return list of variables (arrays) with their geospatial metadata."""
        if self._variables:
            return self._variables

        variables: dict[str, list[ArrayMetadata]] = {}
        if self.multiscales:
            attributes = cast(dict[str, Any], self.input.attrs)
            conventions: list[dict] = attributes.get("zarr_conventions", [])

            crs = _get_proj_crs(attributes) if _has_proj(conventions) else self.crs

            # 1. Get MS groups + geospatial metadata (crs, transform)
            ms_group: dict[str, dict[str, Any]] = {}
            for layout in attributes["multiscales"]["layout"]:
                transform_type = layout.get("spatial:transform_type") or "affine"
                tr = layout.get("spatial:transform")
                if transform_type == "affine" and tr is not None:
                    if layout.get("spatial:registration", "pixel") == "node":
                        # NOTE: If the registration is "node", we need to adjust the transform to
                        # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                        tr[2] -= tr[0] / 2
                        tr[5] -= tr[4] / 2

                ms_group[layout["asset"]] = {
                    "crs": crs,
                    "transform": tr,
                }

            # 2. list all arrays for each layout
            for group_name, meta in ms_group.items():
                group = await self.input.getitem(group_name)

                # NOTE: `ms_group` reference group names so we know `getitem` return a group
                group = cast(zarr.AsyncGroup, group)
                async for array in group.array_values():
                    # NOTE: skip non-data arrays
                    # TODO: be smarter
                    if array.ndim < 2:
                        continue

                    attributes = cast(dict[str, Any], array.attrs)
                    variable_name = array.name.replace(f"/{group_name}/", "")
                    if variable_name not in variables:
                        variables[variable_name] = []

                    transform = attributes.get("spatial:transform")
                    transform_type = attributes.get("spatial:transform_type") or "affine"
                    if transform_type == "affine" and transform is not None:
                        if attributes.get("spatial:registration", "pixel") == "node":
                            # NOTE: If the registration is "node", we need to adjust the transform to
                            # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                            transform[2] -= transform[0] / 2
                            transform[5] -= transform[4] / 2

                    transform = transform or meta["transform"]
                    assert transform, (
                        f"`spatial:transform` missing for multiscales layout {group_name} (path: '{array.name}')"
                    )

                    # TODO: is this always true
                    height, width = array.shape[-2:]

                    variables[variable_name].append(
                        {
                            "array": array,
                            "crs": meta["crs"],
                            "height": height,
                            "width": width,
                            "transform": Affine(*transform),
                        }
                    )

        else:
            async for array in self.input.array_values():
                group_name = self.input.name

                # NOTE: skip non-data arrays
                # TODO: be smarter
                if array.ndim < 2:
                    continue

                attributes = cast(dict[str, Any], array.attrs)
                variable_name = array.name.replace(f"/{group_name}/", "")

                transform = attributes.get("spatial:transform")
                transform_type = attributes.get("spatial:transform_type") or "affine"
                if transform_type == "affine" and transform is not None:
                    if attributes.get("spatial:registration", "pixel") == "node":
                        # NOTE: If the registration is "node", we need to adjust the transform to
                        # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                        transform[2] -= transform[0] / 2
                        transform[5] -= transform[4] / 2

                transform = transform or self.transform
                assert transform, (
                    f"`spatial:transform` missing for array {variable_name} (path: '{array.name}')"
                )

                # TODO: is this always true
                height, width = array.shape[-2:]

                variables[variable_name] = [
                    {
                        "array": array,
                        "crs": self.crs,
                        "height": height,
                        "width": width,
                        "transform": Affine(*transform),
                    }
                ]

        if not variables:
            raise ValueError("No variables (data arrays) found in the dataset.")

        self._variables = variables

        return self._variables

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

    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tile.models.Info: Dataset info.

        """
        raise NotImplementedError

    async def statistics(
        self,
        *,
        variables: Sequence[str] | str | None = None,
        expression: str | None = None,
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
        availables_variables = await self.variables

        variables = variables or list(availables_variables.keys())

        variables = cast_to_sequence(variables)
        if vars := set(variables).difference(availables_variables.keys()):
            raise ValueError(
                f"Variables {vars} not found in the dataset. Available variables: {list(availables_variables.keys())}"
            )

        img = await self.preview(
            variables=variables,
            expression=expression,
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

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        availables_variables = await self.variables

        variables = cast_to_sequence(variables)
        if vars := set(variables).difference(availables_variables.keys()):
            raise ValueError(
                f"Variables {vars} not found in the dataset. Available variables: {list(availables_variables.keys())}"
            )

        async def _part(variable: str) -> ImageData:
            array_metadata = self.select_variable(
                availables_variables[variable],
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )

            async with Reader(
                input=array_metadata["array"],
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                tms=self.tms,
            ) as src:
                return await src.part(
                    bbox,
                    dst_crs=dst_crs,
                    bounds_crs=bounds_crs,
                    max_size=max_size,
                    height=height,
                    width=width,
                    nodata=nodata,
                    reproject_method=reproject_method,
                )

        img_stack = await asyncio.gather(*(_part(variable) for variable in variables))

        img = ImageData.create_from_list(img_stack)
        img.band_names = [f"b{ix + 1}" for ix in range(img.count)]
        if expression:
            return img.apply_expression(expression)

        return img

    async def preview(  # type: ignore[override]
        self,
        *,
        variables: Sequence[str] | str,
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

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        availables_variables = await self.variables

        variables = cast_to_sequence(variables)
        if vars := set(variables).difference(availables_variables.keys()):
            raise ValueError(
                f"Variables {vars} not found in the dataset. Available variables: {list(availables_variables.keys())}"
            )

        async def _preview(variable: str) -> ImageData:
            array_metadata = self.select_variable(
                availables_variables[variable],
                max_size=max_size,
                height=height,
                width=width,
                dst_crs=dst_crs,
            )

            async with Reader(
                input=array_metadata["array"],
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                tms=self.tms,
            ) as src:
                return await src.preview(
                    max_size=max_size,
                    height=height,
                    width=width,
                    dst_crs=dst_crs,
                    nodata=nodata,
                    resampling_method=resampling_method,
                    reproject_method=reproject_method,
                    **kwargs,
                )

        img_stack = await asyncio.gather(*(_preview(variable) for variable in variables))

        img = ImageData.create_from_list(img_stack)
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
        availables_variables = await self.variables

        variables = cast_to_sequence(variables)
        if vars := set(variables).difference(availables_variables.keys()):
            raise ValueError(
                f"Variables {vars} not found in the dataset. Available variables: {list(availables_variables.keys())}"
            )

        async def _point(variable: str) -> PointData:
            array_metadata = self.select_variable(availables_variables[variable])
            async with Reader(
                input=array_metadata["array"],
                transform=array_metadata["transform"],
                crs=array_metadata["crs"],
                tms=self.tms,
            ) as src:
                return await src.point(
                    lon,
                    lat,
                    coord_crs=coord_crs,
                    nodata=nodata,
                )

        point_stack = await asyncio.gather(*(_point(variable) for variable in variables))

        pt = PointData.create_from_list(point_stack)
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
        availables_variables = await self.variables

        variables = cast_to_sequence(variables)
        if vars := set(variables).difference(availables_variables.keys()):
            raise ValueError(
                f"Variables {vars} not found in the dataset. Available variables: {list(availables_variables.keys())}"
            )

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
