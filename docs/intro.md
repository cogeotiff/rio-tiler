
The main goal of `rio-tiler` is to create [slippy map
tiles](https://en.wikipedia.org/wiki/Tiled_web_map) from large raster data
sources and render these tiles dynamically on a web map. `rio-tiler` can read
data and metadata from any raster source supported by Rasterio/GDAL wherever
they may be, including local files and via HTTP, AWS S3, Google Cloud Storage,
etc.

## Read a tile from a file

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

tile_x = 691559
tile_y = 956905
tile_zoom = 21

with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    img = cog.tile(tile_x, tile_y, tile_zoom, tilesize=256)
    assert isinstance(img, ImageData)

    print(img.data.shape)
    >>> (3, 256, 256)
    print(img.mask.shape)
    >>> (256, 256)

    # You can also use the `old style` notation
    data, mask = cog.tile(691559, 956905, 21, tilesize=256)
    print(data.shape)
    >>> (3, 256, 256)
    print(mask.shape)
    >>> (256, 256)
```

The `COGReader` class has other interesting features, please see [User Guide - Readers](readers.md).


## Render the data as an image (PNG/JPEG)

```python
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    img = cog.tile(691559, 956905, 21, tilesize=256)
    buff = img.render() # this returns a buffer (PNG by default)
```

## Rescale non-byte data and/or apply colormap

```python
with COGReader(
  "s3://landsat-pds/c1/L8/015/029/LC08_L1GT_015029_20200119_20200119_01_RT/LC08_L1GT_015029_20200119_20200119_01_RT_B8.TIF",
  nodata=0,
) as cog:
    img = cog.tile(150, 187, 9)

    # Rescale the data from 0-10000 to 0-255
    image_rescale = img.post_process(in_range=(0, 10000), out_range=(0, 255))

    # Get Colormap
    cm = cmap.get("viridis")

    # Apply colormap and create a PNG buffer
    buff = image_rescale.render(colormap=cm) # this returns a buffer (PNG by default)
```

## Use creation options to match `mapnik` defaults.

```python
from rio_tiler.profiles import img_profiles

with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    img = cog.tile(691559, 956905, 21, tilesize=256)

    options = img_profiles.get("webp")

    print(options)
    >>> {'quality': 75, 'lossless': False}

    buff = img.render(img_format="webp", **options)
```

## Write image to file

```python
with open("my.png", "wb") as f:
  f.write(buff)
```

## NumpyTile

You can also export image data to a numpy binary format (`NPY`).

```python
with COGReader(
  "s3://landsat-pds/c1/L8/015/029/LC08_L1GT_015029_20200119_20200119_01_RT/LC08_L1GT_015029_20200119_20200119_01_RT_B8.TIF",
  nodata=0,
) as cog:
    img = cog.tile(150, 187, 9)

    buff = img.render(img_format="npy")

    npy_tile = numpy.load(BytesIO(buff))
    assert npy_tile.shape == (2, 256, 256)  # mask is appened to the end of the data

    buff = img.render(img_format="npy", add_mask=False)

    npy_tile = numpy.load(BytesIO(buff))
    assert npy_tile.shape == (1, 256, 256)
```

Learn more about the **NumpyTile** specification [here](https://github.com/planetlabs/numpytiles-spec).


## `rio-tiler`'s magic: Partial reading

When the output image size, or the AOI is smaller than the input image, `GDAL` will try to
perform *decimated and/or spatial reads* on the raster source, minimizing the amount data to transfer. Because of this, performance will be optimal when the source format permits efficient partial reads.

The [Cloud-Optimized GeoTIFF (COG)](https://www.cogeo.org/) format is the **recommended** format for rio-tiler because it's natively:
- internally tiled
- has a header with a `map` of all the tiles
- can have internal overviews

To learn more about efficiency of COG vs other file formats, check out [this blog post][vincent_s2_jp2_cost].

[vincent_s2_jp2_cost]: https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f