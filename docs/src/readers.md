
`rio-tiler`'s  Reader are built from its abstract base classes (`BaseReader`, `MultiBandReader`, `MultiBaseReader`). Those Classes implements defaults interfaces which helps the integration in broader application. To learn more about `rio-tiler`'s base classes see [Base classes and custom readers](advanced/custom_readers.md)

## rio_tiler.io.rasterio.Reader

The `Reader` is designed to work with simple raster datasets (e.g COG, GeoTIFF, ...).

The class is derived from the `rio_tiler.io.base.BaseReader` base class.
```python
from rio_tiler.io import Reader

Reader.__mro__
>>> (rio_tiler.io.rasterio.Reader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Attributes

- **input** (str): filepath
- **dataset** (rasterio dataset, optional): rasterio opened dataset
- **tms** (morecantile.TileMatrixSet, optional): morecantile TileMatrixSet used for tile reading (defaults to WebMercator)
- **geographic_crs** (rasterio.crs.CRS, optional): CRS to use to calculate the geographic bounds (default to WGS84)
- **colormap** (dict, optional): dataset's colormap
- **options** (rio_tiler.reader.Options, optional): Options to forward to rio_tiler.reader functions (e.g nodata, vrt_options, resampling)

#### Properties

- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84
- **minzoom**: dataset minzoom (in TMS)
- **maxzoom**: dataset maxzoom (in TMS)

```python
from rio_tiler.io import Reader

with Reader("myfile.tif") as src:
    print(src.dataset)
    print(src.tms.identifier)
    print(src.minzoom)
    print(src.maxzoom)
    print(src.bounds)
    print(src.crs)
    print(src.geographic_bounds)
    print(src.colormap)

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
from rio_tiler.io import Reader
from rio_tiler.models import ImageData

with Reader("myfile.tif") as src:
    img = src.read()
    assert isinstance(img, ImageData)
    assert img.crs == src.dataset.crs
    assert img.assets == ["myfile.tif"]
    assert img.width == src.dataset.width
    assert img.height == src.dataset.height
    assert img.count == src.dataset.count

# With indexes
with Reader("myfile.tif") as src:
    img = src.read(indexes=1)  # or src.read(indexes=(1,))
    assert img.count == 1
    assert img.band_names == ["b1"]

# With expression
with Reader("myfile.tif") as src:
    img = src.read(expression="b1/b2")
    assert img.count == 1
    assert img.band_names == ["b1/b2"]
```

- **tile()**: Read map tile from a raster

```python
from rio_tiler.contants import WEB_MERCATOR_CRS
from rio_tiler.io import Reader
from rio_tiler.models import ImageData

with Reader("myfile.tif") as src:
    # src.tile(tile_x, tile_y, tile_z, **kwargs)
    img = src.tile(1, 2, 3, tilesize=256)
    assert isinstance(img, ImageData)
    assert img.crs == WEB_MERCATOR_CRS
    assert img.assets == ["myfile.tif"]

# With indexes
with Reader("myfile.tif") as src:
    img = src.tile(1, 2, 3, tilesize=256, indexes=1)
    assert img.count == 1

# With expression
with Reader("myfile.tif") as src:
    img = src.tile(1, 2, 3, tilesize=256, expression="B1/B2")
    assert img.count == 1

# Using buffer
# Sometime, to avoid edge artefacts, you may want to read buffered tile data.
# ref:
# - https://github.com/cogeotiff/rio-tiler/issues/365
# - https://github.com/cogeotiff/rio-tiler/pull/405
with Reader("myfile.tif") as src:
    # add 0.5 pixel on each side of the tile
    img = src.tile(1, 2, 3, buffer=0.5)
    assert img.width == 257
    assert img.height == 257

    # add 1 pixel on each side of the tile
    img = src.tile(1, 2, 3, buffer=1)
    assert img.width == 258
    assert img.height == 258
```

- **part()**: Read a raster for a given bounding box (`bbox`). By default the bbox is considered to be in WGS84.

```python
from rio_tiler.io import Reader
from rio_tiler.models import ImageData

with Reader("myfile.tif") as src:
    # src.part((minx, miny, maxx, maxy), **kwargs)
    img = src.part((10, 10, 20, 20))
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.assets == ["myfile.tif"]
    assert img.bounds == (10, 10, 20, 20)

# Pass bbox in WGS84 (default) but return data in the input dataset CRS
with Reader("myfile.tif") as src:
    img = src.part((10, 10, 20, 20), dst_crs=src.dataset.crs)
    assert img.crs == src.dataset.crs

