"""test rio_tiler.experimental.zarr.Reader."""

import os
import shutil
import warnings

import numpy
import obstore
import pandas
import pytest
import xarray
import zarr
from affine import Affine
from rasterio.crs import CRS
from rasterio.transform import from_bounds
from zarr.storage import ObjectStore

from rio_tiler.errors import (
    InvalidBounds,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.experimental.zarr import (
    ArrayMixin,
    ArrayReader,
    AsyncArrayReader,
    _format_coordinate_values,
    _get_coordinate_values,
    _sel_indexer,
)
from rio_tiler.io.xarray import XarrayReader

from .utils import (
    coordinates_conventions,
    create_zarr,
    proj_conventions,
    spatial_conventions,
)


@pytest.fixture
def zarr_dataset():
    """Create Zarr fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", "zarr_dataset.zarr")
    create_zarr(path)
    yield path
    if os.path.exists(path):
        shutil.rmtree(path)


@pytest.fixture
def geozarr_dataset():
    """Create Zarr fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", "geozarr_dataset.zarr")
    create_zarr(path, geozarr=True)
    yield path
    if os.path.exists(path):
        shutil.rmtree(path)


@pytest.fixture
def zarr_store() -> zarr.storage.MemoryStore:
    """Create an in-memory zarr array (3D: bands, height, width)."""
    store = zarr.storage.MemoryStore()
    arr_sync = zarr.create(
        store=store,
        shape=(3, 100, 100),
        chunks=(1, 50, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("band", "y", "x"),
    )
    arr_sync[:] = numpy.random.rand(3, 100, 100).astype("float32")
    arr_sync[0, 10:20, 10:20] = -9999.0  # Add some nodata

    return store


@pytest.fixture
def zarr_store_2d() -> zarr.storage.MemoryStore:
    """Create an in-memory zarr array (2D: height, width)."""
    store = zarr.storage.MemoryStore()
    arr_sync = zarr.create(
        store=store,
        shape=(50, 50),
        chunks=(25, 25),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("y", "x"),
    )
    arr_sync[:] = numpy.random.rand(50, 50).astype("float32")
    arr_sync[10:20, 10:20] = -9999.0  # Add some nodata

    return store


@pytest.fixture
def zarr_store_4d() -> zarr.storage.MemoryStore:
    """Create an in-memory 4D zarr array (time, z, y, x)."""
    store = zarr.storage.MemoryStore()
    arr = zarr.create(
        store=store,
        shape=(3, 4, 100, 100),
        chunks=(1, 1, 50, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("time", "z", "y", "x"),
    )
    # value = time * 10 + z (+ x/1000 to make pixels unique)
    data = (
        numpy.arange(3)[:, None, None, None] * 10
        + numpy.arange(4)[None, :, None, None]
        + numpy.arange(100)[None, None, None, :] / 1000
    )
    arr[:] = numpy.broadcast_to(data, (3, 4, 100, 100)).astype("float32")
    return store


@pytest.mark.asyncio
async def test_zarr_reader_async(zarr_store):
    """Test AsyncArrayReader with a 3D array (bands, height, width)."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    # Create reader with geospatial metadata
    # Use a proper north-up transform (pixel 0,0 at top-left)
    # Bounds in UTM: 500000, 4000000 to 500100, 4000100 (100x100m area, 1m pixels)
    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
        assert reader.spatial_dims == ["y", "x"]
        assert reader.dimensions == ["band", "y", "x"]

        # Test _read (full array)
        img = await reader.preview()
        assert img.array.shape == (3, 100, 100)
        assert img.band_names == ["b1", "b2", "b3"]
        assert img.band_descriptions == ["band1", "band2", "band3"]

        # Test _read with window
        img = await reader._read(y_slice=slice(10, 30), x_slice=slice(10, 30))
        assert img.array.shape == (3, 20, 20)

        # Test part (bbox read) - read a 40x40 pixel subset
        img = await reader.part(
            bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
        )
        assert img.array.shape == (3, 40, 40)

        # Test tile method
        img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256)
        assert img.array.shape[0] == 3

        # Test info method
        info = await reader.info()
        assert info.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
        assert info.driver == "Zarr"
        assert info.model_dump()
        assert info.model_dump_json()

        sel = reader._get_non_spatial_selection()
        assert sel["band"] == slice(None)

        sel = reader._get_non_spatial_selection(sel={"band": [1]})
        assert sel["band"] == numpy.array([1])

        sel = reader._get_non_spatial_selection(sel={"band": 0})
        assert sel["band"] == 0


def test_zarr_reader_sync(zarr_store):
    """Test AsyncArrayReader with a 3D array (bands, height, width)."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    # Create reader with geospatial metadata
    # Use a proper north-up transform (pixel 0,0 at top-left)
    # Bounds in UTM: 500000, 4000000 to 500100, 4000100 (100x100m area, 1m pixels)
    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
        assert reader.dimensions == ["band", "y", "x"]

        # Test _read (full array)
        img = reader.preview()
        assert img.array.shape == (3, 100, 100)
        assert img.band_names == ["b1", "b2", "b3"]
        assert img.band_descriptions == ["band1", "band2", "band3"]

        # Test _read with window
        img = reader._read(y_slice=slice(10, 30), x_slice=slice(10, 30))
        assert img.array.shape == (3, 20, 20)

        # Test part (bbox read) - read a 40x40 pixel subset
        img = reader.part(
            bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
        )
        assert img.array.shape == (3, 40, 40)

        # Test tile method
        img = reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256)
        assert img.array.shape[0] == 3

        # Test info method
        info = reader.info()
        assert info.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
        assert info.driver == "Zarr"
        assert info.model_dump()


@pytest.mark.asyncio
async def test_2d_array_async(zarr_store_2d):
    """Test with a 2D array (single band)."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
        assert reader.dimensions == ["y", "x"]

        img = await reader.preview()
        assert img.array.shape == (1, 50, 50), (
            f"Expected (1, 50, 50), got {img.array.shape}"
        )

        # Test info method
        info = await reader.info()
        assert info.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
        assert info.driver == "Zarr"
        assert info.model_dump()

    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
        coordinates={
            "y": {"type": "reference", "convention": "spatial"},
            "x": {"type": "reference", "convention": "spatial"},
        },
    ) as reader:
        assert reader.dimensions == ["y", "x"]


def test_2d_array_sync(zarr_store_2d):
    """Test with a 2D array (single band)."""
    arr = zarr.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
        assert reader.dimensions == ["y", "x"]

        img = reader.preview()
        assert img.array.shape == (1, 50, 50), (
            f"Expected (1, 50, 50), got {img.array.shape}"
        )

        # Test info method
        info = reader.info()
        assert info.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
        assert info.driver == "Zarr"
        assert info.model_dump()

    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
        coordinates={
            "y": {"type": "reference", "convention": "spatial"},
            "x": {"type": "reference", "convention": "spatial"},
        },
    ) as reader:
        assert reader.dimensions == ["y", "x"]


@pytest.mark.asyncio
async def test_part_same_crs_async(zarr_store):
    """Test part() method with same CRS as dataset."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)

        # Read a 40x40 pixel subset
        img = await reader.part(
            bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
        )
        assert img.array.shape == (3, 40, 40)
        assert img.bounds == (500010, 4000010, 500050, 4000050)
        assert img.crs == CRS.from_epsg(32618)


def test_part_same_crs(zarr_store):
    """Test part() method with same CRS as dataset."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)

        # Read a 40x40 pixel subset
        img = reader.part(
            bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
        )
        assert img.array.shape == (3, 40, 40)
        assert img.bounds == (500010, 4000010, 500050, 4000050)
        assert img.crs == CRS.from_epsg(32618)


@pytest.mark.asyncio
async def test_part_with_explicit_size_async(zarr_store):
    """Test part() method with explicit width/height."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read with explicit output size
        img = await reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            width=128,
            height=128,
        )
        assert img.array.shape == (3, 128, 128)
        assert img.bounds == (500010, 4000010, 500050, 4000050)


def test_part_with_explicit_size(zarr_store):
    """Test part() method with explicit width/height."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read with explicit output size
        img = reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            width=128,
            height=128,
        )
        assert img.array.shape == (3, 128, 128)
        assert img.bounds == (500010, 4000010, 500050, 4000050)


@pytest.mark.asyncio
async def test_part_with_max_size_async(zarr_store):
    """Test part() method with max_size constraint."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read with max_size constraint
        img = await reader.part(
            bbox=(500000, 4000000, 500100, 4000100),
            bounds_crs=CRS.from_epsg(32618),
            max_size=50,
        )
        # Should be constrained to max 50 pixels on longest side
        assert max(img.array.shape[1], img.array.shape[2]) == 50


def test_part_with_max_size(zarr_store):
    """Test part() method with max_size constraint."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read with max_size constraint
        img = reader.part(
            bbox=(500000, 4000000, 500100, 4000100),
            bounds_crs=CRS.from_epsg(32618),
            max_size=50,
        )
        # Should be constrained to max 50 pixels on longest side
        assert max(img.array.shape[1], img.array.shape[2]) == 50


@pytest.mark.asyncio
async def test_part_with_sel_async(zarr_store):
    """Test part() method with band selection."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read only band 1
        img = await reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            sel={"band": [0]},
        )
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["band1"]
        assert img.array.shape[0] == 1

        # Read bands 1 and 3
        img = await reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            sel={"band": [0, 2]},
        )
        assert img.band_names == ["b1", "b2"]
        assert img.band_descriptions == ["band1", "band3"]
        assert img.array.shape[0] == 2


