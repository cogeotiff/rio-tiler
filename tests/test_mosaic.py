"""tests ard_tiler.mosaic."""

import os
from unittest.mock import patch

import numpy
import pytest
import rasterio
from rasterio.crs import CRS
from rasterio.warp import transform_bounds

from rio_tiler import mosaic
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import EmptyMosaicError, InvalidMosaicMethod, TileOutsideBounds
from rio_tiler.io import Reader, STACReader
from rio_tiler.models import ImageData, PointData
from rio_tiler.mosaic.methods import defaults

asset1 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_value_1.tif")
asset2 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_value_2.tif")
asset3 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_value_3.tif")
assets = [asset1, asset2]
assets_order = [asset2, asset1]
assets_mixed = [asset1, asset3]

stac_asset = os.path.join(os.path.dirname(__file__), "fixtures", "stac.json")

# Full covered tile
# fully covering mosaic_value_1 an partially covering mosaic_value_2
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
    with Reader(src_path) as src:
        return src.tile(*args, **kwargs)


def _read_part(src_path: str, *args, **kwargs) -> ImageData:
    """Read part from an asset"""
    with Reader(src_path) as src:
        return src.part(*args, **kwargs)


def _read_preview(src_path: str, *args, **kwargs) -> ImageData:
    """Read preview from an asset"""
    with Reader(src_path) as src:
        return src.preview(*args, **kwargs)


def _read_point(src_path: str, *args, **kwargs) -> PointData:
    """Read point from an asset"""
    with Reader(src_path) as src:
        return src.point(*args, **kwargs)


def _read_feature(src_path: str, *args, **kwargs) -> ImageData:
    """Read feature from an asset"""
    with Reader(src_path) as src:
        return src.feature(*args, **kwargs)


def test_mosaic_tiler():
    """Test mosaic tiler."""
    # test with default and full covered tile and default options
    (t, m), assets_used = mosaic.mosaic_reader(assets, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # Should only have value of 1
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    img, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z)
    assert img.band_names == ["b1", "b2", "b3"]

    img, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, indexes=[1])
    assert img.band_names == ["b1"]

    img, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, expression="b1*3")
    assert img.band_names == ["b1*3"]
    # Should only have value of 1 but *3
    assert numpy.unique(img.data[0, m == 255]).tolist() == [3]

    # Test last pixel selection
    assetsr = list(reversed(assets))
    (t, m), _ = mosaic.mosaic_reader(assetsr, _read_tile, x, y, z)
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # Should have values of 2 and 1 because the tile do not fully overlap mosaic_value_2 cog
    assert numpy.unique(t[0, m == 255]).tolist() == [1, 2]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    (t, m), _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, indexes=1)
    assert t.shape == (1, 256, 256)
    assert m.shape == (256, 256)
    assert t.all()
    assert m.all()
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    # Test darkest pixel selection
    (t, m), assets_used = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    assert len(assets_used) == 2
    assert m.all()
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    (to, mo), _ = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.LowestMethod()
    )
    numpy.testing.assert_array_equal(t[0, m], to[0, mo])
    assert to.dtype == "uint16"
    assert mo.dtype == "uint8"

    # Test brightest pixel selection
    # Should return both 1 and 2
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    assert m.all()
    assert numpy.unique(t[0, m == 255]).tolist() == [1, 2]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    (to, mo), _ = mosaic.mosaic_reader(
        assets_order, _read_tile, x, y, z, pixel_selection=defaults.HighestMethod()
    )
    numpy.testing.assert_array_equal(to, t)
    numpy.testing.assert_array_equal(mo, m)
    assert to.dtype == "uint16"
    assert mo.dtype == "uint8"

    # test with default and partially covered tile
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, xp, yp, zp, pixel_selection=defaults.HighestMethod()
    )
    assert t.any()
    assert not m.all()
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    # test when tiler raise errors (outside bounds)
    with pytest.raises(EmptyMosaicError):
        mosaic.mosaic_reader(assets, _read_tile, 150, 300, 9)

    # Test mean pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MeanMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # This should return only 1 because we enforce data_type to be the same
    # as the initial data (uint16) so 1.5 will be casted to 1
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

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
    # We do not cast the data to Uint16 so we should get both 1 and 1.5
    assert numpy.unique(t[0, m == 255]).tolist() == [1, 1.5]
    assert t.dtype == "float64"
    assert m.dtype == "uint8"

    # Test median pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.MedianMethod()
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # This should return only 1 because we enforce data_type to be the same
    # as the initial data (uint16) so 1.5 will be casted to 1
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

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
    # We do not cast the data to Uint16 so we should get both 1 and 1.5
    assert numpy.unique(t[0, m == 255]).tolist() == [1, 1.5]
    assert t.dtype == "float64"
    assert m.dtype == "uint8"

    (t, m), _ = mosaic.mosaic_reader(
        assets_order,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.LastBandHighMethod(),
        indexes=(1, 2, 3, 1),
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # The last band will be either 1 or 2
    # so we should get both 1 and 2
    assert numpy.unique(t[0, m == 255]).tolist() == [1, 2]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    (t, m), _ = mosaic.mosaic_reader(
        assets_order,
        _read_tile,
        x,
        y,
        z,
        pixel_selection=defaults.LastBandLowMethod(),
        indexes=(1, 2, 3, 1),
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    # The last band will be either 1 or 2
    # but we only select where it's the lowest (1)
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    # Test pixel selection as _class_, not instance of class
    (t, m), assets_used = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.FirstMethod
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert numpy.unique(t[0, m == 255]).tolist() == [1]
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    # Test invalid Pixel Selection class
    with pytest.raises(InvalidMosaicMethod):

        class aClass(object):
            pass

        mosaic.mosaic_reader(assets, _read_tile, x, y, z, pixel_selection=aClass())

    # test with preview
    # NOTE: We need to have fix output width and height because each preview could have different size
    # Also because the 2 assets cover different bbox, getting the preview merged together doesn't make real sense
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_preview, width=256, height=256, max_size=None
    )
    assert t.shape == (3, 256, 256)
    assert m.shape == (256, 256)
    assert t.dtype == "uint16"
    assert m.dtype == "uint8"

    # Test count pixel selection
    (t, m), _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, pixel_selection=defaults.CountMethod()
    )
    assert t.shape == (1, 256, 256)
    assert m.shape == (256, 256)
    assert m.all()
    assert t.dtype == "uint8"
    assert m.dtype == "uint8"


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("http://somewhere-over-the-rainbow.io")
    asset = asset.replace(
        "http://somewhere-over-the-rainbow.io",
        os.path.join(os.path.dirname(__file__), "fixtures"),
    )
    return rasterio.open(asset)


