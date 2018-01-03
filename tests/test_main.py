"""tests rio_tiler.base"""

import os
import pytest

from rio_tiler import main
from rio_tiler.errors import TileOutsideBounds

PREFIX = os.path.join(os.path.dirname(__file__), 'fixtures')
ADDRESS = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'.format(PREFIX)
ADDRESS_NODATA = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif'.format(PREFIX)


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

    assert main.tile(ADDRESS, tile_x, tile_y, tile_z).shape == (3, 256, 256)


def test_tile_valid_nodata():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    assert main.tile(ADDRESS_NODATA, tile_x, tile_y, tile_z).shape == (3, 256, 256)


def test_tile_valid_bands():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = (3, 2, 1)

    assert main.tile(ADDRESS, tile_x, tile_y, tile_z, rgb=bands).shape == (3, 256, 256)


def test_tile_valid_oneband():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = 3

    assert main.tile(ADDRESS, tile_x, tile_y, tile_z, rgb=bands).shape == (256, 256)


def test_tile_invalid_bounds():
    """
    Should raise an error with invalid tile
    """

    tile_z = 19
    tile_x = 554
    tile_y = 200458

    with pytest.raises(TileOutsideBounds):
        main.tile(ADDRESS, tile_x, tile_y, tile_z)
