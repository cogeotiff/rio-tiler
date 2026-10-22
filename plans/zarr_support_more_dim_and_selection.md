# Plan: xarray-like `sel` and N-D output for zarr readers

## Prompts

### Prompt 1: initial request
> I need to replace the `indexes` parameter with a more general `sel` parameter which would replicate the behaviour of https://docs.xarray.dev/en/stable/generated/xarray.DataArray.sel.html#xarray.DataArray.sel
> The selection would be for the non-spatial coordinates and the coordinates would be the one defined in the `optional` coordinates attribute.
> The main idea is to be able to do something like
> ```
> ds = AsyncArray(input: zarr.AsyncArray = array, coordinates={"time": {"type": "inline", "values": [...]}})
> im = ds.read(sel={"time": "2025-01-01", "z": 100}, sel_method="nearest"})
> ```
> for context I think the xarray sel methods is based on https://github.com/pydata/xarray/blob/main/xarray/core/indexes.py
>
> Maybe there are already things that exists on xarray, so it would be fine to re-uses something that exist in a really small library

### Prompt 2: revisions
> 1. let's think about how to use `sel` when coordinates is `None`. Maybe we could have something based on the array position and the `dimensions`
> ```
> ds = AsyncArray(input: zarr.AsyncArray = array, dimensions=["time", "x", "y"])
> im = ds.read(sel={"time": [0, 1, 2]}, method="position")
> ```
> or maybe this is implicite when method=None?
>
> 2. We would need to change the signature of the `band_descriptions` from `list[str]` to `dict[str, Any]` which instead of presenting only for first non-spatial dim would show all the values for all the non-spatial dim
>
> 3. The main idea is to be able to have a 4d/5d output from the `_read` methods. The `apply_expression` should not work on this case and should error for non-3d arrays
>
> 4. The ImageData class would need to be slightly refactored to make sure it works for 4/5D array.
> - the apply_expression should error
> - the band_descriptions should be a Union of list[str] | dict[str, Any]
> - I'm not sure what the band_names should be
> - the `render` method should error except when `NPY` or `NPZ` output

### How each prompt shaped the plan
- Prompt 1: numpy-only `sel` / `sel_method` (no pandas/xarray dependency), coordinate-typed matching.
- Prompt 2.1: when a dimension has no coordinates, `sel` uses array positions automatically (no separate `method="position"`).
- Prompt 2.2: `band_descriptions` becomes a dict covering every non-spatial dimension.
- Prompts 2.3 and 2.4: `_read` returns N-D data; `ImageData` raises an error for N-D in expression, colormap and image `render` (only `NPY`/`NPZ` allowed); `band_names` is `b1..bN` for 3D only and `[]` for N-D (per-dimension metadata only, so lists never grow to the product of the dimension sizes).

## Context
`rio_tiler/experimental/zarr.py` readers (`AsyncArrayReader`, `ArrayReader`) select bands via 1-based
`indexes` on the *first* non-spatial dim only, reject ndim > 3, and always return `(bands, h, w)`.
Goal: label-based selection on any non-spatial dim (mirroring `xarray.DataArray.sel(..., method=...)`)
using the optional `coordinates` attribute, and let `_read` return **N-D** data
`(*non_spatial_dims, h, w)` (4D/5D) when several non-spatial dims are left unselected.

```python
src = AsyncArrayReader(input=array, coordinates={"time": {"type": "inline", "values": [...]}, "z": {...}})
img = await src.preview(sel={"time": "2025-01-01", "z": 100}, sel_method="nearest")   # -> (1, h, w)
img = await src.preview(sel={"time": ["2025-01-01", "2025-02-01"]})                     # -> (2, nz, h, w)
src = AsyncArrayReader(input=array, dimensions=["time", "y", "x"])                     # no coordinates
img = await src.preview(sel={"time": [0, 1, 2]})                                       # positional
```

## Dependency decision
xarray's `sel` delegates to `pandas.Index.get_indexer(method=...)`; there is no small standalone lib
for it. Implement with **numpy only** (`searchsorted` on sorted coord values, ~60 lines).

## 1. Selection semantics (`sel`, `sel_method`)
- `sel: dict[str, Any] | None = None`; `sel_method: Literal["nearest", "pad", "ffill", "backfill", "bfill"] | None = None` (None = exact, as xarray).
- Selector per non-spatial dim: scalar → dim dropped; list → dim kept (given order); `slice(a, b)` → label-based inclusive (method ignored).
- Keys must be non-spatial dims (`ValueError` otherwise). Unselected non-spatial dims are kept whole.
- Exact-match miss / pad-before-first / backfill-after-last → `KeyError` (like xarray).
- **No coordinates for a dim → implicit positional labels** `numpy.arange(size)`. Rationale: there are no labels to collide with, so no separate `method="position"` is needed; `nearest/pad/backfill` still behave sensibly on integers. (A future `isel` could cover "positional on a labelled dim" if ever needed.)
- Query-value coercion to the coordinate's type (needed for string inputs from titiler URLs): numeric → `float`; temporal → isochron `parse_datetime` → `datetime64` (UTC, naive); string coords → exact match only (`sel_method` set → `ValueError`).

