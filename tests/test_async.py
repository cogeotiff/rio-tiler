"""test for async Reader."""

import os

import pytest
from async_geotiff import GeoTIFF
from obstore.store import LocalStore

from rio_tiler.experimental._async import Reader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.mark.asyncio
async def test_async_reader():
    """tests async reader."""
    store = LocalStore(PREFIX)
    geotiff = await GeoTIFF.open("cog.tif", store=store)
    async with Reader(geotiff) as src:
        assert src.bounds
        assert src.crs
        assert src.transform
        assert src.height
        assert src.width
        assert not src.input.nodata

    geotiff = await GeoTIFF.open("cog_nodata.tif", store=store)
    async with Reader(geotiff) as src:
        assert src.bounds
        assert src.crs
        assert src.transform
        assert src.height
        assert src.width
        assert src.input.nodata
