"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
import contextlib
import re
import warnings
from functools import cached_property
from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, Union

import attr
import numpy
from affine import Affine
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.warp import calculate_default_transform, transform_bounds

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import (
    AssetAsBandError,
    ExpressionMixingWarning,
    InvalidExpression,
    MissingAssets,
    MissingBands,
    TileOutsideBounds,
)
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.tasks import multi_arrays, multi_points, multi_values
from rio_tiler.types import AssetInfo, BBox, Indexes
from rio_tiler.utils import CRS_to_uri, cast_to_sequence, normalize_bounds


@attr.s
class SpatialMixin:
    """Spatial Info Mixin.

    Attributes:
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.

    """

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    transform: Optional[Affine] = attr.ib(default=None, init=False)
    height: Optional[int] = attr.ib(default=None, init=False)
    width: Optional[int] = attr.ib(default=None, init=False)

    def get_geographic_bounds(self, crs: CRS) -> BBox:
        """Return Geographic Bounds for a Geographic CRS."""
        if self.crs == crs:
            if self.bounds[1] > self.bounds[3]:
                warnings.warn(
                    "BoundingBox of the dataset is inverted (minLat > maxLat).",
                    UserWarning,
                )
                return (
                    self.bounds[0],
                    self.bounds[3],
                    self.bounds[2],
                    self.bounds[1],
                )

            return self.bounds

        try:
            bounds = transform_bounds(self.crs, crs, *self.bounds, densify_pts=21)
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

    @cached_property
    def _dst_geom_in_tms_crs(self):
        """Return dataset geom info in TMS projection."""
        tms_crs = self.tms.rasterio_crs
        if self.crs != tms_crs:
            dst_affine, w, h = calculate_default_transform(
                self.crs,
                tms_crs,
                self.width,
                self.height,
                *self.bounds,
            )
        else:
            dst_affine = list(self.transform)
            w = self.width
            h = self.height

        return dst_affine, w, h

    @cached_property
    def _minzoom(self) -> int:
        """Calculate dataset minimum zoom level."""
        # We assume the TMS tilesize to be constant over all matrices
        # ref: https://github.com/OSGeo/gdal/blob/dc38aa64d779ecc45e3cd15b1817b83216cf96b8/gdal/frmts/gtiff/cogdriver.cpp#L274
        tilesize = self.tms.tileMatrices[0].tileWidth

        if all([self.transform, self.height, self.width]):
            try:
                dst_affine, w, h = self._dst_geom_in_tms_crs

                # The minzoom is defined by the resolution of the maximum theoretical overview level
                # We assume `tilesize`` is the smallest overview size
                overview_level = get_maximum_overview_level(w, h, minsize=tilesize)

                # Get the resolution of the overview
                resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
                ovr_resolution = resolution * (2**overview_level)

                # Find what TMS matrix match the overview resolution
                return self.tms.zoom_for_res(ovr_resolution)

            except:  # noqa
                # if we can't get max zoom from the dataset we default to TMS maxzoom
                warnings.warn(
                    "Cannot determine minzoom based on dataset information, will default to TMS minzoom.",
                    UserWarning,
                )

        return self.tms.minzoom

    @cached_property
    def _maxzoom(self) -> int:
        """Calculate dataset maximum zoom level."""
        if all([self.transform, self.height, self.width]):
            try:
                dst_affine, _, _ = self._dst_geom_in_tms_crs

                # The maxzoom is defined by finding the minimum difference between
                # the raster resolution and the zoom level resolution
                resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))
                return self.tms.zoom_for_res(resolution)

            except:  # noqa
                # if we can't get min/max zoom from the dataset we default to TMS maxzoom
                warnings.warn(
                    "Cannot determine maxzoom based on dataset information, will default to TMS maxzoom.",
                    UserWarning,
                )

        return self.tms.maxzoom

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
        tile_bounds = tuple(self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)))

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
    default_assets: Optional[Sequence[str]] = attr.ib(init=False, default=None)

    ctx: Type[contextlib.AbstractContextManager] = attr.ib(
        init=False, default=contextlib.nullcontext
    )

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

    def _get_reader(self, asset_info: AssetInfo) -> Tuple[Type[BaseReader], Dict]:
        """Get Asset Reader and options."""
        return self.reader, {}

    def parse_expression(self, expression: str, asset_as_band: bool = False) -> Tuple:
        """Parse rio-tiler band math expression."""
        input_assets = "|".join(self.assets)

        if asset_as_band:
            _re = re.compile(rf"\b({input_assets})\b")
        else:
            _re = re.compile(rf"\b({input_assets})_b\d+\b")

        assets = tuple(set(re.findall(_re, expression)))
        if not assets:
            raise InvalidExpression(
                f"Could not find any valid assets in '{expression}' expression. Assets are: {self.assets}"
                if asset_as_band
                else f"Could not find any valid assets in '{expression}' expression, maybe try with `asset_as_band=True`. Assets are: {self.assets}"
            )

        return assets

    def _update_statistics(
        self,
        img: ImageData,
        indexes: Optional[Indexes] = None,
        statistics: Optional[Sequence[Tuple[float, float]]] = None,
    ):
        """Update ImageData Statistics from AssetInfo."""
        indexes = cast_to_sequence(indexes)

        if indexes is None:
            indexes = tuple(range(1, img.count + 1))

        if not img.dataset_statistics and statistics:
            if max(max(indexes), len(indexes)) > len(statistics):  # type: ignore
                return

            img.dataset_statistics = [statistics[bidx - 1] for bidx in indexes]

    def info(
        self,
        assets: Optional[Union[Sequence[str], str]] = None,
        **kwargs: Any,
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
        assets = cast_to_sequence(assets or self.assets)

        def _reader(asset: str, **kwargs: Any) -> Dict:
            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    return src.info()

        return multi_values(assets, _reader, **kwargs)

    def statistics(
        self,
        assets: Optional[Union[Sequence[str], str]] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
        asset_expression: Optional[Dict[str, str]] = None,
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

        assets = cast_to_sequence(assets or self.assets)
        asset_indexes = asset_indexes or {}
        asset_expression = asset_expression or {}

        def _reader(asset: str, *args: Any, **kwargs: Any) -> Dict:
            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    return src.statistics(
                        *args,
                        indexes=asset_indexes.get(asset, kwargs.pop("indexes", None)),
                        expression=asset_expression.get(asset),
                        **kwargs,
                    )

        return multi_values(assets, _reader, **kwargs)

    def merged_statistics(
        self,
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: Optional[List[int]] = None,
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
            assets = cast_to_sequence(assets or self.assets)

        data = self.preview(
            assets=assets,
            expression=expression,
            asset_indexes=asset_indexes,
            max_size=max_size,
            **kwargs,
        )
        return data.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
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
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        assets = cast_to_sequence(assets)
        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets and self.default_assets:
            warnings.warn(
                f"No assets/expression passed, defaults to {self.default_assets}",
                UserWarning,
            )
            assets = self.default_assets

        if not assets:
            raise MissingAssets(
                "assets must be passed via `expression` or `assets` options, or via class-level `default_assets`."
            )

        asset_indexes = asset_indexes or {}

        # We fall back to `indexes` if provided
        indexes = kwargs.pop("indexes", None)

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or indexes

            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    data = src.tile(*args, indexes=idx, **kwargs)

                    self._update_statistics(
                        data,
                        indexes=idx,
                        statistics=asset_info.get("dataset_statistics"),
                    )

                    metadata = data.metadata or {}
                    if m := asset_info.get("metadata"):
                        metadata.update(m)
                    data.metadata = {asset: metadata}

                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use `asset_as_band` for multibands asset"
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
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
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
        assets = cast_to_sequence(assets)
        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets and self.default_assets:
            warnings.warn(
                f"No assets/expression passed, defaults to {self.default_assets}",
                UserWarning,
            )
            assets = self.default_assets

        if not assets:
            raise MissingAssets(
                "assets must be passed via `expression` or `assets` options, or via class-level `default_assets`."
            )

        asset_indexes = asset_indexes or {}

        # We fall back to `indexes` if provided
        indexes = kwargs.pop("indexes", None)

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or indexes

            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    data = src.part(*args, indexes=idx, **kwargs)

                    self._update_statistics(
                        data,
                        indexes=idx,
                        statistics=asset_info.get("dataset_statistics"),
                    )

                    metadata = data.metadata or {}
                    if m := asset_info.get("metadata"):
                        metadata.update(m)
                    data.metadata = {asset: metadata}

                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use `asset_as_band` for multibands asset"
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
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
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
        assets = cast_to_sequence(assets)
        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets and self.default_assets:
            warnings.warn(
                f"No assets/expression passed, defaults to {self.default_assets}",
                UserWarning,
            )
            assets = self.default_assets

        if not assets:
            raise MissingAssets(
                "assets must be passed via `expression` or `assets` options, or via class-level `default_assets`."
            )

        asset_indexes = asset_indexes or {}

        # We fall back to `indexes` if provided
        indexes = kwargs.pop("indexes", None)

        def _reader(asset: str, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or indexes

            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    data = src.preview(indexes=idx, **kwargs)

                    self._update_statistics(
                        data,
                        indexes=idx,
                        statistics=asset_info.get("dataset_statistics"),
                    )

                    metadata = data.metadata or {}
                    if m := asset_info.get("metadata"):
                        metadata.update(m)
                    data.metadata = {asset: metadata}

                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use `asset_as_band` for multibands asset"
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
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
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
        assets = cast_to_sequence(assets)
        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets and self.default_assets:
            warnings.warn(
                f"No assets/expression passed, defaults to {self.default_assets}",
                UserWarning,
            )
            assets = self.default_assets

        if not assets:
            raise MissingAssets(
                "assets must be passed via `expression` or `assets` options, or via class-level `default_assets`."
            )

        asset_indexes = asset_indexes or {}

        # We fall back to `indexes` if provided
        indexes = kwargs.pop("indexes", None)

        def _reader(asset: str, *args: Any, **kwargs: Any) -> PointData:
            idx = asset_indexes.get(asset) or indexes

            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    data = src.point(*args, indexes=idx, **kwargs)

                    metadata = data.metadata or {}
                    if m := asset_info.get("metadata"):
                        metadata.update(m)
                    data.metadata = {asset: metadata}

                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use `asset_as_band` for multibands asset"
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
        assets: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        asset_indexes: Optional[Dict[str, Indexes]] = None,
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
        assets = cast_to_sequence(assets)
        if assets and expression:
            warnings.warn(
                "Both expression and assets passed; expression will overwrite assets parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            assets = self.parse_expression(expression, asset_as_band=asset_as_band)

        if not assets and self.default_assets:
            warnings.warn(
                f"No assets/expression passed, defaults to {self.default_assets}",
                UserWarning,
            )
            assets = self.default_assets

        if not assets:
            raise MissingAssets(
                "assets must be passed via `expression` or `assets` options, or via class-level `default_assets`."
            )

        asset_indexes = asset_indexes or {}

        # We fall back to `indexes` if provided
        indexes = kwargs.pop("indexes", None)

        def _reader(asset: str, *args: Any, **kwargs: Any) -> ImageData:
            idx = asset_indexes.get(asset) or indexes

            asset_info = self._get_asset_info(asset)
            reader, options = self._get_reader(asset_info)

            with self.ctx(**asset_info.get("env", {})):
                with reader(
                    asset_info["url"],
                    tms=self.tms,
                    **{**self.reader_options, **options},
                ) as src:
                    data = src.feature(*args, indexes=idx, **kwargs)

                    self._update_statistics(
                        data,
                        indexes=idx,
                        statistics=asset_info.get("dataset_statistics"),
                    )

                    metadata = data.metadata or {}
                    if m := asset_info.get("metadata"):
                        metadata.update(m)
                    data.metadata = {asset: metadata}

                    if asset_as_band:
                        if len(data.band_names) > 1:
                            raise AssetAsBandError(
                                "Can't use `asset_as_band` for multibands asset"
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
    default_bands: Optional[Sequence[str]] = attr.ib(init=False, default=None)

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
        input_bands = "|".join([rf"\b{band}\b" for band in self.bands])
        _re = re.compile(input_bands.replace("\\\\", "\\"))

        bands = tuple(set(re.findall(_re, expression)))
        if not bands:
            raise InvalidExpression(
                f"Could not find any valid bands in '{expression}' expression."
            )

        return bands

    def info(
        self,
        bands: Optional[Union[Sequence[str], str]] = None,
        **kwargs: Any,
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

        bands = cast_to_sequence(bands or self.bands)

        def _reader(band: str, **kwargs: Any) -> Info:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                return src.info()

        bands_metadata = multi_values(bands, _reader, **kwargs)

        meta = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
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
        bands: Optional[Union[Sequence[str], str]] = None,
        expression: Optional[str] = None,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: Optional[List[int]] = None,
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
            bands = cast_to_sequence(bands or self.bands)

        data = self.preview(
            bands=bands,
            expression=expression,
            max_size=max_size,
            **kwargs,
        )
        return data.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        bands: Optional[Union[Sequence[str], str]] = None,
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
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        bands = cast_to_sequence(bands)
        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands and self.default_bands:
            warnings.warn(
                f"No bands/expression passed, defaults to {self.default_bands}",
                UserWarning,
            )
            bands = self.default_bands

        if not bands:
            raise MissingBands(
                "bands must be passed either via `expression` or `bands` options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                data = src.tile(*args, **kwargs)

                if data.metadata:
                    data.metadata = {band: data.metadata}

                # use `band` as name instead of band index
                data.band_names = [band]

                return data

        img = multi_arrays(bands, _reader, tile_x, tile_y, tile_z, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def part(
        self,
        bbox: BBox,
        bands: Optional[Union[Sequence[str], str]] = None,
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
        bands = cast_to_sequence(bands)
        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands and self.default_bands:
            warnings.warn(
                f"No bands/expression passed, defaults to {self.default_bands}",
                UserWarning,
            )
            bands = self.default_bands

        if not bands:
            raise MissingBands(
                "bands must be passed either via `expression` or `bands` options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                data = src.part(*args, **kwargs)

                if data.metadata:
                    data.metadata = {band: data.metadata}

                # use `band` as name instead of band index
                data.band_names = [band]

                return data

        img = multi_arrays(bands, _reader, bbox, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def preview(
        self,
        bands: Optional[Union[Sequence[str], str]] = None,
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
        bands = cast_to_sequence(bands)
        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands and self.default_bands:
            warnings.warn(
                f"No bands/expression passed, defaults to {self.default_bands}",
                UserWarning,
            )
            bands = self.default_bands

        if not bands:
            raise MissingBands(
                "bands must be passed either via `expression` or `bands` options."
            )

        def _reader(band: str, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                data = src.preview(**kwargs)

                if data.metadata:
                    data.metadata = {band: data.metadata}

                # use `band` as name instead of band index
                data.band_names = [band]

                return data

        img = multi_arrays(bands, _reader, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img

    def point(
        self,
        lon: float,
        lat: float,
        bands: Optional[Union[Sequence[str], str]] = None,
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
        bands = cast_to_sequence(bands)
        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands and self.default_bands:
            warnings.warn(
                f"No bands/expression passed, defaults to {self.default_bands}",
                UserWarning,
            )
            bands = self.default_bands

        if not bands:
            raise MissingBands(
                "bands must be passed either via `expression` or `bands` options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> PointData:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                data = src.point(*args, **kwargs)

                if data.metadata:
                    data.metadata = {band: data.metadata}

                # use `band` as name instead of band index
                data.band_names = [band]

                return data

        data = multi_points(bands, _reader, lon, lat, **kwargs)
        if expression:
            return data.apply_expression(expression)

        return data

    def feature(
        self,
        shape: Dict,
        bands: Optional[Union[Sequence[str], str]] = None,
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
        bands = cast_to_sequence(bands)
        if bands and expression:
            warnings.warn(
                "Both expression and bands passed; expression will overwrite bands parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            bands = self.parse_expression(expression)

        if not bands and self.default_bands:
            warnings.warn(
                f"No bands/expression passed, defaults to {self.default_bands}",
                UserWarning,
            )
            bands = self.default_bands

        if not bands:
            raise MissingBands(
                "bands must be passed either via `expression` or `bands` options."
            )

        def _reader(band: str, *args: Any, **kwargs: Any) -> ImageData:
            url = self._get_band_url(band)
            with self.reader(
                url,
                tms=self.tms,
                **self.reader_options,
            ) as src:
                data = src.feature(*args, **kwargs)

                if data.metadata:
                    data.metadata = {band: data.metadata}

                # use `band` as name instead of band index
                data.band_names = [band]

                return data

        img = multi_arrays(bands, _reader, shape, **kwargs)

        if expression:
            return img.apply_expression(expression)

        return img
