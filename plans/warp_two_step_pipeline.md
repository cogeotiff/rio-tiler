# Plan: Two-Step Warp Pipeline in `rio_tiler._warp`

## TL;DR

Split `_warp.warp()` into two distinct steps — reproject then resample — to match what the sync reader's `WarpedVRT + dataset.read(out_shape=...)` pipeline does internally. This fixes a quality/accuracy difference between the async and sync readers when using non-nearest resampling.

## Background

### Why the results differed

The sync reader (`rio_tiler/reader.py`) uses two separate GDAL operations:

1. **`WarpedVRT(src, resampling=reproject_method)`** — reprojects source data into `dst_crs` at native resolution using the warp kernel (`reproject_method`)
2. **`dataset.read(out_shape=(H, W), resampling=resampling_method)`** — downsamples from native resolution to the requested output size using `resampling_method`

The old `_warp.warp()` did both in a single `rasterio.warp.reproject()` call, using only `reproject_method` for everything. When the output is much smaller than the source (e.g. a 256×256 tile from a large dataset), the one-step approach samples the source sparsely at the output grid, while the two-step approach first creates a full-resolution warped image and then properly averages it down. This produces different (and for averaging kernels, worse) results.

## Implementation

### `rio_tiler/_warp.py`

`warp()` takes `reproject_method` and `resampling_method` and processes the output **tile-by-tile** (`_TILE_SIZE = 128` output pixels per tile) to avoid allocating a large intermediate array.

For each output tile:

**Step 1** — Reproject source → intermediate chunk at native resolution (capped to tile size):
- Map the output tile to an intermediate window via `inter_row/col = round(dst_row * native_height / dst_height)`
- Cap intermediate chunk to `min(native_chunk, tile_size)` — this bounds peak memory and avoids huge allocations when downsampling heavily
- Compute geographic bounds of the intermediate chunk from `output_transform` geometry, then `from_bounds(...)` to get the correct chunk transform
- `rasterio.warp.reproject(..., dst_transform=chunk_transform, resampling=Resampling[reproject_method])`

**Step 2** — Resample intermediate chunk → output tile:
- `resize_array(chunk, tile_h, tile_w, resampling_method)` — skipped when chunk size already equals tile size (heavy downsampling case)

Both data and mask are processed through each step. Mask is carried as `uint8` (255=valid, 0=invalid) through reproject with `resampling=nearest`. Alpha band handled the same way when present.

### `rio_tiler/experimental/geotiff.py`

`part()` — added `resampling_method=resampling_method` to the `warp()` call.

### `rio_tiler/experimental/zarr.py`

`part()` — added `resampling_method=resampling_method` to the `warp()` call.

## Relevant Files

- [rio_tiler/_warp.py](rio_tiler/_warp.py) — core windowed two-step implementation
- [rio_tiler/experimental/geotiff.py](rio_tiler/experimental/geotiff.py) — updated `warp()` call in `part()`
- [rio_tiler/experimental/zarr.py](rio_tiler/experimental/zarr.py) — updated `warp()` call in `part()`

## Status: ✅ Implemented

All changes on `fix/warp-method` branch. No API breaking changes — `resampling_method` defaults to `"nearest"` in `warp()`, matching the previous implicit behavior.
