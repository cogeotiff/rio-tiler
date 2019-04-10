"""tests rio_tiler.landsat8"""

import os
import pytest

from mock import patch

from rasterio.crs import CRS
from rio_toa import toa_utils

from rio_tiler import landsat8
from rio_tiler.errors import (
    TileOutsideBounds,
    InvalidBandName,
    NoOverviewWarning,
    InvalidLandsatSceneId,
)

LANDSAT_SCENE_C1 = "LC08_L1TP_016037_20170813_20170814_01_RT"
LANDSAT_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "landsat-pds")

LANDSAT_PATH = os.path.join(
    LANDSAT_BUCKET, "c1", "L8", "016", "037", LANDSAT_SCENE_C1, LANDSAT_SCENE_C1
)

with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA = toa_utils._parse_mtl_txt(f.read())

with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA_RAW = f.read().encode("utf-8")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "TRUE")


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_bounds_valid(landsat_get_mtl):
    """
    Should work as expected (get and parse metadata)
    """

    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.bounds(LANDSAT_SCENE_C1)
    assert meta.get("sceneid") == LANDSAT_SCENE_C1
    assert len(meta.get("bounds")) == 4


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_metadata_valid_default(landsat_get_mtl, monkeypatch):
    """Get bounds and get stats for all bands."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.metadata(LANDSAT_SCENE_C1)
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 11
    assert len(meta["statistics"]["1"]["histogram"][0]) == 10
    assert list(map(int, meta["statistics"]["1"]["pc"])) == [1210, 7046]

    meta = landsat8.metadata(LANDSAT_SCENE_C1, histogram_bins=20)
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["statistics"]["1"]["histogram"][0]) == 20

    meta = landsat8.metadata(
        LANDSAT_SCENE_C1, histogram_bins=None, histogram_range=[1000, 4000]
    )
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["statistics"]["1"]["histogram"][0]) == 10


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_metadata_valid_custom(landsat_get_mtl, monkeypatch):
    """Get bounds and get stats for all bands with custom percentiles."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.metadata(LANDSAT_SCENE_C1, pmin=10, pmax=90)
    assert meta["sceneid"] == LANDSAT_SCENE_C1
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 11
    assert list(map(int, meta["statistics"]["1"]["pc"])) == [1275, 3918]


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_valid_default(landsat_get_mtl, monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 71
    tile_y = 102

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_valid_nrg(landsat_get_mtl, monkeypatch):
    """Should return a custom band combination tile."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 71
    tile_y = 102
    bands = ("5", "4", "3")
    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_valid_tir(landsat_get_mtl, monkeypatch):
    """Should return a tile and mask from TIR band."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 71
    tile_y = 102
    bands = "10"

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_invalidband(landsat_get_mtl, monkeypatch):
    """Should raise an error on invalid band name."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)

    tile_z = 8
    tile_x = 71
    tile_y = 102
    bands = "25"

    with pytest.raises(InvalidBandName):
        data, mask = landsat8.tile(
            LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=bands
        )
    landsat_get_mtl.assert_not_called()


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_valid_pan(landsat_get_mtl, monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 71
    tile_y = 102

    data, mask = landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, pan=True)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


@patch("rio_tiler.landsat8._landsat_get_mtl")
def test_tile_invalid_bounds(landsat_get_mtl, monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 701
    tile_y = 102

    with pytest.raises(TileOutsideBounds):
        landsat8.tile(LANDSAT_SCENE_C1, tile_x, tile_y, tile_z)


def test_landsat_id_pre_invalid():
    """Raises error on invalid pre-collection."""
    scene = "L0300342017083LGN00"
    with pytest.raises(InvalidLandsatSceneId):
        landsat8._landsat_parse_scene_id(scene)


def test_landsat_id_c1_invalid():
    """Raises error on invalid collection1 sceneid."""
    scene = "LC08_005004_20170410_20170414_01_T1"
    with pytest.raises(InvalidLandsatSceneId):
        landsat8._landsat_parse_scene_id(scene)


def test_landsat_id_pre_valid():
    """Parse landsat valid pre-collection sceneid and return metadata."""
    scene = "LC80300342017083LGN00"
    expected_content = {
        "acquisitionJulianDay": "083",
        "acquisitionYear": "2017",
        "archiveVersion": "00",
        "date": "2017-03-24",
        "groundStationIdentifier": "LGN",
        "key": "L8/030/034/LC80300342017083LGN00/LC80300342017083LGN00",
        "path": "030",
        "row": "034",
        "satellite": "8",
        "scene": "LC80300342017083LGN00",
        "sensor": "C",
    }

    assert landsat8._landsat_parse_scene_id(scene) == expected_content


def test_landsat_id_c1_valid():
    """Parse landsat valid collection1 sceneid and return metadata."""
    scene = "LC08_L1TP_005004_20170410_20170414_01_T1"
    expected_content = {
        "acquisitionDay": "10",
        "acquisitionMonth": "04",
        "acquisitionYear": "2017",
        "collectionCategory": "T1",
        "collectionNumber": "01",
        "date": "2017-04-10",
        "key": "c1/L8/005/004/LC08_L1TP_005004_20170410_\
20170414_01_T1/LC08_L1TP_005004_20170410_20170414_01_T1",
        "path": "005",
        "processingCorrectionLevel": "L1TP",
        "processingDay": "14",
        "processingMonth": "04",
        "processingYear": "2017",
        "row": "004",
        "satellite": "08",
        "scene": "LC08_L1TP_005004_20170410_20170414_01_T1",
        "sensor": "C",
    }

    assert landsat8._landsat_parse_scene_id(scene) == expected_content


@patch("rio_tiler.landsat8.urlopen")
def test_landsat_get_mtl_valid(urlopen):
    """Return MTL metadata."""
    urlopen.return_value.read.return_value = LANDSAT_METADATA_RAW
    meta_data = landsat8._landsat_get_mtl(LANDSAT_SCENE_C1)
    assert (
        meta_data["L1_METADATA_FILE"]["METADATA_FILE_INFO"]["LANDSAT_SCENE_ID"]
        == "LC80160372017225LGN00"
    )


@patch("rio_tiler.landsat8.urlopen")
def test_landsat_get_mtl_invalid(urlopen):
    """Raises error when MTL file not found or empty."""
    urlopen.return_value.read.return_value = {}
    with pytest.raises(Exception):
        landsat8._landsat_get_mtl(LANDSAT_SCENE_C1)


def test_landsat_get_stats_valid():
    """Should return a valid dict with array statistics."""
    stats = landsat8._landsat_stats(
        "4", LANDSAT_PATH, LANDSAT_METADATA["L1_METADATA_FILE"]
    )
    assert stats["bounds"]
    assert stats["bounds"]["crs"] == CRS({"init": "EPSG:4326"})
    assert stats["statistics"]["4"]
    assert isinstance(stats["statistics"]["4"]["pc"][0], float)
    assert list(map(int, stats["statistics"]["4"]["pc"])) == [423, 7028]


def test_landsat_get_stats_validOptions():
    """Should return a valid dict with array statistics."""
    stats = landsat8._landsat_stats(
        "10",
        LANDSAT_PATH,
        LANDSAT_METADATA["L1_METADATA_FILE"],
        overview_level=2,
        percentiles=(5, 95),
        dst_crs="epsg:3857",
    )
    assert stats["bounds"]
    assert stats["bounds"]["crs"] == "epsg:3857"
    assert stats["statistics"]["10"]
    assert list(map(int, stats["statistics"]["10"]["pc"])) == [281, 297]


def test_landsat_get_stats_noOverviews(monkeypatch):
    """Should return a valid dict with array statistics and warns about missing overviews."""
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")
    with pytest.warns(NoOverviewWarning):
        stats = landsat8._landsat_stats(
            "5", LANDSAT_PATH, LANDSAT_METADATA["L1_METADATA_FILE"]
        )
        assert stats["statistics"]["5"]
