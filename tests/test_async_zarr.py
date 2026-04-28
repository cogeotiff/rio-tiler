"""test rio_tiler.experimental.zarr.Reader."""

import os
import shutil
import warnings

import numpy
import obstore
import pytest
import xarray
import zarr
from affine import Affine
from rasterio.crs import CRS
from rasterio.transform import from_bounds
from zarr.storage import ObjectStore

from rio_tiler.errors import (
    ExpressionMixingWarning,
    InvalidBounds,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.experimental.zarr import Reader as AsyncZarrReader
from rio_tiler.io.xarray import XarrayReader

from .utils import create_zarr

pytestmark = pytest.mark.asyncio


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
    assert reader._dims == ["band", "y", "x"]

    # Test _read (full array)
    img = await reader._read()
    assert img.array.shape == (3, 100, 100)
    assert img.band_names == ["b1", "b2", "b3"]
    assert img.band_descriptions == ["b1", "b2", "b3"]

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

    # Test info method
    info = await reader.info()
    assert info.bounds == (500000.0, 4000000.0, 500100.0, 4000100.0)
    assert info.driver == "Zarr-Python"
    assert info.count == 3
    assert info.model_dump()


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
    assert reader._dims == ["y", "x"]

    img = await reader._read()
    assert img.array.shape == (1, 50, 50), f"Expected (1, 50, 50), got {img.array.shape}"

    # Test info method
    info = await reader.info()
    assert info.bounds == (500000.0, 4000000.0, 500050.0, 4000050.0)
    assert info.driver == "Zarr-Python"
    assert info.count == 1
    assert info.model_dump()


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
    assert img.band_names == ["b1"]
    assert img.band_descriptions == ["b1"]

    assert img.array.shape[0] == 1

    # Read bands 1 and 3
    img = await reader.part(
        bbox=(500010, 4000010, 500050, 4000050),
        bounds_crs=CRS.from_epsg(32618),
        indexes=(1, 3),
    )
    assert img.band_names == ["b1", "b3"]
    assert img.band_descriptions == ["b1", "b3"]

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

    with pytest.raises(InvalidBounds):
        bounds = reader.tms.xy_bounds(1000, 1000, 10)
        await reader.part(bounds, bounds_crs=reader.tms.rasterio_crs)


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


async def test_point(zarr_store):
    """Test point() method reads a single pixel value."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store, mode="r")

    transform = Affine.translation(500000, 4000100) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    # Read point in dataset CRS (UTM 18N)
    # Pick a point in the middle of the dataset
    pt = await reader.point(
        lon=500050.0,
        lat=4000050.0,
        coord_crs=CRS.from_epsg(32618),
    )

    assert pt.count == 3
    assert pt.crs == CRS.from_epsg(32618)
    assert pt.coordinates == (500050.0, 4000050.0)
    assert pt.band_names == ["b1", "b2", "b3"]

    # Test method with band selection
    # Read only band 1
    pt = await reader.point(
        lon=500050.0,
        lat=4000050.0,
        coord_crs=CRS.from_epsg(32618),
        indexes=1,
    )
    assert pt.count == 1
    assert pt.band_names == ["b1"]

    # Read bands 1 and 3
    pt = await reader.point(
        lon=500050.0,
        lat=4000050.0,
        coord_crs=CRS.from_epsg(32618),
        indexes=(1, 3),
    )
    assert pt.count == 2
    assert pt.band_names == ["b1", "b3"]

    # Test raises error for points outside bounds.
    # Point outside dataset bounds
    with pytest.raises(PointOutsideBounds):
        await reader.point(
            lon=600000.0,
            lat=5000000.0,
            coord_crs=CRS.from_epsg(32618),
        )


async def test_point_2d(zarr_store_2d):
    """Test point() with a 2D (single-band) array."""
    arr = await zarr.api.asynchronous.open_array(store=zarr_store_2d, mode="r")

    transform = Affine.translation(500000, 4000050) * Affine.scale(1, -1)
    reader = AsyncZarrReader(
        input=arr,
        crs=CRS.from_epsg(32618),
        transform=transform,
    )

    pt = await reader.point(
        lon=500025.0,
        lat=4000025.0,
        coord_crs=CRS.from_epsg(32618),
    )

    assert pt.data.shape == (1,)  # Single band
    assert pt.band_names == ["b1"]


async def test_band_descriptions(zarr_dataset):
    """Test XarrayReader and AsyncZarrReader compatibility."""
    store = obstore.store.from_url(f"file://{zarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
    array = await group.getitem("dataset")

    # Get Time coordinates from the zarr store
    time = await group.getitem("time")
    time_arrray = await time.getitem(slice(None))

    zarrds = AsyncZarrReader(
        input=array,
        crs=CRS.from_epsg(4326),
        transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        band_names=[str(d) for d in time_arrray.tolist()],
    )
    assert zarrds.band_descriptions == ["2022-01-01", "2022-01-02"]

    img = await zarrds.preview(indexes=1)
    assert img.band_descriptions == ["2022-01-01"]

    img = await zarrds.preview(indexes=2)
    assert img.band_descriptions == ["2022-01-02"]

    img = await zarrds.preview(expression="b1/b2")
    assert img.band_descriptions == ["2022-01-01/2022-01-02"]


async def test_geozarr(geozarr_dataset):
    """Test XarrayReader and AsyncZarrReader compatibility."""
    store = obstore.store.from_url(f"file://{geozarr_dataset}")
    zarr_store = ObjectStore(store=store, read_only=True)

    group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
    array = await group.getitem("dataset")

    # Get Time coordinates from the zarr store
    time = await group.getitem("time")
    time_arrray = await time.getitem(slice(None))

    zarrds = AsyncZarrReader(
        input=array,
        band_names=[str(d) for d in time_arrray.tolist()],
    )
    assert zarrds.crs == CRS.from_epsg(4326)
    assert zarrds.bounds == (-180.0, -90.0, 180.0, 90.0)

    img = await zarrds.preview(indexes=1)
    assert img.crs == CRS.from_epsg(4326)
    assert img.bounds == (-180.0, -90.0, 180.0, 90.0)


async def test_compat_xarray(zarr_dataset):
    """Test XarrayReader and AsyncZarrReader compatibility."""
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

    zarrds = AsyncZarrReader(
        input=array,
        crs=CRS.from_epsg(4326),
        # Ref: https://github.com/cogeotiff/rio-tiler/issues/905
        # Use the same transform as xarray to ensure the same bounds and pixel alignment
        # transform=Affine.translation(-180, 90) * Affine.scale(0.1, -0.1),
        transform=transform,
    )

    # Statistics
    stats = xarrayds.statistics(nodata=0)
    zarr_stats = await zarrds.statistics()

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
    zarr_img = await zarrds.preview()
    assert img.array.shape == zarr_img.array.shape
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    # Tile
    img = xarrayds.tile(0, 0, 0)
    assert img.count == 2
    assert img.width == 256
    assert img.height == 256
    assert img.array.dtype == numpy.float32

    zarr_img = await zarrds.tile(0, 0, 0)
    assert zarr_img.count == 2
    assert zarr_img.width == 256
    assert zarr_img.height == 256
    assert zarr_img.array.dtype == numpy.float32

    assert zarr_img.bounds == img.bounds
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    zoom = 10
    x, y = zarrds.tms.xy(-179, -80)
    tile = zarrds.tms._tile(x, y, zoom)
    img = xarrayds.tile(tile.x, tile.y, zoom)
    zarr_img = await zarrds.tile(tile.x, tile.y, zoom)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Part
    img = xarrayds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert img.crs == "epsg:4326"
    assert img.array.shape == (2, 1600, 3200)

    zarr_img = await zarrds.part((-160, -80, 160, 80), bounds_crs="epsg:4326")
    assert zarr_img.crs == "epsg:4326"
    assert zarr_img.array.shape == (2, 1600, 3200)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    img = xarrayds.part((-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 88, 100)

    zarr_img = await zarrds.part((-160, -80, 160, 80), dst_crs="epsg:3857", max_size=100)
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

    zarr_img = await zarrds.part((-160, -80, 160, 80), dst_crs="epsg:3857")
    assert zarr_img.crs == "epsg:3857"
    assert zarr_img.array.shape == (2, 2352, 2696)
    # numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)

    # Point
    pt = xarrayds.point(0, 0)
    assert pt.count == 2
    assert pt.coordinates
    assert pt.pixel_location
    assert pt.array.dtype == numpy.float32

    zarr_pt = await zarrds.point(0, 0)
    assert zarr_pt.count == 2
    assert zarr_pt.coordinates
    assert zarr_pt.pixel_location
    assert zarr_pt.array.dtype == numpy.float32
    numpy.testing.assert_array_equal(pt.array, zarr_pt.array)

    ## Masked
    pt = xarrayds.point(-179, 89, nodata=0)
    zarr_pt = await zarrds.point(-179, 89)
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

    zarr_img = await zarrds.feature(feat)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 1222, 3055)
    numpy.testing.assert_array_equal(img.array, zarr_img.array)

    img = xarrayds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert img.crs == "epsg:3857"
    assert img.array.shape == (2, 56, 100)

    zarr_img = await zarrds.feature(feat, dst_crs="epsg:3857", max_size=100)
    assert zarr_img.array.dtype == numpy.float32
    assert zarr_img.array.shape == (2, 56, 100)
    numpy.testing.assert_allclose(img.array, zarr_img.array, rtol=0.5)
