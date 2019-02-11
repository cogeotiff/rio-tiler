"""tests rio_tiler.base"""

import os
import pytest

from rio_tiler import main
from rio_tiler.errors import TileOutsideBounds

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
ADDRESS = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif".format(
    PREFIX
)
ADDRESS_ALPHA = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif".format(
    PREFIX
)
ADDRESS_NODATA = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif".format(
    PREFIX
)
ADDRESS_MASK = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata_mask.tif".format(
    PREFIX
)
ADDRESS_EXTMASK = "{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata_extmask.tif".format(
    PREFIX
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


def test_bounds_valid():
    """
    Should work as expected (get bounds)
    """

    meta = main.bounds(ADDRESS)
    assert meta.get("url") == ADDRESS
    assert len(meta.get("bounds")) == 4


def test_metadata_valid():
    """Get bounds and get stats for all bands."""
    meta = main.metadata(ADDRESS)
    assert meta["address"] == ADDRESS
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 3
    assert meta["statistics"][1]["pc"] == [12, 198]


def test_metadata_valid_custom():
    """Get bounds and get stats for all bands with custom percentiles."""
    meta = main.metadata(ADDRESS, pmin=5, pmax=90, dst_crs="epsg:3857")
    assert meta["address"] == ADDRESS
    assert meta["bounds"]["crs"] == "epsg:3857"
    assert len(meta["bounds"]["value"]) == 4
    assert len(meta["statistics"].items()) == 3
    assert meta["statistics"][1]["pc"] == [30, 191]


def test_tile_valid_default():
    """
    Should work as expected
    """

    tile_z = 21
    tile_x = 438217
    tile_y = 801835

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.all()


def test_tile_valid_default_boundless():
    """Should work as expected.

    Mask should not be all valid because it's boundless read.
    """
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_bands():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = 1

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z, indexes=bands)
    assert data.shape == (1, 256, 256)


def test_tile_valid_internal_alpha():
    """
    Should work as expected
    """

    # Non-boundless tile
    tile_z = 22
    tile_x = 876432
    tile_y = 1603670

    data, mask = main.tile(ADDRESS_ALPHA, tile_x, tile_y, tile_z, indexes=(1, 2, 3))
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_internal_nodata():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_NODATA, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_external_nodata():
    """Should work as expected"""
    tile_z = 22
    tile_x = 876431
    tile_y = 1603669

    data, mask = main.tile(ADDRESS_NODATA, tile_x, tile_y, tile_z, nodata=0)
    assert data.shape == (3, 256, 256)
    assert not mask.all()
    assert (mask[:, 0:3] == 0).all()


def test_tile_valid_internal_mask():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_MASK, tile_x, tile_y, tile_z, indexes=(1, 2, 3))
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_external_mask():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_EXTMASK, tile_x, tile_y, tile_z, indexes=(1, 2, 3))
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_wrong_nodata():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_NODATA, tile_x, tile_y, tile_z, nodata=10000)
    assert data.shape == (3, 256, 256)
    assert mask.all()


def test_tile_valid_oneband():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = 3

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z, indexes=bands)
    assert data.shape == (1, 256, 256)


def test_tile_invalid_bounds():
    """
    Should raise an error with invalid tile
    """

    tile_z = 19
    tile_x = 554
    tile_y = 200458

    with pytest.raises(TileOutsideBounds):
        main.tile(ADDRESS, tile_x, tile_y, tile_z)