def test_part_with_sel(zarr_store):
    """Test part() method with band selection."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read only band 1
        img = reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            sel={"band": [0]},
        )
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["band1"]
        assert img.array.shape[0] == 1

        # Read bands 1 and 3
        img = reader.part(
            bbox=(500010, 4000010, 500050, 4000050),
            bounds_crs=CRS.from_epsg(32618),
            sel={"band": [0, 2]},
        )
        assert img.band_names == ["b1", "b2"]
        assert img.band_descriptions == ["band1", "band3"]
        assert img.array.shape[0] == 2


@pytest.mark.asyncio
async def test_tile_async(zarr_store):
    """Test tile() method."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Default tile size from TMS
        img = await reader.tile(tile_x=0, tile_y=0, tile_z=0)
        assert img.array.shape[0] == 3  # 3 bands

        # Custom tile size
        img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=512)
        assert img.array.shape == (3, 512, 512)

        # Read only band 2
        img = await reader.tile(
            tile_x=0, tile_y=0, tile_z=0, tilesize=256, sel={"band": [1]}
        )
        assert img.array.shape[0] == 1

        img = await reader.tile(
            tile_x=0, tile_y=0, tile_z=0, tilesize=256, sel={"band": [0, 1]}
        )
        assert img.array.shape[0] == 2

        # Tile that doesn't intersect the dataset
        with pytest.raises(TileOutsideBounds):
            await reader.tile(tile_x=1000, tile_y=1000, tile_z=10)

        with pytest.raises(InvalidBounds):
            bounds = reader.tms.xy_bounds(1000, 1000, 10)
            await reader.part(bounds, bounds_crs=reader.tms.rasterio_crs)


def test_tile(zarr_store):
    """Test tile() method."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Default tile size from TMS
        img = reader.tile(tile_x=0, tile_y=0, tile_z=0)
        assert img.array.shape[0] == 3  # 3 bands

        # Custom tile size
        img = reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=512)
        assert img.array.shape == (3, 512, 512)

        # Read only band 2
        img = reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256, sel={"band": [1]})
        assert img.array.shape[0] == 1

        img = reader.tile(
            tile_x=0, tile_y=0, tile_z=0, tilesize=256, sel={"band": [0, 1]}
        )
        assert img.array.shape[0] == 2

        # Tile that doesn't intersect the dataset
        with pytest.raises(TileOutsideBounds):
            reader.tile(tile_x=1000, tile_y=1000, tile_z=10)

        with pytest.raises(InvalidBounds):
            bounds = reader.tms.xy_bounds(1000, 1000, 10)
            reader.part(bounds, bounds_crs=reader.tms.rasterio_crs)


@pytest.mark.asyncio
async def test_preview_async(zarr_store):
    """Test preview method."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Dataset is 100x100, smaller than default max_size=1024 → no resize
        img = await reader.preview()
        assert img.array.shape == (3, 100, 100)
        assert img.crs == CRS.from_epsg(32618)

        # Test with max_size smaller than dataset dimensions
        img = await reader.preview(max_size=50)
        assert max(img.array.shape[1], img.array.shape[2]) == 50
        # Square dataset → both dims should equal 50
        assert img.array.shape == (3, 50, 50)

        # Test with explicit width (height derived from aspect ratio)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = await reader.preview(width=64)
        assert img.width == 64
        assert img.array.shape[0] == 3

        # Test with explicit height (width derived from aspect ratio)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = await reader.preview(height=64)
        assert img.height == 64
        assert img.array.shape[0] == 3

        # Test  with both explicit width and height
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = await reader.preview(width=64, height=32)
            assert img.array.shape == (3, 32, 64)

        # Test with band selection.
        img = await reader.preview(sel={"band": [0]})
        assert img.array.shape[0] == 1

        img = await reader.preview(sel={"band": [0, 2]})
        assert img.array.shape[0] == 2

        # Test with band expression.
        img = await reader.preview(expression="b1/b2")
        assert img.array.shape[0] == 1

        # Test reprojects to dst_crs
        img = await reader.preview(dst_crs=CRS.from_epsg(4326))
        assert img.crs == CRS.from_epsg(4326)


def test_preview(zarr_store):
    """Test preview method."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Dataset is 100x100, smaller than default max_size=1024 → no resize
        img = reader.preview()
        assert img.array.shape == (3, 100, 100)
        assert img.crs == CRS.from_epsg(32618)

        # Test with max_size smaller than dataset dimensions
        img = reader.preview(max_size=50)
        assert max(img.array.shape[1], img.array.shape[2]) == 50
        # Square dataset → both dims should equal 50
        assert img.array.shape == (3, 50, 50)

        # Test with explicit width (height derived from aspect ratio)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = reader.preview(width=64)
        assert img.width == 64
        assert img.array.shape[0] == 3

        # Test with explicit height (width derived from aspect ratio)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = reader.preview(height=64)
        assert img.height == 64
        assert img.array.shape[0] == 3

        # Test  with both explicit width and height
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            img = reader.preview(width=64, height=32)
            assert img.array.shape == (3, 32, 64)

        # Test with band selection.
        img = reader.preview(sel={"band": [0]})
        assert img.array.shape[0] == 1

        img = reader.preview(sel={"band": [0, 2]})
        assert img.array.shape[0] == 2

        # Test with band expression.
        img = reader.preview(expression="b1/b2")
        assert img.array.shape[0] == 1

        # Test reprojects to dst_crs
        img = reader.preview(dst_crs=CRS.from_epsg(4326))
        assert img.crs == CRS.from_epsg(4326)


@pytest.mark.asyncio
async def test_preview_2d_async(zarr_store_2d):
    """Test preview() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        img = await reader.preview()
        assert img.array.shape == (1, 50, 50)


