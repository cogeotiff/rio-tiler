"""tests rio_tiler.base"""

import os
import pytest

from rio_tiler import main
from rio_tiler.errors import TileOutsideBounds

PREFIX = os.path.join(os.path.dirname(__file__), 'fixtures')
ADDRESS = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'.format(PREFIX)
ADDRESS_ALPHA = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif'.format(PREFIX)
ADDRESS_NODATA = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif'.format(PREFIX)
# ADDRESS_MASK = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata_mask.tif'.format(PREFIX)
# ADDRESS_EXTMASK = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata_extmask.tif.msk'.format(PREFIX)


def test_bounds_valid():
    """
    Should work as expected (get bounds)
    """

    meta = main.bounds(ADDRESS)
    assert meta.get('url') == ADDRESS
    assert len(meta.get('bounds')) == 4


def test_tile_valid_default():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.all()


def test_tile_valid_bands():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = (1)

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z, indexes=bands)
    assert data.shape == (1, 256, 256)


def test_tile_valid_internal_alpha():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_ALPHA, tile_x, tile_y, tile_z, indexes=(1, 2, 3))
    assert data.shape == (3, 256, 256)
    assert not mask.all()


def test_tile_valid_alpha():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS, tile_x, tile_y, tile_z, indexes=(1, 2, 3), alpha=3)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


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
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    data, mask = main.tile(ADDRESS_NODATA, tile_x, tile_y, tile_z, nodata=0)
    assert data.shape == (3, 256, 256)
    assert not mask.all()


# # This test should pass but currently fail with rasterio==1.0a12
# def test_tile_valid_internal_mask():
#     """
#     Should work as expected
#     """
#
#     tile_z = 19
#     tile_x = 109554
#     tile_y = 200458
#
#     data, mask = main.tile(ADDRESS_MASK, tile_x, tile_y, tile_z, rgb=(1, 2, 3))
#     assert data.shape == (3, 256, 256)
#     assert not mask.all()
#
#
# # This test should pass but currently fail with rasterio==1.0a12
# def test_tile_valid_external_mask():
#     """
#     Should work as expected
#     """
#
#     tile_z = 19
#     tile_x = 109554
#     tile_y = 200458
#
#     data, mask = main.tile(ADDRESS_EXTMASK, tile_x, tile_y, tile_z, rgb=(1, 2, 3))
#     assert data.shape == (3, 256, 256)
#     assert not mask.all()


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
