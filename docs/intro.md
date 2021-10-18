
## Read data

```python
from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

tile_x = 691559
tile_y = 956905
tile_zoom = 21

with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    # Read data for a slippy map tile
    img = cog.tile(tile_x, tile_y, tile_zoom, tilesize=256)
    assert isinstance(img, ImageData)

    print(img.data.shape)
    >>> (3, 256, 256)
    print(img.mask.shape)
    >>> (256, 256)

    # Read the entire data
    img = cog.read()
    print(img.data.shape)
    >>> (3, 11666, 19836)

    # Read part of a data for a given bbox (we use `max_size=1024` to limit the data transfer and read lower resolution data)
    img = cog.part([-61.281, 15.539, -61.279, 15.541], max_size=1024)
    print(img.data.shape)
    >>> (3, 1024, 1024)

    # Read data for a given geojson polygon (we use `max_size=1024` to limit the data transfer and read lower resolution data)
    img = cog.feature(geojson_feature, max_size=1024)

    # Get a preview (size is maxed out to 1024 by default to limit the data transfer and read lower resolution data)
    img = cog.preview()
    print(img.data.shape)
    >>> (3, 603, 1024)

    # Get pixel values for a given lon/lat coordinate
    values = cog.point(-61.281, 15.539)
    print(values)
    >>> [47, 62, 43]

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
    image_rescale = img.post_process(
        in_range=((0, 10000),),
        out_range=((0, 255),),
    )

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

Note: Starting with `rio-tiler==2.1`, when the output datatype is not valid for a driver (e.g `float` for `PNG`),
`rio-tiler` will automatically rescale the data using the `min/max` value for the datatype (ref: https://github.com/cogeotiff/rio-tiler/pull/391).

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
