"""rio_tiler.experimental.rasterio: rio-tiler reader built on top of rasterio, without WarpedVRT.

This reader mirrors the logic of `rio_tiler.io.geotiff.Reader` (async-geotiff):

1. Select the overview level matching the output resolution (GDAL's rule, `rio_tiler._warp.get_overview_level`)
2. Read the native (overview) pixels for the requested window, in the dataset CRS
3. Reproject/resample the result using `rio_tiler._warp.warp`

Instead of relying on GDAL's WarpedVRT to do everything in one pass.

"""

from __future__ import annotations

import math
import warnings
from collections.abc import Sequence
from typing import Any, cast

import attr
import numpy
from affine import Affine
from morecantile import Tile
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import ColorInterp, Resampling
from rasterio.transform import rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds
from rasterio.windows import Window
from rasterio.windows import bounds as window_bounds
from rasterio.windows import from_bounds as window_from_bounds

from rio_tiler._warp import get_downsampling_factor, get_overview_level, warp
from rio_tiler.constants import WGS84_CRS
from rio_tiler.errors import (
    ExpressionMixingWarning,
    InvalidBufferSize,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.expression import parse_expression
from rio_tiler.io.rasterio import Reader as RasterioReader
from rio_tiler.models import BandStatistics, ImageData, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import (
    cast_to_sequence,
    estimate_output,
    non_alpha_indexes,
    output_size,
)


@attr.s
class Reader(RasterioReader):
    """Rio-tiler Experimental Reader for rasterio datasets.

    Dataset opening (incl. GCPS), `info` and `feature` are inherited from
    `rio_tiler.io.rasterio.Reader`. All data access methods (`read`, `tile`, `part`,
    `preview`, `point`, `statistics`) are re-implemented to follow the
    `rio_tiler.io.geotiff.Reader` logic (no `rio_tiler.reader` / WarpedVRT).

    Note: Only `nodata` and `unscale` are taken from `options`. Other low-level
    reader options (e.g `padding`, `vrt_options`) are not supported and will be ignored
    (with a warning).

    """

    transform: Affine = attr.ib(init=False)
    height: int = attr.ib(init=False)
    width: int = attr.ib(init=False)

    @staticmethod
    def _warn_unsupported(kwargs: dict[str, Any]) -> None:
        """Warn about options not supported by this reader."""
        if ignored := sorted(k for k, v in kwargs.items() if v is not None):
            warnings.warn(
                f"Unsupported options will be ignored: {', '.join(ignored)}",
                UserWarning,
            )

    def _get_decimation(
        self,
        desired_factor: float,
        resampling_method: RIOResampling = "nearest",
    ) -> int:
        """Return the overview decimation factor (1 = full resolution) for a downsampling factor.

        `desired_factor` is the number of full resolution pixels for one output pixel
        (see `rio_tiler._warp.get_downsampling_factor`). The overview is selected
        with GDAL's rule (see `rio_tiler._warp.get_overview_level`).

        """
        decimations = self.dataset.overviews(1)
        level = get_overview_level(
            [
                # Real downsampling factor of the overview (e.g 2658 / 167 = 15.92 for decim=16)
                min(
                    self.width / math.ceil(self.width / decim),
                    self.height / math.ceil(self.height / decim),
                )
                for decim in decimations
            ],
            desired_factor,
            resampling_method,
        )
        return decimations[level - 1] if level else 1

    def statistics(
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
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        data = self.preview(
            max_size=max_size,
            indexes=indexes,
            expression=expression,
            **kwargs,
        )

        return data.statistics(
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
        indexes: Indexes | None = None,
        expression: str | None = None,
        buffer: float | None = None,
        nodata: NoData | None = None,
        unscale: bool | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output image size.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            buffer (float, optional): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            unscale (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value. Defaults to `False`.
            resampling_method (str, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (str, optional): GDAL Resampling method to use when reprojecting. Defaults to "nearest".
            kwargs (optional): Options to forward to the `Reader.part` method.

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
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            indexes=indexes,
            expression=expression,
            buffer=buffer,
            nodata=nodata,
            unscale=unscale,
            resampling_method=resampling_method,
            reproject_method=reproject_method,
            **kwargs,
        )

    def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: Any | None = None,
        bounds_crs: Any = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        buffer: float | None = None,
        nodata: NoData | None = None,
        unscale: bool | None = None,
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
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            buffer (float, optional): Buffer on each side of the given aoi. It must be a multiple of `0.5`. Output **image size** will be expanded to `output imagesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            unscale (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value. Defaults to `False`.
            resampling_method (str, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (str, optional): GDAL Resampling method to use when reprojecting. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        self._warn_unsupported(kwargs)

        if buffer and buffer % 0.5:
            raise InvalidBufferSize(
                "`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
            )

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        bounds_crs = CRS.from_user_input(bounds_crs)
        dst_crs = CRS.from_user_input(dst_crs) if dst_crs else bounds_crs

        # 1. Transform output bbox from bounds_crs → output_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 2. Estimate output shape and bounds (in dataset CRS)
        height, width, src_bounds = estimate_output(
            dataset_crs=self.crs,
            dataset_transform=self.transform,
            output_bounds=bbox,
            output_crs=dst_crs,
            output_height=height,
            output_width=width,
            max_size=max_size,
        )

        # Apply buffer: expand output bounds by `buffer` output pixels on each side
        if buffer:
            x_res = (bbox[2] - bbox[0]) / width
            y_res = (bbox[3] - bbox[1]) / height
            bbox = (
                bbox[0] - x_res * buffer,
                bbox[1] - y_res * buffer,
                bbox[2] + x_res * buffer,
                bbox[3] + y_res * buffer,
            )
            height += int(buffer * 2)
            width += int(buffer * 2)
            src_bounds = (
                transform_bounds(dst_crs, self.crs, *bbox, densify_pts=21)
                if dst_crs != self.crs
                else bbox
            )

        # 3. Select overview level based on the output resolution
        decim = self._get_decimation(
            get_downsampling_factor(
                output_bounds=bbox,
                output_crs=dst_crs,
                output_width=width,
                output_height=height,
                dataset_crs=self.crs,
                dataset_transform=self.transform,
                dataset_width=self.width,
                dataset_height=self.height,
                dataset_bounds=self.bounds,
            ),
            resampling_method,
        )

        # Overview shape
        ovr_width = math.ceil(self.width / decim)
        ovr_height = math.ceil(self.height / decim)

        # Overview pixel size, in full resolution pixels.
        # NOTE: Like GDAL, we consider that the overview covers the full dataset
        # extent, so the ratio isn't exactly `decim` when the dataset size isn't a
        # multiple of `decim` (e.g 2658 / 167 = 15.92 for decim=16).
        x_ratio = self.width / ovr_width
        y_ratio = self.height / ovr_height

        # 4. Build pixel window (in overview pixel space) from bounds in dataset CRS
        window = window_from_bounds(*src_bounds, transform=self.transform)
        col_off = math.floor(window.col_off / x_ratio)
        row_off = math.floor(window.row_off / y_ratio)
        win_width = math.ceil(window.width / x_ratio) + 1
        win_height = math.ceil(window.height / y_ratio) + 1

        # 5. Validate window intersection
        # TODO: add `minimum_overlap` like in reader.part method
        col_end = min(ovr_width, math.ceil((window.col_off + window.width) / x_ratio))
        row_end = min(ovr_height, math.ceil((window.row_off + window.height) / y_ratio))
        if max(col_off, 0) >= col_end or max(row_off, 0) >= row_end:
            raise ValueError("Input BBOX and dataset's bounds do not intersect")

        # 6. Clamp window to overview bounds
        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(ovr_width, col_off + win_width)
        clipped_row_stop = min(ovr_height, row_off + win_height)

        # 7. Read the dataset at overview resolution
        # NOTE: rasterio can't open an overview as a dataset, so we read the full
        # resolution window (aligned with the overview pixels, so possibly with
        # fractional offsets) with an `out_shape` matching the overview resolution,
        # which makes GDAL fetch the data directly from the overview.
        img = self._read(
            indexes=indexes,
            window=Window(
                col_off=clipped_col_off * x_ratio,
                row_off=clipped_row_off * y_ratio,
                width=(clipped_col_stop - clipped_col_off) * x_ratio,
                height=(clipped_row_stop - clipped_row_off) * y_ratio,
            ),
            out_shape=(
                clipped_row_stop - clipped_row_off,
                clipped_col_stop - clipped_col_off,
            ),
            nodata=nodata,
            unscale=unscale,
        )

        # 8. Reproject/resample using rasterio.warp.reproject
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
        indexes: Indexes | None = None,
        expression: str | None = None,
        max_size: int = 1024,
        height: int | None = None,
        width: int | None = None,
        dst_crs: Any | None = None,
        nodata: NoData | None = None,
        unscale: bool | None = None,
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
            unscale (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value. Defaults to `False`.
            resampling_method (str, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (str, optional): GDAL Resampling method to use when reprojecting. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        self._warn_unsupported(kwargs)

        dst_crs = CRS.from_user_input(dst_crs) if dst_crs else self.crs

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width: int = self.width
        dst_height: int = self.height
        if dst_crs != self.crs:
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

        # 2-3. Select Overview level
        # NOTE: `dst_width/dst_height` is the dataset size in the output CRS, at the
        # dataset resolution (the WarpedVRT size in rio_tiler.io.Reader)
        decim = self._get_decimation(
            min(dst_width / width, dst_height / height),
            resampling_method,
        )

        # 4. Read data at overview resolution
        img = self._read(
            indexes=indexes,
            out_shape=(
                math.ceil(self.height / decim),
                math.ceil(self.width / decim),
            ),
            nodata=nodata,
            unscale=unscale,
        )
        if expression:
            img = img.apply_expression(expression)

        # 5. Reproject if needed
        if dst_crs != self.crs:
            img = img.reproject(dst_crs=dst_crs, reproject_method=reproject_method)

        # 6. Resize
        if width != img.width or height != img.height:
            img = img.resize(
                width=width, height=height, resampling_method=resampling_method
            )

        return img

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: Any = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        out_dtype: str | numpy.dtype | None = None,
        resampling_method: RIOResampling = "nearest",
        interpolate: bool = False,
        unscale: bool | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            out_dtype (str or numpy.dtype, optional): Output data type.
            resampling_method (str, optional): Resampling method to use. Defaults to "nearest".
            interpolate (bool, optional): Interpolate the value if needed. Defaults to `False`.
            unscale: (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value. Defaults to `False`.

        Returns:
            PointData: Pixel value per bands/assets.

        """
        self._warn_unsupported(kwargs)

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

        if interpolate:
            # Ref: https://github.com/cogeotiff/rio-tiler/issues/793
            # https://github.com/OSGeo/gdal/blob/a3d68b069e6b3676ba437faca5dca6ae2076ce24/swig/python/gdal-utils/osgeo_utils/samples/gdallocationinfo.py#L185-L197
            rows, cols = rowcol(self.transform, xs=[lon], ys=[lat], op=lambda x: x)
            row, col = float(rows[0]), float(cols[0])
            # Clamp the 1x1 window inside the dataset (points within half a pixel of the edges)
            row_off = min(max(row - 0.5, 0.0), self.height - 1.0)
            col_off = min(max(col - 0.5, 0.0), self.width - 1.0)

        else:
            if resampling_method != "nearest":
                warnings.warn(
                    f"{resampling_method} resampling will be ignored when `interpolate=False`.",
                    UserWarning,
                )

            row, col = self.dataset.index(lon, lat)
            row_off, col_off = row, col

        img = self._read(
            indexes=indexes,
            window=Window(
                col_off=col_off,
                row_off=row_off,
                width=1,
                height=1,
            ),
            nodata=nodata,
            out_dtype=out_dtype,
            resampling_method=resampling_method,
            unscale=unscale,
        )

        pt = PointData(
            img.array[:, 0, 0],
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            coordinates=coordinates,
            crs=coord_crs,
            pixel_location=(col, row),
            nodata=img.nodata,
            metadata=img.metadata,
            assets=img.assets,
        )
        if expression:
            pt = pt.apply_expression(expression)

        return pt

    def read(
        self,
        indexes: Indexes | None = None,
        expression: str | None = None,
        nodata: NoData | None = None,
        unscale: bool | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read the full Dataset at native resolution, in the dataset CRS.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            unscale (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value. Defaults to `False`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        self._warn_unsupported(kwargs)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        img = self._read(
            indexes=indexes,
            nodata=nodata,
            unscale=unscale,
        )
        if expression:
            img = img.apply_expression(expression)

        return img

    def _read(  # noqa: C901
        self,
        indexes: Sequence[int] | None = None,
        window: Window | None = None,
        out_shape: tuple[int, int] | None = None,
        nodata: NoData | None = None,
        unscale: bool | None = None,
        out_dtype: str | numpy.dtype | None = None,
        resampling_method: RIOResampling = "nearest",
    ) -> ImageData:
        """Read data from the dataset (no reprojection).

        Args:
            indexes (sequence of int, optional): Band indexes.
            window (rasterio.windows.Window, optional): Window to read, in full resolution pixel space.
            out_shape (tuple of int, optional): Output (height, width). Used to read from overviews.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            unscale (bool, optional): Apply dataset's 'scales' and 'offsets' on output data value.
            out_dtype (str or numpy.dtype, optional): Output data type.
            resampling_method (str, optional): Resampling method to use. Defaults to "nearest".

        """
        io_resampling = Resampling[resampling_method]

        if nodata is None:
            nodata = self.options.get("nodata", self.dataset.nodata)

        if unscale is None:
            unscale = self.options.get("unscale", False)

        if not indexes:
            indexes = non_alpha_indexes(self.dataset)

        if out_shape is None:
            out_shape = (
                (int(window.height), int(window.width))
                if window
                else (self.dataset.height, self.dataset.width)
            )

        height, width = out_shape

        alpha_mask: numpy.ndarray | None = None
        if ColorInterp.alpha in self.dataset.colorinterp and nodata is None:
            alpha_idx = self.dataset.colorinterp.index(ColorInterp.alpha) + 1

            # NOTE: the alpha band is always read in its native dtype (not `out_dtype`)
            # so the `opaque` value stays valid.
            # Read Data and Mask separately
            # Special case (see https://github.com/rasterio/rasterio/issues/2798)
            if self.dataset.dtypes[alpha_idx - 1] != self.dataset.dtypes[indexes[0] - 1]:
                values = self.dataset.read(
                    indexes=indexes,
                    window=window,
                    out_shape=(len(indexes), height, width),
                    resampling=io_resampling,
                    out_dtype=out_dtype,
                )
                alpha_mask = self.dataset.read(
                    indexes=alpha_idx,
                    window=window,
                    out_shape=(height, width),
                    resampling=io_resampling,
                )
            else:
                idx = tuple(indexes) + (alpha_idx,)
                values = self.dataset.read(
                    indexes=idx,
                    window=window,
                    out_shape=(len(idx), height, width),
                    resampling=io_resampling,
                )
                values, alpha_mask = values[:-1], values[-1]
                if out_dtype is not None:
                    values = values.astype(out_dtype, casting="unsafe")

            data = numpy.ma.MaskedArray(values)

            _, opaque = dtype_ranges[str(alpha_mask.dtype)]
            data.mask = alpha_mask != opaque

            # ImageData requires the alpha band to share the data dtype
            alpha_mask = alpha_mask.astype(values.dtype, casting="unsafe")

        else:
            if nodata is not None:
                # When the mask only comes from the nodata value, we don't read the
                # dataset mask but re-create it from the data.
                # With `masked=True` or `fill_value`, rasterio reads the masks band by
                # band, which on a WarpedVRT (e.g. datasets with GCPS) skips GDAL's
                # output-size warp and is very slow at low zoom.
                # ref: https://github.com/cogeotiff/rio-tiler/pull/1074
                values = self.dataset.read(
                    indexes=indexes,
                    window=window,
                    out_shape=(len(indexes), height, width),
                    resampling=io_resampling,
                    out_dtype=out_dtype,
                )
                mask = numpy.isnan(values) if numpy.isnan(nodata) else values == nodata
                data = numpy.ma.MaskedArray(values, mask=mask)

            else:
                # NOTE: `masked=True` uses GDAL mask flags (internal mask band or all valid)
                data = self.dataset.read(
                    indexes=indexes,
                    window=window,
                    out_shape=(len(indexes), height, width),
                    resampling=io_resampling,
                    masked=True,
                    out_dtype=out_dtype,
                )

        # Get dataset statistics
        stats = []
        for ix in indexes:
            tags = self.dataset.tags(ix)
            if all(stat in tags for stat in ["STATISTICS_MINIMUM", "STATISTICS_MAXIMUM"]):
                stats.append(
                    (
                        float(tags["STATISTICS_MINIMUM"]),
                        float(tags["STATISTICS_MAXIMUM"]),
                    )
                )

        # We only add dataset statistics if we have them for all the indexes
        dataset_statistics = stats if len(stats) == len(indexes) else None

        # Handle Scale/Offset
        if unscale:
            scales = numpy.array(self.dataset.scales)[numpy.array(indexes) - 1]
            offsets = numpy.array(self.dataset.offsets)[numpy.array(indexes) - 1]
            data = cast(numpy.ma.MaskedArray, data.astype("float32", casting="unsafe"))

            numpy.multiply(data, scales.reshape((-1, 1, 1)), out=data, casting="unsafe")
            numpy.add(data, offsets.reshape((-1, 1, 1)), out=data, casting="unsafe")

            if dataset_statistics:
                stats_array = numpy.array(dataset_statistics)
                numpy.multiply(
                    stats_array,
                    scales.reshape((-1, 1)),
                    out=stats_array,
                    casting="unsafe",
                )
                numpy.add(
                    stats_array,
                    offsets.reshape((-1, 1)),
                    out=stats_array,
                    casting="unsafe",
                )
                dataset_statistics = [tuple(s) for s in stats_array.tolist()]

        return ImageData(
            data,
            bounds=window_bounds(window, self.transform) if window else self.bounds,
            crs=self.crs,
            band_names=[f"b{ix}" for ix in indexes],
            band_descriptions=[
                self.dataset.descriptions[ix - 1] or f"b{ix}" for ix in indexes
            ],
            dataset_statistics=dataset_statistics,
            metadata=self.dataset.tags(),
            nodata=nodata,
            alpha_mask=alpha_mask,
            assets=[self.input] if self.input else None,
        )
