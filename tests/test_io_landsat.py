"""tests rio_tiler.landsat8"""

import os
import pytest

import numpy
from mock import patch

from rio_toa import toa_utils

import rasterio
from rio_tiler.io import landsat8
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidLandsatSceneId


LANDSAT_SCENE_C1 = "LC08_L1TP_016037_20170813_20170814_01_RT"
LANDSAT_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "landsat-pds")

LANDSAT_PATH = os.path.join(
    LANDSAT_BUCKET, "c1", "L8", "016", "037", LANDSAT_SCENE_C1, LANDSAT_SCENE_C1
)

with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA = toa_utils._parse_mtl_txt(f.read())

with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA_RAW = f.read().encode("utf-8")


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("s3://landsat-pds")
    asset = asset.replace("s3://landsat-pds", LANDSAT_BUCKET)
    return rasterio.open(asset)


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "TRUE")


@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_bounds_valid(landsat_get_mtl):
    """Should work as expected (get and parse metadata)."""
    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.bounds(LANDSAT_SCENE_C1)
    assert meta.get("sceneid") == LANDSAT_SCENE_C1
    assert len(meta.get("bounds")) == 4


@patch("rio_tiler.io.landsat8.rasterio")
@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_metadata_valid_default(landsat_get_mtl, rio):
    """Get bounds and get stats for all bands."""
    landsat_get_mtl.return_value = LANDSAT_METADATA
    rio.open = mock_rasterio_open

    meta = landsat8.metadata(LANDSAT_SCENE_C1)
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 12
    assert len(meta["statistics"]["1"]["histogram"][0]) == 10
    assert list(map(int, meta["statistics"]["1"]["pc"])) == [1206, 6957]

    meta = landsat8.metadata(LANDSAT_SCENE_C1, hist_options=dict(bins=20))
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["statistics"]["1"]["histogram"][0]) == 20

    meta = landsat8.metadata(LANDSAT_SCENE_C1, hist_options=dict(range=[1000, 4000]))
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["statistics"]["1"]["histogram"][0]) == 10


@patch("rio_tiler.io.landsat8.rasterio")
@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_metadata_valid_custom(landsat_get_mtl, rio):
    """Get bounds and get stats for all bands with custom percentiles."""
    landsat_get_mtl.return_value = LANDSAT_METADATA
    rio.open = mock_rasterio_open

    meta = landsat8.metadata(LANDSAT_SCENE_C1, pmin=10, pmax=90)
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["bounds"]) == 4
    assert len(meta["statistics"].items()) == 12
    assert list(map(int, meta["statistics"]["1"]["pc"])) == [1274, 3964]


@patch("rio_tiler.io.landsat8.rasterio")
@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_tile_valid(landsat_get_mtl, rio):
    """Should work as expected."""
    landsat_get_mtl.return_value = LANDSAT_METADATA
    rio.open = mock_rasterio_open

    tile_z = 8
    tile_x = 71
    tile_y = 102

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert data.dtype == numpy.uint16
    assert mask.shape == (256, 256)
    assert not mask.all()

    data, mask = landsat8.tile(
        LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=("5", "4", "3")
    )
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands="10")
    assert data.shape == (1, 256, 256)
    assert data.dtype == numpy.uint16
    assert mask.shape == (256, 256)

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands="QA")
    assert data.shape == (1, 256, 256)
    assert data.dtype == numpy.uint16
    assert mask.shape == (256, 256)
    assert not mask.all()

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, pan=True)
    assert data.shape == (3, 256, 256)
    assert data.dtype == numpy.uint16
    assert mask.shape == (256, 256)


@patch("rio_tiler.io.landsat8.rasterio")
@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_tile_invalidband(landsat_get_mtl, rio):
    """Should raise an error on invalid band name."""
    tile_z = 8
    tile_x = 71
    tile_y = 102
    bands = "25"

    with pytest.raises(InvalidBandName):
        landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=bands)

    landsat_get_mtl.assert_not_called()


@patch("rio_tiler.io.landsat8.rasterio")
@patch("rio_tiler.io.landsat8._landsat_get_mtl")
def test_tile_invalid_bounds(landsat_get_mtl, rio):
    """Should raise an error with invalid tile"""
    landsat_get_mtl.return_value = LANDSAT_METADATA
    rio.open = mock_rasterio_open

    tile_z = 8
    tile_x = 701
    tile_y = 102

    with pytest.raises(TileOutsideBounds):
        landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z)


def test_landsat_id_pre_invalid():
    """Raises error on invalid pre-collection."""
    scene = "L0300342017083LGN00"
    with pytest.raises(InvalidLandsatSceneId):
        landsat8.landsat_parser(scene)


def test_landsat_id_c1_invalid():
    """Raises error on invalid collection1 sceneid."""
    scene = "LC08_005004_20170410_20170414_01_T1"
    with pytest.raises(InvalidLandsatSceneId):
        landsat8.landsat_parser(scene)


def test_landsat_id_pre_valid():
    """Parse landsat valid pre-collection sceneid and return metadata."""
    scene = "LC80300342017083LGN00"
    expected_content = {
        "sensor": "C",
        "satellite": "8",
        "path": "030",
        "row": "034",
        "acquisitionYear": "2017",
        "acquisitionJulianDay": "083",
        "groundStationIdentifier": "LGN",
        "archiveVersion": "00",
        "scene": "LC80300342017083LGN00",
        "date": "2017-03-24",
        "scheme": "s3",
        "bucket": "landsat-pds",
        "prefix": "L8/030/034/LC80300342017083LGN00",
    }

    assert landsat8.landsat_parser(scene) == expected_content


def test_landsat_id_c1_valid():
    """Parse landsat valid collection1 sceneid and return metadata."""
    scene = "LC08_L1TP_005004_20170410_20170414_01_T1"
    expected_content = {
        "sensor": "C",
        "satellite": "08",
        "processingCorrectionLevel": "L1TP",
        "path": "005",
        "row": "004",
        "acquisitionYear": "2017",
        "acquisitionMonth": "04",
        "acquisitionDay": "10",
        "processingYear": "2017",
        "processingMonth": "04",
        "processingDay": "14",
        "collectionNumber": "01",
        "collectionCategory": "T1",
        "scene": "LC08_L1TP_005004_20170410_20170414_01_T1",
        "date": "2017-04-10",
        "scheme": "s3",
        "bucket": "landsat-pds",
        "prefix": "c1/L8/005/004/LC08_L1TP_005004_20170410_20170414_01_T1",
    }

    assert landsat8.landsat_parser(scene) == expected_content


@patch("rio_tiler.io.landsat8.urlopen")
def test_landsat_get_mtl_valid(urlopen):
    """Return MTL metadata."""
    urlopen.return_value.read.return_value = LANDSAT_METADATA_RAW
    meta_data = landsat8._landsat_get_mtl(LANDSAT_SCENE_C1)
    assert (
        meta_data["L1_METADATA_FILE"]["METADATA_FILE_INFO"]["LANDSAT_SCENE_ID"]
        == "LC80160372017225LGN00"
    )


@patch("rio_tiler.io.landsat8.urlopen")
def test_landsat_get_mtl_invalid(urlopen):
    """Raises error when MTL file not found or empty."""
    urlopen.return_value.read.return_value = {}
    with pytest.raises(Exception):
        landsat8._landsat_get_mtl(LANDSAT_SCENE_C1)
