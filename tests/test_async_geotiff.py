"""test for async Reader."""

import os

import numpy
import pytest
from async_geotiff import GeoTIFF
from obstore.store import LocalStore

from rio_tiler.errors import ExpressionMixingWarning, TileOutsideBounds
from rio_tiler.experimental.geotiff import Reader as GeoTIFFReader
from rio_tiler.io import Reader
from rio_tiler.models import BandStatistics

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
store = LocalStore(PREFIX)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "src_path,nodata",
    [
        ("cog.tif", None),
        ("cog_nodata.tif", 1),
        ("cog_cmap.tif", 0),
    ],
)
async def test_async_reader(src_path, nodata):
    """tests async reader."""
    geotiff = await GeoTIFF.open(src_path, store=store)
    async with GeoTIFFReader(geotiff) as src:
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
    with Reader(os.path.join(PREFIX, "cog.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            pt = await src.point(-60, 73)
            assert len(pt.data) == 1
            assert len(pt.mask) == 1
            assert pt.band_names == ["b1"]
            sync_pt = sync_src.point(-60, 73)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions
            # assert pt.pixel_location == sync_pt.pixel_location

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
    with Reader(os.path.join(PREFIX, "cog_nodata.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            pt = await src.point(-59.53, 74.03, indexes=(1, 1, 1))
            assert len(pt.data) == 3
            assert not pt._mask[0]
            assert pt.band_descriptions == ["b1", "b1", "b1"]
            sync_pt = sync_src.point(-59.53, 74.03, indexes=(1, 1, 1))
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.band_descriptions == sync_pt.band_descriptions
            # assert pt.pixel_location == sync_pt.pixel_location

    # Test coordinates
    geotiff = await GeoTIFF.open("dataset_2d.tif", store=store)
    with Reader(os.path.join(PREFIX, "dataset_2d.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            pt = await src.point(0, 0)
            sync_pt = sync_src.point(0, 0)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.pixel_location == sync_pt.pixel_location

            pt = await src.point(0.15, 0.15)
            sync_pt = sync_src.point(0.15, 0.15)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.pixel_location == sync_pt.pixel_location

    geotiff = await GeoTIFF.open("cog_scale_epsg4326.tif", store=store)
    with Reader(os.path.join(PREFIX, "cog_scale_epsg4326.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            pt = await src.point(127, 37)
            sync_pt = sync_src.point(127, 37)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.pixel_location == sync_pt.pixel_location
            assert pt.scales == [0.0001, 0.001]
            assert pt.offsets == [1000.0, 2000.0]

            pt = await src.point(127, 37, unscale=True)
            sync_pt = sync_src.point(127, 37, unscale=True)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.scales == [1.0, 1.0]
            assert pt.offsets == [0.0, 0.0]


@pytest.mark.asyncio
async def test_async_reader_preview():
    """Read preview."""
    geotiff = await GeoTIFF.open("cog_ovr.tif", store=store)
    with Reader(os.path.join(PREFIX, "cog_ovr.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
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

    geotiff = await GeoTIFF.open("cog_scale_epsg4326.tif", store=store)
    with Reader(os.path.join(PREFIX, "cog_scale_epsg4326.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            img = await src.preview(max_size=128)
            sync_img = sync_src.preview(max_size=128)
            numpy.testing.assert_array_equal(sync_img.array, img.array)
            assert img.scales == [0.0001, 0.001]
            assert img.offsets == [1000.0, 2000.0]

            img = await src.preview(max_size=128, unscale=True)
            sync_img = sync_src.preview(max_size=128, unscale=True)
            numpy.testing.assert_array_equal(sync_img.array, img.array)
            assert img.scales == [1.0, 1.0]
            assert img.offsets == [0.0, 0.0]

    geotiff = await GeoTIFF.open("red.tif", store=store)
    async with GeoTIFFReader(geotiff) as src:
        img = await src.preview(max_size=128)
        assert img.dataset_statistics == [(6101.0, 65035.0)]


@pytest.mark.asyncio
async def test_async_reader_stats():
    """Read preview."""
    geotiff = await GeoTIFF.open("cog_ovr.tif", store=store)
    with Reader(os.path.join(PREFIX, "cog_ovr.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            stats = await src.statistics()
            assert len(stats) == 1
            assert isinstance(stats["b1"], BandStatistics)
            assert stats["b1"].percentile_2
            assert stats["b1"].percentile_98

            sync_stats = sync_src.statistics()
            assert sync_stats["b1"].percentile_2 == stats["b1"].percentile_2
            assert sync_stats["b1"].percentile_98 == stats["b1"].percentile_98

            stats = await src.statistics(percentiles=[3])
            assert stats["b1"].percentile_3

            stats = await src.statistics(percentiles=[3])
            assert stats["b1"].percentile_3

            # make sure kwargs are passed to `preview`
            stats = await src.statistics(width=100, height=100, max_size=None)
            assert stats["b1"].count == 10000.0

            stats = await src.statistics(expression="b1;b1*2")
            assert stats["b1"]
            assert stats["b1"].description == "b1"
            assert stats["b2"]
            assert stats["b2"].description == "b1*2"
            assert stats["b1"].min == stats["b2"].min / 2

    geotiff = await GeoTIFF.open("cog_cmap.tif", store=store)
    async with GeoTIFFReader(geotiff) as src:
        stats = await src.statistics(categorical=True)
        assert stats["b1"].histogram[1] == [
            1.0,
            3.0,
            4.0,
            5.0,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
        ]

        stats = await src.statistics(categorical=True, categories=[1, 3])
        assert stats["b1"].histogram[1] == [
            1.0,
            3.0,
        ]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "src_path",
    [
        "cog.tif",
        "cog_nodata.tif",
        "cog_cmap.tif",
        "rgb.tif",
        "cog_rgb_mask.tif",
        "cog_rgba.tif",
        "cog_scale_epsg4326.tif",
        "red.tif",
    ],
)
async def test_async_reader_info(src_path):
    """tests async reader."""
    geotiff = await GeoTIFF.open(src_path, store=store)
    async with GeoTIFFReader(geotiff) as src:
        info = await src.info()

    with Reader(os.path.join(PREFIX, src_path)) as sync_src:
        sync_info = sync_src.info()

    assert info.bounds == sync_info.bounds
    assert info.crs == sync_info.crs

    assert info.height == sync_info.height
    assert info.width == sync_info.width

    # TODO: band descriptions are not yet available in async-geotiff
    # assert info.band_descriptions == sync_info.band_descriptions

    assert info.nodata_type == sync_info.nodata_type
    assert info.scales == sync_info.scales
    assert info.offsets == sync_info.offsets


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "src_path",
    [
        # "cog_uint8_rgb_mask.tif",  # async-geotiff has an issue with this file
        "cog_uint8_rgb_nodata.tif",
        "cog_uint8_rgba.tif",
    ],
)
async def test_mask(src_path):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    geotiff = await GeoTIFF.open(src_path, store=store)
    async with GeoTIFFReader(geotiff) as src:
        im = await src.preview(max_size=1024)
        assert im.count == 3

        assert im.array.data[0, 0, 0] == 0
        assert im.array.data[0, -1, -1]
        assert im.array.mask[0, 0, 0]
        assert not im.array.mask[0, -1, -1]

        # GDAL Like mask (0 = valid, 255 = invalid)
        assert im.mask[0, 0] == 0
        assert im.mask[-1, -1] == 255

        # Alpha mask (0 = invalid, 255 = valid)
        if im.alpha_mask is not None:
            assert im.alpha_mask[0, 0] == 0
            assert im.alpha_mask[-1, -1] == 255

    # Check with rio-tiler Reader
    with Reader(os.path.join(PREFIX, src_path)) as sync_src:
        sync_im = sync_src.preview(max_size=1024)
        numpy.testing.assert_array_equal(im.array.data, sync_im.array.data)
        numpy.testing.assert_array_equal(im.array.mask, sync_im.array.mask)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "src_path",
    [
        # "cog_uint8_rgb_mask.tif",  # async-geotiff has an issue with this file
        "cog_nodata.tif",
        "cog_fullearth.tif",
        "cog_dateline.tif",
        "cog_uint8_rgb_nodata.tif",
        "cog_uint8_rgba.tif",
    ],
)
async def test_async_reader_tile(src_path):
    """tests async reader tile() method."""
    geotiff = await GeoTIFF.open(src_path, store=store)
    with Reader(os.path.join(PREFIX, src_path)) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            minzoom, maxzoom = src.minzoom, src.maxzoom
            w, s, e, n = src.get_geographic_bounds("epsg:4326")

            extrema = {}
            for zoom in range(minzoom, maxzoom + 1):
                ul_tile = src.tms.tile(w, n, zoom)
                lr_tile = src.tms.tile(e, s, zoom)
                extrema[zoom] = {
                    "x": {"min": ul_tile.x, "max": lr_tile.x + 1},
                    "y": {"min": ul_tile.y, "max": lr_tile.y + 1},
                }

            for zoom, ext in extrema.items():
                for x in range(ext["x"]["min"], ext["x"]["max"]):
                    for y in range(ext["y"]["min"], ext["y"]["max"]):
                        try:
                            tile = await src.tile(x, y, zoom)
                            sync_tile = sync_src.tile(x, y, zoom)
                            assert tile.bounds == sync_tile.bounds
                            numpy.testing.assert_array_equal(sync_tile.array, tile.array)
                            numpy.testing.assert_array_equal(
                                sync_tile.array.mask, tile.array.mask
                            )
                        except TileOutsideBounds:
                            pass

            with pytest.raises(TileOutsideBounds):
                await src.tile(
                    extrema[minzoom]["x"]["max"], extrema[minzoom]["y"]["max"], minzoom
                )


@pytest.mark.asyncio
async def test_async_reader_part():
    """tests async reader tile() method."""
    bbox = (
        -56.624124590533825,
        73.50183615350426,
        -56.530950796449005,
        73.52687881825946,
    )

    geotiff = await GeoTIFF.open("cog_nodata.tif", store=store)
    with Reader(os.path.join(PREFIX, "cog_nodata.tif")) as sync_src:
        async with GeoTIFFReader(geotiff) as src:
            img = await src.part(bbox)
            sync_img = sync_src.part(bbox)
            assert img.bounds == sync_img.bounds
            numpy.testing.assert_array_equal(sync_img.array, img.array)

            img = await src.part(bbox, dst_crs=src.crs)
            sync_img = sync_src.part(bbox, dst_crs=sync_src.crs)
            assert img.bounds == sync_img.bounds
            numpy.testing.assert_array_equal(sync_img.array, img.array)

            img = await src.part(bbox, dst_crs="EPSG:3857")
            sync_img = sync_src.part(bbox, dst_crs="EPSG:3857")
            assert img.bounds == sync_img.bounds
            numpy.testing.assert_array_equal(sync_img.array, img.array)

            img = await src.part(bbox, max_size=20)
            sync_img = sync_src.part(bbox, max_size=20)
            assert img.bounds == sync_img.bounds
            numpy.testing.assert_array_equal(sync_img.array, img.array)

            img = await src.part(bbox, width=20, height=10)
            sync_img = sync_src.part(bbox, width=20, height=10)
            assert img.bounds == sync_img.bounds
            # NOTE: we loosen a bit the tolerence here
            numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

            bbox = src.get_geographic_bounds("epsg:4326")
            bbox = (
                bbox[0] - 2.0,
                bbox[1] - 2.0,
                bbox[2] + 2.0,
                bbox[3] + 2.0,
            )

            img = await src.part(bbox, dst_crs=src.crs)
            sync_img = sync_src.part(bbox, dst_crs=sync_src.crs)
            # This test fails on github CI
            # assert img.bounds == sync_img.bounds
            numpy.testing.assert_array_equal(sync_img.array, img.array)

            # TODO: this test fails because the output shape is different
            # img = await src.part(bbox, dst_crs="epsg:4326", max_size=1000)
            # sync_img = sync_src.part(bbox, dst_crs="epsg:4326", max_size=1000)
            # assert img.bounds == sync_img.bounds
            # numpy.testing.assert_almost_equal(sync_img.array, img.array)


@pytest.mark.asyncio
async def test_async_reader_valid():
    """Read from feature."""
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

    geotiff = await GeoTIFF.open("cog_nodata.tif", store=store)
    async with GeoTIFFReader(geotiff) as src:
        # dst_crs should default to epsg:4326
        img = await src.feature(feature, max_size=1024)
        assert img.data.shape == (1, 334, 1024)
        assert img.band_names == ["b1"]

        img = await src.feature(feature, dst_crs=src.crs, max_size=1024)
        assert img.data.shape == (1, 1024, 869)

        img = await src.feature(feature, max_size=30)
        assert img.data.shape == (1, 10, 30)

        img = await src.feature(feature, expression="b1*2;b1-100", max_size=1024)
        assert img.data.shape == (2, 334, 1024)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = await src.feature(
                feature, indexes=(1, 2, 3), expression="b1*2", max_size=1024
            )
            assert img.data.shape == (1, 334, 1024)
            assert img.band_descriptions == ["b1*2"]

        img = await src.feature(feature, indexes=1, max_size=1024)
        assert img.data.shape == (1, 334, 1024)

        img = await src.feature(
            feature,
            indexes=(
                1,
                1,
            ),
            max_size=1024,
        )
        assert img.data.shape == (2, 334, 1024)
        assert img.band_descriptions == ["b1", "b1"]

        # feature overlaping on mask area
        mask_feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-54.45922851562499, 73.05143929453952],
                        [-55.052490234375, 72.79658820490461],
                        [-55.61279296874999, 72.46203877644956],
                        [-53.8330078125, 72.36244812858165],
                        [-54.45922851562499, 73.05143929453952],
                    ]
                ],
            },
        }

        img = await src.feature(mask_feat, max_size=1024)
        assert not img._mask.all()

        outside_mask_feature = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-57.3486328125, 72.25226599952339],
                        [-57.041015625, 72.1279362810559],
                        [-56.722412109375, 72.06038062953813],
                        [-54.86572265625, 72.07052969916067],
                        [-54.613037109375, 72.63665259171732],
                        [-56.14013671875, 72.90995232978632],
                        [-57.3486328125, 72.25226599952339],
                    ]
                ],
            },
        }
        img = await src.feature(outside_mask_feature, max_size=1024)
        assert not img._mask.all()
