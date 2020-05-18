"""tests rio_tiler.sentinel2"""

import os
import pytest

from mock import patch

import rasterio
from rio_tiler.io import sentinel2

from rio_tiler.errors import (
    TileOutsideBounds,
    InvalidBandName,
    InvalidSentinelSceneId,
)

SENTINEL_SCENE = "S2A_L1C_20170729_19UDP_0"
SENTINEL_SCENE_L2 = "S2A_L2A_20170729_19UDP_0"
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "sentinel-s2")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def mock_rasterio_open(asset):
    """Mock rasterio Open for Sentinel2 dataset."""
    assert asset.startswith("s3://sentinel-s2-l")
    asset = asset.replace("s3://sentinel-s2", SENTINEL_BUCKET)
    return rasterio.open(asset)


@patch("rio_tiler.io.sentinel2.rasterio")
def test_bounds_valid(rio):
    """Should work as expected (get bounds)."""
    rio.open = mock_rasterio_open

    meta = sentinel2.bounds(SENTINEL_SCENE)
    assert meta.get("sceneid") == "S2A_L1C_20170729_19UDP_0"
    assert len(meta.get("bounds")) == 4


@patch("rio_tiler.reader.rasterio")
def test_metadata_valid_default(rio):
    """Get bounds and get stats for all bands."""
    rio.open = mock_rasterio_open

    meta = sentinel2.metadata(SENTINEL_SCENE)
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 13
    assert meta["statistics"]["01"]["pc"] == [1094, 8170]


@patch("rio_tiler.reader.rasterio")
def test_metadata_valid_custom(rio):
    """Get bounds and get stats for all bands with custom percentiles."""
    rio.open = mock_rasterio_open

    meta = sentinel2.metadata(SENTINEL_SCENE, pmin=5, pmax=95)
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 13
    assert meta["statistics"]["01"]["pc"] == [1116, 7166]

    meta = sentinel2.metadata(
        SENTINEL_SCENE, pmin=5, pmax=95, hist_options=dict(bins=20)
    )
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 13
    assert meta["statistics"]["01"]["pc"] == [1116, 7166]
    assert len(meta["statistics"]["01"]["histogram"][0]) == 20

    meta = sentinel2.metadata(SENTINEL_SCENE, hist_options=dict(range=[1000, 4000]))
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["statistics"]["01"]["histogram"][0]) == 10


@patch("rio_tiler.io.sentinel2.rasterio")
@patch("rio_tiler.reader.rasterio")
def test_tile_valid_default(rio, srio):
    """Should work as expected."""
    rio.open = mock_rasterio_open
    srio.open = mock_rasterio_open

    tile_z = 8
    tile_x = 77
    tile_y = 89

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    data, mask = sentinel2.tile(
        SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=("08", "04", "03")
    )
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands="08")
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)

    with pytest.raises(InvalidBandName):
        sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands="9A")

    tile_z = 8
    tile_x = 177
    tile_y = 89

    with pytest.raises(TileOutsideBounds):
        sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)


def test_sentinel_id_invalid():
    """Raises error on invalid sentinel-2 sceneid."""
    with pytest.raises(InvalidSentinelSceneId):
        sentinel2.sentinel2_parser("S2A_tile_20170323_17SNC")


def test_sentinel_newid_valid():
    """Parse sentinel-2 valid sceneid and return metadata."""
    expected_content = {
        "sensor": "2",
        "satellite": "A",
        "processingLevel": "L1C",
        "acquisitionYear": "2017",
        "acquisitionMonth": "07",
        "acquisitionDay": "29",
        "utm": "19",
        "lat": "U",
        "sq": "DP",
        "num": "0",
        "scene": "S2A_L1C_20170729_19UDP_0",
        "scheme": "s3",
        "bucket": "sentinel-s2-l1c",
        "prefix": "tiles/19/U/DP/2017/7/29/0",
        "preview_file": "preview.jp2",
        "preview_prefix": "",
        "bands": [
            "02",
            "03",
            "04",
            "08",
            "05",
            "06",
            "07",
            "11",
            "12",
            "8A",
            "01",
            "09",
            "10",
        ],
        "valid_bands": [
            "02",
            "03",
            "04",
            "08",
            "05",
            "06",
            "07",
            "11",
            "12",
            "8A",
            "01",
            "09",
            "10",
        ],
    }
    assert sentinel2.sentinel2_parser(SENTINEL_SCENE) == expected_content


def test_sentinel_newidl2a_valid():
    """Parse sentinel-2 valid sceneid and return metadata."""
    expected_content = {
        "sensor": "2",
        "satellite": "A",
        "processingLevel": "L2A",
        "acquisitionYear": "2017",
        "acquisitionMonth": "07",
        "acquisitionDay": "29",
        "utm": "19",
        "lat": "U",
        "sq": "DP",
        "num": "0",
        "scene": "S2A_L2A_20170729_19UDP_0",
        "scheme": "s3",
        "bucket": "sentinel-s2-l2a",
        "prefix": "tiles/19/U/DP/2017/7/29/0",
        "preview_file": "R60m/TCI.jp2",
        "preview_prefix": "R60m",
        "bands": [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "11",
            "12",
            "8A",
        ],
        "valid_bands": [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "11",
            "12",
            "8A",
            "AOT",
            "SCL",
            "WVP",
        ],
    }
    assert sentinel2.sentinel2_parser(SENTINEL_SCENE_L2) == expected_content


@patch("rio_tiler.io.sentinel2.rasterio")
def test_boundsl2_valid(rio):
    """Should work as expected (get bounds)."""
    rio.open = mock_rasterio_open

    meta = sentinel2.bounds(SENTINEL_SCENE_L2)
    assert meta.get("sceneid") == "S2A_L2A_20170729_19UDP_0"
    assert len(meta.get("bounds")) == 4


@patch("rio_tiler.reader.rasterio")
def test_metadatal2_valid_default(rio):
    """Get bounds and get stats for all bands."""
    rio.open = mock_rasterio_open

    meta = sentinel2.metadata(SENTINEL_SCENE_L2)
    assert meta["sceneid"] == SENTINEL_SCENE_L2
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 12
    assert meta["statistics"]["01"]["pc"] == [1094, 8170]


@patch("rio_tiler.io.sentinel2.rasterio")
@patch("rio_tiler.reader.rasterio")
def test_tile_validl2_default(rio, srio):
    """Should work as expected."""
    rio.open = mock_rasterio_open
    srio.open = mock_rasterio_open

    tile_z = 8
    tile_x = 77
    tile_y = 89

    data, mask = sentinel2.tile(SENTINEL_SCENE_L2, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_prefixed_bands():
    """Should work as expected."""
    assert sentinel2._l2_prefixed_band("01") == "R60m/B01"
    assert sentinel2._l2_prefixed_band("02") == "R10m/B02"
    assert sentinel2._l2_prefixed_band("06") == "R20m/B06"
    assert sentinel2._l2_prefixed_band("AOT") == "R10m/AOT"
    assert sentinel2._l2_prefixed_band("SCL") == "R20m/SCL"