def test_preview_2d(zarr_store_2d):
    """Test preview() with a 2D (single-band) array."""
    arr = zarr.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        img = reader.preview()
        assert img.array.shape == (1, 50, 50)


@pytest.mark.asyncio
async def test_statistics_async(zarr_store):
    """Test statistics() method returns BandStatistics for each band."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        stats = await reader.statistics()
        assert isinstance(stats, dict)
        assert set(stats.keys()) == {"b1", "b2", "b3"}
        for band_stats in stats.values():
            assert band_stats.min is not None
            assert band_stats.max is not None
            assert band_stats.mean is not None
            assert band_stats.count > 0
            # nodata pixels should be excluded
            assert band_stats.min >= 0.0
            assert band_stats.max <= 1.0

        # overwrite nodata value
        stats = await reader.statistics(nodata=0, sel={"band": [0]})
        assert isinstance(stats, dict)
        band_stats = stats["b1"]
        assert band_stats.min == -9999.0

        # Test with band selection
        stats = await reader.statistics(sel={"band": [0]})
        assert set(stats.keys()) == {"b1"}

        stats = await reader.statistics(sel={"band": [0, 2]})
        assert set(stats.keys()) == {"b1", "b2"}
        assert stats["b1"].description == "band1"
        assert stats["b2"].description == "band3"

        # Test with a band expression
        stats = await reader.statistics(expression="b1/b2")
        assert len(stats) == 1
        assert set(stats.keys()) == {"b1"}
        assert stats["b1"].description == "band1/band2"

        # Test returns requested percentile values
        stats = await reader.statistics(percentiles=[5, 25, 75, 95])
        for band_stats in stats.values():
            extra = band_stats.model_extra or {}
            assert "percentile_5" in extra
            assert "percentile_25" in extra
            assert "percentile_75" in extra
            assert "percentile_95" in extra


def test_statistics(zarr_store):
    """Test statistics() method returns BandStatistics for each band."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        stats = reader.statistics()
        assert isinstance(stats, dict)
        assert set(stats.keys()) == {"b1", "b2", "b3"}
        for band_stats in stats.values():
            assert band_stats.min is not None
            assert band_stats.max is not None
            assert band_stats.mean is not None
            assert band_stats.count > 0
            # nodata pixels should be excluded
            assert band_stats.min >= 0.0
            assert band_stats.max <= 1.0

        # overwrite nodata value
        stats = reader.statistics(nodata=0, sel={"band": [0]})
        assert isinstance(stats, dict)
        band_stats = stats["b1"]
        assert band_stats.min == -9999.0

        # Test with band selection
        stats = reader.statistics(sel={"band": [0]})
        assert set(stats.keys()) == {"b1"}

        stats = reader.statistics(sel={"band": [0, 2]})
        assert set(stats.keys()) == {"b1", "b2"}
        assert stats["b1"].description == "band1"
        assert stats["b2"].description == "band3"

        # Test with a band expression
        stats = reader.statistics(expression="b1/b2")
        assert len(stats) == 1
        assert set(stats.keys()) == {"b1"}
        assert stats["b1"].description == "band1/band2"

        # Test returns requested percentile values
        stats = reader.statistics(percentiles=[5, 25, 75, 95])
        for band_stats in stats.values():
            extra = band_stats.model_extra or {}
            assert "percentile_5" in extra
            assert "percentile_25" in extra
            assert "percentile_75" in extra
            assert "percentile_95" in extra


@pytest.mark.asyncio
async def test_statistics_2d_async(zarr_store_2d):
    """Test statistics() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        stats = await reader.statistics()
        assert set(stats.keys()) == {"b1"}
        assert stats["b1"].min >= 0.0
        assert stats["b1"].max <= 1.0


def test_statistics_2d(zarr_store_2d):
    """Test statistics() with a 2D (single-band) array."""
    arr = zarr.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        stats = reader.statistics()
        assert set(stats.keys()) == {"b1"}
        assert stats["b1"].min >= 0.0
        assert stats["b1"].max <= 1.0


@pytest.mark.asyncio
async def test_point_async(zarr_store):
    """Test point() method reads a single pixel value."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read point in dataset CRS (UTM 18N)
        # Pick a point in the middle of the dataset
        pt = await reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
        )
        assert pt.array.shape[0] == 3
        assert pt.crs == CRS.from_epsg(32618)
        assert pt.coordinates == (500050.0, 4000050.0)
        assert pt.band_names == ["b1", "b2", "b3"]

        # Test method with band selection
        # Read only band 1
        pt = await reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
            sel={"band": [0]},
        )
        assert pt.array.shape[0] == 1
        assert pt.band_names == ["b1"]

        # Read bands 1 and 3
        pt = await reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
            sel={"band": [0, 2]},
        )
        assert pt.array.shape[0] == 2
        assert pt.band_names == ["b1", "b2"]
        assert pt.band_descriptions == ["band1", "band3"]

        # Test raises error for points outside bounds.
        # Point outside dataset bounds
        with pytest.raises(PointOutsideBounds):
            await reader.point(
                lon=600000.0,
                lat=5000000.0,
                coord_crs=CRS.from_epsg(32618),
            )


def test_point(zarr_store):
    """Test point() method reads a single pixel value."""
    arr = zarr.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        # Read point in dataset CRS (UTM 18N)
        # Pick a point in the middle of the dataset
        pt = reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
        )
        assert pt.array.shape[0] == 3
        assert pt.crs == CRS.from_epsg(32618)
        assert pt.coordinates == (500050.0, 4000050.0)
        assert pt.band_names == ["b1", "b2", "b3"]

        # Test method with band selection
        # Read only band 1
        pt = reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
            sel={"band": [0]},
        )
        assert pt.array.shape[0] == 1
        assert pt.band_names == ["b1"]

        # Read bands 1 and 3
        pt = reader.point(
            lon=500050.0,
            lat=4000050.0,
            coord_crs=CRS.from_epsg(32618),
            sel={"band": [0, 2]},
        )
        assert pt.array.shape[0] == 2
        assert pt.band_names == ["b1", "b2"]
        assert pt.band_descriptions == ["band1", "band3"]

        # Test raises error for points outside bounds.
        # Point outside dataset bounds
        with pytest.raises(PointOutsideBounds):
            reader.point(
                lon=600000.0,
                lat=5000000.0,
                coord_crs=CRS.from_epsg(32618),
            )


