"""tests rio_tiler.io.xarray.XarrayReader"""

from datetime import datetime

import morecantile
import numpy
import pytest
import xarray
import zarr
from affine import Affine
from rasterio.crs import CRS
from xarray.backends.zarr import FillValueCoder

from rio_tiler.experimental.xarray import GeoArrayReader
from rio_tiler.io import XarrayReader


def test_geoxarray_reader():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 3600 * 1800 * 2, dtype="float32").reshape(2, 1800, 3600)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
    ) as dst:
        assert dst.crs == CRS.from_epsg(4326)
        assert dst.bounds == (-180.0, -90.0, 180.0, 90.0)
        assert dst.minzoom == dst.maxzoom == 0
        info = dst.info()
        assert info.band_metadata == [("b1", {}), ("b2", {})]
        assert info.band_descriptions == [
            ("b1", "b1"),
            ("b2", "b2"),
        ]
        assert info.height == 1800
        assert info.width == 3600
        assert info.count == 2
        assert info.attrs
        assert info.dimensions == ("time", "y", "x")

    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        band_names=["2022-01-01T00:00:00.000000", "2022-01-02T00:00:00.000000"],
    ) as dst:
        info = dst.info()
        assert info.band_descriptions == [
            ("b1", "2022-01-01T00:00:00.000000"),
            ("b2", "2022-01-02T00:00:00.000000"),
        ]

        stats = dst.statistics()
        assert list(stats) == [
            "b1",
            "b2",
        ]
        assert stats["b1"].min == 0.0

        stats = dst.statistics(indexes=1)
        assert list(stats) == ["b1"]
        assert stats["b1"].description == "2022-01-01T00:00:00.000000"

        stats = dst.statistics(indexes=2)
        assert list(stats) == ["b2"]
        assert stats["b2"].description == "2022-01-02T00:00:00.000000"

        stats = dst.statistics(indexes=(1, 2))
        assert list(stats) == [
            "b1",
            "b2",
        ]

        with pytest.raises(AssertionError):
            stats = dst.statistics(indexes=0)

        img = dst.tile(0, 0, 0)
        assert img.count == 2
        assert img.width == 256
        assert img.height == 256
        assert img.array.dtype == numpy.float32
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000",
            "2022-01-02T00:00:00.000000",
        ]
        assert img.dataset_statistics == ((arr.min(), arr.max()), (arr.min(), arr.max()))

        img = dst.tile(0, 0, 0, indexes=2)
        assert img.count == 1
        assert img.band_descriptions == [
            "2022-01-02T00:00:00.000000",
        ]

        tms = morecantile.tms.get("WebMercatorQuad")
        zoom = 10
        x, y = tms.xy(-170, -80)
        tile = tms._tile(x, y, zoom)
        bounds = tms.xy_bounds(tile)

        # Test that a high-zoom tile will succeed
        img = dst.tile(tile.x, tile.y, zoom, indexes=1)
        assert img.count == 1
        assert img.width == 256
        assert img.height == 256
        assert img.bounds == bounds
        assert img.dataset_statistics == ((arr.min(), arr.max()),)

        img = dst.part((-160, -80, 160, 80), indexes=1)
        assert img.crs == "epsg:4326"
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000"]
        assert img.array.shape == (1, 1600, 3200)
        assert img.array.dtype == numpy.float32

        img = dst.part((-160, -80, 160, 80), dst_crs="epsg:3857", indexes=1)
        assert img.crs == "epsg:3857"
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000"]
        assert img.array.shape == (1, 2352, 2696)

        img = dst.part(
            (-160, -80, 160, 80), dst_crs="epsg:3857", indexes=1, max_size=1024
        )
        assert img.crs == "epsg:3857"
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000"]
        assert img.array.shape == (1, 894, 1024)

        img = dst.part((-160, -80, 160, 80), max_size=15, indexes=1)
        assert img.array.shape == (1, 8, 15)

        img = dst.part((-160, -80, 160, 80), width=40, height=35, indexes=1)
        assert img.array.shape == (1, 35, 40)

        img = dst.part(
            (-160, -80, 160, 80), max_size=15, resampling_method="bilinear", indexes=1
        )
        assert img.array.shape == (1, 8, 15)

        img = dst.preview()
        assert img.crs == "epsg:4326"
        assert img.count == 2
        assert img.array.dtype == numpy.float32
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000",
            "2022-01-02T00:00:00.000000",
        ]
        assert img.array.shape == (2, 512, 1024)

        img = dst.preview(indexes=1)
        assert img.crs == "epsg:4326"
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000"]
        assert img.array.shape == (1, 512, 1024)

        img = dst.preview(dst_crs="epsg:3857", indexes=2)
        assert img.crs == "epsg:3857"
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-02T00:00:00.000000"]
        assert img.array.shape == (1, 1024, 1024)

        img = dst.preview(max_size=None, indexes=1)
        assert img.array.shape == (1, 1800, 3600)

        img = dst.preview(dst_crs="epsg:3857", max_size=15, indexes=1)
        assert img.array.shape == (1, 15, 15)

        img = dst.preview(max_size=15, indexes=1)
        assert img.array.shape == (1, 8, 15)

        img = dst.preview(height=25, width=25, max_size=None, indexes=1)
        assert img.array.shape == (1, 25, 25)

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
        assert img.count == 2
        assert img.array.dtype == numpy.float32
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000",
            "2022-01-02T00:00:00.000000",
        ]
        assert img.array.shape == (2, 1222, 3055)

        img = dst.feature(feat, indexes=2)
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-02T00:00:00.000000"]
        assert img.array.shape == (1, 1222, 3055)

        img = dst.feature(feat, dst_crs="epsg:3857", indexes=1)
        assert img.count == 1
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000"]
        assert img.crs == "epsg:3857"
        assert img.array.shape == (1, 1601, 2875)

        img = dst.feature(feat, max_size=15, indexes=1)
        assert img.array.shape == (1, 6, 15)

        img = dst.feature(feat, width=50, height=45, indexes=1)
        assert img.array.shape == (1, 45, 50)


