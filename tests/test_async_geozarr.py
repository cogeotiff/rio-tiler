"""test rio_tiler.experimental.zarr.GeoZarrReader."""

from typing import Any

import numpy
import pytest
import zarr
from affine import Affine
from rasterio.crs import CRS

from rio_tiler.experimental.zarr import GeoZarrReader

from .utils import multiscale_conventions, proj_conventions, spatial_conventions

pytestmark = pytest.mark.asyncio


async def test_geozarr_reader():
    """Test XarrayReader and AsyncZarrReader compatibility."""
    store = zarr.storage.MemoryStore()

    # Create zarr dataset
    attributes: dict[str, Any] = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
        multiscale_conventions,
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
                            Affine.translation(500000, 4200000) * Affine.scale(10, -10)
                        ),
                    },
                    {
                        "asset": "1",
                        "spatial:dimensions": ["y", "x"],
                        "spatial:shape": [100, 100],
                        "spatial:transform": list(
                            Affine.translation(500000, 4200000) * Affine.scale(100, -100)
                        ),
                    },
                ]
            },
        }
    )

    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

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
                Affine.translation(500000, 4200000) * Affine.scale(10, -10)
            ),
        },
    )

    # Layout 0
    arr = numpy.arange(0.0, 1000 * 1000, dtype="float32").reshape(1000, 1000)
    arr[0:50, 0:50] = 0

    highres_b01 = highres_group.create_array(
        "b01",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    highres_b01[:] = arr

    highres_b02 = highres_group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    highres_b02[:] = arr

    # Layout 1
    arr = numpy.arange(0.0, 100 * 100, dtype="float32").reshape(100, 100)
    arr[0:5, 0:5] = 0

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
                Affine.translation(500000, 4200000) * Affine.scale(100, -100)
            ),
        },
    )

    lowres_b02 = lowres_group.create_array(
        "b02",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    lowres_b02[:] = arr

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)

    ###########################################################################
    group = await zarr.api.asynchronous.open_group(store=store, mode="r")

    geozarrds = GeoZarrReader(input=group)
    assert geozarrds.crs == CRS.from_epsg(32633)
    assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
    assert geozarrds.transform
    assert geozarrds.minzoom == 10
    assert geozarrds.maxzoom == 14

    info = await geozarrds.info()
    assert info.driver == "Zarr-Python"
    assert info.variables == ["b01", "b02"]

    vars = await geozarrds.list_variables()
    assert vars == ["b01", "b02"]

    # B01 has only one layout to minzoom 14, while b02 has two layouts with minzoom 10 and maxzoom 14
    z = await geozarrds.get_minzoom(variables="b01")
    assert z == 14
    z = await geozarrds.get_maxzoom(variables="b01")
    assert z == 14

    z = await geozarrds.get_minzoom(variables="b02")
    assert z == 10
    z = await geozarrds.get_maxzoom(variables="b02")
    assert z == 14

    meta = await geozarrds.get_group_metadata("root")
    assert meta["multiscale"]
    assert len(meta["arrays"]["b01"]) == 1
    assert len(meta["arrays"]["b02"]) == 2
    assert meta["arrays"]["b01"][0]["width"] == 1000
    assert meta["arrays"]["b02"][0]["width"] == 1000
    assert meta["arrays"]["b02"][1]["width"] == 100

    array = meta["arrays"].get("b02")
    selected = geozarrds.select_variable(array)
    assert selected["width"] == 1000

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