# Limit output size
with Reader("myfile.tif") as src:
    img = src.part((10, 10, 20, 20), max_size=2000)

# With indexes
with Reader("myfile.tif") as src:
    img = src.part((10, 10, 20, 20), indexes=1)

# With expression
with Reader("myfile.tif") as src:
    img = src.part((10, 10, 20, 20), expression="b1/b2")
```

- **feature()**: Read a raster for a geojson feature. By default the feature is considered to be in WGS84.

```python
from rio_tiler.constants import WGS84_CRS
from rio_tiler.io import Reader
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

with Reader("myfile.tif") as src:
    # src.part(geojson_feature, **kwargs)
    img = src.feature(feat)
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.assets == ["myfile.tif"]
    assert img.bounds == (-55.61, 72.36, -53.83, 73.05)  # bbox of the input feature

# Pass bbox in WGS84 (default) but return data in the input dataset CRS
with Reader("myfile.tif") as src:
    img = src.feature(feat, dst_crs=src.dataset.crs)
    assert img.crs == src.dataset.crs

# Limit output size
with Reader("myfile.tif") as src:
    img = src.feature(feat, max_size=2000)

# Read high resolution
with Reader("myfile.tif") as src:
    img = src.feature(feat, max_size=None)

# With indexes
with Reader("myfile.tif") as src:
    img = src.feature(feat, indexes=1)

# With expression
with Reader("myfile.tif") as src:
    img = src.feature(feat, expression="b1/b2")
```

- **preview()**: Read a preview of a raster

```python
from rio_tiler.io import Reader
from rio_tiler.models import ImageData

with Reader("myfile.tif") as src:
    img = src.preview()
    assert isinstance(img, ImageData)

# With indexes
with Reader("myfile.tif") as src:
    img = src.preview(indexes=1)

# With expression
with Reader("myfile.tif") as src:
    img = src.preview(expression="b1+2;b1*4")
```

- **point()**: Read the pixel values of a raster for a given `lon, lat` coordinates. By default the coordinates are considered to be in WGS84.

```python
from rio_tiler.io import Reader
from rio_tiler.models import PointData

with Reader("myfile.tif") as src:
    # src.point(lon, lat)
    pt = src.point(-100, 25)
    assert isinstance(pt, PointData)

# With indexes
with Reader("myfile.tif") as src:
    pt = src.point(-100, 25, indexes=1)
    print(pt.data)
>>> [1]

# With expression
with Reader("myfile.tif") as src:
    pt = src.point(-100, 25, expression="b1+2;b1*4")
    print(pt.data)
>>> [3, 4]
```

- **info()**: Return simple metadata about the dataset

```python
from rio_tiler.io import Reader
from rio_tiler.models import Info

with Reader("myfile.tif") as src:
    info = src.info()
    assert isinstance(info, Info)

