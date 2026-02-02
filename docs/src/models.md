
## ImageData

Reader methods returning image data  (`tile`, `part`, `feature` and `preview`) return a *data holding* class: `rio_tiler.models.ImageData`.

This class has helper methods like `render` which forward internal data and mask to `rio_tiler.utils.render` method, but also helps preserving geospatial information (`bounds` and `crs`) about the data.

#### Attributes

- **array**: image array (numpy.ma.MaskedArray)
- **assets**: assets list used to create the data array (list, optional)
- **bounds**: bounds of the data ([rasterio.coords.BoundingBox](https://github.com/rasterio/rasterio/blob/main/rasterio/coords.py#L8), optional)
- **crs**: coordinate reference system for the data ([rasterio.crs.CRS](https://github.com/rasterio/rasterio/blob/main/rasterio/crs.py#L21), optional)
- **metadata**: additional metadata (dict, optional)
- **band_names**: image band's names (e.g `["b1", "b2"]`)
- **band_descriptions**: image band's descriptions (e.g `["Green", "Red"]`)
- **dataset_statistics**: Dataset's min/max values (list of (min,max), optional)
- **cutline_mask**: array representing the mask for `feature` methods
- **alpha_nask**: array reprsenting the alpha mask (allowing partial transparency)

```python
import numpy
from rio_tiler.models import ImageData

d = numpy.zeros((3, 256, 256))
m = numpy.zeros((3, 256, 256), dtype="bool")

data = numpy.ma.MaskedArray(d, mask=m)

print(ImageData(data))
>>> ImageData(
    array=masked_array(...),
    assets=None,
    bounds=None,
    crs=None,
    metadata={},
    band_names=['b1', 'b2', 'b3'],
    dataset_statistics=None,
    cutline_mask=array(),
)
```


#### Properties

- **width**: number of column in the data array (int)
- **height**: number of row in the data array (int)
- **count**: number of bands in the data array (int)
- **transform**: Affine transform created from the bounds and crs ([affine.Affine](https://github.com/sgillies/affine/blob/master/affine/__init__.py#L116))
- **data**: Return data part of the masked array.
- **mask**: Return the mask part in form of rasterio dataset mask.

#### ClassMethods

- **from_bytes()**: Create an ImageData instance from a Raster buffer

    ```python
    with open("img.tif", "rb") as f:
        img = ImageData.from_bytes(f.read())
    ```

- **create_from_list()**: Create ImageData from a sequence of ImageData objects.

    ```python
    r = ImageData(numpy.zeros((1, 256, 256)))
    g = ImageData(numpy.zeros((1, 256, 256)))
    b = ImageData(numpy.zeros((1, 256, 256)))

    img = ImageData.create_from_list([r, g, b])
    ```

#### Methods

- **data_as_image()**: Return the data array reshaped into an image processing/visualization software friendly order

    ```python
    import numpy
    from rio_tiler.models import ImageData

    d = numpy.zeros((3, 256, 256))
    m = numpy.zeros((3, 256, 256), dtype="bool")
    data = numpy.ma.MaskedArray(d, mask=m)

    img = ImageData(data)
    print(img.data.shape)
    >>> (3, 256, 256)

    image = img.data_as_image()
    print(image.shape)
    >>> (256, 256, 3)
    ```

- **clip()**: Clip data and mask to a bbox (in the ImageData CRS).

    !!! info "New in version 4.0.0"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.zeros((3, 1024, 1024), dtype="uint8")
    img = ImageData(data, crs="epsg:4326", bounds=(-180, -90, 180, 90))

    img_c = img.clip((-100, -50, 100, 50))
    assert img_c.count == 3
    assert img_c.bounds == (-100, -50, 100, 50)
    ```

- **resize()**: Resize data and mask.

    !!! info "New in version 4.0.0"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.zeros((3, 1024, 1024), dtype="uint8")
    img = ImageData(data)

    img_r = img.resize(256, 256)
    assert img_r.count == 3
    assert img_r.width == 256
    assert img_r.height == 256
    ```

- **reproject()**: Reproject the ImageData to a user defined projection

    ```python
    data = numpy.zeros((3, 1024, 1024), dtype="uint8")
    img = ImageData(data, crs="epsg:4326", bounds=(-180, -90, 180, 90))
    img = img.reproject(dst_crs="epsg:3857")
    ```

- **post_process()**: Apply rescaling or/and `color-operations` formula to the data array. Returns a new ImageData instance.

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.random.randint(0, 3000, (3, 256, 256))
    img = ImageData(data)

    print(img.data.dtype)
    >>> 'int64'

    print(img.data.max())
    >>> 2999

    # rescale the data from 0 -> 3000 to 0 -> 255
    # by default rio-tiler will apply the same `in_range` for all the bands
    image = img.post_process(in_range=((0, 3000),))

    # or provide range for each bands
    image = img.post_process(in_range=((0, 3000), (0, 1000), (0, 2000)))

    assert isinstance(image, ImageData)

    print(image.data.dtype)
    >>> 'uint8'

    print(image.data.max())
    >>> 254

    # rescale and apply color-operations formula
    image = img.post_process(
        in_range=((0, 3000),),
        color_formula="Gamma RGB 3.1",
    )
    assert isinstance(image, ImageData)
    ```

- **statistics()**: Return statistics from ImageData.

    !!! info "New in version 4.1.7"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.zeros((1, 256, 256), dtype="uint8")
    data[0, 0:10, 0:10] = 0
    data[0, 10:11, 10:11] = 100
    img = ImageData(data)
    stats = img.statistics(categorical=True)

    print(stats["b1"].min)
    >>> 0

    print(stats["b1"].max)
    >>> 100

    print(stats["b1"].majority)
    >>> 0

    print(stats["b1"].minority)
    >>> 100

    print(stats["b1"].unique)
    >>> 2.0
    ```

- **rescale()**: linear rescaling of the data in place

    !!! info "New in version 3.1.5"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.random.randint(0, 3000, (3, 256, 256))
    img = ImageData(data)

    print(img.data.dtype)
    >>> 'int64'

    print(img.data.max())
    >>> 2999

    # rescale and apply color-operations formula
    img.rescale(in_range=((0, 3000),),)
    print(img.data.max())
    >>> 254

    print(img.data.dtype)
    >>> 'uint8'
    ```

- **apply_color_formula()**: Apply `color-operations`'s color formula in place

    !!! info "New in version 3.1.5"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.random.randint(0, 16000, (3, 256, 256)).astype("uint16")
    img = ImageData(data)

    print(img.data.dtype)
    >>> 'uint16'

    img.apply_color_formula("Gamma RGB 3.5")
    print(img.data.dtype)
    >>> 'uint8'

    print(img.data.max())
    >>> 170
    ```

- **apply_colormap()**: Apply colormap to the image data

    !!! info "New in version 4.1.6"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    cm = {0: (0, 0, 0, 255), 1: (255, 255, 255, 255)}
    im = ImageData(numpy.zeros((1, 256, 256), dtype="uint8")).apply_colormap(cm)
    assert im.data.shape == (3, 256, 256)
    assert im.data[:, 0, 0].tolist() == [0, 0, 0]
    assert im.mask[0, 0] == 255
    assert im.mask.all()
    ```

- **apply_expression()**: Apply band math expression

    !!! info "New in version 4.0"

    ```python
    import numpy
    from rio_tiler.models import ImageData

    data = numpy.random.randint(0, 3000, (3, 256, 256))

    img = ImageData(data)
    print(img.band_names)
    >>> ["b1", "b2", "b3"]  # Defaults

    ratio = img.apply_expression("b1/b2")  # Returns a new ImageData object
    assert isinstance(ratio, ImageData)

    print(ratio.band_descriptions)
    >>> ["b1/b2"]

    print(ratio.data.shape)
    >>> (1, 256, 256)
    ```

- **render()**: Render the data/mask to an image buffer (forward data and mask to rio_tiler.utils.render).

    ```python
    import numpy
    from rasterio.io import MemoryFile
    from rio_tiler.models import ImageData

    def get_meta(content):
        with MemoryFile(content) as mem:
            with mem.open() as dst:
                return dst.meta

    data = numpy.zeros((3, 256, 256), dtype="uint8")

    img = ImageData(data)

    # create a PNG image
    buf = img.render(img_format="png")
    print(get_meta(buf))
    >>> {
        'driver': 'PNG',
        'dtype': 'uint8',
        'nodata': None,
        'width': 256,
        'height': 256,
        'count': 4,
        'crs': None,
        'transform': Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    }

    # create a JPEG image
    buf = img.render(img_format="jpeg")
    print(get_meta(buf))
    >>> {
        'driver': 'JPEG',
        'dtype': 'uint8',
        'nodata': None,
        'width': 256,
        'height': 256,
        'count': 3,
        'crs': None,
        'transform': Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    }
    ```

Note: Starting with `rio-tiler==2.1`, when the output datatype is not valid for a driver (e.g `float` for `PNG`),
`rio-tiler` will automatically rescale the data using the `min/max` value for the datatype (ref: https://github.com/cogeotiff/rio-tiler/pull/391).


- **to_raster()**: Save ImageData array to raster file

    ```python
    img = ImageData(numpy.zeros((1, 256, 256)))
    img.to_raster("img.tif", driver="GTiff")
    ```

## PointData

!!! info "New in version 4.0"

#### Attributes

- **array**: image array (numpy.ma.MaskedArray)
- **assets**: assets list used to create the data array (list, optional)
- **coordinates**: Coordinates of the point (Tuple[float, float], optional)
- **crs**: coordinate reference system for the data ([rasterio.crs.CRS](https://github.com/rasterio/rasterio/blob/master/rasterio/crs.py#L21), optional)
- **metadata**: additional metadata (dict, optional)
- **band_names**: image band's names (e.g `["b1", "b2"]`)
- **band_descriptions**: image band's descriptions (e.g `["Green", "Red"]`)
- **pixel_location**: X, Y coordinates in raster space (Tuple[float, float], optional)

```python
import numpy
from rio_tiler.models import PointData

d = numpy.zeros((3))
m = numpy.zeros((1), dtype="bool")

data = numpy.ma.MaskedArray(d, mask=m)

print(PointData(data))
>>> PointData(
    array=masked_array(data=[0.0, 0.0, 0.0], mask=[False, False, False], fill_value=1e+20),
    band_names=['b1', 'b2', 'b3'],
    coordinates=None,
    crs=None,
    assets=None,
    metadata={},
)
)
```

#### Properties

- **count**: number of bands in the data array (int)
- **data**: Return data part of the masked array.
- **mask**: Return the mask part in form of rasterio dataset mask.

#### Methods

- **apply_expression()**: Apply band math expression

```python
import numpy
from rio_tiler.models import PointData

data = numpy.random.randint(0, 3000, (3))

pts = PointData(data)
print(pts.band_names)
>>> ["b1", "b2", "b3"]  # Defaults

ratio = pts.apply_expression("b1/b2")  # Returns a new PointData object
assert isinstance(ratio, PointData)

print(ratio.band_names)
>>> ["b1/b2"]

print(ratio.count)
>>> 1
```

## Others

Readers methods returning metadata like results (`info()` and `statistics()`) return [pydantic](https://pydantic-docs.helpmanual.io) models to make sure the values are valids.

### Info

```python
from rio_tiler.io import Reader
from rio_tiler.models import Info

# Schema
print(Info.schema())
>>> {
    "$defs": {
        "BoundingBox": {
            "maxItems": 4,
            "minItems": 4,
            "prefixItems": [
                {
                    "title": "Left"
                },
                {
                    "title": "Bottom"
                },
                {
                    "title": "Right"
                },
                {
                    "title": "Top"
                }
            ],
            "type": "array"
        }
    },
    "additionalProperties": true,
    "description": "Dataset Info.",
    "properties": {
        "bounds": {
            "$ref": "#/$defs/BoundingBox"
        },
        "crs": {
            "title": "Crs",
            "type": "string"
        },
        "band_metadata": {
            "items": {
                "maxItems": 2,
                "minItems": 2,
                "prefixItems": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            "title": "Band Metadata",
            "type": "array"
        },
        "band_descriptions": {
            "items": {
                "maxItems": 2,
                "minItems": 2,
                "prefixItems": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            "title": "Band Descriptions",
            "type": "array"
        },
        "dtype": {
            "title": "Dtype",
            "type": "string"
        },
        "nodata_type": {
            "enum": [
                "Alpha",
                "Mask",
                "Internal",
                "Nodata",
                "None"
            ],
            "title": "Nodata Type",
            "type": "string"
        },
        "colorinterp": {
            "anyOf": [
                {
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "title": "Colorinterp"
        },
        "scales": {
            "anyOf": [
                {
                    "items": {
                        "type": "number"
                    },
                    "type": "array"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "title": "Scales"
        },
        "offsets": {
            "anyOf": [
                {
                    "items": {
                        "type": "number"
                    },
                    "type": "array"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "title": "Offsets"
        },
        "colormap": {
            "anyOf": [
                {
                    "additionalProperties": {
                        "maxItems": 4,
                        "minItems": 4,
                        "prefixItems": [
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    },
                    "type": "object"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "title": "Colormap"
        }
    },
    "required": [
        "bounds",
        "crs",
        "band_metadata",
        "band_descriptions",
        "dtype",
        "nodata_type"
    ],
    "title": "Info",
    "type": "object"
}

# Example
with Reader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as src:
    info = src.info()

print(info.nodata_type)
>>> "None"

print(info.model_dump_json(exclude_none=True))
>>> {
    "bounds": [
        683715.3266400001,
        1718548.5702,
        684593.2680000002,
        1719064.90736
    ],
    "crs": "http://www.opengis.net/def/crs/EPSG/0/32620",
    "band_metadata": [
        [
            "b1",
            {}
        ],
        [
            "b2",
            {}
        ],
        [
            "b3",
            {}
        ]
    ],
    "band_descriptions": [
        [
            "b1",
            ""
        ],
        [
            "b2",
            ""
        ],
        [
            "b3",
            ""
        ]
    ],
    "dtype": "uint8",
    "nodata_type": "Mask",
    "colorinterp": [
        "red",
        "green",
        "blue"
    ],
    "scales": [
        1,
        1,
        1
    ],
    "offsets": [
        0,
        0,
        0
    ],
    "driver": "GTiff",
    "count": 3,
    "width": 19836,
    "height": 11666,
    "overviews": [
        2,
        4,
        8,
        16,
        32,
        64
    ]
}
```

Note: starting with `rio-tiler>=2.0.8`, additional metadata can be set (e.g. driver, count, width, height, overviews in `Reader.info()`)

### BandStatistics

```python
from rio_tiler.io import Reader
from rio_tiler.models import BandStatistics

# Schema
print(BandStatistics.schema())
>>> {
    "title": "BandStatistics",
    "description": "Image statistics",
    "type": "object",
    "properties": {
        "min": {
            "title": "Min",
            "type": "number"
        },
        "max": {
            "title": "Max",
            "type": "number"
        },
        "mean": {
            "title": "Mean",
            "type": "number"
        },
        "count": {
            "title": "Count",
            "type": "number"
        },
        "sum": {
            "title": "Sum",
            "type": "number"
        },
        "std": {
            "title": "Std",
            "type": "number"
        },
        "median": {
            "title": "Median",
            "type": "number"
        },
        "majority": {
            "title": "Majority",
            "type": "number"
        },
        "minority": {
            "title": "Minority",
            "type": "number"
        },
        "unique": {
            "title": "Unique",
            "type": "number"
        },
        "histogram": {
            "title": "Histogram",
            "type": "array",
            "items": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "type": "number"
                        },
                        {
                            "type": "integer"
                        }
                    ]
                }
            }
        },
        "valid_percent": {
            "title": "Valid Percent",
            "type": "number"
        },
        "masked_pixels": {
            "title": "Masked Pixels",
            "type": "number"
        },
        "valid_pixels": {
            "title": "Valid Pixels",
            "type": "number"
        }
    },
    "required": [
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "histogram",
        "valid_percent",
        "masked_pixels",
        "valid_pixels"
    ]
}

# Example
with Reader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as src:
    stats = src.statistics()
    assert isinstance(stats["b1"], BandStatistics)

print(stats["b1"].min)
>>> 0.0

print(stats["b1"].model_dump_json(exclude_none=True))
>>> {
    "min": 0,
    "max": 255,
    "mean": 93.16424226523633,
    "count": 617472,
    "sum": 57526311,
    "std": 59.261322978176324,
    "median": 94,
    "majority": 0,
    "minority": 253,
    "unique": 256,
    "histogram": [
        [
            100540,
            43602,
            87476,
            112587,
            107599,
            73453,
            43623,
            21971,
            15006,
            11615
        ],
        [
            0,
            25.5,
            51,
            76.5,
            102,
            127.5,
            153,
            178.5,
            204,
            229.5,
            255
        ]
    ],
    "valid_percent": 100,
    "masked_pixels": 0,
    "valid_pixels": 617472,
    "percentile_2": 0,
    "percentile_98": 228
}
```

## Links

**Attrs** - Classes Without Boilerplate [https://www.attrs.org/en/stable/](https://www.attrs.org/en/stable/)

**Pydantic** - Define how data should be in pure, canonical python [https://pydantic-docs.helpmanual.io](https://pydantic-docs.helpmanual.io)
