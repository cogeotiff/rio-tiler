"""tests rio_tiler.utils"""

import os
import pytest

from mock import patch

import numpy as np
import mercantile

from rio_toa import toa_utils

import rasterio
from rasterio.crs import CRS
from rasterio.enums import Resampling

from rio_tiler import utils
from rio_tiler.errors import NoOverviewWarning, DeprecationWarning, TileOutsideBounds

from .conftest import requires_webp


SENTINEL_SCENE = "S2A_tile_20170729_19UDP_0"
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "sentinel-s2-l1c")
SENTINEL_PATH = os.path.join(SENTINEL_BUCKET, "tiles/19/U/DP/2017/7/29/0/")

LANDSAT_SCENE_C1 = "LC08_L1TP_016037_20170813_20170814_01_RT"
LANDSAT_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "landsat-pds")
LANDSAT_PATH = os.path.join(
    LANDSAT_BUCKET, "c1", "L8", "016", "037", LANDSAT_SCENE_C1, LANDSAT_SCENE_C1
)

S3_KEY = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif"
S3_KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
S3_KEY_NODATA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif"
S3_KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"
S3_KEY_EXTMASK = (
    "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_extmask.tif"
)

S3_LOCAL = PREFIX = os.path.join(os.path.dirname(__file__), "fixtures", "my-bucket")
S3_PATH = os.path.join(S3_LOCAL, S3_KEY)
S3_ALPHA_PATH = os.path.join(S3_LOCAL, S3_KEY_ALPHA)
S3_NODATA_PATH = os.path.join(S3_LOCAL, S3_KEY_NODATA)
S3_MASK_PATH = os.path.join(S3_LOCAL, S3_KEY_MASK)
S3_EXTMASK_PATH = os.path.join(S3_LOCAL, S3_KEY_EXTMASK)

KEY_PIX4D = "pix4d/pix4d_alpha_nodata.tif"
PIX4D_PATH = os.path.join(S3_LOCAL, KEY_PIX4D)

COG_DST = os.path.join(os.path.dirname(__file__), "fixtures", "cog_name.tif")
COG_WEB_TILED = os.path.join(os.path.dirname(__file__), "fixtures", "web.tif")
COG_NOWEB = os.path.join(os.path.dirname(__file__), "fixtures", "noweb.tif")


with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA = toa_utils._parse_mtl_txt(f.read())


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "TRUE")


def test_tile_read_valid():
    """Should work as expected (read landsat band)."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_validResampling():
    """Should return a 1 band array and a mask."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize, resampling_method="nearest")
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_resampling_returns_different_results():
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize)
    arr2, mask2 = utils.tile_read(
        address, bounds, tilesize, resampling_method="nearest"
    )
    assert not np.array_equal(arr, arr2)


def test_resampling_with_diff_padding_returns_different_results():
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize)
    arr2, mask2 = utils.tile_read(address, bounds, tilesize, tile_edge_padding=0)
    assert not np.array_equal(arr, arr2)


def test_tile_padding_only_effects_edge_pixels():
    """Adding tile padding should effect edge pixels only."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize)
    arr2, mask2 = utils.tile_read(address, bounds, tilesize, tile_edge_padding=0)
    assert not np.array_equal(arr[0][0], arr2[0][0])
    assert np.array_equal(arr[0][5:-5][5:-5], arr2[0][5:-5][5:-5])


def test_that_tiling_ignores_padding_if_web_friendly_internal_tiles_exist():
    address = COG_WEB_TILED
    bounds = mercantile.bounds(147, 182, 9)
    tilesize = 256

    arr, mask = utils.tile_read(address, bounds, tilesize)
    arr2, mask2 = utils.tile_read(address, bounds, tilesize, tile_edge_padding=0)
    assert np.array_equal(arr, arr2)


def test_tile_read_invalidResampling():
    """Should raise an error on invalid resampling method name."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16
    with pytest.raises(KeyError):
        arr, mask = utils.tile_read(
            address, bounds, tilesize, resampling_method="jacques"
        )


def test_tile_read_list_index():
    """
    Should work as expected
    """
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=(1))
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_int_index():
    """
    Should work as expected
    """
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=1)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_rgb():
    """
    Should work as expected (read rgb)
    """
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=(3, 2, 1))
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_alpha():
    """Read masked area."""
    # non-boundless tile covering the alpha masked part
    mercator_tile = mercantile.Tile(x=876432, y=1603670, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_ALPHA_PATH, bounds, 256, indexes=(1, 2, 3))
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_internal_nodata():
    """Read masked area."""
    # non-boundless tile covering the nodata part
    mercator_tile = mercantile.Tile(x=876431, y=1603670, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_NODATA_PATH, bounds, 256, indexes=(1, 2, 3))
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_wrong_nodata():
    """Return empty mask on wrong nodata."""
    # non-boundless tile covering the nodata part
    mercator_tile = mercantile.Tile(x=438217, y=801835, z=21)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(
        S3_NODATA_PATH, bounds, 256, indexes=(1, 2, 3), nodata=1000
    )
    assert arr.shape == (3, 256, 256)
    assert mask.all()

    # Mask boundless values
    mercator_tile = mercantile.Tile(x=109554, y=200458, z=19)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(
        S3_NODATA_PATH, bounds, 256, indexes=(1, 2, 3), nodata=1000
    )
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_mask():
    """Read masked area."""
    # non-boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603669, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_MASK_PATH, bounds, 256)
    assert arr.shape == (3, 256, 256)
    assert mask.shape == (256, 256)
    assert not mask.all()

    # boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603668, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_MASK_PATH, bounds, 256)
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_extmask():
    """Read masked area."""
    # non-boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603669, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_EXTMASK_PATH, bounds, 256)
    assert arr.shape == (3, 256, 256)
    assert mask.shape == (256, 256)
    assert not mask.all()

    # boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603668, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    arr, mask = utils.tile_read(S3_MASK_PATH, bounds, 256)
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_nodata():
    """Should work as expected when forcing nodata value."""
    address = "{}_B4.TIF".format(LANDSAT_PATH)
    bounds = (
        -9040360.209344367,
        3991847.365165044,
        -9001224.450862356,
        4030983.1236470537,
    )

    tilesize = 16
    nodata = 0

    arr, mask = utils.tile_read(address, bounds, tilesize, nodata=nodata)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)
    assert not mask.all()


def test_tile_read_nodata_and_alpha():
    """Should work as expected when forcing nodata value"""
    bounds = (
        13604568.04230881,
        -333876.9395496497,
        13605791.034761373,
        -332653.9470970885,
    )

    tilesize = 16
    arr, mask = utils.tile_read(PIX4D_PATH, bounds, tilesize, indexes=[1, 2, 3])
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)
    assert not mask.all()


def test_tile_read_dataset():
    """
    Should work as expected (read rgb)
    """

    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    with rasterio.open(address) as src:
        arr, mask = utils.tile_read(src, bounds, tilesize)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)
    assert src.closed


def test_tile_read_dataset_nodata():
    """
    Should work as expected (read rgb)
    """
    # non-boundless tile covering the nodata part 22-876431-1603670
    bounds = (
        -11663535.70066358,
        4715027.644399633,
        -11663526.146035044,
        4715037.199028169,
    )
    tilesize = 16

    with rasterio.open(S3_NODATA_PATH) as src:
        arr, mask = utils.tile_read(src, bounds, tilesize)
    assert arr.shape == (3, 16, 16)
    assert not mask.all()
    assert src.closed


def test_tile_read_not_covering_the_whole_tile():
    """Should raise an error when dataset doesn't cover more than 50% of the tile."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)

    bounds = (
        -9079495.967826376,
        3991847.365165044,
        -9001224.450862356,
        4070118.882129065,
    )
    tilesize = 16
    with pytest.raises(TileOutsideBounds):
        utils.tile_read(address, bounds, tilesize, minimum_tile_cover=0.6)


def test_linear_rescale_valid():
    """
    Should work as expected (read data band)
    """

    data = np.zeros((1, 1), dtype=np.int16) + 1000
    expected_value = np.zeros((1, 1), dtype=np.int16) + 25.5
    assert (
        utils.linear_rescale(data, in_range=(0, 10000), out_range=(0, 255))
        == expected_value
    )


def test_tile_exists_valid():
    """
    Should work as expected (return true)
    """

    tile = "7-36-50"
    tile_z, tile_x, tile_y = map(int, tile.split("-"))
    bounds = [-78.75, 34.30714385628803, -75.93749999999999, 36.59788913307021]
    assert utils.tile_exists(bounds, tile_z, tile_x, tile_y)


def test_get_colormap_valid():
    """Returns 'cfastie' colormap in a PIL friendly format."""
    assert len(utils.get_colormap()) == 768  # 3 x256


def test_get_colormap_schwarzwald():
    """Returns 'schwarzwald' colormap in a GDAL friendly format."""
    assert len(utils.get_colormap(name="schwarzwald")) == 768  # 3 x256


def test_get_colormap_rplumbo():
    """Returns 'rplumbo' colormap in a GDAL friendly format."""
    assert len(utils.get_colormap(name="rplumbo")) == 768  # 3 x256


def test_get_colormap_gdal():
    """Returns 'cfastie' colormap in a GDAL friendly format."""
    assert len(utils.get_colormap(format="gdal")) == 256  # 256 x 3


def test_get_colormap_unsupported():
    """Raise error on unsupported format."""
    with pytest.raises(Exception):
        utils.get_colormap(format="gal")


def test_mapzen_elevation_rgb():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 3000, size=(512, 512))
    assert utils.mapzen_elevation_rgb(arr).shape == (3, 512, 512)


@patch("rio_tiler.landsat8.tile")
def test_expression_ndvi(landsat_tile):
    """
    Should work as expected
    """

    landsat_tile.return_value = [
        np.random.randint(0, 255, size=(2, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255,
    ]

    expr = "(b5 - b4) / (b5 + b4)"

    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = "LC08_L1TP_016037_20170813_20170814_01_RT"
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)
    assert len(landsat_tile.call_args[1].get("bands")) == 2


@patch("rio_tiler.sentinel2.tile")
def test_expression_sentinel2(sentinel2):
    """
    Should work as expected
    """

    sentinel2.return_value = [
        np.random.randint(0, 255, size=(2, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255,
    ]

    expr = "(b8A - b12) / (b8A + b12)"

    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = "S2A_tile_20170323_17SNC_0"
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)
    assert sorted(list(sentinel2.call_args[1].get("bands"))) == ["12", "8A"]


@patch("rio_tiler.landsat8.tile")
def test_expression_landsat_rgb(landsat_tile):
    """
    Should work as expected
    """

    landsat_tile.return_value = [
        np.random.randint(0, 255, size=(3, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255,
    ]

    expr = "b5*0.8, b4*1.1, b3*0.8"
    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = "LC08_L1TP_016037_20170813_20170814_01_RT"
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (3, 512, 512)
    mask.shape == (512, 512)
    assert len(landsat_tile.call_args[1].get("bands")) == 3


@patch("rio_tiler.cbers.tile")
def test_expression_cbers_rgb(cbers_tile):
    """Should read tile from CBERS data."""
    cbers_tile.return_value = [
        np.random.randint(0, 255, size=(3, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255,
    ]

    expr = "b8*0.8, b7*1.1, b6*0.8"
    tile_z = 10
    tile_x = 664
    tile_y = 495

    sceneid = "CBERS_4_MUX_20171121_057_094_L2"
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (3, 512, 512)
    mask.shape == (512, 512)
    assert len(cbers_tile.call_args[1].get("bands")) == 3


def test_expression_main_ratio():
    """Should work as expected."""
    expr = "(b3 - b2) / (b3 + b2)"
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), "fixtures")
    sceneid = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
        prefix
    )
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)

    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr=expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)


def test_expression_main_rgb():
    """
    Should work as expected
    """

    expr = "b1*0.8, b2*1.1, b3*0.8"
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), "fixtures")
    sceneid = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
        prefix
    )
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (3, 256, 256)
    mask.shape == (256, 256)


def test_expression_main_kwargs():
    """
    Should work as expected
    """

    expr = "(b3 - b2) / (b3 + b2)"
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), "fixtures")
    sceneid = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
        prefix
    )
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr, tilesize=512)
    data.shape == (1, 512, 512)
    mask.shape == (512, 512)


def test_expression_missing():
    """Should raise an exception on missing expression"""
    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    prefix = os.path.join(os.path.dirname(__file__), "fixtures")
    sceneid = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
        prefix
    )
    with pytest.raises(Exception):
        utils.expression(sceneid, tile_x, tile_y, tile_z, tilesize=512)


def test_get_vrt_transform_valid():
    """Should return correct transform and size."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )

    with rasterio.open(S3_PATH) as src:
        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(src, bounds)
    assert vrt_transform[2] == -11663507.036777973
    assert vrt_transform[5] == 4715037.199028169
    assert vrt_width == 100
    assert vrt_height == 100


def test_get_vrt_transform_deprWarning():
    """Should Warn user for bounds_crs depreciation."""
    bounds = (
        -104.77523803710938,
        38.95353532141205,
        -104.77455139160156,
        38.954069293441066,
    )
    with pytest.warns(DeprecationWarning):
        with rasterio.open(S3_PATH) as src:
            vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
                src, bounds, bounds_crs="epsg:4326"
            )

    assert vrt_transform[2] == -104.77523803710938
    assert vrt_transform[5] == 38.954069293441066
    assert vrt_width == 420
    assert vrt_height == 327


def test_get_vrt_transform_valid4326():
    """Should return correct transform and size."""
    bounds = (
        -104.77523803710938,
        38.95353532141205,
        -104.77455139160156,
        38.954069293441066,
    )
    with rasterio.open(S3_PATH) as src:
        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, dst_crs="epsg:4326"
        )

    assert vrt_transform[2] == -104.77523803710938
    assert vrt_transform[5] == 38.954069293441066
    assert vrt_width == 420
    assert vrt_height == 327


def test_statsFunction_valid():
    """Should return a valid dict with array statistics."""
    with rasterio.open(S3_ALPHA_PATH) as src:
        arr = src.read(indexes=[1], masked=True)
    stats = utils._stats(arr)
    assert stats["pc"] == [10, 200]
    assert stats["min"] == 0
    assert stats["max"] == 254
    assert int(stats["std"]) == 55
    assert len(stats["histogram"]) == 2
    assert len(stats["histogram"][0]) == 10

    stats = utils._stats(arr, percentiles=(5, 95))
    assert stats["pc"] == [31, 195]

    stats = utils._stats(arr, percentiles=(5, 95), bins=20)
    assert len(stats["histogram"][0]) == 20


def test_raster_get_stats_valid():
    """Should return a valid dict with array statistics."""
    stats = utils.raster_get_stats(S3_PATH)
    assert stats["bounds"]
    assert stats["bounds"]["crs"] == CRS({"init": "EPSG:4326"})
    assert len(stats["statistics"]) == 3
    assert stats["statistics"][1]["pc"] == [11, 199]
    assert stats["statistics"][2]["pc"] == [26, 201]
    assert stats["statistics"][3]["pc"] == [54, 192]
    assert stats["minzoom"]
    assert stats["maxzoom"]
    assert len(stats["band_descriptions"]) == 3
    assert (1, "band1") == stats["band_descriptions"][0]

    with rasterio.open(S3_PATH) as src_dst:
        stats = utils.raster_get_stats(src_dst)
        assert stats["bounds"]
        assert stats["bounds"]["crs"] == CRS({"init": "EPSG:4326"})
        assert len(stats["statistics"]) == 3
        assert stats["statistics"][1]["pc"] == [11, 199]
        assert stats["statistics"][2]["pc"] == [26, 201]
        assert stats["statistics"][3]["pc"] == [54, 192]
        assert stats["minzoom"]
        assert stats["maxzoom"]
        assert len(stats["band_descriptions"]) == 3
        assert (1, "band1") == stats["band_descriptions"][0]

    stats = utils.raster_get_stats(COG_DST)
    assert stats["minzoom"]
    assert stats["maxzoom"]
    assert len(stats["band_descriptions"]) == 1
    assert (1, "b1") == stats["band_descriptions"][0]

    stats = utils.raster_get_stats(S3_PATH, histogram_bins=20)
    assert len(stats["statistics"][1]["histogram"][0]) == 20

    stats = utils.raster_get_stats(
        S3_PATH, histogram_bins=None, histogram_range=[30, 70]
    )
    assert len(stats["statistics"][1]["histogram"][0]) == 10

    stats = utils.raster_get_stats(
        S3_PATH,
        histogram_bins=None,
        histogram_range=[30, 70],
        warp_vrt_option=dict(source_extra=10, num_threads=10),
    )
    assert len(stats["statistics"][1]["histogram"][0]) == 10