## 2. Zarr reader changes (`rio_tiler/experimental/zarr.py`)
1. `_get_coordinate_values(coords) -> numpy.ndarray` (numeric / `datetime64` / str), refactored from `_get_bnames_from_coordinates` (reuse its inline/interval/isochron logic). Label formatting (`format_datetime` / `str`) as a small helper.
2. `_sel_indexer(values, selector, method) -> int | ndarray | slice` (numpy-only).
3. `ArrayMixin`:
   - accept `ndim >= 2` (drop the `(2, 3)` check); `nbands` = product of non-spatial dim sizes (1 for 2D).
   - `cached_property _coordinate_values: dict[dim, ndarray]` (from `coordinates` + arange fallback).
   - **`band_descriptions` → `dict[str, list[Any]]`**: `{dim: [labels...]}` for *every* non-spatial dim, in array order (`{}` for 2D).
   - `_get_selection(sel, sel_method) -> (selection: dict[dim, int|ndarray|slice], kept: dict[dim, list[labels]], scalars: dict[dim, label])`.
   - `_info()`: `count = nbands`; `band_descriptions`/`band_metadata` as a list only when ≤1 non-spatial dim, otherwise `[]`; the dict form goes in a new extra key `"dimension_values"` (Info allows extra fields) — avoids emitting thousands of entries for e.g. 1000×50 cubes.
4. `_read` (async ~L871 & sync ~L1509): params `sel`, `sel_method` replace `indexes`; build the orthogonal selection (+ y/x slices), `get_orthogonal_selection`, then `moveaxis` y/x to the last two axes using the *remaining* dims order → shape `(*kept_dims, h, w)`; `expand_dims` to `(1, h, w)` when nothing is kept. MaxArraySize uses the selected sizes. Returns `ImageData(..., band_descriptions=kept, metadata={"sel": scalars} if scalars)`.
5. Public methods of both Array readers (`statistics`, `tile`, `part`, `preview`, `point`, `feature`): `indexes` → `sel`, `sel_method`. Expression is applied after read (no more `parse_expression` → indexes; drop "expression overwrites indexes" warnings). `point` uses `img.array[..., 0, 0]`.
6. Group readers (`AsyncGroupReader`, `GroupReader`): accept and forward `sel`, `sel_method` to the per-variable Array reader calls (`_part`, `_preview`, `_point`, … closures). `create_from_list` of multiple N-D images → error (see §3); single variable passes through.
7. Remove unused imports (`Indexes`, `parse_expression`, `ExpressionMixingWarning`, …).

## 3. `ImageData` / `PointData` refactor (`rio_tiler/models.py`)
Array layout convention: `(*leading, height, width)`; 3D stays exactly as today.
- `height = shape[-2]`, `width = shape[-1]`; `count = shape[0]` (unchanged meaning: size of the first axis); new helper `is_nd = array.ndim > 3`.
- **Rule: no per-flattened-band metadata for N-D.** Anything sized `prod(shape[:-2])` (e.g. 1000 times × 50 levels = 50 000 entries) is never materialised; N-D metadata is per-dimension only (`sum` of dim sizes, 1 050 entries in that example).
- **`band_names`**: 3D → unchanged (`b1..bN`). N-D → defaults to `[]`, i.e. bands aren't individually addressable; this is consistent with `apply_expression` (the only `bN` consumer) being 3D-only.
- **`scales` / `offsets`**: 3D → unchanged. N-D → one value broadcast to every band (`[s]` / `[o]`), which matches zarr (one `scale_factor`/`add_offset` per array). Validate `len in (1, count)` for N-D.
- **`band_descriptions: list[str] | dict[str, list[Any]]`**: 3D → `list[str]` (a one-key dict is converted to its label list, so 3D stays exactly as today); N-D → `dict[dim, labels]` per leading axis (in axis order), never expanded to the cartesian product.
- `_mask`: `logical_or.reduce` over all leading axes (`~mask.reshape(-1, h, w)`), so `mask` stays `(h, w)`.
- Geometry ops reshape to `(prod, h, w)` → op → reshape back (array only, metadata untouched): `resize`, `clip`, `reproject`, `rio_tiler/_warp.py::warp`, `get_coverage_array` (2D).
- **Error on N-D** (`ValueError("... only supported for 3D (bands, h, w) data")`): `apply_expression`, `apply_colormap`, `apply_color_formula`, `rescale`, `data_as_image`, `to_raster`, `statistics` (a result per combination would be the same oversized list: select down to 3D first with `sel`), `create_from_list` (when any input is N-D and len > 1), and `render` unless `img_format in ("NPY", "NPZ")`. For `NPY` + `add_mask=True` with N-D data, the 2D mask can't be stacked as an extra band → raise suggesting `NPZ` or `add_mask=False`; `NPZ` stores `data` (N-D) + `mask` (2D).
- `PointData`: same rules (`band_names=[]`, per-dim dict `band_descriptions`, broadcast scales/offsets for `array.ndim > 1`); `apply_expression` errors for `array.ndim > 1`.
- Zarr readers' `statistics()` method therefore requires the selection to leave ≤1 non-spatial dim (clear error otherwise).

## Tests
- `tests/test_zarr_array.py`, `tests/test_zarr_group.py`: convert `indexes=` cases to `sel=`, remove expression+indexes warning tests; new 4D (`time, z, y, x`) fixture covering exact / nearest / pad / backfill / list / slice / string inputs / errors / no-coordinates positional fallback; N-D output shape for `preview`, `part`, `tile`, `point`, `feature`; `band_descriptions` dict; `metadata["sel"]`.
- `tests/test_models.py`: N-D `ImageData` — height/width/count/mask, resize/reproject round-trip shape, render NPZ ok / PNG raises / NPY+mask raises, `apply_expression` / `statistics` raise, N-D `band_names == []`, per-dim dict `band_descriptions`, broadcast scales/offsets, one-key dict → list for 3D.

## Verification
Per user preference tests are not run unless asked; when asked:
`uv run pytest tests/test_models.py tests/test_zarr_array.py tests/test_zarr_group.py -q`.
Manual check: in-memory 4D `zarr` array, compare `AsyncArrayReader.preview(sel=..., sel_method="nearest").array` with `xarray.DataArray(...).sel(..., method="nearest")` on the same data.