@patch("rio_tiler.io.rasterio.rasterio")
def test_stac_mosaic_tiler(rio):
    """Test mosaic tiler with STACReader."""
    rio.open = mock_rasterio_open

    def _reader(src_path: str, *args, **kwargs) -> ImageData:
        """Read tile from an asset"""
        with STACReader(src_path) as stac:
            return stac.tile(*args, **kwargs)

    (data, mask), assets_used = mosaic.mosaic_reader(
        [stac_asset],
        _reader,
        71,
        102,
        8,
        assets="green",
        threads=0,
    )
    assert assets_used == [stac_asset]
    assert data.shape == (1, 256, 256)
    assert mask.shape == (256, 256)

    img, _ = mosaic.mosaic_reader(
        [stac_asset],
        _reader,
        71,
        102,
        8,
        assets="green",
        threads=0,
    )
    assert img.band_names == ["green_b1"]

    img, _ = mosaic.mosaic_reader(
        [stac_asset],
        _reader,
        71,
        102,
        8,
        expression="green_b1*2",
        threads=0,
    )
    assert img.band_names == ["green_b1*2"]


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

    # TileOutSide bounds should be ignored but no tile is created
    with pytest.raises(EmptyMosaicError):
        mosaic.mosaic_reader(assets, _read_tile, xo, yo, zo, threads=2)

    # TileOutSide bounds should be ignored but no tile is created
    with pytest.raises(EmptyMosaicError):
        mosaic.mosaic_reader(assets, _read_tile, xo, yo, zo, threads=0)

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
    # assert img.data[0][-1][-1] == 8682
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
        max_size=None,
        pixel_selection=defaults.LowestMethod(),
    )
    assert img.data.shape == (3, 256, 256)
    assert img.mask.shape == (256, 256)
    assert assets_used == img.assets == assets
    assert img.crs
    assert img.bounds

    bbox = [-75.98703377413767, 44.93504283293786, -71.337604723999, 47.09685599202324]
    with Reader(assets[0]) as src:
        crs1 = src.dataset.crs

    with Reader(assets[0]) as src:
        crs2 = src.dataset.crs

    img, assets_used = mosaic.mosaic_reader(
        assets, _read_part, bbox=bbox, dst_crs=crs1, bounds_crs=WGS84_CRS, max_size=1024
    )
    assert img.data.shape == (3, 689, 1024)
    assert img.mask.shape == (689, 1024)
    assert img.mask.any()
    assert assets_used == img.assets == assets
    assert img.crs == crs1 == crs2
    assert not img.bounds == bbox
    bbox_in_crs = transform_bounds(WGS84_CRS, crs1, *bbox, densify_pts=21)
    for xc, yc in zip(img.bounds, bbox_in_crs):
        assert round(xc, 5) == round(yc, 5)


