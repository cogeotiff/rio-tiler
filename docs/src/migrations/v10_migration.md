
!!! note

    This migration guide was generated with the help of Claude AI and may require review.

`rio-tiler` version 10.0 introduced [many breaking changes](../release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 10.0.

Changelog: https://github.com/cogeotiff/rio-tiler/compare/9.4.13..10.0.0


## Python and Dependencies

- Python **3.11** support has been removed (`rasterio>=1.5` requires Python >=3.12)
- `rasterio>=1.5.1` is now required
- `affine>=3.0` is now required

With `affine>=3.0`, using `*` for matrix multiplication is deprecated (`PendingDeprecationWarning`). Use `@` instead:

```python
from affine import Affine

# before (9.x)
transform = dataset.transform * Affine.translation(col_off, row_off)

# now (10.x)
transform = dataset.transform @ Affine.translation(col_off, row_off)
```


## `scales` and `offsets` Removed from ImageData and PointData

The `scales` and `offsets` attributes have been removed from the `ImageData` and `PointData` models. They are no longer accepted as init arguments, and they are no longer propagated through `create_from_list`, `rescale`, `apply_color_formula`, `reproject`, `resize`, `clip`, etc.

The `unscale` option of the readers is still available and still applies the **dataset's** scales/offsets to the output data.

```python
from rio_tiler.io import Reader

# before (9.x)
with Reader("cog.tif") as src:
    img = src.read()
    print(img.scales, img.offsets)
    >> [0.0001] [0.0]

# now (10.x)
with Reader("cog.tif") as src:
    img = src.read()
    img.scales
    >> AttributeError: 'ImageData' object has no attribute 'scales'

    # Option 1: let rio-tiler apply them
    img = src.read(unscale=True)

    # Option 2: get them from the dataset
    print(src.dataset.scales, src.dataset.offsets)
    >> (0.0001,) (0.0,)
```

```python
from rio_tiler.models import ImageData

# before (9.x)
img = ImageData(array, scales=[1.0], offsets=[0.0])

# now (10.x)
img = ImageData(array)
```


## `count` Removed from ImageData and PointData

The `count` attribute has been removed from the `ImageData` and `PointData` models. Because the models now support N-D data (see [N-D Support](#n-d-support-in-imagedata-and-pointdata)), the "number of bands" isn't always a single value anymore. Use the array shape instead:

```python
from rio_tiler.io import Reader

# before (9.x)
with Reader("cog.tif") as src:
    img = src.read()
    print(img.count)
    >> 3

# now (10.x)
with Reader("cog.tif") as src:
    img = src.read()
    print(img.array.shape[0])
    >> 3
```

This also applies to custom `MosaicMethodBase` implementations or any code that read `img.count` / `pt.count`.


## Band Names and Descriptions in Mosaic Readers

`mosaic_reader`, `mosaic_point_reader` and `async_mosaic_reader` no longer forward the `band_names` and `band_descriptions` of the first asset to the output `ImageData`/`PointData`. The output uses the default values (`b1`, `b2`, ...) and the first asset's `band_descriptions` are stored in `metadata["band_descriptions"]`.

```python
from rio_tiler.io import Reader
from rio_tiler.mosaic import mosaic_reader

def tiler(asset, *args, **kwargs):
    with Reader(asset) as src:
        return src.tile(*args, **kwargs)

# before (9.x)
img, assets = mosaic_reader(["cog1.tif", "cog2.tif"], tiler, x, y, z)
print(img.band_descriptions)
>> ["red", "green", "blue"]

# now (10.x)
img, assets = mosaic_reader(["cog1.tif", "cog2.tif"], tiler, x, y, z)
print(img.band_descriptions)
>> ["b1", "b2", "b3"]

print(img.metadata["band_descriptions"])
>> ["red", "green", "blue"]

# restore the previous behavior
img.band_descriptions = img.metadata["band_descriptions"]
```


## N-D Support in ImageData and PointData

`ImageData` and `PointData` now accept N-D arrays with shape `(*leading, height, width)` (`(*leading,)` for `PointData`) and have a new `dimensions` attribute.

For 3D data (the default for all non-experimental readers), nothing changes: `dimensions` defaults to `["b", "y", "x"]` and `band_names`/`band_descriptions` are still `list[str]`.

```python
import numpy
from rio_tiler.models import ImageData

# 3D: same as 9.x
img = ImageData(numpy.ma.zeros((3, 256, 256)))
print(img.dimensions, img.band_names)
>> ['b', 'y', 'x'] ['b1', 'b2', 'b3']

# N-D (new in 10.x)
img = ImageData(
    numpy.ma.zeros((2, 3, 256, 256)),
    dimensions=["time", "band", "y", "x"],
)
print(img.is_nd)
>> True

print(img.band_names)
>> {'time': ['time1', 'time2'], 'band': ['band1', 'band2', 'band3']}
```

The band names of 3D data are derived from the first dimension name (`{dimension}{n}`), so data created with a custom `dimensions` will have different band names (and expressions must use them):

```python
img = ImageData(numpy.ma.zeros((2, 256, 256)), dimensions=["band", "y", "x"])
print(img.band_names)
>> ['band1', 'band2']

img.apply_expression("band1/band2")
```

!!! important

    Expressions, colormaps, color formulas, `rescale`, `statistics`, `to_raster` and image rendering (except `NPY`/`NPZ` formats) only work with 3D data and raise a `ValueError` for N-D data. Use `ImageData.reduce()` (or `sel` in the zarr readers) to get back to 3D data first.

If your code assumes `band_names`/`band_descriptions` are always lists (e.g. in a custom reader or a titiler dependency), make sure to handle the `dict` case (or check `img.is_nd`).


## Experimental Zarr Readers

The `rio_tiler.experimental.zarr` readers (`ArrayReader`, `AsyncArrayReader`, `GroupReader`, `AsyncGroupReader`) have been refactored to use **named dimensions**.

### Array Readers Init Options

- `band_names` has been **removed**. Band descriptions are now derived from the coordinates of the non-spatial dimensions (fallback to `{dimension}{n}`)
- `dimensions` is **new** (defaults to the zarr `dimension_names` metadata, which is now required)
- `spatial_dims` is **new** (`[y_dim, x_dim]`, defaults to `spatial:dimensions` from the `spatial` zarr-convention). Y/X no longer need to be the last two axes
- `coordinates` now holds the full `coords:coordinates` mapping (`{dimension: {...}}`) instead of the coordinate of the first non-spatial dimension
- 2D and 3D arrays are no longer the only supported shapes: any array with `>=2` dimensions can be read

```python
from rio_tiler.experimental.zarr import ArrayReader

# before (9.x)
with ArrayReader(
    array,  # shape (3, height, width)
    crs=crs,
    transform=transform,
    band_names=["red", "green", "blue"],
) as src:
    ...

# now (10.x)
with ArrayReader(
    array,  # shape (3, height, width)
    crs=crs,
    transform=transform,
    dimensions=["band", "y", "x"],  # if not in the zarr metadata
    spatial_dims=["y", "x"],  # if not set by the `spatial` zarr-convention
    coordinates={
        "band": {"type": "inline", "values": ["red", "green", "blue"]},
    },
) as src:
    ...
```

### `indexes` replaced by `sel`/`sel_method`

The `indexes` option has been **removed** from all the zarr readers' methods (`read`, `tile`, `part`, `preview`, `point`, `feature`, `statistics`). Non-spatial dimensions are now selected with xarray-like `sel` and `sel_method` options:

- `sel`: `{dimension: value | list | slice}`, selection using the `coordinates` values (or positions when a dimension has no coordinates). A scalar drops the dimension
- `sel_method`: `None` (exact match, default), `nearest`, `pad`/`ffill` or `backfill`/`bfill`

```python
# before (9.x)
with ArrayReader(array, band_names=["red", "green", "blue"]) as src:
    img = src.tile(x, y, z, indexes=[1, 2])

# now (10.x)
with ArrayReader(array) as src:  # dimensions: ["band", "y", "x"]
    # select by coordinate values
    img = src.tile(x, y, z, sel={"band": ["red", "green"]})

    # or by position, when the dimension has no coordinates
    img = src.tile(x, y, z, sel={"band": [0, 1]})

    # inexact match on a time dimension
    img = src.tile(x, y, z, sel={"time": "2025-01-15"}, sel_method="nearest")
```

Unselected non-spatial dimensions are kept, so readers now return `(*non-spatial dims, height, width)` data, which can be N-D. The selected labels are stored in `ImageData.metadata["selected"]`.

### Expressions and Statistics Keys

Band names are now derived from the name of the non-spatial dimension instead of always being `b{n}`. Expressions and `statistics()` keys must use them:

```python
# before (9.x)
with ArrayReader(array) as src:  # shape (3, height, width)
    img = src.tile(x, y, z, expression="b1/b2")
    stats = src.statistics()
    print(list(stats))
    >> ["b1", "b2", "b3"]

# now (10.x)
with ArrayReader(array) as src:  # dimensions: ["band", "y", "x"]
    img = src.tile(x, y, z, expression="band1/band2")
    stats = src.statistics()
    print(list(stats))
    >> ["band1", "band2", "band3"]
```

!!! note

    2D arrays (`(y, x)`, or reduced to 2D with a scalar `sel`) still use the default `b` dimension (`b1`).

### `info()` Response

- `dimensions` now returns the reader's `dimensions` attribute
- per-band metadata (`band_metadata`, `band_descriptions`) is no longer listed
- new `dimensions_count` (`{dimension: size}`)
- new `coordinates` (`{dimension: labels}`) when called with `with_coordinates=True`

```python
# now (10.x)
with ArrayReader(array) as src:
    info = src.info(with_coordinates=True)
    print(info.dimensions_count)
    >> {'time': 12, 'y': 1024, 'x': 1024}
```

### Group Readers: Variables Stacking

`GroupReader` and `AsyncGroupReader` now stack the variables along a new `variables` dimension (using `ImageData.create_from_list(..., stack_on_dim="variables")`) instead of concatenating them along the band dimension.

- when all the variables are 2D, the output is 3D with dimensions `["variables", y, x]`
- otherwise the output is N-D with dimensions `["variables", *non-spatial dims, y, x]`
- when only one variable is requested, its data is returned as is (no `variables` dimension)

The variable names are stored in `band_descriptions`, while `band_names` are `variables1`, `variables2`, ..., which are the names to use in expressions or to access `statistics()` results.

```python
from rio_tiler.experimental.zarr import GroupReader

# before (9.x)
with GroupReader(group) as src:
    img = src.tile(
        x, y, z,
        variables=["b08", "b04"],
        expression="(b1-b2)/(b1+b2)",
    )

# now (10.x)
with GroupReader(group) as src:
    img = src.tile(
        x, y, z,
        variables=["b08", "b04"],
        expression="(variables1-variables2)/(variables1+variables2)",
    )

    img = src.tile(x, y, z, variables=["b04", "b03", "b02"])
    print(img.dimensions)
    >> ['variables', 'y', 'x']

    print(img.band_names, img.band_descriptions)
    >> ['variables1', 'variables2', 'variables3'] ['b04', 'b03', 'b02']
```

### Custom Array Reader Subclasses

The internal `_read` method signature changed from `_read(row_slice=, col_slice=, indexes=)` to `_read(y_slice=, x_slice=, sel=, sel_method=)`, and reads now use zarr's `get_orthogonal_selection`.


## New Features

### `ImageData.reduce` / `PointData.reduce`

Reduce N-D data along a non-spatial dimension. Reduced dimensions are listed in `metadata["reduced"]`.

```python
import numpy

with ArrayReader(array) as src:  # dimensions: ["time", "band", "y", "x"]
    img = src.preview()
    print(img.dimensions)
    >> ['time', 'band', 'y', 'x']

    img = img.reduce("time", numpy.ma.mean)
    print(img.dimensions, img.metadata["reduced"])
    >> ['band', 'y', 'x'] ['time']

    # back to 3D: expressions, rendering, statistics... work again
    img.render(img_format="PNG")
```

### `stack_on_dim` in `create_from_list`

`ImageData.create_from_list` and `PointData.create_from_list` accept a `stack_on_dim` option to stack data along a new leading dimension instead of concatenating them along the first dimension:

```python
from rio_tiler.models import ImageData

img = ImageData.create_from_list([img1, img2], stack_on_dim="time")
print(img.dimensions)
>> ['time', 'y', 'x']  # 2D inputs (`(1, y, x)` with a `b` dimension)
# or
>> ['time', 'b', 'y', 'x']  # multi-band inputs
```

### `resampling_method` in Zarr Array Readers `tile`

The zarr Array readers' `tile` method now accepts a `resampling_method` option.

### `rio_tiler.utils.run_sync`

Run a blocking function in a worker thread (`asyncio.to_thread`), forwarding the active rasterio environment. The async experimental readers (`geotiff.Reader`, `zarr.AsyncArrayReader`) and `AsyncBaseBackend` now use it for warp/reproject/resize/rasterize operations to avoid blocking the event loop.

```python
from rio_tiler.utils import run_sync

img = await run_sync(img.resize, 512, 512)
```


## Migration Checklist

1. **Upgrade Python and dependencies** - Python >=3.12, `rasterio>=1.5.1`, `affine>=3.0` (use `@` instead of `*` for `Affine` multiplication)

2. **Remove `scales`/`offsets` usage** - Stop passing them to `ImageData`/`PointData`, use `unscale=True` or read them from the dataset

3. **Replace `.count`** - Use `img.array.shape[0]` (or `img.dimensions`/`img.array.shape` for N-D data)

4. **Update mosaic band descriptions handling** - Read the first asset's descriptions from `img.metadata["band_descriptions"]`

5. **Handle N-D data** - If you consume `ImageData`/`PointData` from experimental readers, `band_names`/`band_descriptions` can be `dict`; check `img.is_nd` and use `reduce()` before rendering

6. **Update zarr Array readers init** - Replace `band_names` with `coordinates` and set `dimensions`/`spatial_dims` if not in the zarr metadata

7. **Replace `indexes` with `sel`** - In all zarr readers' methods

8. **Update zarr expressions and statistics keys** - Use `{dimension}{n}` (e.g. `band1`) for Array readers and `variables{n}` for Group readers

9. **Update custom zarr reader subclasses** - `_read(row_slice=, col_slice=)` -> `_read(y_slice=, x_slice=, sel=, sel_method=)`
