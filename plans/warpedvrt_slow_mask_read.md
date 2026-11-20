# Slow tiles from reprojected COGs: masks and single-band reads skip GDAL's output-size warp

> Note: this plan was written by Claude Code under the supervision of vincentsarago.

Refs: https://github.com/cogeotiff/rio-tiler/issues/1066, PR https://github.com/cogeotiff/rio-tiler/pull/1067

Tested with GDAL 3.12.1 (rasterio 1.5.0) and GDAL 3.13.3 (CLI), rio-tiler `main` (f0197bf).

## In short

A zoomed-out tile from a large COG that needs reprojection can take **7–19 s of CPU**,
when the actual pixel data takes **0.02 s**.

1. To make a tile, rio-tiler builds a `WarpedVRT` at the source's **native** resolution
   (for z3 that VRT is 406644×406644) and asks for a 256×256 downsampled read.
2. GDAL has an **output-size warp** for that (`VRTWarpedDataset::IRasterIO`): it warps directly
   at 256×256 from a suitable source overview. This only works when **all bands are read
   at once** (and the whole VRT is read). This is the **fast path**: "fast" means only about
   one tile's worth of pixels gets warped, so it costs milliseconds of CPU.
3. Any read that is **not all bands at once** goes to GDAL's slow **block-by-block warp**. It warps from the
   VRT's coarsest overview (25443×25443 here, still about 100× bigger than the tile). That's the
   seconds of CPU.
4. Reading **masks** is always per band, so a mask read always takes the block-by-block warp.
5. rio-tiler asks rasterio for masks (`masked=True, fill_value=nodata`). With either option
   set, rasterio reads the masks per band (`_io.pyx:573`). Then rio-tiler throws that mask away and
   rebuilds it from `data == nodata` (`rio_tiler/reader.py` ~L246-251).

```
           rio-tiler: vrt.read(out_shape=(3, 256, 256), ...)
                                  │
              WarpedVRT 406644×406644 (native resolution)
                                  │
            ┌─────────────────────┴─────────────────────┐
            │                                           │
  all bands, whole VRT                        single band or mask
  (VRTWarpedDataset::IRasterIO)               (per-band read)
            │                                           │
            ▼                                           ▼
  ┌──────────────────────────┐          ┌─────────────────────────────┐
  │ OUTPUT-SIZE WARP         │          │ BLOCK-BY-BLOCK WARP         │
  │ pick the source COG      │          │ pick the VRT's coarsest     │
  │ overview (686×686)       │          │ overview (25443×25443)      │
  │ warp straight to 256×256 │          │ warp it block by block      │
  │                          │          │ then downsample to 256×256  │
  └──────────────────────────┘          └─────────────────────────────┘
            │                                           │
            ▼                                           ▼
       ~0.02 s CPU                             ~2.4 s CPU per band

  Pixels warped:  256×256 (output-size)  vs  25443×25443 (block-by-block)  →  ~10 000× more
```

So the cost of the block-by-block warp is GDAL's, and rio-tiler triggers it for nothing.

Note: TCI.tif has no mask band. The mask comes from GDAL's implicit nodata mask
(`MaskFlags.nodata`), which is still computed through the warped band.

## Reproduce with GDAL only

The `GDAL_VRT_WARP_USE_DATASET_RASTERIO=NO` option turns off the output-size warp, which shows the cost
of the path used by mask and single-band reads.

```bash
SRC=/vsicurl/https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/54/S/UE/2023/1/S2B_54SUE_20230102_0_L2A/TCI.tif

# Warped VRT for WebMercator tile z3/x7/y3 at native resolution
# (same extent/resolution as rio-tiler's get_vrt_transform)
gdalwarp -q -overwrite -of VRT -t_srs EPSG:3857 \
  -te 15028131.257091936 0.0 20037508.342789244 5009377.085697312 \
  -tr 12.318826997809651 12.318826997809662 \
  -srcnodata 0 -dstnodata 0 \
  "$SRC" warp.vrt

gdalinfo warp.vrt | grep -E "Size is|Overviews" | head -2
# Size is 406644, 406644
#   Overviews: 203322x203322, 101661x101661, 50849x50849, 25443x25443

# Fast path = output-size warp (default): ~0.13 s user CPU
time gdal_translate -q -of MEM -outsize 256 256 warp.vrt /dev/null

# Block-by-block warp (output-size warp disabled): ~6.6 s user CPU
time gdal_translate -q -of MEM -outsize 256 256 \
  --config GDAL_VRT_WARP_USE_DATASET_RASTERIO NO warp.vrt /dev/null
```

