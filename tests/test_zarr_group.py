"""test rio_tiler.experimental.zarr.AsyncGroupReader."""

from typing import Any

import attr
import numpy
import pytest
import zarr
from affine import Affine
from rasterio.crs import CRS

from rio_tiler.experimental.zarr import AsyncGroupReader, GroupReader

from .utils import (
    coordinates_conventions,
    multiscale_conventions,
    proj_conventions,
    spatial_conventions,
)


@pytest.fixture
def geozarr_store():
    """Create an in-memory GeoZarr store"""
    store = zarr.storage.MemoryStore()

    # Create zarr dataset
    attributes: dict[str, Any] = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
        multiscale_conventions,
        coordinates_conventions,
    ]
    attributes.update(
        {
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4190000, 510000, 4200000],
            "proj:code": "EPSG:32633",
            "multiscales": {
                "layout": [
                    {
                        "asset": "0",
                        "spatial:dimensions": ["y", "x"],
                        "spatial:shape": [1000, 1000],
                        "spatial:transform": list(
                            Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
                        ),
                    },
                    {
                        "asset": "1",
                        "spatial:dimensions": ["y", "x"],
                        "spatial:shape": [100, 100],
                        "spatial:transform": list(
                            Affine.translation(500000, 4200000) @ Affine.scale(100, -100)
                        ),
                    },
                ]
            },
            "coords:coordinates": {
                "time": {"type": "inline", "values": ["2022-01-01T00:00:00Z"]},
                "y": {"type": "reference", "convention": "spatial"},
                "x": {"type": "reference", "convention": "spatial"},
            },
        }
    )

    # /
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

    # /0
    # Layout 0 - b01 and b02 arrays
    highres_group = root.create_group(
        name="0",
        attributes={
            "zarr_conventions": [
                spatial_conventions,
                proj_conventions,
            ],
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4190000, 510000, 4200000],
            "proj:code": "EPSG:32633",
            "spatial:transform": list(
                Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
            ),
        },
    )

    arr = numpy.zeros((1, 1000, 1000), dtype="float32") + 1
    arr[:, 0:50, 0:50] = 0

    highres_b01 = highres_group.create_array(
        "b01",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    highres_b01[:] = arr

    highres_b02 = highres_group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    highres_b02[:] = arr

    # /1
    # Layout 1 - b02 array only
    arr = numpy.zeros((1, 100, 100), dtype="float32") + 2
    arr[:, 0:5, 0:5] = 0

    lowres_group = root.create_group(
        name="1",
        attributes={
            "zarr_conventions": [
                spatial_conventions,
                proj_conventions,
            ],
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4190000, 510000, 4200000],
            "proj:code": "EPSG:32633",
            "spatial:transform": list(
                Affine.translation(500000, 4200000) @ Affine.scale(100, -100)
            ),
        },
    )

    lowres_b02 = lowres_group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    lowres_b02[:] = arr

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)

    return store


@pytest.fixture
def geozarr_root_store():
    """Create an in-memory GeoZarr store without multiscale groups"""
    store = zarr.storage.MemoryStore()

    attributes: dict[str, Any] = {}
    # /
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

    # /data
    group = root.create_group(
        name="data",
        attributes={
            "zarr_conventions": [
                spatial_conventions,
                proj_conventions,
                coordinates_conventions,
            ],
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4190000, 510000, 4200000],
            "proj:code": "EPSG:32633",
            "spatial:transform": list(
                Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
            ),
            "coords:coordinates": {
                "time": {"type": "inline", "values": ["2022-01-01T00:00:00Z"]},
                "y": {"type": "reference", "convention": "spatial"},
                "x": {"type": "reference", "convention": "spatial"},
            },
        },
    )

    arr = numpy.arange(0.0, 1000 * 1000, dtype="float32").reshape(1, 1000, 1000)
    arr[:, 0:50, 0:50] = 0

    b01 = group.create_array(
        "b01",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    b01[:] = arr

    b02 = group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    b02[:] = arr

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)
    return store


