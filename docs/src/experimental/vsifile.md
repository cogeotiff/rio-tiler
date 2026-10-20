
Required dependencies:
- `vsifile>=0.2`

A rio-tiler Reader using VSIFile/Obstore as file system handler. Starting with GDAL>=3.0, **VSI plugin** was added in order to enable users to provide their own file system handler (class handling the file requests).

The reader is considered experimental because [`VSIFile`](https://github.com/vincentsarago/vsifile) is still under development. Users should also note that changes available in GDAL>=3.10 will drastically improve the performance of this reader (https://github.com/vincentsarago/vsifile/issues/13#issuecomment-2683310594)

```python
from rio_tiler.experimental.vsifile import VSIReader

with VSIReader("https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/15/T/VK/2023/10/S2B_15TVK_20231008_0_L2A/TCI.tif") as src:
    print(src.info())

>>> bounds=(399960.0, 4890240.0, 509760.0, 5000040.0) crs='http://www.opengis.net/def/crs/EPSG/0/32615' band_metadata=[('b1', {}), ('b2', {}), ('b3', {})] band_descriptions=[('b1', ''), ('b2', ''), ('b3', '')] dtype='uint8' nodata_type='Nodata' colorinterp=['red', 'green', 'blue'] colormap=None driver='GTiff' count=3 width=10980 height=10980 overviews=[2, 4, 8, 16] nodata_value=0.0
```

#### Links

- https://github.com/OSGeo/gdal/pull/1289
- https://github.com/rasterio/rasterio/pull/2141

