"""tests rio_tiler.sentinel2"""

import os
import pytest

from rio_tiler import cbers
from rio_tiler.errors import TileOutsideBounds

CBERS_SCENE = 'CBERS_4_MUX_20171121_057_094_L2'
CBERS_BUCKET = os.path.join(os.path.dirname(__file__), 'fixtures', 'cbers-pds')
CBERS_PATH = os.path.join(CBERS_BUCKET, 'CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2/')


def test_bounds_valid(monkeypatch):
    """
    Should work as expected (get bounds)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.bounds(CBERS_SCENE)
    assert meta.get('sceneid') == 'CBERS_4_MUX_20171121_057_094_L2'
    assert len(meta.get('bounds')) == 4


def test_metadata_valid_default(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.metadata(CBERS_SCENE)
    assert meta.get('sceneid') == 'CBERS_4_MUX_20171121_057_094_L2'
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')


def test_metadata_valid_custom(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.metadata(CBERS_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == 'CBERS_4_MUX_20171121_057_094_L2'
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')


def test_tile_valid_default(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495

    assert cbers.tile(CBERS_SCENE, tile_x, tile_y, tile_z).shape == (3, 256, 256)


def test_tile_valid_nrg(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    bands = (8, 7, 6)

    assert cbers.tile(CBERS_SCENE, tile_x, tile_y, tile_z, rgb=bands).shape == (3, 256, 256)


def test_tile_valid_onband(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    bands = 8

    assert cbers.tile(CBERS_SCENE, tile_x, tile_y, tile_z, rgb=bands).shape == (1, 256, 256)


def test_tile_invalid_bounds(monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 694
    tile_y = 495

    with pytest.raises(TileOutsideBounds):
        cbers.tile(CBERS_SCENE, tile_x, tile_y, tile_z)