@pytest.mark.asyncio
async def test_point_2d_async(zarr_store_2d):
    """Test point() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    async with AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        pt = await reader.point(
            lon=500025.0,
            lat=4000025.0,
            coord_crs=CRS.from_epsg(32618),
        )
        assert pt.data.shape == (1,)  # Single band
        assert pt.band_names == ["b1"]


def test_point_2d(zarr_store_2d):
    """Test point() with a 2D (single-band) array."""
    arr = zarr.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) @ Affine.scale(1, -1)
    with ArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
        spatial_dims=["y", "x"],
    ) as reader:
        pt = reader.point(
            lon=500025.0,
            lat=4000025.0,
            coord_crs=CRS.from_epsg(32618),
        )
        assert pt.data.shape == (1,)  # Single band
        assert pt.band_names == ["b1"]


@pytest.mark.asyncio
async def test_band_descriptions_async(zarr_dataset):
    """Test XarrayReader and AsyncArrayReader compatibility."""
    store = obstore.store.from_url(f"file://{zarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
    array = await group.getitem("dataset")

    # Get Time coordinates from the zarr store
    time = await group.getitem("time")
    time_arrray = await time.getitem(slice(None))

    async with AsyncArrayReader(
        input=array,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) @ Affine.scale(0.1, -0.1),
        spatial_dims=["y", "x"],
        coordinates={
            "time": {"type": "inline", "values": [str(d) for d in time_arrray.tolist()]}
        },
    ) as reader:
        assert reader.dimensions == ["time", "y", "x"]

        img = await reader.preview(sel={"time": ["2022-01-01"]})
        assert img.band_descriptions == ["2022-01-01"]

        img = await reader.preview(sel={"time": ["2022-01-02"]})
        assert img.band_descriptions == ["2022-01-02"]

        img = await reader.preview(expression="b1/b2")
        assert img.band_descriptions == ["2022-01-01/2022-01-02"]


def test_band_descriptions(zarr_dataset):
    """Test XarrayReader and AsyncArrayReader compatibility."""
    store = obstore.store.from_url(f"file://{zarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = zarr.open_group(store=zarr_store, mode="r")
    array = group["dataset"]

    # Get Time coordinates from the zarr store
    time = group["time"]
    time_arrray = time[:]

    with ArrayReader(
        input=array,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) @ Affine.scale(0.1, -0.1),
        spatial_dims=["y", "x"],
        coordinates={
            "time": {"type": "inline", "values": [str(d) for d in time_arrray.tolist()]}
        },
    ) as reader:
        img = reader.preview(sel={"time": ["2022-01-01"]})
        assert img.band_descriptions == ["2022-01-01"]

        img = reader.preview(sel={"time": ["2022-01-02"]})
        assert img.band_descriptions == ["2022-01-02"]

        img = reader.preview(expression="b1/b2")
        assert img.band_descriptions == ["2022-01-01/2022-01-02"]


@pytest.mark.asyncio
async def test_geozarr_async(geozarr_dataset):
    """Test GeoZarr with AsyncArrayReader."""
    store = obstore.store.from_url(f"file://{geozarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
    array = await group.getitem("dataset")

    # Get Time coordinates from the zarr store
    time = await group.getitem("time")
    time_arrray = await time.getitem(slice(None))

    async with AsyncArrayReader(
        input=array,
        coordinates={
            "time": {"type": "inline", "values": [str(d) for d in time_arrray.tolist()]}
        },
    ) as reader:
        assert reader.crs == CRS.from_epsg(4326)
        assert reader.bounds == (-180.0, -90.0, 180.0, 90.0)
        info = await reader.info()
        assert info.dimensions_count == {"time": 2, "y": 1800, "x": 3600}

        img = await reader.preview(sel={"time": ["2022-01-01"]})
        assert img.crs == CRS.from_epsg(4326)
        assert img.bounds == (-180.0, -90.0, 180.0, 90.0)
        assert img.band_descriptions == ["2022-01-01"]

    # bands names from coords convention
    async with AsyncArrayReader(input=array) as reader:
        img = await reader.preview()
        assert img.band_descriptions == [
            "2022-01-01T00:00:00Z",
            "2022-01-02T00:00:00Z",
        ]


def test_geozarr(geozarr_dataset):
    """Test GeoZarr with ArrayReader."""
    store = obstore.store.from_url(f"file://{geozarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = zarr.open_group(store=zarr_store, mode="r")
    array = group["dataset"]

    # Get Time coordinates from the zarr store
    time = group["time"]
    time_arrray = time[:]

    with ArrayReader(
        input=array,
        coordinates={
            "time": {"type": "inline", "values": [str(d) for d in time_arrray.tolist()]}
        },
    ) as reader:
        assert reader.crs == CRS.from_epsg(4326)
        assert reader.bounds == (-180.0, -90.0, 180.0, 90.0)

        img = reader.preview(sel={"time": ["2022-01-01"]})
        assert img.crs == CRS.from_epsg(4326)
        assert img.bounds == (-180.0, -90.0, 180.0, 90.0)
        assert img.band_descriptions == ["2022-01-01"]

    # bands names from coords convention
    with ArrayReader(input=array) as reader:
        img = reader.preview()
        assert img.band_descriptions == [
            "2022-01-01T00:00:00Z",
            "2022-01-02T00:00:00Z",
        ]


@pytest.mark.asyncio
async def test_compat_xarray_async(zarr_dataset):
    """Test XarrayReader and AsyncArrayReader compatibility."""
    store = obstore.store.from_url(f"file://{zarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    ds = xarray.open_dataset(
        zarr_store,  # type: ignore
        decode_times=True,
        decode_coords="all",
        consolidated=True,
        engine="zarr",
    )
    xarray_array = ds["dataset"]
    xarray_array = xarray_array.rio.write_crs("epsg:4326")

    xarrayds = XarrayReader(input=xarray_array)
    transform = from_bounds(*xarrayds.bounds, xarrayds.width, xarrayds.height)

    group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
    array = await group.getitem("dataset")

    async_zarrds = AsyncArrayReader(
        input=array,
        crs=CRS.from_epsg(4326),
        # Ref: https://github.com/cogeotiff/rio-tiler/issues/905
        # Use the same transform as xarray to ensure the same bounds and pixel alignment
        # transform=Affine.translation(-180, 90) @ Affine.scale(0.1, -0.1),
        transform=transform,
        spatial_dims=["y", "x"],
    )

    # Statistics
    stats = xarrayds.statistics(nodata=0)
    zarr_stats = await async_zarrds.statistics()
    assert stats["b1"]
    assert zarr_stats["b1"]
    assert zarr_stats["b1"].min == stats["b1"].min
    assert zarr_stats["b1"].max == stats["b1"].max
    assert zarr_stats["b1"].mean == stats["b1"].mean
    assert zarr_stats["b1"].count == stats["b1"].count
    assert zarr_stats["b1"].sum == stats["b1"].sum
    assert zarr_stats["b1"].percentile_2 == stats["b1"].percentile_2
    assert zarr_stats["b1"].histogram == stats["b1"].histogram

    # Preview
    img = xarrayds.preview(nodata=0)
    zarr_img = await async_zarrds.preview()
    assert img.array.shape == zarr_img.array.shape
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    # Tile
    img = xarrayds.tile(0, 0, 0)
    assert img.array.shape[0] == 2
    assert img.width == 256
    assert img.height == 256
    assert img.array.dtype == numpy.float32

    zarr_img = await async_zarrds.tile(0, 0, 0)
    assert zarr_img.array.shape[0] == 2
    assert zarr_img.width == 256
    assert zarr_img.height == 256
    assert zarr_img.array.dtype == numpy.float32

    assert zarr_img.bounds == img.bounds
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    zoom = 10
    x, y = async_zarrds.tms.xy(-179, -80)
    tile = async_zarrds.tms._tile(x, y, zoom)
    img = xarrayds.tile(tile.x, tile.y, zoom)
    zarr_img = await async_zarrds.tile(tile.x, tile.y, zoom)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Part
    img = xarrayds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert img.crs == "epsg:4326"
    assert img.array.shape == (2, 1600, 3200)

    zarr_img = await async_zarrds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert zarr_img.crs == "epsg:4326"
    assert zarr_img.array.shape == (2, 1600, 3200)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    img = xarrayds.part((-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 88, 100)

    zarr_img = await async_zarrds.part(
        (-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100
    )
    assert zarr_img.crs == "epsg:3857"
    assert zarr_img.array.shape == (2, 88, 100)

    ###############################################################
    # NOTE: shape of the reprojected image is different from xarray
    # and zarr due to differences in how they calculate the output
    # dimensions during reprojection. This is maybe a bug
    ###############################################################
    img = xarrayds.part((-160, -80, 160, 80), dst_crs="epsg:3857")
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 2350, 2694)

    zarr_img = await async_zarrds.part((-160, -80, 160, 80), dst_crs="epsg:3857")
    assert zarr_img.crs == "epsg:3857"
    assert zarr_img.array.shape == (2, 2352, 2696)
    # numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Point
    pt = xarrayds.point(0, 0)
    assert pt.array.shape[0] == 2
    assert pt.coordinates
    assert pt.pixel_location
    assert pt.array.dtype == numpy.float32

    zarr_pt = await async_zarrds.point(0, 0)
    assert zarr_pt.array.shape[0] == 2
    assert zarr_pt.coordinates
    assert zarr_pt.pixel_location
    assert zarr_pt.array.dtype == numpy.float32
    numpy.testing.assert_array_equal(pt.array, zarr_pt.array)

    ## Masked
    pt = xarrayds.point(-179, 89, nodata=0)
    zarr_pt = await async_zarrds.point(-179, 89)
    numpy.testing.assert_array_equal(pt.array, zarr_pt.array)

    # Feature
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
    img = xarrayds.feature(feat)
    assert img.array.dtype == numpy.float32
    assert img.array.shape == (2, 1222, 3055)

    zarr_img = await async_zarrds.feature(feat)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 1222, 3055)
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    img = xarrayds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 56, 100)

    zarr_img = await async_zarrds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 56, 100)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)


def test_compat_xarray(zarr_dataset):
    """Test XarrayReader and AsyncArrayReader compatibility."""
    store = obstore.store.from_url(f"file://{zarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    ds = xarray.open_dataset(
        zarr_store,  # type: ignore
        decode_times=True,
        decode_coords="all",
        consolidated=True,
        engine="zarr",
    )
    xarray_array = ds["dataset"]
    xarray_array = xarray_array.rio.write_crs("epsg:4326")

    xarrayds = XarrayReader(input=xarray_array)
    transform = from_bounds(*xarrayds.bounds, xarrayds.width, xarrayds.height)

    group = zarr.open_group(store=zarr_store, mode="r")
    array = group["dataset"]

    zarrds = ArrayReader(
        input=array,
        crs=CRS.from_epsg(4326),
        # Ref: https://github.com/cogeotiff/rio-tiler/issues/905
        # Use the same transform as xarray to ensure the same bounds and pixel alignment
        # transform=Affine.translation(-180, 90) @ Affine.scale(0.1, -0.1),
        transform=transform,
        spatial_dims=["y", "x"],
    )

    # Statistics
    stats = xarrayds.statistics(nodata=0)
    zarr_stats = zarrds.statistics()
    assert stats["b1"]
    assert zarr_stats["b1"]
    assert zarr_stats["b1"].min == stats["b1"].min
    assert zarr_stats["b1"].max == stats["b1"].max
    assert zarr_stats["b1"].mean == stats["b1"].mean
    assert zarr_stats["b1"].count == stats["b1"].count
    assert zarr_stats["b1"].sum == stats["b1"].sum
    assert zarr_stats["b1"].percentile_2 == stats["b1"].percentile_2
    assert zarr_stats["b1"].histogram == stats["b1"].histogram

    # Preview
    img = xarrayds.preview(nodata=0)
    zarr_img = zarrds.preview()
    assert img.array.shape == zarr_img.array.shape
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    # Tile
    img = xarrayds.tile(0, 0, 0)
    assert img.array.shape[0] == 2
    assert img.width == 256
    assert img.height == 256
    assert img.array.dtype == numpy.float32

    zarr_img = zarrds.tile(0, 0, 0)
    assert zarr_img.array.shape[0] == 2
    assert zarr_img.width == 256
    assert zarr_img.height == 256
    assert zarr_img.array.dtype == numpy.float32

    assert zarr_img.bounds == img.bounds
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    zoom = 10
    x, y = zarrds.tms.xy(-179, -80)
    tile = zarrds.tms._tile(x, y, zoom)
    img = xarrayds.tile(tile.x, tile.y, zoom)
    zarr_img = zarrds.tile(tile.x, tile.y, zoom)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Part
    img = xarrayds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert img.crs == "epsg:4326"
    assert img.array.shape == (2, 1600, 3200)

    zarr_img = zarrds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert zarr_img.crs == "epsg:4326"
    assert zarr_img.array.shape == (2, 1600, 3200)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    img = xarrayds.part((-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 88, 100)

    zarr_img = zarrds.part((-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100)
    assert zarr_img.crs == "epsg:3857"
    assert zarr_img.array.shape == (2, 88, 100)

    ###############################################################
    # NOTE: shape of the reprojected image is different from xarray
    # and zarr due to differences in how they calculate the output
    # dimensions during reprojection. This is maybe a bug
    ###############################################################
    img = xarrayds.part((-160, -80, 160, 80), dst_crs="epsg:3857")
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 2350, 2694)

    zarr_img = zarrds.part((-160, -80, 160, 80), dst_crs="epsg:3857")
    assert zarr_img.crs == "epsg:3857"
    assert zarr_img.array.shape == (2, 2352, 2696)
    # numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Point
    pt = xarrayds.point(0, 0)
    assert pt.array.shape[0] == 2
    assert pt.coordinates
    assert pt.pixel_location
    assert pt.array.dtype == numpy.float32

    zarr_pt = zarrds.point(0, 0)
    assert zarr_pt.array.shape[0] == 2
    assert zarr_pt.coordinates
    assert zarr_pt.pixel_location
    assert zarr_pt.array.dtype == numpy.float32
    numpy.testing.assert_array_equal(pt.array, zarr_pt.array)

    ## Masked
    pt = xarrayds.point(-179, 89, nodata=0)
    zarr_pt = zarrds.point(-179, 89)
    numpy.testing.assert_array_equal(pt.array, zarr_pt.array)

    # Feature
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
    img = xarrayds.feature(feat)
    assert img.array.dtype == numpy.float32
    assert img.array.shape == (2, 1222, 3055)

    zarr_img = zarrds.feature(feat)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 1222, 3055)
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    img = xarrayds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 56, 100)

    zarr_img = zarrds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 56, 100)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)


@pytest.mark.asyncio
async def test_coords_conventions_mixin():
    """Test Coordinates convention support."""
    store = zarr.storage.MemoryStore()

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
        coordinates_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(1, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    # add coordinates metadata
    attributes["coords:coordinates"] = {
        "time": {"type": "inline", "values": ["t1", "t2", "t3"]},
        "y": {"type": "reference", "convention": "spatial"},
        "x": {"type": "reference", "convention": "spatial"},
    }
    arr_sync = zarr.create(
        store=store,
        shape=(3, 100, 100),
        chunks=(1, 50, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("time", "y", "x"),
        attributes=attributes,
    )
    arr_sync[:] = numpy.random.rand(3, 100, 100).astype("float32")
    arr_sync[0, 10:20, 10:20] = -9999.0  # Add some nodata

    arr = await zarr.api.asynchronous.open_array(store=store, mode="r")

    reader = ArrayMixin(input=arr)
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader.dimensions == ["time", "y", "x"]
    assert reader.coordinates["time"] == {"type": "inline", "values": ["t1", "t2", "t3"]}
    assert reader.height == 100
    assert reader.width == 100

    # Interval
    reader = ArrayMixin(
        input=arr,
        coordinates={
            "time": {"type": "interval", "start": 1000, "stop": 3000, "step": 1000}
        },
    )
    assert reader.coordinates["time"] == {
        "type": "interval",
        "start": 1000,
        "stop": 3000,
        "step": 1000,
    }
    assert reader.height == 100
    assert reader.width == 100

    # Date Interval
    reader = ArrayMixin(
        input=arr,
        coordinates={
            "time": {
                "type": "interval",
                "start": "2024-01-01T00:00:00Z",
                "stop": "2024-01-03T00:00:00Z",
                "step": "P1D",
            }
        },
    )
    assert reader.height == 100
    assert reader.width == 100
    assert reader.coordinates["time"] == {
        "type": "interval",
        "start": "2024-01-01T00:00:00Z",
        "stop": "2024-01-03T00:00:00Z",
        "step": "P1D",
    }

    # Date Interval - hours
    reader = ArrayMixin(
        input=arr,
        coordinates={
            "time": {
                "type": "interval",
                "start": "2024-01-01T00:00:00Z",
                "stop": "2024-01-01T02:00:00Z",
                "step": "PT1H",
            }
        },
    )
    assert reader.coordinates["time"] == {
        "type": "interval",
        "start": "2024-01-01T00:00:00Z",
        "stop": "2024-01-01T02:00:00Z",
        "step": "PT1H",
    }


@pytest.mark.asyncio
async def test_inverted_axis_async_3d():
    """Test zarr with inverted and lat/lon axis."""
    store = zarr.storage.MemoryStore()

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["lat", "lon"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(0.5, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    arr_sync = zarr.create(
        store=store,
        shape=(200, 3, 100),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("lon", "time", "lat"),
        attributes=attributes,
    )
    # create an array of shape (lon=200, b=3, lat=100)
    arr_sync[:] = numpy.random.rand(200, 3, 200).astype("float32")
    arr_sync[0:, :, 10:15] = -9999.0  # Add some nodata
    arr_sync[10:15, :, 0:] = -9999.0  # Add some nodata

    arr = await zarr.api.asynchronous.open_array(store=store, mode="r")

    reader = AsyncArrayReader(input=arr)
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader.dimensions == ["lon", "time", "lat"]
    assert reader.height == 100
    assert reader.width == 200

    img = await reader._read()
    assert img.array.shape == (3, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert img.band_descriptions == ["time1", "time2", "time3"]

    img = await reader.preview()
    assert img.array.shape == (3, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)


def test_inverted_axis_async_3d_sync():
    """Test zarr with inverted and lat/lon axis."""
    store = zarr.storage.MemoryStore()

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["lat", "lon"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(0.5, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    arr_sync = zarr.create(
        store=store,
        shape=(200, 3, 100),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("lon", "time", "lat"),
        attributes=attributes,
    )
    # create an array of shape (lon=200, b=3, lat=100)
    arr_sync[:] = numpy.random.rand(200, 3, 200).astype("float32")
    arr_sync[0:, :, 10:15] = -9999.0  # Add some nodata
    arr_sync[10:15, :, 0:] = -9999.0  # Add some nodata

    arr = zarr.open_array(store=store, mode="r")

    reader = ArrayReader(input=arr)
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader.dimensions == ["lon", "time", "lat"]
    assert reader.height == 100
    assert reader.width == 200

    img = reader._read()
    assert img.array.shape == (3, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert img.band_descriptions == ["time1", "time2", "time3"]

    img = reader.preview()
    assert img.array.shape == (3, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)


@pytest.mark.asyncio
async def test_inverted_axis_async_2d():
    """Test zarr with inverted and lat/lon axis, shape (x, y) intead of (y, x)."""
    store = zarr.storage.MemoryStore()

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["lat", "lon"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(0.5, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    arr_sync = zarr.create(
        store=store,
        shape=(200, 100),
        chunks=(50, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("lon", "lat"),
        attributes=attributes,
    )
    # create an array of shape (lon=200, lat=100)
    arr_sync[:] = numpy.random.rand(200, 100).astype("float32")
    arr_sync[0:, 10:15] = -9999.0  # Add some nodata
    arr_sync[10:15, 0:] = -9999.0  # Add some nodata

    arr = await zarr.api.asynchronous.open_array(store=store, mode="r")

    reader = AsyncArrayReader(input=arr)
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader.dimensions == ["lon", "lat"]
    assert reader.height == 100
    assert reader.width == 200

    img = await reader._read()
    assert img.array.shape == (1, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert img.band_descriptions == ["b1"]

    img = await reader._read(y_slice=slice(0, 20))
    assert img.array.shape == (1, 20, 200)
    assert img.bounds == (500000.0, 4000080.0, 500100.0, 4000100.0)

    img = await reader.preview()
    assert img.array.shape == (1, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)


def test_inverted_axis_async_2d_sync():
    """Test zarr with inverted and lat/lon axis, shape (x, y) intead of (y, x)."""
    store = zarr.storage.MemoryStore()

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["lat", "lon"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(0.5, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    arr_sync = zarr.create(
        store=store,
        shape=(200, 100),
        chunks=(50, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("lon", "lat"),
        attributes=attributes,
    )
    # create an array of shape (lon=200, lat=100)
    arr_sync[:] = numpy.random.rand(200, 100).astype("float32")
    arr_sync[0:, 10:15] = -9999.0  # Add some nodata
    arr_sync[10:15, 0:] = -9999.0  # Add some nodata

    arr = zarr.open_array(store=store, mode="r")

    reader = ArrayReader(input=arr)
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader.dimensions == ["lon", "lat"]
    assert reader.height == 100
    assert reader.width == 200

    img = reader._read()
    assert img.array.shape == (1, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)

    img = reader._read(y_slice=slice(0, 20))
    assert img.array.shape == (1, 20, 200)
    assert img.bounds == (500000.0, 4000080.0, 500100.0, 4000100.0)

    img = reader.preview()
    assert img.array.shape == (1, 100, 200)
    assert img.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)


###############################################################################
# Selection (sel/sel_method) and N-D arrays
###############################################################################
TIMES = ["2025-01-01T00:00:00Z", "2025-02-01T00:00:00Z", "2025-03-01T00:00:00Z"]
LEVELS = [0, 100, 200, 300]

COORDS_4D = {
    "time": {"type": "inline", "values": TIMES},
    "z": {"type": "interval", "start": 0, "stop": 300, "step": 100},
}


@pytest.mark.parametrize(
    "selector,method,result",
    [
        (15, "nearest", 20.0),
        (15, "pad", 10.0),
        (15, "ffill", 10.0),
        (15, "backfill", 20.0),
        (15, "bfill", 20.0),
        (5, "nearest", 10.0),
        (20, "nearest", 20.0),
        (-5, "nearest", 0.0),
        (100, "nearest", 70.0),
        (20, None, 20.0),
    ],
)
def test_sel_indexer_numeric(selector, method, result):
    """Compare with xarray/pandas."""
    values = numpy.array([0.0, 10.0, 20.0, 50.0, 70.0])
    selected = _sel_indexer(values, selector, method, "z")
    assert values[selected] == result

    # Check compat with xarray results
    da = xarray.DataArray(numpy.zeros(5), dims=("z",), coords={"z": values})
    expected = da.indexes["z"].get_indexer([selector], method=method)[0]
    assert selected == expected


@pytest.mark.parametrize(
    "selector,method,idx",
    [
        ("2025-01-20", "nearest", 1),
        ("2025-01-20T00:00:00Z", "pad", 0),
        ("2025-01-20T00:00:00", "backfill", 1),
        ("2025-02-01", None, 1),
        ("2025-03-01", None, 2),
    ],
)
def test_sel_indexer_datetime(selector, method, idx):
    """Compare with xarray/pandas."""
    values = _get_coordinate_values({"type": "inline", "values": TIMES})
    assert values is not None
    assert values.dtype.kind == "M"
    selected = _sel_indexer(values, selector, method, "time")
    assert selected == idx

    # Check compat with xarray results
    da = xarray.DataArray(numpy.zeros(3), dims=("time",), coords={"time": values})
    ts = pandas.Timestamp(selector)
    if ts.tzinfo is not None:
        ts = ts.tz_convert(None)
    expected = da.indexes["time"].get_indexer([ts], method=method)[0]
    assert selected == expected


def test_sel_indexer():
    """Test list/slice/string selection and errors."""
    values = numpy.array([0.0, 10.0, 20.0, 50.0, 70.0])

    # list keeps the order
    assert _sel_indexer(values, [50, 0]).tolist() == [3, 0]
    assert _sel_indexer(values, [12, 48], "nearest").tolist() == [1, 3]

    # slice (inclusive bounds)
    assert _sel_indexer(values, slice(10, 50)) == slice(1, 4)
    assert _sel_indexer(values, slice(5, None)) == slice(1, 5)
    assert _sel_indexer(values, slice(None, 20)) == slice(0, 3)

    # slice on decreasing coordinates
    assert _sel_indexer(values[::-1], slice(50, 10)) == slice(1, 4)

    # string inputs are cast to the coordinates type
    assert _sel_indexer(values, "20") == 2
    assert _sel_indexer(values, "21", "nearest") == 2

    with pytest.raises(KeyError):
        _sel_indexer(values, 15)

    with pytest.raises(KeyError):
        _sel_indexer(values, -1, "pad")

    with pytest.raises(KeyError):
        _sel_indexer(values, 71, "backfill")

    with pytest.raises(KeyError):
        _sel_indexer(values, slice(80, 90))

    with pytest.raises(ValueError):
        _sel_indexer(values, slice(0, 20, 2))

    with pytest.raises(ValueError):
        _sel_indexer(values, 10, "linear")

    with pytest.raises(ValueError):
        _sel_indexer(numpy.array([0, 20, 10]), slice(0, 10))

    # string coordinates (exact match only)
    values = _get_coordinate_values({"type": "inline", "values": ["b01", "b02"]})
    assert _sel_indexer(values, "b02") == 1
    with pytest.raises(ValueError):
        _sel_indexer(values, "b02", "nearest")


def test_coordinate_values():
    """Test coordinate values and labels."""
    values = _get_coordinate_values(
        {"type": "interval", "start": 0, "stop": 300, "step": 100}
    )
    assert values.tolist() == [0, 100, 200, 300]
    assert _format_coordinate_values(values) == [0, 100, 200, 300]

    values = _get_coordinate_values(
        {"type": "interval", "start": 0.5, "stop": 1.5, "step": 0.5}
    )
    assert values.tolist() == [0.5, 1.0, 1.5]

    values = _get_coordinate_values(
        {
            "type": "interval",
            "start": "2024-01-01T00:00:00Z",
            "stop": "2024-01-03T00:00:00Z",
            "step": "P1D",
        }
    )
    assert values.dtype.kind == "M"
    assert _format_coordinate_values(values) == [
        "2024-01-01T00:00:00Z",
        "2024-01-02T00:00:00Z",
        "2024-01-03T00:00:00Z",
    ]

    values = _get_coordinate_values({"type": "inline", "values": [1, 2, 3]})
    assert values.dtype.kind == "i"

    values = _get_coordinate_values({"type": "inline", "values": ["b01", "b02"]})
    assert values.dtype.kind == "U"

    with pytest.warns(UserWarning):
        assert _get_coordinate_values({"type": "reference"}) is None


@pytest.mark.asyncio
async def test_reader_4d_async(zarr_store_4d):
    """Test N-D reader async."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_4d, mode="r")

    reader = AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
        coordinates=COORDS_4D,
    )
    assert reader.dimensions == ["time", "z", "y", "x"]
    assert reader.non_spatial_dims == ["time", "z"]

    selection = reader._get_non_spatial_selection()
    assert selection["time"] == slice(None)
    assert selection["z"] == slice(None)

    selection = reader._get_non_spatial_selection(
        sel={"time": "2025-01-20"}, sel_method="nearest"
    )
    assert selection["time"] == 1

    selection = reader._get_non_spatial_selection(
        sel={"time": ["2025-01-20"]}, sel_method="nearest"
    )
    assert selection["time"] == [1]

    info = await reader.info(with_coordinates=True)
    assert info.dimensions_count == {
        "time": len(TIMES),
        "z": len(LEVELS),
        "x": 100,
        "y": 100,
    }
    assert info.dimensions == ["time", "z", "y", "x"]
    assert info.coordinates["time"] == TIMES
    assert info.coordinates["z"] == LEVELS
    assert info.model_dump()
    assert info.model_dump_json()

    img = await reader.preview()
    assert img.array.shape == (3, 4, 100, 100)
    assert img.band_names == []
    assert img.band_descriptions == {"time": TIMES, "z": LEVELS}
    assert img.metadata == {}
    assert img.array[2, 3, 0, 0] == 23

    # scalar selection on all dimensions: 3D output (1, h, w)
    img = await reader.preview(sel={"time": "2025-02-01", "z": 200})
    assert img.array.shape == (1, 100, 100)
    assert img.band_names == ["b1"]
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [200]}}
    assert img.array[0, 0, 0] == 12

    # nearest
    img = await reader.preview(sel={"time": "2025-01-20", "z": 120}, sel_method="nearest")
    assert img.array.shape == (1, 100, 100)
    assert img.band_names == ["b1"]
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [100]}}
    assert img.array[0, 0, 0] == 11

    # pad / backfill
    img = await reader.preview(sel={"time": "2025-01-20", "z": 120}, sel_method="pad")
    assert img.metadata == {"selected": {"time": ["2025-01-01T00:00:00Z"], "z": [100]}}

    img = await reader.preview(
        sel={"time": "2025-01-20", "z": 120}, sel_method="backfill"
    )
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [200]}}

    # scalar on one dimension: 3D output with the other dimension as bands
    img = await reader.preview(sel={"time": TIMES[2]})
    assert img.array.shape == (4, 100, 100)
    assert img.band_names == ["b1", "b2", "b3", "b4"]
    assert img.band_descriptions == ["0", "100", "200", "300"]
    assert img.metadata == {
        "selected": {"time": ["2025-03-01T00:00:00Z"], "z": [0, 100, 200, 300]}
    }
    assert img.array[:, 0, 0].tolist() == [20, 21, 22, 23]

    # list selection keeps the order
    img = await reader.preview(sel={"time": [TIMES[2], TIMES[0]]})
    assert img.array.shape == (2, 4, 100, 100)
    assert img.band_descriptions == {"time": [TIMES[2], TIMES[0]], "z": LEVELS}
    assert img.metadata == {
        "selected": {
            "time": ["2025-03-01T00:00:00Z", "2025-01-01T00:00:00Z"],
            "z": [0, 100, 200, 300],
        }
    }
    assert img.array[:, 1, 0, 0].tolist() == [21, 1]

    # slice
    img = await reader.preview(sel={"z": slice(100, 200)})
    assert img.array.shape == (3, 2, 100, 100)
    assert img.band_descriptions == {"time": TIMES, "z": [100, 200]}
    assert img.metadata == {
        "selected": {
            "time": [
                "2025-01-01T00:00:00Z",
                "2025-02-01T00:00:00Z",
                "2025-03-01T00:00:00Z",
            ],
            "z": [100, 200],
        }
    }

    # string values (e.g from query parameters)
    img = await reader.preview(sel={"time": "2025-01-01", "z": "300"})
    assert img.array.shape == (1, 100, 100)
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-01-01T00:00:00Z"], "z": [300]}}
    assert img.array[0, 0, 0] == 3

    # Invalid dimensions
    with pytest.raises(ValueError):
        await reader.preview(sel={"y": 0})

    with pytest.raises(ValueError):
        await reader.preview(sel={"band": 0})

    # Value not found
    with pytest.raises(KeyError):
        await reader.preview(sel={"z": 150})

    # No coordinates: `{dim}{n}` labels
    reader = AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
    )

    img = await reader.preview()
    assert img.array.shape == (3, 4, 100, 100)
    assert img.band_descriptions == {
        "time": ["time1", "time2", "time3"],
        "z": ["z1", "z2", "z3", "z4"],
    }
    assert img.metadata == {}

    img = await reader.preview(sel={"time": 0})
    assert img.array.shape == (4, 100, 100)
    assert img.band_descriptions == ["z1", "z2", "z3", "z4"]
    assert img.metadata == {
        "selected": {"time": ["time1"], "z": ["z1", "z2", "z3", "z4"]}
    }

    img = await reader.preview(sel={"time": 0, "z": 0})
    assert img.array.shape == (1, 100, 100)
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["time1"], "z": ["z1"]}}

    # Coordinates not matching the dimension size: fallback to positions
    reader = AsyncArrayReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
        coordinates={"time": {"type": "inline", "values": TIMES[:2]}},
    )
    with pytest.warns(UserWarning):
        img = await reader.preview()
        assert img.band_descriptions["time"] == ["time1", "time2", "time3"]


