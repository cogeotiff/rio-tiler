"""rio_tiler.experimental.async_geotiff: rio-tiler Async reader built on top of async-geotiff."""

from __future__ import annotations

import abc
import warnings
from typing import TYPE_CHECKING, Any

import attr
from async_geotiff import Window
from morecantile import TileMatrixSet
from rasterio.crs import CRS
from rasterio.warp import transform as transform_coords

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import ExpressionMixingWarning, PointOutsideBounds
from rio_tiler.expression import parse_expression
from rio_tiler.io.base import SpatialMixin
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes
from rio_tiler.utils import cast_to_sequence

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from async_geotiff import GeoTIFF


@attr.s
class AsyncBaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Rio-tiler.io AsyncBaseReader."""

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    async def info(self) -> Awaitable[Info]:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        ...

    @abc.abstractmethod
    async def statistics(self) -> Awaitable[dict[str, BandStatistics]]:
        """Return bands statistics from a dataset.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        ...

    @abc.abstractmethod
    async def tile(self, tile_x: int, tile_y: int, tile_z: int) -> Awaitable[ImageData]:
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
    async def part(self, bbox: BBox, **kwargs: Any) -> Awaitable[ImageData]:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def preview(self) -> Awaitable[ImageData]:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def point(self, lon: float, lat: float) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            list: Pixel value per bands/assets.

        """
        ...

    @abc.abstractmethod
    async def feature(self, shape: dict) -> Awaitable[ImageData]:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...


@attr.s
class Reader(AsyncBaseReader):
    """Rio-tiler.io AsyncBaseReader."""

    input: GeoTIFF = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    colormap: dict | None = attr.ib(default=None)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def __attrs_post_init__(self):
        """Post init."""
        self.bounds = self.input.bounds
        self.crs = CRS.from_user_input(self.input.crs)

        self.transform = self.input.transform
        self.height = self.input.height
        self.width = self.input.width

        if self.colormap is None and self.input.colormap is not None:
            self.colormap = self.input.colormap.as_rasterio()

    async def info(self) -> Awaitable[Info]:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        raise NotImplementedError

    async def statistics(self) -> Awaitable[dict[str, BandStatistics]]:
        """Return bands statistics from a dataset.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        raise NotImplementedError

    async def tile(self, tile_x: int, tile_y: int, tile_z: int) -> Awaitable[ImageData]:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        raise NotImplementedError

    async def part(self, bbox: BBox, **kwargs: Any) -> Awaitable[ImageData]:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    async def preview(self) -> Awaitable[ImageData]:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    async def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.

        Returns:
            list: Pixel value per bands/assets.

        """
        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        if coord_crs != self.crs:
            xs, ys = transform_coords(coord_crs, self.crs, [lon], [lat])
            lon, lat = xs[0], ys[0]

        dataset_min_lon, dataset_min_lat, dataset_max_lon, dataset_max_lat = self.bounds
        # check if latitude is inverted
        if dataset_min_lat > dataset_max_lat:
            warnings.warn(
                "BoundingBox of the dataset is inverted (minLat > maxLat).",
                UserWarning,
            )

        dataset_min_lat, dataset_max_lat = (
            min(dataset_min_lat, dataset_max_lat),
            max(dataset_min_lat, dataset_max_lat),
        )
        if not (
            (dataset_min_lon < lon < dataset_max_lon)
            and (dataset_min_lat < lat < dataset_max_lat)
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        # TODO: handle interpolation
        row, col = self.input.index(lon, lat)
        row_off, col_off = row, col

        window = Window(row_off=row_off, col_off=col_off, width=1, height=1)

        array = await self.input.read(window=window)
        indexes = indexes or list(range(1, self.input.count + 1))

        pt = PointData(
            array.as_masked()[[ix - 1 for ix in indexes], 0, 0],
            coordinates=(lon, lat),
            crs=coord_crs,
            pixel_location=(row, col),
            band_descriptions=[f"b{ix}" for ix in indexes],
        )

        if expression:
            return pt.apply_expression(expression)

        return pt

    async def feature(self, shape: dict) -> Awaitable[ImageData]:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError
