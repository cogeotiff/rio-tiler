"""tests rio_tiler.utils"""

import os

import mercantile
import numpy as np
import pytest
import rasterio
from mock import patch

from rio_tiler import colormap, constants, utils

from .conftest import requires_webp

S3_KEY = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif"
S3_KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
S3_KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"

S3_LOCAL = PREFIX = os.path.join(os.path.dirname(__file__), "fixtures", "my-bucket")
S3_PATH = os.path.join(S3_LOCAL, S3_KEY)
S3_ALPHA_PATH = os.path.join(S3_LOCAL, S3_KEY_ALPHA)
S3_MASK_PATH = os.path.join(S3_LOCAL, S3_KEY_MASK)

KEY_PIX4D = "pix4d/pix4d_alpha_nodata.tif"
PIX4D_PATH = os.path.join(S3_LOCAL, KEY_PIX4D)

COG_DST = os.path.join(os.path.dirname(__file__), "fixtures", "cog_name.tif")
COG_WEB_TILED = os.path.join(os.path.dirname(__file__), "fixtures", "web.tif")
COG_NOWEB = os.path.join(os.path.dirname(__file__), "fixtures", "noweb.tif")
NOCOG = os.path.join(os.path.dirname(__file__), "fixtures", "nocog.tif")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_linear_rescale_valid():
    """Should work as expected (read data band)."""
    data = np.zeros((1, 1), dtype=np.int16) + 1000
    expected_value = np.zeros((1, 1), dtype=np.int16) + 25.5
    assert (
        utils.linear_rescale(data, in_range=(0, 10000), out_range=(0, 255))
        == expected_value
    )


def test_tile_exists_valid():
    """Should work as expected (return true)."""
    bounds = [-80, 34, -75, 40]
    assert utils.tile_exists(bounds, 7, 36, 50)
    assert not utils.tile_exists(bounds, 7, 36, 40)
    assert not utils.tile_exists(bounds, 7, 36, 60)
    assert not utils.tile_exists(bounds, 7, 25, 50)
    assert not utils.tile_exists(bounds, 7, 70, 50)


def test_mapzen_elevation_rgb():
    """Should work as expected."""
    arr = np.random.randint(0, 3000, size=(512, 512))
    assert utils.mapzen_elevation_rgb(arr).shape == (3, 512, 512)


@patch("rio_tiler.io.landsat8.tile")
def test_expression_ndvi(landsat_tile):
    """Should work as expected"""
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


@patch("rio_tiler.io.sentinel2.tile")
def test_expression_sentinel2(sentinel2):
    """Should work as expected."""
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


@patch("rio_tiler.io.landsat8.tile")
def test_expression_landsat_rgb(landsat_tile):
    """Should work as expected."""
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


@patch("rio_tiler.io.cbers.tile")
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
    """Should work as expected."""
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
    """Should work as expected."""
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
    """Should raise an exception on missing expression."""
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
        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, 64, 64
        )
        assert vrt_transform[2] == -11663507.036777973
        assert vrt_transform[5] == 4715037.199028169
        assert vrt_width == 100
        assert vrt_height == 100

        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, 256, 256
        )
        assert vrt_transform[2] == -11663507.036777973
        assert vrt_transform[5] == 4715037.199028169
        assert vrt_width == 256
        assert vrt_height == 256


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
            src, bounds, 256, 256, dst_crs=constants.WGS84_CRS
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


def test_render_valid_1band():
    """Creates PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)
    assert utils.render(arr)


def test_render_valid_colormap():
    """Creates 'colormaped' PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)
    cmap = colormap.get_colormap("cfastie")
    assert utils.render(arr, mask, colormap=cmap, img_format="jpeg")


def test_render_valid_colormapDict():
    """Create 'colormaped' PNG image buffer from one band array using discrete cmap."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    cmap = {
        1: [255, 255, 255, 255],
        50: [255, 255, 0, 255],
        100: [255, 0, 0, 255],
        150: [0, 0, 255, 255],
    }
    assert utils.render(arr, colormap=cmap)


def test_render_valid_mask():
    """Creates image buffer from 3 bands array and mask."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)
    assert utils.render(arr, mask=mask)
    assert utils.render(arr, mask=mask, img_format="jpeg")


def test_render_valid_options():
    """Creates image buffer with driver options."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.render(arr, mask=mask, img_format="png", ZLEVEL=9)


def test_render_geotiff16Bytes():
    """Creates GeoTIFF image buffer from 3 bands array."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint16)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.render(arr, mask=mask, img_format="GTiff")


def test_render_geotiff():
    """Creates GeoTIFF image buffer from 3 bands array."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    ops = utils.geotiff_options(1, 0, 0)
    assert utils.render(arr, mask=mask, img_format="GTiff", **ops)


@requires_webp
def test_render_valid_1bandWebp():
    """Creates WEBP image buffer from 1 band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    assert utils.render(arr, img_format="WEBP")


def test_aligned_with_internaltile():
    """Check if COG is in WebMercator and aligned with internal tiles."""
    bounds = mercantile.bounds(43, 25, 7)
    with rasterio.open(COG_DST) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256, 256
        )

    with rasterio.open(NOCOG) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256, 256
        )

    bounds = mercantile.bounds(147, 182, 9)
    with rasterio.open(COG_NOWEB) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256, 256
        )

    with rasterio.open(COG_WEB_TILED) as src_dst:
        assert utils._requested_tile_aligned_with_internal_tile(
            src_dst, bounds, 256, 256
        )


def test_find_non_alpha():
    """Return valid indexes."""
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)

    with rasterio.open(PIX4D_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)


def test_has_alpha():
    """Check if rasters have alpha bands."""
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        assert utils.has_alpha_band(src_dst)

    with rasterio.open(COG_DST) as src_dst:
        assert not utils.has_alpha_band(src_dst)


def test_has_mask():
    """Should return True."""
    with rasterio.open(S3_MASK_PATH) as src_dst:
        assert utils.has_mask_band(src_dst)

    with rasterio.open(COG_DST) as src_dst:
        assert not utils.has_mask_band(src_dst)


def test_chunck():
    """Should split a list in multiple chunks."""
    chuncks = list(utils._chunks(list(range(10)), 3))
    assert len(chuncks) == 4


def test_div():
    """Should return up rounded value."""
    assert utils._div_round_up(3, 2) == 2
    assert utils._div_round_up(2, 2) == 1


def test_ovr_level():
    """Should return the correct overview level."""
    with rasterio.open(COG_DST) as src_dst:
        # raw/-1: 2667x2658 0: 1329x1334, 1: 665x667, 2: 333x334, 3: 167x167
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 100, 100, dst_crs=src_dst.crs
            )
            == 3
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 200, 200, dst_crs=src_dst.crs
            )
            == 2
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 500, 500, dst_crs=src_dst.crs
            )
            == 1
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 800, 800, dst_crs=src_dst.crs
            )
            == 0
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 1500, 1500, dst_crs=src_dst.crs
            )
            == -1
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 3000, 3000, dst_crs=src_dst.crs
            )
            == -1
        )
