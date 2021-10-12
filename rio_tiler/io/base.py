"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
import asyncio
import re
import warnings
from typing import Any, Coroutine, Dict, List, Optional, Sequence, Tuple, Type, Union

import attr
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.warp import transform_bounds

from ..constants import WEB_MERCATOR_TMS, WGS84_CRS, BBox, Indexes
from ..errors import (
    ExpressionMixingWarning,
    MissingAssets,
    MissingBands,
    TileOutsideBounds,
)
from ..expression import apply_expression
from ..models import BandStatistics, ImageData, ImageStatistics, Info, Metadata
from ..tasks import multi_arrays, multi_values
from ..utils import get_array_statistics


@attr.s
class SpatialMixin:
    """Spatial Info Mixin.

    Attributes:
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int): Dataset Min Zoom level. **Not in __init__**.
        maxzoom (int): Dataset Max Zoom level. **Not in __init__**.
        bounds (tuple): Dataset bounds (left, bottom, right, top). **Not in __init__**.
        crs (rasterio.crs.CRS): Dataset crs. **Not in __init__**.

    """

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    @property
    def geographic_bounds(self) -> BBox:
        """return bounds in WGS84."""
        try:
            bounds = transform_bounds(
                self.crs, WGS84_CRS, *self.bounds, densify_pts=21,
            )
        except:  # noqa
            warnings.warn(
                "Cannot dertermine bounds in WGS84, will default to (-180.0, -90.0, 180.0, 90.0).",
                UserWarning,
            )
            bounds = (-180.0, -90, 180.0, 90)

        return bounds

    def tile_exists(self, tile_x: int, tile_y: int, tile_z: int) -> bool:
        """Check if a tile intersects the dataset bounds.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            bool: True if the tile intersects the dataset bounds.

        """
        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        try:
            dataset_bounds = transform_bounds(
                self.crs, self.tms.rasterio_crs, *self.bounds, densify_pts=21,
            )
        except:  # noqa
            # HACK: gdal will first throw an error for invalid transformation
            # but if retried it will then pass.
            # Note: It might return `+/-inf` values
            dataset_bounds = transform_bounds(
                self.crs, self.tms.rasterio_crs, *self.bounds, densify_pts=21,
            )

        return (
            (tile_bounds[0] < dataset_bounds[2])
            and (tile_bounds[2] > dataset_bounds[0])
            and (tile_bounds[3] > dataset_bounds[1])
            and (tile_bounds[1] < dataset_bounds[3])
        )


@attr.s
class BaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Rio-tiler.io BaseReader."""

    def __enter__(self):
        """Support using with Context Managers."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tile.models.Info: Dataset info.

        """
        ...

    @abc.abstractmethod
    def stats(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any,
    ) -> Dict[str, ImageStatistics]:
        """Return Dataset's statistics.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.

        Returns:
            rio_tile.models.ImageStatistics: Dataset statistics.

        """
        ...

    def metadata(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any,
    ) -> Metadata:
        """Return Dataset's statistics and info.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.

        Returns:
            rio_tile.models.Metadata: Dataset statistics and metadata.

        """
        warnings.warn(
            "Metadata method will be removed in rio-tiler v3.0.0", DeprecationWarning
        )

        info = self.info()
        stats = self.stats(pmin, pmax, **kwargs)
        return Metadata(statistics=stats, **info.dict())

    @abc.abstractmethod
    def statistics(self, **kwargs: Any) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        ...

    @abc.abstractmethod
    def tile(self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        ...

    @abc.abstractmethod
    def part(self, bbox: BBox, **kwargs: Any) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    def preview(self, **kwargs: Any) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    def point(self, lon: float, lat: float, **kwargs: Any) -> List:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latittude.

        Returns:
            list: Pixel value per bands/assets.

        """
        ...

    @abc.abstractmethod
    def feature(self, shape: Dict, **kwargs: Any) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...


