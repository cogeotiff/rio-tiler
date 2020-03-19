"""tests rio_tiler.reader"""

import os
import pytest

import numpy
import mercantile

import rasterio

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.errors import TileOutsideBounds, AlphaBandWarning


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

COG_WEB_TILED = os.path.join(os.path.dirname(__file__), "fixtures", "web.tif")
COG_SCALE = os.path.join(os.path.dirname(__file__), "fixtures", "cog_scale.tif")
COG_CMAP = os.path.join(os.path.dirname(__file__), "fixtures", "cog_cmap.tif")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_tile_read_valid():
    """Should work as expected (read landsat band)."""
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_validResampling():
    """Should return a 1 band array and a mask."""
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, resampling_method="nearest")
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_resampling_returns_different_results():
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, _ = reader.part(src_dst, bounds, 16, 16)
        arr2, _ = reader.part(src_dst, bounds, 16, 16, resampling_method="nearest")

    assert not numpy.array_equal(arr, arr2)


def test_resampling_with_diff_padding_returns_different_results():
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, _ = reader.part(src_dst, bounds, 32, 32, nodata=0)
        arr2, _ = reader.part(src_dst, bounds, 32, 32, nodata=0, padding=2)

    assert not numpy.array_equal(arr, arr2)


# This is NOT TRUE, padding affects the whole array not just the border.
# def test_tile_padding_only_effects_edge_pixels():
#     """Adding tile padding should effect edge pixels only."""
#     bounds = (
#         -8844681.416934313,
#         3757032.814272982,
#         -8766409.899970293,
#         3835304.331237001,
#     )
#     with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
#         arr, _ = reader.part(src_dst, bounds, 32, 32, nodata=0)
#         arr2, _ = reader.part(src_dst, bounds, 32, 32, nodata=0, padding=2)
#     assert not np.array_equal(arr[0][0], arr2[0][0])
#     assert np.array_equal(arr[0][5:-5][5:-5], arr2[0][5:-5][5:-5])


def test_that_tiling_ignores_padding_if_web_friendly_internal_tiles_exist():
    """Ignore Padding when COG is aligned."""
    with rasterio.open(COG_WEB_TILED) as src_dst:
        arr, _ = reader.tile(src_dst, 147, 182, 9, tilesize=256, padding=0)
        arr2, _ = reader.tile(src_dst, 147, 182, 9, tilesize=256, padding=100)
    assert numpy.array_equal(arr, arr2)


def test_tile_read_invalidResampling():
    """Should raise an error on invalid resampling method name."""
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    with pytest.raises(KeyError):
        with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
            reader.part(src_dst, bounds, 16, 16, resampling_method="jacques")