def test_raster_get_stats_validAlpha():
    """Should return a valid dict with array statistics."""
    with pytest.warns(NoOverviewWarning):
        stats = utils.raster_get_stats(S3_ALPHA_PATH)
    assert len(stats["statistics"]) == 3
    assert stats["statistics"][1]["pc"] == [10, 200]
    assert stats["statistics"][2]["pc"] == [27, 202]
    assert stats["statistics"][3]["pc"] == [55, 193]


def test_raster_get_stats_validNodata():
    """Should return a valid dict with array statistics."""
    with pytest.warns(NoOverviewWarning):
        stats = utils.raster_get_stats(S3_NODATA_PATH)
    assert stats["bounds"]
    assert len(stats["statistics"]) == 3
    assert stats["statistics"][1]["pc"] == [13, 199]
    assert stats["statistics"][2]["pc"] == [27, 202]
    assert stats["statistics"][3]["pc"] == [56, 192]

    with pytest.warns(NoOverviewWarning):
        stats = utils.raster_get_stats(S3_NODATA_PATH, nodata=0)
    assert stats["bounds"]
    assert len(stats["statistics"]) == 3
    assert stats["statistics"][1]["pc"] == [13, 199]
    assert stats["statistics"][2]["pc"] == [27, 202]
    assert stats["statistics"][3]["pc"] == [56, 192]


def test_raster_get_stats_validOptions():
    """Should return a valid dict with array statistics."""
    stats = utils.raster_get_stats(
        S3_PATH, indexes=3, overview_level=1, percentiles=(10, 90), dst_crs="epsg:3857"
    )
    assert stats["bounds"]["crs"] == "epsg:3857"
    assert len(stats["statistics"]) == 1
    assert stats["statistics"][3]["pc"] == [77, 178]

    stats = utils.raster_get_stats(S3_PATH, indexes=(3,))
    assert len(stats["statistics"]) == 1
    assert stats["statistics"][3]["pc"] == [54, 192]


def test_raster_get_stats_ovr():
    """Validate that overview level return the same result than reeading the overview."""
    resampling_method = "bilinear"
    rio_stats = utils.raster_get_stats(
        S3_PATH, overview_level=1, resampling_method=resampling_method
    )

    with rasterio.open(S3_PATH, overview_level=1) as src_dst:
        indexes = src_dst.indexes
        arr = src_dst.read(resampling=Resampling[resampling_method], masked=True)
        stats = {indexes[b]: utils._stats(arr[b], bins=10) for b in range(arr.shape[0])}
    assert rio_stats["statistics"] == stats


def test_array_to_image_valid_1band():
    """Creates PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)
    assert utils.array_to_image(arr)


def test_array_to_image_valid_colormap():
    """Creates 'colormaped' PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    cmap = utils.get_colormap(name="cfastie", format="gdal")
    assert utils.array_to_image(arr, color_map=cmap)