def test_mosaic_point():
    """Test mosaic point."""
    cog1 = (-75.38645768740565, 45.769670480435394)
    both = (-73.69990294755982, 45.49950291143219)
    cog2 = (-72.02385676824944, 46.06897125935538)

    pt, _ = mosaic.mosaic_point_reader(assets, _read_point, *cog1)
    assert pt.data.tolist() == [1, 1, 1]
    assert pt.mask.tolist() == [255]
    assert pt.assets == [asset1]
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == cog1

    pt, _ = mosaic.mosaic_point_reader(assets, _read_point, *cog2)
    assert pt.data.tolist() == [2, 2, 2]
    assert pt.mask.tolist() == [255]
    assert pt.assets == [asset2]
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == cog2

    pt, _ = mosaic.mosaic_point_reader(assets, _read_point, *both)
    assert pt.data.tolist() == [1, 1, 1]
    assert pt.mask.tolist() == [255]
    assert pt.assets == [asset1]
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == both

    pt, _ = mosaic.mosaic_point_reader(
        assets, _read_point, *both, pixel_selection=defaults.LowestMethod
    )
    assert pt.data.tolist() == [1, 1, 1]
    assert pt.mask.tolist() == [255]
    assert pt.assets == [asset1, asset2]
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == both

    pt, _ = mosaic.mosaic_point_reader(
        assets, _read_point, *both, pixel_selection=defaults.HighestMethod
    )
    assert pt.data.tolist() == [2, 2, 2]
    assert pt.mask.tolist() == [255]
    assert pt.assets == [asset1, asset2]
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == both

    with pytest.raises(EmptyMosaicError):
        mosaic.mosaic_point_reader(assets, _read_point, -78, 43)


@pytest.mark.parametrize(
    "m",
    [
        defaults.FirstMethod,
        defaults.HighestMethod,
        defaults.LowestMethod,
        defaults.MeanMethod,
        defaults.MedianMethod,
        defaults.StdevMethod,
    ],
)
def test_mosaic_all_methods(m):
    """Test mosaic methods."""
    pt, _ = mosaic.mosaic_point_reader(
        assets, _read_point, -73.69990294755982, 45.49950291143219, pixel_selection=m
    )
    assert len(pt.data) == 3
    assert len(pt.mask) == 1
    assert len(pt.assets) > 0
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == (-73.69990294755982, 45.49950291143219)

    img, _ = mosaic.mosaic_reader(assets, _read_tile, x, y, z, pixel_selection=m)
    assert img.data.shape == (3, 256, 256)
    assert img.mask.shape == (256, 256)
    assert img.mask.all()
    assert img.crs == WEB_MERCATOR_TMS.crs
    assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(x, y, z)


@pytest.mark.parametrize(
    "m",
    [
        defaults.LastBandHighMethod,
        defaults.LastBandLowMethod,
    ],
)
def test_mosaic_methods_last(m):
    """test LAST mosaic method."""
    pt, _ = mosaic.mosaic_point_reader(
        assets,
        _read_point,
        -73.69990294755982,
        45.49950291143219,
        pixel_selection=m,
        indexes=(1, 2, 3, 3),
    )
    assert len(pt.data) == 3
    assert len(pt.mask) == 1
    assert len(pt.assets) > 0
    assert pt.crs == WGS84_CRS
    assert pt.coordinates == (-73.69990294755982, 45.49950291143219)

    img, _ = mosaic.mosaic_reader(
        assets, _read_tile, x, y, z, indexes=(1, 2, 3, 3), pixel_selection=m
    )
    assert img.data.shape == (3, 256, 256)
    assert img.mask.shape == (256, 256)
    assert img.mask.all()
    assert img.crs == WEB_MERCATOR_TMS.crs
    assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(x, y, z)


