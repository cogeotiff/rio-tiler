# Plan: stack N-D data in zarr group readers (`stack_on_dim`)

## Prompts

### Prompt 1: initial request
> continuing on the last PR #1025, we need to handle ND arrays in `group` readers.
> The main idea would be to `merge` the arrays but adding a new dimensions
> ```
> img1 = ImageData(array=numpy.zeros((2, 10, 10), dimensions=["time", "y", "x"])
> img2 = ImageData(array=numpy.zeros((2, 10, 10), dimensions=["time", "y", "x"])
>
> img = ImageData.create_from_list([img1, img2])
> print(img.dimensions)
> >> ["assets", "time", "y", "x"]
> print(img.array.shape)
>  >> (2, 2, 10, 10)
> ```

### Prompt 2: revisions
> let's stack when using specific `kwargs`: `create_new_dim="assets"`?
> this would return a ND image data with `dimensions=["assets", "b", "y", "x"]` and band_names/band_descriptions set accordingly
> The idea is to use this new option only for the zarr experimental group readers

> let's start changing the code but do relatively small commits. Try not to create new functions.
> We'll write the tests after

> what do you think about `stack_on_dim: str | None = None` option name?

> I think we shoud always stack on new dim even when they are 1 band

## Context

PR #1025 added N-D support to `ImageData`/`PointData` and the zarr Array readers, but
`ImageData.create_from_list` / `PointData.create_from_list` raised for N-D inputs, so the
zarr `GroupReader`/`AsyncGroupReader` could not merge variables returning N-D data. Also,
3D variables (e.g. `["time", "y", "x"]`) were concatenated into a single mixed `time` axis.

## Design

Add an opt-in `stack_on_dim: str | None = None` option to `create_from_list`. When set,
the inputs are **stacked** along a new leading dimension instead of being concatenated:

```python
img1 = ImageData(numpy.zeros((2, 10, 10)), dimensions=["time", "y", "x"])
img = ImageData.create_from_list([img1, img1], stack_on_dim="assets")
img.dimensions   # ["assets", "time", "y", "x"]
img.array.shape  # (2, 2, 10, 10)
```

Only the zarr experimental group readers use it. The default behaviour (concatenate, and
raise for N-D inputs) is unchanged, so `MultiBaseReader`/STAC readers and
`tasks.multi_arrays` are untouched.

## Implementation (done)

### 1. `ImageData.create_from_list(data, stack_on_dim=None)` (`rio_tiler/models.py`)
- `stack_on_dim` set:
  - always stack, even for a single input
  - raise `ValueError` if `stack_on_dim` is already a dimension, or if the inputs have different `dimensions` or `array.shape[:-2]`
  - resize to max height/width as before; N-D data are flattened with `_as_3d` for `resize_array`, then reshaped back
  - `arr = numpy.ma.stack(...)`, `dimensions = [stack_on_dim, *data[0].dimensions]`
  - `band_names` / `band_descriptions` = `{stack_on_dim: [f"{stack_on_dim}{ix + 1}", ...], **per-dim labels of data[0]}` (a 3D `list` becomes `{dimensions[0]: list}`)
  - `dataset_statistics=None`
- No new helper functions; the logic is inline in `create_from_list`.

### 2. `PointData.create_from_list(data, stack_on_dim=None)`
Same semantics, raising `InvalidPointDataError` and validating against the full `array.shape`.

### 3. zarr `GroupReader` / `AsyncGroupReader` (`part`, `preview`, `point`; `tile`/`feature` go through `part`)
- Always call `create_from_list(stack, stack_on_dim="variables")`, even for single-band variables.
- Set `band_descriptions["variables"] = list(variables)`.
- The `if not img.is_nd: band_names = [...]` reset is removed, since the output is always N-D.

### 4. `CHANGES.md`
Entries for the new `stack_on_dim` option and for the group readers always returning N-D data.

## Open issues

- The group readers' `expression` option now always raises, because `apply_expression` rejects N-D data. For example, two single-band variables return `(n_variables, 1, y, x)`. Options:
  1. remove `expression` from the group readers
  2. squeeze a size-1 band dimension before applying the expression (recommended)
  3. keep it and document that it raises

## Tests (next)

- `tests/test_models.py`
  - stack 3D `["time", "y", "x"]` inputs: dims, shape, dict `band_names`/`band_descriptions`
  - stack N-D (4D) inputs into 5D output
  - a single input with `stack_on_dim` still gets the new dimension
  - mismatched dimensions or shapes, and an already-existing dimension name, raise
  - different height/width warn and resize
  - `PointData` equivalents
  - the default call (no `stack_on_dim`) still raises for N-D inputs
- `tests/test_zarr_group.py`
  - `part`/`preview`/`point` with several variables return `["variables", ...]` dims and `band_descriptions["variables"] == variables`
  - update the existing expectations that relied on concatenation