def test_tile_read_tuple_index():
    """Should work as expected"""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=(1,))
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_int_index():
    """Should work as expected."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=1)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_bgr():
    """Should work as expected (read rgb)"""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=(3, 2, 1))
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_alpha():
    """Read masked area."""
    # non-boundless tile covering the alpha masked part
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        arr, mask = reader.tile(
            src_dst, 876432, 1603670, 22, tilesize=256, indexes=(1, 2, 3)
        )
    assert arr.shape == (3, 256, 256)
    assert not mask.all()

    with pytest.warns(AlphaBandWarning):
        with rasterio.open(S3_ALPHA_PATH) as src_dst:
            nb = src_dst.count
            arr, mask = reader.tile(src_dst, 876432, 1603670, 22, tilesize=256)
    assert not nb == arr.shape[0]
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_internal_nodata():
    """Read masked area."""
    # non-boundless tile covering the nodata part
    with rasterio.open(S3_NODATA_PATH) as src_dst:
        arr, mask = reader.tile(
            src_dst, 876431, 1603670, 22, tilesize=256, indexes=(1, 2, 3)
        )
    assert arr.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_read_wrong_nodata():
    """Return empty mask on wrong nodata."""
    # non-boundless tile covering the nodata part
    with rasterio.open(S3_NODATA_PATH) as src_dst:
        arr, mask = reader.tile(
            src_dst, 438217, 801835, 21, tilesize=256, indexes=(1, 2, 3), nodata=1000
        )
        assert arr.shape == (3, 256, 256)
        assert mask.all()

        # Mask boundless values
        arr, mask = reader.tile(
            src_dst, 109554, 200458, 19, tilesize=256, indexes=(1, 2, 3), nodata=1000
        )
        assert arr.shape == (3, 256, 256)
        assert not mask.all()


def test_tile_read_mask():
    """Read masked area."""
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR"):
        # non-boundless tile covering the masked part
        with rasterio.open(S3_MASK_PATH) as src_dst:
            arr, mask = reader.tile(src_dst, 876431, 1603669, 22, tilesize=16)
        assert arr.shape == (3, 16, 16)
        assert mask.shape == (16, 16)
        assert not mask.all()

        # boundless tile covering the masked part
        with rasterio.open(S3_MASK_PATH) as src_dst:
            arr, mask = reader.tile(src_dst, 876431, 1603668, 22, tilesize=256)
        assert arr.shape == (3, 256, 256)
        assert not mask.all()


def test_tile_read_extmask():
    """Read masked area."""
    # non-boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603669, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="TRUE"):
        with rasterio.open(S3_EXTMASK_PATH) as src_dst:
            arr, mask = reader.part(src_dst, bounds, 256, 256)
        assert arr.shape == (3, 256, 256)
        assert mask.shape == (256, 256)
        assert not mask.all()

    # boundless tile covering the masked part
    mercator_tile = mercantile.Tile(x=876431, y=1603668, z=22)
    bounds = mercantile.xy_bounds(mercator_tile)
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR"):
        with rasterio.open(S3_MASK_PATH) as src_dst:
            arr, mask = reader.part(src_dst, bounds, 256, 256)
        assert arr.shape == (3, 256, 256)
        assert not mask.all()


def test_tile_read_nodata():
    """Should work as expected when forcing nodata value."""
    bounds = (
        -9040360.209344367,
        3991847.365165044,
        -9001224.450862356,
        4030983.1236470537,
    )

    tilesize = 16
    with rasterio.open(f"{LANDSAT_PATH}_B4.TIF") as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, nodata=0)
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
    with rasterio.open(PIX4D_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, indexes=[1, 2, 3])
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)
    assert not mask.all()


def test_tile_read_dataset():
    """Should work as expected"""
    address = f"{LANDSAT_PATH}_B2.TIF"
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16
    with rasterio.open(address) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_dataset_nodata():
    """Should work as expected (read rgb)"""
    # non-boundless tile covering the nodata part 22-876431-1603670
    bounds = (
        -11663535.70066358,
        4715027.644399633,
        -11663526.146035044,
        4715037.199028169,
    )
    tilesize = 16
    with rasterio.open(S3_NODATA_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize)
    assert arr.shape == (3, 16, 16)
    assert not mask.all()


def test_tile_read_not_covering_the_whole_tile():
    """Should raise an error when dataset doesn't cover more than 50% of the tile."""
    bounds = (
        -9079495.967826376,
        3991847.365165044,
        -9001224.450862356,
        4070118.882129065,
    )
    tilesize = 16
    with pytest.raises(TileOutsideBounds):
        with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
            reader.part(src_dst, bounds, tilesize, tilesize, minimum_overlap=0.6)


# See https://github.com/cogeotiff/rio-tiler/issues/105#issuecomment-492268836
def test_tile_read_validMask():
    """Dataset mask should be the same as the actual mask."""
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 128
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, nodata=0)

    masknodata = (arr[0] != 0).astype(numpy.uint8) * 255
    numpy.testing.assert_array_equal(mask, masknodata)


