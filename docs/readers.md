
`rio-tiler`'s  COGReader and STACReader are built from its abstract base classes (`AsyncBaseReader`, `BaseReader`, `MultiBandReader`, `MultiBaseReader`). Thoses Classes implements defaults interfaces which helps the integration in broder application. To learn more about `rio-tiler`'s base classes see [Base classes and custom readers](advanced/custom_readers.md)

## rio_tiler.io.COGReader

The `COGReader` is designed to work with simple raster datasets (e.g COG, GeoTIFF, ...).

The class is derieved from the `rio_tiler.io.base.BaseReader` base class.
```python
from rio_tiler.io import COGReader

COGReader.__mro__
>>> (rio_tiler.io.cogeo.COGReader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Properties

- **dataset**: rasterio openned dataset
- **tms**: morecantile TileMatrixSet used for tile reading
- **minzoom**: dataset's minimum zoom level (for input tms)
- **maxzoom**: dataset's maximum zoom level (for input tms)
- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84
- **colormap**: dataset's internal colormap


```python
from rio_tiler.io import COGReader

with COGReader("myfile.tif") as cog:
    print(cog.dataset)
    print(cog.tms.identifier)
    print(cog.minzoom)
    print(cog.maxzoom)
    print(cog.bounds)
    print(cog.crs)
    print(cog.geographic_bounds)
    print(cog.colormap)

>> <open DatasetReader name='myfile.tif' mode='r'>
WebMercatorQuad
16
22
(683715.3266400001, 1718548.5702, 684593.2680000002, 1719064.90736)
EPSG:32620
(-61.287001876638215, 15.537756794450583, -61.27877967704677, 15.542486503997608)
{}
```

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
    assert img.count == 1

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.read(expression="B1/B2")
    assert img.count == 1
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
    assert img.count == 1

# With expression
with COGReader("myfile.tif") as cog:
    img = cog.tile(1, 2, 3, tilesize=256, expression="B1/B2")
    assert img.count == 1

# Using buffer
# Sometime, to avoid edge artefacts, you may want to read buffered tile data.
# ref:
# - https://github.com/cogeotiff/rio-tiler/issues/365
# - https://github.com/cogeotiff/rio-tiler/pull/405
with COGReader("myfile.tif") as cog:
    # add 0.5 pixel on each side of the tile
    img = cog.tile(1, 2, 3, tile_buffer=0.5)
    assert img.width == 257
    assert img.height == 257

    # add 1 pixel on each side of the tile
    img = cog.tile(1, 2, 3, tile_buffer=1)
    assert img.width == 258
    assert img.height == 258
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
    stats = cog.statistics()
    assert isinstance(stats, dict)

# stats will be in form or {"band": BandStatistics(), ...}
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

## rio_tiler.io.STACReader

In `rio-tiler` v2, we added a `rio_tiler.io.STACReader` to allow tile/metadata fetching of assets withing a STAC item.

The class is derieved from the `rio_tiler.io.base.MultiBaseReader` base class which help handling responses from multiple `BaseReader` (each asset will be read with a `BaseReader`).
```python
from rio_tiler.io import STACReader

