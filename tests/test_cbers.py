"""tests rio_tiler.sentinel2"""

import os
import pytest

from rio_tiler import cbers
from rio_tiler.errors import TileOutsideBounds

CBERS_BUCKET = os.path.join(os.path.dirname(__file__), 'fixtures', 'cbers-pds')
CBERS_MUX_SCENE = 'CBERS_4_MUX_20171121_057_094_L2'
CBERS_AWFI_SCENE = 'CBERS_4_AWFI_20170420_146_129_L2'
CBERS_PAN10M_SCENE = 'CBERS_4_PAN10M_20170427_161_109_L4'
CBERS_PAN5M_SCENE = 'CBERS_4_PAN5M_20170425_153_114_L4'
# Currently not being used, not defining for new instruments
CBERS_MUX_PATH = os.path.join(CBERS_BUCKET, 'CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2/')

def test_bounds_valid(monkeypatch):
    """
    Should work as expected (get bounds)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.bounds(CBERS_MUX_SCENE)
    assert meta.get('sceneid') == CBERS_MUX_SCENE
    assert len(meta.get('bounds')) == 4

    meta = cbers.bounds(CBERS_AWFI_SCENE)
    assert meta.get('sceneid') == CBERS_AWFI_SCENE
    assert len(meta.get('bounds')) == 4

    meta = cbers.bounds(CBERS_PAN10M_SCENE)
    assert meta.get('sceneid') == CBERS_PAN10M_SCENE
    assert len(meta.get('bounds')) == 4

    meta = cbers.bounds(CBERS_PAN5M_SCENE)
    assert meta.get('sceneid') == CBERS_PAN5M_SCENE
    assert len(meta.get('bounds')) == 4

def test_metadata_valid_default(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.metadata(CBERS_MUX_SCENE)
    assert meta.get('sceneid') == CBERS_MUX_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_AWFI_SCENE)
    assert meta.get('sceneid') == CBERS_AWFI_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_PAN10M_SCENE)
    assert meta.get('sceneid') == CBERS_PAN10M_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_PAN5M_SCENE)
    assert meta.get('sceneid') == CBERS_PAN5M_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

def test_metadata_valid_custom(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    meta = cbers.metadata(CBERS_MUX_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == CBERS_MUX_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_AWFI_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == CBERS_AWFI_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_PAN10M_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == CBERS_PAN10M_SCENE
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')

    meta = cbers.metadata(CBERS_PAN5M_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == CBERS_PAN5M_SCENE
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


def test_tile_valid_nrg(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    bands = (8, 7, 6)
    data, mask = cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)
        
    tile_z = 10
    tile_x = 401
    tile_y = 585
    bands = (16, 15, 14)
    data, mask = cbers.tile(CBERS_AWFI_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

    tile_z = 10
    tile_x = 370
    tile_y = 535
    bands = (4, 3, 2)
    data, mask = cbers.tile(CBERS_PAN10M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)
    
    tile_z = 10
    tile_x = 390
    tile_y = 547
    bands = (1, 1, 1)
    data, mask = cbers.tile(CBERS_PAN5M_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)

def test_tile_valid_onband(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 664
    tile_y = 495
    bands = 8

    data, mask = cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_invalid_bounds(monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(cbers, 'CBERS_BUCKET', CBERS_BUCKET)

    tile_z = 10
    tile_x = 694
    tile_y = 495

    with pytest.raises(TileOutsideBounds):
        cbers.tile(CBERS_MUX_SCENE, tile_x, tile_y, tile_z)