@attr.s
class AsyncBaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Rio-tiler.io AsyncBaseReader."""

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    async def info(self) -> Coroutine[Any, Any, Info]:
        """Return Dataset's info.

        Returns:
            rio_tile.models.Info: Dataset info.

        """
        ...

    @abc.abstractmethod
    async def stats(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any
    ) -> Coroutine[Any, Any, Dict[str, ImageStatistics]]:
        """Return Dataset's statistics.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.

        Returns:
            rio_tile.models.ImageStatistics: Dataset statistics.

        """
        ...

    async def metadata(
        self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any,
    ) -> Coroutine[Any, Any, Metadata]:
        """Return Dataset's statistics and info.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.

        Returns:
            rio_tile.models.Metadata: Dataset statistics and metadata.

        """
        warnings.warn(
            "Metadata method will be removed in rio-tiler v3.0.0", DeprecationWarning
        )

        info, stats = await asyncio.gather(
            *[self.info(), self.stats(pmin, pmax, **kwargs)]
        )
        return Metadata(statistics=stats, **info.dict())

    @abc.abstractmethod
    async def statistics(
        self, **kwargs: Any,
    ) -> Coroutine[Any, Any, Dict[str, BandStatistics]]:
        """Return bands statistics from a dataset.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        ...

    @abc.abstractmethod
    async def tile(
        self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        ...

    @abc.abstractmethod
    async def part(self, bbox: BBox, **kwargs: Any) -> Coroutine[Any, Any, ImageData]:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def preview(self, **kwargs: Any) -> Coroutine[Any, Any, ImageData]:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def point(
        self, lon: float, lat: float, **kwargs: Any
    ) -> Coroutine[Any, Any, List]:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latittude.

        Returns:
            list: Pixel value per bands/assets.

        """
        ...

    @abc.abstractmethod
    async def feature(
        self, shape: Dict, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...


@attr.s
class MultiBaseReader(BaseReader, metaclass=abc.ABCMeta):
    """MultiBaseReader Reader.

    This Reader is suited for dataset that are composed of multiple assets (e.g. STAC).

    Attributes:
        reader (rio_tiler.io.BaseReader): reader.
        reader_options (dict, option): options to forward to the reader. Defaults to `{}`.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        assets (sequence): Asset list. **READ ONLY attribute**.

    """

    reader: Type[BaseReader] = attr.ib()
    reader_options: Dict = attr.ib(factory=dict)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    assets: Sequence[str] = attr.ib(init=False)

    @abc.abstractmethod
    def _get_asset_url(self, asset: str) -> str:
        """Validate asset name and construct url."""
        ...

    def parse_expression(self, expression: str) -> Tuple:
        """Parse rio-tiler band math expression."""
        assets = "|".join([fr"\b{asset}\b" for asset in self.assets])
        _re = re.compile(assets.replace("\\\\", "\\"))
        return tuple(set(re.findall(_re, expression)))

    def info(  # type: ignore
        self, assets: Union[Sequence[str], str] = None, **kwargs: Any
    ) -> Dict[str, Info]:
        """Return metadata from multiple assets.

        Args:
            assets (sequence of str or str, optional): assets to fetch info from. Required keyword argument.

        Returns:
            dict: Multiple assets info in form of {"asset1": rio_tile.models.Info}.

        """
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, **kwargs: Any) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.info()

        return multi_values(assets, _reader, **kwargs)

    def stats(  # type: ignore
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict[str, Dict[str, ImageStatistics]]:
        """Return array statistics from multiple assets.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.
            assets (sequence of str or str): assets to fetch info from. Required keyword argument.
            kwargs (optional): Options to forward to the `self.reader.stats` method.

        Returns:
            dict: Multiple assets statistics in form of {"asset1": rio_tile.models.ImageStatistics}.

        """
        warnings.warn(
            "`stats` method will be removed and replaced by `statistics` in rio-tiler v3.0.0",
            DeprecationWarning,
        )

        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.stats(*args, **kwargs)

        return multi_values(assets, _reader, pmin, pmax, **kwargs)

    def metadata(  # type: ignore
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict[str, Metadata]:
        """Return metadata from multiple assets.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.
            assets (sequence of str or str): assets to fetch info from. Required keyword argument.
            kwargs (optional): Options to forward to the `self.reader.metadata` method.

        Returns:
            dict: Multiple assets info and statistics in form of {"asset1": rio_tile.models.Metadata}.

        """
        warnings.warn(
            "Metadata method will be removed in rio-tiler v3.0.0", DeprecationWarning
        )

        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.metadata(*args, **kwargs)

        return multi_values(assets, _reader, pmin, pmax, **kwargs)

    def statistics(  # type: ignore
        self,
        assets: Union[Sequence[str], str] = None,
        indexes: Optional[Indexes] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> Dict[str, Dict[str, BandStatistics]]:
        """Return array statistics for multiple assets.

        Args:
            assets (sequence of str or str): assets to fetch info from.
            indexes (int or sequence of int, optional): Band indexes.
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.statistics` method.

        Returns:
            dict: Multiple assets statistics in form of {"asset1": {"1": rio_tiler.models.BandStatistics, ...}}.

        """
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.statistics(*args, **kwargs)

        return multi_values(
            assets, _reader, indexes=indexes, expression=asset_expression, **kwargs,
        )

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge Wep Map tiles from multiple assets.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.tile` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside image bounds"
            )

        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.tile(*args, **kwargs)
                data.band_names = [f"{asset}_{n}" for n in data.band_names]
                return data

        output = multi_arrays(
            assets,
            _reader,
            tile_x,
            tile_y,
            tile_z,
            expression=asset_expression,
            **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)
            output.band_names = blocks

        return output

    def part(
        self,
        bbox: BBox,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts from multiple assets.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.part` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.part(*args, **kwargs)
                data.band_names = [f"{asset}_{n}" for n in data.band_names]
                return data

        output = multi_arrays(
            assets, _reader, bbox, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)
            output.band_names = blocks

        return output

    def preview(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge previews from multiple assets.

        Args:
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.preview` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, **kwargs: Any) -> ImageData:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.preview(**kwargs)
                data.band_names = [f"{asset}_{n}" for n in data.band_names]
                return data

        output = multi_arrays(assets, _reader, expression=asset_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)
            output.band_names = blocks

        return output

    def point(
        self,
        lon: float,
        lat: float,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> List:
        """Read pixel value from multiple assets.

        Args:
            lon (float): Longitude.
            lat (float): Latittude.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.point` method.

        Returns:
            list: Pixel values per assets.

        """
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, *args, **kwargs: Any) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.point(*args, **kwargs)

        data = multi_values(
            assets, _reader, lon, lat, expression=asset_expression, **kwargs,
        )

        values = [d for _, d in data.items()]
        if expression:
            blocks = expression.split(",")
            values = apply_expression(blocks, assets, values).tolist()

        return values

    def feature(
        self,
        shape: Dict,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts defined by geojson feature from multiple assets.

        Args:
            shape (dict): Valid GeoJSON feature.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_expression (str, optional): rio-tiler expression for each asset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.feature` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.feature(*args, **kwargs)
                data.band_names = [f"{asset}_{n}" for n in data.band_names]
                return data

        output = multi_arrays(
            assets, _reader, shape, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)
            output.band_names = blocks

        return output


@attr.s
class MultiBandReader(BaseReader, metaclass=abc.ABCMeta):
    """Multi Band Reader.

    This Reader is suited for dataset that stores spectral bands as separate files  (e.g. Sentinel 2).

    Attributes:
        reader (rio_tiler.io.BaseReader): reader.
        reader_options (dict, option): options to forward to the reader. Defaults to `{}`.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        bands (sequence): Band list. **READ ONLY attribute**.

    """

    reader: Type[BaseReader] = attr.ib()
    reader_options: Dict = attr.ib(factory=dict)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    bands: Sequence[str] = attr.ib(init=False)

    @abc.abstractmethod
    def _get_band_url(self, band: str) -> str:
        """Validate band name and construct url."""
        ...

    def parse_expression(self, expression: str) -> Tuple:
        """Parse rio-tiler band math expression."""
        bands = "|".join([fr"\b{band}\b" for band in self.bands])
        _re = re.compile(bands.replace("\\\\", "\\"))
        return tuple(set(re.findall(_re, expression)))

    def info(
        self, bands: Union[Sequence[str], str] = None, *args, **kwargs: Any
    ) -> Info:
        """Return metadata from multiple bands.

        Args:
            bands (sequence of str or str, optional): band names to fetch info from. Required keyword argument.

        Returns:
            dict: Multiple bands info in form of {"band1": rio_tile.models.Info}.

        """
        if not bands:
            raise MissingBands("Missing 'bands' option")

        if isinstance(bands, str):
            bands = (bands,)

        def _reader(band: str, **kwargs: Any) -> Info:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.info()

        bands_metadata = multi_values(bands, _reader, *args, **kwargs)

        meta = {
            "bounds": self.geographic_bounds,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
        }

        # We only keep the value for the first band.
        meta["band_metadata"] = [
            (band, bands_metadata[band].band_metadata[0][1])
            for ix, band in enumerate(bands)
        ]
        meta["band_descriptions"] = [
            (band, bands_metadata[band].band_descriptions[0][1])
            for ix, band in enumerate(bands)
        ]
        meta["dtype"] = bands_metadata[bands[0]].dtype
        meta["colorinterp"] = [
            bands_metadata[band].colorinterp[0] for _, band in enumerate(bands)
        ]
        meta["nodata_type"] = bands_metadata[bands[0]].nodata_type
        return Info(**meta)

    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        bands: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict[str, ImageStatistics]:
        """Return array statistics from multiple bands.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.
            bands (sequence of str or str): bands to fetch info from. Required keyword argument.
            kwargs (optional): Options to forward to the `self.reader.stats` method.

        Returns:
            dict: Multiple bands statistics in form of {"band1": rio_tile.models.ImageStatistics}.

        """
        warnings.warn(
            "`stats` method will be removed and replaced by `statistics` in rio-tiler v3.0.0",
            DeprecationWarning,
        )

        if not bands:
            raise MissingBands("Missing 'bands' option")

        if isinstance(bands, str):
            bands = (bands,)

        def _reader(band: str, *args, **kwargs) -> Dict:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                # We only return statistics for Band `1` of each dataset.
                stats = cog.stats(*args, **kwargs)
                return stats.get(list(stats)[0])

        return multi_values(bands, _reader, pmin, pmax, **kwargs)

    def metadata(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        bands: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Metadata:
        """Return metadata from multiple bands.

        Args:
            pmin (float, optional): Histogram minimum cut. Defaults to `2.0`.
            pmax (float, optional): Histogram maximum cut. Defaults to `98.0`.
            bands (sequence of str or str): bands to fetch info from. Required keyword argument.
            kwargs (optional): Options to forward to the `self.reader.stats` method.

        Returns:
            dict: Multiple bands info an statistics in form of {"band1": rio_tile.models.Metadata}.

        """
        warnings.warn(
            "Metadata method will be removed in rio-tiler v3.0.0", DeprecationWarning
        )

        if not bands:
            raise MissingBands("Missing 'bands' option")

        if isinstance(bands, str):
            bands = (bands,)

        def _reader(band: str, *args, **kwargs) -> Metadata:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.metadata(*args, **kwargs)

        bands_metadata = multi_values(bands, _reader, pmin, pmax, **kwargs)

        meta = {
            "bounds": self.geographic_bounds,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
        }
        meta["band_metadata"] = [
            (band, bands_metadata[band].band_metadata[0][1])
            for ix, band in enumerate(bands)
        ]
        meta["band_descriptions"] = [
            (band, bands_metadata[band].band_descriptions[0][1])
            for ix, band in enumerate(bands)
        ]
        meta["dtype"] = bands_metadata[bands[0]].dtype
        meta["colorinterp"] = [
            bands_metadata[band].colorinterp[0] for _, band in enumerate(bands)
        ]
        meta["nodata_type"] = bands_metadata[bands[0]].nodata_type
        meta["statistics"] = {
            # We only keep statistics for Band `1` of each dataset.
            band: bands_metadata[band].statistics.get(
                list(bands_metadata[band].statistics)[0]
            )
            for _, band in enumerate(bands)
        }
        return Metadata(**meta)

    def statistics(
        self,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: List[int] = [2, 98],
        hist_options: Optional[Dict] = None,
        max_size: int = 1024,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return array statistics for multiple assets.

        Args:
            bands (sequence of str or str): bands to fetch info from. Required keyword argument.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band dataset (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.statistics` method.

        Returns:
            dict: Multiple assets statistics in form of {"1": rio_tiler.models.BandStatistics, ...}.

        """
        data = self.preview(
            bands=bands,
            expression=expression,
            band_expression=band_expression,
            max_size=max_size,
            **kwargs,
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
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge Web Map tiles multiple bands.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.tile` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside image bounds"
            )

        if isinstance(bands, str):
            bands = (bands,)

        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands:
            raise MissingBands(
                "bands must be passed either via expression or bands options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.tile(*args, **kwargs)
                data.band_names = [band]
                return data

        output = multi_arrays(
            bands,
            _reader,
            tile_x,
            tile_y,
            tile_z,
            expression=band_expression,
            **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)
            output.band_names = blocks

        return output

    def part(
        self,
        bbox: BBox,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts from multiple bands.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the 'self.reader.part' method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(bands, str):
            bands = (bands,)

        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands:
            raise MissingBands(
                "bands must be passed either via expression or bands options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.part(*args, **kwargs)
                data.band_names = [band]
                return data

        output = multi_arrays(
            bands, _reader, bbox, expression=band_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)
            output.band_names = blocks

        return output

    def preview(
        self,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge previews from multiple bands.

        Args:
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.preview` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(bands, str):
            bands = (bands,)

        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands:
            raise MissingBands(
                "bands must be passed either via expression or bands options."
            )

        def _reader(band: str, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.preview(**kwargs)
                data.band_names = [band]
                return data

        output = multi_arrays(bands, _reader, expression=band_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)
            output.band_names = blocks

        return output

    def point(
        self,
        lon: float,
        lat: float,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        **kwargs: Any,
    ) -> List:
        """Read a pixel values from multiple bands.

        Args:
            lon (float): Longitude.
            lat (float): Latittude.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.point` method.

        Returns:
            list: Pixel value per bands.

        """
        if isinstance(bands, str):
            bands = (bands,)

        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands:
            raise MissingBands(
                "bands must be passed either via expression or bands options."
            )

        def _reader(band: str, *args, **kwargs: Any) -> Dict:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.point(*args, **kwargs)[0]  # We only return the firt value

        data = multi_values(
            bands, _reader, lon, lat, expression=band_expression, **kwargs,
        )

        values = [d for _, d in data.items()]
        if expression:
            blocks = expression.split(",")
            values = apply_expression(blocks, bands, values).tolist()

        return values

    def feature(
        self,
        shape: Dict,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band dataset based on band indexes
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts defined by geojson feature from multiple bands.

        Args:
            shape (dict): Valid GeoJSON feature.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            band_expression (str, optional): rio-tiler expression for each band (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.feature` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if isinstance(bands, str):
            bands = (bands,)

        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands:
            raise MissingBands(
                "bands must be passed either via expression or bands options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                data = cog.feature(*args, **kwargs)
                data.band_names = [band]
                return data

        output = multi_arrays(
            bands, _reader, shape, expression=band_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)
            output.band_names = blocks

        return output
