
## COGReader

#### Properties

- **dataset**: rasterio openned dataset
- **tms**: morecantile TileMatrixSet used for tile reading
- **minzoom**: dataset's minimum zoom level (for input tms)
- **maxzoom**: dataset's maximum zoom level (for input tms)
- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84
- **colormap**: dataset's internal colormap

#### Methods

- **read()**: Read the entire dataset

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("myfile.tif") as cog:
    img = cog.read()
    assert isinstance(img, ImageData)
    assert img.crs == cog.dataset.crs
    assert img.assets == ["myfile.tif"]
    assert img.width == cog.dataset.width
    assert img.height == cog.dataset.height
    assert img.count == cog.dataset.count

# With indexes
with COGReader("myfile.tif") as cog:
    img = cog.read(indexes=1)  # or cog.read(indexes=(1,))
    assert img.data.count == 1

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.read(expression="B1/B2")
    assert img.data.count == 1
```

- **tile()**: Read map tile from a raster

```python
from rio_tiler.contants import WEB_MERCATOR_CRS
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("myfile.tif") as cog:
    # cog.tile(tile_x, tile_y, tile_z, **kwargs)
    img = cog.tile(1, 2, 3, tilesize=256)
    assert isinstance(img, ImageData)
    assert img.crs == WEB_MERCATOR_CRS
    assert img.assets == ["myfile.tif"]

# With indexes
with COGReader("myfile.tif") as cog:
    img = cog.tile(1, 2, 3, tilesize=256, indexes=1)
    assert img.data.count == 1

# With expression
with COGReader("myfile.tif"s) as cog:
    img = cog.tile(1, 2, 3, tilesize=256, expression="B1/B2")
    assert img.data.count == 1
```

- **part()**: Read a raster for a given bounding box (`bbox`). By default the bbox is considered to be in WGS84.

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("myfile.tif") as cog:
    # cog.part((minx, miny, maxx, maxy), **kwargs)
    img = cog.part((10, 10, 20, 20))
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.assets == ["myfile.tif"]
    assert img.bounds == (10, 10, 20, 20)

# Pass bbox in WGS84 (default) but return data in the input COG CRS
with COGReader("myfile.tif") as cog:
    img = cog.part((10, 10, 20, 20), dst_crs=cog.dataset.crs)
    assert img.crs == cog.dataset.crs

# Limit output size
with COGReader("myfile.tif") as cog:
    img = cog.part((10, 10, 20, 20), max_size=2000)

# With indexes
with COGReader("myfile.tif") as cog:
    img = cog.part((10, 10, 20, 20), indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.part((10, 10, 20, 20), expression="B1/B2")
```

- **feature()**: Read a raster for a geojson feature. By default the feature is considered to be in WGS84.

```python
from rio_tiler.constants import WGS84_CRS
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

feat = {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-54.45, 73.05],
                [-55.05, 72.79],
                [-55.61, 72.46],
                [-53.83, 72.36],
                [-54.45, 73.05],
            ]
        ],
    },
}

with COGReader("myfile.tif") as cog:
    # cog.part(geojson_feature, **kwargs)
    img = cog.feature(feat)
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.assets == ["myfile.tif"]
    assert img.bounds == (-55.61, 72.36, -53.83, 73.05)  # bbox of the input feature

# Pass bbox in WGS84 (default) but return data in the input COG CRS
with COGReader("myfile.tif") as cog:
    img = cog.feature(feat, dst_crs=cog.dataset.crs)
    assert img.crs == cog.dataset.crs

# Limit output size
with COGReader("myfile.tif") as cog:
    img = cog.feature(feat, max_size=2000)

# Read high resolution
with COGReader("myfile.tif") as cog:
    img = cog.feature(feat, max_size=None)

# With indexes
with COGReader("myfile.tif") as cog:
    img = cog.feature(feat, indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.feature(feat, expression="B1/B2")
```

- **preview()**: Read a preview of a raster

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("myfile.tif") as cog:
    img = cog.preview()
    assert isinstance(img, ImageData)

