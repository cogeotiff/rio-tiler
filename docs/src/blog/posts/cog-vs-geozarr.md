---
date: 2026-11-19
authors:
  - vincentsarago
categories:
  - Benchmarks
---

# Anatomy of a tile request: COG vs GeoZarr

What happens on the wire when rio-tiler serves one `256×256` web-map tile
from the same Sentinel-2 band (B04, red), stored as a COG and as a GeoZarr.

<!-- more -->

!!! note

    This post, along with its benchmark scripts and figures, was written with the help of [Claude Code](https://claude.com/claude-code) (Anthropic).


---

## The two datasets

Both are the same scene: Sentinel-2 tile `26SMJ`, 2026-08-10, 10980×10980 px at 10 m, EPSG:32626.

| | COG | GeoZarr (EOPF) |
|---|---|---|
| URL | `cogs/S2C_26SMJ_20260810_0_L2A_B04.tif` | `geozarrs/S2C_MSIL2A_…_T26SMJ_….zarr/measurements/reflectance` |
| Content | one band | **all bands × all resolutions** (87 arrays) |
| dtype | `uint16` | `float32` |
| Compression | DEFLATE + predictor 2 | Blosc (zstd, shuffle) |
| Internal tiling | blocks of **1024×1024** | 1 shard per level, inner chunks of **244×244** (r10m) / 183×183 |
| Pyramid | overviews ×2, ×4, ×8, ×16 (same file) | `r10m` `r20m` `r60m` `r120m` `r360m` `r720m` (sibling groups) |
| Metadata | TIFF header, read the first **32 KB** | consolidated `zarr.json`, **166 KB** |
| Size (B04 full res) | 222 MB file | 374 MB shard (`r10m/b04/c/0/0`) |

Bucket: `https://titiler-benchmark-public.s3.us-east-1.amazonaws.com`

![COG vs GeoZarr structure](img/cog_vs_geozarr/structure.svg#only-light)
![COG vs GeoZarr structure](img/cog_vs_geozarr/structure_dark.svg#only-dark)

---

## A tile request, in two steps

![A tile request in two steps](img/cog_vs_geozarr/tile_request_flow.svg#only-light)
![A tile request in two steps](img/cog_vs_geozarr/tile_request_flow_dark.svg#only-dark)

On object storage the cost is **round trips**, not bytes.
Each round trip that has to wait for the previous one adds a full latency.

---

### COG — ① read the header

One ranged GET for the first 32 KB. The header contains everything:
the image layout (IFDs) **and the byte offset of every block** of every level.

![COG header read](img/cog_vs_geozarr/cog_header.svg#only-light)
![COG header read](img/cog_vs_geozarr/cog_header_dark.svg#only-dark)

After this single request, the reader knows the exact byte range of any block.
No more metadata requests are needed.

---

### COG — ② fetch the blocks

The tile footprint is intersected with the 1024×1024 block grid.
All the needed blocks are fetched **in parallel** — a single round trip.

![COG block fetch](img/cog_vs_geozarr/cog_blocks.svg#only-light)
![COG block fetch](img/cog_vs_geozarr/cog_blocks_dark.svg#only-dark)

Trade-off: big blocks → few requests, but a z14 tile uses only ~3% of the
1024² block it downloads.

---

### GeoZarr — ① read `zarr.json`

The GeoZarr is a hierarchy: one group per resolution, one array per band.
With **consolidated metadata**, the root `zarr.json` already describes all of it.

![GeoZarr hierarchy and zarr.json](img/cog_vs_geozarr/zarr_tree.svg#only-light)
![GeoZarr hierarchy and zarr.json](img/cog_vs_geozarr/zarr_tree_dark.svg#only-dark)

What `zarr.json` tells us: shapes, transforms, chunk grid, codecs.
What it **does not** tell us: where each inner chunk sits inside the shard.

---

### GeoZarr — ② the shard index, then the chunks

A shard is a file with many compressed inner chunks plus an **index at the end**
(`offset, nbytes` per chunk). Reading a chunk is a two-step dance:

![GeoZarr shard index and coalesced chunk read](img/cog_vs_geozarr/zarr_shard.svg#only-light)
![GeoZarr shard index and coalesced chunk read](img/cog_vs_geozarr/zarr_shard_dark.svg#only-dark)

②b is coalesced: zarr-python merges the chunk ranges into one GET when the gap
between them is < 1 MiB — even if that means downloading the chunks in between.

---

### Side by side: the round trips

![Round trips, COG vs GeoZarr](img/cog_vs_geozarr/round_trips.svg#only-light)
![Round trips, COG vs GeoZarr](img/cog_vs_geozarr/round_trips_dark.svg#only-dark)

COG: 2 dependent round trips. GeoZarr (sharded): 3.

---

## Profiles (1 Band)

### Requests and bytes

Async readers (`rio_tiler.experimental.geotiff.Reader` / `rio_tiler.experimental.zarr.AsyncGroupReader`),
one cold store per request, every byte range recorded.

| Tile | Level used (COG / Zarr) | COG GETs | COG bytes | Zarr GETs | Zarr bytes |
|---|---|---|---|---|---|
| `14/6944/6268` | full res / `r10m` | 1 + 1 | 1,519,289 | 1 + 1 + 1 | 1,467,606 |
| `12/1736/1567` | full res / `r20m` | 1 + 2 | 677,661 | 1 + 1 + 1 | 1,895,980 |
| `10/434/391` | overview / `r120m` | 1 + 4 | 864,440 | 1 + 1 + 1 | 1,355,346 |
| `9/217/195` | overview / `r120m` | 1 + 4 | 532,687 | 1 + 1 + 1 | 1,748,580 |

![Bytes per tile](img/cog_vs_geozarr/bytes_per_tile.svg#only-light)
![Bytes per tile](img/cog_vs_geozarr/bytes_per_tile_dark.svg#only-dark)

- COG metadata is 32 KB; Zarr's is 166 KB (it describes 87 arrays, we use 1).
- Zarr over-reads because of coalescing, and because it stores `float32` (vs `uint16`).

---

### Time

10 runs per tile, median, from a laptop over the public internet to `us-east-1`.

| Tile | COG open | COG tile | **COG total** | Zarr open | Zarr tile | **Zarr total** |
|---|---|---|---|---|---|---|
| z14 | 524 ms | 634 ms | **1158 ms** | 636 ms | 275 ms | **926 ms** |
| z12 | 522 ms | 636 ms | **1173 ms** | 662 ms | 282 ms | **978 ms** |
| z10 | 532 ms | 540 ms | **1081 ms** | 666 ms | 277 ms | **998 ms** |
| z9  | 519 ms | 432 ms | **954 ms**  | 712 ms | 294 ms | **1006 ms** |

![Time per tile](img/cog_vs_geozarr/time_per_tile.svg#only-light)
![Time per tile](img/cog_vs_geozarr/time_per_tile_dark.svg#only-dark)

- **Open** is dominated by the first request (DNS + TLS + cold connection): ~500 ms for both.
- Totals are within ~20% of each other. Run-to-run spread on Zarr went up to 1.8 s.


**Why is Zarr's tile step faster with *more* round trips?**

Not explained by the format. What we checked:

- A bigger first read warms the TCP connection: fetching the same 1.4 MB COG
  range after a 166 KB read instead of a 32 KB one: **562 → 418 ms** (median, 8 runs).
  Zarr always opens with 166 KB.
- The rest of the gap is not explained yet. Identical 1.4 MB range GETs varied
  from 140 ms to 600 ms between runs from this machine.

---

## Profiles (3 Bands)

A true-color tile needs three bands (RGB). As COGs that means **three files**; in the GeoZarr
it is **three arrays of the same store**.

- COG: `rio_tiler.experimental.async_stac.AsyncSTACReader` with a STAC Item listing the
  three files, fetched from the bucket
  ([`cogs/S2C_26SMJ_20260810_0_L2A.json`](https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A.json), 2.7 KB).
  Each asset is opened with `async-geotiff` (`rio_tiler.experimental.geotiff.Reader`) and
  its own obstore `HTTPStore`, since in real life the files can live in different buckets.
- GeoZarr: `rio_tiler.experimental.zarr.AsyncGroupReader`.

```python
@asynccontextmanager
async def reader(url: str, *args, **kwargs):
    parsed = urlparse(url)
    store = HTTPStore.from_url(f"{parsed.scheme}://{parsed.netloc}{posixpath.dirname(parsed.path)}")
    geotiff = await GeoTIFF.open(posixpath.basename(parsed.path), store=store)
    async with Reader(geotiff, *args, **kwargs) as src:
        yield src

item = json.loads(httpx.get("https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A.json").content)
async with AsyncSTACReader(input=item, reader=reader) as dst:
    img = await dst.tile(1736, 1567, 12, assets=["B04", "B03", "B02"])

async with AsyncGroupReader(input=group) as src:
    img = await src.tile(1736, 1567, 12, variables=["b04", "b03", "b02"])
```

**Round trips**

![Round trips for a 3-band tile](img/cog_vs_geozarr/multiband_round_trips.svg#only-light)
![Round trips for a 3-band tile](img/cog_vs_geozarr/multiband_round_trips_dark.svg#only-dark)

- **COG**: the STAC Item first (bounds, CRS and zooms come from its `proj:*` fields, so
  the reader doesn't open any file to get them). Then the three bands concurrently: one
  header per file, then the blocks of each file → **3 dependent round trips**.
- **GeoZarr**: `zarr.json` once, then the three shard indexes together, then the three
  chunk reads → **3 dependent round trips**.

Same shape on both sides: the STAC Item plays the role of `zarr.json`, then one metadata
read per band, then one data read per band.

### Requests and bytes

| Tile | COG calls | COG bytes | GeoZarr GETs | GeoZarr bytes |
|---|---|---|---|---|
| `14/6944/6268` | Item + 3 headers + 3 block reads (7 ranges) | 4,579,541 | 7 | 4,053,842 |
| `12/1736/1567` | Item + 3 headers + 3 block reads (10 ranges) | 2,038,332 | 7 | 5,315,058 |
| `10/434/391` | Item + 3 headers + 3 block reads (16 ranges) | 2,606,638 | 7 | 3,701,878 |

![Bytes per 3-band tile](img/cog_vs_geozarr/multiband_bytes.svg#only-light)
![Bytes per 3-band tile](img/cog_vs_geozarr/multiband_bytes_dark.svg#only-dark)

- Metadata: COG = 2.7 KB STAC Item + 3 × 32 KB headers; GeoZarr = one 166 KB `zarr.json` + 3 shard indexes.
- COG bytes are ~3× the single-band numbers (z14: 3 × 1.52 MB ≈ 4.58 MB).
  GeoZarr grows less than 3× because `zarr.json` is paid only once (z14: 1.47 MB → 4.05 MB).

### Time

10 cold runs per tile (fresh process each time), median, laptop → `us-east-1`.

| Tile | COG open | COG tile | **COG total** | Zarr open | Zarr tile | **Zarr total** |
|---|---|---|---|---|---|---|
| z14 | 500 ms | 1258 ms | **1778 ms** | 687 ms | 1150 ms | **1849 ms** |
| z12 | 496 ms | 1214 ms | **1718 ms** | 689 ms | 1120 ms | **1814 ms** |
| z10 | 490 ms | 1155 ms | **1650 ms** | 695 ms | 983 ms | **1702 ms** |

![Time per 3-band tile](img/cog_vs_geozarr/multiband_time.svg#only-light)
![Time per 3-band tile](img/cog_vs_geozarr/multiband_time_dark.svg#only-dark)

- **COG and GeoZarr are within ~3–5%** (1.65–1.78 s vs 1.70–1.85 s): same number of
  round trips.
- COG **opens** faster (2.7 KB STAC Item vs 166 KB `zarr.json`, ~500 vs ~690 ms), but
  its **tile** step is ~100–170 ms slower: with one store per file, each band's first
  request opens a new HTTPS connection, while the three GeoZarr index reads reuse the
  one store's connections.

---

## Takeaways

| | COG | GeoZarr (sharded) |
|---|---|---|
| metadata request | 32 KB, one file | 166 KB, whole hierarchy |
| dependent round trips | 2 | 3 (index lives in the shard) |
| read granularity | 1024² block | 244² / 183² inner chunk |
| bytes per tile | 0.5 – 1.5 MB | 1.4 – 1.9 MB |
| multi-band access | 1 file per band | 1 open for all bands |
| 3-band tile round trips | 3 (STAC Item, headers, blocks) | 3 |

- **Round trips**: COG has the block index in its header → 2 trips.
  A sharded Zarr needs to read the shard index first → 3 trips.
  Caching shard indexes (like the header) would bring Zarr down to 2 trips.
- **Bytes**: smaller inner chunks *should* mean fewer bytes, but coalescing
  (1 MiB gap) and `float32` storage cancel that out here.
- **Metadata**: consolidated `zarr.json` pays off when reading several bands
  or levels from the same store — and costs extra for a single-band tile.
- **Several bands**: the round trips don't grow with the number of bands (bands are read
  concurrently): 3 for both, with the STAC Item playing the role of `zarr.json`. COG pays
  one header and one new connection per file; GeoZarr reads `zarr.json` once and reuses
  the store's connections.

---

## Reproduce

- Benchmarks: `tests/benchmarks/async_cog_benchmarks.py`, `tests/benchmarks/async_geozarr_benchmarks.py`
- Request assertions: `tests/benchmarks/requests.py`, `tests/benchmarks/geozarr_requests.py`
- Profiles: `uv run pytest tests/profiles/geotiff_profiles.py tests/profiles/zarr_array_profiles.py -s`
- Multi-band: `uv run python docs/scripts/cog_vs_geozarr/multiband_measure.py trace` (requests),
  `uv run python docs/scripts/cog_vs_geozarr/multiband_drive.py 10` (timings)
- Figures: `python3 docs/scripts/cog_vs_geozarr/make_figures.py`

Recording byte ranges (the trick used for the numbers above):

```python
# COG: wrap the obstore store given to async_geotiff.GeoTIFF.open
class TracingStore:
    def __init__(self, store): self.store, self.log = store, []
    async def get_range_async(self, path, *, start, end=None, length=None):
        r = await self.store.get_range_async(path, start=start, end=end, length=length)
        self.log.append((start, len(r))); return r
    async def get_ranges_async(self, path, *, starts, ends=None, lengths=None):
        r = await self.store.get_ranges_async(path, starts=starts, ends=ends, lengths=lengths)
        self.log += [(s, len(b)) for s, b in zip(starts, r)]; return r

# Zarr: WrapperStore forwards get_ranges() straight to the inner store,
# so route it through the base coalescer to see each merged GET in get()
class TracingZarrStore(zarr.storage.WrapperStore):
    log = []
    async def get(self, key, prototype, byte_range=None):
        r = await self._store.get(key, prototype, byte_range)
        self.log.append((key, byte_range, len(r) if r else 0)); return r
    def get_ranges(self, key, byte_ranges, *, prototype, **kw):
        kw = {k: v for k, v in kw.items() if v is not None}
        return zarr.abc.store.Store.get_ranges(self, key, byte_ranges, prototype=prototype, **kw)
```