print(info.model_dump(exclude_none=True))
>>> {
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [["b1", {}]],
    "band_descriptions": [["b1", ""]],
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
from rio_tiler.io import Reader

with Reader("myfile.tif") as src:
    stats = src.statistics()
    assert isinstance(stats, dict)

# stats will be in form or {"band": BandStatistics(), ...}
print(stats)
>>> {
    'b1': BandStatistics(...),
    'b2': BandStatistics(...),
    'b3': BandStatistics(...)
}

print(stats["b1"].model_dump())
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

with Reader("myfile_with_colormap.tif") as src:
    stats = src.statistics(categorical=True, categories=[1, 2])  # we limit the categories to 2 defined value (defaults to all dataset values)
    assert isinstance(stats, dict)

print(stats)
>>> {
    'b1': BandStatistics(...)
}
# For categorical data, the histogram will represent the density of EACH value.
print(stats["b1"].model_dump())
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

`Reader` accepts several input options which will be forwarded to the `rio_tiler.reader.read` function (low level function accessing the data), those options can be set as reader's attribute or within each method calls:

- **nodata**: Overwrite the nodata value (or set if not present)
- **unscale**: Apply internal rescaling factors
- **vrt_options**: Pass WarpedVRT Option (see: https://gdal.org/api/gdalwarp_cpp.html?highlight=vrt#_CPPv415GDALWarpOptions)
- **resampling_method**: Set default `resampling_method`
- **reprojection_method**: Set default `reprojection_method`
- **post_process**: Function to apply after the read operations

```python
with Reader("my_cog.tif", options={"nodata": 0}) as src:
   src.tile(1, 1, 1)

# is equivalent to

with Reader("my_cog.tif") as src:
    src.tile(1, 1, 1, nodata=0)
```

## rio_tiler.io.stac.STACReader

In `rio-tiler` v2, we added a `rio_tiler.io.STACReader` to allow tile/metadata fetching of assets withing a STAC item.

The class is derived from the `rio_tiler.io.base.MultiBaseReader` base class which help handling responses from multiple `BaseReader` (each asset will be read with a `BaseReader`).
```python
from rio_tiler.io import STACReader

STACReader.__mro__
>>> (rio_tiler.io.stac.STACReader,
 rio_tiler.io.base.MultiBaseReader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Attributes

- **input** (str): STAC Item path, URL or S3 URL
- **item**: PySTAC item
- **tms** (morecantile.TileMatrixSet, optional): morecantile TileMatrixSet used for tile reading (defaults to WebMercator)
- **minzoom** (int, optional): dataset's minimum zoom level (for input tms)
- **maxzoom** (int, optional): dataset's maximum zoom level (for input tms)
- **geographic_crs** (rasterio.crs.CRS, optional): CRS to use to calculate the geographic bounds (default to WGS84)
- **include_assets** (set, optional): Set of assets to include from the `available` asset list
- **exclude_assets** (set, optional): Set of assets to exclude from the `available` asset list
- **include_asset_types** (set, optional): asset types to consider as valid type for the reader
- **exclude_asset_types** (set, optional): asset types to consider as invalid type for the reader
- **reader** (BaseReader, optional): Reader to use to read assets (defaults to rio_tiler.io.rasterio.Reader)
- **reader_options** (dict, optional): Options to forward to the reader init
- **fetch_options** (dict, optional): Options to pass to the `httpx.get` or `boto3` when fetching the STAC item

#### Properties

- **assets**: Asset list.
- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84

```python
from rio_tiler.io import STACReader

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A",
    exclude_assets={"thumbnail"}
) as stac:
    print(stac.input)
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

The `STACReader` has the same methods as the `Reader` (defined by the BaseReader/MultiBaseReader classes).

!!! Important
    - Most of `STACReader` methods require to set either `assets=` or `expression=` option.
    - `asset_indexes` and `asset_expression` are available for all STACReader methods except `info`.

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
>>> ['B01_b1', 'B02_b1']

# Using `expression=`
with STACReader(stac_url, exclude_assets={"thumbnail"}) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        expression="B01_b1/B02_b1",
    )
    assert img.count == 1

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

- **point()**: Read the pixel values for assets for a given `lon, lat` coordinates. By default the coordinates are considered to be in WGS84.

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.point(lon, lat, assets=?, expression=?, asset_expression=?, asset_indexes=?, **kwargs)
    data = stac.point(24.1, 31.9, assets=["B01", "B02"])

