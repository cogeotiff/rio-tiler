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

Both are the same scene: Sentinel-2 tile `33TVF`, 2026-09-28, 10980×10980 px at 10 m, EPSG:32633.

| | COG | GeoZarr (EOPF) |
|---|---|---|
| URL | `cogs/S2C_33TVF_20260928_0_L2A_B04.tif` | `geozarrs/S2C_MSIL2A_…_T33TVF_….zarr/measurements/reflectance` |
| Content | one band | **all bands × all resolutions** (81 arrays) |
| dtype | `uint16` | `uint16` on disk, decoded to `float32` reflectance by the `scale_offset` + `cast_value` codecs |
| Compression | DEFLATE + predictor 2 | Blosc (zstd, shuffle) |
| Internal tiling | blocks of **1024×1024** | 1 shard per level, inner chunks of **244×244** (r10m) / 183×183 |
| Pyramid | overviews ×2, ×4, ×8, ×16 (same file) | `r10m` `r20m` `r60m` `r120m` `r360m` `r720m` (sibling groups) |
| Metadata | TIFF header, read the first **32 KB** | consolidated `zarr.json`, **215 KB** |
| Size (B04 full res) | 212 MB file | 150 MB shard (`r10m/b04/c/0/0`) |

Bucket: `https://titiler-benchmark-public.s3.us-east-1.amazonaws.com`

