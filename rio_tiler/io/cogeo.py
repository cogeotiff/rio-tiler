"""rio_tiler.io.cogeo: raster processing."""

import contextlib
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

import attr
import numpy
import rasterio
from morecantile import Tile, TileMatrixSet
from rasterio import transform
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.features import bounds as featureBounds
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform

from .. import reader
from ..constants import WEB_MERCATOR_TMS, WGS84_CRS
from ..errors import ExpressionMixingWarning, NoOverviewWarning, TileOutsideBounds
from ..expression import parse_expression
from ..models import BandStatistics, ImageData, Info, PointData
from ..types import BBox, DataMaskType, Indexes, NoData, NumType
from ..utils import create_cutline, get_array_statistics, has_alpha_band, has_mask_band
from .base import BaseReader


@attr.s
class COGReader(BaseReader):
    """Cloud Optimized GeoTIFF Reader.

    Attributes:
        input (str): Cloud Optimized GeoTIFF path.
        dataset (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT, optional): Rasterio dataset.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        geographic_crs (rasterio.crs.CRS, optional): CRS to use as geographic coordinate system. Defaults to WGS84.
        colormap (dict, optional): Overwrite internal colormap.
        nodata (int or float or str, optional): Global options, overwrite internal nodata value.
        unscale (bool, optional): Global options, apply internal scale and offset on all read operations.
        resampling_method (rasterio.enums.Resampling, optional): Global options, resampling method to use for read operations.
        vrt_options (dict, optional): Global options, WarpedVRT options to use for read operations.
        post_process (callable, optional): Global options, Function to apply after all read operations.

    Examples:
        >>> with COGReader(src_path) as cog:
            cog.tile(...)

        >>> # Set global options
            with COGReader(src_path, unscale=True, nodata=0) as cog:
                cog.tile(...)

        >>> with rasterio.open(src_path) as src_dst:
                with WarpedVRT(src_dst, ...) as vrt_dst:
                    with COGReader(None, dataset=vrt_dst) as cog:
                        cog.tile(...)

        >>> with rasterio.open(src_path) as src_dst:
                with COGReader(None, dataset=src_dst) as cog:
                    cog.tile(...)

    """

    input: str = attr.ib()
    dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None
    )

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    colormap: Dict = attr.ib(default=None)

    # Define global options to be forwarded to functions reading the data (e.g `rio_tiler.reader.read`)
    nodata: Optional[NoData] = attr.ib(default=None)
    unscale: Optional[bool] = attr.ib(default=None)
    resampling_method: Optional[Resampling] = attr.ib(default=None)
    vrt_options: Optional[Dict] = attr.ib(default=None)
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
    ] = attr.ib(default=None)

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

    # Context Manager to handle rasterio open/close
    _ctx_stack = attr.ib(init=False, factory=contextlib.ExitStack)

    _minzoom: int = attr.ib(init=False, default=None)
    _maxzoom: int = attr.ib(init=False, default=None)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        if self.nodata is not None:
            self._kwargs["nodata"] = self.nodata
        if self.unscale is not None:
            self._kwargs["unscale"] = self.unscale
        if self.resampling_method is not None:
            self._kwargs["resampling_method"] = self.resampling_method
        if self.vrt_options is not None:
            self._kwargs["vrt_options"] = self.vrt_options
        if self.post_process is not None:
            self._kwargs["post_process"] = self.post_process

        if not self.dataset:
            dataset = self._ctx_stack.enter_context(rasterio.open(self.input))
            if dataset.gcps[0]:
                self.dataset = self._ctx_stack.enter_context(
                    WarpedVRT(
                        dataset,
                        src_crs=dataset.gcps[1],
                        src_transform=transform.from_gcps(dataset.gcps[0]),
                    )
                )
            else:
                self.dataset = dataset

        self.bounds = tuple(self.dataset.bounds)
        self.crs = self.dataset.crs

        self.nodata = self.nodata if self.nodata is not None else self.dataset.nodata

        if self.colormap is None:
            self._get_colormap()

        if min(
            self.dataset.width, self.dataset.height
        ) > 512 and not self.dataset.overviews(1):
            warnings.warn(
                "The dataset has no Overviews. rio-tiler performances might be impacted.",
                NoOverviewWarning,
            )

    def close(self):
        """Close rasterio dataset."""
        self._ctx_stack.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    def _dst_geom_in_tms_crs(self):
        """Return dataset info in TMS projection."""
        if self.dataset.crs != self.tms.rasterio_crs:
            dst_affine, w, h = calculate_default_transform(
                self.dataset.crs,
                self.tms.rasterio_crs,
                self.dataset.width,
                self.dataset.height,
                *self.dataset.bounds,
            )
        else:
            dst_affine = list(self.dataset.transform)
            w = self.dataset.width
            h = self.dataset.height

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
                # if we can't get max zoom from the dataset we default to TMS maxzoom
                warnings.warn(
                    "Cannot determine minzoom based on dataset information, will default to TMS minzoom.",
                    UserWarning,
                )
                self._minzoom = self.tms.minzoom

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

    def _get_colormap(self):
        """Retrieve the internal colormap."""
        try:
            self.colormap = self.dataset.colormap(1)
        except ValueError:
            self.colormap = {}
            pass

    def info(self) -> Info:
        """Return COG info."""

        def _get_descr(ix):
            """Return band description."""
            return self.dataset.descriptions[ix - 1] or ""

        if has_alpha_band(self.dataset):
            nodata_type = "Alpha"
        elif has_mask_band(self.dataset):
            nodata_type = "Mask"
        elif self.nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        meta = {
            "bounds": self.geographic_bounds,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
            "band_metadata": [
                (f"b{ix}", self.dataset.tags(ix)) for ix in self.dataset.indexes
            ],
            "band_descriptions": [
                (f"b{ix}", _get_descr(ix)) for ix in self.dataset.indexes
            ],
            "dtype": self.dataset.meta["dtype"],
            "colorinterp": [
                self.dataset.colorinterp[ix - 1].name for ix in self.dataset.indexes
            ],
            "nodata_type": nodata_type,
            # additional info (not in default model)
            "driver": self.dataset.driver,
            "count": self.dataset.count,
            "width": self.dataset.width,
            "height": self.dataset.height,
            "overviews": self.dataset.overviews(1),
        }
        if self.dataset.scales[0] and self.dataset.offsets[0]:
            meta.update(
                {"scale": self.dataset.scales[0], "offset": self.dataset.offsets[0]}
            )

        if self.colormap:
            meta.update({"colormap": self.colormap})

        if nodata_type == "Nodata":
            meta.update({"nodata_value": self.nodata})

        return Info(**meta)

    def statistics(
        self,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: List[int] = [2, 98],
        hist_options: Optional[Dict] = None,
        max_size: int = 1024,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            kwargs (optional): Options to forward to `self.read`.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        kwargs = {**self._kwargs, **kwargs}

        data = self.read(
            max_size=max_size, indexes=indexes, expression=expression, **kwargs
        )

        hist_options = hist_options or {}

        stats = get_array_statistics(
            data.as_masked(),
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            **hist_options,
        )

        return {
            f"{data.band_names[ix]}": BandStatistics(**stats[ix])
            for ix in range(len(stats))
        }

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        tile_buffer: Optional[NumType] = None,
        buffer: Optional[float] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read a Web Map tile from a COG.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output image size. Defaults to `256`.
            indexes (int or sequence of int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            tile_buffer (int or float, optional): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258). DEPRECATED
            buffer (float, optional): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            kwargs (optional): Options to forward to the `COGReader.part` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside {self.input} bounds"
            )

        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        if tile_buffer:
            warnings.warn(
                "`tile_buffer` is deprecated, use `buffer`.", DeprecationWarning
            )
            buffer = tile_buffer

        return self.part(
            tile_bounds,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=None,
            height=tilesize,
            width=tilesize,
            max_size=None,
            indexes=indexes,
            expression=expression,
            buffer=buffer,
            **kwargs,
        )

    def part(
        self,
        bbox: BBox,
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = WGS84_CRS,
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = None,
        max_size: Optional[int] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        buffer: Optional[float] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a COG.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs ("dst_crs").
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            bounds_crs (rasterio.crs.CRS, optional): Bounds Coordinate Reference System. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            buffer (float, optional): Buffer on each side of the given aoi. It must be a multiple of `0.5`. Output **image size** will be expanded to `output imagesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            kwargs (optional): Options to forward to the `rio_tiler.reader.part` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        if not dst_crs:
            dst_crs = bounds_crs

        img = reader.part(
            self.dataset,
            bbox,
            max_size=max_size,
            width=width,
            height=height,
            bounds_crs=bounds_crs,
            dst_crs=dst_crs,
            indexes=indexes,
            buffer=buffer,
            **kwargs,
        )
        img.assets = [self.input]

        if expression:
            return img.apply_expression(expression)

        return img

    def preview(
        self,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        max_size: int = 1024,
        height: Optional[int] = None,
        width: Optional[int] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Return a preview of a COG.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            kwargs (optional): Options to forward to the `self.read` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        return self.read(
            indexes=indexes,
            expression=expression,
            max_size=max_size,
            height=height,
            width=width,
            **kwargs,
        )

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a pixel value from a COG.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `rio_tiler.reader.point` function.

        Returns:
            PointData

        """
        kwargs = {**self._kwargs, **kwargs}

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        pt = reader.point(
            self.dataset, (lon, lat), indexes=indexes, coord_crs=coord_crs, **kwargs
        )
        pt.assets = [self.input]

        if expression:
            return pt.apply_expression(expression)

        return pt

    def feature(
        self,
        shape: Dict,
        dst_crs: Optional[CRS] = None,
        shape_crs: CRS = WGS84_CRS,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        max_size: Optional[int] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        buffer: Optional[NumType] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a COG defined by a geojson feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            buffer (int or float, optional): Buffer on each side of the given aoi. It must be a multiple of `0.5`. Output **image size** will be expanded to `output imagesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            kwargs (optional): Options to forward to the `COGReader.part` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if not dst_crs:
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        cutline = create_cutline(self.dataset, shape, geometry_crs=shape_crs)
        vrt_options = kwargs.pop("vrt_options", {})
        vrt_options.update({"cutline": cutline})

        return self.part(
            bbox,
            dst_crs=dst_crs,
            bounds_crs=shape_crs,
            indexes=indexes,
            expression=expression,
            max_size=max_size,
            width=width,
            height=height,
            vrt_options=vrt_options,
            buffer=buffer,
            **kwargs,
        )

    def read(
        self,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read the COG.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `rio_tiler.reader.read` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        img = reader.read(self.dataset, indexes=indexes, **kwargs)
        img.assets = [self.input]

        if expression:
            return img.apply_expression(expression)

        return img


@attr.s
class GCPCOGReader(COGReader):
    """Custom COG Reader with GCPS support.

    Attributes:
        input (str): Cloud Optimized GeoTIFF path.
        src_dataset (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT, optional): Rasterio dataset.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Overwrite Min Zoom level.
        maxzoom (int, optional): Overwrite Max Zoom level.
        colormap (dict, optional): Overwrite internal colormap.
        nodata (int or float or str, optional): Global options, overwrite internal nodata value.
        unscale (bool, optional): Global options, apply internal scale and offset on all read operations.
        resampling_method (rasterio.enums.Resampling, optional): Global options, resampling method to use for read operations.
        vrt_options (dict, optional): Global options, WarpedVRT options to use for read operations.
        post_process (callable, optional): Global options, Function to apply after all read operations.
        dataset (rasterio.vrtWarpedVRT): Warped VRT constructed with dataset GCPS info. **READ ONLY attribute**.

    Examples:
        >>> with COGReader(src_path) as cog:
            cog.tile(...)
            assert cog.dataset
            assert cog.src_dataset

        >>> with rasterio.open(src_path) as src_dst:
                with COGReader(None, src_dataset=src_dst) as cog:
                    cog.tile(...)

    """

    input: str = attr.ib()
    src_dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None
    )

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    colormap: Dict = attr.ib(default=None)

    # Define global options to be forwarded to functions reading the data (e.g `rio_tiler.reader.read`)
    nodata: Optional[NoData] = attr.ib(default=None)
    unscale: Optional[bool] = attr.ib(default=None)
    resampling_method: Optional[Resampling] = attr.ib(default=None)
    vrt_options: Optional[Dict] = attr.ib(default=None)
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
    ] = attr.ib(default=None)

    # for GCPCOGReader, dataset is not a input option.
    dataset: WarpedVRT = attr.ib(init=False)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        warnings.warn(
            "GCPCOGReader is deprecated and will be removed in 4.0. Please use COGReader.",
            DeprecationWarning,
        )

        self.src_dataset = self.src_dataset or self._ctx_stack.enter_context(
            rasterio.open(self.input)
        )
        self.dataset = self._ctx_stack.enter_context(
            WarpedVRT(
                self.src_dataset,
                src_crs=self.src_dataset.gcps[1],
                src_transform=transform.from_gcps(self.src_dataset.gcps[0]),
            )
        )
        super().__attrs_post_init__()