print(data.data)
>>> [
    3595,  # values for B01
    3198  # values for B02
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
    "band_metadata": [["b1", {}]],
    "band_descriptions": [["b1", ""]],
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

- **statistics()**: Return per assets statistics (Min/Max/Stdev)

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.statistics(assets=?, asset_expression=?, asset_indexes=?, **kwargs)
    stats = stac.statistics(assets=["B01", "B02"], max_size=128)

# stats will be in form or {"asset": {"band": BandStatistics(), ...}, ...}
print(list(stats))
>>> ["B01", "B02"]

print(list(stats["B01"]))
>>> ["b1"]  # B01 has only one band entry "1"

print(stats["B01"]["b1"].json(exclude_none=True))
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

- **merged_statistics()**: Return statistics when merging assets

The `merged_statistics` enable the use of `expression` to perform assets mixing (e.g `"asset1/asset2"`). The main difference with the `statistics` method is that we will first use the `self.preview` method to obtain a merged array and then calculate the statistics.

```python
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.statistics(assets=?, asset_expression=?, asset_indexes=?, **kwargs)
    stats = stac.merged_statistics(assets=["B01", "B02"], max_size=128)

# stats will be in form or {"band": BandStatistics(), ...}
print(list(stats))
>>> ["B01_b1", "B02_b1"]

assert isinstance(stats["B01_b1"], BandStatistics)

print(info["B01_b1"].json(exclude_none=True))
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

with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    # stac.statistics(assets=?, asset_expression=?, asset_indexes=?, **kwargs)
    stats = stac.merged_statistics(expression=["B01_b1/B02_b1"], max_size=128)

print(list(stats))
>>> ["B01_b1/B02_b1"]

assert isinstance(stats["B01_b1/B02_b1"], BandStatistics)
```

### STAC Expression

When using `expression`, the user will need to explicitly pass the band number to use within the asset e.g: `asset1_b1 + asset2_b2`.

### Asset As Band

in rio-tiler `4.1.0`, we've added `asset_as_band: bool` option to the data methods (tile, feature, part, preview, point) to tell the reader to treat each asset as a dataset band. This is specifically useful for `expression`

```python
# For expression, without `asset_as_band` tag, users have to pass `_b{n}` suffix to indicate the band index
with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, expression="green_b1/red_b1")
    assert img.band_names == ["green_b1/red_b1"]

# With `asset_as_band=True`, expression can be the asset names
with STACReader(STAC_PATH) as stac:
    img = stac.tile(71, 102, 8, expression="green/red", asset_as_band=True)
    assert img.band_names == ["green/red"]
```

## rio_tiler.io.rasterio.ImageReader

The `Reader` is designed to work with simple raster datasets in their pixel coordinates.

The class is derived from the `rio_tiler.io.rasterio.Reader` class.
```python
from rio_tiler.io import ImageReader

ImageReader.__mro__
>>> (rio_tiler.io.rasterio.ImageReader,
 rio_tiler.io.rasterio.Reader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Attributes

- **input** (str): filepath
- **dataset** (rasterio dataset, optional): rasterio opened dataset
- **colormap** (dict, optional): dataset's colormap
- **options** (rio_tiler.reader.Options, optional): Options to forward to rio_tiler.reader functions (e.g nodata, vrt_options, resampling)

#### Properties

- **bounds**: dataset's bounds (in dataset crs)
- **transform**: dataset Affine transform (in pixel coordinates)
- **minzoom**: dataset minzoom
- **maxzoom**: dataset maxzoom

```python
from rio_tiler.io import ImageReader

with ImageReader("image.jpg") as src:
    print(src.dataset)
    print(src.minzoom)
    print(src.maxzoom)
    print(src.transform)
    print(src.bounds)
    print(src.colormap)

>> <open DatasetReader name='image.jpeg' mode='r'>
0
3
Affine(1.0, 0.0, 0.0,  0.0, 1.0, 0.0)
(0, 2000, 2000, 0)
{}
```

#### Methods

- **read()**: Read the entire dataset

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import ImageData

with ImageReader("image.jpeg") as src:
    img = src.read()
    assert isinstance(img, ImageData)
    assert not img.crs
    assert img.assets == ["image.jpeg"]
    assert img.width == src.dataset.width
    assert img.height == src.dataset.height
    assert img.count == src.dataset.count

# With indexes
with ImageReader("image.jpeg") as src:
    img = src.read(indexes=1)  # or src.read(indexes=(1,))
    assert img.count == 1
    assert img.band_names == ["b1"]

# With expression
with ImageReader("image.jpeg") as src:
    img = src.read(expression="b1/b2")
    assert img.count == 1
    assert img.band_names == ["b1/b2"]
```

- **tile()**: Read tile from the image

For ImageReader we are using a custom `LocalTileMatrixSet` constructed from the dataset width and height. The origin is the Top-Left of the image.

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import ImageData

with ImageReader("image.jpeg") as src:
    # src.tile(tile_x, tile_y, tile_z, **kwargs)
    img = src.tile(0, 0, src.maxzoom)
    assert isinstance(img, ImageData)
    assert not img.crs
    assert img.bounds == (0, 256, 256, 0)

    img = src.tile(0, 0, src.minzoom)
    assert isinstance(img, ImageData)
    assert img.bounds[0] == 0
    assert img.bounds[3] == 0

# With indexes
with ImageReader("image.jpeg") as src:
    img = src.tile(1, 2, 3, tilesize=256, indexes=1)
    assert img.count == 1

# With expression
with ImageReader("image.jpeg") as src:
    img = src.tile(1, 2, 3, tilesize=256, expression="B1/B2")
    assert img.count == 1
```

- **part()**: Read an image for a given bounding box (`bbox`). The origin is the Top-Left of the image.

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import ImageData

with ImageReader("image.jpeg") as src:
    # src.part((left, bottom, right, top), **kwargs)
    img = src.part((0, 256, 256, 0))  # read the top-left 256x256 square of the image
    assert isinstance(img, ImageData)
    assert img.assets == ["myfile.tif"]
    assert img.bounds == (0, 256, 256, 0)

# Limit output size
with ImageReader("image.jpeg") as src:
    img = src.part((0, 256, 256, 0), max_size=50)

# With indexes
with ImageReader("image.jpeg") as src:
    img = src.part((0, 256, 256, 0), indexes=1)

# With expression
with ImageReader("image.jpeg") as src:
    img = src.part((0, 256, 256, 0), expression="b1/b2")
```

- **feature()**: Read an image for a geojson feature. In the pixel coordinate system.

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import ImageData

feat = {
    "coordinates": [
        [
            [-100.0, -100.0],
            [1000.0, 100.0],
            [500.0, 1000.0],
            [-50.0, 500.0],
            [-100.0, -100.0],
        ]
    ],
    "type": "Polygon",
}

with ImageReader("image.jpeg") as src:
    # src.part(geojson_feature, **kwargs)
    img = src.feature(feat)
    assert isinstance(img, ImageData)
    assert img.assets == ["image.jpeg"]
    assert img.bounds == (-100.0, 1000.0, 1000.0, -100.0)  # bbox of the input feature

# Limit output size
with ImageReader("image.jpeg") as src:
    img = src.feature(feat, max_size=100)

# Read high resolution
with ImageReader("image.jpeg") as src:
    img = src.feature(feat, max_size=None)

# With indexes
with ImageReader("image.jpeg") as src:
    img = src.feature(feat, indexes=1)

# With expression
with ImageReader("image.jpeg") as src:
    img = src.feature(feat, expression="b1/b2")
```

- **preview()**: Read a preview of a raster

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import ImageData

with ImageReader("image.jpeg") as src:
    img = src.preview()
    assert isinstance(img, ImageData)

# With indexes
with ImageReader("image.jpeg") as src:
    img = src.preview(indexes=1)

# With expression
with ImageReader("image.jpeg") as src:
    img = src.preview(expression="b1+2;b1*4")
```

- **point()**: Read the pixel values of a raster for a given `x, y` coordinates. The origin is the Top-Left of the image.

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import PointData

with ImageReader("image.jpeg") as src:
    # src.point(x, y)
    pt = src.point(0, 0)  # pixel at the origin
    assert isinstance(pt, PointData)

# With indexes
with ImageReader("image.jpeg") as src:
    pt = src.point(0,0 , indexes=1)
    print(pt.data)
>>> [1]

# With expression
with ImageReader("image.jpeg") as src:
    pt = src.point(0, 0, expression="b1+2;b1*4")
    print(pt.data)
>>> [3, 4]
```

- **info()**: Return simple metadata about the dataset

```python
from rio_tiler.io import ImageReader
from rio_tiler.models import Info

with ImageReader("image.jpeg") as src:
    info = src.info()
    assert isinstance(info, Info)

print(info.model_dump(exclude_none=True))
>>> {
    "bounds": [0, 4000, 4000, 0],
    "minzoom": 0,
    "maxzoom": 3,
    "band_metadata": [["b1", {}]],
    "band_descriptions": [["b1", ""]],
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
    "width": 4000,
    "height": 4000,
    "overviews": [2, 4, 8],
}
```

- **statistics()**: Return image statistics (Min/Max/Stdev)

```python
from rio_tiler.io import ImageReader

with ImageReader("image.jpeg") as src:
    stats = src.statistics()
    assert isinstance(stats, dict)

# stats will be in form or {"band": BandStatistics(), ...}
print(stats)
>>> {
    'b1': BandStatistics(...),
    'b2': BandStatistics(...),
    'b3': BandStatistics(...)
}

print(stats["b1"].model_dump())
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
```


## rio_tiler.io.xarray.XarrayReader

The `Reader` is designed to work with xarray.DataReader with full geo-reference metadata (CRS) and variables (X,Y)

The class is derived from the `rio_tiler.io.base.BaseReader` class.
```python
from rio_tiler.io.xarray import XarrayReader

XarrayReader.__mro__
>>> (rio_tiler.io.xarray.XarrayReader,
 rio_tiler.io.base.BaseReader,
 rio_tiler.io.base.SpatialMixin,
 object)
```

#### Attributes

- **input** (xarray.DataArray): Xarray DataArray
- **tms** (morecantile.TileMatrixSet, optional): morecantile TileMatrixSet used for tile reading (defaults to WebMercator)
- **geographic_crs** (rasterio.crs.CRS, optional): CRS to use to calculate the geographic bounds (default to WGS84)

#### Properties

- **bounds**: dataset's bounds (in dataset crs)
- **crs**: dataset's crs
- **geographic_bounds**: dataset's bounds in WGS84
- **minzoom**: dataset minzoom (in TMS)
- **maxzoom**: dataset maxzoom (in TMS)


```python
import numpy
import xarray
from datetime import datetime
from rio_tiler.io.xarray import XarrayReader

arr = numpy.random.randn(1, 33, 35)
data = xarray.DataArray(
    arr,
    dims=("time", "y", "x"),
    coords={
        "x": list(range(-170, 180, 10)),
        "y": list(range(-80, 85, 5)),
        "time": [datetime(2022, 1, 1)],
    },
)
data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})
data.rio.write_crs("epsg:4326", inplace=True)