![COG vs GeoZarr structure](img/cog_vs_geozarr/structure.svg#only-light)
![COG vs GeoZarr structure](img/cog_vs_geozarr/structure_dark.svg#only-dark)

!!! tip "Reading this GeoZarr"

    The scale/offset is done by Zarr codecs, not by CF attributes: zarr-python returns
    `float32` reflectance (`DN / 10000 − 0.1`) directly. With zarr-python 3.4, the
    `cast_value` codec needs the optional `cast-value-rs` package.

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
Inner chunks are written in Morton (Z) order, so two chunks side by side on the map
can have other chunks between them in the file: here 7 chunks (580 KB) are downloaded
for the 2 the tile needs (163 KB).

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
| `14/8849/6139` | full res / `r10m` | 1 + 1 | 1,600,142 | 1 + 1 + 1 | 827,412 |
| `12/2212/1534` | full res / `r20m` | 1 + 4 | 1,643,723 | 1 + 1 + 1 | 853,837 |
| `10/553/383` | overview / `r120m` | 1 + 2 | 817,099 | 1 + 1 + 1 | 500,999 |
| `9/276/191` | overview / `r120m` | 1 + 1 | 407,420 | 1 + 1 + 1 | 891,666 |

COG "1 + 4" means the header, then one call with 4 block ranges.

![Bytes per tile](img/cog_vs_geozarr/bytes_per_tile.svg#only-light)
![Bytes per tile](img/cog_vs_geozarr/bytes_per_tile_dark.svg#only-dark)

- COG metadata is 32 KB; Zarr's is 215 KB (it describes 81 arrays, we use 1).
- From z14 to z10, **Zarr downloads about half the bytes of the COG** (0.5–0.9 MB vs
  0.8–1.6 MB): both store `uint16`, but the 244² / 183² inner chunks fit the tile much more
  tightly than 1024² blocks, even with the coalescing over-read.
- At z9 it is the other way around: the COG reads one block of its ×16 overview (407 KB),
  while Zarr reads the whole `r120m` array (676 KB) in one coalesced GET.

---

### Time

10 cold runs per tile (fresh process each time), median, from a laptop over the public
internet to `us-east-1`.

| Tile | COG open | COG tile | **COG total** | Zarr open | Zarr tile | **Zarr total** |
|---|---|---|---|---|---|---|
| z14 | 544 ms | 738 ms | **1281 ms** | 769 ms | 533 ms | **1290 ms** |
| z12 | 572 ms | 874 ms | **1465 ms** | 796 ms | 509 ms | **1291 ms** |
| z10 | 565 ms | 657 ms | **1205 ms** | 786 ms | 391 ms | **1175 ms** |
| z9  | 580 ms | 485 ms | **1066 ms** | 791 ms | 498 ms | **1283 ms** |

![Time per tile](img/cog_vs_geozarr/time_per_tile.svg#only-light)
![Time per tile](img/cog_vs_geozarr/time_per_tile_dark.svg#only-dark)

- **Open** is dominated by the first request (DNS + TLS + cold connection). It costs
  ~560 ms for the COG (32 KB header) and ~790 ms for Zarr (215 KB `zarr.json`).
- **Totals are close**: within 3% at z14 and z10. Zarr is 12% faster at z12 (half the bytes),
  the COG 17% faster at z9 (half the bytes, the other way around).

**Why is Zarr's tile step faster with *more* round trips?**

Zarr's tile step (2 dependent GETs: shard index, then chunks) takes 390–530 ms, the COG's
(1 GET for the blocks) 490–870 ms. From a laptop, bandwidth is part of the cost:

- Zarr downloads about half the bytes from z14 to z10, which pays for its extra round trip.
- A bigger first read also warms the TCP connection: in an earlier run of this benchmark,
  fetching the same 1.4 MB COG range after a 166 KB read instead of a 32 KB one went from
  **562 to 418 ms** (median, 8 runs). Zarr always opens with a bigger read.

➡ These timings should be re-run from compute in `us-east-1` (where RTT is ~10 ms and
bandwidth is not the bottleneck) before drawing conclusions on time.

---

## Profiles (3 Bands)

A true-color tile needs three bands (RGB). As COGs that means **three files**; in the GeoZarr
it is **three arrays of the same store**.

- COG: `rio_tiler.experimental.async_stac.AsyncSTACReader` with a STAC Item listing the
  three files, fetched from the bucket
  ([`cogs/S2C_33TVF_20260928_0_L2A.json`](https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_33TVF_20260928_0_L2A.json), 2.7 KB).
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

item = json.loads(httpx.get("https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_33TVF_20260928_0_L2A.json").content)
async with AsyncSTACReader(input=item, reader=reader) as dst:
    img = await dst.tile(2212, 1534, 12, assets=["B04", "B03", "B02"])

async with AsyncGroupReader(input=group) as src:
    img = await src.tile(2212, 1534, 12, variables=["b04", "b03", "b02"])
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
| `14/8849/6139` | Item + 3 headers + 3 block reads (7 ranges) | 4,716,679 | 7 | 1,991,013 |
| `12/2212/1534` | Item + 3 headers + 3 block reads (16 ranges) | 4,838,992 | 7 | 2,062,192 |
| `10/553/383` | Item + 3 headers + 3 block reads (10 ranges) | 2,393,540 | 7 | 1,032,839 |

![Bytes per 3-band tile](img/cog_vs_geozarr/multiband_bytes.svg#only-light)
![Bytes per 3-band tile](img/cog_vs_geozarr/multiband_bytes_dark.svg#only-dark)

- Metadata: COG = 2.7 KB STAC Item + 3 × 32 KB headers; GeoZarr = one 215 KB `zarr.json` + 3 shard indexes.
- **GeoZarr downloads ~2.3× fewer bytes** (1.0–2.1 MB vs 2.4–4.8 MB). COG bytes are ~3× the
  single-band numbers (z14: 3 × 1.6 MB ≈ 4.7 MB); GeoZarr grows less than 3× because
  `zarr.json` is paid only once (z14: 0.83 MB → 1.99 MB).

### Time

10 cold runs per tile (fresh process each time), median, laptop → `us-east-1`.

| Tile | COG open | COG tile | **COG total** | Zarr open | Zarr tile | **Zarr total** |
|---|---|---|---|---|---|---|
| z14 | 503 ms | 1339 ms | **1854 ms** | 780 ms | 973 ms | **1764 ms** |
| z12 | 502 ms | 1457 ms | **1949 ms** | 786 ms | 986 ms | **1767 ms** |
| z10 | 490 ms | 1182 ms | **1684 ms** | 795 ms | 767 ms | **1566 ms** |

![Time per 3-band tile](img/cog_vs_geozarr/multiband_time.svg#only-light)
![Time per 3-band tile](img/cog_vs_geozarr/multiband_time_dark.svg#only-dark)

- **GeoZarr is 5–9% faster** (1.57–1.77 s vs 1.68–1.95 s), with the same number of round trips.
- COG **opens** faster (2.7 KB STAC Item vs 215 KB `zarr.json`, ~500 vs ~790 ms), but
  its **tile** step is ~370–470 ms slower: it downloads more than twice the bytes, and with
  one store per file each band's first request opens a new HTTPS connection, while the
  three GeoZarr index reads reuse the one store's connections.

---

## Takeaways

| | COG | GeoZarr (sharded) |
|---|---|---|
| metadata request | 32 KB, one file | 215 KB, whole hierarchy |
| dependent round trips | 2 | 3 (index lives in the shard) |
| read granularity | 1024² block | 244² / 183² inner chunk |
| bytes per tile (z14–z10) | 0.8 – 1.6 MB | 0.5 – 0.9 MB |
| multi-band access | 1 file per band | 1 open for all bands |
| 3-band tile round trips | 3 (STAC Item, headers, blocks) | 3 |

- **Round trips**: COG has the block index in its header → 2 trips.
  A sharded Zarr needs to read the shard index first → 3 trips.
  Caching shard indexes (like the header) would bring Zarr down to 2 trips.
- **Bytes**: with the same `uint16` storage, small inner chunks pay off — about half the
  bytes of the COG's 1024² blocks at high zoom, even though coalescing over Morton-ordered
  chunks still downloads chunks the tile doesn't need. At low zoom, a level picked finer
  than the COG's overview can cost more (z9).
- **Metadata**: consolidated `zarr.json` pays off when reading several bands
  or levels from the same store — and costs extra (~230 ms here) for a single-band tile.
- **Several bands**: the round trips don't grow with the number of bands (bands are read
  concurrently): 3 for both, with the STAC Item playing the role of `zarr.json`. COG pays
  one header and one new connection per file; GeoZarr reads `zarr.json` once, reuses the
  store's connections, and downloads less than half the bytes.

---

## Reproduce

- Requests and timings: `uv run python docs/scripts/cog_vs_geozarr/measure.py trace` (every request),
  `uv run python docs/scripts/cog_vs_geozarr/drive.py 10` (10 cold runs per reader and tile)
- Profiles: `uv run pytest tests/profiles/geotiff_profiles.py tests/profiles/zarr_array_profiles.py -s`
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

Versions: zarr-python 3.4.2, cast-value-rs 0.5.1, measured 2026-11-23.
