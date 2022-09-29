"""rio_tiler.io.xarray: Xarray Reader."""

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


import xarray


@attr.s
class XarrayReader(BaseReader):
    """Xarray Reader.

    Attributes:
        input (str): Zarr path.
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
    dataset: Any = attr.ib(default=None)  # Xarray or rio Xarray

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    config = attr.ib(factory=dict)

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

    # Context Manager to handle rasterio open/close
    _ctx_stack = attr.ib(init=False, factory=contextlib.ExitStack)

    _minzoom: int = attr.ib(init=False, default=None)
    _maxzoom: int = attr.ib(init=False, default=None)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        if self.config:
            self._kwargs.update(**default)

        if not self.dataset:
            # self.dataset = self._ctx_stack.enter_context(rasterio.open(self.input))
            # TODO
            pass

        # TODO: Get bounds
        self.bounds = tuple(self.dataset.bounds)

        # TODO Get CRS
        self.crs = WGS84_CRS


    def close(self):
        """Close rasterio dataset."""
        self._ctx_stack.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    def get_minzoom(self) -> int:
        """Define dataset minimum zoom level."""
        if self._minzoom is None:
            # TODO: Get transform from the data and figure the MaxZoom
            # self._minzoom = self.tms.zoom_for_res(resolution)
            pass

        return self._minzoom

    def get_maxzoom(self) -> int:
        """Define dataset maximum zoom level."""
        if self._maxzoom is None:
            # TODO: Get transform from the data and figure the MaxZoom
            # self._minzoom = self.tms.zoom_for_res(resolution)
            pass

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
        """Return COG info."""
        raise NotImplemented

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
        raise NotImplemented

    # TODO: Do we want time dimension?
    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        variables: Any = None,
        expression: Optional[str] = None,
        tile_buffer: Optional[NumType] = None,  # IGNORE THIS
        buffer: Optional[float] = None,  # WE CAN IGNORE THIS FOR NOW
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
        if isinstance(indexes, int):
            indexes = (indexes,)

        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside {self.input} bounds"
            )

        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        if not dst_crs:
            dst_crs = bounds_crs

        # TODO: Implement the part read
        # img = reader.part(
        #     self.dataset,
        #     bbox,
        #     max_size=max_size,
        #     width=width,
        #     height=height,
        #     bounds_crs=bounds_crs,
        #     dst_crs=dst_crs,
        #     indexes=indexes,
        #     buffer=buffer,
        #     **kwargs,
        # )
        img.assets = [self.input]

        if expression:
            return img.apply_expression(expression)

        return img

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
        raise NotImplemented

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
            kwargs (optional): Options to forward to the `rio_tiler.reader.preview` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplemented


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
        raise NotImplemented


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
        raise NotImplemented


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
        raise NotImplemented
