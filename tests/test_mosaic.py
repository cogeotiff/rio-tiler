"""tests ard_tiler.mosaic."""

import os
from typing import Tuple

import numpy
import pytest

from rio_tiler import mosaic
from rio_tiler.io import COGReader
from rio_tiler.mosaic import MosaicReader
from rio_tiler.mosaic.methods import defaults

asset1 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_cog1.tif")
asset2 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_cog2.tif")
assets = [asset1, asset2]
assets_order = [asset2, asset1]

# Full covered tile
x = 150
y = 182
z = 9

# Partially covered tile
xp = 150
yp = 180
zp = 9


def _read_tile(src_path: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Read tile from an asset"""
    with COGReader(src_path) as cog:
        tile, mask = cog.tile(*args, **kwargs)
    return tile, mask


def _read_preview(
    src_path: str, *args, **kwargs
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Read preview from an asset"""
    with COGReader(src_path) as cog:
        data, mask = cog.preview(*args, **kwargs)
    return data, mask


def test_mosaic_tiler():
    """Test mosaic tiler."""
    # test with mosaic_tiler for compatibility
    t, m = mosaic.mosaic_tiler(assets, x, y, z, _read_tile)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8682

    # test with default and full covered tile and default options
    t, m = mosaic.mosaic_reader(assets, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8682

    # Test last pixel selection
    assetsr = list(reversed(assets))
    t, m = mosaic.mosaic_reader(assetsr, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8057

    t, m = mosaic.mosaic_reader(assets, _read_tile, x, y, z, indexes=1)
    assert t.shape == (1, 256, 256)
    assert m.shape == (256, 256)
    assert t.all()
    assert m.all()
    assert t[0][-1][-1] == 8682

    # Test darkest pixel selection
    t, m = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    assert m.all()
    assert t[0][-1][-1] == 8057

    to, mo = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    numpy.testing.assert_array_equal(t[0, m], to[0, mo])

    # Test brightest pixel selection
    t, m = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    assert m.all()
    assert t[0][-1][-1] == 8682

    to, mo = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    numpy.testing.assert_array_equal(to, t)
    numpy.testing.assert_array_equal(mo, m)

    # test with default and partially covered tile
    t, m = mosaic.mosaic_reader(
        assets, _read_tile, xp, yp, zp, pixel_selection=defaults.HighestMethod()
    )
    assert t.any()
    assert not m.all()

    # test when tiler raise errors (outside bounds)
    t, m = mosaic.mosaic_reader(assets, _read_tile, 150, 300, 9)
    assert not t
    assert not m

    # Test mean pixel selection
    t, m = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MeanMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8369

    # Test mean pixel selection
    t, m = mosaic.mosaic_reader(
        assets,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.MeanMethod(enforce_data_type=False),
    )
    assert m.all()
    assert t[0][-1][-1] == 8369.5

    # Test median pixel selection
    t, m = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MedianMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8369

    # Test median pixel selection
    t, m = mosaic.mosaic_reader(
        assets,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.MedianMethod(enforce_data_type=False),
    )
    assert m.all()
    assert t[0][-1][-1] == 8369.5

    # Test invalid Pixel Selection class
    with pytest.raises(Exception):

        class aClass(object):
            pass

        mosaic.mosaic_reader(assets, _read_tile, x, y, z, pixel_selection=aClass())

    # test with preview
    # NOTE: We need to fix the output width and height because each preview could have different size
    t, m = mosaic.mosaic_reader(assets, _read_preview, width=256, height=256)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)


def test_mosaic_tiler_Stdev():
    """Test Stdev mosaic methods."""
    tile1, _ = _read_tile(assets[0], x, y, z)
    tile2, _ = _read_tile(assets[1], x, y, z)

    t, m = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.StdevMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == numpy.std([tile1[0][-1][-1], tile2[0][-1][-1]])
    assert t[1][-1][-1] == numpy.std([tile1[1][-1][-1], tile2[1][-1][-1]])
    assert t[2][-1][-1] == numpy.std([tile1[2][-1][-1], tile2[2][-1][-1]])


def test_threads():
    """Test mosaic tiler."""
    assets = [asset1, asset2, asset1, asset2, asset1, asset2]

    tnothread, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, threads=0)
    tmulti_threads, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, threads=1)
    numpy.testing.assert_array_equal(tnothread, tmulti_threads)

    t, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, threads=0, chunk_size=2)
    assert t.shape == (3, 256, 256)
    t, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, threads=2, chunk_size=4)
    assert t.shape == (3, 256, 256)


