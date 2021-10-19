
## ImageData

Reader methods returning image data  (`tile`, `part`, `feature` and `preview`) return a *data holding* class: `rio_tiler.models.ImageData`.

This class has helper methods like `render` which forward internal data and mask to `rio_tiler.utils.render` method, but also helps preserving geospatial informations (`bounds` and `crs`) about the data.

#### Attributes

- **data**: image data array (numpy.ndarray)
- **mask**: gdal/rasterio mask data array (numpy.ndarray)
- **assets**: assets list used to create the data array (list, optional)
- **bounds**: bounds of the data ([rasterio.coords.BoundingBox](https://github.com/mapbox/rasterio/blob/master/rasterio/coords.py#L8), optional)
- **crs**: coordinate reference system for the data ([rasterio.crs.CRS](https://github.com/mapbox/rasterio/blob/master/rasterio/crs.py#L21), optional)
- **metadata**: additional metadata (dict, optional)
- **band_names**: image band's names

```python
import numpy
from rio_tiler.models import ImageData

d = numpy.zeros((3, 256, 256))
m = numpy.zeros((256, 256)) + 255

print(ImageData(d, m))
>>> ImageData(
    data=array(...),
    mask=array(...),
    assets=None,
    bounds=None,
    crs=None,
    metadata={},
    band_names=['1', '2', '3'],
)
```


#### Properties

- **width**: number of column in the data array (int)
- **height**: number of row in the data array (int)
- **count**: number of bands in the data array (int)
- **transform**: Affine transform created from the bounds and crs ([affine.Affine](https://github.com/sgillies/affine/blob/master/affine/__init__.py#L116))

#### Methods

- **as_masked()**: Return the data array as a `numpy.ma.MaskedArray`

```python
import numpy
from rio_tiler.models import ImageData

d = numpy.zeros((3, 256, 256))
m = numpy.zeros((256, 256)) + 255

masked = ImageData(d, m).as_masked()
print(type(masked))
>>> numpy.ma.core.MaskedArray
```

- **data_as_image()**: Return the data array reshaped into an image processing/visualization software friendly order

```python
import numpy
from rio_tiler.models import ImageData

d = numpy.zeros((3, 256, 256))
m = numpy.zeros((256, 256)) + 255

img = ImageData(d, m)
print(img.data.shape)
>>> (3, 256, 256)

image = img.data_as_image()
print(image.shape)
>>> (256, 256, 3)
```

- **post_process()**: Apply rescaling or/and rio-color formula to the data array. Returns a new ImageData instance.

```python
import numpy
from rio_tiler.models import ImageData

d = numpy.random.randint(0, 3000, (3, 256, 256))
m = numpy.zeros((256, 256)) + 255

img = ImageData(d, m)

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

# rescale and apply rio-color formula
image = img.post_process(
    in_range=((0, 3000),),
    color_formula="Gamma RGB 3.1",
)
assert isinstance(image, ImageData)
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

d = numpy.zeros((3, 256, 256), dtype="uint8")
m = numpy.zeros((256, 256)) + 255

img = ImageData(d, m)

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

## Others

Readers methods (`info`, `metadata` and `stats`) returning metadata like results return [pydantic](https://pydantic-docs.helpmanual.io) models to make sure the values are valids.

### Info

```python
from rio_tiler.io import COGReader
from rio_tiler.models import Info

# Schema
print(Info.schema())
>>> {
    "title": "Info",
    "description": "Dataset Info.",
    "type": "object",
    "properties": {
        "bounds": {
            "title": "Bounds",
            "type": "array",
            "items": [
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
            ]
        },
        "minzoom": {
            "title": "Minzoom",
            "type": "integer"
        },
        "maxzoom": {
            "title": "Maxzoom",
            "type": "integer"
        },
        "band_metadata": {
            "title": "Band Metadata",
            "type": "array",
            "items": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "object"
                    }
                ]
            }
        },
        "band_descriptions": {
            "title": "Band Descriptions",
            "type": "array",
            "items": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "string"
                    }
                ]
            }
        },
        "dtype": {
            "title": "Dtype",
            "type": "string"
        },
        "nodata_type": {
            "$ref": "#/definitions/NodataTypes"
        },
        "colorinterp": {
            "title": "Colorinterp",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "scale": {
            "title": "Scale",
            "type": "number"
        },
        "offset": {
            "title": "Offset",
            "type": "number"
        },
        "colormap": {
            "title": "Colormap",
            "type": "object",
            "additionalProperties": {
                "type": "array",
                "items": [
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
                ]
            }
        }
    },
    "required": [
        "bounds",
        "minzoom",
        "maxzoom",
        "band_metadata",
        "band_descriptions",
        "dtype",
        "nodata_type"
    ],
    "definitions": {
        "NodataTypes": {
            "title": "NodataTypes",
            "description": "rio-tiler Nodata types.",
            "enum": [
                "Alpha",
                "Mask",
                "Internal",
                "Nodata",
                "None"
            ],
            "type": "string"
        }
    }
}

# Example
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    info = cog.info()

print(info["nodata_type"])
>>> "None"

print(info.nodata_type)
>>> "None"

print(info.json(exclude_none=True))
>>> {
    'bounds': [-61.287001876638215, 15.537756794450583, -61.27877967704677, 15.542486503997608],
    'minzoom': 16,
    'maxzoom': 22,
    'band_metadata': [('1', {}), ('2', {}), ('3', {})],
    'band_descriptions': [('1', ''), ('2', ''), ('3', '')],
    'dtype': 'uint8',
    'nodata_type': 'None',
    'colorinterp': ['red', 'green', 'blue'],
    'count': 3,
    'driver': 'GTiff',
    'height': 11666,
    'overviews': [2, 4, 8, 16, 32, 64],
    'width': 19836
}
```

Note: starting with `rio-tiler>=2.0.8`, additional metadata can be set (e.g. driver, count, width, height, overviews in `COGReader.info()`)

### BandStatistics

```python
from rio_tiler.io import COGReader
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
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    stats = cog.statistics()
    assert isinstance(stats["1"], BandStatistics)

print(stats["1"]["min"])
>>> 0.0

print(stats["1"].min)
>>> 0.0

print(stats["1"].json(exclude_none=True))
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
