"""tests rio_tiler.sentinel2"""

import os
import pytest
from io import BytesIO

from mock import patch

from rio_tiler import sentinel1
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidSentinelSceneId

SENTINEL_SCENE = "S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B"
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "sentinel-s1-l1c")

with open(
    "{}/GRD/2018/7/16/IW/DV/S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B/productInfo.json".format(
        SENTINEL_BUCKET
    ),
    "r",
) as f:
    SENTINEL_METADATA = f.read().encode("utf-8")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


@patch("rio_tiler.sentinel1.boto3_session")
def test_bounds_valid(session, monkeypatch):
    """Should work as expected (get bounds)"""
    monkeypatch.setattr(sentinel1, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    session.return_value.client.return_value.get_object.return_value = {
        "Body": BytesIO(SENTINEL_METADATA)
    }

    meta = sentinel1.bounds(SENTINEL_SCENE)
    assert (
        meta["sceneid"]
        == "S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B"
    )
    assert len(meta.get("bounds")) == 4


def test_parse_sceneid():
    """Test sentinel1._sentinel_parse_scene_id."""
    meta = sentinel1._sentinel_parse_scene_id(SENTINEL_SCENE)
    meta[
        "key"
    ] = "GRD/2018/7/16/IW/DV/S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B"

    with pytest.raises(InvalidSentinelSceneId):
        sentinel1._sentinel_parse_scene_id("S2A_tile_20170729_19UDP_0")


def test_metadata(monkeypatch):
    """Test sentinel1.metadata."""
    monkeypatch.setattr(sentinel1, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    meta = sentinel1.metadata(SENTINEL_SCENE, bands=("vv", "vh"))
    assert meta["sceneid"] == SENTINEL_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 2
    assert meta["statistics"]["vv"]["min"] == 4
    assert meta["statistics"]["vh"]["max"] == 730
    assert meta["minzoom"] == 7
    assert meta["maxzoom"] == 9

    meta = sentinel1.metadata(SENTINEL_SCENE, bands="vv")
    assert len(meta["statistics"].items()) == 1

    with pytest.raises(InvalidBandName):
        sentinel1.metadata(SENTINEL_SCENE, bands=("nope", "vh"))

    with pytest.raises(InvalidBandName):
        sentinel1.metadata(SENTINEL_SCENE)


def test_tile_valid_default(monkeypatch):
    """Test tile reading."""
    monkeypatch.setattr(sentinel1, "SENTINEL_BUCKET", SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 183
    tile_y = 120

    data, mask = sentinel1.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands="vv")
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)

    data, mask = sentinel1.tile(
        SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=("vv", "vh")
    )
    assert data.shape == (2, 256, 256)
    assert mask.shape == (256, 256)

    with pytest.raises(InvalidBandName):
        sentinel1.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)

    with pytest.raises(InvalidBandName):
        sentinel1.tile(
            SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=("vv", "vh", "nope")
        )

    tile_z = 8
    tile_x = 183
    tile_y = 130

    with pytest.raises(TileOutsideBounds):
        sentinel1.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=("vv"))