def test_mosaic_Reader():
    """Test MosaicReader."""
    # test with mosaic_tiler for compatibility
    with MosaicReader(assets, COGReader) as mr:
        t, m = mr.tile(x, y, z)
        assert t.shape == (3, 256, 256)
        assert m.shape == (256, 256)
        assert m.all()
        assert t[0][-1][-1] == 8682

    assetsr = list(reversed(assets))
    with MosaicReader(assetsr, COGReader) as mr:
        t, m = mr.tile(x, y, z)
        assert t.shape == (3, 256, 256)
        assert m.shape == (256, 256)
        assert m.all()
        assert t[0][-1][-1] == 8057

    with MosaicReader(assets, COGReader) as mr:
        t, m = mr.tile(x, y, z, indexes=1)
        assert t.shape == (1, 256, 256)
        assert m.shape == (256, 256)
        assert t.all()
        assert m.all()
        assert t[0][-1][-1] == 8682

    with MosaicReader(assets, COGReader) as mr:
        # Test darkest pixel selection
        t, m = mr.tile(x, y, z, pixel_selection=defaults.LowestMethod())
        assert m.all()
        assert t[0][-1][-1] == 8057

    with MosaicReader(assets_order, COGReader) as mr:
        to, mo = mr.tile(x, y, z, pixel_selection=defaults.LowestMethod())
        numpy.testing.assert_array_equal(t[0, m], to[0, mo])

    with MosaicReader(assets, COGReader) as mr:
        # Test brightest pixel selection
        t, m = mr.tile(x, y, z, pixel_selection=defaults.HighestMethod())
        assert m.all()
        assert t[0][-1][-1] == 8682

    with MosaicReader(assets_order, COGReader) as mr:
        to, mo = mr.tile(x, y, z, pixel_selection=defaults.HighestMethod())
        numpy.testing.assert_array_equal(to, t)
        numpy.testing.assert_array_equal(mo, m)

    with MosaicReader(assets, COGReader) as mr:
        # test with default and partially covered tile
        t, m = mr.tile(xp, yp, zp, pixel_selection=defaults.HighestMethod())
        assert t.any()
        assert not m.all()

        # Test mean pixel selection
        t, m = mr.tile(x, y, z, pixel_selection=defaults.MeanMethod())
        assert t.shape == (3, 256, 256)
        assert m.shape == (256, 256)
        assert m.all()
        assert t[0][-1][-1] == 8369

        # Test mean pixel selection
        t, m = mr.tile(
            x, y, z, pixel_selection=defaults.MeanMethod(enforce_data_type=False),
        )
        assert m.all()
        assert t[0][-1][-1] == 8369.5

        # Test median pixel selection
        t, m = mr.tile(x, y, z, pixel_selection=defaults.MedianMethod())
        assert t.shape == (3, 256, 256)
        assert m.shape == (256, 256)
        assert m.all()
        assert t[0][-1][-1] == 8369

        # Test median pixel selection
        t, m = mr.tile(
            x, y, z, pixel_selection=defaults.MedianMethod(enforce_data_type=False),
        )
        assert m.all()
        assert t[0][-1][-1] == 8369.5

        # Test invalid Pixel Selection class
        with pytest.raises(Exception):

            class aClass(object):
                pass

            mr.tile(x, y, z, pixel_selection=aClass())

        # test with preview
        # NOTE: We need to fix the output width and height because each preview could have different size

        t, m = mr.preview(width=256, height=256)
        assert t.shape == (3, 256, 256)
        assert m.shape == (256, 256)
