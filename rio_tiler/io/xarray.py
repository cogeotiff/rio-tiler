"""rio_tiler.io.xarray: Xarray Reader."""
from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional

import attr
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.features import is_valid_geom
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.transform import from_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import PointOutsideBounds, RioTilerError, TileOutsideBounds
from rio_tiler.io.base import BaseReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox

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
        geographic_crs (rasterio.crs.CRS, optional): CRS to use as geographic coordinate system. Defaults to WGS84.

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
    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    _minzoom: int = attr.ib(init=False, default=None)
    _maxzoom: int = attr.ib(init=False, default=None)

    _dims: List = attr.ib(init=False, factory=list)

    def __attrs_post_init__(self):
        """Set bounds and CRS."""
        assert xarray is not None, "xarray must be installed to use XarrayReader"
        assert rioxarray is not None, "rioxarray must be installed to use XarrayReader"

        self.bounds = tuple(self.input.rio.bounds())
        self.crs = self.input.rio.crs

        self._dims = [
            d
            for d in self.input.dims
            if d not in [self.input.rio.x_dim, self.input.rio.y_dim]
        ]

    def _dst_geom_in_tms_crs(self):
        """Return dataset info in TMS projection."""
        if self.crs != self.tms.rasterio_crs:
            dst_affine, w, h = calculate_default_transform(
                self.crs,
                self.tms.rasterio_crs,
                self.input.rio.width,
                self.input.rio.height,
                *self.bounds,
            )
        else:
            dst_affine = list(self.input.rio.transform())
            w = self.input.rio.width
            h = self.input.rio.height

        return dst_affine, w, h

    def get_minzoom(self) -> int:
        """Define dataset minimum zoom level."""
        if self._minzoom is None:
            # We assume the TMS tilesize to be constant over all matrices
            # ref: https://github.com/OSGeo/gdal/blob/dc38aa64d779ecc45e3cd15b1817b83216cf96b8/gdal/frmts/gtiff/cogdriver.cpp#L274
            tilesize = self.tms.tileMatrix[0].tileWidth

            try:
                dst_affine, w, h = self._dst_geom_in_tms_crs()

                # The minzoom is defined by the resolution of the maximum theoretical overview level
                # We assume `tilesize`` is the smallest overview size
                overview_level = get_maximum_overview_level(w, h, minsize=tilesize)

                # Get the resolution of the overview
                resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
                ovr_resolution = resolution * (2**overview_level)

                # Find what TMS matrix match the overview resolution
                self._minzoom = self.tms.zoom_for_res(ovr_resolution)

            except:  # noqa
                # if we can't get min/max zoom from the dataset we default to TMS maxzoom
                warnings.warn(
                    "Cannot determine maxzoom based on dataset information, will default to TMS maxzoom.",
                    UserWarning,
                )
                self._minzoom = self.tms.maxzoom

        return self._minzoom

    def get_maxzoom(self) -> int:
        """Define dataset maximum zoom level."""
        if self._maxzoom is None:
            try:
                dst_affine, _, _ = self._dst_geom_in_tms_crs()

                # The maxzoom is defined by finding the minimum difference between
                # the raster resolution and the zoom level resolution
                resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
                self._maxzoom = self.tms.zoom_for_res(resolution)

            except:  # noqa
                # if we can't get min/max zoom from the dataset we default to TMS maxzoom
                warnings.warn(
                    "Cannot determine maxzoom based on dataset information, will default to TMS maxzoom.",
                    UserWarning,
                )
                self._maxzoom = self.tms.maxzoom

        return self._maxzoom

    @property
    def minzoom(self):
        """Return dataset minzoom."""
        return self.get_minzoom()

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self.get_maxzoom()

    def info(self) -> Info:
        """Return xarray.DataArray info."""
        bands = [str(band) for d in self._dims for band in self.input[d].values]
        metadata = [band.attrs for d in self._dims for band in self.input[d]]

        meta = {
            "bounds": self.geographic_bounds,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
            "band_metadata": [(f"b{ix}", v) for ix, v in enumerate(metadata, 1)],
            "band_descriptions": [(f"b{ix}", v) for ix, v in enumerate(bands, 1)],
            "dtype": str(self.input.dtype),
            "nodata_type": "Nodata" if self.input.rio.nodata is not None else "None",
            "name": self.input.name,
            "count": self.input.rio.count,
            "width": self.input.rio.width,
            "height": self.input.rio.height,
            "attrs": self.input.attrs,
        }
        return Info(**meta)

    def statistics(
        self,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: List[int] = [2, 98],
        hist_options: Optional[Dict] = None,
        max_size: int = 1024,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset."""
        raise NotImplementedError

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        resampling_method: Resampling = "nearest",
    ) -> ImageData:
        """Read a Web Map tile from a dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output image size. Defaults to `256`.
            resampling_method (rasterio.enums.Resampling, optional): Rasterio's resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside bounds"
            )

        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        # Create source array by clipping the xarray dataset to extent of the tile.
        ds = self.input.rio.clip_box(*tile_bounds, crs=self.tms.rasterio_crs)
        ds = ds.rio.reproject(
            self.tms.rasterio_crs,
            shape=(tilesize, tilesize),
            transform=from_bounds(*tile_bounds, height=tilesize, width=tilesize),
            resampling=Resampling[resampling_method],
        )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * ds.rio.count

        band_names = [str(band) for d in self._dims for band in self.input[d].values]

        return ImageData(
            ds.data,
            bounds=tile_bounds,
            crs=self.tms.rasterio_crs,
            dataset_statistics=stats,
            band_names=band_names,
        )

    def part(
        self,
        bbox: BBox,
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = WGS84_CRS,
        resampling_method: Resampling = "nearest",
    ) -> ImageData:
        """Read part of a dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs ("dst_crs").
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            bounds_crs (rasterio.crs.CRS, optional): Bounds Coordinate Reference System. Defaults to `epsg:4326`.
            resampling_method (rasterio.enums.Resampling, optional): Rasterio's resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        dst_crs = dst_crs or bounds_crs
        ds = self.input.rio.clip_box(*bbox, crs=bounds_crs)

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
                resampling=Resampling[resampling_method],
            )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * ds.rio.count

        band_names = [str(band) for d in self._dims for band in self.input[d].values]

        return ImageData(
            ds.data,
            bounds=ds.rio.bounds(),
            crs=ds.rio.crs,
            dataset_statistics=stats,
            band_names=band_names,
        )

    def preview(
        self,
        max_size: int = 1024,
        height: Optional[int] = None,
        width: Optional[int] = None,
    ) -> ImageData:
        """Return a preview of a dataset.

        Args:
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
    ) -> PointData:
        """Read a pixel value from a dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.

        Returns:
            PointData

        """
        ds_lon, ds_lat = transform_coords(coord_crs, self.crs, [lon], [lat])

        if not (
            (self.bounds[0] < ds_lon[0] < self.bounds[2])
            and (self.bounds[1] < ds_lat[0] < self.bounds[3])
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        y, x = rowcol(self.input.rio.transform(), ds_lon, ds_lat)

        band_names = [str(band) for d in self._dims for band in self.input[d].values]

        return PointData(
            self.input.data[:, y[0], x[0]],
            coordinates=(lon, lat),
            crs=coord_crs,
            band_names=band_names,
        )

    def feature(
        self,
        shape: Dict,
        dst_crs: Optional[CRS] = None,
        shape_crs: CRS = WGS84_CRS,
        resampling_method: Resampling = "nearest",
    ) -> ImageData:
        """Read part of a dataset defined by a geojson feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if not dst_crs:
            dst_crs = shape_crs

        if "geometry" in shape:
            shape = shape["geometry"]

        if not is_valid_geom(shape):
            raise RioTilerError("Invalid geometry")

        ds = self.input.rio.clip([shape], crs=shape_crs)

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
                resampling=Resampling[resampling_method],
            )

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = ds.attrs.get("valid_min"), ds.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * ds.rio.count

        band_names = [str(band) for d in self._dims for band in self.input[d].values]

        return ImageData(
            ds.data,
            bounds=ds.rio.bounds(),
            crs=ds.rio.crs,
            dataset_statistics=stats,
            band_names=band_names,
        )