@pytest.fixture
def geozarr_root_array_store():
    """Create an in-memory GeoZarr store without groups (only arrays)"""
    store = zarr.storage.MemoryStore()

    attributes = {
        "zarr_conventions": [
            spatial_conventions,
            proj_conventions,
            coordinates_conventions,
        ],
        "spatial:dimensions": ["y", "x"],
        "spatial:bbox": [500000, 4190000, 510000, 4200000],
        "proj:code": "EPSG:32633",
        "spatial:transform": list(
            Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
        ),
        "coords:coordinates": {
            "time": {"type": "inline", "values": ["2022-01-01T00:00:00Z"]},
            "y": {"type": "reference", "convention": "spatial"},
            "x": {"type": "reference", "convention": "spatial"},
        },
    }
    # /
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

    arr = numpy.arange(0.0, 1000 * 1000, dtype="float32").reshape(1, 1000, 1000)
    arr[:, 0:50, 0:50] = 0

    b01 = root.create_array(
        "b01",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    b01[:] = arr

    b02 = root.create_array(
        "b02",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["time", "y", "x"],
        attributes={},
    )
    b02[:] = arr

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)
    return store


@pytest.mark.asyncio
async def test_geozarr_reader_async(geozarr_store):
    """Test zarr AsyncGroupReader."""
    group = await zarr.api.asynchronous.open_group(store=geozarr_store, mode="r")

    async with AsyncGroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(32633)
        assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
        assert geozarrds.transform
        assert geozarrds.minzoom == 10
        assert geozarrds.maxzoom == 14

        info = await geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": True,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": True,
                "name": "b02",
            },
        ]

        vars = await geozarrds.list_variables()
        assert vars == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": True,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": True,
                "name": "b02",
            },
        ]

        # B01 has only one layout to minzoom 14, while b02 has two layouts with minzoom 10 and maxzoom 14
        z = await geozarrds.get_minzoom(variables="b01")
        assert z == 14
        z = await geozarrds.get_maxzoom(variables="b01")
        assert z == 14

        z = await geozarrds.get_minzoom(variables="b02")
        assert z == 10
        z = await geozarrds.get_maxzoom(variables="b02")
        assert z == 14

        meta = await geozarrds.get_group_metadata()
        assert meta["multiscale"]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 2
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b02"][1]["width"] == 100
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        array = meta["arrays"].get("b02")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        selected = geozarrds.select_variable(array, max_size=900)
        assert selected["width"] == 1000

        selected = geozarrds.select_variable(array, max_size=150)
        assert selected["width"] == 100

        selected = geozarrds.select_variable(array, max_size=50)
        assert selected["width"] == 100

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000

        selected = geozarrds.select_variable(array, max_size=50)
        assert selected["width"] == 1000

        img = await geozarrds.preview(variables=["b01", "b02"])
        assert img.array.shape == (2, 1, 1000, 1000)
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }
        assert not img.metadata

        img = await geozarrds.preview(
            variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.dimensions == ["variables", "y", "x"]
        assert img.array.shape == (2, 1000, 1000)
        assert img.band_descriptions == ["b01", "b02"]
        assert img.metadata == {"reduced": ["time"]}
        # max-size=1024 so we select the highest resolution (ones)
        assert numpy.ma.unique(img.array[0]).tolist() == [1.0, None]
        assert numpy.ma.unique(img.array[1]).tolist() == [1.0, None]

        img = await geozarrds.preview(
            variables=["b01", "b02"], max_size=100, reduce=[("time", numpy.ma.mean)]
        )
        assert img.band_descriptions == ["b01", "b02"]
        # b01 has only one array (ones)
        assert numpy.ma.unique(img.array[0]).tolist() == [1.0, None]
        # b02 has two arrays (ones: (1000x1000), twos: (100x100))
        assert numpy.ma.unique(img.array[1]).tolist() == [2.0, None]

        stats = await geozarrds.statistics(
            variables=["b01", "b02"], max_size=1024, reduce=[("time", numpy.ma.mean)]
        )
        assert stats["variables1"].description == "b01"
        assert stats["variables1"].min == 1.0
        assert stats["variables1"].max == 1.0
        assert stats["variables2"].description == "b02"
        assert stats["variables2"].min == 1.0
        assert stats["variables2"].max == 1.0

        stats = await geozarrds.statistics(
            variables=["b01", "b02"], max_size=100, reduce=[("time", numpy.ma.mean)]
        )
        assert stats["variables1"].min == 1.0
        assert stats["variables1"].max == 1.0
        assert stats["variables2"].min == 2.0
        assert stats["variables2"].max == 2.0

        pt = await geozarrds.point(
            505000,
            4195000,
            variables=["b01", "b02"],
            coord_crs="EPSG:32633",
        )
        assert pt.array.shape == (2, 1)
        assert pt.dimensions == ["variables", "time"]
        assert pt.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        pt = await geozarrds.point(
            505000,
            4195000,
            variables=["b01", "b02"],
            coord_crs="EPSG:32633",
            reduce=[("time", numpy.ma.mean)],
        )
        # select the highest resolution
        assert pt.array.shape == (2,)
        assert pt.data.tolist() == [1.0, 1.0]
        assert pt.band_descriptions == ["b01", "b02"]

        bounds = geozarrds.get_geographic_bounds("epsg:4326")
        center = ((bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2)
        z10_tile = geozarrds.tms.tile(center[0], center[1], 10)
        z14_tile = geozarrds.tms.tile(center[0], center[1], 14)

        # low res
        img = await geozarrds.tile(
            *z10_tile, variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.statistics()["variables1"].min == 1.0
        assert img.statistics()["variables2"].min == 2.0

        # high res
        img = await geozarrds.tile(
            *z14_tile, variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.statistics()["variables1"].min == 1.0
        assert img.statistics()["variables2"].min == 1.0

        z14_tile = geozarrds.tms.tile(center[0], center[1], 14)
        wgs84_bounds = geozarrds.tms.bounds(z14_tile)

        # PART
        # When no dst_crs is provided, the output should be in the same CRS as the bounds_crs
        img = await geozarrds.part(
            wgs84_bounds,
            variables=["b01", "b02"],
            bounds_crs="EPSG:4326",
            reduce=[("time", numpy.ma.mean)],
        )
        assert img.crs == "EPSG:4326"
        assert img.bounds == wgs84_bounds

        img = await geozarrds.part(
            wgs84_bounds,
            variables=["b01", "b02"],
            bounds_crs="EPSG:4326",
            dst_crs="EPSG:3857",
            reduce=[("time", numpy.ma.mean)],
        )
        assert img.crs == "EPSG:3857"
        assert img.bounds != wgs84_bounds


def test_geozarr_reader(geozarr_store):
    """Test zarr GroupReader."""
    group = zarr.open_group(store=geozarr_store, mode="r")

    with GroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(32633)
        assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
        assert geozarrds.transform
        assert geozarrds.minzoom == 10
        assert geozarrds.maxzoom == 14

        info = geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": True,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": True,
                "name": "b02",
            },
        ]

        vars = geozarrds.list_variables()
        assert vars == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": True,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": True,
                "name": "b02",
            },
        ]

        # B01 has only one layout to minzoom 14, while b02 has two layouts with minzoom 10 and maxzoom 14
        z = geozarrds.get_minzoom(variables="b01")
        assert z == 14
        z = geozarrds.get_maxzoom(variables="b01")
        assert z == 14

        z = geozarrds.get_minzoom(variables="b02")
        assert z == 10
        z = geozarrds.get_maxzoom(variables="b02")
        assert z == 14

        meta = geozarrds.get_group_metadata()
        assert meta["multiscale"]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 2
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b02"][1]["width"] == 100
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        array = meta["arrays"].get("b02")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        selected = geozarrds.select_variable(array, max_size=900)
        assert selected["width"] == 1000

        selected = geozarrds.select_variable(array, max_size=150)
        assert selected["width"] == 100

        selected = geozarrds.select_variable(array, max_size=50)
        assert selected["width"] == 100

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000

        selected = geozarrds.select_variable(array, max_size=50)
        assert selected["width"] == 1000

        img = geozarrds.preview(variables=["b01", "b02"])
        assert img.array.shape == (2, 1, 1000, 1000)
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }
        assert not img.metadata

        img = geozarrds.preview(
            variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.dimensions == ["variables", "y", "x"]
        assert img.array.shape == (2, 1000, 1000)
        assert img.band_descriptions == ["b01", "b02"]
        assert img.metadata == {"reduced": ["time"]}
        # max-size=1024 so we select the highest resolution (ones)
        assert numpy.ma.unique(img.array[0]).tolist() == [1.0, None]
        assert numpy.ma.unique(img.array[1]).tolist() == [1.0, None]

        img = geozarrds.preview(
            variables=["b01", "b02"], max_size=100, reduce=[("time", numpy.ma.mean)]
        )
        assert img.band_descriptions == ["b01", "b02"]
        # b01 has only one array (ones)
        assert numpy.ma.unique(img.array[0]).tolist() == [1.0, None]
        # b02 has two arrays (ones: (1000x1000), twos: (100x100))
        assert numpy.ma.unique(img.array[1]).tolist() == [2.0, None]

        stats = geozarrds.statistics(
            variables=["b01", "b02"], max_size=1024, reduce=[("time", numpy.ma.mean)]
        )
        assert stats["variables1"].min == 1.0
        assert stats["variables1"].max == 1.0
        assert stats["variables2"].min == 1.0
        assert stats["variables2"].max == 1.0

        stats = geozarrds.statistics(
            variables=["b01", "b02"], max_size=100, reduce=[("time", numpy.ma.mean)]
        )
        assert stats["variables1"].min == 1.0
        assert stats["variables1"].max == 1.0
        assert stats["variables2"].min == 2.0
        assert stats["variables2"].max == 2.0

        pt = geozarrds.point(
            505000,
            4195000,
            variables=["b01", "b02"],
            coord_crs="EPSG:32633",
        )
        assert pt.array.shape == (2, 1)
        assert pt.dimensions == ["variables", "time"]
        assert pt.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        pt = geozarrds.point(
            505000,
            4195000,
            variables=["b01", "b02"],
            coord_crs="EPSG:32633",
            reduce=[("time", numpy.ma.mean)],
        )
        # select the highest resolution
        assert pt.array.shape == (2,)
        assert pt.data.tolist() == [1.0, 1.0]
        assert pt.band_descriptions == ["b01", "b02"]

        bounds = geozarrds.get_geographic_bounds("epsg:4326")
        center = ((bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2)
        z10_tile = geozarrds.tms.tile(center[0], center[1], 10)
        z14_tile = geozarrds.tms.tile(center[0], center[1], 14)

        # low res
        img = geozarrds.tile(
            *z10_tile, variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.statistics()["variables1"].min == 1.0
        assert img.statistics()["variables2"].min == 2.0

        # high res
        img = geozarrds.tile(
            *z14_tile, variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.statistics()["variables1"].min == 1.0
        assert img.statistics()["variables2"].min == 1.0

        z14_tile = geozarrds.tms.tile(center[0], center[1], 14)
        wgs84_bounds = geozarrds.tms.bounds(z14_tile)

        # PART
        # When no dst_crs is provided, the output should be in the same CRS as the bounds_crs
        img = geozarrds.part(
            wgs84_bounds,
            variables=["b01", "b02"],
            bounds_crs="EPSG:4326",
            reduce=[("time", numpy.ma.mean)],
        )
        assert img.crs == "EPSG:4326"
        assert img.bounds == wgs84_bounds

        img = geozarrds.part(
            wgs84_bounds,
            variables=["b01", "b02"],
            bounds_crs="EPSG:4326",
            dst_crs="EPSG:3857",
            reduce=[("time", numpy.ma.mean)],
        )
        assert img.crs == "EPSG:3857"
        assert img.bounds != wgs84_bounds


@pytest.mark.asyncio
async def test_geozarr_root_async(geozarr_root_store):
    """Test AsyncGroupReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    group = await zarr.api.asynchronous.open_group(store=geozarr_root_store, mode="r")

    async with AsyncGroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(4326)
        assert geozarrds.bounds == (-180, -90, 180, 90)
        assert not geozarrds.transform
        assert geozarrds.minzoom == 0
        assert geozarrds.maxzoom == 24

        info = await geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": "data",
                "long_name": "data:b01",
                "multiscale": False,
                "name": "b01",
                # "nbands": 1,
            },
            {
                "group": "data",
                "long_name": "data:b02",
                "multiscale": False,
                "name": "b02",
                # "nbands": 1,
            },
        ]

        vars = await geozarrds.list_variables()
        assert vars == [
            {
                "group": "data",
                "long_name": "data:b01",
                "multiscale": False,
                "name": "b01",
                # "nbands": 1,
            },
            {
                "group": "data",
                "long_name": "data:b02",
                "multiscale": False,
                "name": "b02",
                # "nbands": 1,
            },
        ]

        # No arrays/metadata at root level
        meta = await geozarrds.get_group_metadata()
        assert meta == {
            "crs": None,
            "bbox": None,
            "transform": None,
            "multiscale": False,
            "arrays": {},
        }

        meta = await geozarrds.get_group_metadata("data")
        assert meta["crs"] == CRS.from_epsg(32633)
        assert meta["bbox"] == [500000, 4190000, 510000, 4200000]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 1
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        # No Multiscale
        z = await geozarrds.get_minzoom(variables="data:b01")
        assert z == 14
        z = await geozarrds.get_maxzoom(variables="data:b01")
        assert z == 14

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        bbox = await geozarrds.get_bounds(variables="data:b01")
        assert bbox == (
            14.999999999999982,
            37.857404200399316,
            15.113817624024337,
            37.94758957178317,
        )

        bbox = await geozarrds.get_bounds(variables="data:b01", crs=CRS.from_epsg(32633))
        assert bbox == (500000, 4190000, 510000, 4200000)

        img = await geozarrds.preview(variables=["data:b01", "data:b02"])
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["data:b01", "data:b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        img = await geozarrds.preview(
            variables=["data:b01", "data:b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_descriptions == ["data:b01", "data:b02"]


def test_geozarr_root(geozarr_root_store):
    """Test AsyncGroupReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    group = zarr.open_group(store=geozarr_root_store, mode="r")

    with GroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(4326)
        assert geozarrds.bounds == (-180, -90, 180, 90)
        assert not geozarrds.transform
        assert geozarrds.minzoom == 0
        assert geozarrds.maxzoom == 24

        info = geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": "data",
                "long_name": "data:b01",
                "multiscale": False,
                "name": "b01",
                # "nbands": 1,
            },
            {
                "group": "data",
                "long_name": "data:b02",
                "multiscale": False,
                "name": "b02",
                # "nbands": 1,
            },
        ]

        vars = geozarrds.list_variables()
        assert vars == [
            {
                "group": "data",
                "long_name": "data:b01",
                "multiscale": False,
                "name": "b01",
                # "nbands": 1,
            },
            {
                "group": "data",
                "long_name": "data:b02",
                "multiscale": False,
                "name": "b02",
                # "nbands": 1,
            },
        ]

        # No arrays/metadata at root level
        meta = geozarrds.get_group_metadata()
        assert meta == {
            "crs": None,
            "bbox": None,
            "transform": None,
            "multiscale": False,
            "arrays": {},
        }

        meta = geozarrds.get_group_metadata("data")
        assert meta["crs"] == CRS.from_epsg(32633)
        assert meta["bbox"] == [500000, 4190000, 510000, 4200000]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 1
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        # No Multiscale
        z = geozarrds.get_minzoom(variables="data:b01")
        assert z == 14
        z = geozarrds.get_maxzoom(variables="data:b01")
        assert z == 14

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        bbox = geozarrds.get_bounds(variables="data:b01")
        assert bbox == (
            14.999999999999982,
            37.857404200399316,
            15.113817624024337,
            37.94758957178317,
        )

        bbox = geozarrds.get_bounds(variables="data:b01", crs=CRS.from_epsg(32633))
        assert bbox == (500000, 4190000, 510000, 4200000)

        img = geozarrds.preview(variables=["data:b01", "data:b02"])
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["data:b01", "data:b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        img = geozarrds.preview(
            variables=["data:b01", "data:b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_descriptions == ["data:b01", "data:b02"]


@pytest.mark.asyncio
async def test_geozarr_root_with_arrays_async(geozarr_root_array_store):
    """Test AsyncGroupReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    group = await zarr.api.asynchronous.open_group(
        store=geozarr_root_array_store, mode="r"
    )

    async with AsyncGroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(32633)
        assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
        assert geozarrds.transform
        assert geozarrds.minzoom == 14
        assert geozarrds.maxzoom == 14

        info = await geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": False,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": False,
                "name": "b02",
            },
        ]

        vars = await geozarrds.list_variables()
        assert vars == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": False,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": False,
                "name": "b02",
            },
        ]

        meta = await geozarrds.get_group_metadata()
        assert meta["crs"] == CRS.from_epsg(32633)
        assert meta["bbox"] == [500000, 4190000, 510000, 4200000]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 1
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        # No Multiscale
        z = await geozarrds.get_minzoom(variables="b01")
        assert z == 14
        z = await geozarrds.get_maxzoom(variables="b01")
        assert z == 14

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        bbox = await geozarrds.get_bounds(variables="b01")
        assert bbox == (
            14.999999999999982,
            37.857404200399316,
            15.113817624024337,
            37.94758957178317,
        )

        bbox = await geozarrds.get_bounds(variables="b01", crs=CRS.from_epsg(32633))
        assert bbox == (500000, 4190000, 510000, 4200000)

        img = await geozarrds.preview(variables=["b01", "b02"])
        assert img.array.shape == (2, 1, 1000, 1000)
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        img = await geozarrds.preview(
            variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.array.shape == (2, 1000, 1000)
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_descriptions == ["b01", "b02"]


def test_geozarr_root_with_arrays(geozarr_root_array_store):
    """Test AsyncGroupReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    group = zarr.open_group(store=geozarr_root_array_store, mode="r")

    with GroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(32633)
        assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
        assert geozarrds.transform
        assert geozarrds.minzoom == 14
        assert geozarrds.maxzoom == 14

        info = geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": False,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": False,
                "name": "b02",
            },
        ]

        vars = geozarrds.list_variables()
        assert vars == [
            {
                "group": None,
                "long_name": "b01",
                "multiscale": False,
                "name": "b01",
            },
            {
                "group": None,
                "long_name": "b02",
                "multiscale": False,
                "name": "b02",
            },
        ]

        meta = geozarrds.get_group_metadata()
        assert meta["crs"] == CRS.from_epsg(32633)
        assert meta["bbox"] == [500000, 4190000, 510000, 4200000]
        assert len(meta["arrays"]["b01"]) == 1
        assert len(meta["arrays"]["b02"]) == 1
        assert meta["arrays"]["b01"][0]["width"] == 1000
        assert meta["arrays"]["b02"][0]["width"] == 1000
        assert meta["arrays"]["b01"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }
        assert meta["arrays"]["b02"][0]["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        # No Multiscale
        z = geozarrds.get_minzoom(variables="b01")
        assert z == 14
        z = geozarrds.get_maxzoom(variables="b01")
        assert z == 14

        array = meta["arrays"].get("b01")
        selected = geozarrds.select_variable(array)
        assert selected["width"] == 1000
        assert selected["coordinates"]["time"] == {
            "type": "inline",
            "values": ["2022-01-01T00:00:00Z"],
        }

        bbox = geozarrds.get_bounds(variables="b01")
        assert bbox == (
            14.999999999999982,
            37.857404200399316,
            15.113817624024337,
            37.94758957178317,
        )

        bbox = geozarrds.get_bounds(variables="b01", crs=CRS.from_epsg(32633))
        assert bbox == (500000, 4190000, 510000, 4200000)

        img = geozarrds.preview(variables=["b01", "b02"])
        assert img.array.shape == (2, 1, 1000, 1000)
        assert img.dimensions == ["variables", "time", "y", "x"]
        assert img.band_descriptions == {
            "variables": ["b01", "b02"],
            "time": ["2022-01-01T00:00:00Z"],
        }

        img = geozarrds.preview(
            variables=["b01", "b02"], reduce=[("time", numpy.ma.mean)]
        )
        assert img.array.shape == (2, 1000, 1000)
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_descriptions == ["b01", "b02"]


@pytest.mark.asyncio
async def test_custom_geozarr_separator_async():
    """Test Custom AsyncGroupReader"""

    @attr.s
    class CAsyncGroupReader(AsyncGroupReader):
        """Custom AsyncGroupReader with custom group/variable separator."""

        _group_var_sep: str = "::"

    store = zarr.storage.MemoryStore()

    attributes: dict[str, Any] = {}
    # /
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

    # /data
    group = root.create_group(
        name="data",
        attributes={
            "zarr_conventions": [
                spatial_conventions,
                proj_conventions,
            ],
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4190000, 510000, 4200000],
            "proj:code": "EPSG:32633",
            "spatial:transform": list(
                Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
            ),
        },
    )

    arr = numpy.arange(0.0, 1000 * 1000, dtype="float32").reshape(1000, 1000)
    arr[0:50, 0:50] = 0

    b01 = group.create_array(
        "b01",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    b01[:] = arr

    b02 = group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    b02[:] = arr

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)

    ###########################################################################
    group = await zarr.api.asynchronous.open_group(store=store, mode="r")

    async with CAsyncGroupReader(input=group) as geozarrds:
        assert geozarrds.crs == CRS.from_epsg(4326)
        assert geozarrds.bounds == (-180, -90, 180, 90)
        assert not geozarrds.transform
        assert geozarrds.minzoom == 0
        assert geozarrds.maxzoom == 24

        info = await geozarrds.info()
        assert info.driver == "GeoZarr"
        assert info.variables == [
            {
                "group": "data",
                "long_name": "data::b01",
                "multiscale": False,
                "name": "b01",
                # "nbands": 1,
            },
            {
                "group": "data",
                "long_name": "data::b02",
                "multiscale": False,
                "name": "b02",
                # "nbands": 1,
            },
        ]

        # No arrays/metadata at root level
        meta = await geozarrds.get_group_metadata()
        assert meta == {
            "crs": None,
            "bbox": None,
            "transform": None,
            "multiscale": False,
            "arrays": {},
        }

        # No Multiscale
        z = await geozarrds.get_minzoom(variables="data::b01")
        assert z == 14


TIMES = ["2025-01-01T00:00:00Z", "2025-02-01T00:00:00Z"]


@pytest.fixture
def geozarr_4d_store():
    """Create an in-memory GeoZarr store with 4D (time, z, y, x) arrays."""
    store = zarr.storage.MemoryStore()
    root = zarr.open_group(store, mode="w", zarr_format=3)

    group = root.create_group(
        name="data",
        attributes={
            "zarr_conventions": [
                spatial_conventions,
                proj_conventions,
                coordinates_conventions,
            ],
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000, 4199000, 501000, 4200000],
            "proj:code": "EPSG:32633",
            "spatial:transform": list(
                Affine.translation(500000, 4200000) @ Affine.scale(10, -10)
            ),
            "coords:coordinates": {
                "time": {"type": "inline", "values": TIMES},
                "z": {"type": "inline", "values": [0, 10, 20]},
                "y": {"type": "reference", "convention": "spatial"},
                "x": {"type": "reference", "convention": "spatial"},
            },
        },
    )

    # value = offset + time * 10 + z
    data = (
        numpy.arange(2)[:, None, None, None] * 10
        + numpy.arange(3)[None, :, None, None]
        + numpy.zeros((2, 3, 100, 100))
    ).astype("float32")
    for name, offset in [("a", 100), ("b", 200)]:
        arr = group.create_array(
            name,
            shape=data.shape,
            chunks=(1, 1, 50, 50),
            dtype="float32",
            fill_value=-1,
            dimension_names=["time", "z", "y", "x"],
        )
        arr[:] = data + offset

    return store


def test_group_reader_sel(geozarr_4d_store):
    """Test sel/sel_method forwarded to the arrays."""
    with GroupReader(input=zarr.open_group(geozarr_4d_store, mode="r")) as src:
        # Scalar selection on all the dimensions: one band per variable (2D)
        # 2D variables are stacked directly on the `variables` dimension
        img = src.preview(variables=["data:a", "data:b"], sel={"time": TIMES[1], "z": 10})
        assert img.array.shape == (2, 100, 100)
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_names == ["variables1", "variables2"]
        assert img.band_descriptions == ["data:a", "data:b"]
        assert img.array[:, 0, 0].tolist() == [111, 211]

        img = src.preview(
            variables=["data:a", "data:b"],
            sel={"time": "2025-01-20", "z": 12},
            sel_method="nearest",
            expression="variables2-variables1",
        )
        assert img.array[0, 0, 0] == 100

        # 3D output for one variable
        img = src.part(
            (500000, 4199500, 500500, 4200000),
            bounds_crs=CRS.from_epsg(32633),
            variables="data:a",
            sel={"time": TIMES[0]},
        )
        assert img.array.shape == (1, 3, 50, 50)
        assert img.dimensions == ["variables", "z", "y", "x"]
        assert img.array[0, :, 0, 0].tolist() == [100, 101, 102]

        img = src.tile(
            # center of the dataset (EPSG:32633 500250, 4199750)
            *src.tms.tile(15.0028, 37.9453, 15),
            variables="data:a",
            sel={"z": 0},
        )
        assert img.array.shape == (1, 2, 256, 256)

        pt = src.point(
            500005,
            4199995,
            coord_crs=CRS.from_epsg(32633),
            variables=["data:a", "data:b"],
            sel={"time": TIMES[0], "z": 20},
        )
        assert pt.dimensions == ["variables"]
        assert pt.band_descriptions == ["data:a", "data:b"]
        assert pt.array.tolist() == [102, 202]

        stats = src.statistics(variables="data:a", sel={"time": TIMES[1], "z": 0})
        assert stats["variables1"].min == 110
        assert stats["variables1"].description == "data:a"

        # N-D output for one variable
        img = src.preview(variables="data:a")
        assert img.array.shape == (1, 2, 3, 100, 100)
        assert img.band_names == {
            "variables": ["variables1"],
            "time": ["time1", "time2"],
            "z": ["z1", "z2", "z3"],
        }
        assert img.band_descriptions == {
            "variables": ["data:a"],
            "time": TIMES,
            "z": ["0", "10", "20"],
        }

        pt = src.point(
            500005, 4199995, coord_crs=CRS.from_epsg(32633), variables="data:a"
        )
        assert pt.array.shape == (1, 2, 3)

        # N-D output for multiple variables
        img = src.preview(variables=["data:a", "data:b"])
        assert img.array.shape == (2, 2, 3, 100, 100)
        assert img.dimensions == ["variables", "time", "z", "y", "x"]

        img = src.preview(
            variables=["data:a", "data:b"],
            reduce=[("time", numpy.ma.mean), ("z", numpy.ma.max)],
        )
        assert img.array.shape == (2, 100, 100)
        assert img.dimensions == ["variables", "y", "x"]
        # mean(time) = 5 and max(z) = 2
        assert img.array[:, 0, 0].tolist() == [107, 207]


@pytest.mark.asyncio
async def test_async_group_reader_sel(geozarr_4d_store):
    """Test sel/sel_method forwarded to the arrays."""
    group = await zarr.api.asynchronous.open_group(store=geozarr_4d_store, mode="r")
    async with AsyncGroupReader(input=group) as src:
        img = await src.preview(
            variables=["data:a", "data:b"], sel={"time": TIMES[1], "z": 10}
        )
        assert img.array[:, 0, 0].tolist() == [111, 211]
        assert img.dimensions == ["variables", "y", "x"]
        assert img.band_names == ["variables1", "variables2"]
        assert img.band_descriptions == ["data:a", "data:b"]

        img = await src.feature(
            {
                "type": "Polygon",
                "coordinates": [
                    [
                        [500000, 4199500],
                        [500500, 4199500],
                        [500500, 4200000],
                        [500000, 4200000],
                        [500000, 4199500],
                    ]
                ],
            },
            shape_crs=CRS.from_epsg(32633),
            variables="data:a",
            sel={"z": [0, 20]},
        )
        assert img.array.shape == (1, 2, 2, 50, 50)
        assert img.band_descriptions == {
            "variables": ["data:a"],
            "time": TIMES,
            "z": ["0", "20"],
        }

        pt = await src.point(
            500005,
            4199995,
            coord_crs=CRS.from_epsg(32633),
            variables="data:b",
            sel={"z": 0},
        )
        assert pt.array.tolist() == [[200, 210]]

        pt = await src.point(
            500005,
            4199995,
            coord_crs=CRS.from_epsg(32633),
            variables="data:b",
            sel={"z": 0},
            reduce=[("variables", numpy.ma.mean)],
        )
        assert pt.dimensions == ["time"]
        assert pt.array.tolist() == [200, 210]
