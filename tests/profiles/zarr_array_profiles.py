"""Profiles for zarr-python Array Readers.

Run with:

    uv run pytest tests/profiles/zarr_array_profiles.py -s

- `test_sync_array_reader` / `test_async_array_reader`: pyinstrument call tree
  and store calls for one tile.
- `test_async_event_loop_lag`: event loop lag while tiles are read concurrently.
- `test_async_slow_callbacks`: steps blocking the event loop for more than 5ms
  (asyncio debug mode).

Note: zarr fetches chunks in tasks it spawns, so in the async pyinstrument tree
the I/O time appears next to `AsyncArrayReader.tile` (under `Handle._run`), while
the reader's own CPU work (warp, ...) appears under it.

Note: zarr's sync API runs I/O and decoding in a background thread that
pyinstrument doesn't sample. Use py-spy to see all threads, including native
(GDAL, codecs) frames:

    sudo py-spy record --threads --native --idle -f speedscope -o zarr.json -- \
        uv run pytest tests/profiles/zarr_array_profiles.py -s -k sync
"""

import asyncio
import logging
import re
import time
from typing import cast

import pytest
import zarr
from affine import Affine
from obstore.store import HTTPStore
from pyinstrument import Profiler
from rasterio.crs import CRS
from zarr.storage import LoggingStore, ObjectStore

from rio_tiler.experimental.zarr import ArrayReader, AsyncArrayReader

src_path = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance"
array_path = "r10m/b04"

# Spatial metadata is stored on the `r10m` group, not on the arrays
array_options = {
    "crs": CRS.from_epsg(32626),
    "transform": Affine(10.0, 0.0, 399965.0, 0.0, -10.0, 4400035.0),
    "spatial_dims": ["y", "x"],
}

# zoom 14 is close to the native 10m resolution
tile = (6944, 6268, 14)

# 4x4 zoom 14 tiles
tiles = [(x, y, 14) for x in range(6944, 6948) for y in range(6268, 6272)]


def _store() -> LoggingStore:
    """Remote store counting the calls made by zarr."""
    return LoggingStore(
        ObjectStore(store=HTTPStore(src_path), read_only=True),
        log_level="WARNING",
        log_handler=logging.NullHandler(),
    )


def _print_profile(title: str, profiler: Profiler, store: LoggingStore):
    print(f"\n=== {title} ===")
    print(f"store calls: {dict(store.counter)}")
    print(profiler.output_text(unicode=True, color=False))


def test_sync_array_reader():
    """profile ArrayReader on a remote zarr Array."""
    store = _store()

    profiler = Profiler()
    with profiler:
        group = zarr.open_group(store=store, mode="r")
        array = cast(zarr.Array, group[array_path])
        with ArrayReader(input=array, **array_options) as src:
            img = src.tile(*tile)

    assert img.array.shape == (1, 256, 256)
    _print_profile("ArrayReader.tile", profiler, store)


@pytest.mark.asyncio
async def test_async_array_reader():
    """profile AsyncArrayReader on a remote zarr Array."""
    store = _store()

    profiler = Profiler(async_mode="enabled")
    with profiler:
        group = await zarr.api.asynchronous.open_group(store=store, mode="r")
        array = cast(zarr.AsyncArray, await group.getitem(array_path))
        async with AsyncArrayReader(input=array, **array_options) as src:
            img = await src.tile(*tile)

    assert img.array.shape == (1, 256, 256)
    _print_profile("AsyncArrayReader.tile", profiler, store)


@pytest.mark.asyncio
async def test_async_event_loop_lag():
    """measure event loop lag while AsyncArrayReader reads tiles concurrently."""
    store = _store()
    loop = asyncio.get_running_loop()

    interval = 0.005
    lags: list[float] = []
    done = asyncio.Event()

    async def _probe():
        while not done.is_set():
            start = loop.time()
            await asyncio.sleep(interval)
            lags.append(loop.time() - start - interval)

    group = await zarr.api.asynchronous.open_group(store=store, mode="r")
    array = cast(zarr.AsyncArray, await group.getitem(array_path))
    async with AsyncArrayReader(input=array, **array_options) as src:
        probe = asyncio.create_task(_probe())
        start = time.perf_counter()
        imgs = await asyncio.gather(*(src.tile(*t) for t in tiles))
        elapsed = time.perf_counter() - start
        done.set()
        await probe

    assert all(img.array.shape == (1, 256, 256) for img in imgs)

    lags.sort()
    print(f"\n=== AsyncArrayReader.tile x {len(tiles)} (concurrent) ===")
    print(f"store calls: {dict(store.counter)}")
    print(f"total: {elapsed * 1000:.1f} ms")
    print(
        f"event loop lag: max {lags[-1] * 1000:.1f} ms, "
        f"p99 {lags[int(len(lags) * 0.99)] * 1000:.1f} ms, "
        f"median {lags[len(lags) // 2] * 1000:.1f} ms"
    )


@pytest.mark.asyncio
async def test_async_slow_callbacks(caplog):
    """list the steps blocking the event loop for more than 5ms."""
    store = _store()
    loop = asyncio.get_running_loop()

    caplog.set_level(logging.WARNING, logger="asyncio")
    loop.set_debug(True)
    loop.slow_callback_duration = 0.005
    try:
        group = await zarr.api.asynchronous.open_group(store=store, mode="r")
        array = cast(zarr.AsyncArray, await group.getitem(array_path))
        async with AsyncArrayReader(input=array, **array_options) as src:
            imgs = await asyncio.gather(*(src.tile(*t) for t in tiles))
    finally:
        loop.set_debug(False)

    assert all(img.array.shape == (1, 256, 256) for img in imgs)

    # e.g "Executing <Task ... coro=<AsyncArrayReader.tile() ...> took 0.008 seconds"
    slow = [
        f"{m.group(1)}: {float(m.group(2)) * 1000:.1f} ms"
        for r in caplog.records
        if r.name == "asyncio"
        and (m := re.search(r"coro=<(\S+?)\(\).* took ([\d.]+) seconds", r.getMessage()))
    ]
    print(f"\n=== AsyncArrayReader.tile x {len(tiles)}: blocking steps > 5ms ===")
    print("\n".join(slow) or "none")
