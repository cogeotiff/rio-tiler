"""tests rio_tiler.io.stac"""

import json
import os

import pytest
import rasterio
from mock import patch

from rio_tiler.errors import InvalidBandName, TileOutsideBounds

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

with open(os.path.join(PREFIX, "stac.json")) as f:
    stac_item = json.loads(f.read())


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("http://somewhere-over-the-rainbow.io")
    asset = asset.replace("http://somewhere-over-the-rainbow.io", PREFIX)
    return rasterio.open(asset)


@pytest.fixture(autouse=True)
def app(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")

    from rio_tiler.io import stac

    return stac


def test_spatial_info_valid(app):
    """Should raise an exception."""
    with pytest.raises(Exception):
        app.spatial_info(stac_item)


def test_bounds_valid(app):
    """Should work as expected (get bounds)"""
    meta = app.bounds(stac_item)
    assert meta["id"] == stac_item["id"]
    assert len(meta["bounds"]) == 4


@patch("rio_tiler.reader.rasterio")
def test_metadata_valid(rio, app):
    """Get bounds and get stats for all bands."""
    rio.open = mock_rasterio_open

    with pytest.raises(InvalidBandName):
        app.metadata(stac_item, "vert")

    meta = app.metadata(stac_item, "green")
    assert meta["id"] == stac_item["id"]
    assert len(meta["bounds"]) == 4
    assert meta["band_descriptions"][0] == (1, "green")
    assert len(meta["statistics"].items()) == 1
    assert meta["nodata_types"] == {"green": "Nodata"}
    assert meta["dtypes"] == {"green": "uint16"}

    meta = app.metadata(stac_item, ["green", "red", "blue"])
    assert meta["id"] == stac_item["id"]
    assert len(meta["bounds"]) == 4
    assert meta["band_descriptions"] == [(1, "green"), (2, "red"), (3, "blue")]
    assert len(meta["statistics"].items()) == 3
    assert meta["nodata_types"] == {
        "green": "Nodata",
        "red": "Nodata",
        "blue": "Nodata",
    }


@patch("rio_tiler.reader.rasterio")
def test_tile_valid(rio, app):
    """Should raise or return tiles."""
    rio.open = mock_rasterio_open

    with pytest.raises(TileOutsideBounds):
        app.tile(stac_item, "green", 701, 102, 8)

    data, mask = app.tile(stac_item, "green", 71, 102, 8)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)