STACReader.__mro__
>>> (rio_tiler.io.stac.STACReader,
 rio_tiler.io.base.MultiBaseReader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Properties

- **filepath**: STAC Item path, URL or S3 URL
- **item**: PySTAC item
- **assets**: Asset list.
- **tms**: morecantile TileMatrixSet used for tile reading
- **minzoom**: dataset's minimum zoom level (for input tms)
- **maxzoom**: dataset's maximum zoom level (for input tms)
- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84

```python
from rio_tiler.io import STACReader

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    print(stac.filepath)
    print(stac.item)
    print(stac.assets)
    print(stac.tms.identifier)
    print(stac.minzoom)
    print(stac.maxzoom)
    print(stac.bounds)
    print(stac.crs)
    print(stac.geographic_bounds)

>>> https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A
<Item id=S2A_34SGA_20200318_0_L2A>
['overview', 'visual', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12', 'AOT', 'WVP', 'SCL']
WebMercatorQuad
0
24
[23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106]
EPSG:4326
(23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106)
```

#### Methods

The `STACReader` as the same methods as the `COGReader` (defined by the BaseReader/MultiBaseReader classes).

!!! important
    `STACReader` methods require to set either `assets=` or `expression=` option.

- **tile()**: Read map tile from a STAC Item

```python
from rio_tiler.io import STACReader

stac_url = "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A"

# Using `assets=`
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.tile(x, y, z, assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        assets=["B01", "B02"],
    )
    assert img.count == 2  # each assets have one band

print(img.assets)
>>> [
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B01.tif',
    'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/34/S/GA/2020/3/S2A_34SGA_20200318_0_L2A/B02.tif',
]
print(img.band_names)
>>> ['B01_1', 'B02_1']

# Using `expression=`
with STACReader(stac_url, exclude_assets={"thumbnail"}) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        expression="B01/B02",
    )
    assert img.count == 1


# Using `assets=` + `asset_expression` (apply band math in an asset)
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        assets=["B01", "B02"],
        asset_expression={
            "B01": "b1+500",  # add 500 to the first band
            "B02": "b1-100",  # substract 100 to the first band
        }
    )
    assert img.count == 2

# Using `assets=` + `asset_indexes` (select a specific index in an asset)
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        assets=["B01"],
        asset_indexes={
            "B01": (1, 1, 1),  # return the first band 3 times
        }
    )
    assert img.count == 3
```

`asset_indexes` and `asset_expression` are available for all STACReader methods expect `info`.


- **part()**: Read a STAC item for a given bounding box (`bbox`). By default the bbox is considered to be in WGS84.

```python
bbox = (23.8, 31.9, 24.1, 32.2)
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.part((minx, miny, maxx, maxy), assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    img = stac.part(bbox, assets=["B01", "B02"], max_size=128)
    assert img.count == 2  # each assets have one band
```

- **feature()**: Read a STAC item for a geojson feature. By default the feature is considered to be in WGS84.

```python
feat = {
    "type": "Feature",
    "geometry": {
        "coordinates": [
            [
                [23.8, 32.2],
                [23.8, 31.9],
                [24.1, 31.9],
                [24.1, 32.2],
                [23.8, 32.2]
            ]
        ],
        "type": "Polygon"
    }
}
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.feature(feature, assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    img = stac.feature(feat, assets=["B01", "B02"], max_size=128)
    assert img.count == 2  # each assets have one band
```

- **preview()**: Read a preview of STAC Item

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.preview(assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    img = stac.preview(assets=["B01", "B02"], max_size=128)
    assert img.count == 2  # each assets have one band
```

- **point()**: Read the pixel values for assets for a given `lon, lat` coordinates. By default the coordinates are considered to be in WGS84.

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.point(lon, lat, assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    data = stac.point(24.1, 31.9, assets=["B01", "B02"])

print(data)
>>> [
    [3595],  # values for B01
    [3198]  # values for B02
]
```

- **info()**: Return simple metadata about the assets

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.info(assets=?, **kwargs)
    info = stac.info(assets=["B01", "B02"])

print(list(info))
>>> ["B01", "B02"]

print(info["B01"].json(exclude_none=True))
>>> {
    "bounds": [23.106076243528157, 31.505173744374172, 24.296464503939948, 32.519334871696195],
    "minzoom": 8,
    "maxzoom": 11,
    "band_metadata": [["1", {}]],
    "band_descriptions": [["1", ""]],
    "dtype": "uint16",
    "nodata_type": "Nodata",
    "colorinterp": ["gray"],
    "nodata_value": 0.0,
    "width": 1830,
    "driver": "GTiff",
    "height": 1830,
    "overviews": [2, 4, 8],
    "count": 1
}
```

- **statistics()**: Return image statistics (Min/Max/Stdev)

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.statistics(assets=?, asset_expression=?, asset_indexes=?, **kwargs)
    stats = stac.statistics(assets=["B01", "B02"], max_size=128)

# stats will be in form or {"asset": {"band": BandStatistics(), ...}, ...}
print(list(info))
>>> ["B01", "B02"]

print(list(info["B01"]))
>>> ["1"]  # B01 has only one band entry "1"

print(info["B01"]["1"].json(exclude_none=True))
{
    "min": 283.0,
    "max": 7734.0,
    "mean": 1996.959687371452,
    "count": 12155.0,
    "sum": 24273045.0,
    "std": 1218.4455268717047,
    "median": 1866.0,
    "majority": 322.0,
    "minority": 283.0,
    "unique": 4015.0,
    "histogram": [
        [3257.0, 2410.0, 2804.0, 1877.0, 1050.0, 423.0, 199.0, 93.0, 31.0, 11.0],
        [283.0, 1028.1, 1773.2, 2518.3, 3263.4, 4008.5, 4753.6, 5498.7, 6243.8, 6988.900000000001, 7734.0]
    ],
    "valid_percent": 74.19,
    "masked_pixels": 4229.0,
    "valid_pixels": 12155.0,
    "percentile_2": 326.08000000000004,
    "percentile_98": 5026.76
}
```
