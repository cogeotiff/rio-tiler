"""tests rio_tiler.aws"""

import os
import pytest

from rio_tiler import aws
from rio_tiler.errors import TileOutsideBounds

KEY = 'hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'
KEY_NODATA = 'hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif'
BUCKET = 'my-bucket'
PREFIX = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_bounds_valid():
    """
    Should work as expected (get bounds)
    """

    meta = aws.bounds(BUCKET, KEY, PREFIX)
    assert meta.get('key') == 'hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'
    assert meta.get('bucket') == 'my-bucket'
    assert len(meta.get('bounds')) == 4


def test_tile_valid_default():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    assert aws.tile(BUCKET, KEY, tile_x, tile_y, tile_z,
                    prefix=PREFIX).shape == (3, 256, 256)


def test_tile_valid_nodata():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    assert aws.tile(BUCKET, KEY_NODATA, tile_x, tile_y, tile_z,
                    prefix=PREFIX).shape == (3, 256, 256)


def test_tile_valid_bands():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = (3, 2, 1)

    assert aws.tile(BUCKET, KEY, tile_x, tile_y, tile_z, rgb=bands,
                    prefix=PREFIX).shape == (3, 256, 256)


def test_tile_valid_oneband():
    """
    Should work as expected
    """

    tile_z = 19
    tile_x = 109554
    tile_y = 200458
    bands = 3

    assert aws.tile(BUCKET, KEY, tile_x, tile_y, tile_z, rgb=bands,
                    prefix=PREFIX).shape == (256, 256)


def test_tile_invalid_bounds():
    """
    Should raise an error with invalid tile
    """

    tile_z = 19
    tile_x = 554
    tile_y = 200458

    with pytest.raises(TileOutsideBounds):
        aws.tile(BUCKET, KEY, tile_x, tile_y, tile_z, prefix=PREFIX)
