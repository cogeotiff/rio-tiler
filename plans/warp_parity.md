# PR #1083: warp parity with `rio_tiler.io.Reader`

PR: https://github.com/cogeotiff/rio-tiler/pull/1083 (branch `fix/experimental-warp`)

> This PR was made by Claude Code under the supervision of vincentsarago. This document is a guide for reviewers; the PR description has the full changelog.

This PR makes the experimental readers return the same pixels as `rio_tiler.io.Reader`. Three changes do that: the warp runs in a single pass, overviews are chosen with GDAL's rule, and each band keeps its own nodata during the warp.

## At a glance

| Area | Change |
| --- | --- |
| Warp | `_warp.warp` warps the source pixels straight onto the output grid instead of reprojecting at native resolution and then resizing. |
| Overviews | Overview selection follows GDAL's `GDALBandGetBestOverviewLevel2` instead of the aiocogeo 50% rule. |
| Nodata | A pixel that is nodata in one band no longer becomes nodata in every band. |

The experimental readers affected are `experimental.geotiff.Reader`, the `experimental.zarr` group readers and `experimental.xarray`. All of them call the shared helpers in `rio_tiler/_warp.py`. `rio_tiler.io.Reader` is unchanged and serves as the reference.

## 1. Single-pass warp

Before, `warp()` resampled twice: it reprojected at the dataset's native resolution, then resized to the output shape. GDAL's `WarpedVRT`, which the sync reader uses, warps the selected overview directly onto the requested grid in one pass.

```
Before:  read overview → reproject at native res → resize to output
After:   read overview → warp onto output grid
```

- The kernel matches the sync reader: `reproject_method` when the CRS changes (WarpedVRT), `resampling_method` when it doesn't (RasterIO).
- `gauss` is not supported by GDAL's warper, so it keeps the two-step path.
- The output is still processed in 2048 px chunks to bound memory.

## 2. GDAL overview selection

The readers used the aiocogeo 50% rule. When the output resolution fell between two overviews, that rule could pick the coarser one and upsample it. The new `get_overview_level()` uses GDAL's rule: pick the most downsampled overview whose factor is below

```
desired_factor × threshold + 0.1
threshold = 1.2 for nearest, 1.0 for other methods
```

- With `bilinear` or `cubic`, an overview coarser than the output is never used. A finer one is read and downsampled, as GDAL does.
- The threshold can be set with the new `RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD` environment variable (`constants.OVERVIEW_OVERSAMPLING_THRESHOLD`). If it's unset, GDAL's `GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD` is used when defined, so both readers keep picking the same overview.
- The new `get_downsampling_factor()` computes the requested factor the way the sync reader does. For a reprojection, that's the WarpedVRT size at dataset resolution in the output CRS, divided by the output size.
- Zarr group readers apply the same rule to multiscale levels, using each level's resolution. GeoZarr levels don't have to be powers of 2 or share an extent.

## 3. Per-band nodata in the warp

When `rasterio.warp.reproject` gets a masked array, it merges the band masks into a single validity band, `~np.logical_or.reduce(source.mask)`. A pixel then counts as invalid if *any* band is masked, and comes out as nodata in all bands. rio-tiler treats a pixel as valid if *any* band is valid (`ImageData._mask`), and so does GDAL's WarpedVRT.

On a Sentinel-2 true-color COG with `nodata=0`, sea pixels whose red value is exactly 0 lost their real green and blue values. On a z14 tile, 6,577 pixels (about 10%) were blanked in all three bands.

The fix in `warp()`:

1. Before warping, mask only the pixels where all bands are masked, so partly valid pixels keep their values.
2. After warping, mask each band again where its value equals `img.nodata` (NaN-aware). This is the same thing `rio_tiler.reader.read` does.

```python
src_mask = numpy.logical_and.reduce(numpy.ma.getmaskarray(src_array), axis=0)
src_array = numpy.ma.MaskedArray(
    src_array.data,
    mask=numpy.broadcast_to(src_mask, src_array.shape),
)
...
if img.nodata is not None:
    out_mask |= numpy.isnan(dst_data) if numpy.isnan(img.nodata) else dst_data == img.nodata
```

With bilinear or cubic, a pixel that is nodata in only some bands now counts as valid in every band, so band 1's zeros can be blended into neighbouring values. GDAL's WarpedVRT does the same: see the parity table below.

## Measurements

### Overview rule and single-pass warp

Async-geotiff reader vs `rio_tiler.io.Reader`, on every `tests/fixtures/cog.tif` tile from minzoom to maxzoom. Cells give the share of identical values as median / worst tile.

| zoom | tiles | nearest main | nearest PR | bilinear main | bilinear PR | cubic main | cubic PR | mask mismatch main | mask mismatch PR |
| ---: | ----: | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 5 | 4 | 91.3% / 87.2% | 100% / 100% | 68.4% / 56.6% | 100% / 100% | 56.4% / 44.7% | 100% / 100% | 67 | 0 |
| 6 | 6 | 93.8% / 87.7% | 100% / 100% | 82.0% / 60.9% | 100% / 100% | 74.0% / 47.9% | 100% / 100% | 135 | 1 |
| 7 | 16 | 97.5% / 88.9% | 100% / 100% | 90.7% / 57.9% | 100% / 100% | 85.5% / 37.3% | 100% / 100% | 170 | 1 |
| 8 | 49 | 98.4% / 82.3% | 100% / 100% | 92.7% / 46.2% | 100% / 100% | 87.3% / 23.6% | 100% / 100% | 127 | 0 |
| 9 | 170 | 99.3% / 87.5% | 100% / 100% | 97.7% / 52.6% | 100% / 100% | 95.5% / 25.6% | 100% / 100% | 147 | 1 |

