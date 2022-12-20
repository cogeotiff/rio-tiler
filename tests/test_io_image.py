import os
import warnings

import numpy
import pytest
from rasterio.errors import NotGeoreferencedWarning

from rio_tiler.errors import PointOutsideBounds, TileOutsideBounds
from rio_tiler.io.rasterio import ImageReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
NO_GEO = os.path.join(PREFIX, "no_geo.jpg")
NO_GEO_PORTRAIT = os.path.join(PREFIX, "no_geo2.jpg")
GEO = os.path.join(PREFIX, "cog_nonearth.tif")


def test_non_geo_image():
    """Test ImageReader usage with Non-Geo Images."""
    with pytest.warns() as w:
        with ImageReader(NO_GEO) as src:
            assert src.minzoom == 0
            assert src.maxzoom == 3
        assert len(w) == 1
        assert issubclass(w[0].category, NotGeoreferencedWarning)

    with warnings.catch_warnings():
        with ImageReader(NO_GEO) as src:
            assert list(src.tms.xy_bounds(0, 0, 3)) == [0, 256, 256, 0]
            assert list(src.tms.xy_bounds(0, 0, 2)) == [0, 512, 512, 0]
            assert list(src.tms.xy_bounds(0, 0, 1)) == [0, 1024, 1024, 0]
            assert list(src.tms.xy_bounds(0, 0, 0)) == [0, 2048, 2048, 0]

            img = src.tile(0, 0, 3)
            assert img.mask.all()

            # Make sure no resampling was done at full resolution
            data = src.dataset.read(window=((0, 256), (0, 256)))
            numpy.testing.assert_array_equal(data, img.data)

            # Tile at zoom 0 should have masked part
            img = src.tile(0, 0, 0)
            assert not img.mask.all()

            with pytest.raises(TileOutsideBounds):
                max_x_tile = src.dataset.width // 256 + 1
                max_y_tile = src.dataset.height // 256 + 1
                src.tile(max_x_tile, max_y_tile, 3)

            img = src.part((0, 256, 256, 0))
            data = src.dataset.read(window=((0, 256), (0, 256)))
            numpy.testing.assert_array_equal(data, img.data)

            img = src.preview()
            assert img.width == 1024
            assert img.height == 1024

            pt = src.point(0, 0)
            assert list(pt.data) == [31, 34, 17]
            assert len(pt.mask) == 1
            assert pt.mask[0] == 255
            data = list(src.dataset.sample([(0, 0)]))[0]
            numpy.testing.assert_array_equal(pt.data, data)

            pt = src.point(50, 100)
            assert list(pt.data) == [48, 55, 14]
            assert len(pt.mask) == 1
            assert pt.mask[0] == 255
            data = list(src.dataset.sample([(50, 100)]))[0]
            numpy.testing.assert_array_equal(pt.data, data)

            pt = src.point(1999, 1999)
            data = list(src.dataset.sample([(1999, 1999)]))[0]
            numpy.testing.assert_array_equal(pt.data, data)

            with pytest.raises(PointOutsideBounds):
                src.point(2000, 2000)

            poly = {
                "coordinates": [
                    [
                        [-100.0, -100.0],
                        [1000.0, 100.0],
                        [500.0, 1000.0],
                        [-50.0, 500.0],
                        [-100.0, -100.0],
                    ]
                ],
                "type": "Polygon",
            }
            im = src.feature(poly)
            assert im.data.shape == (3, 1100, 1100)

    with warnings.catch_warnings():
        with ImageReader(NO_GEO_PORTRAIT) as src:
            img = src.tile(5, 2, 3)
            assert not img.mask.all()


def test_with_geo_image():
    """Test ImageReader usage with Geo Images."""
    with ImageReader(GEO) as src:
        assert src.minzoom == 0
        assert src.maxzoom == 2

        assert list(src.tms.xy_bounds(0, 0, 2)) == [0, 256, 256, 0]
        assert list(src.tms.xy_bounds(0, 0, 1)) == [0, 512, 512, 0]
        assert list(src.tms.xy_bounds(0, 0, 0)) == [0, 1024, 1024, 0]

        img = src.tile(10, 12, 4)
        assert img.mask.all()
        # img should keep the geo information from the dataset
        assert img.crs == src.dataset.crs
        assert img.bounds != list(src.tms.xy_bounds(10, 12, 4))

        img = src.tile(0, 0, 3)
        assert not img.mask.any()

        # Make sure no resampling was done at full resolution
        data = src.dataset.read(window=((0, 256), (0, 256)))
        numpy.testing.assert_array_equal(data, img.data)

        # Tile at zoom 0 should have masked part
        img = src.tile(0, 0, 0)
        assert not img.mask.all()

        with pytest.raises(TileOutsideBounds):
            max_x_tile = src.dataset.width // 256 + 1
            max_y_tile = src.dataset.height // 256 + 1
            src.tile(max_x_tile, max_y_tile, 2)

        img = src.part((0, 256, 256, 0))
        data = src.dataset.read(window=((0, 256), (0, 256)))
        numpy.testing.assert_array_equal(data, img.data)

        img = src.preview()
        assert img.width == 921
        assert img.height == 884
        # img should keep the geo information from the dataset
        assert img.crs == src.dataset.crs
        assert img.bounds != list(src.tms.xy_bounds(10, 12, 4))

        pt = src.point(0, 0)
        # pixel 0,0 is masked
        assert len(pt.mask) == 1
        assert pt.mask[0] == 0

        data = list(src.dataset.sample([(0, 0)]))[0]
        numpy.testing.assert_array_equal(pt.data, data)

        pt = src.point(400, 800)
        # pixel 400,800 has valid values
        assert len(pt.mask) == 1
        assert pt.mask[0] == 255

        pt = src.point(920, 883)
        data = list(src.dataset.sample([(920, 883)]))[0]
        numpy.testing.assert_array_equal(pt.data, data)
        assert pt.crs == src.dataset.crs
        assert pt.coordinates != [920, 883]

        with pytest.raises(PointOutsideBounds):
            src.point(2000, 2000)

        poly = {
            "coordinates": [
                [
                    [-100.0, -100.0],
                    [1000.0, 100.0],
                    [500.0, 1000.0],
                    [-50.0, 500.0],
                    [-100.0, -100.0],
                ]
            ],
            "type": "Polygon",
        }
        im = src.feature(poly)
        assert im.data.shape == (1, 1100, 1100)
