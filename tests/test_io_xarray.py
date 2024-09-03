"""tests rio_tiler.io.xarray.XarrayReader"""

from datetime import datetime

import morecantile
import numpy
import pytest
import rioxarray
import xarray

from rio_tiler.errors import InvalidGeographicBounds, MissingCRS
from rio_tiler.io import XarrayReader


def test_xarray_reader():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 33 * 35).reshape(1, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": list(range(-170, 180, 10)),
            "y": list(range(-80, 85, 5)),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    data.rio.write_crs("epsg:4326", inplace=True)
    with XarrayReader(data) as dst:
        info = dst.info()
        assert info.minzoom == 0
        assert info.maxzoom == 0
        assert info.band_metadata == [("b1", {})]
        assert info.band_descriptions == [("b1", "2022-01-01T00:00:00.000000000")]
        assert info.height == 33
        assert info.width == 35
        assert info.count == 1
        assert info.attrs

    with XarrayReader(data) as dst:
        img = dst.tile(0, 0, 0)
        assert img.count == 1
        assert img.width == 256
        assert img.height == 256
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]
        assert img.dataset_statistics == ((arr.min(), arr.max()),)

        # Tests for auto_expand
        # Test that a high-zoom tile will error with auto_expand=False
        tms = morecantile.tms.get("WebMercatorQuad")
        zoom = 10
        x, y = tms.xy(-170, -80)
        tile = tms._tile(x, y, zoom)
        bounds = tms.xy_bounds(tile)
        with pytest.raises(rioxarray.exceptions.OneDimensionalRaster) as error:
            dst.tile(tile.x, tile.y, zoom, auto_expand=False)
        assert "At least one of the clipped raster x,y coordinates" in str(error.value)

        # Test that a high-zoom tile will succeed with auto_expand=True (and that is the default)
        img = dst.tile(tile.x, tile.y, zoom)
        assert img.count == 1
        assert img.width == 256
        assert img.height == 256
        assert img.bounds == bounds
        assert img.dataset_statistics == ((arr.min(), arr.max()),)

        img = dst.part((-160, -80, 160, 80))
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        pt = dst.point(0, 0)
        assert pt.count == 1
        assert pt.band_names == ["2022-01-01T00:00:00.000000000"]
        assert pt.coordinates
        xys = [[0, 2.499], [0, 2.501], [-4.999, 0], [-5.001, 0], [-170, 80]]
        for xy in xys:
            x = xy[0]
            y = xy[1]
            pt = dst.point(x, y)
            assert pt.data[0] == data.sel(x=x, y=y, method="nearest")

        feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-92.46093749999999, 72.91963546581484],
                        [-148.0078125, 33.137551192346145],
                        [-143.08593749999997, -28.613459424004414],
                        [43.9453125, -47.04018214480665],
                        [142.734375, -12.897489183755892],
                        [157.5, 68.13885164925573],
                        [58.71093750000001, 74.95939165894974],
                        [-40.42968749999999, 75.14077784070429],
                        [-92.46093749999999, 72.91963546581484],
                    ]
                ],
            },
        }
        img = dst.feature(feat)
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        img = dst.feature(feat, dst_crs="epsg:3857")
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]
        assert img.crs.to_epsg() == 3857


def test_xarray_reader_external_nodata():
    """test XarrayReader."""
    # Create a 360/180 dataset that covers the whole world
    arr = numpy.arange(0.0, 360 * 180).reshape(1, 180, 360)
    arr[:, 0:50, 0:50] = 0  # we set the top-left corner to 0

    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-179.5, 180.5, 1),
            "y": numpy.arange(89.5, -90.5, -1),
            "time": [datetime(2022, 1, 1)],
        },
    )

    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    data.rio.write_crs("epsg:4326", inplace=True)
    with XarrayReader(data) as dst:
        info = dst.info()
        assert info.height == 180
        assert info.width == 360
        assert info.count == 1

    with XarrayReader(data) as dst:
        # TILE
        img = dst.tile(0, 0, 1)
        assert img.mask.all()
        assert img.data[0, 0, 0] == 0
        assert img.data[0, 100, 100]

        # overwrite the nodata value to 0
        img = dst.tile(0, 0, 1, nodata=0)
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 100, 100]  # pixel 100,100 shouldn't be masked

        # PART
        img = dst.part((-160, -80, 160, 80))
        assert img.mask.all()
        assert img.data[0, 0, 0] == 0
        assert img.data[0, 100, 100]

        # overwrite the nodata value to 0
        img = dst.part((-160, -80, 160, 80), nodata=0)
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 100, 100]  # pixel 100,100 shouldn't be masked

        # POINT
        pt = dst.point(-179, 89)
        assert pt.mask[0] == 255

        # overwrite the nodata value to 0
        pt = dst.point(-179, 89, nodata=0)
        assert pt.count == 1
        assert pt.mask[0] == 0

        feat = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-180.0, 0],
                        [-180.0, 85.0511287798066],
                        [0, 85.0511287798066],
                        [0, 6.023673383202919e-13],
                        [-180.0, 0],
                    ]
                ],
            },
            "properties": {"title": "XYZ tile (0, 0, 1)"},
        }

        # FEATURE
        img = dst.feature(feat)
        assert img.mask.all()
        assert img.data[0, 0, 0] == 0
        assert img.data[0, 50, 100]

        # overwrite the nodata value to 0
        img = dst.feature(feat, nodata=0)
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 50, 100]  # pixel 50,100 shouldn't be masked


def test_xarray_reader_internal_nodata():
    """test XarrayReader."""
    # Create a 360/180 dataset that covers the whole world
    arr = numpy.arange(0.0, 360 * 180).reshape(1, 180, 360)
    arr[:, 0:50, 0:50] = 0  # we set the top-left corner to 0

    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-179.5, 180.5, 1),
            "y": numpy.arange(89.5, -90.5, -1),
            "time": [datetime(2022, 1, 1)],
        },
        attrs={
            "missing_value": 0,
        },
    )

    data.rio.write_crs("epsg:4326", inplace=True)

    with XarrayReader(data) as dst:
        # TILE
        img = dst.tile(0, 0, 1)
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 100, 100]  # pixel 100,100 shouldn't be masked

        # PART
        img = dst.part((-160, -80, 160, 80))
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 100, 100]  # pixel 100,100 shouldn't be masked

        # POINT
        pt = dst.point(-179, 89)
        assert pt.count == 1
        assert pt.mask[0] == 0

        feat = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-180.0, 0],
                        [-180.0, 85.0511287798066],
                        [0, 85.0511287798066],
                        [0, 6.023673383202919e-13],
                        [-180.0, 0],
                    ]
                ],
            },
            "properties": {"title": "XYZ tile (0, 0, 1)"},
        }

        # FEATURE
        img = dst.feature(feat)
        assert not img.mask.all()  # not all the mask value are set to 255
        assert img.array.mask[0, 0, 0]  # the top left pixel should be masked
        assert not img.array.mask[0, 50, 100]  # pixel 50,100 shouldn't be masked


def test_xarray_reader_resampling():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 33 * 35).reshape(1, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": list(range(-170, 180, 10)),
            "y": list(range(-80, 85, 5)),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    data.rio.write_crs("epsg:4326", inplace=True)

    with XarrayReader(data) as dst:
        # TILE
        # default nearest
        img = dst.tile(0, 0, 1)
        img_cubic = dst.tile(0, 0, 1, reproject_method="cubic")
        assert not numpy.array_equal(img.array, img_cubic.array)

        with pytest.warns(DeprecationWarning):
            _ = dst.tile(0, 0, 1, resampling_method="nearest")

        # PART
        img = dst.part((-160, -80, 160, 80), dst_crs="epsg:3857")
        img_cubic = dst.part(
            (-160, -80, 160, 80), dst_crs="epsg:3857", reproject_method="cubic"
        )
        assert not numpy.array_equal(img.array, img_cubic.array)

        with pytest.warns(DeprecationWarning):
            _ = dst.part((-160, -80, 160, 80), resampling_method="nearest")

        feat = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-180.0, 0],
                        [-180.0, 85.0511287798066],
                        [0, 85.0511287798066],
                        [0, 6.023673383202919e-13],
                        [-180.0, 0],
                    ]
                ],
            },
            "properties": {"title": "XYZ tile (0, 0, 1)"},
        }

        # FEATURE
        img = dst.feature(feat, dst_crs="epsg:3857")
        img_cubic = dst.feature(feat, dst_crs="epsg:3857", reproject_method="cubic")
        assert not numpy.array_equal(img.array, img_cubic.array)

        with pytest.warns(DeprecationWarning):
            _ = dst.feature(feat, resampling_method="nearest")


def test_xarray_reader_no_crs():
    """Should raise MissingCRS."""
    arr = numpy.arange(0.0, 33 * 35).reshape(1, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-170, 180, 10),
            "y": numpy.arange(-80, 85, 5),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})
    with pytest.raises(MissingCRS):
        with XarrayReader(data):
            pass


def test_xarray_reader_invalid_bounds_crs():
    """Should raise InvalidGeographicBounds."""
    arr = numpy.arange(0.0, 33 * 35).reshape(1, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": list(range(10, 360, 10)),
            "y": list(range(-80, 85, 5)),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.rio.write_crs("epsg:4326", inplace=True)
    with pytest.raises(InvalidGeographicBounds):
        with XarrayReader(data):
            pass

    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": list(range(-170, 180, 10)),
            "y": list(range(15, 180, 5)),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.rio.write_crs("epsg:4326", inplace=True)
    with pytest.raises(InvalidGeographicBounds):
        with XarrayReader(data):
            pass
