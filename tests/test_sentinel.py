"""tests rio_tiler.sentinel2"""

import os
import pytest

from rio_tiler import sentinel2
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidSentinelSceneId

SENTINEL_SCENE = "S2A_tile_20170729_19UDP_0"
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "sentinel-s2-l1c")
SENTINEL_PATH = os.path.join(SENTINEL_BUCKET, "tiles/19/U/DP/2017/7/29/0/")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_bounds_valid(monkeypatch):
    """
    Should work as expected (get bounds)
    """

    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    meta = sentinel2.bounds(SENTINEL_SCENE)
    assert meta.get("sceneid") == "S2A_tile_20170729_19UDP_0"
    assert len(meta.get("bounds")) == 4


def test_metadata_valid_default(monkeypatch):
    """Get bounds and get stats for all bands."""
    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    meta = sentinel2.metadata(SENTINEL_SCENE)
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 13
    assert meta["statistics"]["01"]["pc"] == [1088, 8235]


def test_metadata_valid_custom(monkeypatch):
    """Get bounds and get stats for all bands with custom percentiles."""
    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    meta = sentinel2.metadata(SENTINEL_SCENE, pmin=5, pmax=95)
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 13
    assert meta["statistics"]["01"]["pc"] == [1110, 7236]


def test_tile_valid_default(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_valid_nrg(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89
    bands = ("08", "04", "03")

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_valid_oneband(monkeypatch):
    """Test when passing a string instead of a tuple."""
    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89
    bands = "08"

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_invalid_band(monkeypatch):
    """Should raise an error on invalid band name."""
    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89
    bands = "9A"

    with pytest.raises(InvalidBandName):
        data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=bands)


def test_tile_invalid_bounds(monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(sentinel2, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 177
    tile_y = 89

    with pytest.raises(TileOutsideBounds):
        sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)


def test_sentinel_id_invalid():
    """Raises error on invalid sentinel-2 sceneid."""
    scene = "S2A_tile_20170323_17SNC"
    with pytest.raises(InvalidSentinelSceneId):
        sentinel2._sentinel_parse_scene_id(scene)


def test_sentinel_id_valid():
    """Parse sentinel-2 valid sceneid and return metadata."""
    scene = "S2A_tile_20170323_17SNC_0"
    expected_content = {
        "acquisitionDay": "23",
        "acquisitionMonth": "03",
        "acquisitionYear": "2017",
        "key": "tiles/17/S/NC/2017/3/23/0",
        "lat": "S",
        "num": "0",
        "satellite": "A",
        "scene": "S2A_tile_20170323_17SNC_0",
        "sensor": "2",
        "sq": "NC",
        "utm": "17",
    }

    assert sentinel2._sentinel_parse_scene_id(scene) == expected_content


def test_sentinel_id_valid_strip():
    """Parse sentinel-2 valid sceneid with leading 0 and return metadata."""
    scene = "S2A_tile_20170323_07SNC_0"
    expected_content = {
        "acquisitionDay": "23",
        "acquisitionMonth": "03",
        "acquisitionYear": "2017",
        "key": "tiles/7/S/NC/2017/3/23/0",
        "lat": "S",
        "num": "0",
        "satellite": "A",
        "scene": "S2A_tile_20170323_07SNC_0",
        "sensor": "2",
        "sq": "NC",
        "utm": "07",
    }

    assert sentinel2._sentinel_parse_scene_id(scene) == expected_content
