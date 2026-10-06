"""async/sync benchmarks for GeoTIFF Readers."""

import asyncio

import pytest
import rasterio
from async_geotiff import GeoTIFF
from obstore.store import HTTPStore

from rio_tiler.experimental.geotiff import Reader as AsyncReader
from rio_tiler.io import Reader as SyncReader

src_path = "https://maxar-opendata.s3.amazonaws.com/events/afghanistan-earthquake22/ard/42/120200201121/2022-06-27/10300100D4928800-visual.tif"


@pytest.mark.asyncio
async def test_async_geotiff(async_benchmark):
    """benchmark AsyncGeoTIFF Reader on a remote GeoTIFF."""

    async def _tile():
        store = HTTPStore(
            "https://maxar-opendata.s3.amazonaws.com/events/afghanistan-earthquake22/ard/42/120200201121/2022-06-27"
        )
        geotiff = await GeoTIFF.open("10300100D4928800-visual.tif", store=store)
        async with AsyncReader(input=geotiff) as src:
            return await src.tile(11365, 6592, 14)

    _ = await async_benchmark(_tile)


@pytest.mark.asyncio
async def test_sync_geotiff(async_benchmark):
    """benchmark Rasterio Reader on a remote GeoTIFF."""

    def sync_tile():
        with rasterio.Env(
            GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
            NUM_THREADS="all",
            CPL_VSIL_CURL_NON_CACHED="/vsicurl/https://maxar-opendata.s3.amazonaws.com/events/afghanistan-earthquake22/ard/42/120200201121/2022-06-27/10300100D4928800-visual.tif",
        ):
            with SyncReader(
                "https://maxar-opendata.s3.amazonaws.com/events/afghanistan-earthquake22/ard/42/120200201121/2022-06-27/10300100D4928800-visual.tif"
            ) as src:
                return src.tile(11365, 6592, 14)

    async def _tile():
        return await asyncio.to_thread(sync_tile)

    _ = await async_benchmark(_tile)
