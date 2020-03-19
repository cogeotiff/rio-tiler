# rio-tiler 1.0 to 2.0 migration

rio-tiler version 2.0 introduced a lot of breaking changes [see](https://github.com/cogeotiff/rio-tiler/blob/f55134b383b14e5ed0a79f3dc27da0d9adbb21a4/CHANGES.txt#L10-L26). This documents aims to help with migrating your code to use rio-tiler 2.0.

## Python **3** only

First and main change is the drop of python 2 support. To be honest we first started this lib as a python 3 only and then switch back to support python 2. Now we are in 2020 and python 2 is [officially dead](https://pythonclock.org) we decided to remove python 2 support and to continue with only python 3.

If you need help moving from python 2 to 3 checkout the official [doc](https://docs.python.org/3/howto/pyporting.html).

### Type hints

By switching to python 3 we also embrace new code style with the adoption of type hints:

    Python 3.6+ has support for optional "type hints".
    These "type hints" are a new syntax (since Python 3.6+) that allow declaring the type of a variable.
    By declaring types for your variables, editors and tools can give you better support.
from:  https://fastapi.tiangolo.com/python-types/

Other docs:
- https://kishstats.com/python/2019/01/07/python-type-hinting.html
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

Example:
```python
def get_vrt_transform(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: Tuple[float, float, float, float],
    dst_crs: CRS = constants.WEB_MERCATOR_CRS,
) -> Tuple[Affine, int, int]:
```

## Rasterio >= **1.1.3**

Recent changes in rasterio makes masking more reliable.

## New **rio_tiler.io** submodules

Mostly to gain in code clarity, we moved the mission specific submodules (e.g. rio_tiler.landsat8) to an `rio_tiler.io` submodule. `rio_tiler.main` has also be renamed `rio_tiler.io.cogeo`.

```python
# v1
from rio_tiler.main import tile as cogTiler
tile, mask = cogTiler('my_tif.tif', 691559, 956905, 21, tilesize=256)

# v2
from rio_tiler.io.cogeo import tile as cogTiler
tile, mask = cogTiler('my_tif.tif', 691559, 956905, 21, tilesize=256)
```

```python
# v1
from rio_tiler import landsat8
landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')

# v2
from rio_tiler.io import landsat8
landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')
```

## **rio_tiler.reader**

Internal tile/data reading functions have been refactored and moved to a new `rio_tiler.reader` submodule.

### calculate_default_transform

When creating warped virtual raster dataset (WarpedVRT) we need to be able to predict both Affine matrix and size of the resulting array (height x width). For this in *rio-tiler==1* we used `rasterio.warp.calculate_default_transform` but our friends from TerraCotta project pointed out that it wasn't performing well at high latittude (and for non-squared pixel). In *rio-tiler==2* we switched to their implementation of `calculate_default_transform`, which should improve the global performance of the reads ([#155](https://github.com/cogeotiff/rio-tiler/pull/155)).

### tile

In *rio_tiler==1* most of the magic was happening in [`rio_tiler.utils._tile_read`](https://github.com/cogeotiff/rio-tiler/blob/master/rio_tiler/utils.py#L337-L349). In *rio_tiler==2* this function is now splited in 2 `rio_tiler.reader.part` and `rio_tiler_reader._read` to reduce code reutilisation and make code more robust. The `part` function now takes `height` and `width` instead of a unique `tilesize` to specify the output array size. 

To ease the transition we added `rio_tiler.reader.tile` function.

Note: The new `rio_tiler.reader.part` function enables to perform non-squared data cropping of different.

```python
# v1
with rasterio.open("my_tif.tif") as src_dst:
    # get tile bounds and read raster
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    t, m = rio_tiler.utils._tile_read(src, tile_bounds, 256)


# v2
with rasterio.open("my_tif.tif") as src_dst:
    t, m = rio_tiler.reader.tile(src_dst, tile_x, tile_y, tile_z, 256) # Will check if tile is valid

# Or
with rasterio.open("my_tif.tif") as src_dst:
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    t, m = rio_tiler.reader.part(src_dst, tile_bounds, 256, 256)
```

*Options changes*
- `tile_edge_padding` -> `padding`, and set to **0** by default
- `minimum_tile_cover` -> `minimum_overlap`
- `unscale` (**New**): add ability to apply scale and offset to the data (Default: False)

```python
# v1
with rasterio.open("my_tif.tif") as src_dst:
    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)
    t, m = rio_tiler.utils._tile_read(src, tile_bounds, 256, tile_edge_padding=4, minimum_tile_cover=0.3)

# v2
with rasterio.open("my_tif.tif") as src_dst:
    t, m = rio_tiler.reader.tile(src_dst, tile_x, tile_y, tile_z, 256, padding=4, minimum_overlap=0.3)
```

### metadata

`rio_tiler.utils._raster_get_stats` has been replace by `rio_tiler.reader.metadata` which uses the new `reader.part` and `reader.preview` functions. Meaning that now you can get metadata for a specific area by passing a bbox. To limit the data transfer (with the idea of getting the metadata from the COG overviews) we uses only the `max_size` options, meaning the `overview_level` options has been removed (at least for version 2.0.0).

```python
# v1 
import rio_tiler
with rasterio.open("my_tif.tif") as src_dst:
    meta = rio_tiler.utils._raster_get_stats(src_dst)

# v2
with rasterio.open("my_tif.tif") as src_dst: 
    rio_tiler.reader.metadata(src_dst)
```

*Options changes*
- removed `histogram_bins` and `histogram_range` which should now be passed in `hist_options` (e.g: hist_options={bins=10, range=(0, 10)})
- removed `overview_level`
- added `bounds`

*Output*

The output has also been updated. The new `metadata` output doesn't 
return min/max zoom and bounds is return in WGS84 by default.


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
            "pc": [1, 16],
            "min": 1,
            "max": 18,
            "std": 4.069636227214257,
            "histogram": [
                [...],
                [...]
            ]
        }
    },
    "band_descriptions": [[1, "band1"]],
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
In addition to a new colormap specific submodule (`rio_tiler.colormap`), in *rio-tiler==2*, colormaps are now RGBA values.

We also removed `PIL` colormap compatibility.

```python
# v1
cmap = rio_tiler.utils.get_colormap("viridis", format="gdal")
print(cmap[0])
> [68, 1, 84]

# v2
cmap = rio_tiler.colormap.get_colormap("viridis")
print(cmap[0])
> [68, 1, 84, 255]
```

## render

In *rio-tiler==1.** to create image blob from an array we used `rio_tiler.utils.array_to_image` function. We have renamed and slightly refactor the function but it works the same.

```python
# v1
img = rio_tiler.utils.array_to_image(tile, mask, img_format="PNG")

# v2
img = rio_tiler.utils.render(tile, mask, img_format="PNG")
```

## Mission specific changes

Each `rio_tiler.io.{mission}` **scene id parsers** (e.g cbers_parser) have been refactored and now return aws s3 path information.

```python
rio_tiler.io.landsat8.landsat_parser("LC08_L1TP_016037_20170813_20170814_01_RT")) 
{
    "sensor": "C",
    "satellite": "08",
    "processingCorrectionLevel": "L1TP",
    "path": "016",
    "row": "037",
    "acquisitionYear": "2017",
    "acquisitionMonth": "08",
    "acquisitionDay": "13",
    "processingYear": "2017",
    "processingMonth": "08",
    "processingDay": "14",
    "collectionNumber": "01",
    "collectionCategory": "RT",
    "scene": "LC08_L1TP_016037_20170813_20170814_01_RT",
    "date": "2017-08-13",
--> "scheme": "s3",
--> "bucket": "landsat-pds",
--> "prefix": "c1/L8/016/037/LC08_L1TP_016037_20170813_20170814_01_RT"
}
```