def test_geoxarray_reader_point():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 3600 * 1800 * 2, dtype="float32").reshape(2, 1800, 3600)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-179.9, 180.1, 0.1),
            "y": numpy.arange(89.9, -90.1, -0.1),
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        band_names=["2022-01-01T00:00:00.000000", "2022-01-02T00:00:00.000000"],
    ) as dst:
        pt = dst.point(0, 0)
        assert pt.count == 2
        assert pt.band_descriptions == [
            "2022-01-01T00:00:00.000000",
            "2022-01-02T00:00:00.000000",
        ]
        assert pt.coordinates
        assert pt.pixel_location
        assert pt.array.dtype == numpy.float32

        xys = [[0, 2.499], [0, 2.501], [-4.999, 0], [-5.001, 0], [-170, 80]]
        for xy in xys:
            x = xy[0]
            y = xy[1]
            pt = dst.point(x, y)
            coords = pt.pixel_location
            numpy.testing.assert_array_equal(
                pt.data,
                data.values[:, coords[1], coords[0]],
            )

            # The GeoArray Reader assume coordinates registration to be `pixel` while
            # the xarray coordinates represent the center of the pixel.
            # So we need to shift the coordinates by half a pixel to get the correct value.
            transform = dst.transform
            x += transform.a / 2
            y += transform.e / 2

            numpy.testing.assert_array_equal(
                pt.data, data.sel(x=x, y=y, method="nearest").to_numpy()
            )

        pt = dst.point(0, 0, indexes=2)
        assert pt.count == 1
        assert pt.band_descriptions == ["2022-01-02T00:00:00.000000"]
        assert pt.coordinates
        xys = [[0, 2.499], [0, 2.501], [-4.999, 0], [-5.001, 0], [-170, 80]]
        for xy in xys:
            x = xy[0]
            y = xy[1]
            pt = dst.point(x, y)
            transform = dst.transform
            x += transform.a / 2
            y += transform.e / 2
            assert pt.data[0] == data.sel(
                time="2022-01-01T00:00:00.000000", x=x, y=y, method="nearest"
            )


def test_geoxarray_reader_compat():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 3600 * 1800 * 2, dtype="float32").reshape(2, 1800, 3600)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-179.9, 180.1, 0.1),
            "y": numpy.arange(89.9, -90.1, -0.1),
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})
    data.rio.write_crs("epsg:4326", inplace=True)

    geo_dst = GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        band_names=["2022-01-01T00:00:00.000000", "2022-01-02T00:00:00.000000"],
    )

    dst = XarrayReader(data)
    assert dst.crs == geo_dst.crs

    assert dst.transform != geo_dst.transform

    # The bounds of the XarrayReader are calculated from the coordinates (node registration),
    # while the bounds of the GeoArrayReader are calculated from the transform.
    assert dst.bounds != geo_dst.bounds

    info = dst.info()
    geoinfo = geo_dst.info()
    assert info.band_descriptions == geoinfo.band_descriptions

    stats = dst.statistics()
    geostat = geo_dst.statistics()
    assert list(stats) == list(geostat)

    tms = morecantile.tms.get("WebMercatorQuad")
    zoom = 10
    x, y = tms.xy(-170, -80)
    tile = tms._tile(x, y, zoom)

    img = dst.tile(tile.x, tile.y, zoom, indexes=1)
    geoimg = geo_dst.tile(tile.x, tile.y, zoom, indexes=1)

    numpy.testing.assert_allclose(img.array, geoimg.array, rtol=0.001)


