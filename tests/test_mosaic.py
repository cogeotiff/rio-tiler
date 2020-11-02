"""tests ard_tiler.mosaic."""

import os
from typing import Tuple

import numpy
import pytest
from rasterio.warp import transform_bounds

from rio_tiler import mosaic
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidMosaicMethod, TileOutsideBounds
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData
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

# Outside tile
xo = 200
yo = 180
zo = 9


def _read_tile(src_path: str, *args, **kwargs) -> ImageData:
    """Read tile from an asset"""
    with COGReader(src_path) as cog:
        return cog.tile(*args, **kwargs)


def _read_part(src_path: str, *args, **kwargs) -> ImageData:
    """Read part from an asset"""
    with COGReader(src_path) as cog:
        return cog.part(*args, **kwargs)


def _read_preview(
    src_path: str, *args, **kwargs
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Read preview from an asset"""
    with COGReader(src_path) as cog:
        data, mask = cog.preview(*args, **kwargs)
    return data, mask


def test_mosaic_tiler():
    """Test mosaic tiler."""
    # test with default and full covered tile and default options
    (t, m), assets_used = mosaic.mosaic_reader(assets, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8682

    # Test last pixel selection
    assetsr = list(reversed(assets))
    (t, m), _ = mosaic.mosaic_reader(assetsr, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8057

    (t, m), _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, indexes=1)
    assert t.shape == (1, 256, 256)
    assert m.shape == (256, 256)
    assert t.all()
    assert m.all()
    assert t[0][-1][-1] == 8682

    # Test darkest pixel selection
    (t, m), assets_used = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    assert len(assets_used) == 2
    assert m.all()
    assert t[0][-1][-1] == 8057

    (to, mo), _ = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    numpy.testing.assert_array_equal(t[0, m], to[0, mo])

    # Test brightest pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    assert m.all()
    assert t[0][-1][-1] == 8682

    (to, mo), _ = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    numpy.testing.assert_array_equal(to, t)
    numpy.testing.assert_array_equal(mo, m)

    # test with default and partially covered tile
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, xp, yp, zp, pixel_selection=defaults.HighestMethod()
    )
    assert t.any()
    assert not m.all()

    # test when tiler raise errors (outside bounds)
    (t, m), _ = mosaic.mosaic_reader(assets, _read_tile, 150, 300, 9)
    assert not t
    assert not m

    # Test mean pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MeanMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8369

    # Test mean pixel selection
    (t, m), _ = mosaic.mosaic_reader(
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
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MedianMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8369

    # Test median pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.MedianMethod(enforce_data_type=False),
    )
    assert m.all()
    assert t[0][-1][-1] == 8369.5

    (t, m), _ = mosaic.mosaic_reader(
        assets_order,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.LastBandHigh(),
        indexes=(1, 2, 3, 1),
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8682

    (t, m), _ = mosaic.mosaic_reader(
        assets_order,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.LastBandLow(),
        indexes=(1, 2, 3, 1),
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8057

    # Test pixel selection as _class_, not instance of class
    (t, m), assets_used = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.FirstMethod
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t[0][-1][-1] == 8682

    # Test invalid Pixel Selection class
    with pytest.raises(InvalidMosaicMethod):

        class aClass(object):
            pass

        mosaic.mosaic_reader(assets, _read_tile, x, y, z, pixel_selection=aClass())

    # test with preview
    # NOTE: We need to fix the output width and height because each preview could have different size
    # Also because the 2 assets cover different bbox, getting the preview merged together doesn't make real sense
    (t, m), _ = mosaic.mosaic_reader(assets, _read_preview, width=256, height=256)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)


def test_mosaic_tiler_Stdev():
    """Test Stdev mosaic methods."""
    tile1, _ = _read_tile(assets[0], x, y, z)
    tile2, _ = _read_tile(assets[1], x, y, z)

    (t, m), _ = mosaic.mosaic_reader(
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
    assets = [asset2, asset1, asset1, asset2, asset1, asset2]

    # TileOutSide bounds should be ignore and thus Tile is None
    (tnothread, _), _ = mosaic.mosaic_reader(assets, _read_tile, xo, yo, zo, threads=2)
    assert not tnothread

    # TileOutSide bounds should be ignore and thus Tile is None
    (tnothread, _), _ = mosaic.mosaic_reader(assets, _read_tile, xo, yo, zo, threads=0)
    assert not tnothread

    # Only cover asset1
    xpp = 147
    ypp = 180
    zpp = 9

    with pytest.raises(TileOutsideBounds):
        mosaic.mosaic_reader(
            assets,
            _read_tile,
            xpp,
            ypp,
            zpp,
            pixel_selection=defaults.MedianMethod,
            allowed_exceptions=None,
        )

    # Partial tile, some assets should Error with TileOutside bounds
    (tnothread, _), a = mosaic.mosaic_reader(
        assets,
        _read_tile,
        xpp,
        ypp,
        zpp,
        threads=0,
        pixel_selection=defaults.MedianMethod,
    )
    assert len(a) == 3
    assert tnothread.shape

    # Partial tile, some assets should Error with TileOutside bounds
    (tnothread, _), a = mosaic.mosaic_reader(
        assets,
        _read_tile,
        xpp,
        ypp,
        zpp,
        threads=1,
        pixel_selection=defaults.MedianMethod,
    )
    assert len(a) == 3
    assert tnothread.shape

    (tnothread, _), _ = mosaic.mosaic_reader(
        assets,
        _read_tile,
        xpp,
        ypp,
        zpp,
        threads=0,
        pixel_selection=defaults.MedianMethod,
    )
    (tmulti_threads, _), _ = mosaic.mosaic_reader(
        assets,
        _read_tile,
        xpp,
        ypp,
        zpp,
        threads=3,
        pixel_selection=defaults.MedianMethod,
    )
    numpy.testing.assert_array_equal(tnothread, tmulti_threads)

    (t, _), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, threads=0, chunk_size=2
    )
    assert t.shape == (3, 256, 256)
    (t, _), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, threads=2, chunk_size=4
    )
    assert t.shape == (3, 256, 256)


def test_mosaic_tiler_with_imageDataClass():
    """Test mosaic tiler."""
    img, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z)
    assert img.data.shape == (3, 256, 256)
    assert img.mask.shape == (256, 256)
    assert img.mask.all()
    assert img.data[0][-1][-1] == 8682
    assert len(img.assets) == 1

    assert img.crs == WEB_MERCATOR_TMS.crs
    assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(x, y, z)

    img, assets_used = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    assert assets_used == img.assets == assets
    assert img.crs == WEB_MERCATOR_TMS.crs
    assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(x, y, z)

    img, assets_used = mosaic.mosaic_reader(
        assets,
        _read_preview,
        width=256,
        height=256,
        pixel_selection=defaults.LowestMethod(),
    )
    assert img.data.shape == (3, 256, 256)
    assert img.mask.shape == (256, 256)
    assert assets_used == img.assets == assets
    assert not img.crs
    assert not img.bounds

    bbox = [-75.98703377413767, 44.93504283293786, -71.337604723999, 47.09685599202324]
    with COGReader(assets[0]) as cog:
        crs1 = cog.dataset.crs

    with COGReader(assets[0]) as cog:
        crs2 = cog.dataset.crs

    img, assets_used = mosaic.mosaic_reader(
        assets, _read_part, bbox=bbox, dst_crs=crs1, bounds_crs=WGS84_CRS, max_size=1024
    )
    assert img.data.shape == (3, 690, 1024)
    assert img.mask.shape == (690, 1024)
    assert img.mask.any()
    assert assets_used == img.assets == assets
    assert img.crs == crs1 == crs2
    assert not img.bounds == bbox
    bbox_in_crs = transform_bounds(WGS84_CRS, crs1, *bbox, densify_pts=21)
    assert img.bounds == bbox_in_crs
