"""rio_tiler.io.xarray: Xarray Reader."""

from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional

import attr
import numpy
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.transform import from_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_geom

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    InvalidGeographicBounds,
    MissingCRS,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.io.base import BaseReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.reader import _get_width_height
from rio_tiler.types import BBox, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import CRS_to_uri, _validate_shape_input, get_array_statistics

try:
    import xarray
except ImportError:  # pragma: nocover
    xarray = None  # type: ignore

try:
    import rioxarray
except ImportError:  # pragma: nocover
    rioxarray = None  # type: ignore


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

    _dims: List = attr.ib(init=False, factory=list)

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
            if d not in [self.input.rio.x_dim, self.input.rio.y_dim]
        ]

    @property
    def minzoom(self):
        """Return dataset minzoom."""
        return self._minzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self._maxzoom

    @property
    def band_names(self) -> List[str]:
        """Return list of `band names` in DataArray."""
        return [str(band) for d in self._dims for band in self.input[d].values] or [
            "value"
        ]

    def info(self) -> Info:
        """Return xarray.DataArray info."""
        bands = [str(band) for d in self._dims for band in self.input[d].values] or [
            "value"
        ]
        metadata = [band.attrs for d in self._dims for band in self.input[d]] or [{}]

        meta = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            "band_metadata": [(f"b{ix}", v) for ix, v in enumerate(metadata, 1)],
            "band_descriptions": [(f"b{ix}", v) for ix, v in enumerate(bands, 1)],
            "dtype": str(self.input.dtype),
            "nodata_type": "Nodata" if self.input.rio.nodata is not None else "None",
            "name": self.input.name,
            "count": self.input.rio.count,
            "width": self.input.rio.width,
            "height": self.input.rio.height,
            "attrs": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in self.input.attrs.items()
            },
        }

        return Info(**meta)

    def statistics(
        self,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: Optional[List[int]] = None,
        hist_options: Optional[Dict] = None,
        nodata: Optional[NoData] = None,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return statistics from a dataset."""
        hist_options = hist_options or {}

        ds = self.input
        if nodata is not None:
            ds = ds.rio.write_nodata(nodata)

        data = ds.to_masked_array()
        data.mask |= data.data == ds.rio.nodata

        stats = get_array_statistics(
            data,
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            **hist_options,
        )

        return {
            self.band_names[ix]: BandStatistics(**val) for ix, val in enumerate(stats)
        }

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: Optional[NoData] = None,
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

        ds = self.input
        if nodata is not None:
            ds = ds.rio.write_nodata(nodata)

        tile_bounds = tuple(self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)))
        dst_crs = self.tms.rasterio_crs

        # Create source array by clipping the xarray dataset to extent of the tile.
        ds = ds.rio.clip_box(
            *tile_bounds,
            crs=dst_crs,
            auto_expand=auto_expand,
        )
        ds = ds.rio.reproject(
            dst_crs,
            shape=(tilesize, tilesize),
            transform=from_bounds(*tile_bounds, height=tilesize, width=tilesize),
            resampling=Resampling[reproject_method],
            nodata=nodata,
        )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None and nodata not in [minv, maxv]:
            stats = ((minv, maxv),) * ds.rio.count

        arr = ds.to_masked_array()
        arr.mask |= arr.data == ds.rio.nodata

        output_bounds = ds.rio._unordered_bounds()
        if output_bounds[1] > output_bounds[3] and ds.rio.transform().e > 0:
            yaxis = self.input.dims.index(self.input.rio.y_dim)
            arr = numpy.flip(arr, axis=yaxis)

        return ImageData(
            arr,
            bounds=tile_bounds,
            crs=dst_crs,
            dataset_statistics=stats,
            band_names=self.band_names,
        )

    def part(
        self,
        bbox: BBox,
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = WGS84_CRS,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: Optional[NoData] = None,
        max_size: Optional[int] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        resampling_method: RIOResampling = "nearest",
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
        if max_size and width and height:
            warnings.warn(
                "'max_size' will be ignored with with 'height' and 'width' set.",
                UserWarning,
            )

        dst_crs = dst_crs or bounds_crs

        ds = self.input
        if nodata is not None:
            ds = ds.rio.write_nodata(nodata)

        ds = ds.rio.clip_box(
            *bbox,
            crs=bounds_crs,
            auto_expand=auto_expand,
        )

        if dst_crs != self.crs:
            dst_transform, w, h = calculate_default_transform(
                self.crs,
                dst_crs,
                ds.rio.width,
                ds.rio.height,
                *ds.rio.bounds(),
            )
            ds = ds.rio.reproject(
                dst_crs,
                shape=(h, w),
                transform=dst_transform,
                resampling=Resampling[reproject_method],
                nodata=nodata,
            )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * ds.rio.count

        arr = ds.to_masked_array()
        arr.mask |= arr.data == ds.rio.nodata

        output_bounds = ds.rio._unordered_bounds()
        if output_bounds[1] > output_bounds[3] and ds.rio.transform().e > 0:
            yaxis = self.input.dims.index(self.input.rio.y_dim)
            arr = numpy.flip(arr, axis=yaxis)

        img = ImageData(
            arr,
            bounds=ds.rio.bounds(),
            crs=ds.rio.crs,
            dataset_statistics=stats,
            band_names=self.band_names,
        )

        output_height = height or img.height
        output_width = width or img.width
        if max_size and not (width and height):
            output_height, output_width = _get_width_height(
                max_size, img.height, img.width
            )

        if output_height != img.height or output_width != img.width:
            img = img.resize(
                output_height, output_width, resampling_method=resampling_method
            )

        return img

    def preview(
        self,
        max_size: int = 1024,
        height: Optional[int] = None,
        width: Optional[int] = None,
        nodata: Optional[NoData] = None,
        dst_crs: Optional[CRS] = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
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
        if max_size and width and height:
            warnings.warn(
                "'max_size' will be ignored with with 'height' and 'width' set.",
                UserWarning,
            )

        ds = self.input
        if nodata is not None:
            ds = ds.rio.write_nodata(nodata)

        if dst_crs and dst_crs != self.crs:
            dst_transform, w, h = calculate_default_transform(
                self.crs,
                dst_crs,
                ds.rio.width,
                ds.rio.height,
                *ds.rio.bounds(),
            )
            ds = ds.rio.reproject(
                dst_crs,
                shape=(h, w),
                transform=dst_transform,
                resampling=Resampling[reproject_method],
                nodata=nodata,
            )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * ds.rio.count

        arr = ds.to_masked_array()
        arr.mask |= arr.data == ds.rio.nodata

        output_bounds = ds.rio._unordered_bounds()
        if output_bounds[1] > output_bounds[3] and ds.rio.transform().e > 0:
            yaxis = self.input.dims.index(self.input.rio.y_dim)
            arr = numpy.flip(arr, axis=yaxis)

        img = ImageData(
            arr,
            bounds=ds.rio.bounds(),
            crs=ds.rio.crs,
            dataset_statistics=stats,
            band_names=self.band_names,
        )

        output_height = height or img.height
        output_width = width or img.width
        if max_size and not (width and height):
            output_height, output_width = _get_width_height(
                max_size, img.height, img.width
            )

        if output_height != img.height or output_width != img.width:
            img = img.resize(
                output_height, output_width, resampling_method=resampling_method
            )

        return img

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        nodata: Optional[NoData] = None,
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
        ds_lon, ds_lat = transform_coords(coord_crs, self.crs, [lon], [lat])

        if not (
            (self.bounds[0] < ds_lon[0] < self.bounds[2])
            and (self.bounds[1] < ds_lat[0] < self.bounds[3])
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        ds = self.input
        if nodata is not None:
            ds = ds.rio.write_nodata(nodata)

        y, x = rowcol(ds.rio.transform(), ds_lon, ds_lat)

        if ds.ndim == 2:
            arr = numpy.expand_dims(ds[int(y[0]), int(x[0])].to_masked_array(), axis=0)
        else:
            arr = ds[:, int(y[0]), int(x[0])].to_masked_array()

        arr.mask |= arr.data == ds.rio.nodata

        return PointData(
            arr,
            coordinates=(lon, lat),
            crs=coord_crs,
            band_names=self.band_names,
        )

    def feature(
        self,
        shape: Dict,
        dst_crs: Optional[CRS] = None,
        shape_crs: CRS = WGS84_CRS,
        reproject_method: WarpResampling = "nearest",
        auto_expand: bool = True,
        nodata: Optional[NoData] = None,
        max_size: Optional[int] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        resampling_method: RIOResampling = "nearest",
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
            max_size=max_size,
            width=width,
            height=height,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
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
