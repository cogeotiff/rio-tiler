![](https://user-images.githubusercontent.com/10407788/105767632-3f959e80-5f29-11eb-9331-969f3f53111e.png)

Starting with `rio-tiler` v2, a `.feature()` method exists on `rio-tiler`'s readers (e.g `Reader`) which enables data reading for GeoJSON defined (polygon or multipolygon) shapes.

```python
from rio_tiler.io import Reader
from rio_tiler.models import ImageData

with Reader("my-tif.tif") as cog:
    # Read data for a given geojson polygon
    img: ImageData = cog.feature(geojson_feature, max_size=1024)  # we limit the max_size to 1024
```

Under the hood, the `.feature` method uses rasterio's [`rasterize`](https://rasterio.readthedocs.io/en/latest/api/rasterio.features.html#rasterio.features.rasterize)
function and the `.part()` method. The below process is roughly what `.feature` does for you.

```python
from rasterio.features import rasterize, bounds as featureBounds

from rio_tiler.io import Reader

# Use Reader to open and read the dataset
with Reader("my_tif.tif") as cog:

    # Get BBOX of the polygon
    bbox = featureBounds(feat)

    # Read part of the data overlapping with the geometry bbox
    # assuming that the geometry coordinates are in web mercator
    img = cog.part(bbox, bounds_crs=f"EPSG:3857", max_size=1024)

    # Rasterize geometry using the same geotransform parameters
    cutline = rasterize(
        [feat],
        out_shape=(img.height, img.width),
        transform=img.transform,
        ...
    )

    # Apply geometry mask to imagery
    img.array.mask = numpy.where(~cutline, img.array.mask, True)
```

Another interesting way to cut features is to use the GDALWarpVRT's `cutline`
option with the .part(), .preview(), or .tile() methods:

```python
from rio_tiler.utils import create_cutline

bbox = featureBounds(feat)

# Use Reader to open and read the dataset
with Reader("my_tif.tif") as cog:
    # Create WTT Cutline
    cutline = create_cutline(cog.dataset, feat, geometry_crs="epsg:4326")

    # Get a part of the geotiff but use the cutline to mask the data
    bbox = featureBounds(feat)
    img = cog.part(bbox, vrt_options={'cutline': cutline})

    # Get a preview of the whole geotiff but use the cutline to mask the data
    img = cog.preview(vrt_options={'cutline': cutline})

    # Read a mercator tile and use the cutline to mask the data
    img = cog.tile(1, 1, 1, vrt_options={'cutline': cutline})
```