def test_array_to_image_valid_colormapDict():
    """Create 'colormaped' PNG image buffer from one band array using discrete cmap."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    cmap = {1: [255, 255, 255], 50: [255, 255, 0], 100: [255, 0, 0], 150: [0, 0, 255]}
    assert utils.array_to_image(arr, color_map=cmap)


def test_apply_discrete_colormap_valid():
    """Apply discrete colormap to array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    arr[0, 0, 0] = 1
    arr[0, 1, 1] = 100
    cmap = {1: [255, 255, 255], 50: [255, 255, 0], 100: [255, 0, 0], 150: [0, 0, 255]}
    res = utils._apply_discrete_colormap(arr, cmap)
    assert res[:, 0, 0].tolist() == [255, 255, 255]
    assert res[:, 1, 1].tolist() == [255, 0, 0]


def test_array_to_image_valid_mask():
    """Creates image buffer from 3 bands array and mask."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)
    assert utils.array_to_image(arr, mask=mask)
    assert utils.array_to_image(arr, mask=mask, img_format="jpeg")


def test_array_to_image_valid_options():
    """Creates image buffer with driver options."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.array_to_image(arr, mask=mask, img_format="png", ZLEVEL=9)


def test_array_to_image_geotiff16Bytes():
    """Creates GeoTIFF image buffer from 3 bands array."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint16)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.array_to_image(arr, mask=mask, img_format="GTiff")


def test_array_to_image_geotiff():
    """Creates GeoTIFF image buffer from 3 bands array."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.array_to_image(arr, mask=mask, img_format="GTiff")


@requires_webp
def test_array_to_image_valid_1bandWebp():
    """Creates WEBP image buffer from 1 band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    assert utils.array_to_image(arr, img_format="WEBP")


def test_aligned_with_internaltile():
    """Check if COG is in WebMercator and aligned with internal tiles."""
    bounds = mercantile.bounds(43, 25, 7)
    with rasterio.open(COG_DST) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256
        )

    bounds = mercantile.bounds(147, 182, 9)
    with rasterio.open(COG_NOWEB) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256
        )

    with rasterio.open(COG_WEB_TILED) as src_dst:
        assert utils._requested_tile_aligned_with_internal_tile(src_dst, bounds, 256)


# See https://github.com/cogeotiff/rio-tiler/issues/105#issuecomment-492268836
# def test_tile_read_validMask():
#     """Dataset mask should be the same as the actual mask."""
#     address = "{}_B2.TIF".format(LANDSAT_PATH)

#     bounds = (
#         -8844681.416934313,
#         3757032.814272982,
#         -8766409.899970293,
#         3835304.331237001,
#     )
#     tilesize = 128
#     arr, mask = utils.tile_read(address, bounds, tilesize, nodata=0)
#     masknodata = (arr[0] != 0).astype(np.uint8) * 255
#     np.testing.assert_array_equal(mask, masknodata)


def test_tile_read_crs():
    """Read tile using different target CRS and bounds CRS."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16

    # Test target CRS with input bounds in bounds_crs
    arr, mask = utils.tile_read(
        S3_PATH,
        bounds,
        tilesize,
        indexes=(3, 2, 1),
        dst_crs="epsg:4326",
        bounds_crs="epsg:3857",
    )
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)

    # Test target CRS with input bounds in target CRS
    bounds = (
        -104.7750663757324,
        38.95353532141203,
        -104.77489471435543,
        38.95366881479646,
    )
    arr_crs, mask_crs = utils.tile_read(
        S3_PATH, bounds, tilesize, indexes=(3, 2, 1), dst_crs="epsg:4326"
    )
    assert np.array_equal(arr, arr_crs)


def test_tile_read_vrt_option():
    """Should work as expected (read landsat band)."""
    address = "{}_B2.TIF".format(LANDSAT_PATH)
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16

    arr, mask = utils.tile_read(
        address, bounds, tilesize, warp_vrt_option=dict(source_extra=10, num_threads=10)
    )
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_find_non_alpha():
    """Return valid indexes."""
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)

    with rasterio.open(PIX4D_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)


def test_get_overview_level():
    """Test overview level calculation."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        assert utils.get_overview_level(src_dst, bounds, tilesize=8) == 2
        assert utils.get_overview_level(src_dst, bounds, tilesize=16) == 1
        assert utils.get_overview_level(src_dst, bounds, tilesize=32) == 0
        assert utils.get_overview_level(src_dst, bounds, tilesize=64) == -1