Look at `user` time, because `real` includes network latency.

`gdal_translate -b 1` / `-b mask,1` did **not** reliably reproduce the slow single-band read
(it was fast in later runs), so it is not used here.

## Reproduce with rio-tiler / rasterio

### 1. The slow tile

```python
import time
from rio_tiler.io import Reader

url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/54/S/UE/2023/1/S2B_54SUE_20230102_0_L2A/TCI.tif"

with Reader(url) as src:  # EPSG:32654, nodata=0
    for z, x, y in [(2, 3, 1), (3, 7, 3)]:
        t = time.process_time()
        src.tile(x, y, z)
        print(f"z{z}: {time.process_time() - t:.2f}s CPU")
# z2: ~18.6s CPU
# z3: ~7.4s CPU
```

### 2. What makes it slow: mask reads, single-band reads, and the output-size warp

```python
import time

import morecantile
import rasterio
from rasterio.vrt import WarpedVRT

from rio_tiler.utils import get_vrt_transform

url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/54/S/UE/2023/1/S2B_54SUE_20230102_0_L2A/TCI.tif"
bounds = morecantile.tms.get("WebMercatorQuad").xy_bounds(7, 3, 3)


def timeit(label, func):
    t = time.process_time()
    func()
    print(f"{label:45s} {time.process_time() - t:.2f}s CPU")


with rasterio.open(url) as ds:
    tr, w, h = get_vrt_transform(ds, bounds, 256, 256, dst_crs="EPSG:3857")
    params = dict(
        crs="EPSG:3857", transform=tr, width=w, height=h,
        nodata=0, src_nodata=0, add_alpha=False,
    )

    cases = [
        ("read [1,2,3]", dict(indexes=[1, 2, 3], out_shape=(3, 256, 256))),
        ("read [1,2,3] fill_value=0", dict(indexes=[1, 2, 3], out_shape=(3, 256, 256), fill_value=0)),
        ("read [1,2,3] masked=True", dict(indexes=[1, 2, 3], out_shape=(3, 256, 256), masked=True)),
        ("read [1]", dict(indexes=[1], out_shape=(1, 256, 256))),
    ]
    for label, kwargs in cases:
        with WarpedVRT(ds, **params) as vrt:  # new VRT each time, no cache reuse
            timeit(label, lambda: vrt.read(**kwargs))

    with rasterio.Env(GDAL_VRT_WARP_USE_DATASET_RASTERIO="NO"):
        with WarpedVRT(ds, **params) as vrt:
            timeit("read [1,2,3] (output-size warp disabled)",
                   lambda: vrt.read(indexes=[1, 2, 3], out_shape=(3, 256, 256)))

# read [1,2,3]                                  ~0.02s CPU   <- output-size warp
# read [1,2,3] fill_value=0                     ~7.3s  CPU   <- rasterio also reads masks
# read [1,2,3] masked=True                      ~7.5s  CPU   <- same
# read [1]                                      ~2.5s  CPU   <- single band = block-by-block warp
# read [1,2,3] (output-size warp disabled)      ~7.2s  CPU   <- 3 x single band
```

The `[1,2,3]` read takes 0.02 s, and every read that misses the output-size warp costs about 2.4 s
**per band**.

## Why the VRT is at native resolution

`part()` sizes the WarpedVRT with `get_vrt_transform` (`rio_tiler/utils.py` ~L466-478), which only
uses the output `width`/`height` when **over-zooming** (output resolution finer than the dataset's).
When zooming out it keeps the dataset's native resolution, reprojected (`dst_transform.a/e`).
The history:

1. Originally the VRT was built with the output size (e.g. 256×256 for a tile).
2. PR #648 (fix for #647) removed `width`/`height`. With the VRT already at output size,
   `read(out_shape=...)` had nothing to resize, so `resampling_method` had no effect.
   The PR explicitly wanted to keep "fetching the overviews".
3. PR #701 added `width`/`height` back, but only for over-zooming.

#648 does keep overviews working, but only for GDAL's all-bands output-size warp. Mask and single-band
reads fall back to block-by-block warping of a VRT ~1600× wider than the tile (z3), which is
where the time goes.

## Fixes

### In rio-tiler (PR #1067): don't ask for a mask we throw away

When nodata is set, matches the dataset's nodata, and every requested band's mask flags are just
`[MaskFlags.nodata]`, read with `masked=False` and no `fill_value` (keep `fill_value`
for boundless reads, where rasterio reads masks only if `masked=True`), then build the mask from
the data. Output is identical, and z2 goes from ~18.6 s to ~0.03 s.

The guard matters: on the non-reprojected path, a user nodata that differs from the file's
nodata currently also masks the file's own nodata pixels (they're filled with the user value).
Skipping the mask read without the guard would change that.

