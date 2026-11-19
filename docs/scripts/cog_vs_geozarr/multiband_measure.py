"""Measure a 3-band tile: COG (STAC Item, 3 files) vs GeoZarr (1 store, 3 variables).

COG: rio_tiler.experimental.async_stac.AsyncSTACReader + async-geotiff, one obstore
HTTPStore per file. GeoZarr: rio_tiler.experimental.zarr.AsyncGroupReader.

Usage:
    python multiband_measure.py trace          # every request, one run per tile
    python multiband_measure.py one cog 0      # one cold run (used by multiband_drive.py)
"""

import asyncio
import json
import posixpath
import sys
import time
from contextlib import asynccontextmanager
from typing import Any
from urllib.parse import urlparse

import obstore
import zarr
import zarr.abc.store
from async_geotiff import GeoTIFF
from obstore.store import HTTPStore
from zarr.storage import ObjectStore, WrapperStore

from rio_tiler.experimental.async_stac import AsyncSTACReader
from rio_tiler.experimental.geotiff import Reader
from rio_tiler.experimental.zarr import AsyncGroupReader

BUCKET = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com"
ZARR = f"{BUCKET}/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance"
ITEM = f"{BUCKET}/cogs/S2C_26SMJ_20260810_0_L2A.json"
TILES = [(6944, 6268, 14), (1736, 1567, 12), (434, 391, 10)]


# ---------------- COG: trace every range request made by async-geotiff ----------------
class TracingStore:
    """Record every call: (start ms, end ms, path, [(offset, bytes), ...])."""

    def __init__(self, store, log, t0):
        self.store, self.log, self.t0 = store, log, t0

    async def get_range_async(self, path, *, start, end=None, length=None):
        s = time.perf_counter()
        r = await self.store.get_range_async(path, start=start, end=end, length=length)
        self.log.append(
            (
                round((s - self.t0) * 1000),
                round((time.perf_counter() - self.t0) * 1000),
                path,
                [(start, len(r))],
            )
        )
        return r

    async def get_ranges_async(self, path, *, starts, ends=None, lengths=None):
        s = time.perf_counter()
        r = await self.store.get_ranges_async(
            path, starts=starts, ends=ends, lengths=lengths
        )
        self.log.append(
            (
                round((s - self.t0) * 1000),
                round((time.perf_counter() - self.t0) * 1000),
                path,
                [(a, len(b)) for a, b in zip(starts, r)],
            )
        )
        return r


def traced_reader(log, t0):
    """Async-geotiff reader factory: one (traced) HTTPStore per file."""

    @asynccontextmanager
    async def reader(url: str, *args: Any, **kwargs: Any):
        parsed = urlparse(url)
        store_url = f"{parsed.scheme}://{parsed.netloc}{posixpath.dirname(parsed.path)}"
        store = TracingStore(HTTPStore.from_url(store_url), log, t0)
        geotiff = await GeoTIFF.open(posixpath.basename(parsed.path), store=store)
        async with Reader(geotiff, *args, **kwargs) as src:
            yield src

    return reader


def cog_run(tile):
    async def go():
        log: list = []
        t0 = time.perf_counter()
        # fetch the STAC Item (its own store, like any asset could be elsewhere)
        store_url, name = ITEM.rsplit("/", 1)
        resp = await obstore.get_async(HTTPStore.from_url(store_url), name)
        body = await resp.bytes_async()
        log.append((0, round((time.perf_counter() - t0) * 1000), name, [(0, len(body))]))
        item = json.loads(bytes(body))
        async with AsyncSTACReader(input=item, reader=traced_reader(log, t0)) as dst:
            t1 = time.perf_counter()
            img = await dst.tile(*tile, assets=["B04", "B03", "B02"], tilesize=256)
        t2 = time.perf_counter()
        assert img.array.shape[0] == 3, img.array.shape
        return (t1 - t0) * 1000, (t2 - t1) * 1000, log

    return asyncio.run(go())


def n_ranges(log):
    return sum(len(r[3]) for r in log)


def n_bytes(log):
    return sum(b for r in log for _, b in r[3])


# ---------------- Zarr: trace every GET ----------------
class TracingZarrStore(WrapperStore):
    def __init__(self, store):
        super().__init__(store)
        self.log = []
        self.t0 = time.perf_counter()

    async def get(self, key, prototype, byte_range=None):
        s = time.perf_counter()
        r = await self._store.get(key, prototype, byte_range)
        self.log.append(
            (
                round((s - self.t0) * 1000),
                round((time.perf_counter() - self.t0) * 1000),
                key,
                byte_range,
                len(r) if r else 0,
            )
        )
        return r

    def get_ranges(self, key, byte_ranges, *, prototype, **kw):
        kw = {k: v for k, v in kw.items() if v is not None}
        return zarr.abc.store.Store.get_ranges(
            self, key, byte_ranges, prototype=prototype, **kw
        )


def zarr_run(tile):
    async def go():
        store = TracingZarrStore(ObjectStore(store=HTTPStore(ZARR), read_only=True))
        t0 = time.perf_counter()
        group = await zarr.api.asynchronous.open_group(
            store=store, mode="r", zarr_format=3, use_consolidated=True
        )
        async with AsyncGroupReader(input=group) as src:
            t1 = time.perf_counter()
            img = await src.tile(*tile, variables=["b04", "b03", "b02"], tilesize=256)
        t2 = time.perf_counter()
        assert img.array.shape[0] == 3, img.array.shape
        return (t1 - t0) * 1000, (t2 - t1) * 1000, store.log

    return asyncio.run(go())


# ---------------- entry points ----------------
def one(reader, ti):
    """One cold run in this process; prints `RESULT {json}`."""
    tile = TILES[int(ti)]
    if reader == "cog":
        o, t, log = cog_run(tile)
        out = dict(
            open=o, tile=t, gets=len(log), ranges=n_ranges(log), bytes=n_bytes(log)
        )
    else:
        o, t, log = zarr_run(tile)
        out = dict(
            open=o, tile=t, gets=len(log), ranges=len(log), bytes=sum(r[4] for r in log)
        )
    print("RESULT " + json.dumps(out))


if __name__ == "__main__":
    if sys.argv[1] == "one":
        one(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "trace":
        for tile in TILES:
            print(f"\n===== tile {tile[2]}/{tile[0]}/{tile[1]}")
            o, t, log = cog_run(tile)
            print(
                f"-- COG open {o:.0f} ms, tile {t:.0f} ms, "
                f"calls {len(log)}, ranges {n_ranges(log)}, bytes {n_bytes(log):,}"
            )
            for row in log:
                print("  ", row)
            o, t, log = zarr_run(tile)
            print(
                f"-- GeoZarr open {o:.0f} ms, tile {t:.0f} ms, GETs {len(log)}, bytes {sum(r[4] for r in log):,}"
            )
            for row in log:
                print("  ", row)
