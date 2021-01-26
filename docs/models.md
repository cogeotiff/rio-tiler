
## ImageData

Reader methods returning image data  (`tile`, `part`, `feature` and `preview`) return a *data holding* class: `rio_tiler.models.ImageData`.

This class has helper methods like `render` which forward internal data and mask to `rio_tiler.utils.render` method, but also helps preserving geospatial informations (`bounds` and `crs`) about the data.

#### Attributes

- **data**: image data array (numpy.ndarray)
- **mask**: gdal/rasterio mask data array (numpy.ndarray)
- **assets**: assets list used to create the data array (list, optional)
- **bounds**: bounds of the data ([rasterio.coords.BoundingBox](https://github.com/mapbox/rasterio/blob/master/rasterio/coords.py#L8), optional)
- **crs**: coordinate reference system for the data ([rasterio.crs.CRS](https://github.com/mapbox/rasterio/blob/master/rasterio/crs.py#L21), optional)

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
image = img.post_process(in_range=(0, 3000))
assert isinstance(image, ImageData)

print(image.data.dtype)
>>> 'uint8'

print(image.data.max())
>>> 254

# rescale and apply rio-color formula
image = img.post_process(in_range=(0, 3000), color_formula="Gamma RGB 3.1")
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

## Others

Readers methods (`spatial_info`, `info`, `metadata` and `stats`) returning metadata like results return [pydantic](https://pydantic-docs.helpmanual.io) models to make sure the values are valids.

### SpatialInfo

```python
from rio_tiler.io import COGReader
from rio_tiler.models import SpatialInfo

# Schema
print(SpatialInfo.schema())
>>> {
    'title': 'SpatialInfo',
    'description': 'Dataset SpatialInfo',
    'type': 'object',
    'properties': {
        'bounds': {'title': 'Bounds', 'type': 'array', 'items': {}},
        'center': {
            'title': 'Center',
            'type': 'array',
            'items': [
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'type': 'integer'}
            ]
        },
        'minzoom': {'title': 'Minzoom', 'type': 'integer'},
        'maxzoom': {'title': 'Maxzoom', 'type': 'integer'}
    },
    'required': ['bounds', 'center', 'minzoom', 'maxzoom']
}

# Example
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    spatial_info = cog.spatial_info

print(spatial_info["minzoom"])
>>> 15

print(spatial_info.minzoom)
>>> 15

print(spatial_info.dict())
>>> {
    'bounds': (-61.28700187663819, 15.53775679445058, -61.27877967704676, 15.542486503997605),
    'center': (-61.28289077684248, 15.540121649224092, 15),
    'minzoom': 15,
    'maxzoom': 21
}
```

### Info

```python
from rio_tiler.io import COGReader
from rio_tiler.models import Info

# Schema
print(Info.schema())
>>> {
    'title': 'Info',
    'description': 'Dataset Info.',
    'type': 'object',
    'properties': {
        'bounds': {'title': 'Bounds', 'type': 'array', 'items': {}},
        'center': {
            'title': 'Center',
            'type': 'array',
            'items': [
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'type': 'integer'}
            ]
        },
        'minzoom': {'title': 'Minzoom', 'type': 'integer'},
        'maxzoom': {'title': 'Maxzoom', 'type': 'integer'},
        'band_metadata': {'title': 'Band Metadata', 'type': 'array', 'items': {'type': 'array', 'items': [{'type': 'string'}, {'type': 'object'}]}},
        'band_descriptions': {'title': 'Band Descriptions', 'type': 'array', 'items': {'type': 'array', 'items': [{'type': 'string'}, {'type': 'string'}]}},
        'dtype': {'title': 'Dtype', 'type': 'string'},
        'nodata_type': {'$ref': '#/definitions/NodataTypes'},
        'colorinterp': {'title': 'Colorinterp', 'type': 'array', 'items': {'type': 'string'}},
        'scale': {'title': 'Scale', 'type': 'number'},
        'offset': {'title': 'Offset', 'type': 'number'},
        'colormap': {'title': 'Colormap', 'type': 'object', 'additionalProperties': {'type': 'array', 'items': [{'type': 'integer'}, {'type': 'integer'}, {'type': 'integer'}, {'type': 'integer'}]}}
    },
    'required': ['bounds', 'center', 'minzoom', 'maxzoom', 'band_metadata', 'band_descriptions', 'dtype', 'nodata_type'],
    'definitions': {
        'NodataTypes': {'title': 'NodataTypes', 'description': 'rio-tiler Nodata types.', 'enum': ['Alpha', 'Mask', 'Internal', 'Nodata', 'None'], 'type': 'string'}
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

print(info.dict(exclude_none=True))
>>> {
    'bounds': (-61.28700187663819, 15.53775679445058, -61.27877967704676, 15.542486503997605),
    'center': (-61.28289077684248, 15.540121649224092, 15),
    'minzoom': 15,
    'maxzoom': 21,
    'band_metadata': [('1', {}), ('2', {}), ('3', {})],
    'band_descriptions': [('1', ''), ('2', ''), ('3', '')],
    'dtype': 'uint8',
    'nodata_type': 'None',
    'colorinterp': ['red', 'green', 'blue']
}
```

### Metadata

```python
from rio_tiler.io import COGReader
from rio_tiler.models import Metadata

# Schema
print(Metadata.schema())
>>> {
    'title': 'Metadata',
    'description': 'Dataset metadata and statistics.',
    'type': 'object',
    'properties': {
        'bounds': {'title': 'Bounds', 'type': 'array', 'items': {}},
        'center': {
            'title': 'Center',
            'type': 'array',
            'items': [
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                {'type': 'integer'}
            ]
        },
        'minzoom': {'title': 'Minzoom', 'type': 'integer'},
        'maxzoom': {'title': 'Maxzoom', 'type': 'integer'},
        'band_metadata': {'title': 'Band Metadata', 'type': 'array', 'items': {'type': 'array', 'items': [{'type': 'string'}, {'type': 'object'}]}},
        'band_descriptions': {'title': 'Band Descriptions', 'type': 'array', 'items': {'type': 'array', 'items': [{'type': 'string'}, {'type': 'string'}]}},
        'dtype': {'title': 'Dtype', 'type': 'string'},
        'nodata_type': {'$ref': '#/definitions/NodataTypes'},
        'colorinterp': {'title': 'Colorinterp', 'type': 'array', 'items': {'type': 'string'}},
        'scale': {'title': 'Scale', 'type': 'number'},
        'offset': {'title': 'Offset', 'type': 'number'},
        'colormap': {'title': 'Colormap', 'type': 'object', 'additionalProperties': {'type': 'array', 'items': [{'type': 'integer'}, {'type': 'integer'}, {'type': 'integer'}, {'type': 'integer'}]}}
        'statistics': {
            'title': 'Statistics', 'type': 'object', 'additionalProperties': {'$ref': '#/definitions/ImageStatistics'}
        }
    },
    'required': ['bounds', 'center', 'minzoom', 'maxzoom', 'band_metadata', 'band_descriptions', 'dtype', 'nodata_type', 'statistics'],
    'definitions': {
        'NodataTypes': {'title': 'NodataTypes', 'description': 'rio-tiler Nodata types.', 'enum': ['Alpha', 'Mask', 'Internal', 'Nodata', 'None'], 'type': 'string'},
        'ImageStatistics': {
            'title': 'ImageStatistics',
            'description': 'Image statistics',
            'type': 'object',
            'properties': {
                'percentiles': {'title': 'Percentiles','type': 'array', 'items': {'anyOf': [{'type': 'number'}, {'type': 'integer'}]}},
                'min': {'title': 'Min', 'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                'max': {'title': 'Max', 'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                'std': {'title': 'Std', 'anyOf': [{'type': 'number'}, {'type': 'integer'}]},
                'histogram': {
                    'title': 'Histogram', 'type': 'array', 'items': {'type': 'array', 'items': {'anyOf': [{'type': 'number'}, {'type': 'integer'}]}}
                }
            },
            'required': ['percentiles', 'min', 'max', 'std', 'histogram']
        }
    }
}

# Example
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as cog:
    metadata = cog.metadata()

print(metadata["statistics"]["1"]["min"])
>>> 0.0

print(metadata.statistics["1"].min)
>>> 0.0

print(metadata.dict(exclude_none=True))
>>> {
    'bounds': (-61.28700187663819, 15.53775679445058, -61.27877967704676, 15.542486503997605),
    'center': (-61.28289077684248, 15.540121649224092, 15),
    'minzoom': 15,
    'maxzoom': 21,
    'band_metadata': [('1', {}), ('2', {}), ('3', {})],
    'band_descriptions': [('1', ''), ('2', ''), ('3', '')],
    'dtype': 'uint8',
    'nodata_type': 'None',
    'colorinterp': ['red', 'green', 'blue'],
    'statistics': {
        '1': {
            'percentiles': [0.0, 228.0],
            'min': 0.0,
            'max': 255.0,
            'std': 59.261322978176324,
            'histogram': [
                [100540.0,43602.0, 87476.0, 112587.0, 107599.0, 73453.0, 43623.0, 21971.0, 15006.0, 11615.0],
                [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0]
            ]
        },
        '2': {
            'percentiles': [0.0, 231.0],
            'min': 0.0,
            'max': 255.0,
            'std': 58.768241799458224,
            'histogram': [
                [95196.0, 33243.0, 67186.0, 116180.0, 128328.0, 82649.0, 45167.0, 22637.0, 13985.0, 12901.0],
                [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0]
            ]
        },
        '3': {
            'percentiles': [0.0, 232.0],
            'min': 0.0,
            'max': 255.0,
            'std': 57.85261614653745,
            'histogram': [
                [122393.0, 94783.0, 136757.0, 100639.0, 63487.0, 32661.0, 24458.0, 16910.0, 11900.0, 13484.0],
                [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0]
            ]
        }
    }
}
```

## Links

**Attrs** - Classes Without Boilerplate [https://www.attrs.org/en/stable/](https://www.attrs.org/en/stable/)

**Pydantic** - Define how data should be in pure, canonical python [https://pydantic-docs.helpmanual.io](https://pydantic-docs.helpmanual.io)
