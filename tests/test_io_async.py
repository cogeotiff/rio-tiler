"""Test Async BaseClass."""

import asyncio
import functools
import os
import typing
from typing import Any, Coroutine, Dict, List, Type

import attr
import morecantile
import pytest

from rio_tiler.constants import WEB_MERCATOR_TMS, BBox
from rio_tiler.io import AsyncBaseReader, COGReader
from rio_tiler.models import BandStatistics, ImageData, Info

try:
    import contextvars  # Python 3.7+ only or via contextvars backport.
except ImportError:  # pragma: no cover
    contextvars = None  # type: ignore

T = typing.TypeVar("T")

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
COGEO = os.path.join(PREFIX, "cog_nodata.tif")


async def run_in_threadpool(
    func: typing.Callable[..., T], *args: typing.Any, **kwargs: typing.Any
) -> T:
    """Mock Sync function for Async call.Any

    Code from https://github.com/encode/starlette/blob/master/starlette/concurrency.py
    """
    loop = asyncio.get_event_loop()
    if contextvars is not None:  # pragma: no cover
        # Ensure we run in the same context
        child = functools.partial(func, *args, **kwargs)
        context = contextvars.copy_context()
        func = context.run
        args = (child,)
    elif kwargs:  # pragma: no cover
        # loop.run_in_executor doesn't accept 'kwargs', so bind them in here
        func = functools.partial(func, **kwargs)
    return await loop.run_in_executor(None, func, *args)


@attr.s
class AsyncCOGReader(AsyncBaseReader):

    input: Type[COGReader] = attr.ib()
    tms: morecantile.TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    def __attrs_post_init__(self):
        """Update dataset info."""
        self.bounds = self.input.bounds
        self.crs = self.input.crs
        self.minzoom = self.input.minzoom
        self.maxzoom = self.input.maxzoom

    async def info(self) -> Coroutine[Any, Any, Info]:
        """Return Dataset's info."""
        return await run_in_threadpool(self.input.info)  # type: ignore

    async def statistics(
        self, **kwargs: Any
    ) -> Coroutine[Any, Any, Dict[str, BandStatistics]]:
        """Return Dataset's statistics."""
        return await run_in_threadpool(self.input.statistics, **kwargs)  # type: ignore

    async def tile(
        self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Map tile from the Dataset."""
        return await run_in_threadpool(
            self.input.tile, tile_x, tile_y, tile_z, **kwargs  # type: ignore
        )

    async def part(self, bbox: BBox, **kwargs: Any) -> Coroutine[Any, Any, ImageData]:
        """Read a Part of a Dataset."""
        return await run_in_threadpool(self.input.part, bbox, **kwargs)  # type: ignore

    async def preview(self, **kwargs: Any) -> Coroutine[Any, Any, ImageData]:
        """Return a preview of a Dataset."""
        return await run_in_threadpool(self.input.preview, **kwargs)  # type: ignore

    async def point(
        self, lon: float, lat: float, **kwargs: Any
    ) -> Coroutine[Any, Any, List]:
        """Read a value from a Dataset."""
        return await run_in_threadpool(self.input.point, lon, lat, **kwargs)  # type: ignore

    async def feature(
        self, shape: Dict, **kwargs: Any
    ) -> Coroutine[Any, Any, ImageData]:
        """Read a Dataset for a GeoJSON feature"""
        return await run_in_threadpool(self.input.feature, shape, **kwargs)  # type: ignore


@pytest.mark.asyncio
async def test_async():
    dataset = COGReader(COGEO)

    async with AsyncCOGReader(dataset) as cog:
        info = await cog.info()
        assert info == dataset.info()

        assert cog.minzoom == 5
        assert cog.maxzoom == 9

        stat = await cog.statistics()
        assert stat == dataset.statistics()

        data, mask = await cog.tile(43, 24, 7)
        assert data.shape == (1, 256, 256)
        assert mask.all()

        lon = -56.624124590533825
        lat = 73.52687881825946
        pts = await cog.point(lon, lat)
        assert len(pts) == 1

        bbox = (
            -56.624124590533825,
            73.50183615350426,
            -56.530950796449005,
            73.52687881825946,
        )
        data, mask = await cog.part(bbox)
        assert data.shape == (1, 11, 40)

        data, mask = await cog.preview(max_size=128)
        assert data.shape == (1, 128, 128)

        feature = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-56.4697265625, 74.17307693616263],
                        [-57.667236328125, 73.53462847039683],
                        [-57.59033203125, 73.13451013251789],
                        [-56.195068359375, 72.94865294642922],
                        [-54.964599609375, 72.96797135377102],
                        [-53.887939453125, 73.84623016391944],
                        [-53.97583007812499, 74.0165183926664],
                        [-54.73388671875, 74.23289305339864],
                        [-55.54687499999999, 74.2269213699517],
                        [-56.129150390625, 74.21497138945001],
                        [-56.2060546875, 74.21198251594369],
                        [-56.4697265625, 74.17307693616263],
                    ]
                ],
            },
        }

        img = await cog.feature(feature, max_size=1024)
        assert img.data.shape == (1, 348, 1024)
