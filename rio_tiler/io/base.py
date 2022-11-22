"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
import contextlib
import re
import warnings
from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, Union

import attr
import numpy
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.warp import transform_bounds

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    AssetAsBandError,
    ExpressionMixingWarning,
    MissingAssets,
    MissingBands,
    TileOutsideBounds,
)
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.tasks import multi_arrays, multi_points, multi_values
from rio_tiler.types import AssetInfo, BBox, Indexes
from rio_tiler.utils import get_array_statistics, normalize_bounds


@attr.s
class SpatialMixin:
    """Spatial Info Mixin.

    Attributes:
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.

    """

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    geographic_crs: CRS = attr.ib(init=False, default=WGS84_CRS)

    @property
    def geographic_bounds(self) -> BBox:
        """Return dataset bounds in geographic_crs."""
        if self.crs == self.geographic_crs:
            return self.bounds

        try:
            bounds = transform_bounds(
                self.crs,
                self.geographic_crs,
                *self.bounds,
                densify_pts=21,
            )
        except:  # noqa
            warnings.warn(
                "Cannot determine bounds in geographic CRS, will default to (-180.0, -90.0, 180.0, 90.0).",
                UserWarning,
            )
            bounds = (-180.0, -90, 180.0, 90)

        if not all(numpy.isfinite(bounds)):
            warnings.warn(
                "Transformation to geographic CRS returned invalid values, will default to (-180.0, -90.0, 180.0, 90.0).",
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
        # bounds in TileMatrixSet's CRS
        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        if not self.tms.rasterio_crs == self.crs:
            # Transform the bounds to the dataset's CRS
            try:
                tile_bounds = transform_bounds(
                    self.tms.rasterio_crs,
                    self.crs,
                    *tile_bounds,
                    densify_pts=21,
                )
            except:  # noqa
                # HACK: gdal will first throw an error for invalid transformation
                # but if retried it will then pass.
                # Note: It might return `+/-inf` values
                tile_bounds = transform_bounds(
                    self.tms.rasterio_crs,
                    self.crs,
                    *tile_bounds,
                    densify_pts=21,
                )

        # If tile_bounds has non-finite value in the dataset CRS we return True
        if not all(numpy.isfinite(tile_bounds)):
            return True

        tile_bounds = normalize_bounds(tile_bounds)
        dst_bounds = normalize_bounds(self.bounds)

        return (
            (tile_bounds[0] < dst_bounds[2])
            and (tile_bounds[2] > dst_bounds[0])
            and (tile_bounds[3] > dst_bounds[1])
            and (tile_bounds[1] < dst_bounds[3])
        )


@attr.s
class BaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Rio-tiler.io BaseReader.

    Attributes:
        input (any): Reader's input.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.

    """

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

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
    def statistics(self) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        ...

    @abc.abstractmethod
    def tile(self, tile_x: int, tile_y: int, tile_z: int) -> ImageData:
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
    def part(self, bbox: BBox) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    def preview(self) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    def point(self, lon: float, lat: float) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            rio_tiler.models.PointData: PointData instance with data, mask and spatial info.

        """
        ...

    @abc.abstractmethod
    def feature(self, shape: Dict) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...


@attr.s
class MultiBaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """MultiBaseReader Reader.

    This Abstract Base Class Reader is suited for dataset that are composed of multiple assets (e.g. STAC).

    Attributes:
        input (any): input data.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set dataset's minzoom.
        maxzoom (int, optional): Set dataset's maxzoom.
        reader_options (dict, option): options to forward to the reader. Defaults to `{}`.

    """

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    reader: Type[BaseReader] = attr.ib(init=False)
    reader_options: Dict = attr.ib(factory=dict)

    assets: Sequence[str] = attr.ib(init=False)

    ctx: Any = attr.ib(init=False, default=contextlib.nullcontext)

    def __enter__(self):
        """Support using with Context Managers."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    def _get_asset_info(self, asset: str) -> AssetInfo:
        """Validate asset name and construct url."""
        ...

    def parse_expression(self, expression: str, asset_as_band: bool = False) -> Tuple:
        """Parse rio-tiler band math expression."""
        assets = "|".join(self.assets)
        if asset_as_band:
            _re = re.compile(rf"\b({assets})\b")
        else:
            _re = re.compile(rf"\b({assets})_b\d+\b")
        return tuple(set(re.findall(_re, expression)))

    def info(
        self, assets: Union[Sequence[str], str] = None, **kwargs: Any
    ) -> Dict[str, Info]:
        """Return metadata from multiple assets.

        Args:
            assets (sequence of str or str, optional): assets to fetch info from. Required keyword argument.

        Returns:
            dict: Multiple assets info in form of {"asset1": rio_tile.models.Info}.

        """
        if not assets:
            warnings.warn(
                "No `assets` option passed, will fetch info for all available assets.",
                UserWarning,
            )

        assets = assets or self.assets

        if isinstance(assets, str):
            assets = (assets,)

        def _reader(asset: str, **kwargs: Any) -> Dict:
            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    return src.info()

        return multi_values(assets, _reader, **kwargs)

    def statistics(
        self,
        assets: Union[Sequence[str], str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_expression: Optional[Dict[str, str]] = None,  # Expression for each asset
        **kwargs: Any,
    ) -> Dict[str, Dict[str, BandStatistics]]:
        """Return array statistics for multiple assets.

        Args:
            assets (sequence of str or str): assets to fetch info from.
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
            asset_expression (dict, optional): rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}).
            kwargs (optional): Options to forward to the `self.reader.statistics` method.

        Returns:
            dict: Multiple assets statistics in form of {"asset1": {"1": rio_tiler.models.BandStatistics, ...}}.

        """
        if not assets:
            warnings.warn(
                "No `assets` option passed, will fetch statistics for all available assets.",
                UserWarning,
            )

        assets = assets or self.assets

        if isinstance(assets, str):
            assets = (assets,)

        asset_indexes = asset_indexes or {}
        asset_expression = asset_expression or {}

        def _reader(asset: str, *args, **kwargs) -> Dict:
            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    return src.statistics(
                        *args,
                        indexes=asset_indexes.get(asset, kwargs.pop("indexes", None)),  # type: ignore
                        expression=asset_expression.get(asset),  # type: ignore
                        **kwargs,
                    )

        return multi_values(assets, _reader, **kwargs)

    def merged_statistics(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: List[int] = [2, 98],
        hist_options: Optional[Dict] = None,
        max_size: int = 1024,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return array statistics for multiple assets.

        Args:
            assets (sequence of str or str): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            kwargs (optional): Options to forward to the `self.preview` method.


        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        if not expression:
            if not assets:
                warnings.warn(
                    "No `assets` option passed, will fetch statistics for all available assets.",
                    UserWarning,
                )
            assets = assets or self.assets

        data = self.preview(
            assets=assets,
            expression=expression,
            asset_indexes=asset_indexes,
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
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_as_band: bool = False,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge Wep Map tiles from multiple assets.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
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
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_indexes = asset_indexes or {}

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or kwargs.pop("indexes", None)  # type: ignore

            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    data = src.tile(*args, indexes=idx, **kwargs)
                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use asset_as_band for multibands asset"
                            )
                        data.band_names = [asset]
                    else:
                        data.band_names = [f"{asset}_{n}" for n in data.band_names]

                    return data

        img = multi_arrays(assets, _reader, tile_x, tile_y, tile_z, **kwargs)
        if expression:
            return img.apply_expression(expression)

        return img

    def part(
        self,
        bbox: BBox,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_as_band: bool = False,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts from multiple assets.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
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
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_indexes = asset_indexes or {}

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or kwargs.pop("indexes", None)  # type: ignore

            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    data = src.part(*args, indexes=idx, **kwargs)
                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use asset_as_band for multibands asset"
                            )
                        data.band_names = [asset]
                    else:
                        data.band_names = [f"{asset}_{n}" for n in data.band_names]

                    return data

        img = multi_arrays(assets, _reader, bbox, **kwargs)
        if expression:
            return img.apply_expression(expression)

        return img

    def preview(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_as_band: bool = False,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge previews from multiple assets.

        Args:
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
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
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_indexes = asset_indexes or {}

        def _reader(asset: str, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or kwargs.pop("indexes", None)  # type: ignore

            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    data = src.preview(indexes=idx, **kwargs)
                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use asset_as_band for multibands asset"
                            )
                        data.band_names = [asset]
                    else:
                        data.band_names = [f"{asset}_{n}" for n in data.band_names]

                    return data

        img = multi_arrays(assets, _reader, **kwargs)
        if expression:
            return img.apply_expression(expression)

        return img

    def point(
        self,
        lon: float,
        lat: float,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_as_band: bool = False,
        **kwargs: Any,
    ) -> PointData:
        """Read pixel value from multiple assets.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
            kwargs (optional): Options to forward to the `self.reader.point` method.

        Returns:
            PointData

        """
        if isinstance(assets, str):
            assets = (assets,)

        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_indexes = asset_indexes or {}

        def _reader(asset: str, *args, **kwargs: Any) -> PointData:
            idx = asset_indexes.get(asset) or kwargs.pop("indexes", None)  # type: ignore

            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    data = src.point(*args, indexes=idx, **kwargs)
                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use asset_as_band for multibands asset"
                            )
                        data.band_names = [asset]
                    else:
                        data.band_names = [f"{asset}_{n}" for n in data.band_names]

                    return data

        data = multi_points(assets, _reader, lon, lat, **kwargs)
        if expression:
            return data.apply_expression(expression)

        return data

    def feature(
        self,
        shape: Dict,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,  # Indexes for each asset
        asset_as_band: bool = False,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts defined by geojson feature from multiple assets.

        Args:
            shape (dict): Valid GeoJSON feature.
            assets (sequence of str or str, optional): assets to fetch info from.
            expression (str, optional): rio-tiler expression for the asset list (e.g. asset1/asset2+asset3).
            asset_indexes (dict, optional): Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}).
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
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_indexes = asset_indexes or {}

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or kwargs.pop("indexes", None)  # type: ignore

            asset_meta = self._get_asset_info(asset)
            url = asset_meta["url"]
            with self.ctx(**asset_meta.get("env", {})):
                with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                    data = src.feature(*args, indexes=idx, **kwargs)
                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use asset_as_band for multibands asset"
                            )
                        data.band_names = [asset]
                    else:
                        data.band_names = [f"{asset}_{n}" for n in data.band_names]

                    return data

        img = multi_arrays(assets, _reader, shape, **kwargs)
        if expression:
            return img.apply_expression(expression)

        return img


@attr.s
class MultiBandReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Multi Band Reader.

    This Abstract Base Class Reader is suited for dataset that stores spectral bands as separate files  (e.g. Sentinel 2).

    Attributes:
        input (any): input data.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set dataset's minzoom.
        maxzoom (int, optional): Set dataset's maxzoom.
        reader_options (dict, option): options to forward to the reader. Defaults to `{}`.

    """

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    reader: Type[BaseReader] = attr.ib(init=False)
    reader_options: Dict = attr.ib(factory=dict)

    bands: Sequence[str] = attr.ib(init=False)

    def __enter__(self):
        """Support using with Context Managers."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    def _get_band_url(self, band: str) -> str:
        """Validate band name and construct url."""
        ...

    def parse_expression(self, expression: str) -> Tuple:
        """Parse rio-tiler band math expression."""
        bands = "|".join([rf"\b{band}\b" for band in self.bands])
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
            warnings.warn(
                "No `bands` option passed, will fetch info for all available bands.",
                UserWarning,
            )

        bands = bands or self.bands

        if isinstance(bands, str):
            bands = (bands,)

        def _reader(band: str, **kwargs: Any) -> Info:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                return src.info()

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

    def statistics(
        self,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
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
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            kwargs (optional): Options to forward to the `self.preview` method.

        Returns:
            dict: Multiple assets statistics in form of {"{band}/{expression}": rio_tiler.models.BandStatistics, ...}.

        """
        if not expression:
            if not bands:
                warnings.warn(
                    "No `bands` option passed, will fetch statistics for all available bands.",
                    UserWarning,
                )
            bands = bands or self.bands

        data = self.preview(
            bands=bands,
            expression=expression,
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
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge Web Map tiles multiple bands.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
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
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                data = src.tile(*args, **kwargs)
                data.band_names = [band]  # use `band` as name instead of band index
                return data

        img = multi_arrays(bands, _reader, tile_x, tile_y, tile_z, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def part(
        self,
        bbox: BBox,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts from multiple bands.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
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
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                data = src.part(*args, **kwargs)
                data.band_names = [band]  # use `band` as name instead of band index
                return data

        img = multi_arrays(bands, _reader, bbox, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def preview(
        self,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge previews from multiple bands.

        Args:
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
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
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                data = src.preview(**kwargs)
                data.band_names = [band]  # use `band` as name instead of band index
                return data

        img = multi_arrays(bands, _reader, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def point(
        self,
        lon: float,
        lat: float,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a pixel values from multiple bands.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
            kwargs (optional): Options to forward to the `self.reader.point` method.

        Returns:
            PointData

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

        def _reader(band: str, *args, **kwargs: Any) -> PointData:
            url = self._get_band_url(band)
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                data = src.point(*args, **kwargs)
                data.band_names = [band]  # use `band` as name instead of band index
                return data

        data = multi_points(bands, _reader, lon, lat, **kwargs)
        if expression:
            return data.apply_expression(expression)

        return data

    def feature(
        self,
        shape: Dict,
        bands: Union[Sequence[str], str] = None,
        expression: Optional[str] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read and merge parts defined by geojson feature from multiple bands.

        Args:
            shape (dict): Valid GeoJSON feature.
            bands (sequence of str or str, optional): bands to fetch info from.
            expression (str, optional): rio-tiler expression for the band list (e.g. b1/b2+b3).
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
            with self.reader(url, tms=self.tms, **self.reader_options) as src:  # type: ignore
                data = src.feature(*args, **kwargs)
                data.band_names = [band]  # use `band` as name instead of band index
                return data

        img = multi_arrays(bands, _reader, shape, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img
