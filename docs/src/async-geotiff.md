
An asynchronous rio-tiler reader built on top of [`async-geotiff`](https://github.com/developmentseed/async-geotiff).

Required dependencies:
- `async-geotiff>=0.5,<0.6`
- `obstore` 

You can install the dependencies with `python -m pip install "rio-tiler[geotiff]"`.

```python
from obstore.store import S3Store
from async_geotiff import GeoTIFF
from rio_tiler.io.geotiff import Reader as GeoTIFFReader

# Create Obstore Store
store = S3Store("sentinel-cogs", skip_signature=True, region="us-west-2")

# Creage GeoTIFF instance
geotiff = await GeoTIFF.open("sentinel-s2-l2a-cogs/15/T/VK/2023/10/S2B_15TVK_20231008_0_L2A/TCI.tif", store=store)

# Get Tile
async with GeoTIFFReader(geotiff) as src:
    img = await src.tile(493, 741, 11)
```

See [Async-STAC](async-stac.md) to use this reader with STAC Items.
