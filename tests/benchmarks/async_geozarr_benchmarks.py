"""async/sync benchmarks for zarr-python Group Readers."""

import asyncio

import pytest
import zarr
from obstore.store import HTTPStore
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import AsyncGroupReader, GroupReader

src_path = "https://s3.explorer.eopf.copernicus.eu/esa-zarr-sentinel-explorer-fra/tests-output/sentinel-2-l2a/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance"


@pytest.mark.asyncio
async def test_async(async_benchmark):
    """benchmark AsyncGroupReader on a remote GeoZarr."""

    async def _tile():
        store = HTTPStore(src_path)
        zarr_store = ObjectStore(store=store, read_only=True)
        group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")
        async with AsyncGroupReader(input=group) as src:
            img = await src.tile(1736, 1567, 12, variables=["b04"])
            assert img.array.shape == (1, 256, 256)
            return img

    _ = await async_benchmark(_tile)


@pytest.mark.asyncio
async def test_sync(async_benchmark):
    """benchmark Rasterio Reader on a remote GeoTIFF."""

    def sync_tile():
        store = HTTPStore(src_path)
        zarr_store = ObjectStore(store=store, read_only=True)
        group = zarr.open_group(store=zarr_store, mode="r")

        with GroupReader(input=group) as src:
            img = src.tile(1736, 1567, 12, variables=["b04"])
            assert img.array.shape == (1, 256, 256)
            return img

    async def _tile():
        return await asyncio.to_thread(sync_tile)

    _ = await async_benchmark(_tile)