# With indexes
with COGReader("myfile.tif") as cog:
    img = cog.preview(indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.preview(expression="B1+2,B1*4")
```

- **point()**: Read the pixel values of a raster for a given `lon, lat` coordinates. By default the coordinates are considered to be in WGS84.

```python
from rio_tiler.io import COGReader

with COGReader("myfile.tif") as cog:
    # cog.point(lon, lat)
    print(cog.point(-100, 25))

# With indexes
with COGReader("myfile.tif") as cog:
    print(cog.point(-100, 25, indexes=1))
>>> [1]

# With expression
with COGReader("myfile.tif") as cog:
    print(cog.point(-100, 25, expression="B1+2,B1*4"))
>>> [3, 4]
```

- **info()**: Return simple metadata about the dataset

```python
from rio_tiler.io import COGReader
from rio_tiler.models import Info

with COGReader("myfile.tif") as cog:
    info = cog.info()
    assert isinstance(info, Info)

print(info.dict(exclude_none=True))
>>> {
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [["1", {}]],
    "band_descriptions": [["1", ""]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "nodata_type": "Nodata",
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255],
        ...
    },
    "driver": "GTiff",
    "count": 1,
    "width": 1000,
    "height": 2000,
    "overviews": [2, 4, 8],
}
```

- **statistics()**: Return image statistics (Min/Max/Stdev)

```python
from rio_tiler.io import COGReader

with COGReader("myfile.tif") as cog:
    # cog.stats(**kwargs)
    stats = cog.statistics()
    assert isinstance(stats, dict)

print(stats)
>>> {
    '1': BandStatistics(...),
    '2': BandStatistics(...),
    '3': BandStatistics(...)
}

print(stats["1"].dict())
>>> {
    "min": 1,
    "max": 7872,
    "mean": 2107.524612053134,
    "count": 1045504,
    "sum": 2203425412,
    "std": 2271.0065537857326,
    "median": 2800,
    "majority": 1,
    "minority": 7072,
    "unique": 15,
    "histogram": [
        [...],
        [...]
    ],
    "valid_percent": 100,
    "masked_pixels": 0,
    "valid_pixels": 1045504,
    "percentile_98": 6896,
    "percentile_2": 1
}

with COGReader("myfile_with_colormap.tif") as cog:
    # cog.stats(**kwargs)
    stats = cog.statistics(categorical=True, categories=[1, 2])  # we limit the categories to 2 defined value (defaults to all dataset values)
    assert isinstance(stats, dict)

print(stats)
>>> {
    '1': BandStatistics(...)
}
# For categorical data, the histogram will represent the density of EACH value.
print(stats["1"].dict())
>>> {
    ...
    "histogram": [
        [1, 2],
        [100, 20000]
    ],
    ...
}
```

#### Read Options

`COGReader` accepts several options which will be forwarded to the `rio_tiler.reader.read` function (low level function accessing the data), those options can be set as reader's attribute or within each method calls:

- **nodata**: Overwrite the nodata value (or set if not present)
- **unscale**: Apply internal rescaling factors
- **vrt_options**: Pass WarpedVRT Option (see: https://gdal.org/api/gdalwarp_cpp.html?highlight=vrt#_CPPv415GDALWarpOptions)
- **resampling_method**: Set default `resampling_method`
- **post_process**: Function to apply after the read operations

```python
with COGReader("my_cog.tif", nodata=0) as cog:
   cog.tile(1, 1, 1)

# is equivalent to

with COGReader("my_cog.tif") as cog:
    cog.tile(1, 1, 1, nodata=0)
```

## STACReader

In `rio-tiler` v2, we added a `rio_tiler.io.STACReader` to allow tile/metadata fetching of assets withing a STAC item. The STACReader objects has the same properties/methods as the COGReader.

```python
from typing import Dict
from rio_tiler.io import STACReader

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    print(stac.bounds)
    print(stac.geographic_bounds)
    print(stac.assets)

>>> [23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106]
>>> [23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106]
>>> ['overview', 'visual', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12', 'AOT', 'WVP', 'SCL']

# Name of assets to read
assets = ["B01", "B02"]

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    img = stac.tile(145, 103, 8, tilesize=256, assets=assets)

print(img.assets)
>>> [
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B01.tif',
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B02.tif'
]

print(img.data.shape)
>>> (2, 256, 256)

# With expression
with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    img = stac.tile(145, 103, 8, tilesize=256, expression="B01/B02")

print(img.assets)
>>> [
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B01.tif',
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B02.tif'
]

print(img.data.shape)
>>> (1, 256, 256)
```

Note: `STACReader` is based on `rio_tiler.io.base.MultiBaseReader` class.
