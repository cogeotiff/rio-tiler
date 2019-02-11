"""tests rio_tiler.sentinel2"""

import os
import pytest

from rio_tiler import cbers
from rio_tiler.errors import (
    TileOutsideBounds,
    InvalidBandName,
    DeprecationWarning,
    InvalidCBERSSceneId,
)

CBERS_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "cbers-pds")
CBERS_MUX_SCENE = "CBERS_4_MUX_20171121_057_094_L2"
CBERS_AWFI_SCENE = "CBERS_4_AWFI_20170420_146_129_L2"
CBERS_PAN10M_SCENE = "CBERS_4_PAN10M_20170427_161_109_L4"
CBERS_PAN5M_SCENE = "CBERS_4_PAN5M_20170425_153_114_L4"
# Currently not being used, not defining for new instruments
CBERS_MUX_PATH = os.path.join(
    CBERS_BUCKET, "CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2/"
)


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "TRUE")


def test_bounds_valid(monkeypatch):
    """
    Should work as expected (get bounds)
    """

    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    meta = cbers.bounds(CBERS_MUX_SCENE)
    assert meta.get("sceneid") == CBERS_MUX_SCENE
    assert len(meta.get("bounds")) == 4

    meta = cbers.bounds(CBERS_AWFI_SCENE)
    assert meta.get("sceneid") == CBERS_AWFI_SCENE
    assert len(meta.get("bounds")) == 4

    meta = cbers.bounds(CBERS_PAN10M_SCENE)
    assert meta.get("sceneid") == CBERS_PAN10M_SCENE
    assert len(meta.get("bounds")) == 4

    meta = cbers.bounds(CBERS_PAN5M_SCENE)
    assert meta.get("sceneid") == CBERS_PAN5M_SCENE
    assert len(meta.get("bounds")) == 4


def test_metadata_valid_default(monkeypatch):
    """Should work as expected.

    Get bounds and get histogram cuts values for all bands

    """
    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    meta = cbers.metadata(CBERS_MUX_SCENE)
    assert meta["sceneid"] == CBERS_MUX_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 4
    assert meta["statistics"]["5"]["pc"] == [28, 93]

    meta = cbers.metadata(CBERS_AWFI_SCENE)
    assert meta["sceneid"] == CBERS_AWFI_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 4

    meta = cbers.metadata(CBERS_PAN10M_SCENE)
    assert meta["sceneid"] == CBERS_PAN10M_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 3

    meta = cbers.metadata(CBERS_PAN5M_SCENE)
    assert meta["sceneid"] == CBERS_PAN5M_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 1


def test_metadata_valid_custom(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    meta = cbers.metadata(CBERS_MUX_SCENE, pmin=5, pmax=95)
    assert meta.get("sceneid") == CBERS_MUX_SCENE
    assert len(meta["bounds"]["value"]) == 4
    assert meta["statistics"]["5"]["pc"] == [29, 59]


def test_tile_valid_default(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    data, mask = cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 401
    tile_y = 585
    data, mask = cbers.tile(CBERS_AWFI_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 370
    tile_y = 535
    data, mask = cbers.tile(CBERS_PAN10M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 390
    tile_y = 547
    data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_valid_custom(monkeypatch):
    """Should return custom band combination tiles."""
    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    bands = ("8", "7", "6")
    data, mask = cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 401
    tile_y = 585
    bands = ("16", "15", "14")
    data, mask = cbers.tile(CBERS_AWFI_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 370
    tile_y = 535
    bands = ("4", "3", "2")
    data, mask = cbers.tile(CBERS_PAN10M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = ("1", "1", "1")
    data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


# TODO: Remove on 1.0.0
def test_tile_warnsInteger(monkeypatch):
    """Should warns on integer band name."""
    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = 1

    with pytest.warns(DeprecationWarning):
        data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z, bands=bands)
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)


def test_tile_valid_oneband(monkeypatch):
    """Test when passing a string instead of a tuple."""
    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = "1"

    data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_invalid_band(monkeypatch):
    """Should raise an error on invalid band name."""
    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = "21"

    with pytest.raises(InvalidBandName):
        data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z, bands=bands)


def test_tile_invalid_bounds(monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(cbers, "CBERS_BUCKET", CBERS_BUCKET)

    tile_z = 10
    tile_x = 694
    tile_y = 495

    with pytest.raises(TileOutsideBounds):
        cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z)


def test_cbers_id_invalid():
    """Raises error on invalid cbers sceneid."""
    scene = "CBERS_4_MUX_20171121_057_094"
    with pytest.raises(InvalidCBERSSceneId):
        cbers._cbers_parse_scene_id(scene)


def test_cbers_id_valid():
    """Parse valid CBERS sceneids and return metadata."""
    scene = "CBERS_4_MUX_20171121_057_094_L2"
    expected_content = {
        "acquisitionDay": "21",
        "acquisitionMonth": "11",
        "acquisitionYear": "2017",
        "instrument": "MUX",
        "key": "CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2",
        "path": "057",
        "processingCorrectionLevel": "L2",
        "row": "094",
        "mission": "4",
        "scene": "CBERS_4_MUX_20171121_057_094_L2",
        "reference_band": "6",
        "bands": ["5", "6", "7", "8"],
        "rgb": ("7", "6", "5"),
        "satellite": "CBERS",
    }

    assert cbers._cbers_parse_scene_id(scene) == expected_content

    scene = "CBERS_4_AWFI_20171121_057_094_L2"
    expected_content = {
        "acquisitionDay": "21",
        "acquisitionMonth": "11",
        "acquisitionYear": "2017",
        "instrument": "AWFI",
        "key": "CBERS4/AWFI/057/094/CBERS_4_AWFI_20171121_057_094_L2",
        "path": "057",
        "processingCorrectionLevel": "L2",
        "row": "094",
        "mission": "4",
        "scene": "CBERS_4_AWFI_20171121_057_094_L2",
        "reference_band": "14",
        "bands": ["13", "14", "15", "16"],
        "rgb": ("15", "14", "13"),
        "satellite": "CBERS",
    }

    assert cbers._cbers_parse_scene_id(scene) == expected_content

    scene = "CBERS_4_PAN10M_20171121_057_094_L2"
    expected_content = {
        "acquisitionDay": "21",
        "acquisitionMonth": "11",
        "acquisitionYear": "2017",
        "instrument": "PAN10M",
        "key": "CBERS4/PAN10M/057/094/CBERS_4_PAN10M_20171121_057_094_L2",
        "path": "057",
        "processingCorrectionLevel": "L2",
        "row": "094",
        "mission": "4",
        "scene": "CBERS_4_PAN10M_20171121_057_094_L2",
        "reference_band": "4",
        "bands": ["2", "3", "4"],
        "rgb": ("3", "4", "2"),
        "satellite": "CBERS",
    }

    assert cbers._cbers_parse_scene_id(scene) == expected_content

    scene = "CBERS_4_PAN5M_20171121_057_094_L2"
    expected_content = {
        "acquisitionDay": "21",
        "acquisitionMonth": "11",
        "acquisitionYear": "2017",
        "instrument": "PAN5M",
        "key": "CBERS4/PAN5M/057/094/CBERS_4_PAN5M_20171121_057_094_L2",
        "path": "057",
        "processingCorrectionLevel": "L2",
        "row": "094",
        "mission": "4",
        "scene": "CBERS_4_PAN5M_20171121_057_094_L2",
        "reference_band": "1",
        "bands": ["1"],
        "rgb": ("1", "1", "1"),
        "satellite": "CBERS",
    }

    assert cbers._cbers_parse_scene_id(scene) == expected_content
