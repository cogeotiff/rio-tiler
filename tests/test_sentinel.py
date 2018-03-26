"""tests rio_tiler.sentinel2"""

import os
import pytest

from rio_tiler import sentinel2
from rio_tiler.errors import TileOutsideBounds

SENTINEL_SCENE = 'S2A_tile_20170729_19UDP_0'
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__),
                               'fixtures', 'sentinel-s2-l1c')
SENTINEL_PATH = os.path.join(SENTINEL_BUCKET, 'tiles/19/U/DP/2017/7/29/0/')


def test_bounds_valid(monkeypatch):
    """
    Should work as expected (get bounds)
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    meta = sentinel2.bounds(SENTINEL_SCENE)
    assert meta.get('sceneid') == 'S2A_tile_20170729_19UDP_0'
    assert len(meta.get('bounds')) == 4


def test_metadata_valid_default(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    meta = sentinel2.metadata(SENTINEL_SCENE)
    assert meta.get('sceneid') == 'S2A_tile_20170729_19UDP_0'
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')


def test_metadata_valid_custom(monkeypatch):
    """
    Should work as expected (get bounds and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    meta = sentinel2.metadata(SENTINEL_SCENE, pmin=5, pmax=95)
    assert meta.get('sceneid') == 'S2A_tile_20170729_19UDP_0'
    assert len(meta.get('bounds')) == 4
    assert meta.get('rgbMinMax')


def test_tile_valid_default(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_valid_nrg(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89
    bands = ('08', '04', '03')

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (3, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_valid_onband(monkeypatch):
    """
    Should work as expected
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 77
    tile_y = 89
    bands = '08'

    data, mask = sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z, bands=bands)
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)


def test_tile_invalid_bounds(monkeypatch):
    """
    Should raise an error with invalid tile
    """

    monkeypatch.setattr(sentinel2, 'SENTINEL_BUCKET', SENTINEL_BUCKET)

    tile_z = 8
    tile_x = 177
    tile_y = 89

    with pytest.raises(TileOutsideBounds):
        sentinel2.tile(SENTINEL_SCENE, tile_x, tile_y, tile_z)
