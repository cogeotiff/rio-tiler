"""tests rio_tiler.utils"""

import os

import mercantile
import numpy as np
import pytest
import rasterio
from rasterio.features import bounds as featureBounds

from rio_tiler import colormap, constants, utils
from rio_tiler.errors import RioTilerError
from rio_tiler.expression import parse_expression
from rio_tiler.io import COGReader

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
COGEO = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")


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
    # Contains
    assert utils.tile_exists(bounds, 7, 36, 50)  # bounds contains tile bounds
    assert utils.tile_exists(bounds, 3, 2, 3)  # tile bounds contains bounds

    # Intersects
    assert utils.tile_exists(bounds, 7, 35, 50)
    assert utils.tile_exists(bounds, 7, 37, 50)
    assert utils.tile_exists(bounds, 7, 36, 51)
    assert utils.tile_exists(bounds, 7, 37, 51)
    assert utils.tile_exists(bounds, 7, 35, 51)
    assert utils.tile_exists(bounds, 7, 35, 48)
    assert utils.tile_exists(bounds, 7, 37, 48)

    # Outside tiles
    assert not utils.tile_exists(bounds, 7, 36, 40)
    assert not utils.tile_exists(bounds, 7, 36, 60)
    assert not utils.tile_exists(bounds, 7, 25, 50)
    assert not utils.tile_exists(bounds, 7, 70, 50)


def test_mapzen_elevation_rgb():
    """Should work as expected."""
    arr = np.random.randint(0, 3000, size=(512, 512))
    assert utils.mapzen_elevation_rgb(arr).shape == (3, 512, 512)


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
    cmap = colormap.cmap.get("cfastie")
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


def test_cutline():
    """Test rio_tiler.utils.create_cutline."""
    feat = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-52.6025390625, 73.86761239709705],
                    [-52.6025390625, 73.59679245247814],
                    [-51.591796875, 73.60299628304274],
                    [-51.591796875, 73.90420357134279],
                    [-52.4267578125, 74.0437225981325],
                    [-52.6025390625, 73.86761239709705],
                ]
            ],
        },
    }

    feature_bounds = featureBounds(feat)

    with COGReader(COGEO) as cog:
        cutline = utils.create_cutline(cog.dataset, feat, geometry_crs="epsg:4326")
        data, mask = cog.part(feature_bounds, vrt_options={"cutline": cutline})
        assert not mask.all()

        cutline = utils.create_cutline(
            cog.dataset, feat["geometry"], geometry_crs="epsg:4326"
        )
        data, mask = cog.part(feature_bounds, vrt_options={"cutline": cutline})
        assert not mask.all()

    feat_line = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-55.37109374999999, 74.17607298699065],
                [-53.85498046874999, 75.06734898853098],
                [-54.16259765625, 75.11822201684025],
                [-54.228515625, 75.23066741281573],
            ],
        },
    }

    with COGReader(COGEO) as cog:
        with pytest.raises(RioTilerError):
            utils.create_cutline(cog.dataset, feat_line, geometry_crs="epsg:4326")


def test_parse_expression():
    """test parsing rio-tiler expression."""
    assert sorted(parse_expression("b1*b11+b3,b1*b2+B4")) == [1, 2, 3, 4, 11]
    assert sorted(parse_expression("b1*b11+b3,b1*b2+B4", cast=False)) == [
        "1",
        "11",
        "2",
        "3",
        "4",
    ]
