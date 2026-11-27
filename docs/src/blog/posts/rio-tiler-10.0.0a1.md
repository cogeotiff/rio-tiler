---
date:
  created: 2026-11-27
authors:
  - vincentsarago
categories:
  - Releases
slug: rio-tiler-10-0-0a1
---

# rio-tiler 10.0.0a1: a pre-release

rio-tiler `10.0.0a1` is out. It is the first **pre-release** of rio-tiler 10. The
async-geotiff, zarr-python and async STAC readers leave `experimental`. zarr-python readers now use named
dimensions, `ImageData` supports N-D data, and the readers that don't use GDAL's `WarpedVRT`
now warp in a single pass and pick overviews with GDAL's rule.

<!-- more -->

!!! note

    This post was written with the help of [Claude Code](https://claude.com/claude-code) (Anthropic).

!!! warning "This is a pre-release"

    `10.0.0a1` is an **alpha**. The API can still change before `10.0.0`. Please don't pin it
    in production yet.

    `pip` doesn't install pre-releases by default. To try it, ask for it:

    ```bash
    python -m pip install --pre rio-tiler
    # or
    python -m pip install "rio-tiler==10.0.0a1"
    ```

    Please test it with your code and tell us what breaks, in a
    [GitHub issue](https://github.com/cogeotiff/rio-tiler/issues/new/choose).

---

## Read the migration guide first

rio-tiler 10 has **breaking changes**. The
[v9.0 → v10.0 migration guide](../../migrations/v10_migration.md) lists each one with
"before" and "after" code, and ends with a checklist.

The changes that affect most users:

- Python **>=3.12**, `rasterio>=1.5.1` and `affine>=3.0` are now required. Use `@` instead of
  `*` to multiply `Affine` matrices.
- `ImageData` and `PointData` no longer have `scales`, `offsets` and `count` attributes.
- Mosaic readers no longer copy the first asset's `band_names` and `band_descriptions` to the
  output. The descriptions are in `metadata["band_descriptions"]`.
- The zarr-python readers replace `indexes` with `sel`, and `band_names` with `coordinates`.

If you only use `rio_tiler.io.Reader` or `STACReader` with COGs, the first three points are
probably all you need to check.

The full list is in the [release notes](../../release-notes.md).

---

## New features

### The new readers are no longer experimental

The async-geotiff, zarr-python and async STAC readers moved from `rio_tiler.experimental` to
`rio_tiler.io`:

```python
# before (9.x)
from rio_tiler.experimental.geotiff import Reader
from rio_tiler.experimental.zarr import AsyncGroupReader
from rio_tiler.experimental.async_stac import AsyncSTACReader

# now (10.x)
from rio_tiler.io.geotiff import Reader
from rio_tiler.io.zarr import AsyncGroupReader
from rio_tiler.io import AsyncSTACReader
```

They still need their optional dependencies: `rio-tiler[geotiff]` and `rio-tiler[zarr]`.

See [async-geotiff Reader](../../async-geotiff.md), [GeoZarr Readers](../../geozarr.md) and
[Async-STAC Reader](../../async-stac.md).

### zarr-python readers: named dimensions and `sel`

The zarr-python readers (`ArrayReader`, `AsyncArrayReader`, `GroupReader`, `AsyncGroupReader`) now
work with **named dimensions**, like xarray.

You select non-spatial dimensions with `sel`, by coordinate label (or by position when a
dimension has no coordinates). `method` allows inexact matches (`nearest`, `pad`/`ffill`,
`backfill`/`bfill`):

```python
img = await src.tile(
    x, y, z,
    sel=[{"dimension": "time", "values": "2025-01-15", "method": "nearest"}],
)
print(img.metadata["selected"])
```

Other changes:

- Y/X don't need to be the last two axes anymore. Set them with `spatial_dims`, or let the
  reader read them from the `spatial` zarr-convention.
- Band descriptions come from the coordinates (`coords:coordinates`).
- Group readers stack variables along a new `variables` dimension.
- `list_variables()` returns `selectable_dimensions` for each variable: the values you can pass
  to `sel`.
- Group metadata is cached and shared by all readers. Concurrent calls share one request. You can
  set the cache size and TTL with `RIO_TILER_ZARR_METADATA_CACHE_MAXSIZE` and
  `RIO_TILER_ZARR_METADATA_CACHE_TTL`.
- `AsyncGroupReader` fetches the multiscale levels concurrently.
- `part()` reads only the pixels it needs, not the whole neighbouring chunks.

### N-D `ImageData` and `PointData`

`ImageData` and `PointData` accept arrays of shape `(*leading, height, width)`, with a new
`dimensions` attribute. A Zarr array with `time` and `band` dimensions can now be read in one
call:

```python
img = await src.preview()
print(img.dimensions)
>> ['time', 'band', 'y', 'x']

print(img.band_names)
>> {'time': ['time1', 'time2'], 'band': ['band1', 'band2', 'band3']}
```

Use `reduce()` to get back to 3D data:

```python
import numpy

img = img.reduce("time", numpy.ma.mean)
print(img.dimensions)
>> ['band', 'y', 'x']

img.render(img_format="PNG")
```

Expressions, colormaps, `rescale`, statistics and rendering (except `NPY`/`NPZ`) only work with
3D data. They raise a `ValueError` for N-D data.

`create_from_list()` also has a new `stack_on_dim` option. It stacks images along a new
dimension, instead of concatenating their bands.

For 3D data, nothing changes: `dimensions` is `["b", "y", "x"]` and band names are still
`b1`, `b2`, ...

### Single-pass warping and GDAL's overview rule

The async-geotiff, zarr-python and Xarray readers don't use GDAL's `WarpedVRT`. They read native pixels,
then warp them in memory. In 10.0:

- **Single pass.** `rio_tiler._warp.warp` warps the source pixels directly onto the output
  grid. Before, it reprojected at native resolution and then resized.
- **GDAL's overview rule.** `geotiff.Reader` and the zarr-python group readers pick the overview (or
  multiscale level) the same way GDAL does, instead of the old 50% rule. With `bilinear`,
  `cubic`, ... they now read a finer overview and downsample it, instead of upsampling a coarser
  one. Set the threshold with `RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD`.
- **Non-blocking.** The async readers run warp, reproject and resize in a worker thread, so they
  don't block the event loop. The helper is public: `rio_tiler.utils.run_sync`.

Tiles from these readers are now much closer to tiles from `rio_tiler.io.Reader`.

### A rasterio reader without `WarpedVRT` (experimental)

`rio_tiler.experimental.rasterio.Reader` is a variant of `rio_tiler.io.Reader` that reads
native pixels with rasterio, then warps them with the same code as the async-geotiff reader:

```python
from rio_tiler.experimental.rasterio import Reader

with Reader("cog.tif") as src:
    img = src.tile(21, 12, 6)
```

[Read, then warp](../../experimental/rasterio.md) explains how it works and compares its output
with `rio_tiler.io.Reader`.

### Smaller changes

- `Reader.tile()` emits a `ZoomOutsideNativeRangeWarning` when the zoom is below the dataset
  `minzoom`. These tiles can be slow to create.
- `rio_tiler.reader.read` doesn't read the dataset mask when the mask only comes from the nodata
  value.
- zarr-python Array readers' `tile()` accepts `resampling_method`.
- New `rio_tiler.utils.has_undefined_extent`.

---

## Fixes

- `tile()` raises `TileOutsideBounds`, instead of returning misplaced data, when the tile bounds
  can't be transformed to the dataset CRS (e.g. far outside a UTM zone).
- `ImageData.reproject` masks the output pixels the source doesn't cover.
- `median` and `percentile_*` statistics are correct with `float32` coverage arrays
  ([#1045](https://github.com/cogeotiff/rio-tiler/issues/1045)).
- Warping no longer raises `ZeroDivisionError` when the source contains a pole and the output
  CRS is geographic.

---

## What's next

We will publish more pre-releases until the API is stable, then `10.0.0`. Your feedback decides
what changes before then. Please try `10.0.0a1`, read the
[migration guide](../../migrations/v10_migration.md), and
[open an issue](https://github.com/cogeotiff/rio-tiler/issues/new/choose) if something is wrong
or missing.
