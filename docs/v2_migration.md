
`rio-tiler` version 2.0 introduced [many breaking changes](release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 2.0.

## Python **3** only

First and foremost is the drop of Python 2 support. We are in 2020 and Python 2
is [officially dead](https://pythonclock.org). For ease of maintenance we
decided to remove Python 2 support and to continue with only Python 3. **Python
3.6 or later is required.**

If you need help moving from Python 2 to 3 check out the official transition
[documentation](https://docs.python.org/3/howto/pyporting.html).

### Type hints

As part of switching to Python 3, we also embraced modern code style with the
adoption of type hints. Python 3.6+ has new syntax support for optional "type
hinting" -- declaring the type of a variable -- which enables an improved
development experience in editors and tools.

**This does not require any changes to your code as long as you're using Python 3.6+.**

For more information see:

- <https://fastapi.tiangolo.com/python-types/>
- <https://kishstats.com/python/2019/01/07/python-type-hinting.html>
- <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>

Typing example:

```python
def get_vrt_transform(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: Tuple[float, float, float, float],
    dst_crs: CRS = constants.WEB_MERCATOR_CRS,
) -> Tuple[Affine, int, int]:
```

## Rasterio >= **1.1.7**

Rasterio 1.1.7 or newer is required.

## ~~Mercantile~~ -> Morecantile

With [Morecantile](https://github.com/developmentseed/morecantile) we can support more than the Web Mercator TMS.

See [tms](advanced/tms.md)

## New **rio_tiler.io** submodules

We created revised submodules for working with COGs and STAC:

- `rio_tiler.io.cogeo` is a modified version of the previous `rio_tiler.main.tile`.
- `rio_tiler.io.stac` is a new module to work with [SpatioTemporal Asset Catalogs (STAC)](https://stacspec.org/).

We now support reading files through a
[`ContextManager`](https://docs.python.org/3.6/library/stdtypes.html#typecontextmanager)
to enable accessing the source rasterio dataset.

```python
# v1
from rio_tiler.main import tile as cogTiler
tile, mask = cogTiler('my_tif.tif', 691559, 956905, 21, tilesize=256)

# v2
from rio_tiler.io import COGReader
with COGReader("my_tif.tif") as cog:
    img = cog.tile(691559, 956905, 21, tilesize=256)

    print(cog.dataset) # rasterio dataset (returned by rasterio.open())
    print(cog.dataset.meta) # rasterio metadata
    print(cog.bounds)       # WGS84 bounds
    print(cog.colormap)     # internal colormap
```

Expression support is now directly available in the `COGReader`

```python
with COGReader("my_tif.tif") as cog:
    tile, mask = cog.tile(691559, 956905, 21, expression="b1/b2")
```

See [`COGReader`](readers.md#cogreader) amd [`STACReader`](readers.md#stacreader) for more info.

## Internal API: **rio_tiler.reader**

Internal tile/data reading functions have been refactored and moved to a new `rio_tiler.reader` submodule.

### tile

In `rio_tiler` v1 most of the magic was happening in [`rio_tiler.utils._tile_read`](https://github.com/cogeotiff/rio-tiler/blob/4286e55d43172040b4027575a845532e55a0fdf9/rio_tiler/utils.py#L337-L458). In the version 2, this function is now split in two, `rio_tiler.reader.part` and `rio_tiler_reader.read`, to reduce code reutilisation and to make the code more robust. The `part` function now takes `height` and `width` instead of a unique `tilesize` to specify the output array size.

```python
# v1
with rasterio.open("my_tif.tif") as src_dst:
    # get tile bounds and read raster
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    t, m = rio_tiler.utils._tile_read(src_dst, tile_bounds, 256)

# v2
with rasterio.open("my_tif.tif") as src_dst:
    t, m = rio_tiler.reader.tile(src_dst, tile_x, tile_y, tile_z, 256) # Will check if tile is valid

    # Or
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)
    t, m = rio_tiler.reader.part(src_dst, tile_bounds, 256, 256)
```

*Options changes:*

- `tile_edge_padding` -> `padding`, and set to **0** by default
- `minimum_tile_cover` -> `minimum_overlap`
- `warp_vrt_option` -> `vrt_options`
- `unscale` (**New**): add ability to apply scale and offset to the data (Default: False)
- `force_binary_mask` (**New**): force mask to either be 0 or 255, set to `True` by default.
- `post_process` (**New**): add post process callback to apply operation on the data and mask arrays.

```python
# v1
with rasterio.open("my_tif.tif") as src_dst:
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)
    t, m = rio_tiler.utils._tile_read(src_dst, tile_bounds, 256, tile_edge_padding=4, minimum_tile_cover=0.3)

# v2
with rasterio.open("my_tif.tif") as src_dst:
    t, m = rio_tiler.reader.tile(src_dst, tile_x, tile_y, tile_z, 256, padding=4, minimum_overlap=0.3)
```

#### Alpha band

Since the first version, `rio-tiler` returns a tuple of **(data, mask)** in most of the `reading` function. This design was made early and without thinking about datasets with an alpha channel, which resulted in issues like [#126](https://github.com/cogeotiff/rio-tiler/pull/126), where a user gets a 4 bands data array + a mask (instead of 3 bands + mask).

In version 2, when no `indexes` options are passed, **we remove the alpha channel from the output data array**.

```python
# v1
with rasterio.open("my_tif_alpha.tif") as src_dst:
    t, m = rio_tiler.utils._tile_read(src_dst, tile_bounds, 256, indexes=(1,2,3))

# v2
with rasterio.open("my_tif_alpha.tif") as src_dst:
    # because rio-tiler will remove the alpha band we don't need to use the indexes option
    t, m = rio_tiler.reader.tile(src_dst, tile_x, tile_y, tile_z, 256)
```

### metadata

`rio_tiler.utils._raster_get_stats` has been replaced by `rio_tiler.reader.metadata` which uses the new `reader.part` and `reader.preview` functions. Meaning that now you can get metadata for a specific area by passing a bbox.

To limit the data transfer (with the idea of getting the metadata from the COG overviews) we use the `max_size` options, meaning the `overview_level` options have been removed.

```python
# v1
import rio_tiler
with rasterio.open("my_tif.tif") as src_dst:
    meta = rio_tiler.utils._raster_get_stats(src_dst)

# v2
with rasterio.open("my_tif.tif") as src_dst:
    meta = rio_tiler.reader.metadata(src_dst)
```

*Options changes*

- removed `histogram_bins` and `histogram_range` which should now be passed in `hist_options` (e.g: hist_options={bins=10, range=(0, 10)})
- removed `overview_level`
- added `bounds`

*Output*

The output has also been updated. The new `metadata` output doesn't return min/max zoom and bounds is return in WGS84 by default.


```python
# v1
with rasterio.open("my_tif.tif") as src_dst:
    rio_tiler.utils._raster_get_stats(src_dst)

> {
    "bounds": {
        "value": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
        "crs": "EPSG:4326"
    },
    "minzoom": 3,
    "maxzoom": 12,
    "band_descriptions": [
        [1,  "band1"]
    ],
    "statistics": {
        "1": {
            "pc": [1, 17],
            "min": 1,
            "max": 18,
            "std": 4.418616203143802,
            "histogram": [
                [...],
                [...]
            ]
        }
    }
}

# v2
with rasterio.open("my_tif.tif") as src_dst:
    rio_tiler.reader.metadata(src_dst)

> {
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "statistics": {
        "1": {
            "percentiles": [1, 16],
            "min": 1,
            "max": 18,
            "std": 4.069636227214257,
            "histogram": [
                [...],
                [...]
            ]
        }
    },
    "nodata_type": "Nodata",
    "band_metadata": [["1", {}]],
    "band_descriptions": [["1", ""]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255 ],
        "2": [148, 56, 112, 255],
        ...
    }
}
```

## colormaps

In addition to a new colormap specific submodule `rio_tiler.colormap`, and colormap holder `rio_tiler.colormap.cmap`, in version 2, colormaps are now RGBA values.

We also removed `PIL` colormap compatibility.

```python
# v1
cmap = rio_tiler.utils.get_colormap("viridis", format="gdal")
print(cmap[0])
> [68, 1, 84]

# v2
from rio_tiler.colormap import cmap

colormap = cmap.get("viridis")
print(colormap[0])
> [68, 1, 84, 255]
```

## render

In version 1, to create an image blob from an array we used the `rio_tiler.utils.array_to_image` function. We have renamed and slightly refactored the function but it works the same.

```python
# v1
img = rio_tiler.utils.array_to_image(tile, mask, img_format="PNG")

# v2
img = rio_tiler.utils.render(tile, mask, img_format="PNG")
```

## Pydantic models

The `.io` readers now returns pydantic models hosting the results. This enables easy API definition.

See [models](models.md)

## Mission specific changes

**Mission-specific tilers have been moved to the [`rio-tiler-pds`][rio-tiler-pds] package.**

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds
