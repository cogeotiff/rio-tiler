"""test rio_tiler.experimental._async.AsyncZarrReader."""

import warnings

import numpy as np
import pytest
import zarr
from affine import Affine
from rasterio.crs import CRS

from rio_tiler.errors import ExpressionMixingWarning, TileOutsideBounds
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


async def test_preview(zarr_store):
    """Test preview method."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

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
    assert img.count == 3

    # Test with explicit height (width derived from aspect ratio)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        img = await reader.preview(height=64)
    assert img.height == 64
    assert img.count == 3

    # Test  with both explicit width and height
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        img = await reader.preview(width=64, height=32)
    assert img.array.shape == (3, 32, 64)

    # Test with band selection.
    img = await reader.preview(indexes=1)
    assert img.count == 1

    img = await reader.preview(indexes=(1, 3))
    assert img.count == 2

    # Test with band expression.
    img = await reader.preview(expression="b1/b2")
    assert img.count == 1

    # Test warns when both expression and indexes are passed
    with pytest.warns(ExpressionMixingWarning):
        img = await reader.preview(indexes=1, expression="b1/b2")
    assert img.count == 1

    # Test reprojects to dst_crs
    img = await reader.preview(dst_crs=CRS.from_epsg(4326))
    assert img.crs == CRS.from_epsg(4326)


async def test_preview_2d(zarr_store_2d):
    """Test preview() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    img = await reader.preview()
    assert img.array.shape == (1, 50, 50)


async def test_statistics(zarr_store):
    """Test statistics() method returns BandStatistics for each band."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

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
    stats = await reader.statistics(nodata=0, indexes=1)
    assert isinstance(stats, dict)
    band_stats = stats["b1"]
    assert band_stats.min == -9999.0

    # Test with band selection
    stats = await reader.statistics(indexes=1)
    assert set(stats.keys()) == {"b1"}

    stats = await reader.statistics(indexes=(1, 3))
    assert set(stats.keys()) == {"b1", "b3"}

    # Test with a band expression
    stats = await reader.statistics(expression="b1/b2")
    assert len(stats) == 1
    assert set(stats.keys()) == {"b1"}
    assert stats["b1"].description == "b1/b2"

    # Test returns requested percentile values
    stats = await reader.statistics(percentiles=[5, 25, 75, 95])
    for band_stats in stats.values():
        extra = band_stats.model_extra or {}
        assert "percentile_5" in extra
        assert "percentile_25" in extra
        assert "percentile_75" in extra
        assert "percentile_95" in extra


async def test_statistics_2d(zarr_store_2d):
    """Test statistics() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    stats = await reader.statistics()
    assert set(stats.keys()) == {"b1"}
    assert stats["b1"].min >= 0.0
    assert stats["b1"].max <= 1.0
