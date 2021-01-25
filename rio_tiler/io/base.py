"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
import asyncio
import re
import warnings
from typing import Any, Coroutine, Dict, List, Optional, Sequence, Tuple, Type, Union

import attr
from morecantile import Tile, TileMatrixSet

from ..constants import WEB_MERCATOR_TMS
from ..errors import (
    ExpressionMixingWarning,
    MissingAssets,
    MissingBands,
    TileOutsideBounds,
)
from ..expression import apply_expression
from ..models import ImageData, ImageStatistics, Info, Metadata, SpatialInfo
from ..tasks import multi_arrays, multi_values


@attr.s
class SpatialMixin:
    """Spatial Info Mixin.

    Attributes:
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        bbox (tuple): Dataset bounds (left, bottom, right, top). **READ ONLY attribute**.
        minzoom (int): Overwrite Min Zoom level. **READ ONLY attribute**.
        maxzoom (int): Overwrite Max Zoom level. **READ ONLY attribute**.

    """

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    bounds: Tuple[float, float, float, float] = attr.ib(init=False)
    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    @property
    def center(self) -> Tuple[float, float, int]:
        """Dataset center + minzoom."""
        return (
            (self.bounds[0] + self.bounds[2]) / 2,
            (self.bounds[1] + self.bounds[3]) / 2,
            self.minzoom,
        )

    @property
    def spatial_info(self) -> SpatialInfo:
        """Return Dataset's spatial info."""
        return SpatialInfo(
            bounds=self.bounds,
            center=self.center,
            minzoom=self.minzoom,
            maxzoom=self.maxzoom,
        )

    def tile_exists(self, tile_z: int, tile_x: int, tile_y: int) -> bool:
        """Check if a tile is intersets the dataset bounds.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            bool: True if the tile is intersets the dataset bounds.

        """
        tile = Tile(x=tile_x, y=tile_y, z=tile_z)
        tile_bounds = self.tms.bounds(*tile)
        return (
            (tile_bounds[0] < self.bounds[2])
            and (tile_bounds[2] > self.bounds[0])
            and (tile_bounds[3] > self.bounds[1])
            and (tile_bounds[1] < self.bounds[3])
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
        info = self.info()
        stats = self.stats(pmin, pmax, **kwargs)
        return Metadata(statistics=stats, **info.dict())

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
    def part(self, bbox: Tuple[float, float, float, float], **kwargs: Any) -> ImageData:
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
        info, stats = await asyncio.gather(
            *[self.info(), self.stats(pmin, pmax, **kwargs)]
        )
        return Metadata(statistics=stats, **info.dict())

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
    async def part(
        self, bbox: Tuple[float, float, float, float], **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
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
        self, assets: Union[Sequence[str], str] = None, *args, **kwargs: Any
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

        return multi_values(assets, _reader, *args, **kwargs)

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
        if not assets:
            raise MissingAssets("Missing 'assets' option")

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, *args, **kwargs) -> Dict:
            url = self._get_asset_url(asset)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.metadata(*args, **kwargs)

        return multi_values(assets, _reader, pmin, pmax, **kwargs)

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on index names
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
        if not self.tile_exists(tile_z, tile_x, tile_y):
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
                return cog.tile(*args, **kwargs)

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

        return output

    def part(
        self,
        bbox: Tuple[float, float, float, float],
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on index names
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
                return cog.part(*args, **kwargs)

        output = multi_arrays(
            assets, _reader, bbox, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)

        return output

    def preview(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on index names
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
                return cog.preview(**kwargs)

        output = multi_arrays(assets, _reader, expression=asset_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)

        return output

    def point(
        self,
        lon: float,
        lat: float,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_expression: Optional[
            str
        ] = None,  # Expression for each asset based on index names
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
        ] = None,  # Expression for each asset based on index names
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
                return cog.feature(*args, **kwargs)

        output = multi_arrays(
            assets, _reader, shape, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, assets, output.data)

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

        meta = self.spatial_info.dict()

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
        if not bands:
            raise MissingBands("Missing 'bands' option")

        if isinstance(bands, str):
            bands = (bands,)

        def _reader(band: str, *args, **kwargs) -> Metadata:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as cog:  # type: ignore
                return cog.metadata(*args, **kwargs)

        bands_metadata = multi_values(bands, _reader, pmin, pmax, **kwargs)

        meta = self.spatial_info.dict()
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

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band based on index names
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
        if not self.tile_exists(tile_z, tile_x, tile_y):
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
                return cog.tile(*args, **kwargs)

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

        return output

    def part(
        self,
        bbox: Tuple[float, float, float, float],
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band based on index names
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
                return cog.part(*args, **kwargs)

        output = multi_arrays(
            bands, _reader, bbox, expression=band_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)

        return output

    def preview(
        self,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band based on index names
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
                return cog.preview(**kwargs)

        output = multi_arrays(bands, _reader, expression=band_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)

        return output

    def point(
        self,
        lon: float,
        lat: float,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        band_expression: Optional[
            str
        ] = None,  # Expression for each band based on index names (b1, b2, ...)
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
        ] = None,  # Expression for each band based on index names
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
                return cog.feature(*args, **kwargs)

        output = multi_arrays(
            bands, _reader, shape, expression=band_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            output.data = apply_expression(blocks, bands, output.data)

        return output
