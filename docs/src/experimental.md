# Experimental Features

In this section you will find documentation for new, experimental features in rio-tiler. These features are subject to change or removal, and we are looking for feedback and suggestions before making them a permanent part of Pydantic.


## Feedback

We welcome feedback on experimental features! Please open an issue on the [rio-tiler GitHub repository](https://github.com/cogeotiff/rio-tiler/issues/new/choose) to share your thoughts, requests, or suggestions.

We also encourage you to read through existing feedback and add your thoughts to existing issues.

## Warnings on Import

When you import an experimental feature from the `experimental` module, you'll see a warning message that the feature is experimental. You can disable this warning with the following:

```python
import warnings
from rio_tiler.errors import RioTilerExperimentalWarning

warnings.filterwarnings('ignore', category=RioTilerExperimentalWarning)
```

## VSIFile Reader

Required dependencies:
- `vsifile>=0.2`

A rio-tiler Reader using VSIFile/Obstore as file system handler. Starting with GDAL>=3.0, **VSI plugin** was added in order to enable users to provide their own file system handler (class handling the file requests).

The reader is considered experimental because [`VSIFile`](https://github.com/vincentsarago/vsifile) is still under development. Users should also note that changes available in GDAL>=3.10 will drastically improve the performance of this reader (https://github.com/vincentsarago/vsifile/issues/13#issuecomment-2683310594)

```python
from rio_tiler.experimental.vsifile import VSIReader

with VSIReader("https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/15/T/VK/2023/10/S2B_15TVK_20231008_0_L2A/TCI.tif") as src:
    print(src.info())

>>> bounds=(399960.0, 4890240.0, 509760.0, 5000040.0) crs='http://www.opengis.net/def/crs/EPSG/0/32615' band_metadata=[('b1', {}), ('b2', {}), ('b3', {})] band_descriptions=[('b1', ''), ('b2', ''), ('b3', '')] dtype='uint8' nodata_type='Nodata' colorinterp=['red', 'green', 'blue'] scales=[1.0, 1.0, 1.0] offsets=[0.0, 0.0, 0.0] colormap=None driver='GTiff' count=3 width=10980 height=10980 overviews=[2, 4, 8, 16] nodata_value=0.0
```

#### Links

- https://github.com/OSGeo/gdal/pull/1289
- https://github.com/rasterio/rasterio/pull/2141


## GeoTIFF Reader

A asynchronous rio-tiler reader built on top [`async-geotiff`](https://github.com/developmentseed/async-geotiff). This reader is considered experimental because the API might evolve in the future and the `part()` method might be refactored to avoid using `rasterio.warp.reproject`.

Required dependencies:
- `async-geotiff>=0.3,<0.4`
- `obstore` 

You can install the dependencies with `python -m pip install "rio-tiler[geotiff]".

```python
from obstore.store import S3Store
from async_geotiff import GeoTIFF
from rio_tiler.experimental.geotiff import Reader as GeoTIFFReader

# Create Obstore Store
store = S3Store("sentinel-cogs", skip_signature=True, region="us-west-2")

# Creage GeoTIFF instance
geotiff = await GeoTIFF.open("sentinel-s2-l2a-cogs/15/T/VK/2023/10/S2B_15TVK_20231008_0_L2A/TCI.tif", store=store)

# Get Tile
await with GeoTIFFReader(geotiff) as src:
    img = await src.tile(493, 741, 11)
```

## ZARR Reader (Array)

A asynchronous rio-tiler reader built on top [`zarr-python`](https://zarr.readthedocs.io/) that can read single array.

Required dependencies:
- `zarr>=3.0`
- `obstore` 

You can install the dependencies with `python -m pip install "rio-tiler[zarr]".

```python
from affine import Affine
from obstore.store import S3Store
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import Reader as ZarrReader

# Create Obstore Store
store = S3Store("mur-sst/zarr-v1", skip_signature=True, region="us-west-2")
zarr_store = ObjectStore(store=store, read_only=True)

# Get Group and Array
group = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")

# List Arrays
async for key in group.keys():
    print(key)

>> analysed_sst
analysis_error
lat
lon
mask
sea_ice_fraction
time

# Fetch time coordinate for `band_names`
time = await group.getitem("time")
time_arrray = await time.getitem(slice(None))

# Fetch Lon/Lat coordinates
lon = await group.getitem("lon")
lon_arrray = await lon.get_coordinate_selection([0, -1])

lat = await group.getitem("lat")
lat_arrray = await lat.get_coordinate_selection([0, -1])

# Get Min/Max Coordinates
xmin, xmax = lon_arrray[0], lon_arrray[-1]
ymin, ymax = lat_arrray[0], lat_arrray[-1]

# Calculate resolution
xres = (xmax - xmin) / lon.shape[0]
yres = (ymax - ymin) / lat.shape[0]

# Adjust coordinates to match pixel edges
xmin = xmin - xres
ymax = ymax + yres

# Select an array ("analysed_sst")
array = await group.getitem("analysed_sst")

ds = ZarrReader(
    input=array,
    crs=CRS.from_epsg(4326),
    transform=Affine.translation(xmin, ymax) * Affine.scale(xres, -yres),
    band_names=[str(d) for d in time_arrray.tolist()],
)
img = await ds.tile(9, 10, 5, indexes=10)
```

## GeoZARR Reader (Group + GeoZARR conventions)

A asynchronous rio-tiler reader built on top [`zarr-python`](https://zarr.readthedocs.io/) that can read Groups of arrays.

Required dependencies:
- `zarr>=3.0`
- `obstore` 


#### Open Top level group in the Zarr store

```python
from obstore.store import HTTPStore
import zarr
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import GeoZarrReader

from matplotlib.pyplot import imshow

# Create Obstore Store
store = HTTPStore("https://s3.explorer.eopf.copernicus.eu/esa-zarr-sentinel-explorer-fra/tests-output/sentinel-2-l2a/S2B_MSIL2A_20260216T142149_N0512_R096_T25WFV_20260216T165051.zarr")
zarr_store = ObjectStore(store=store, read_only=True)
geozarr = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")

# Initiate the reader
reader = GeoZarrReader(geozarr)

print(reader.bounds)
# the top level zarr store doesn't have spatial:bbox attributes
>> (-180, -90, 180, 90)

# List available variables (arrays with group or array Geo/Spatial conventions)
variables = await reader.list_variables()
print(variables)
>>> ['measurements/reflectance:b01', 'measurements/reflectance:b02', 'measurements/reflectance:b03', 'measurements/reflectance:b04', 'measurements/reflectance:b05', 'measurements/reflectance:b06', 'measurements/reflectance:b07', 'measurements/reflectance:b08', 'measurements/reflectance:b09', 'measurements/reflectance:b11', 'measurements/reflectance:b12', 'measurements/reflectance:b8a', 'quality/atmosphere/r10m:aot', 'quality/atmosphere/r10m:wvp', 'quality/atmosphere/r20m:aot', 'quality/atmosphere/r20m:wvp', 'quality/atmosphere/r60m:aot', 'quality/atmosphere/r60m:wvp', 'quality/mask/r10m:b02', 'quality/mask/r10m:b03', 'quality/mask/r10m:b04', 'quality/mask/r10m:b08', 'quality/mask/r20m:b05', 'quality/mask/r20m:b06', 'quality/mask/r20m:b07', 'quality/mask/r20m:b11', 'quality/mask/r20m:b12', 'quality/mask/r20m:b8a', 'quality/mask/r60m:b01', 'quality/mask/r60m:b09', 'quality/mask/r60m:b10', 'quality/probability/r20m:cld', 'quality/probability/r20m:snw']

# Get the preview for a specific variable
img = await reader.preview(variables=["measurements/reflectance:b02"], max_size=128)

# Get Bounds for a specific set of variables (The root store can have multiple spatial extents)
bounds = await reader.get_bounds(variables=["measurements/reflectance:b02"], crs="EPSG:4326")

# Get Minzoom for a specific set of variables (The root store doesn't have transform/shape)
minzoom = await reader.get_minzoom(variables=["measurements/reflectance:b02"])

# Get Time image
tile = reader.tms.tile(bounds[0], bounds[1], minzoomminzoom)
img = await dreaders.tile(tile.x, tile.y, tile.z, variables=("measurements/reflectance:b04", "measurements/reflectance:b03", "measurements/reflectance:b02"))
```

#### Open a specific Zarr Group

```python
from obstore.store import HTTPStore
import zarr
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import GeoZarrReader

from matplotlib.pyplot import imshow

# Create Obstore Store
store = HTTPStore("https://s3.explorer.eopf.copernicus.eu/esa-zarr-sentinel-explorer-fra/tests-output/sentinel-2-l2a/S2B_MSIL2A_20260216T142149_N0512_R096_T25WFV_20260216T165051.zarr/measurements/reflectance/")
zarr_store = ObjectStore(store=store, read_only=True)
geozarr = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")

# Initiate the reader
reader = GeoZarrReader(geozarr)

# The `/measurements/reflectance` group has spatial/geo conventions
print(reader.bounds)
>> (600005.0, 7890245.0, 709795.0, 8000035.0)

print(reader.crs)
>> CRS.from_epsg(32625)

# List available variables (arrays with group or array Geo/Spatial conventions)
variables = await reader.list_variables()
print(variables)
>>> ['b01', 'b02', 'b03', 'b04', 'b05', 'b06', 'b07', 'b08', 'b09', 'b11', 'b12', 'b8a']

# Get the preview for a specific variable
img = await reader.preview(variables=["b02"], max_size=128)

bounds = 
# Get Time image
tile = reader.tms.tile(bounds[0], bounds[1], reader.minzoom)
img = await reader.tile(tile.x, tile.y, tile.z, variables=("b04", "b03", "b02"))
```

## AsyncSTACReader

An experimental *Reader* built on top the `AsyncMultiReaderBase` abstract base class. This reader differs from the regular STACReader with:

    - takes a `pystac.Item` as input (not a URL)
    - `reader: AsyncBaseReader = ...` is a required argument (no default async reader exist outside the experimental ones)


```python
from typing import Any

import posixpath
from contextlib import asynccontextmanager
from urllib.parse import urlparse

from async_geotiff import GeoTIFF
from obstore.store import from_url
from rio_tiler.experimental.geotiff import Reader as GeoTIFFReader
from rio_tiler.experimental.async_stac import AsyncSTACReader
import pystac 

@asynccontextmanager
async def reader(url: str, *args: Any,  **kwargs: Any):
    """Custom Async Reader using obstore+async-geotiff"""
    parsed = urlparse(url)

    directory = posixpath.dirname(parsed.path)
    store_url = f"{parsed.scheme}://{parsed.netloc}{directory}"
    store = from_url(store_url, skip_signature=True)

    filename = posixpath.basename(parsed.path)
    geotiff = await GeoTIFF.open(filename, store=store)
    async with GeoTIFFReader(geotiff, *args, **kwargs) as src:
        yield src

item = pystac.Item.from_file("https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2B_35LQL_20260423_0_L2A")
async with AsyncSTACReader(input=item, reader=reader) as stac:
    print(stac)

    >>> AsyncSTACReader(bounds=(699960.0, 8990200.0, 809760.0, 9100000.0), crs=CRS.from_epsg(32735), transform=Affine(10.0, 0.0, 699960.0,
        0.0, -10.0, 9100000.0), height=10980, width=10980, input=<Item id=S2B_35LQL_20260423_0_L2A>, reader=<function reader at 0x1668721f0>, tms=<TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, minzoom=8, maxzoom=14, include_assets=None, exclude_assets=None, include_asset_types={'image/tiff', 'image/x.geotiff', 'application/x-hdf5', 'image/tiff; application=geotiff; profile=cloud-optimized', 'image/tiff; profile=cloud-optimized; application=geotiff', 'image/tiff; application=geotiff', 'application/x-hdf', 'image/jp2', 'image/vnd.stac.geotiff; cloud-optimized=true'}, exclude_asset_types=None, default_assets=None, reader_options={}, item=<Item id=S2B_35LQL_20260423_0_L2A>, assets=['aot', 'blue', 'cloud', 'coastal', 'green', 'nir', 'nir08', 'nir09', 'red', 'rededge1', 'rededge2', 'rededge3', 'scl', 'snow', 'swir16', 'swir22', 'visual', 'wvp', 'aot-jp2', 'blue-jp2', 'coastal-jp2', 'green-jp2', 'nir-jp2', 'nir08-jp2', 'nir09-jp2', 'red-jp2', 'rededge1-jp2', 'rededge2-jp2', 'rededge3-jp2', 'scl-jp2', 'swir16-jp2', 'swir22-jp2', 'visual-jp2', 'wvp-jp2'])


    img = await stac.preview(assets={"name": "red", "indexes": [0]})
    print(img.statistics())                      
    >>> {'b1': BandStatistics(min=5.0, max=10664.0, mean=3308.9022180896536, count=66679.0, sum=220634291.0, std=2403.0317223160237, median=2767.0, majority=441.0, minority=5.0, unique=9456.0, histogram=[[14203, 12648, 10254, 8267, 6805, 5550, 4288, 2724, 1573, 367], [5.0, 1070.9, 2136.8, 3202.7000000000003, 4268.6, 5334.5, 6400.400000000001, 7466.300000000001, 8532.2, 9598.1, 10664.0]], valid_percent=6.36, masked_pixels=981897.0, valid_pixels=66679.0, description='red_b0', percentile_2=294.0, percentile_98=8826.0)}
```