def test_mosaic_feature():
    """Test mosaic feature."""
    cog1 = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [479966, 5076955],
                    [485507, 5083109],
                    [490381, 5078849],
                    [488014, 5073641],
                    [479966, 5076955],
                ]
            ],
        },
    }
    cog2 = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [700570, 5042202],
                    [706585, 5046212],
                    [713045, 5040643],
                    [709035, 5036410],
                    [700570, 5042202],
                ]
            ],
        },
    }
    both = {
        "type": "Polygon",
        "coordinates": [
            [
                [575815, 5049776],
                [584726, 5055123],
                [589405, 5046212],
                [581830, 5046212],
                [575815, 5049776],
            ]
        ],
    }
    edge = {
        "type": "Polygon",
        "coordinates": [
            [
                [614608, 5021770],
                [633407, 5021770],
                [633407, 5030735],
                [614608, 5030735],
                [614608, 5021770],
            ]
        ],
    }
    away = {
        "type": "Polygon",
        "coordinates": [
            [
                [900570, 5042202],
                [906585, 5046212],
                [913045, 5040643],
                [909035, 5036410],
                [900570, 5042202],
            ]
        ],
    }
    crs = CRS.from_epsg(32618)

    dat, _ = mosaic.mosaic_reader(assets, _read_feature, shape=cog1, shape_crs=crs)
    assert dat.data.shape == (3, 32, 35)
    assert list(numpy.unique(dat.array.mask)) == [False, True]
    assert dat.assets == [asset1]
    assert dat.crs == crs

    dat, _ = mosaic.mosaic_reader(
        assets_order, _read_feature, shape=cog2, shape_crs=crs
    )
    assert dat.data.shape == (3, 33, 42)
    assert list(numpy.unique(dat.array.mask)) == [False, True]
    assert dat.assets == [asset2]
    assert dat.crs == crs

    dat, _ = mosaic.mosaic_reader(assets, _read_feature, shape=both, shape_crs=crs)
    assert dat.data.shape == (3, 30, 45)
    assert list(numpy.unique(dat.array.mask)) == [False, True]
    assert dat.assets == [asset1]  # Covers both but finishes early
    assert dat.crs == crs

    dat, _ = mosaic.mosaic_reader(assets, _read_feature, shape=edge, shape_crs=crs)
    assert dat.data.shape == (3, 30, 63)
    assert list(numpy.unique(dat.array.mask)) == [
        False
    ]  # Squared polygon, fills all pixels
    assert dat.assets == [
        asset1,
        asset2,
    ]  # At edge of asset 1, will need asset 2 to complete
    assert dat.crs == crs

    dat, _ = mosaic.mosaic_reader(assets, _read_feature, shape=away, shape_crs=crs)
    assert dat.data.shape == (3, 33, 42)
    assert list(numpy.unique(dat.array.mask)) == [True]
    assert dat.assets == [asset1, asset2]
    assert dat.crs == crs

    dat, _ = mosaic.mosaic_reader(
        assets,
        _read_feature,
        shape=cog1,
        shape_crs=crs,
        pixel_selection=defaults.HighestMethod,
    )
    assert dat.data.shape == (3, 32, 35)
    assert list(numpy.unique(dat.array.mask)) == [False, True]
    assert dat.assets == [asset1, asset2]
    assert dat.crs == crs


def test_mosaic_feature_size_diff():
    """Test mosaic feature with ."""
    feature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": [
                [
                    [-74.08023862322486, 45.69787317293694],
                    [-74.08023862322486, 45.2992447541925],
                    [-73.43873302640402, 45.2992447541925],
                    [-73.43873302640402, 45.69787317293694],
                    [-74.08023862322486, 45.69787317293694],
                ]
            ],
            "type": "Polygon",
        },
    }

    with pytest.warns(UserWarning):
        dat, _ = mosaic.mosaic_reader(assets_mixed, _read_feature, shape=feature)
        assert dat.data.shape == (3, 120, 193)
