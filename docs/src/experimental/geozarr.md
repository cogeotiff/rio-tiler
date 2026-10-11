
Asynchronous rio-tiler readers built on top [`zarr-python`](https://zarr.readthedocs.io/) that can read zarr groups or arrays.

Required dependencies:
- `zarr>=3.0`
- `obstore` 
- `isochron`

You can install the dependencies with `python -m pip install "rio-tiler[zarr]".

**Zarr Array Mini Spec**

If not provided as attribute, the `AsyncArrayReader`/`ArrayReader` will require some zarr-metadata/conventions:

- `dimensions` MUST be set in the zarr metadata 

- `zarr_conventions`:
    - **spatial**
        - `spatial:dimensions` MUST be defined (as per the spatial specification)
        - `spatial:transform` MUST be defined

    - **proj**
        - one of `proj:code, proj:wkt2, proj:projjson` MUST be defined (as per the spatial specification)


    - **coords** (Optional)
        - `coords:coordinates`: CAN be defined to indicate the non-spatial coordinates names (band-descriptions)

Example: 

```python
    store = zarr.storage.MemoryStore()

    spatial_conventions = {
        "schema_url": "https://raw.githubusercontent.com/zarr-conventions/spatial/refs/tags/v1/schema.json",
        "spec_url": "https://github.com/zarr-conventions/spatial/blob/v1/README.md",
        "uuid": "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4",
        "name": "spatial:",
        "description": "Spatial coordinate information",
    }
    proj_conventions = {
        "schema_url": "https://raw.githubusercontent.com/zarr-experimental/geo-proj/refs/tags/v1/schema.json",
        "spec_url": "https://github.com/zarr-experimental/geo-proj/blob/v1/README.md",
        "uuid": "f17cb550-5864-4468-aeb7-f3180cfb622f",
        "name": "proj:",
        "description": "Coordinate reference system information for geospatial data",
    }
    multiscale_conventions = {
        "schema_url": "https://raw.githubusercontent.com/zarr-conventions/multiscales/refs/tags/v1/schema.json",
        "spec_url": "https://github.com/zarr-conventions/multiscales/blob/v1/README.md",
        "uuid": "d35379db-88df-4056-af3a-620245f8e347",
        "name": "multiscales",
        "description": "Multiscale layout of zarr datasets",
    }
    coordinates_conventions = {
        "schema_url": "https://raw.githubusercontent.com/zarr-conventions/coords/refs/tags/v1/schema.json",
        "spec_url": "https://github.com/zarr-conventions/coords/blob/v1/README.md",
        "uuid": "6ca4454a-658a-4348-a667-b39ced0e58cb",
        "name": "coords",
        "description": "Domain-agnostic mapping between Zarr array index space and coordinate space.",
    }

    attributes = {}
    attributes["zarr_conventions"] = [
        spatial_conventions,
        proj_conventions,
        coordinates_conventions,
    ]

    # add spatial and projection metadata
    attributes.update(
        {
            "spatial:dimensions": ["lat", "lon"],
            "spatial:transform": list(
                Affine.translation(500000, 4000100) @ Affine.scale(0.5, -1)
            ),
            "spatial:bbox": [500000.0, 4000000.0, 500100.0, 4000100.0],
            "proj:code": "EPSG:32618",
        }
    )

    # add coordinates metadata
    attributes["coords:coordinates"] = {
        "lat": {"type": "reference", "convention": "spatial"},
        "time": {"type": "inline", "values": ["t1", "t2", "t3"]},
        "lon": {"type": "reference", "convention": "spatial"},
    }
    arr_sync = zarr.create(
        store=store,
        shape=(100, 3, 200),
        chunks=(50, 1, 50),
        dtype="float32",
        fill_value=-9999.0,
        dimension_names=("lat", "time", "lon"),
        attributes=attributes,
    )
```

### AsyncArrayReader

```python
from affine import Affine
from obstore.store import S3Store
import zarr
from zarr.storage import ObjectStore
from rasterio.crs import CRS
from rio_tiler.experimental.zarr import AsyncArrayReader

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

ds = AsyncArrayReader(
    input=array,
    # The `analysed_sst` array doesn't have any zarr-convention
    # so we pass the information via the attributes
    crs=CRS.from_epsg(4326),
    transform=Affine.translation(xmin, ymax) @ Affine.scale(xres, -yres),
    dimensions=["time", "lat", "lon"],
    spatial_dims=["lat", "lon"],
    coordinates={
        "time": {"type": "inline", "values": time_arrray.tolist()},
    },
)
img = await ds.tile(9, 10, 5, indexes=10)
```

## AsyncGroupReader

#### Open Top level group in the Zarr store

```python
from obstore.store import HTTPStore
import zarr
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import AsyncGroupReader

from matplotlib.pyplot import imshow

# Create Obstore Store
store = HTTPStore("https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr")
zarr_store = ObjectStore(store=store, read_only=True)
geozarr = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")

# Initiate the reader
reader = AsyncGroupReader(geozarr)

print(reader.bounds)
# the top level zarr store doesn't have spatial:bbox attributes
>> (-180, -90, 180, 90)

# List available variables (arrays with group or array Geo/Spatial conventions)
variables = await reader.list_variables()
print(variables)
>>> [{'name': 'b02',
  'group': 'measurements/reflectance',
  'long_name': 'measurements/reflectance:b02',
  'multiscale': True,
  'nbands': 1},
 ...
 {'name': 'snw',
  'group': 'quality/probability/r20m',
  'long_name': 'quality/probability/r20m:snw',
  'multiscale': False,
  'nbands': 1}]

await reader.get_group_metadata("measurements/reflectance")
>> {'crs': CRS.from_epsg(32626),
 'bbox': [399965.0, 4290245.0, 509755.0, 4400035.0],
 'transform': None,
 'multiscale': True,
 'arrays': {'b02': [{'array': <AsyncArray object_store://HTTPStore("https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr")/measurements/reflectance/r10m/b02 shape=(10980, 10980) dtype=float32>,
    'crs': CRS.from_epsg(32626),
    'height': 10980,
    'width': 10980,
    'transform': Affine(10.0, 0.0, 399965.0,
           0.0, -10.0, 4400035.0),
    'coordinates': None},
....


# Get the preview for a specific variable
img = await reader.preview(variables=["measurements/reflectance:b02"], max_size=64)

# Get Bounds for a specific set of variables (The root store can have multiple spatial extents)
bounds = await reader.get_bounds(variables=["measurements/reflectance:b02"], crs="EPSG:4326")

# Get Minzoom for a specific set of variables (The root store doesn't have transform/shape)
minzoom = await reader.get_minzoom(variables=["measurements/reflectance:b02"])

# Get Time image
tile = reader.tms.tile(bounds[0], bounds[1], minzoom)
img = await reader.tile(tile.x, tile.y, tile.z, variables=("measurements/reflectance:b04", "measurements/reflectance:b03", "measurements/reflectance:b02"))
```

#### Open a specific Zarr Group

```python
from obstore.store import HTTPStore
import zarr
from zarr.storage import ObjectStore

from rio_tiler.experimental.zarr import GeoZarrReader

from matplotlib.pyplot import imshow

# Create Obstore Store
store = HTTPStore("https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance")
zarr_store = ObjectStore(store=store, read_only=True)
geozarr = await zarr.api.asynchronous.open_group(store=zarr_store, mode="r")

# Initiate the reader
reader = AsyncGroupReader(geozarr)

# The `/measurements/reflectance` group has spatial/geo conventions
print(reader.bounds)
>> (399965.0, 4290245.0, 509755.0, 4400035.0)

print(reader.crs)
>> CRS.from_epsg(32626)

# List available variables (arrays with group or array Geo/Spatial conventions)
variables = await reader.list_variables()
print([b["name"] for b in variables])
>>> ['b01', 'b02', 'b03', 'b04', 'b05', 'b06', 'b07', 'b08', 'b09', 'b11', 'b12', 'b8a']

# Get the preview for a specific variable
img = await reader.preview(variables=["b02"], max_size=128)

bounds = reader.get_geographic_bounds("epsg:4326")
# Get Time image
tile = reader.tms.tile(bounds[0], bounds[1], reader.minzoom)
img = await reader.tile(tile.x, tile.y, tile.z, variables=("b04", "b03", "b02"))
```
