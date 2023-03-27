
`rio-tiler` version 5.0 introduced [many breaking changes](release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 5.0.


## **PER_DATASET** -> **PER_BAND** mask

When we started to work on rio-tiler we chose to use `PER_DATASET` mask, a 2D `(height, width)` array which represent the masked array for the whole dataset, as `Alpha` or `Mask` bands are designed for.
The `PER_DATASET` model suffers precision when dealing with datasets that use `nodata` value because combining all `band nodata mask` will exclude good data (see https://github.com/cogeotiff/rio-tiler/issues/579#issuecomment-1455223893).

To support the `PER_BAND` model, we updated the `ImageData` class to use `numpy.ma.MaskedArray` which will hold both the data and the mask with the same shape. The `image data` is now hosted in `.array` ImageData/PointData attribute.

```python
# before
with COGReader("cog.tif") as src:
    img = src.preview(width=128, height=128, max_size=None)
    assert isinstance(img.data, numpy.ndarray)
    assert img.data.shape == (3, 128, 128)

    assert isinstance(img.mask, numpy.ndarray)
    assert img.mask.shape == (128, 128)

# now
with COGReader("cog.tif") as src:
    img = src.preview(width=128, height=128, max_size=None)
    assert isinstance(img.array, numpy.ma.MaskedArray)
    assert img.array.data.shape == (3, 128, 128)
    assert img.array.mask.shape == (3, 128, 128)
```

For compatibility reason we kept `data` and `mask` as *properties* in the `ImageData` class. `ImageData().mask` will represent the `PER_DATASET` mask.

```python
with COGReader("cog.tif") as src:
    img = src.preview(width=128, height=128, max_size=None)
    assert isinstance(img.array, numpy.ma.MaskedArray)

    assert img.data.shape == (3, 128, 128)
    assert img.mask.shape == (128, 128)
```

## ImageData/PointData

As explained, the `ImageData` and `PointData` classes now use `MaskedArray` as input.


```python
# before
arr = numpy.zeros((1, 256, 256))
mask = numpy.zeros((256, 256), dtype="uint8")
im = ImageData(arr, mask)

# now
arr = numpy.ma.MaskedArray(numpy.zeros((1, 256, 256)))
arr.mask = False
im = ImageData(arr)
```


## post_process callback

Introduced in `2.0`, `rio-tiler`'s low level reader (`rio_tiler.reader.read`) accept a `post_process` option which should be a Callable that take some data as input and returns modified data. Because of the changes in ImageData input type (now as MaskedArray), the `post_process` callback should be design to be of type `Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray]`.


```python
# before
def callback(data: numpy.ndarray, mask: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray]:
    mask.fill(255)
    data = data * 2
    return data, mask

with Reader("cog.tif") as src:
    im = src.preview(post_process=callback)

# now
def callback(data: numpy.ma.MaskedArray) -> numpy.ma.MaskedArray:
    data = data * 2
    return data

with Reader("cog.tif") as src:
    im = src.preview(post_process=callback)
```


## MosaicMethod

The `.data` property of `rio-tiler`'s MosaicMethods should now return `numpy.ma.MaskedArray`. This change should be almost non-breaking because the MosaicMethod where designed using MaskedArrays.

```python
# before
def data(self) -> Tuple[Optional[numpy.ndarray], Optional[numpy.ndarray]]:
    """Return data and mask."""
    if self.tile is not None:
        data = numpy.ma.getdata(self.tile)
        mask = ~numpy.logical_or.reduce(numpy.ma.getmaskarray(self.tile))  # create PER_DATASET Mask
        return (data, mask * numpy.uint8(255))

    else:
        return None, None

# now
@property
def data(self) -> Optional[numpy.ma.MaskedArray]:
    """Return data."""
    return self.tile
```

## Reprojection and Resizing resampling methods

With `rio-tiler >=5.0`, you can now select with resampling method to use for the `reprojection` and `resizing` processes independently by using the `reproject_method` and `resampling_method` options in `rio_tiler.reader`'s function.

The `resampling_method` option will control the `IO` resampling (e.g resizing) while the `reproject_method` will be using in the `WarpedVRT` for the reprojection.

```python
# before
with Reader("cog.tif") as src:
    im = src.preview(
        dst_crs="epsg:4326",
        resampling_method="bilinear",  # use `bilinear` for both resizing and reprojection
    )

# now
with Reader("cog.tif") as src:
    im = src.preview(
        dst_crs="epsg:4326",
        resampling_method="cubic",  # use `cubic` for resizing
        reproject_method="bilinear",  # use `bilinear` for reprojection
    )
```


!!! Important
    In the `XarrayReader` we are still using only one `resampling_method` option because we are using `rioxarray` for read and reprojection processes and it does not have both options available.
