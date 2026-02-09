"""rio_tiler.experimental.async_base: ABC class for rio-tiler Async readers."""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any

import attr
from morecantile import TileMatrixSet

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.io.base import SpatialMixin
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox

if TYPE_CHECKING:
    from collections.abc import Awaitable


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
    async def point(self, lon: float, lat: float) -> Awaitable[PointData]:
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
