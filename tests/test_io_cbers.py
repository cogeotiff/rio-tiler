"""tests rio_tiler.sentinel2"""

import os

import pytest
import rasterio
from mock import patch

from rio_tiler.errors import InvalidBandName, InvalidCBERSSceneId, TileOutsideBounds
from rio_tiler.io import cbers

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


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("s3://cbers-pds")
    asset = asset.replace("s3://cbers-pds", CBERS_BUCKET)
    return rasterio.open(asset)


@patch("rio_tiler.io.cbers.rasterio")
def test_bounds_valid(rio):
    """Should work as expected (get bounds)"""
    rio.open = mock_rasterio_open

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


@patch("rio_tiler.reader.rasterio")
def test_metadata_valid_default(rio):
    """
    Should work as expected.

    Get bounds and get histogram cuts values for all bands

    """
    rio.open = mock_rasterio_open

    meta = cbers.metadata(CBERS_MUX_SCENE)
    assert meta["sceneid"] == CBERS_MUX_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 4
    assert meta["statistics"]["5"]["pc"] == [28, 98]

    meta = cbers.metadata(CBERS_MUX_SCENE, hist_options=dict(bins=20))
    assert meta["sceneid"] == CBERS_MUX_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 4
    assert len(meta["statistics"]["5"]["histogram"][0]) == 20
    assert meta["statistics"]["5"]["pc"] == [28, 98]

    meta = cbers.metadata(CBERS_AWFI_SCENE)
    assert meta["sceneid"] == CBERS_AWFI_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 4

    meta = cbers.metadata(CBERS_PAN10M_SCENE)
    assert meta["sceneid"] == CBERS_PAN10M_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 3

    meta = cbers.metadata(CBERS_PAN5M_SCENE)
    assert meta["sceneid"] == CBERS_PAN5M_SCENE
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 1


@patch("rio_tiler.reader.rasterio")
def test_metadata_valid_custom(rio):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """
    rio.open = mock_rasterio_open

    meta = cbers.metadata(CBERS_MUX_SCENE, pmin=5, pmax=95)
    assert meta.get("sceneid") == CBERS_MUX_SCENE
    assert len(meta["bounds"]) == 4
    assert meta["statistics"]["5"]["pc"] == [30, 61]


@patch("rio_tiler.reader.rasterio")
@patch("rio_tiler.io.cbers.rasterio")
def test_tile_valid_default(crio, rio):
    """Should work as expected"""
    crio.open = mock_rasterio_open
    rio.open = mock_rasterio_open

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


@patch("rio_tiler.reader.rasterio")
@patch("rio_tiler.io.cbers.rasterio")
def test_tile_valid_custom(crio, rio):
    """Should return custom band combination tiles."""
    crio.open = mock_rasterio_open
    rio.open = mock_rasterio_open

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


@patch("rio_tiler.reader.rasterio")
@patch("rio_tiler.io.cbers.rasterio")
def test_tile_valid_oneband(crio, rio):
    """Test when passing a string instead of a tuple."""
    crio.open = mock_rasterio_open
    rio.open = mock_rasterio_open

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = "1"

    data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


@patch("rio_tiler.reader.rasterio")
@patch("rio_tiler.io.cbers.rasterio")
def test_tile_invalid_band(crio, rio):
    """Should raise an error on invalid band name."""
    crio.open = mock_rasterio_open
    rio.open = mock_rasterio_open

    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = "21"

    with pytest.raises(InvalidBandName):
        cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z, bands=bands)


@patch("rio_tiler.reader.rasterio")
@patch("rio_tiler.io.cbers.rasterio")
def test_tile_invalid_bounds(crio, rio):
    """Should raise an error with invalid tile."""
    crio.open = mock_rasterio_open
    rio.open = mock_rasterio_open

    tile_z = 10
    tile_x = 694
    tile_y = 495

    with pytest.raises(TileOutsideBounds):
        cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z)


def test_cbers_id_invalid():
    """Raises error on invalid cbers sceneid."""
    scene = "CBERS_4_MUX_20171121_057_094"
    with pytest.raises(InvalidCBERSSceneId):
        cbers.cbers_parser(scene)


def test_cbers_id_valid():
    """Parse valid CBERS sceneids and return metadata."""
    scene = "CBERS_4_MUX_20171121_057_094_L2"
    expected_content = {
        "satellite": "CBERS",
        "mission": "4",
        "instrument": "MUX",
        "acquisitionYear": "2017",
        "acquisitionMonth": "11",
        "acquisitionDay": "21",
        "path": "057",
        "row": "094",
        "processingCorrectionLevel": "L2",
        "scene": "CBERS_4_MUX_20171121_057_094_L2",
        "reference_band": "6",
        "bands": ("5", "6", "7", "8"),
        "rgb": ("7", "6", "5"),
        "scheme": "s3",
        "bucket": "cbers-pds",
        "prefix": "CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2",
    }

    assert cbers.cbers_parser(scene) == expected_content

    scene = "CBERS_4_AWFI_20171121_057_094_L2"
    expected_content = {
        "satellite": "CBERS",
        "mission": "4",
        "instrument": "AWFI",
        "acquisitionYear": "2017",
        "acquisitionMonth": "11",
        "acquisitionDay": "21",
        "path": "057",
        "row": "094",
        "processingCorrectionLevel": "L2",
        "scene": "CBERS_4_AWFI_20171121_057_094_L2",
        "reference_band": "14",
        "bands": ("13", "14", "15", "16"),
        "rgb": ("15", "14", "13"),
        "scheme": "s3",
        "bucket": "cbers-pds",
        "prefix": "CBERS4/AWFI/057/094/CBERS_4_AWFI_20171121_057_094_L2",
    }

    assert cbers.cbers_parser(scene) == expected_content

    scene = "CBERS_4_PAN10M_20171121_057_094_L2"
    expected_content = {
        "satellite": "CBERS",
        "mission": "4",
        "instrument": "PAN10M",
        "acquisitionYear": "2017",
        "acquisitionMonth": "11",
        "acquisitionDay": "21",
        "path": "057",
        "row": "094",
        "processingCorrectionLevel": "L2",
        "scene": "CBERS_4_PAN10M_20171121_057_094_L2",
        "reference_band": "4",
        "bands": ("2", "3", "4"),
        "rgb": ("3", "4", "2"),
        "scheme": "s3",
        "bucket": "cbers-pds",
        "prefix": "CBERS4/PAN10M/057/094/CBERS_4_PAN10M_20171121_057_094_L2",
    }

    assert cbers.cbers_parser(scene) == expected_content

    scene = "CBERS_4_PAN5M_20171121_057_094_L2"
    expected_content = {
        "satellite": "CBERS",
        "mission": "4",
        "instrument": "PAN5M",
        "acquisitionYear": "2017",
        "acquisitionMonth": "11",
        "acquisitionDay": "21",
        "path": "057",
        "row": "094",
        "processingCorrectionLevel": "L2",
        "scene": "CBERS_4_PAN5M_20171121_057_094_L2",
        "reference_band": "1",
        "bands": ("1"),
        "rgb": ("1", "1", "1"),
        "scheme": "s3",
        "bucket": "cbers-pds",
        "prefix": "CBERS4/PAN5M/057/094/CBERS_4_PAN5M_20171121_057_094_L2",
    }

    assert cbers.cbers_parser(scene) == expected_content
