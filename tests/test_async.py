"""test for async Reader."""

import os

import numpy
import pytest
from async_geotiff import GeoTIFF
from obstore.store import LocalStore

from rio_tiler.errors import ExpressionMixingWarning
from rio_tiler.experimental._async import Reader
from rio_tiler.io import Reader as SyncReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
store = LocalStore(PREFIX)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "src_path,nodata",
    [
        ("cog.tif", None),
        ("cog_nodata.tif", 1),
    ],
)
async def test_async_reader(src_path, nodata):
    """tests async reader."""
    geotiff = await GeoTIFF.open(src_path, store=store)
    async with Reader(geotiff) as src:
        assert src.bounds
        assert src.crs
        assert src.transform
        assert src.height
        assert src.width
        assert src.input.nodata == nodata


@pytest.mark.asyncio
async def test_async_reader_point():
    """tests async reader point() method."""
    geotiff = await GeoTIFF.open("cog.tif", store=store)
    with SyncReader(os.path.join(PREFIX, "cog.tif")) as sync_src:
        async with Reader(geotiff) as src:
            pt = await src.point(-60, 73)
            assert len(pt.data) == 1
            assert len(pt.mask) == 1
            assert pt.band_names == ["b1"]
            sync_pt = sync_src.point(-60, 73)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions

            pt = await src.point(-60, 73, indexes=1)
            assert len(pt.data) == 1
            assert len(pt.mask) == 1
            assert pt.band_names == ["b1"]
            sync_pt = sync_src.point(-60, 73, indexes=1)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions

            pt = await src.point(-60, 73, indexes=[1, 1, 1])
            assert len(pt.data) == 3
            assert len(pt.mask) == 1
            assert pt.band_descriptions == ["b1", "b1", "b1"]
            sync_pt = sync_src.point(-60, 73, indexes=[1, 1, 1])
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions

            pt = await src.point(-60, 73, expression="b1*2;b1-100")
            assert len(pt.data) == 2
            assert len(pt.mask) == 1
            assert pt._mask[0]
            assert pt.band_descriptions == ["b1*2", "b1-100"]
            sync_pt = sync_src.point(-60, 73, expression="b1*2;b1-100")
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions

            with pytest.warns(ExpressionMixingWarning):
                pt = await src.point(-60, 73, indexes=(1, 1, 1), expression="b1*2")
                assert len(pt.data) == 1
                assert pt.band_descriptions == ["b1*2"]

    geotiff = await GeoTIFF.open("cog_nodata.tif", store=store)
    with SyncReader(os.path.join(PREFIX, "cog_nodata.tif")) as sync_src:
        async with Reader(geotiff) as src:
            pt = await src.point(-59.53, 74.03, indexes=(1, 1, 1))
            assert len(pt.data) == 3
            assert not pt._mask[0]
            assert pt.band_descriptions == ["b1", "b1", "b1"]
            sync_pt = sync_src.point(-59.53, 74.03, indexes=(1, 1, 1))
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions


@pytest.mark.asyncio
async def test_async_reader_preview():
    """Read preview."""
    geotiff = await GeoTIFF.open("cog_ovr.tif", store=store)
    with SyncReader(os.path.join(PREFIX, "cog_ovr.tif")) as sync_src:
        async with Reader(geotiff) as src:
            img = await src.preview()
            assert img.array.shape == (1, 1024, 1021)
            assert img.band_descriptions == ["b1"]
            sync_img = sync_src.preview()
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            img = await src.preview(max_size=128)
            assert img.array.shape == (1, 128, 128)
            assert img.band_descriptions == ["b1"]
            sync_img = sync_src.preview(max_size=128)
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            img = await src.preview(max_size=None)
            assert img.array.shape == (1, 2667, 2658)
            assert img.band_descriptions == ["b1"]
            sync_img = sync_src.preview(max_size=None)
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            img = await src.preview(dst_crs="epsg:4326")
            assert img.array.shape == (1, 278, 1024)
            assert img.band_descriptions == ["b1"]
            sync_img = sync_src.preview(dst_crs="epsg:4326")
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            img = await src.preview(dst_crs="epsg:4326", max_size=512)
            assert img.array.shape == (1, 139, 512)
            assert img.band_descriptions == ["b1"]
            sync_img = sync_src.preview(dst_crs="epsg:4326", max_size=512)
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            img = await src.preview(max_size=128, expression="b1*2;b1-100")
            assert img.array.shape == (2, 128, 128)
            assert img.band_descriptions == ["b1*2", "b1-100"]
            sync_img = sync_src.preview(max_size=128, expression="b1*2;b1-100")
            numpy.testing.assert_array_equal(img.array, sync_img.array)
            assert img.band_descriptions == sync_img.band_descriptions

            with pytest.warns(ExpressionMixingWarning):
                img = await src.preview(
                    max_size=128, indexes=(1, 2, 3), expression="b1*2"
                )
                assert img.array.shape == (1, 128, 128)
                assert img.band_descriptions == ["b1*2"]
