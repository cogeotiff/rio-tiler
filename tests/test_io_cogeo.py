"""tests rio_tiler.base"""

import os
import pytest

from rio_tiler.io import cogeo
from rio_tiler.errors import TileOutsideBounds

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
ADDRESS = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
    PREFIX
)
COG_TAGS = os.path.join(os.path.dirname(__file__), "fixtures", "cog_tags.tif")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_spatial_info_valid():
    """Should work as expected (get spatial info)"""
    meta = cogeo.spatial_info(ADDRESS)
    assert meta.get("address")
    assert meta.get("minzoom")
    assert meta.get("maxzoom")
    assert meta.get("center")
    assert len(meta.get("bounds")) == 4


def test_bounds_valid():
    """Should work as expected (get bounds)"""
    meta = cogeo.bounds(ADDRESS)
    assert meta.get("address") == ADDRESS
    assert len(meta.get("bounds")) == 4


def test_info_valid():
    """Should work as expected (get file info)"""
    meta = cogeo.info(COG_TAGS)
    assert meta.get("address") == COG_TAGS
    assert meta.get("bounds")
    assert meta.get("minzoom")
    assert meta.get("maxzoom")
    assert meta.get("band_descriptions")
    assert meta.get("dtype") == "int16"
    assert meta.get("colorinterp") == ["gray"]
    assert meta.get("nodata_type") == "Nodata"
    assert meta.get("scale")
    assert meta.get("offset")
    assert meta.get("band_metadata")
    bmeta = meta.get("band_metadata")[0][1]
    assert bmeta.get("STATISTICS_MAXIMUM")
    assert bmeta.get("STATISTICS_MEAN")
    assert bmeta.get("STATISTICS_MINIMUM")


def test_metadata_valid():
    """Get bounds and get stats for all bands."""
    meta = cogeo.metadata(ADDRESS)
    assert meta["address"] == ADDRESS
    assert len(meta["band_descriptions"]) == 3
    assert (1, "band1") == meta["band_descriptions"][0]
    assert len(meta["statistics"].items()) == 3
    assert meta["statistics"][1]["pc"] == [12, 198]


def test_metadata_valid_custom():
    """Get bounds and get stats for all bands with custom percentiles."""
    meta = cogeo.metadata(
        ADDRESS, pmin=5, pmax=90, hist_options=dict(bins=20), max_size=128
    )
    assert meta["address"] == ADDRESS
    assert len(meta["statistics"].items()) == 3
    assert len(meta["statistics"][1]["histogram"][0]) == 20
    assert meta["statistics"][1]["pc"] == [41, 184]


def test_tile_valid_default():
    """Should return a 3 bands array and a full valid mask."""
    tile_z = 21
    tile_x = 438217
    tile_y = 801835

    data, mask = cogeo.tile(ADDRESS, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.all()


def test_tile_invalid_bounds():
    """Should raise an error with invalid tile."""
    tile_z = 19
    tile_x = 554
    tile_y = 200458

    with pytest.raises(TileOutsideBounds):
        cogeo.tile(ADDRESS, tile_x, tile_y, tile_z)