async def test_geozarr_root():
    """Test GeoZarrReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    store = zarr.storage.MemoryStore()

    attributes: dict[str, Any] = {}
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

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
                Affine.translation(500000, 4200000) * Affine.scale(10, -10)
            ),
        },
    )

    # Layout 0
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

    geozarrds = GeoZarrReader(input=group)
    assert geozarrds.crs == CRS.from_epsg(4326)
    assert geozarrds.bounds == (-180, -90, 180, 90)
    assert not geozarrds.transform
    assert geozarrds.minzoom == 0
    assert geozarrds.maxzoom == 24

    info = await geozarrds.info()
    assert info.driver == "Zarr-Python"
    assert info.variables == ["data:b01", "data:b02"]

    vars = await geozarrds.list_variables()
    assert vars == ["data:b01", "data:b02"]

    # No arrays/metadata at root level
    meta = await geozarrds.get_group_metadata("root")
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

    # No Multiscale
    z = await geozarrds.get_minzoom(variables="data:b01")
    assert z == 14
    z = await geozarrds.get_maxzoom(variables="data:b01")
    assert z == 14

    array = meta["arrays"].get("b01")
    selected = geozarrds.select_variable(array)
    assert selected["width"] == 1000

    bbox = await geozarrds.get_bounds(variables="data:b01")
    assert bbox == (
        14.999999999999982,
        37.857404200399316,
        15.113817624024337,
        37.94758957178317,
    )

    bbox = await geozarrds.get_bounds(variables="data:b01", crs=CRS.from_epsg(32633))
    assert bbox == (500000, 4190000, 510000, 4200000)


async def test_geozarr_root_with_arrays():
    """Test GeoZarrReader

    - root zarr store without any attribute:
        - bounds should be (-180, -90, 180, 90)
        - CRS should be EPSG:4326
        - minzoom should be 0 (TMS)
        - maxzoom should be 24 (TMS)

    """
    store = zarr.storage.MemoryStore()

    attributes = {
        "zarr_conventions": [
            spatial_conventions,
            proj_conventions,
        ],
        "spatial:dimensions": ["y", "x"],
        "spatial:bbox": [500000, 4190000, 510000, 4200000],
        "proj:code": "EPSG:32633",
        "spatial:transform": list(
            Affine.translation(500000, 4200000) * Affine.scale(10, -10)
        ),
    }
    root = zarr.open_group(store, mode="w", zarr_format=3, attributes=attributes)

    # Layout 0
    arr = numpy.arange(0.0, 1000 * 1000, dtype="float32").reshape(1000, 1000)
    arr[0:50, 0:50] = 0

    b01 = root.create_array(
        "b01",
        shape=arr.shape,
        chunks=(64, 64),
        dtype="float32",
        fill_value=0,
        dimension_names=["y", "x"],
        attributes={},
    )
    b01[:] = arr

    b02 = root.create_array(
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

    geozarrds = GeoZarrReader(input=group)
    assert geozarrds.crs == CRS.from_epsg(32633)
    assert geozarrds.bounds == (500000, 4190000, 510000, 4200000)
    assert geozarrds.transform
    assert geozarrds.minzoom == 14
    assert geozarrds.maxzoom == 14

    info = await geozarrds.info()
    assert info.driver == "Zarr-Python"
    assert info.variables == ["b01", "b02"]

    vars = await geozarrds.list_variables()
    assert vars == ["b01", "b02"]

    meta = await geozarrds.get_group_metadata("root")
    assert meta["crs"] == CRS.from_epsg(32633)
    assert meta["bbox"] == [500000, 4190000, 510000, 4200000]
    assert len(meta["arrays"]["b01"]) == 1
    assert len(meta["arrays"]["b02"]) == 1
    assert meta["arrays"]["b01"][0]["width"] == 1000
    assert meta["arrays"]["b02"][0]["width"] == 1000

    # No Multiscale
    z = await geozarrds.get_minzoom(variables="b01")
    assert z == 14
    z = await geozarrds.get_maxzoom(variables="b01")
    assert z == 14

    array = meta["arrays"].get("b01")
    selected = geozarrds.select_variable(array)
    assert selected["width"] == 1000

    bbox = await geozarrds.get_bounds(variables="b01")
    assert bbox == (
        14.999999999999982,
        37.857404200399316,
        15.113817624024337,
        37.94758957178317,
    )

    bbox = await geozarrds.get_bounds(variables="b01", crs=CRS.from_epsg(32633))
    assert bbox == (500000, 4190000, 510000, 4200000)
