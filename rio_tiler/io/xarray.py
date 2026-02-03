"""rio_tiler.io.xarray: Xarray Reader."""

from __future__ import annotations

import math
import os
import warnings
from typing import Any, cast

import attr
import numpy
from morecantile import Tile, TileMatrixSet
from rasterio import windows
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.transform import from_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds, transform_geom

from rio_tiler.constants import WEB_MERCATOR_CRS, WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    InvalidGeographicBounds,
    MaxArraySizeError,
    MissingCRS,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.io.base import BaseReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import (
    CRS_to_uri,
    _get_width_height,
    _missing_size,
    _validate_shape_input,
    cast_to_sequence,
    get_array_statistics,
)

try:
    import xarray
except ImportError:  # pragma: nocover
    xarray = None  # type: ignore

try:
    import rioxarray
except ImportError:  # pragma: nocover
    rioxarray = None  # type: ignore


MAX_ARRAY_SIZE = int(os.environ.get("RIO_TILER_MAX_ARRAY_SIZE", 1_000_000_000))  # 1Gb


@attr.s
class XarrayReader(BaseReader):
    """Xarray Reader.

    Attributes:
        dataset (xarray.DataArray): Xarray DataArray dataset.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.

    Examples:
        >>> ds = xarray.open_dataset(
                "https://pangeo.blob.core.windows.net/pangeo-public/daymet-rio-tiler/na-wgs84.zarr",
                engine="zarr",
                decode_coords="all",
                consolidated=True,
            )
            da = ds["tmax"]

            with XarrayReader(da) as dst:
                img = dst.tile(...)

    """

    input: xarray.DataArray = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    _dims: list = attr.ib(init=False, factory=list)

    def __attrs_post_init__(self):
        """Set bounds and CRS."""
        assert xarray is not None, "xarray must be installed to use XarrayReader"
        assert rioxarray is not None, "rioxarray must be installed to use XarrayReader"

        # NOTE: rioxarray returns **ordered** bounds in form of (minx, miny, maxx, maxx)
        self.bounds = tuple(self.input.rio.bounds())
        self.crs = self.input.rio.crs
        if not self.crs:
            raise MissingCRS(
                "Dataset doesn't have CRS information, please add it before using rio-tiler (e.g. `ds.rio.write_crs('epsg:4326', inplace=True)`)"
            )

        # adds half x/y resolution on each values
        # https://github.com/corteva/rioxarray/issues/645#issuecomment-1461070634
        xres, yres = map(abs, self.input.rio.resolution())
        if self.crs == WGS84_CRS and (
            self.bounds[0] + xres / 2 < -180
            or self.bounds[1] + yres / 2 < -90
            or self.bounds[2] - xres / 2 > 180
            or self.bounds[3] - yres / 2 > 90
        ):
            raise InvalidGeographicBounds(
                f"Invalid geographic bounds: {self.bounds}. Must be within (-180, -90, 180, 90)."
            )

        self.transform = self.input.rio.transform()
        self.height = self.input.rio.height
        self.width = self.input.rio.width

        self._dims = [
            d
            for d in self.input.dims
            if d
            not in [
                self.input.rio.x_dim,
                self.input.rio.y_dim,
                "spatial_ref",
                "crs_wkt",
                "grid_mapping",
            ]
        ]
        assert len(self._dims) in [0, 1], "Can't handle >=4D DataArray"

    @property
    def minzoom(self):
        """Return dataset minzoom."""
        return self._minzoom

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
        if not self._dims:
            coords_name = [
                d
                for d in self.input.coords
                if d
                not in [
                    self.input.rio.x_dim,
                    self.input.rio.y_dim,
                    "spatial_ref",
                    "crs_wkt",
                    "grid_mapping",
                ]
            ]
            if coords_name:
                return [str(self.input.coords[coords_name[0]].data)]

            return [self.input.name or "b1"]  # type: ignore

        return [str(band) for d in self._dims for band in self.input[d].values]

    def info(self) -> Info:
        """Return xarray.DataArray info."""
        metadata = [band.attrs for d in self._dims for band in self.input[d]] or [{}]

        meta = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            "band_metadata": [(f"b{ix}", v) for ix, v in enumerate(metadata, 1)],
            "band_descriptions": [
                (f"b{ix}", v or f"b{ix}")
                for ix, v in enumerate(self.band_descriptions, 1)
            ],
            "dtype": str(self.input.dtype),
            "nodata_type": "Nodata" if self.input.rio.nodata is not None else "None",
            "name": self.input.name,
            "count": self.input.rio.count,
            "width": self.input.rio.width,
            "height": self.input.rio.height,
            "dimensions": self.input.dims,
            "attrs": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in self.input.attrs.items()
            },
        }

        return Info(**meta)

    def _sel_indexes(
        self,
        indexes: Indexes | None = None,
    ) -> tuple[xarray.DataArray, list[str]]:
        """Select `band` indexes in DataArray."""
        da = self.input
        band_descriptions = self.band_descriptions

        if indexes := cast_to_sequence(indexes):
            assert all(v > 0 for v in indexes), "Indexes value must be >= 1"
            if da.ndim == 2:
                if set(indexes) != set({1}):
                    raise ValueError(
                        f"Invalid indexes {indexes} for array of shape {da.shape}"
                    )

                return da, band_descriptions

            indexes = [idx - 1 for idx in indexes]

            da = da[indexes]
            band_descriptions = [band_descriptions[idx] for idx in indexes]

        return da, band_descriptions

    def statistics(
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return statistics from a dataset."""
        hist_options = hist_options or {}

        da, band_descriptions = self._sel_indexes(indexes)

        if nodata is not None:
            da = da.rio.write_nodata(nodata)

        data = da.to_masked_array()
        data.mask |= data.data == da.rio.nodata

        stats = get_array_statistics(
            data,
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            **hist_options,
        )

        return {
            f"b{ix +1}": BandStatistics(
                **val,
                description=band_descriptions[ix],
            )
            for ix, val in enumerate(stats)
        }

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int | None = None,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        out_dtype: str | numpy.dtype | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read a Web Map tile from a dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output image size. Defaults to `256`.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            auto_expand (boolean, optional): When True, rioxarray's clip_box will expand clip search if only 1D raster found with clip. When False, will throw `OneDimensionalRaster` error if only 1 x or y data point is found. Defaults to True.
            nodata (int or float, optional): Overwrite dataset internal nodata value.

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
            reproject_method=reproject_method,
            auto_expand=auto_expand,
            nodata=nodata,
            indexes=indexes,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            out_dtype=out_dtype,
            **kwargs,
        )

    def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        resampling_method: RIOResampling = "nearest",
        out_dtype: str | numpy.dtype | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs ("dst_crs").
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            bounds_crs (rasterio.crs.CRS, optional): Bounds Coordinate Reference System. Defaults to `epsg:4326`.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            auto_expand (boolean, optional): When True, rioxarray's clip_box will expand clip search if only 1D raster found with clip. When False, will throw `OneDimensionalRaster` error if only 1 x or y data point is found. Defaults to True.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        dst_crs = dst_crs or bounds_crs

        da, band_descriptions = self._sel_indexes(indexes)

        if nodata is not None:
            da = da.rio.write_nodata(nodata)

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = da.attrs.get("valid_min"), da.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * da.rio.count

        da = da.rio.clip_box(
            *bbox,
            crs=bounds_crs,
            auto_expand=auto_expand,
        )

        if da.nbytes > MAX_ARRAY_SIZE:
            raise MaxArraySizeError(
                f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put DataArray of {da.shape} in memory."
            )

        src_width = da.rio.width
        src_height = da.rio.height
        src_bounds = list(da.rio.bounds())
        src_transform = da.rio.transform()

        # Fix for https://github.com/cogeotiff/rio-tiler/issues/654
        #
        # When using `calculate_default_transform` with dataset
        # which span at high/low latitude outside the area_of_use
        # of the WebMercator projection, we `crop` the dataset
        # to get the transform (resolution).
        #
        # Note: Should be handled in gdal 3.8 directly
        # https://github.com/OSGeo/gdal/pull/8775
        if (
            self.crs == WGS84_CRS
            and dst_crs == WEB_MERCATOR_CRS
            and (src_bounds[1] < -85.06 or src_bounds[3] > 85.06)
        ):
            warnings.warn(
                "Adjusting dataset latitudes to avoid re-projection overflow",
                UserWarning,
            )
            src_bounds[1] = max(src_bounds[1], -85.06)
            src_bounds[3] = min(src_bounds[3], 85.06)

            # North->South
            if src_transform.e > 0:
                src_bounds = [src_bounds[0], src_bounds[3], src_bounds[2], src_bounds[1]]
            # West->East
            if src_transform.a < 0:
                src_bounds = [src_bounds[2], src_bounds[1], src_bounds[1], src_bounds[3]]

            w = windows.from_bounds(*src_bounds, transform=src_transform)
            src_height = round(w.height)
            src_width = round(w.width)

        if dst_crs != self.crs:
            # transform of the reprojected dataset
            dst_transform, _, _ = calculate_default_transform(
                self.crs, dst_crs, src_width, src_height, *src_bounds
            )
        else:
            dst_transform = from_bounds(*src_bounds, src_width, src_height)

        if bounds_crs and bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        w, s, e, n = bbox
        # max size of the output dataset for the bbox
        dst_width = max(1, round((e - w) / dst_transform.a))
        dst_height = max(1, round((s - n) / dst_transform.e))

        if max_size:
            height, width = _get_width_height(max_size, dst_height, dst_width)

        elif _missing_size(height, width):
            ratio = dst_height / dst_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        height = height or dst_height
        width = width or dst_width
        da = da.rio.reproject(
            dst_crs,
            shape=(height, width),
            transform=from_bounds(w, s, e, n, width, height),
            resampling=Resampling[reproject_method],
            nodata=nodata,
        )

        arr = da.to_masked_array()
        arr.mask |= arr.data == da.rio.nodata
        if out_dtype:
            arr = arr.astype(out_dtype)

        output_bounds = da.rio._unordered_bounds()
        if output_bounds[1] > output_bounds[3] and da.rio.transform().e > 0:
            yaxis = self.input.dims.index(self.input.rio.y_dim)
            arr = numpy.flip(arr, axis=yaxis)

        return ImageData(
            arr,
            bounds=bbox,
            crs=da.rio.crs,
            dataset_statistics=stats,
            band_descriptions=band_descriptions,
            nodata=da.rio.nodata,
        )

    def preview(  # noqa: C901
        self,
        max_size: int = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        dst_crs: CRS | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        out_dtype: str | numpy.dtype | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Return a preview of a dataset.

        Args:
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            dst_crs (rasterio.crs.CRS, optional): target coordinate reference system.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        da, band_descriptions = self._sel_indexes(indexes)

        if da.nbytes > MAX_ARRAY_SIZE:
            raise MaxArraySizeError(
                f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put DataArray of {da.shape} in memory."
            )

        if nodata is not None:
            da = da.rio.write_nodata(nodata)

        if dst_crs and dst_crs != self.crs:
            src_width = da.rio.width
            src_height = da.rio.height
            src_bounds = list(da.rio.bounds())
            src_transform = da.rio.transform()

            # Fix for https://github.com/cogeotiff/rio-tiler/issues/654
            #
            # When using `calculate_default_transform` with dataset
            # which span at high/low latitude outside the area_of_use
            # of the WebMercator projection, we `crop` the dataset
            # to get the transform (resolution).
            #
            # Note: Should be handled in gdal 3.8 directly
            # https://github.com/OSGeo/gdal/pull/8775
            if (
                self.crs == WGS84_CRS
                and dst_crs == WEB_MERCATOR_CRS
                and (src_bounds[1] < -85.06 or src_bounds[3] > 85.06)
            ):
                warnings.warn(
                    "Adjusting dataset latitudes to avoid re-projection overflow",
                    UserWarning,
                )
                src_bounds[1] = max(src_bounds[1], -85.06)
                src_bounds[3] = min(src_bounds[3], 85.06)

                # North->South
                if src_transform.e > 0:
                    src_bounds = [
                        src_bounds[0],
                        src_bounds[3],
                        src_bounds[2],
                        src_bounds[1],
                    ]
                # West->East
                if src_transform.a < 0:
                    src_bounds = [
                        src_bounds[2],
                        src_bounds[1],
                        src_bounds[1],
                        src_bounds[3],
                    ]

                w = windows.from_bounds(*src_bounds, transform=src_transform)
                src_height = round(w.height)
                src_width = round(w.width)

            dst_transform, w, h = calculate_default_transform(
                self.crs, dst_crs, src_width, src_height, *src_bounds
            )
            da = da.rio.reproject(
                dst_crs,
                shape=(h, w),
                transform=dst_transform,
                resampling=Resampling[reproject_method],
                nodata=nodata,
            )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = da.attrs.get("valid_min"), da.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * da.rio.count

        arr = da.to_masked_array()
        if out_dtype:
            arr = cast(numpy.ma.MaskedArray, arr.astype(out_dtype))
        arr.mask |= arr.data == da.rio.nodata

        output_bounds = da.rio._unordered_bounds()
        if output_bounds[1] > output_bounds[3] and da.rio.transform().e > 0:
            yaxis = self.input.dims.index(self.input.rio.y_dim)
            arr = cast(numpy.ma.MaskedArray, numpy.flip(arr, axis=yaxis))

        img = ImageData(
            arr,
            bounds=da.rio.bounds(),
            crs=da.rio.crs,
            dataset_statistics=stats,
            band_descriptions=band_descriptions,
            nodata=da.rio.nodata,
        )

        if max_size:
            height, width = _get_width_height(max_size, img.height, img.width)

        elif _missing_size(height, width):
            ratio = img.height / img.width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        if (height and width) and (height != da.rio.height or width != da.rio.width):
            img = img.resize(height, width, resampling_method=resampling_method)

        return img

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        out_dtype: str | numpy.dtype | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a pixel value from a dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            nodata (int or float, optional): Overwrite dataset internal nodata value.

        Returns:
            PointData

        """
        da_lon, da_lat = transform_coords(coord_crs, self.crs, [lon], [lat])

        if not (
            (self.bounds[0] < da_lon[0] < self.bounds[2])
            and (self.bounds[1] < da_lat[0] < self.bounds[3])
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        da, band_descriptions = self._sel_indexes(indexes)

        if nodata is not None:
            da = da.rio.write_nodata(nodata)

        y, x = rowcol(da.rio.transform(), da_lon, da_lat)

        if da.ndim == 2:
            arr = numpy.expand_dims(da[int(y[0]), int(x[0])].to_masked_array(), axis=0)
        else:
            arr = da[:, int(y[0]), int(x[0])].to_masked_array()

        if out_dtype:
            arr = arr.astype(out_dtype)
        arr.mask |= arr.data == da.rio.nodata  # type: ignore [attr-defined]

        return PointData(
            arr,
            coordinates=(lon, lat),
            crs=coord_crs,
            band_descriptions=band_descriptions,
            pixel_location=(x, y),
            nodata=da.rio.nodata,
        )

    def feature(
        self,
        shape: dict,
        dst_crs: CRS | None = None,
        shape_crs: CRS = WGS84_CRS,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: NoData | None = None,
        indexes: Indexes | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        resampling_method: RIOResampling = "nearest",
        out_dtype: str | numpy.dtype | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a dataset defined by a geojson feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            auto_expand (boolean, optional): When True, rioxarray's clip_box will expand clip search if only 1D raster found with clip. When False, will throw `OneDimensionalRaster` error if only 1 x or y data point is found. Defaults to True.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.

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
            nodata=nodata,
            indexes=indexes,
            max_size=max_size,
            width=width,
            height=height,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
            out_dtype=out_dtype,
            auto_expand=auto_expand,
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
