"""test rio_tiler.experimental._async.AsyncZarrReader."""

import numpy as np
import pytest
import zarr
from affine import Affine
from rasterio.crs import CRS

from rio_tiler.errors import TileOutsideBounds
from rio_tiler.experimental._async import AsyncZarrReader

pytestmark = pytest.mark.asyncio


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
    arr_sync[:] = np.random.rand(3, 100, 100).astype("float32")
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
    arr_sync[:] = np.random.rand(50, 50).astype("float32")
    arr_sync[10:20, 10:20] = -9999.0  # Add some nodata

    return store


async def test_async_zarr_reader(zarr_store):
    """Test AsyncZarrReader with a 3D array (bands, height, width)."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    # Create reader with geospatial metadata
    # Use a proper north-up transform (pixel 0,0 at top-left)
    # Bounds in UTM: 500000, 4000000 to 500100, 4000100 (100x100m area, 1m pixels)
    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert reader._dims == ["band"]

    # Test _read (full array)
    img = await reader._read()
    assert img.array.shape == (3, 100, 100)

    # Test _read with window
    img = await reader._read(row_slice=slice(10, 30), col_slice=slice(10, 30))
    assert img.array.shape == (3, 20, 20)

    # Test part (bbox read) - read a 40x40 pixel subset
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
    )
    assert img.array.shape == (3, 40, 40)

    # Test tile method
    img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256)
    assert img.array.shape[0] == 3


async def test_2d_array(zarr_store_2d):
    """Test with a 2D array (single band)."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )
    assert reader.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
    assert reader._dims == []

    img = await reader._read()
    assert img.array.shape == (1, 50, 50), f"Expected (1, 50, 50), got {img.array.shape}"


async def test_part_same_crs(zarr_store):
    """Test part() method with same CRS as dataset."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )
    assert reader.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)

    # Read a 40x40 pixel subset
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050), bounds_crs=CRS.from_epsg(32618)
    )

    assert img.array.shape == (3, 40, 40)
    assert img.bounds == (500010, 4000010, 500050, 4000050)
    assert img.crs == CRS.from_epsg(32618)


async def test_part_with_explicit_size(zarr_store):
    """Test part() method with explicit width/height."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Read with explicit output size
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050),
        bounds_crs=CRS.from_epsg(32618),
        width=128,
        height=128,
    )

    assert img.array.shape == (3, 128, 128)
    assert img.bounds == (500010, 4000010, 500050, 4000050)


async def test_part_with_max_size(zarr_store):
    """Test part() method with max_size constraint."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Read with max_size constraint
    img = await reader.part(
        bbox=(500000, 4000000, 500100, 4000100),
        bounds_crs=CRS.from_epsg(32618),
        max_size=50,
    )

    # Should be constrained to max 50 pixels on longest side
    assert max(img.array.shape[1], img.array.shape[2]) == 50


async def test_part_with_indexes(zarr_store):
    """Test part() method with band selection."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Read only band 1
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050),
        bounds_crs=CRS.from_epsg(32618),
        indexes=1,
    )

    assert img.array.shape[0] == 1

    # Read bands 1 and 3
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050),
        bounds_crs=CRS.from_epsg(32618),
        indexes=(1, 3),
    )

    assert img.array.shape[0] == 2


async def test_tile(zarr_store):
    """Test tile() method."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Default tile size from TMS
    img = await reader.tile(tile_x=0, tile_y=0, tile_z=0)
    assert img.array.shape[0] == 3  # 3 bands


async def test_tile_custom_size(zarr_store):
    """Test tile() method with custom tilesize."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Custom tile size
    img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=512)
    assert img.array.shape == (3, 512, 512)


async def test_tile_with_indexes(zarr_store):
    """Test tile() method with band selection."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Read only band 2
    img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256, indexes=2)
    assert img.array.shape[0] == 1

    img = await reader.tile(tile_x=0, tile_y=0, tile_z=0, tilesize=256, indexes=(1, 2))
    assert img.array.shape[0] == 2


async def test_tile_outside_bounds(zarr_store):
    """Test tile() raises error for tiles outside bounds."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Tile that doesn't intersect the dataset
    with pytest.raises(TileOutsideBounds):
        await reader.tile(tile_x=1000, tile_y=1000, tile_z=10)
