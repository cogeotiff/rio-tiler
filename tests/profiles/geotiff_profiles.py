"""Profiles for GeoTIFF Readers (rasterio and async-geotiff).

Run with:

    uv run pytest tests/profiles/geotiff_profiles.py -s

=== rasterio Reader.tile ===
store calls: {'open: ': 1, 'tile: ': 1}
2.541 test_sync_rasterio_reader  tests/profiles/geotiff_profiles.py:119
├─ 1.810 Reader.__init__  <attrs generated methods rio_tiler.io.rasterio.Reader>:32
│  └─ 1.810 Reader.__attrs_post_init__  rio_tiler/io/rasterio.py:95
│     └─ 1.809 wrapper  rasterio/env.py:443
│           [54 frames hidden]  rasterio, botocore, urllib3, http, so...
│              0.659 _SSLSocket.read  <built-in>
│              0.819 open  rasterio/__init__.py:100
└─ 0.730 Reader.tile  rio_tiler/io/rasterio.py:264
   └─ 0.716 Reader.part  rio_tiler/io/rasterio.py:322
      └─ 0.716 part  rio_tiler/reader.py:331
         └─ 0.714 read  rio_tiler/reader.py:71

=== async-geotiff Reader.tile ===
store calls: {'open: get_range_async': 1, 'tile: get_ranges_async': 1}
1.260 _UnixSelectorEventLoop._run_once  asyncio/base_events.py:1966
└─ 1.259 Handle._run  asyncio/events.py:92
   ├─ 0.631 CountingStore.get_ranges_async  tests/profiles/geotiff_profiles.py:88
   │  └─ 0.631 HTTPStore.get_ranges_async  obstore/store.py:254
   │     └─ 0.631 [await]  obstore/store.py
   ├─ 0.580 CountingStore.get_range_async  tests/profiles/geotiff_profiles.py:83
   │  └─ 0.580 HTTPStore.get_range_async  obstore/store.py:212
   │     └─ 0.580 [await]  obstore/store.py
   └─ 0.048 test_async_geotiff_reader  tests/profiles/geotiff_profiles.py:142
      └─ 0.043 Reader.tile  rio_tiler/io/geotiff.py:212
         └─ 0.042 Reader.part  rio_tiler/io/geotiff.py:256
            ├─ 0.016 Reader._read  rio_tiler/io/geotiff.py:630
            │  └─ 0.015 GeoTIFF.read  async_geotiff/_read.py:34
            │        [3 frames hidden]  async_geotiff
            └─ 0.015 run_sync  rio_tiler/utils.py:966
               └─ 0.015 to_thread  asyncio/threads.py:12
                  └─ 0.015 [await]  asyncio/threads.py

"""

import logging
from collections import Counter

import pytest
import rasterio
from async_geotiff import GeoTIFF
from obstore.store import HTTPStore
from pyinstrument import Profiler

from rio_tiler.io import Reader
from rio_tiler.io.geotiff import Reader as AsyncGeoTIFFReader

base_url = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs"
filename = "S2C_33TVF_20260928_0_L2A_B04.tif"
src_path = f"{base_url}/{filename}"

# zoom 14 is close to the native 10m resolution
tile = (8849, 6139, 14)

gdal_env = {
    "GDAL_HTTP_MERGE_CONSECUTIVE_RANGES": "YES",
    "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
    "GDAL_INGESTED_BYTES_AT_OPEN": 32768,
    "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif",
    "CPL_VSIL_CURL_NON_CACHED": f"/vsicurl/{src_path}",
    "CPL_DEBUG": "ON",
    "CPL_CURL_VERBOSE": "YES",
    "GDAL_NUM_THREADS": "1",
}


class CountingStore:
    """Obspec store wrapper counting the calls made by async-geotiff."""

    def __init__(self, store: HTTPStore):
        """Init."""
        self.store = store
        self.counter: Counter = Counter()
        self.ranges: Counter = Counter()
        self.phase = "open"

    async def get_range_async(self, path, *, start, end=None, length=None):
        """Count and forward `get_range_async` calls."""
        self.counter[f"{self.phase}: get_range_async"] += 1
        return await self.store.get_range_async(path, start=start, end=end, length=length)

    async def get_ranges_async(self, path, *, starts, ends=None, lengths=None):
        """Count and forward `get_ranges_async` calls."""
        self.counter[f"{self.phase}: get_ranges_async"] += 1
        self.ranges[f"{self.phase}: get_ranges_async"] += len(starts)
        return await self.store.get_ranges_async(
            path, starts=starts, ends=ends, lengths=lengths
        )


class GDALRequestCounter(logging.Handler):
    """Logging handler counting the HTTP requests made by GDAL (from CPL_DEBUG)."""

    def __init__(self):
        """Init."""
        super().__init__(level=logging.DEBUG)
        self.counter: Counter = Counter()
        self.phase = "open"

    def emit(self, record: logging.LogRecord):
        """Count VSICURL download messages."""
        msg = record.getMessage()
        if "VSICURL" in msg and "Downloading" in msg:
            self.counter[f"{self.phase}: "] += 1


def _print_profile(title: str, profiler: Profiler, counter: Counter):
    print(f"\n=== {title} ===")
    print(f"store calls: {dict(counter)}")
    print(profiler.output_text(unicode=True, color=False, short_mode=True))


def test_sync_rasterio_reader():
    """profile rasterio Reader on a remote COG."""
    handler = GDALRequestCounter()
    logger = logging.getLogger("rasterio")
    previous_level = logger.level
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    try:
        profiler = Profiler()
        with profiler:
            with rasterio.Env(**gdal_env):
                with Reader(src_path) as src:
                    handler.phase = "tile"
                    img = src.tile(*tile)
    finally:
        logger.removeHandler(handler)
        logger.setLevel(previous_level)

    assert img.array.shape == (1, 256, 256)
    _print_profile("rasterio Reader.tile", profiler, handler.counter)


@pytest.mark.asyncio
async def test_async_geotiff_reader():
    """profile async-geotiff Reader on a remote COG."""
    store = CountingStore(HTTPStore.from_url(base_url))

    profiler = Profiler(async_mode="enabled")
    with profiler:
        geotiff = await GeoTIFF.open(filename, store=store)
        store.phase = "tile"
        async with AsyncGeoTIFFReader(geotiff) as src:
            img = await src.tile(*tile)

    assert img.array.shape == (1, 256, 256)
    _print_profile("async-geotiff Reader.tile", profiler, store.counter)
