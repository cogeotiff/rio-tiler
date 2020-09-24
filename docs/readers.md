
### COGReader

<details>

```python
class COGReader:
    """
    Cloud Optimized GeoTIFF Reader.

    Examples
    --------
    with COGReader(src_path) as cog:
        cog.tile(...)

    # Set global options
    with COGReader(src_path, unscale=True, nodata=0) as cog:
        cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with WarpedVRT(src_dst, ...) as vrt_dst:
            with COGReader(None, dataset=vrt_dst) as cog:
                cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with COGReader(None, dataset=src_dst) as cog:
            cog.tile(...)

    Attributes
    ----------
    filepath: str
        Cloud Optimized GeoTIFF path.
    dataset: rasterio.DatasetReader, optional
        Rasterio dataset.

    Properties
    ----------
    minzoom: int
        COG minimum zoom level.
    maxzoom: int
        COG maximum zoom level.
    bounds: tuple[float]
        COG bounds in WGS84 crs.
    center: tuple[float, float, int]
        COG center + minzoom
    colormap: dict
        COG internal colormap.

    Methods
    -------
    tile(0, 0, 0, indexes=(1,2,3), expression="B1/B2", tilesize=512, resampling_methods="nearest")
        Read a map tile from the COG.
    part((0,10,0,10), indexes=(1,2,3,), expression="B1/B20", max_size=1024)
        Read part of the COG.
    preview(max_size=1024)
        Read preview of the COG.
    point((10, 10), indexes=1)
        Read a point value from the COG.
    info: dict
        General information about the COG (datatype, indexes, ...)
    stats(pmin=5, pmax=95)
        Get Raster statistics.
    meta(pmin=5, pmax=95)
        Get info + raster statistics
    """
```

</details>

#### Properties

- **dataset**: Return the rasterio dataset
- **colormap**: Return the dataset's internal colormap
- **minzoom**: Return minimum Mercator Zoom
- **maxzoom**: Return maximum Mercator Zoom
- **bounds**: Return the dataset bounds in WGS84
- **center**: Return the center of the dataset + minzoom
- **spatial_info**: Return the bounds, center and zoom infos

#### Methods

- **tile()**: Read map tile from a raster

```python
with COGReader("myfile.tif") as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256)

# With indexes
with COGReader("myfile.tif") as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256, indexes=1)

# With expression
with COGReader("myfile.tif"s) as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256, expression="B1/B2")
```

- **part()**: Read part of a raster

```python
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20))

# Limit output size (default is set to 1024)
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), max_size=2000)

# Read high resolution
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), max_size=None)

# With indexes
with COGReader("myfile.tif") as cog:
     data, mask = cog.part((10, 10, 20, 20), indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), expression="B1/B2")
```

- **preview()**: Read a preview of a raster

```python
with COGReader("myfile.tif") as cog:
    data, mask = cog.preview()

# With indexes
with COGReader("myfile.tif") as cog:
    data, mask = cog.preview(indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    data, mask = cog.preview(expression="B1+2,B1*4")
```

- **point()**: Read point value of a raster

```python
with COGReader("myfile.tif") as cog:
    print(cog.point(-100, 25))

# With indexes
with COGReader("myfile.tif") as cog:
    print(cog.point(-100, 25, indexes=1))
[1]

# With expression
with COGReader("myfile.tif") as cog:
    print(cog.point(-100, 25, expression="B1+2,B1*4"))
[3, 4]
```

- **info()**: Return simple metadata about the dataset

```python
with COGReader("myfile.tif") as cog:
    print(cog.info())
{
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "center": [-101.98868496889182, 23.548959503763047, 3],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [[1, {}]],
    "band_descriptions": [[1,"band1"]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "nodata_type": "Nodata",
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255],
        ...
    }
}
```

- **stats()**: Return image statistics (Min/Max/Stdev)

```python
with COGReader("myfile.tif") as cog:
    print(cog.stats())
{
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
}
```

- **metadata()**: Return COG info + statistics

```python
with COGReader("myfile.tif") as cog:
    print(cog.metadata())
{
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "center": [-101.98868496889182, 23.548959503763047, 3],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [[1, {}]],
    "band_descriptions": [[1,"band1"]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "nodata_type": "Nodata",
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255],
        ...
    }
    "statistics" : {
        1: {
            "pc": [1, 16],
            "min": 1,
            "max": 18,
            "std": 4.069636227214257,
            "histogram": [
                [...],
                [...]
            ]
        }
    }
}
```

##### Global Options

COGReader accept several options which will be forwarded to the `rio_tiler.reader._read` function (low level function accessing the data):
- `nodata`: Overwrite the nodata value (or set if not present)
- `unscale`: Apply internal rescaling factors
- `vrt_options`: Pass WarpedVRT Option (see: https://gdal.org/api/gdalwarp_cpp.html?highlight=vrt#_CPPv415GDALWarpOptions)
- `resampling_method`: Set default `resampling_method`

Note: Those options could already be passed on each `method` call.

```python
with COGReader("my_cog.tif", nodata=0) as cog:
    tile, mask = cog.tile(1, 1, 1)

# is equivalent to

with COGReader("my_cog.tif") as cog:
    tile, mask = cog.tile(1, 1, 1, nodata=0)
```

### STACReader

In rio-tiler v2, we added a `rio_tiler.io.STACReader` to allow tile/metadata fetching of assets withing a STAC item. The STACReader objects has the same properties/methods as the COGReader.

```python
from typing import Dict
from rio_tiler.io import STACReader

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    print(stac.bounds)
    print(stac.assets)

> [23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106]
> ['overview', 'visual', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12', 'AOT', 'WVP', 'SCL']

# Name of assets to read
assets = ["B01", "B02"]

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    tile, mask = stac.tile(145, 103, 8, tilesize=256, assets=assets)

print(tile.shape)
> (2, 256, 256)

# With expression
with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    tile, mask = stac.tile(145, 103, 8, tilesize=256, expression="B01/B02")

print(tile.shape)
> (1, 256, 256)
```

Note: STACReader is based on `rio_tiler.io.base.MultiBaseReader` class.
