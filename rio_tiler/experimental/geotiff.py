"""rio_tiler.experimental.geotiff reader: rio-tiler Async reader built on top of async-geotiff."""

from __future__ import annotations

import math
import warnings
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, cast

import attr
import numpy
from async_geotiff import Window
from async_geotiff.enums import ColorInterp
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.transform import array_bounds, from_bounds
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds, transform_geom
from rasterio.windows import from_bounds as window_from_bounds

from rio_tiler._warp import warp
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    ExpressionMixingWarning,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.expression import parse_expression
from rio_tiler.io import AsyncBaseReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes, RIOResampling, WarpResampling
from rio_tiler.utils import (
    CRS_to_uri,
    _get_width_height,
    _missing_size,
    _validate_shape_input,
    cast_to_sequence,
)

if TYPE_CHECKING:
    from async_geotiff import GeoTIFF, Overview


@attr.s
class Reader(AsyncBaseReader):
    """Rio-tiler.io GeoTIFFReader."""

    input: GeoTIFF = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    colormap: dict | None = attr.ib(default=None)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def __attrs_post_init__(self):
        """Post init."""
        self.bounds = self.input.bounds
        self.crs = CRS.from_user_input(self.input.crs)

        self.transform = self.input.transform
        self.height = self.input.height
        self.width = self.input.width

        if self.colormap is None and self.input.colormap is not None:
            self.colormap = self.input.colormap.as_rasterio()

    @property
    def minzoom(self):
        """Return dataset minzoom."""
        return self._minzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self._maxzoom

    def _get_overview_level(
        self,
        target_res: float,
        zoom_level_strategy: Literal["AUTO", "LOWER", "UPPER"] = "AUTO",
    ) -> int:
        """Return the overview level corresponding to the resolution."""
        src_res = max(abs(self.input.transform.a), abs(self.input.transform.e))

        available_resolutions = [src_res] + [
            min(abs(ovr.transform.a), abs(ovr.transform.e))
            for ovr in self.input.overviews
        ]

        # Based on aiocogeo:
        # https://github.com/geospatial-jeff/aiocogeo/blob/5a1d32c3f22c883354804168a87abb0a2ea1c328/aiocogeo/partial_reads.py#L113-L147
        percentage = {"AUTO": 50, "LOWER": 100, "UPPER": 0}.get(zoom_level_strategy, 50)

        assert 0 <= percentage <= 100
        # Iterate over zoom levels from lowest/coarsest to highest/finest. If the `target_res` is more than `percentage`
        # percent of the way from the zoom level below to the zoom level above, then upsample the zoom level below, else
        # downsample the zoom level above.
        for i in reversed(range(1, len(available_resolutions))):
            res_current = available_resolutions[i]
            res_higher = available_resolutions[i - 1]
            threshold = res_current - (res_current - res_higher) * (percentage / 100.0)
            if target_res > threshold or target_res == res_current:
                return i

        return 0

    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        if self.input.nodata is not None:
            nodata_type = "Nodata"
        elif any(c == ColorInterp.ALPHA for c in self.input.colorinterp):
            nodata_type = "Alpha"
        elif self.input._mask_ifd:
            nodata_type = "Mask"
        else:
            nodata_type = "None"

        overviews = [
            math.ceil(self.input.width / ovr.width) for ovr in self.input.overviews
        ]

        meta: dict[str, Any] = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            # TODO: get we can band metadata from async-geotiff
            "band_metadata": [(f"b{ix + 1}", {}) for ix in range(self.input.count)],
            # TODO: get we can band names from async-geotiff
            "band_descriptions": [
                (f"b{ix + 1}", f"b{ix + 1}") for ix in range(self.input.count)
            ],
            "dtype": self.input.dtype.name,
            "colorinterp": [ix.name for ix in self.input.colorinterp],
            "nodata_type": nodata_type,
            # additional info (not in default model)
            "driver": "GTiff",
            "count": self.input.count,
            "width": self.input.width,
            "height": self.input.height,
            "overviews": overviews,
            "scales": self.input.scales,
            "offsets": self.input.offsets,
        }

        if self.colormap:
            meta.update({"colormap": self.colormap})

        if nodata_type == "Nodata":
            meta.update({"nodata_value": self.input.nodata})

        return Info.model_validate(meta)

    async def statistics(
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        max_size: int = 1024,
        indexes: Indexes | None = None,
        expression: str | None = None,
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
            kwargs (optional): Options to forward to `self._read`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        data = await self.preview(
            max_size=max_size, indexes=indexes, expression=expression, **kwargs
        )

        return data.statistics(
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
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            max_size=None,
            indexes=indexes,
            expression=expression,
            **kwargs,
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
        unscale: bool = False,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system. Defaults to bounds_crs.
            bounds_crs (rasterio.crs.CRS, optional): Coordinate reference system of the input bounds. Defaults to WGS84.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
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

        dst_crs = dst_crs or bounds_crs

        # Transform bbox from bounds_crs → dst_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 1. Estimate `max` output dimensions
        if dst_crs != self.crs:
            # Case 1: Reprojection needed
            # - reproject bbox to dataset CRS
            # - compute native output shape in dataset resolution/CRS
            # - compute output shape in output CRS
            dst_bounds = transform_bounds(dst_crs, self.crs, *bbox, densify_pts=21)
            native_src_w = max(
                1, round((dst_bounds[2] - dst_bounds[0]) / abs(self.input.transform.a))
            )
            native_src_h = max(
                1, round((dst_bounds[3] - dst_bounds[1]) / abs(self.input.transform.e))
            )
            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, native_src_w, native_src_h, *dst_bounds
            )

        else:
            # Case 2: No reprojection needed
            # - keep output dataset bbox as input bbox
            # - compute output shape in dataset resolution/CRS
            dst_bounds = bbox
            dst_width = max(1, round((bbox[2] - bbox[0]) / abs(self.input.transform.a)))
            dst_height = max(1, round((bbox[3] - bbox[1]) / abs(self.input.transform.e)))

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

        # 3. Select IFD based on output resolution in dataset CRS
        if dst_crs != self.crs:
            # Get Transform from output shape and bbox
            transform, _, _ = calculate_default_transform(
                dst_crs, self.crs, width, height, *bbox
            )
        else:
            transform = from_bounds(*bbox, width, height)

        target_res = min(abs(transform.a), abs(transform.e))

        dataset: GeoTIFF | Overview = self.input
        if level := self._get_overview_level(target_res):
            dataset = self.input.overviews[level - 1]

        # 4. Build pixel window, clamped to dataset bounds
        rasterio_win = window_from_bounds(*dst_bounds, transform=dataset.transform)
        row_off = math.floor(rasterio_win.row_off)
        col_off = math.floor(rasterio_win.col_off)
        win_width = math.ceil(rasterio_win.width) + 1
        win_height = math.ceil(rasterio_win.height) + 1

        # TODO: add `minimum_overlap` like in reader.part method
        col_end = min(dataset.width, math.ceil(rasterio_win.col_off + rasterio_win.width))
        row_end = min(
            dataset.height, math.ceil(rasterio_win.row_off + rasterio_win.height)
        )
        if col_off >= col_end or row_off >= row_end:
            raise ValueError("Input BBOX and dataset's bounds do not intersect")

        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(dataset.width, col_off + win_width)
        clipped_row_stop = min(dataset.height, row_off + win_height)
        clipped_width = clipped_col_stop - clipped_col_off
        clipped_height = clipped_row_stop - clipped_row_off

        # 5. Read GeotTIFF/Overview dataset with input window in dataset CRS
        img = await self._read(
            dataset,
            indexes=indexes,
            window=Window(
                col_off=clipped_col_off,
                row_off=clipped_row_off,
                width=clipped_width,
                height=clipped_height,
            ),
            unscale=unscale,
        )

        # 6. Reproject/resample using rasterio.warp.reproject
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
        max_size: int = 1024,
        height: int | None = None,
        width: int | None = None,
        unscale: bool = False,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
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
        dst_width = self.input.width
        dst_height = self.input.height
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

        # 2. determine overview level to read
        # Output dataset `transform` in the output CRS
        if dst_crs and dst_crs != self.crs:
            proj_bbox = transform_bounds(
                self.crs, dst_crs, *self.input.bounds, densify_pts=21
            )
            transform, _, _ = calculate_default_transform(
                dst_crs,
                self.crs,
                width,
                height,
                *proj_bbox,
            )
        else:
            transform = from_bounds(*self.input.bounds, width, height)

        # 3. Select Overview level
        target_res = min(abs(transform.a), abs(transform.e))
        dataset: GeoTIFF | Overview = self.input
        if level := self._get_overview_level(target_res):
            dataset = self.input.overviews[level - 1]

        # 4. Read data
        img = await self._read(dataset, indexes=indexes, unscale=unscale)
        if expression:
            img = img.apply_expression(expression)

        # 5. Reproject if needed
        if dst_crs and dst_crs != self.crs:
            img = img.reproject(
                dst_crs=dst_crs,
                reproject_method=reproject_method,
            )

        # 6. Resize
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
        unscale: bool = False,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.
            unscale: (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.

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

        row, col = self.input.index(lon, lat)
        window = Window(row_off=row, col_off=col, width=1, height=1)
        img = await self._read(
            self.input, indexes=indexes, window=window, unscale=unscale
        )

        pt = PointData(
            img.array[:, 0, 0],
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            coordinates=coordinates,
            crs=coord_crs,
            pixel_location=(col, row),
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
            **kwargs: Any: Additional parameters to pass to `.part()` method.

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
            width=width,
            height=height,
            **kwargs,
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
        dataset: GeoTIFF | Overview,
        indexes: Sequence[int] | None = None,
        window: Window | None = None,
        unscale: bool = False,
    ) -> ImageData:
        """Reader Data from GeoTIFF or Overview."""
        array = await dataset.read(window=window)
        data = array.as_masked()

        if indexes is None:
            indexes = [
                ix
                for ix, c in enumerate(self.input.colorinterp, 1)
                if c != ColorInterp.ALPHA
            ]

        # RGBA datasets
        alpha_mask: numpy.ndarray | None = None
        if ColorInterp.ALPHA in self.input.colorinterp:
            alpha_idx = self.input.colorinterp.index(ColorInterp.ALPHA) + 1
            idx = tuple(indexes) + (alpha_idx,)
            data = data[[ix - 1 for ix in idx]]

            data, alpha_mask = data[:-1], data[-1].data
        else:
            data = data[[ix - 1 for ix in indexes]]

            # if data has Nodata then we simply make sure the mask == the nodata
            if self.input.nodata is not None:
                if numpy.isnan(self.input.nodata):
                    data.mask = numpy.isnan(data.data)
                else:
                    data.mask = data.data == self.input.nodata

        # Handle Scale/Offset
        scales = numpy.array(self.input.scales)[numpy.array(indexes) - 1]
        offsets = numpy.array(self.input.offsets)[numpy.array(indexes) - 1]
        if unscale:
            data = cast(numpy.ma.MaskedArray, data.astype("float32", casting="unsafe"))

            numpy.multiply(data, scales.reshape((-1, 1, 1)), out=data, casting="unsafe")
            numpy.add(data, offsets.reshape((-1, 1, 1)), out=data, casting="unsafe")

            scales = numpy.zeros(len(indexes)) + 1.0
            offsets = numpy.zeros(len(indexes))

        # Get dataset statistics
        stats = []
        if gdal_stats := self.input.stored_stats:
            for ii in indexes:
                if b := gdal_stats.get(ii):
                    if b.min is not None and b.max is not None:
                        stats.append((b.min, b.max))

        # We only add dataset statistics if we have them for all the indexes
        dataset_statistics = stats if len(stats) == len(indexes) else None

        # Create ImageData object
        return ImageData(
            data,
            bounds=array_bounds(array.height, array.width, array.transform),
            crs=CRS.from_user_input(array.crs),
            band_names=[f"b{ix}" for ix in indexes],
            band_descriptions=[f"b{ix}" for ix in indexes],
            dataset_statistics=dataset_statistics,
            nodata=array.nodata,
            alpha_mask=alpha_mask if alpha_mask is not None else None,
            scales=scales.tolist(),
            offsets=offsets.tolist(),
        )