def test_reader_4d_sync(zarr_store_4d):
    """Test N-D reader."""
    reader = ArrayReader(
        input=zarr.open_array(store=zarr_store_4d, mode="r"),
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
        coordinates=COORDS_4D,
    )
    assert reader.dimensions == ["time", "z", "y", "x"]
    assert reader.non_spatial_dims == ["time", "z"]

    selection = reader._get_non_spatial_selection()
    assert selection["time"] == slice(None)
    assert selection["z"] == slice(None)

    selection = reader._get_non_spatial_selection(
        sel={"time": "2025-01-20"}, sel_method="nearest"
    )
    assert selection["time"] == 1

    selection = reader._get_non_spatial_selection(
        sel={"time": ["2025-01-20"]}, sel_method="nearest"
    )
    assert selection["time"] == [1]

    info = reader.info(with_coordinates=True)
    assert info.dimensions_count == {
        "time": len(TIMES),
        "z": len(LEVELS),
        "x": 100,
        "y": 100,
    }
    assert info.dimensions == ["time", "z", "y", "x"]
    assert info.coordinates["time"] == TIMES
    assert info.coordinates["z"] == LEVELS
    assert info.model_dump()
    assert info.model_dump_json()

    img = reader.preview()
    assert img.array.shape == (3, 4, 100, 100)
    assert img.band_names == []
    assert img.band_descriptions == {"time": TIMES, "z": LEVELS}
    assert img.metadata == {}
    assert img.array[2, 3, 0, 0] == 23

    # scalar selection on all dimensions: 3D output (1, h, w)
    img = reader.preview(sel={"time": "2025-02-01", "z": 200})
    assert img.array.shape == (1, 100, 100)
    assert img.band_names == ["b1"]
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [200]}}
    assert img.array[0, 0, 0] == 12

    # nearest
    img = reader.preview(sel={"time": "2025-01-20", "z": 120}, sel_method="nearest")
    assert img.array.shape == (1, 100, 100)
    assert img.band_names == ["b1"]
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [100]}}
    assert img.array[0, 0, 0] == 11

    # pad / backfill
    img = reader.preview(sel={"time": "2025-01-20", "z": 120}, sel_method="pad")
    assert img.metadata == {"selected": {"time": ["2025-01-01T00:00:00Z"], "z": [100]}}

    img = reader.preview(sel={"time": "2025-01-20", "z": 120}, sel_method="backfill")
    assert img.metadata == {"selected": {"time": ["2025-02-01T00:00:00Z"], "z": [200]}}

    # scalar on one dimension: 3D output with the other dimension as bands
    img = reader.preview(sel={"time": TIMES[2]})
    assert img.array.shape == (4, 100, 100)
    assert img.band_names == ["b1", "b2", "b3", "b4"]
    assert img.band_descriptions == ["0", "100", "200", "300"]
    assert img.metadata == {
        "selected": {"time": ["2025-03-01T00:00:00Z"], "z": [0, 100, 200, 300]}
    }
    assert img.array[:, 0, 0].tolist() == [20, 21, 22, 23]

    # list selection keeps the order
    img = reader.preview(sel={"time": [TIMES[2], TIMES[0]]})
    assert img.array.shape == (2, 4, 100, 100)
    assert img.band_descriptions == {"time": [TIMES[2], TIMES[0]], "z": LEVELS}
    assert img.metadata == {
        "selected": {
            "time": ["2025-03-01T00:00:00Z", "2025-01-01T00:00:00Z"],
            "z": [0, 100, 200, 300],
        }
    }
    assert img.array[:, 1, 0, 0].tolist() == [21, 1]

    # slice
    img = reader.preview(sel={"z": slice(100, 200)})
    assert img.array.shape == (3, 2, 100, 100)
    assert img.band_descriptions == {"time": TIMES, "z": [100, 200]}
    assert img.metadata == {
        "selected": {
            "time": [
                "2025-01-01T00:00:00Z",
                "2025-02-01T00:00:00Z",
                "2025-03-01T00:00:00Z",
            ],
            "z": [100, 200],
        }
    }

    # string values (e.g from query parameters)
    img = reader.preview(sel={"time": "2025-01-01", "z": "300"})
    assert img.array.shape == (1, 100, 100)
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["2025-01-01T00:00:00Z"], "z": [300]}}
    assert img.array[0, 0, 0] == 3

    # Invalid dimensions
    with pytest.raises(ValueError):
        reader.preview(sel={"y": 0})

    with pytest.raises(ValueError):
        reader.preview(sel={"band": 0})

    # Value not found
    with pytest.raises(KeyError):
        reader.preview(sel={"z": 150})

    # No coordinates: `{dim}{n}` labels
    reader = ArrayReader(
        input=zarr.open_array(store=zarr_store_4d, mode="r"),
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
    )

    img = reader.preview()
    assert img.array.shape == (3, 4, 100, 100)
    assert img.band_descriptions == {
        "time": ["time1", "time2", "time3"],
        "z": ["z1", "z2", "z3", "z4"],
    }
    assert img.metadata == {}

    img = reader.preview(sel={"time": 0})
    assert img.array.shape == (4, 100, 100)
    assert img.band_descriptions == ["z1", "z2", "z3", "z4"]
    assert img.metadata == {
        "selected": {"time": ["time1"], "z": ["z1", "z2", "z3", "z4"]}
    }

    img = reader.preview(sel={"time": 0, "z": 0})
    assert img.array.shape == (1, 100, 100)
    assert img.band_descriptions == ["b1"]
    assert img.metadata == {"selected": {"time": ["time1"], "z": ["z1"]}}

    # Coordinates not matching the dimension size: fallback to positions
    reader = ArrayReader(
        input=zarr.open_array(store=zarr_store_4d, mode="r"),
        crs=CRS.from_epsg(32618),
        transform=Affine.translation(500000, 4000100) @ Affine.scale(1, -1),
        spatial_dims=["y", "x"],
        coordinates={"time": {"type": "inline", "values": TIMES[:2]}},
    )
    with pytest.warns(UserWarning):
        img = reader.preview()
        assert img.band_descriptions["time"] == ["time1", "time2", "time3"]
