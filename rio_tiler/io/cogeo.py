"""rio_tiler.io.cogeo: raster processing."""

import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

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
from rasterio.warp import calculate_default_transform, transform_bounds

from .. import reader
from ..constants import WEB_MERCATOR_TMS, WGS84_CRS, BBox, Indexes, NoData
from ..errors import ExpressionMixingWarning, NoOverviewWarning, TileOutsideBounds
from ..expression import apply_expression, parse_expression
from ..models import ImageData, ImageStatistics, Info
from ..utils import create_cutline, has_alpha_band, has_mask_band
from .base import BaseReader


@attr.s
class COGReader(BaseReader):
    """Cloud Optimized GeoTIFF Reader.

    Attributes:
        filepath (str): Cloud Optimized GeoTIFF path.
        dataset (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT, optional): Rasterio dataset.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Overwrite Min Zoom level.
        maxzoom (int, optional): Overwrite Max Zoom level.
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

    filepath: str = attr.ib()
    dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None
    )
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)
    colormap: Dict = attr.ib(default=None)

    # Define global options to be forwarded to functions reading the data (e.g `rio_tiler.reader.read`)
    nodata: Optional[NoData] = attr.ib(default=None)
    unscale: Optional[bool] = attr.ib(default=None)
    resampling_method: Optional[Resampling] = attr.ib(default=None)
    vrt_options: Optional[Dict] = attr.ib(default=None)
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]]
    ] = attr.ib(default=None)

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        self.dataset = self.dataset or rasterio.open(self.filepath)

        self.nodata = self.nodata if self.nodata is not None else self.dataset.nodata

        self.bounds = transform_bounds(
            self.dataset.crs, WGS84_CRS, *self.dataset.bounds, densify_pts=21
        )
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
        if self.filepath:
            self.dataset.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    def get_zooms(self, tilesize: int = 256) -> Tuple[int, int]:
        """Calculate raster min/max zoom level."""
        if self.dataset.crs != self.tms.crs:
            dst_affine, w, h = calculate_default_transform(
                self.dataset.crs,
                self.tms.crs,
                self.dataset.width,
                self.dataset.height,
                *self.dataset.bounds,
            )
        else:
            dst_affine = list(self.dataset.transform)
            w = self.dataset.width
            h = self.dataset.height

        resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
        maxzoom = self.tms.zoom_for_res(resolution)

        overview_level = get_maximum_overview_level(w, h, minsize=tilesize)
        ovr_resolution = resolution * (2 ** overview_level)
        minzoom = self.tms.zoom_for_res(ovr_resolution)

        return minzoom, maxzoom

    def _set_zooms(self):
        """Calculate raster min/max zoom level."""
        minzoom, maxzoom = self.get_zooms()
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
            "bounds": self.bounds,
            "center": self.center,
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

    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        hist_options: Optional[Dict] = None,
        **kwargs: Any,
    ) -> Dict[str, ImageStatistics]:
        """Return bands statistics from a COG.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            kwargs (optional): Options to forward to `rio_tiler.reader.stats`.

        Returns:
            rio_tiler.models.ImageStatistics: bands statistics.

        """
        kwargs = {**self._kwargs, **kwargs}

        hist_options = hist_options or {}

        if self.colormap and not hist_options.get("bins"):
            hist_options["bins"] = [
                k for k, v in self.colormap.items() if v != (0, 0, 0, 255)
            ]

        stats = reader.stats(
            self.dataset, percentiles=(pmin, pmax), hist_options=hist_options, **kwargs,
        )
        return {b: ImageStatistics(**s) for b, s in stats.items()}

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        tile_buffer: Optional[int] = None,
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
            kwargs (optional): Options to forward to the `rio_tiler.reader.part` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        if not self.tile_exists(tile_z, tile_x, tile_y):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside {self.filepath} bounds"
            )

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        tile_bounds = self.tms.xy_bounds(*Tile(x=tile_x, y=tile_y, z=tile_z))
        if tile_buffer:
            x_res = (tile_bounds[2] - tile_bounds[0]) / tilesize
            y_res = (tile_bounds[3] - tile_bounds[1]) / tilesize
            tile_bounds = (
                tile_bounds[0] - x_res * tile_buffer,
                tile_bounds[1] - y_res * tile_buffer,
                tile_bounds[2] + x_res * tile_buffer,
                tile_bounds[3] + y_res * tile_buffer,
            )
            tilesize += tile_buffer * 2

        tile, mask = reader.part(
            self.dataset,
            tile_bounds,
            tilesize,
            tilesize,
            indexes=indexes,
            dst_crs=self.tms.crs,
            **kwargs,
        )
        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            tile = apply_expression(blocks, bands, tile)

        return ImageData(
            tile, mask, bounds=tile_bounds, crs=self.tms.crs, assets=[self.filepath]
        )

    def part(
        self,
        bbox: BBox,
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = WGS84_CRS,
        max_size: int = 1024,
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a COG.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs ("dst_crs").
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            bounds_crs (rasterio.crs.CRS, optional): Bounds Coordinate Reference System. Defaults to `epsg:4326`.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to `1024`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
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
            bounds_crs=bounds_crs,
            dst_crs=dst_crs,
            indexes=indexes,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        if dst_crs == bounds_crs:
            bounds = bbox
        else:
            bounds = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        return ImageData(
            data, mask, bounds=bounds, crs=dst_crs, assets=[self.filepath],
        )

    def preview(
        self,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Return a preview of a COG.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
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

        data, mask = reader.preview(self.dataset, indexes=indexes, **kwargs)

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        return ImageData(
            data,
            mask,
            bounds=self.dataset.bounds,
            crs=self.dataset.crs,
            assets=[self.filepath],
        )

    def point(
        self,
        lon: float,
        lat: float,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> List:
        """Read a pixel value from a COG.

        Args:
            lon (float): Longitude.
            lat (float): Latittude.
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

        point = reader.point(self.dataset, (lon, lat), indexes=indexes, **kwargs)

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            point = apply_expression(blocks, bands, point).tolist()

        return point

    def feature(
        self,
        shape: Dict,
        dst_crs: Optional[CRS] = None,
        shape_crs: CRS = WGS84_CRS,
        max_size: int = 1024,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a COG defined by a geojson feature.

        Args:
            shape (dict): Valid GeoJSON feature.
            dst_crs (rasterio.crs.CRS, optional): Overwrite target coordinate reference system.
            shape_crs (rasterio.crs.CRS, optional): Input geojson coordinate reference system. Defaults to `epsg:4326`.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to `1024`.
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
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
            dst_crs = shape_crs

        # Get BBOX of the polygon
        bbox = featureBounds(shape)

        cutline = create_cutline(self.dataset, shape, geometry_crs=shape_crs)
        vrt_options = kwargs.pop("vrt_options", {})
        vrt_options.update({"cutline": cutline})

        data, mask = reader.part(
            self.dataset,
            bbox,
            max_size=max_size,
            bounds_crs=shape_crs,
            dst_crs=dst_crs,
            indexes=indexes,
            vrt_options=vrt_options,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        if dst_crs == shape_crs:
            bounds = bbox
        else:
            bounds = transform_bounds(shape_crs, dst_crs, *bbox, densify_pts=21)

        return ImageData(
            data, mask, bounds=bounds, crs=dst_crs, assets=[self.filepath],
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
            bounds=self.dataset.bounds,
            crs=self.dataset.crs,
            assets=[self.filepath],
        )


@attr.s
class GCPCOGReader(COGReader):
    """Custom COG Reader with GCPS support.

    Attributes:
        filepath (str): Cloud Optimized GeoTIFF path.
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

    filepath: str = attr.ib()
    src_dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None
    )
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)
    colormap: Dict = attr.ib(default=None)

    # Define global options to be forwarded to functions reading the data (e.g `rio_tiler.reader.read`)
    nodata: Optional[NoData] = attr.ib(default=None)
    unscale: Optional[bool] = attr.ib(default=None)
    resampling_method: Optional[Resampling] = attr.ib(default=None)
    vrt_options: Optional[Dict] = attr.ib(default=None)
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]]
    ] = attr.ib(default=None)

    # for GCPCOGReader, dataset is not a input option.
    dataset: WarpedVRT = attr.ib(init=False)

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        self.src_dataset = self.src_dataset or rasterio.open(self.filepath)
        self.dataset = WarpedVRT(
            self.src_dataset,
            src_crs=self.src_dataset.gcps[1],
            src_transform=transform.from_gcps(self.src_dataset.gcps[0]),
        )
        super().__attrs_post_init__()

    def close(self):
        """Close rasterio dataset."""
        self.dataset.close()
        if self.filepath:
            self.src_dataset.close()
