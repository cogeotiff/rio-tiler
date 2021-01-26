![](https://user-images.githubusercontent.com/10407788/105767632-3f959e80-5f29-11eb-9331-969f3f53111e.png)

Starting with `rio-tiler` v2, a `.feature()` method exists on `rio-tiler`'s readers (e.g `COGReader`) which enables data reading for GeoJSON defined (polygon or multipolygon) shapes.

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("my-tif.tif") as cog:
    # Read data for a given geojson polygon (size is maxed out to 1024)
    img: ImageData = cog.feature(geojson_feature)
```

Under the hood, the `.feature` method uses `GDALWarpVRT`'s `cutline` option and
the `.part()` method. The below process is roughly what `.feature` does for you.

```python
from rio_tiler.io import COGReader
from rio_tiler.utils import create_cutline
from rasterio.features import bounds as featureBounds

# Use COGReader to open and read the dataset
with COGReader("my_tif.tif") as cog:
    # Create WTT Cutline
    cutline = create_cutline(cog.dataset, feat, geometry_crs="epsg:4326")

    # Get BBOX of the polygon
    bbox = featureBounds(feat)

    # Read part of the data (bbox) and use the cutline to mask the data
    data, mask = cog.part(bbox, vrt_options={'cutline': cutline})
```

Another interesting fact about the `cutline` option is that it can be used with other methods:

```python
bbox = featureBounds(feat)

# Use COGReader to open and read the dataset
with COGReader("my_tif.tif") as cog:
    # Create WTT Cutline
    cutline = create_cutline(cog.dataset, feat, geometry_crs="epsg:4326")

    # Get a preview of the whole geotiff but use the cutline to mask the data
    data, mask = cog.preview(vrt_options={'cutline': cutline})

    # Read a mercator tile and use the cutline to mask the data
    data, mask = cog.tile(1, 1, 1, vrt_options={'cutline': cutline})

    # Get image statistics over a bbox and use the cutline as mask
    stats = cog.stats(bounds=bbox, vrt_options={'cutline': cutline})
```