def test_tile_read_crs():
    """Read tile using different target CRS and bounds CRS."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16
    with rasterio.open(S3_PATH) as src_dst:
        # Test target CRS with input bounds in bounds_crs
        arr, mask = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            indexes=(3, 2, 1),
            dst_crs=constants.WGS84_CRS,
            bounds_crs=constants.WEB_MERCATOR_CRS,
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
        arr_crs, _ = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            indexes=(3, 2, 1),
            dst_crs=constants.WGS84_CRS,
        )

        assert numpy.array_equal(arr, arr_crs)


def test_tile_read_vrt_option():
    """Should work as expected (read landsat band)."""
    bounds = (
        -8844681.416934313,
        3757032.814272982,
        -8766409.899970293,
        3835304.331237001,
    )
    tilesize = 16
    with rasterio.open(f"{LANDSAT_PATH}_B2.TIF") as src_dst:
        arr, mask = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            warp_vrt_option=dict(source_extra=10, num_threads=10),
        )
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_read_unscale():
    """Should or Shouldn't apply scale and offset to a data."""
    with rasterio.open(COG_SCALE) as src_dst:
        arr, mask = reader.tile(src_dst, 218, 99, 8, tilesize=128)
        arrS, maskS = reader.tile(src_dst, 218, 99, 8, tilesize=128, unscale=True)

        assert arr.dtype == "int16"
        assert arrS.dtype == "float32"
        assert not numpy.array_equal(arr, arrS)
        numpy.testing.assert_array_equal(mask, maskS)

        meta = reader.metadata(src_dst)
        assert isinstance(meta["statistics"][1]["min"], int)

        meta = reader.metadata(src_dst, unscale=True)
        assert isinstance(meta["statistics"][1]["min"], float)

        p = reader.point(src_dst, [310000, 4100000], coord_crs=src_dst.crs)
        assert p == [8917]

        p = reader.point(
            src_dst, [310000, 4100000], coord_crs=src_dst.crs, unscale=True
        )
        assert round(p[0], 3) == 1000.892


def test_point():
    """Read point values"""
    with rasterio.open(COG_SCALE) as src_dst:
        p = reader.point(src_dst, [310000, 4100000], coord_crs=src_dst.crs, indexes=1)
        assert p == [8917]

        p = reader.point(src_dst, [310000, 4100000], coord_crs=src_dst.crs)
        assert p == [8917]

        with pytest.raises(Exception):
            reader.point(src_dst, [810000, 4100000], coord_crs=src_dst.crs)


def test_metadata():
    """Should return correct metadata."""
    with rasterio.open(COG_CMAP) as src_dst:
        meta = reader.metadata(src_dst)
        assert meta["dtype"] == "int8"
        assert meta["colorinterp"] == ["palette"]
        assert not meta.get("scale")
        assert not meta.get("ofsset")
        assert meta.get("colormap")

    with rasterio.open(COG_SCALE) as src_dst:
        meta = reader.metadata(src_dst)
        assert meta["dtype"] == "int16"
        assert meta["colorinterp"] == ["gray"]
        assert meta["scale"] == 0.0001
        assert meta["offset"] == 1000.0
        assert meta["band_descriptions"] == [(1, "Green")]
        assert not meta.get("colormap")
        assert meta["nodata_type"] == "Nodata"

        meta = reader.metadata(src_dst, indexes=1)
        assert meta["colorinterp"] == ["gray"]

        bounds = mercantile.bounds(mercantile.Tile(x=218, y=99, z=8))
        meta = reader.metadata(src_dst, bounds)
        assert meta["colorinterp"] == ["gray"]
        assert meta["bounds"] == bounds

    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        with pytest.warns(AlphaBandWarning):
            meta = reader.metadata(src_dst)
            assert len(meta["band_descriptions"]) == 3
            assert meta["colorinterp"] == ["red", "green", "blue"]
            assert meta["nodata_type"] == "Alpha"

        meta = reader.metadata(src_dst, indexes=(1, 2, 3, 4))
        assert len(meta["band_descriptions"]) == 4
        assert meta["colorinterp"] == ["red", "green", "blue", "alpha"]
        assert meta["nodata_type"] == "Alpha"

    with rasterio.open(S3_MASK_PATH) as src_dst:
        meta = reader.metadata(src_dst)
        assert meta["nodata_type"] == "Mask"