For bilinear and cubic, the readers now read a finer overview and downsample it. Compared with the earlier rasterio-based experimental reader, that meant 1.34× more native pixels read, the same amount `rio_tiler.io.Reader` reads.

### Per-band nodata

Async-geotiff reader vs `rio_tiler.io.Reader`, 3-band Sentinel-2 TCI COG (`nodata=0`), nearest, tiles over the Gulf of Salerno. The figures count pixels that differ between the two readers.

| tile | before: render mask | after: render mask | after: per-band mask | after: data |
| --- | ---: | ---: | ---: | ---: |
| `12/2212/1541` | 0 | 0 | 0 | 0 |
| `13/4425/3083` | 6,673 (10.2%) | 0 | 0 | 0 |
| `14/8850/6166` | 6,577 (10.0%) | 0 | 0 | 0 |
| `16/35400/24664` | 8,182 (12.5%) | 0 | 0 | 0 |

### Parity with GDAL for non-nearest kernels

A synthetic 3-band UTM image (band 1 a 0/200 checkerboard with `nodata=0`, bands 2 and 3 constant) warped to WGS84 at the WarpedVRT's native size (87 × 25), using the sync reader's VRT options (`nodata=0, src_nodata=0, add_alpha=False`).

| kernel | path | band 1 blended values | band 1 zeros | bands 2–3 intact | band 1 pixels ≠ `warp()` |
| --- | --- | ---: | ---: | --- | ---: |
| bilinear | WarpedVRT | 1018 | 515 | yes | 0 |
| bilinear | `warp()` | 1018 | 515 | yes | — |
| cubic | WarpedVRT | 841 | 607 | yes | 0 |
| cubic | `warp()` | 841 | 607 | yes | — |

I also passed `UNIFIED_SRC_NODATA` set to `NO`, `PARTIAL` and `YES` through `warp_extras`, and the output was byte-identical each time. The sync reader doesn't set that option, so the default is the behaviour to match.

## Where to look

| File | What to review |
| --- | --- |
| `rio_tiler/_warp.py` | Most of the change. `warp()` (single pass, per-band nodata), `get_overview_level()`, `get_downsampling_factor()`. Check the kernel choice and the mask handling before and after `reproject`. |
| `rio_tiler/experimental/geotiff.py` | `part()` and `preview()` use the GDAL rule. `part()` now raises `ValueError` for a bbox entirely left of or above the dataset; it used to build a window with a negative size. |
| `rio_tiler/experimental/zarr.py` | Multiscale level selection uses the GDAL rule. `select_variable()` takes `resampling_method`. `GroupReader.part()` now accepts and passes on `resampling_method`, which was documented but missing. |
| `rio_tiler/constants.py` | New `OVERVIEW_OVERSAMPLING_THRESHOLD`, read from `RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD`. |
| `tests/test_warp.py` | Kernel tests rewritten for the new rules. New `test_get_overview_level`, `test_get_downsampling_factor` and `test_warp_per_band_nodata`, which compares against WarpedVRT. |
| `tests/test_zarr_group.py` | Updated multiscale expectations: `max_size=150` on a 1000 px variable now keeps full resolution. New `bilinear` case. |
| `CHANGES.md`, `docs/src/experimental/geozarr.md` | Changelog entries and a description of how the GeoZarr level is selected. |

The internal `zoom_level_strategy` option of the overview selection methods is removed.

## Known differences

- **Same-CRS reads near an overview's resolution.** With bilinear or cubic, values can still differ when the output resolution is within a few percent of an overview's. Both readers pick the same overview, but the sync reader resamples with GDAL's RasterIO and `warp()` uses GDAL's warper, and the two kernels differ slightly at about 1:1.
- **`gauss` when downsampling.** The two-step path caps the intermediate grid at the output size to bound memory, so the resize does nothing and the output equals nearest. That's unchanged from main.
- **Masks without nodata.** Without a nodata value, the warp produces one mask shared by all bands, like `rio_tiler.io.Reader`'s WarpedVRT alpha band. Only nodata-based masks are kept per band, in both readers.
- **Zarr readers.** Level selection is covered by unit tests on synthetic levels; there was no pixel comparison like the one for geotiff.

## Testing

- **Passed:** `tests/test_warp.py`, 10 passed, including `test_warp_per_band_nodata`, run after the nodata fix.
- **Passed:** earlier run, before the overview-rule change: `test_warp`, `test_resampling`, `test_geoxarray`, `test_io_zarr`, `test_zarr_array`, `test_zarr_group` (140 passed, 1 skipped).
- **Not run:** the rest of the suite after the overview-rule change and the nodata fix, including the geotiff, xarray and zarr reader tests that call `warp()`.
- **Passed:** pre-commit (isort, ruff, ruff format, mypy).

Measurements come from scratch scripts run against GDAL 3.12.2, rasterio 1.5.2 and async-geotiff 0.5.1.
