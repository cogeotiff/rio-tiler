# Plan: `reduce(dim, func)` for ImageData and PointData

## Context
Since #1025, `ImageData` (`(*leading, y, x)`) and `PointData` (`(*leading,)`) can hold N-D data, but most 3D-only methods (`apply_expression`, `rescale`, `statistics`, `render` to PNG/JPEG, colormap...) raise on N-D data. There is no way to collapse a dimension (e.g. a temporal mean over `time`) to get back to 3D/1D data that the rest of the pipeline understands. Add a `reduce(dim, func)` method on both models.

## API
```python
def reduce(self, dim: str, func: Callable[..., numpy.ma.MaskedArray]) -> "ImageData":
    """Reduce data along a non-spatial dimension (e.g `img.reduce("time", numpy.ma.mean)`)."""
```
Same signature on `PointData` (returns `PointData`).

- `func` is called as `func(self.array, axis=axis)` — numpy-style reducers. Masked-aware ones (`numpy.ma.mean`, `numpy.ma.max`, `numpy.ma.median`, ...) give correct nodata handling (a pixel is masked only if all values along `dim` are masked). Result is passed through `numpy.ma.asarray` + `masked_and_3d`/`to_masked` so plain-numpy reducers still work.
- One dimension per call; chain calls to reduce several (`img.reduce("time", f).reduce("z", g)`).

## Behavior / validation (in `rio_tiler/models.py`)
- `dim not in self.dimensions` → `ValueError`.
- ImageData: `dim` in `self.dimensions[-2:]` (spatial y/x) → `ValueError`.
- New `dimensions` = `self.dimensions` minus `dim`.
- `band_names` / `band_descriptions` (dicts for N-D): drop the `dim` key.
  - If the result is still N-D → keep the dict.
  - If the result is 3D (ImageData) / 1D (PointData) → convert to the list of the remaining dimension (`dict[remaining_dim]`), so it passes the non-N-D asserts in `__attrs_post_init__` (lines ~508-515 / ~242-249).
- Reducing the last non-spatial dim of a 3D ImageData (e.g. `"b"` on `(3, h, w)`) or the only dim of a 1D PointData: result keeps a length-1 axis via `numpy.expand_dims(..., 0)`; `dimensions=[dim, "y", "x"]` / `[dim]`, `band_names`/`band_descriptions` use the defaults (`[f"{dim}1"]`).
- Forward unchanged: `assets`, `crs`, `bounds`/`coordinates`, `nodata`, `metadata`, `alpha_mask`, `cutline_mask` (ImageData), `pixel_location` (PointData).
- Drop `dataset_statistics` (no longer valid after reduction).
- Small helper to share the band metadata logic between both classes, e.g. a module-level `_reduce_band_metadata(meta, dim, remaining_dims, is_nd)` near `to_masked`/`masked_and_3d`. Keep it minimal.

## Files
- `rio_tiler/models.py` — add `PointData.reduce` (after `apply_expression`, ~line 381) and `ImageData.reduce` (after `apply_expression`, ~line 874), plus the shared helper. Add `Callable` to imports if missing.
- `tests/test_models.py` — next to the existing N-D tests (`_nd_image`, `test_nd_image_metadata`, `test_nd_point_data`):
  - 4D → 3D: `_nd_image(dimensions=["time","z","y","x"], band_descriptions=...)`, `reduce("time", numpy.ma.mean)` → shape `(3, 10, 12)`, `not is_nd`, `band_descriptions == ["0","10","20"]`, values match `numpy.ma.mean(arr, axis=0)`; then `apply_expression("z1+z2")` works.
  - 5D → 4D keeps dict metadata.
  - mask: pixel masked in all `time` slices stays masked; masked in one slice stays valid.
  - errors: unknown dim, `"y"`/`"x"`.
  - 3D `reduce("b", numpy.ma.max)` → `(1, h, w)`.
  - PointData 2D → 1D and 1D → `(1,)`.
- `CHANGES.md` — under `# Unreleased`: `* add: \`reduce(dim, func)\` method to \`ImageData\` and \`PointData\` to reduce N-D data along a non-spatial dimension`.
- `docs/src/models.md` — short section with an example.

## Verification
- `uv run pytest tests/test_models.py -k "nd or reduce"` (only when asked to run tests, per preference).
- Quick sanity snippet: build 4D ImageData, `reduce("time", numpy.ma.mean).render(img_format="PNG")` succeeds after rescale.