def test_geoxarray_nodata():
    """test nodata in xarray."""
    arr = numpy.arange(0.0, 3600 * 1800, dtype="float32").reshape(1800, 3600)
    arr[0:50, 0:50] = 0.0  # we set the top-left corner to 0

    data = xarray.DataArray(arr, dims=("y", "x"))
    data.attrs.update(
        {
            "valid_min": arr.min(),
            "valid_max": arr.max(),
            "_FillValue": 0.0,
        }
    )

    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={},
    ) as dst:
        info = dst.info()
        assert info.nodata_type == "Nodata"

        img = dst.preview()
        assert numpy.ma.is_masked(img.array)
        assert img.array.mask[0, 0, 0]
        assert not img.array.mask[0, -1, -1]

    # missing_value
    data = xarray.DataArray(arr, dims=("y", "x"))
    data.attrs.update(
        {
            "valid_min": arr.min(),
            "valid_max": arr.max(),
            "missing_value": 0.0,
        }
    )
    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={},
    ) as dst:
        info = dst.info()
        assert info.nodata_type == "Nodata"

        img = dst.preview()
        assert numpy.ma.is_masked(img.array)
        assert img.array.mask[0, 0, 0]
        assert not img.array.mask[0, -1, -1]

    # fill_value (Xarray specific)
    data = xarray.DataArray(arr, dims=("y", "x"))
    data.attrs.update(
        {
            "valid_min": arr.min(),
            "valid_max": arr.max(),
            "fill_value": 0.0,
        }
    )
    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={},
    ) as dst:
        info = dst.info()
        assert info.nodata_type == "Nodata"

        img = dst.preview()
        assert numpy.ma.is_masked(img.array)
        assert img.array.mask[0, 0, 0]
        assert not img.array.mask[0, -1, -1]

    # nodata - GDAL like
    data = xarray.DataArray(arr, dims=("y", "x"))
    data.attrs.update(
        {
            "valid_min": arr.min(),
            "valid_max": arr.max(),
            "nodata": 0.0,
        }
    )

    with GeoArrayReader(
        input=data,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={},
    ) as dst:
        info = dst.info()
        assert info.nodata_type == "Nodata"

        img = dst.preview()
        assert numpy.ma.is_masked(img.array)
        assert img.array.mask[0, 0, 0]
        assert not img.array.mask[0, -1, -1]


def test_geoxarray_zarr_fill_value():
    """Interpret fill_value as Nodata within a Zarr Array."""
    store = zarr.storage.MemoryStore()
    dataset = zarr.create_group(store=store)
    zarrobj = dataset.create_array(
        "data",
        shape=(1800, 3600),
        chunks=(100, 100),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("y", "x"),
        attributes={
            "_FillValue": FillValueCoder.encode(-9999.0, numpy.dtype("float32")),
        },
    )
    zarrobj[:] = numpy.arange(0.0, 3600 * 1800, dtype="float32").reshape(1800, 3600)
    zarrobj[0:50, 0:50] = -9999.0  # Add some nodata
    zarr.consolidate_metadata(dataset.store)

    ds = xarray.open_dataset(
        store,  # type: ignore
        decode_times=False,
        decode_coords=False,
        consolidated=True,
        engine="zarr",
    )

    xarray_array = ds["data"]
    geods = GeoArrayReader(
        input=xarray_array,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={},
    )
    # The FillValue is not a `nodata` value per say in Zarr V3 model
    assert geods._nodata_value is None
    img = geods.preview()
    assert numpy.ma.is_masked(img.array)
    assert img.array.mask[0, 0, 0]
    assert not img.array.mask[0, -1, -1]


def test_geoxarray_zarr_nodata():
    """Merge both fill_value mask and nodata maske."""
    store = zarr.storage.MemoryStore()
    dataset = zarr.create_group(store=store)
    zarrobj = dataset.create_array(
        "data",
        shape=(1800, 3600),
        chunks=(100, 100),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("y", "x"),
        attributes={
            "_FillValue": FillValueCoder.encode(-9999.0, numpy.dtype("float32")),
        },
    )
    zarrobj[:] = numpy.arange(0.0, 3600 * 1800, dtype="float32").reshape(1800, 3600)
    zarrobj[0:50, 0:50] = -9999.0  # Add some nodata
    zarrobj[50:100, 0:50] = 0.0  # Add secondary nodata value

    zarr.consolidate_metadata(dataset.store)

    ds = xarray.open_dataset(
        store,  # type: ignore
        decode_times=False,
        decode_coords=False,
        consolidated=True,
        engine="zarr",
    )

    xarray_array = ds["data"]
    geods = GeoArrayReader(
        input=xarray_array,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        options={"nodata": 0.0},
    )
    # The FillValue is not a `nodata` value per say in Zarr V3 model
    assert geods._nodata_value is None
    # use max_size 3600 to return the full array without resampling
    img = geods.preview(max_size=3600)
    assert img.array.shape == (1, 1800, 3600)
    assert numpy.ma.is_masked(img.array)
    assert img.array.mask[0, 0, 0]
    assert img.array.mask[0, 50, 0]
    assert not img.array.mask[0, 100, 0]
    assert not img.array.mask[0, -1, -1]