with XarrayReader(data) as src:
    print(src.input)
    print(src.tms.identifier)
    print(src.minzoom)
    print(src.maxzoom)
    print(src.bounds)
    print(src.crs)
    print(src.geographic_bounds)

>> <xarray.DataArray (time: 1, y: 33, x: 35)>
WebMercatorQuad
0
0
(-175.0, -82.5, 175.0, 82.5)
EPSG:4326
(-175.0, -82.5, 175.0, 82.5)
```

#### Methods

- **tile()**: Read map tile from a raster

```python
from rio_tiler.constants import WEB_MERCATOR_CRS
from rio_tiler.io import XarrayReader
from rio_tiler.models import ImageData

with XarrayReader(data) as src:
    # src.tile(tile_x, tile_y, tile_z, tilesize, reproject_method)
    img = src.tile(1, 2, 3)
    assert isinstance(img, ImageData)
    assert img.crs == WEB_MERCATOR_CRS
```

- **part()**: Read a DataArray for a given bounding box (`bbox`). By default the bbox is considered to be in WGS84.

```python
from rio_tiler.io import XarrayReader
from rio_tiler.models import ImageData

with XarrayReader(data) as src:
    # src.part((minx, miny, maxx, maxy), dst_crs, bounds_crs, reproject_method)
    img = src.part((10, 10, 20, 20))
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.bounds == (10, 10, 20, 20)

