"""Measure tile requests: COG vs GeoZarr, one band (B04) and three bands (B04 + B03 + B02).

- COG, one band: rio_tiler.io.geotiff.Reader (async-geotiff + obstore).
- COG, three bands: rio_tiler.io.stac.AsyncSTACReader on a STAC Item
  (fetched from the bucket), one obstore HTTPStore per file.
- GeoZarr: rio_tiler.io.zarr.AsyncGroupReader on `measurements/reflectance`.

Every request is recorded (start ms, end ms, key, byte ranges).

Usage:
    uv run python docs/scripts/cog_vs_geozarr/measure.py trace        # every request, one run per tile
    uv run python docs/scripts/cog_vs_geozarr/measure.py one cog1 0   # one cold run (see drive.py)

Readers: cog1, zarr1 (B04) / cog3, zarr3 (B04 + B03 + B02).
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

from rio_tiler.io.geotiff import Reader
from rio_tiler.io.stac import AsyncSTACReader
from rio_tiler.io.zarr import AsyncGroupReader

BUCKET = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com"
SCENE = "S2C_33TVF_20260928_0_L2A"
COG = f"{BUCKET}/cogs/{SCENE}_B04.tif"
ITEM = f"{BUCKET}/cogs/{SCENE}.json"
ZARR = f"{BUCKET}/geozarrs/S2C_MSIL2A_20260928T095031_N0513_R079_T33TVF_20260928T130916.zarr/measurements/reflectance"

# Same point (14.45, 41.05), from full resolution to overviews
TILES = [(8849, 6139, 14), (2212, 1534, 12), (553, 383, 10), (276, 191, 9)]
MULTI_TILES = TILES[:3]


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


def split(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    return (
        f"{parsed.scheme}://{parsed.netloc}{posixpath.dirname(parsed.path)}",
        posixpath.basename(parsed.path),
    )


def traced_reader(log, t0):
    """Async-geotiff reader factory: one (traced) HTTPStore per file."""

    @asynccontextmanager
    async def reader(url: str, *args: Any, **kwargs: Any):
        store_url, name = split(url)
        store = TracingStore(HTTPStore.from_url(store_url), log, t0)
        geotiff = await GeoTIFF.open(name, store=store)
        async with Reader(geotiff, *args, **kwargs) as src:
            yield src

    return reader


def cog1_run(tile):
    async def go():
        log: list = []
        t0 = time.perf_counter()
        async with traced_reader(log, t0)(COG) as src:
            t1 = time.perf_counter()
            img = await src.tile(*tile, tilesize=256)
        t2 = time.perf_counter()
        assert img.array.shape[0] == 1, img.array.shape
        return (t1 - t0) * 1000, (t2 - t1) * 1000, log

    return asyncio.run(go())


def cog3_run(tile):
    async def go():
        log: list = []
        t0 = time.perf_counter()
        store_url, name = split(ITEM)
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
        # WrapperStore forwards get_ranges() to the inner store: go through the base
        # coalescer instead, so that each merged GET shows up in get()
        kw = {k: v for k, v in kw.items() if v is not None}
        return zarr.abc.store.Store.get_ranges(
            self, key, byte_ranges, prototype=prototype, **kw
        )


def zarr_run(tile, variables):
    async def go():
        store = TracingZarrStore(ObjectStore(store=HTTPStore(ZARR), read_only=True))
        t0 = time.perf_counter()
        store.t0 = t0
        group = await zarr.api.asynchronous.open_group(
            store=store, mode="r", zarr_format=3, use_consolidated=True
        )
        async with AsyncGroupReader(input=group) as src:
            t1 = time.perf_counter()
            img = await src.tile(*tile, variables=variables, tilesize=256)
        t2 = time.perf_counter()
        assert img.array.shape[0] == len(variables), img.array.shape
        return (t1 - t0) * 1000, (t2 - t1) * 1000, store.log

    return asyncio.run(go())


RUNS = {
    "cog1": cog1_run,
    "cog3": cog3_run,
    "zarr1": lambda tile: zarr_run(tile, ["b04"]),
    "zarr3": lambda tile: zarr_run(tile, ["b04", "b03", "b02"]),
}


def summary(reader, log):
    if reader.startswith("cog"):
        return dict(
            gets=len(log),
            ranges=sum(len(r[3]) for r in log),
            bytes=sum(b for r in log for _, b in r[3]),
        )
    return dict(gets=len(log), ranges=len(log), bytes=sum(r[4] for r in log))


def one(reader, ti):
    """One cold run in this process; prints `RESULT {json}`."""
    o, t, log = RUNS[reader](TILES[int(ti)])
    print("RESULT " + json.dumps(dict(open=o, tile=t, **summary(reader, log))))


if __name__ == "__main__":
    if sys.argv[1] == "one":
        one(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "trace":
        for readers, tiles in (
            (("cog1", "zarr1"), TILES),
            (("cog3", "zarr3"), MULTI_TILES),
        ):
            for tile in tiles:
                print(f"\n===== tile {tile[2]}/{tile[0]}/{tile[1]}")
                for reader in readers:
                    o, t, log = RUNS[reader](tile)
                    print(
                        f"-- {reader} open {o:.0f} ms, tile {t:.0f} ms, {summary(reader, log)}"
                    )
                    for row in log:
                        print("  ", row)
