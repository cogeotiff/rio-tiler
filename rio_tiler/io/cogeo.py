"""rio_tiler.io.cogeo: raster processing."""

import contextlib
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import attr
import numpy
import rasterio
from morecantile import BoundingBox, Tile, TileMatrixSet
from rasterio import transform
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.features import bounds as featureBounds
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform, transform_bounds

from .. import reader
from ..constants import WEB_MERCATOR_TMS, WGS84_CRS
from ..errors import (
    ExpressionMixingWarning,
    IncorrectTileBuffer,
    NoOverviewWarning,
    TileOutsideBounds,
)
from ..expression import apply_expression, parse_expression
from ..models import BandStatistics, ImageData, Info
from ..types import BBox, DataMaskType, Indexes, NoData, NumType
from ..utils import (
    create_cutline,
    get_array_statistics,
    get_bands_names,
    has_alpha_band,
    has_mask_band,
)
from .base import BaseReader


@attr.s
class COGReader(BaseReader):
    """Cloud Optimized GeoTIFF Reader.

    Attributes:
        input (str): Cloud Optimized GeoTIFF path.
        dataset (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT, optional): Rasterio dataset.
        bounds (tuple): Dataset bounds (left, bottom, right, top).
        crs (rasterio.crs.CRS): Dataset CRS.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set minzoom for the tiles.
        maxzoom (int, optional): Set maxzoom for the tiles.
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

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

    # Context Manager to handle rasterio open/close
    _ctx_stack = attr.ib(init=False, factory=contextlib.ExitStack)

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

        self.dataset = self.dataset or self._ctx_stack.enter_context(
            rasterio.open(self.input)
        )
        self.bounds = tuple(self.dataset.bounds)
        self.crs = self.dataset.crs

        self.nodata = self.nodata if self.nodata is not None else self.dataset.nodata

        if self.minzoom is None or self.maxzoom is None:
            self._set_zooms()

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

    def get_zooms(self, tilesize: int = 256) -> Tuple[int, int]:
        """Calculate raster min/max zoom level for input TMS."""
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

        # The maxzoom is defined by finding the minimum difference between
        # the raster resolution and the zoom level resolution
        resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
        maxzoom = self.tms.zoom_for_res(resolution)

        # The minzoom is defined by the resolution of the maximum theoretical overview level
        overview_level = get_maximum_overview_level(w, h, minsize=tilesize)
        ovr_resolution = resolution * (2 ** overview_level)
        minzoom = self.tms.zoom_for_res(ovr_resolution)

        return (minzoom, maxzoom)

    def _set_zooms(self):
        """Calculate raster min/max zoom level."""
        try:
            minzoom, maxzoom = self.get_zooms()
        except:  # noqa
            # if we can't get min/max zoom from the dataset we default to TMS min/max zoom
            warnings.warn(
                "Cannot dertermine min/max zoom based on dataset information, will default to TMS min/max zoom.",
                UserWarning,
            )
            minzoom, maxzoom = self.tms.minzoom, self.tms.maxzoom

        self.minzoom = self.minzoom if self.minzoom is not None else minzoom
        self.maxzoom = self.maxzoom if self.maxzoom is not None else maxzoom
        return

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
                (f"{ix}", self.dataset.tags(ix)) for ix in self.dataset.indexes
            ],
            "band_descriptions": [
                (f"{ix}", _get_descr(ix)) for ix in self.dataset.indexes
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
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        kwargs = {**self._kwargs, **kwargs}

        data = self.preview(max_size=max_size, **kwargs)

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
            tile_buffer (int or float, optional): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            kwargs (optional): Options to forward to the `COGReader.part` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside {self.input} bounds"
            )

        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))
        if tile_buffer is not None:
            if tile_buffer % 0.5:
                raise IncorrectTileBuffer(
                    "`tile_buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
                )

            x_res = (tile_bounds.right - tile_bounds.left) / tilesize
            y_res = (tile_bounds.top - tile_bounds.bottom) / tilesize

            # Buffered Tile Bounds
            tile_bounds = BoundingBox(
                tile_bounds.left - x_res * tile_buffer,
                tile_bounds.bottom - y_res * tile_buffer,
                tile_bounds.right + x_res * tile_buffer,
                tile_bounds.top + y_res * tile_buffer,
            )

            # Buffered Tile Size
            tilesize += int(tile_buffer * 2)

        return self.part(
            tile_bounds,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=None,
            height=tilesize,
            width=tilesize,
            max_size=None,
            indexes=indexes,
            expression=expression,
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
            kwargs (optional): Options to forward to the `rio_tiler.reader.part` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        if not dst_crs:
            dst_crs = bounds_crs

        data, mask = reader.part(
            self.dataset,
            bbox,
            max_size=max_size,
            width=width,
            height=height,
            bounds_crs=bounds_crs,
            dst_crs=dst_crs,
            indexes=indexes,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        if bounds_crs and bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        return ImageData(
            data,
            mask,
            bounds=bbox,
            crs=dst_crs,
            assets=[self.input],
            band_names=get_bands_names(
                indexes=indexes, expression=expression, count=data.shape[0]
            ),
        )

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
        kwargs = {**self._kwargs, **kwargs}

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        data, mask = reader.preview(
            self.dataset,
            indexes=indexes,
            max_size=max_size,
            width=width,
            height=height,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        return ImageData(
            data,
            mask,
            bounds=self.bounds,
            crs=self.crs,
            assets=[self.input],
            band_names=get_bands_names(
                indexes=indexes, expression=expression, count=data.shape[0]
            ),
        )

    def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> List:
        """Read a pixel value from a COG.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `rio_tiler.reader.point` function.

        Returns:
            list: Pixel value per band indexes.

        """
        kwargs = {**self._kwargs, **kwargs}

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        point = reader.point(
            self.dataset, (lon, lat), indexes=indexes, coord_crs=coord_crs, **kwargs
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            point = apply_expression(blocks, bands, numpy.array(point)).tolist()

        return point

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

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        data, mask = reader.read(self.dataset, indexes=indexes, **kwargs)

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        return ImageData(
            data,
            mask,
            bounds=self.bounds,
            crs=self.crs,
            assets=[self.input],
            band_names=get_bands_names(
                indexes=indexes, expression=expression, count=data.shape[0]
            ),
        )


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
