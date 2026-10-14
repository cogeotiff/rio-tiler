
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