Both `masked` **and** `fill_value` must be dropped. Dropping only `masked=True` gives no speedup.

### Not covered by #1067: requests for a subset of bands

`indexes=1`, or an expression that uses only `b1`, on a multi-band COG with reprojection
is still slow **far below the dataset `minzoom`** (z3 on TCI: ~2.5 s per band). Inside the native
zoom range the warped VRT's own overviews keep it cheap (z7 on TCI, `indexes=[1]`: ~0.03 s).
Options:

- rio-tiler: read all bands from the VRT and select in numpy. Only worth it when the read is
  downsampled (VRT larger than the output) and the band count is small or the data is
  pixel-interleaved. It's a bad trade for many-band, band-interleaved data (e.g. hyperspectral).
- rio-tiler: cap the VRT size when downsampling. Tested and rejected (see below).
- GDAL (better): let single-band and mask reads use the same output-size warp
  (`frmts/vrt/vrtwarped.cpp`, `VRTWarpedDataset::IRasterIO`, the `nBandCount < nBands`
  fallback), or give the warped VRT overviews coarser than the source's coarsest one.

### Rejected: don't build the VRT at native resolution when downsampling

The idea was to size the VRT in `get_vrt_transform` smaller than the native resolution when
zooming out, so the block-by-block warp (masks, single band, alpha, boundless) only has a small
VRT to fill. Two variants were prototyped by patching `get_vrt_transform` (TCI, z3/z7/z9/z11,
all bands, `nearest`/`bilinear`/`average`):

- **overview-sized**: VRT at the resolution of the coarsest source overview whose factor is
  ≤ the requested downsampling (what GDAL would pick).
- **overview-sized, capped**: same, but never more than 4× the output size per axis.

Results:

| zoom | overview GDAL picks | VRT today | VRT overview-sized | mean / max \|diff\| vs today (0–255) |
|---|---|---|---|---|
| z3 | 16× | 406644 | 25415 (capped: 1024) | 0 (capped: 10.7 / 53) |
| z7 | 16× | 25415 | 1588 (capped: 1024) | 12.6 / 187 |
| z9 | 16× | 6354 | 397 | 21.8 / 228 |
| z11 | 4× | 1588 | 397 | 13.2 / 201 |

Why it was rejected:

- **The output gets worse, not just slightly different.** Today's tile looks like the source
  overview, reprojected: the output-size warp reads the source overviews, which were built with
  averaging. A WarpedVRT's full-resolution level is always filled from the source's
  **full-resolution** data, never from its overviews (only the VRT's own internal overviews
  map to source overviews). So a VRT sized "at the 16× overview resolution" is filled by
  nearest-sampling 10 m pixels, and the tile comes out grainy and aliased. This holds for every
  `resampling_method`, `nearest` included.
- **Sizing at the overview resolution alone doesn't speed anything up.** At z3 the
  overview-sized VRT (25415) is the same size as the VRT overview the block-by-block warp
  already uses today. Only the cap makes it smaller, and the cap is where the quality loss is.
- **The slow case is now narrow.** With #1067, all-bands reads take the output-size warp and
  are fast at every zoom (0.01–0.04 s). Single-band reads are fast inside the native zoom range.
  Only single-band or mask reads far below `minzoom` stay slow.

### Done instead (added to PR #1067): warn below `minzoom`

`Reader.tile()` emits a `ZoomOutsideNativeRangeWarning` (`rio_tiler/errors.py`) when the tile
zoom is below the dataset `minzoom`: the output is resampled beyond the coarsest overview and
the read can be slow. The pixels returned don't change. Over-zoom (`> maxzoom`) doesn't warn,
because tile servers do it routinely.

### Separate issue to open: `resampling_method` is ignored on all-bands reprojected reads

While prototyping, all-bands reprojected reads gave **identical** output for `nearest`,
`bilinear` and `average` when downsampling (z7, z9), today and with a smaller VRT. GDAL's
output-size warp goes straight to the output size and only applies the warp kernel
(`reproject_method`), so the `read(out_shape=...)` resampling never runs. Single-band reads
do honour `resampling_method` (mean |diff| nearest vs bilinear: 2.5 at z7, 4.7 at z9). This is
#647 again, now coming from GDAL rather than from rio-tiler.
