"""test for async Reader."""

import os

import pytest
from async_geotiff import GeoTIFF
from obstore.store import LocalStore

from rio_tiler.errors import ExpressionMixingWarning
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


@pytest.mark.asyncio
async def test_async_reader_point():
    """tests async reader."""
    store = LocalStore(PREFIX)
    geotiff = await GeoTIFF.open("cog.tif", store=store)
    async with Reader(geotiff) as src:
        pt = await src.point(-60, 73, coord_crs="epsg:4326")
        assert len(pt.data) == 1
        assert len(pt.mask) == 1
        assert pt.band_names == ["b1"]

        pt = await src.point(-60, 73, coord_crs="epsg:4326", indexes=1)
        assert len(pt.data) == 1
        assert len(pt.mask) == 1
        assert pt.band_names == ["b1"]

        pt = await src.point(-60, 73, coord_crs="epsg:4326", indexes=[1, 1, 1])
        assert len(pt.data) == 3
        assert len(pt.mask) == 1
        assert pt.band_descriptions == ["b1", "b1", "b1"]

        pt = await src.point(-60, 73, expression="b1*2;b1-100")
        assert len(pt.data) == 2
        assert len(pt.mask) == 1
        assert pt._mask[0]
        assert pt.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            pt = await src.point(-60, 73, indexes=(1, 1, 1), expression="b1*2")
            assert len(pt.data) == 1
            assert pt.band_descriptions == ["b1*2"]

    geotiff = await GeoTIFF.open("cog_nodata.tif", store=store)
    async with Reader(geotiff) as src:
        pt = await src.point(-59.53, 74.03, indexes=(1, 1, 1))
        assert len(pt.data) == 3
        assert not pt._mask[0]
        assert pt.band_descriptions == ["b1", "b1", "b1"]