# Pass bbox in WGS84 (default) but return data in the input dataset CRS
with XarrayReader(data) as src:
    img = src.part((10, 10, 20, 20), dst_crs=src.dataset.crs)
    assert img.crs == src.dataset.crs
```

- **feature()**: Read a DataArray for a geojson feature. By default the feature is considered to be in WGS84.

```python
from rio_tiler.constants import WGS84_CRS
from rio_tiler.io import XarrayReader
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

with XarrayReader(data) as src:
    # src.part(geojson_feature, **kwargs)
    img = src.feature(feat)
    assert isinstance(img, ImageData)
    assert img.crs == WGS84_CRS
    assert img.bounds == (-55.61, 72.36, -53.83, 73.05)  # bbox of the input feature

# Pass bbox in WGS84 (default) but return data in the input dataset CRS
with XarrayReader(data) as src:
    img = src.feature(feat, dst_crs=src.dataset.crs)
    assert img.crs == src.dataset.crs
```

- **point()**: Read the pixel values of a DataArray for a given `lon, lat` coordinates. By default the coordinates are considered to be in WGS84.

```python
from rio_tiler.io import XarrayReader
from rio_tiler.models import PointData

with XarrayReader(data) as src:
    # src.point(lon, lat, coord_crs)
    pt = src.point(-100, 25)
    assert isinstance(pt, PointData)
```

- **info()**: Return simple metadata about the DataArray

```python
from rio_tiler.io import XarrayReader
from rio_tiler.models import Info

with XarrayReader(data) as src:
    info = src.info()
    assert isinstance(info, Info)

print(info.json(exclude_none=True))
>>> {
    "bounds": [-175.0, -82.5, 175.0, 82.5],
    "minzoom": 0,
    "maxzoom": 0,
    "band_metadata": [["b1", {}]],
    "band_descriptions": [["b1", "2022-01-01T00:00:00.000000000"]],
    "dtype": "float64",
    "nodata_type": "None",
    "width": 35,
    "attrs": {
        "valid_min": -3.148671506292848,
        "valid_max": 4.214148915352746
    },
    "count": 1,
    "height": 33
}
```

- **preview()**:

!!! Important

    Not Implemented


- **statistics()**:

!!! Important

    Not Implemented


#### Settings

`RIO_TILER_XARRAY_DEFAULT_WGS84=TRUE/FALSE` environment variable can be used to enable setting `WGS84` CRS by default when the CRS information is not defined in the Xarray dataset. Defaults to `False`.
