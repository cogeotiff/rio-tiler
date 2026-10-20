
An experimental *Reader* built on top the `XarrayReader` but remove the usage of rioxarray and instead rely on the Geo/Spatial conventions (or user input CRS/Transform) for geospatial operations (e.g coordinates selection). This reader differs from the regular XarrayReader with:

    - allows`crs` and `transform` input parameters or relies on Zarr Geo/Spatial conventions attributes
    - do not read coordinates arrays
    - allows `band_names` input parameter to specify the 3d dimension names

You can install the dependencies with `python -m pip install "rio-tiler[geoarray]"`.

```python
from obstore.store import HTTPStore
import zarr
from zarr.storage import ObjectStore
import xarray
from rasterio.crs import CRS
from affine import Affine
from rio_tiler.experimental.xarray import GeoArrayReader

# Create Obstore Store
store = HTTPStore("https://s3.explorer.eopf.copernicus.eu/esa-zarr-sentinel-explorer-fra/tests-output/sentinel-2-l2a/S2B_MSIL2A_20260216T142149_N0512_R096_T25WFV_20260216T165051.zarr")
zarr_store = ObjectStore(store=store, read_only=True)

ds = xarray.open_datatree(
    zarr_store,  # type: ignore
    decode_times=True,
    decode_coords="all",
    create_default_indexes=False,
    consolidated=True,
    engine="zarr",
)
group = ds["/measurements/reflectance/r720m"]

crs = CRS.from_user_input(group.attrs["proj:code"])
transform = Affine(*group.attrs["spatial:transform"])

# Select an array ("b02")
dataarray = group["b02"]

# Initiate the reader
reader = GeoArrayReader(
    input=dataarray,
    crs=crs,
    transform=transform,
)

# The `/measurements/reflectance` group has spatial/geo conventions
print(reader.bounds)
>> (600000.0, 7890600.0, 709440.0, 8000040.0

print(reader.crs)
>> CRS.from_epsg(32625)

# info
print(reader.info())
>> bounds=(600000.0, 7890600.0, 709440.0, 8000040.0) crs='http://www.opengis.net/def/crs/EPSG/0/32625' band_metadata=[('b1', {})] band_descriptions=[('b1', 'b1')] dtype='float32' nodata_type='None' colorinterp=None colormap=None name='b02' count=1 width=152 height=152 dimensions=('y', 'x') attrs={'_eopf_attrs': {'add_offset': -0.1, 'coordinates': ['y', 'x'], 'dimensions': ['y', 'x'], 'dtype': '<u2', 'eopf_is_masked': True, 'eopf_target_dtype': '<f8', 'fill_value': 0, 'long_name': 'BOA reflectance from MSI acquisition at spectral band 02 490 nm', 'scale_factor': 0.0001, 'short_name': 'b02_60m', 'units': 'digital_counts', 'valid_max': 65535, 'valid_min': 1}, 'dtype': '<u2', 'long_name': 'BOA reflectance from MSI acquisition at spectral band 02 490 nm', 'units': 'digital_counts'}

# Get the preview for a specific variable
img = reader.preview()
```