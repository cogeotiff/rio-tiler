
Natively rio-tiler support mostly `bbox` reading. Using GDALWarpVRT **Cutline** option, it's possible to read a dataset for a given polygon.

```python

from rio_tiler.io import COGReader
from rio_tiler.utils import create_cutline
from rasterio.features import bounds as featureBounds

feat =     {
    "type": "Feature",
    "properties": {},
    "geometry": {
    "type": "Polygon",
    "coordinates": [
        [
        [-52.6025390625, 73.86761239709705],
        [-52.6025390625, 73.59679245247814],
        [-51.591796875, 73.60299628304274],
        [-51.591796875, 73.90420357134279],
        [-52.4267578125, 74.0437225981325],
        [-52.6025390625, 73.86761239709705]
        ]
    ]
    }
}

# Get BBOX of the polygon
bbox = featureBounds(feat)

# Use COGReader to open and read the dataset
with COGReader("my_tif.tif") as cog:
    # Create WTT Cutline
    cutline = create_cutline(cog.dataset, feat, geometry_crs="epsg:4326")

    # Read part of the data (bbox) and use the cutline to mask the data
    data, mask = cog.part(bbox, vrt_options={'cutline': cutline})
```

The previous example uses the `.part` method but any method that uses the `rio_tiler.reader._read` function will accept the `cutline` options.

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
