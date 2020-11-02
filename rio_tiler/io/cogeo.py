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
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform, transform_bounds

from .. import constants, reader
from ..errors import ExpressionMixingWarning, TileOutsideBounds
from ..expression import apply_expression, parse_expression
from ..models import ImageData, ImageStatistics, Info
from ..utils import has_alpha_band, has_mask_band
from .base import BaseReader


@attr.s
class COGReader(BaseReader):
    """
    Cloud Optimized GeoTIFF Reader.

    Examples
    --------
    with COGReader(src_path) as cog:
        cog.tile(...)

    # Set global options
    with COGReader(src_path, unscale=True, nodata=0) as cog:
        cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with WarpedVRT(src_dst, ...) as vrt_dst:
            with COGReader(None, dataset=vrt_dst) as cog:
                cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with COGReader(None, dataset=src_dst) as cog:
            cog.tile(...)

    Attributes
    ----------
    filepath: str
        Cloud Optimized GeoTIFF path.
    dataset: rasterio.DatasetReader, optional
        Rasterio dataset.

    Properties
    ----------
    minzoom: int
        COG minimum zoom level.
    maxzoom: int
        COG maximum zoom level.
    bounds: tuple[float]
        COG bounds in WGS84 crs.
    center: tuple[float, float, int]
        COG center + minzoom
    colormap: dict
        COG internal colormap.
    info: dict
        General information about the COG (datatype, indexes, ...)

    Methods
    -------
    tile(0, 0, 0, indexes=(1,2,3), expression="B1/B2", tilesize=512, resampling_methods="nearest")
        Read a map tile from the COG.
    part((0,10,0,10), indexes=(1,2,3,), expression="B1/B20", max_size=1024)
        Read part of the COG.
    preview(max_size=1024)
        Read preview of the COG.
    point((10, 10), indexes=1)
        Read a point value from the COG.
    stats(pmin=5, pmax=95)
        Get Raster statistics.
    meta(pmin=5, pmax=95)
        Get info + raster statistics

    """

    filepath: str = attr.ib()
    dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None
    )
    tms: TileMatrixSet = attr.ib(default=constants.WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)
    colormap: Dict = attr.ib(default=None)

    # Define global options to be forwarded to functions reading the data (e.g rio_tiler.reader._read)
    nodata: Optional[Union[float, int, str]] = attr.ib(default=None)
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
            self.dataset.crs, constants.WGS84_CRS, *self.dataset.bounds, densify_pts=21
        )
        if self.minzoom is None or self.maxzoom is None:
            self._set_zooms()

        if self.colormap is None:
            self._get_colormap()

    def close(self):
        """Close rasterio dataset."""
        if self.filepath:
            self.dataset.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    def get_zooms(self, tilesize: int = 256) -> Tuple[int, int]:
        """Calculate raster min/max zoom level."""
        dst_affine, w, h = calculate_default_transform(
            self.dataset.crs,
            self.tms.crs,
            self.dataset.width,
            self.dataset.height,
            *self.dataset.bounds,
        )
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

        indexes = self.dataset.indexes
        band_descr = [(f"{ix}", _get_descr(ix)) for ix in indexes]
        band_meta = [(f"{ix}", self.dataset.tags(ix)) for ix in indexes]
        colorinterp = [self.dataset.colorinterp[ix - 1].name for ix in indexes]

        if has_alpha_band(self.dataset):
            nodata_type = "Alpha"
        elif has_mask_band(self.dataset):
            nodata_type = "Mask"
        elif self.nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        other_meta = {}
        if self.dataset.scales[0] and self.dataset.offsets[0]:
            other_meta.update(
                {"scale": self.dataset.scales[0], "offset": self.dataset.offsets[0]}
            )

        if self.colormap:
            other_meta.update({"colormap": self.colormap})

        meta = {
            "bounds": self.bounds,
            "center": self.center,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
            "band_metadata": band_meta,
            "band_descriptions": band_descr,
            "dtype": self.dataset.meta["dtype"],
            "colorinterp": colorinterp,
            "nodata_type": nodata_type,
        }
        meta.update(**other_meta)
        return Info(**meta)

    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        hist_options: Optional[Dict] = None,
        **kwargs: Any,
    ) -> Dict[str, ImageStatistics]:
        """
        Return bands statistics from a COG.

        Attributes
        ----------
        pmin: float, optional, (default: 2)
            Histogram minimum cut.
        pmax: float, optional, (default: 98)
            Histogram maximum cut.
        hist_options: dict, optional
            Options to forward to numpy.histogram function.
            e.g: {bins=20, range=(0, 1000)}
        kwargs: optional
            These are passed to 'rio_tiler.reader.stats'

        Returns
        -------
        out: dict
            Dictionary with bands statistics.

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
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = "",
        **kwargs: Any,
    ) -> ImageData:
        """
        Read a Mercator Map tile from a COG.

        Attributes
        ----------
        tile_x: int
            Mercator tile X index.
        tile_y: int
            Mercator tile Y index.
        tile_z: int
            Mercator tile ZOOM level.
        tilesize: int, optional (default: 256)
            Output image size.
        indexes: int or sequence of int
            Band indexes (e.g. 1 or (1, 2, 3))
        expression: str
            rio-tiler expression (e.g. b1/b2+b3)
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.part' function.

        Returns
        -------
        data: numpy ndarray
        mask: numpy array

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
        bbox: Tuple[float, float, float, float],
        dst_crs: Optional[CRS] = None,
        bounds_crs: CRS = constants.WGS84_CRS,
        max_size: int = 1024,
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = "",
        **kwargs: Any,
    ) -> ImageData:
        """
        Read part of a COG.

        Attributes
        ----------
        bbox: tuple
            bounds to read (left, bottom, right, top) in "bounds_crs".
        dst_crs: CRS or str, optional
            Target coordinate reference system, default is the bbox CRS.
        bounds_crs: CRS or str, optional
            bounds coordinate reference system, default is "epsg:4326"
        max_size: int, optional
            Limit output size array, default is 1024.
        indexes: int or sequence of int
            Band indexes (e.g. 1 or (1, 2, 3))
        expression: str
            rio-tiler expression (e.g. b1/b2+b3)
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.part' function.

        Returns
        -------
        data: numpy ndarray
        mask: numpy array

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
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = "",
        **kwargs: Any,
    ) -> ImageData:
        """
        Return a preview of a COG.

        Attributes
        ----------
        indexes: int or sequence of int
            Band indexes (e.g. 1 or (1, 2, 3))
        expression: str
            rio-tiler expression (e.g. b1/b2+b3)
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.preview' function.

        Returns
        -------
        data: numpy ndarray
        mask: numpy array

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
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = "",
        **kwargs: Any,
    ) -> List:
        """
        Read a value from a COG.

        Attributes
        ----------
        address: str
            file url.
        lon: float
            Longitude
        lat: float
            Latittude.
        indexes: int or sequence of int
            Band indexes (e.g. 1 or (1, 2, 3))
        expression: str
            rio-tiler expression (e.g. b1/b2+b3)
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.point' function.

        Returns
        -------
        point: list
            List of pixel values per bands indexes.

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


@attr.s
class GCPCOGReader(COGReader):
    """Custom COG Reader with GCPS support.

    Attributes:
        src_dataset (DatasetReader): rasterio openned dataset.
        dataset (WarpedVRT): rasterio WarpedVRT dataset.

    """

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

        self.src_dataset = rasterio.open(self.filepath)
        self.dataset = WarpedVRT(
            self.src_dataset,
            src_crs=self.src_dataset.gcps[1],
            src_transform=transform.from_gcps(self.src_dataset.gcps[0]),
        )

        self.nodata = self.nodata if self.nodata is not None else self.dataset.nodata

        self.bounds = transform_bounds(
            self.dataset.crs, constants.WGS84_CRS, *self.dataset.bounds, densify_pts=21
        )

        if self.minzoom is None or self.maxzoom is None:
            self._set_zooms()

        if self.colormap is None:
            self._get_colormap()

        return self

    def close(self):
        """Close rasterio dataset."""
        self.dataset.close()
        self.src_dataset.close()
