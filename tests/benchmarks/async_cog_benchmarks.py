"""async/sync benchmarks for GeoTIFF Readers."""

import asyncio

import pytest
import rasterio
from async_geotiff import GeoTIFF
from obstore.store import HTTPStore

from rio_tiler.experimental.geotiff import Reader as AsyncReader
from rio_tiler.io import Reader as SyncReader

src_path = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A_B04.tif"


@pytest.mark.asyncio
async def test_async_geotiff(async_benchmark):
    """benchmark AsyncGeoTIFF Reader on a remote GeoTIFF."""

    async def _tile():
        store = HTTPStore(
            "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs"
        )
        geotiff = await GeoTIFF.open("S2C_26SMJ_20260810_0_L2A_B04.tif", store=store)
        async with AsyncReader(input=geotiff) as src:
            return await src.tile(1736, 1567, 12)

    _ = await async_benchmark(_tile)


@pytest.mark.asyncio
async def test_sync_geotiff(async_benchmark):
    """benchmark Rasterio Reader on a remote GeoTIFF."""

    def sync_tile():
        with rasterio.Env(
            GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
            NUM_THREADS="all",
            CPL_VSIL_CURL_NON_CACHED="/vsicurl/https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A_B04.tif",
        ):
            with SyncReader(
                "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A_B04.tif"
            ) as src:
                return src.tile(1736, 1567, 12)

    async def _tile():
        return await asyncio.to_thread(sync_tile)

    _ = await async_benchmark(_tile)
