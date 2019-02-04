"""tests rio_tiler.landsat8"""

import os
import pytest

from mock import patch

from rio_toa import toa_utils

from rio_tiler import landsat8
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, DeprecationWarning

LANDSAT_SCENE_C1 = "LC08_L1TP_016037_20170813_20170814_01_RT"
LANDSAT_BUCKET = os.path.join(os.path.dirname(__file__), "fixtures", "landsat-pds")

LANDSAT_PATH = os.path.join(
    LANDSAT_BUCKET, "c1", "L8", "016", "037", LANDSAT_SCENE_C1, LANDSAT_SCENE_C1
)

with open("{}_MTL.txt".format(LANDSAT_PATH), "r") as f:
    LANDSAT_METADATA = toa_utils._parse_mtl_txt(f.read())


@patch("rio_tiler.utils.landsat_get_mtl")
def test_bounds_valid(landsat_get_mtl):
    """
    Should work as expected (get and parse metadata)
    """

    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.bounds(LANDSAT_SCENE_C1)
    assert meta.get("sceneid") == "LC08_L1TP_016037_20170813_20170814_01_RT"
    assert len(meta.get("bounds")) == 4


@patch("rio_tiler.utils.landsat_get_mtl")
def test_metadata_valid_default(landsat_get_mtl, monkeypatch):
    """
    Should work as expected (get metadata and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.metadata(LANDSAT_SCENE_C1)
    assert meta.get("sceneid") == "LC08_L1TP_016037_20170813_20170814_01_RT"
    assert len(meta.get("bounds")) == 4
    assert len(meta.get("rgbMinMax")) == 11


@patch("rio_tiler.utils.landsat_get_mtl")
def test_metadata_valid_custom(landsat_get_mtl, monkeypatch):
    """
    Should work as expected (get metadata and get histogram cuts values
    for all bands)
    """

    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    meta = landsat8.metadata(LANDSAT_SCENE_C1)
    assert meta.get("sceneid") == "LC08_L1TP_016037_20170813_20170814_01_RT"
    assert len(meta.get("bounds")) == 4
    assert len(meta.get("rgbMinMax")) == 11


@patch("rio_tiler.utils.landsat_get_mtl")
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


@patch("rio_tiler.utils.landsat_get_mtl")
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


# TODO: Remove on 1.0.0
@patch("rio_tiler.utils.landsat_get_mtl")
def test_tile_warnsInteger(landsat_get_mtl, monkeypatch):
    """Should warns on integer band name."""
    monkeypatch.setattr(landsat8, "LANDSAT_BUCKET", LANDSAT_BUCKET)
    landsat_get_mtl.return_value = LANDSAT_METADATA

    tile_z = 8
    tile_x = 71
    tile_y = 102
    bands = (5, 4, 3)
    with pytest.warns(DeprecationWarning):
        data, mask = landsat8.tile(
            LANDSAT_SCENE_C1, tile_x, tile_y, tile_z, bands=bands
        )
        assert data.shape == (3, 256, 256)
        assert mask.shape == (256, 256)


@patch("rio_tiler.utils.landsat_get_mtl")
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


@patch("rio_tiler.utils.landsat_get_mtl")
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


@patch("rio_tiler.utils.landsat_get_mtl")
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


@patch("rio_tiler.utils.landsat_get_mtl")
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
