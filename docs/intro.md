
## Usage

The `rio_tiler` module can create mercator tiles from any raster source supported by Rasterio/GDAL (i.e. local files, http, s3, gcs etc.). Additional method are availables (see [COGReader](#COGReader))

#### Read a tile from a file

```python
from rio_tiler.io import COGReader

with COGReader("http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif") as cog:
    tile, mask = cog.tile(691559, 956905, 21, tilesize=256)

print(tile.shape)
> (3, 256, 256)

print(mask.shape)
> (256, 256)
```

#### Render the array as an image (PNG/JPEG)

```python
from rio_tiler.utils import render

buffer = render(tile, mask=mask) # this returns a buffer (PNG by default)
```

Rescale non-byte data and/or apply colormap

```python
from rio_tiler.colormap import cmap
from rio_tiler.utils import linear_rescale

# Rescale the tile array only where mask is valid and cast it to byte
tile = numpy.where(
    mask,
    linear_rescale(tile, in_range=(0, 1000), out_range=[0, 255]),
    0
).astype(numpy.uint8)

cm = cmap.get("viridis")

buffer = render(tile, mask=mask, colormap=cm)
```

Use creation options to match `mapnik` defaults.

```python
from rio_tiler.utils import render
from rio_tiler.profiles import img_profiles

options = img_profiles.get("webp")
buffer = render(tile, mask=mask, img_format="webp", **options)
```

Write image to file

```python
with open("my.png", "wb") as f:
  f.write(buffer)
```

##### NumpyTile

You can also export image data to a numpy binary format (`NPY`)

```python
from io import BytesIO
import numpy
from rio_tiler.utils import render

buffer = render(tile, mask=mask, img_format="npy")
npy_tile = numpy.load(BytesIO(buffer))
assert npy_tile.shape == (4, 256, 256)  # mask is appened to the end of the data
```
