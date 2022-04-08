# Module rio_tiler.models

rio-tiler models.

None

## Variables

```python3
dtype_ranges
```

## Functions

    
### to_coordsbbox

```python3
def to_coordsbbox(
    bbox
) -> Union[rasterio.coords.BoundingBox, NoneType]
```

    
Convert bbox to CoordsBbox nameTuple.

## Classes

### BandStatistics

```python3
class BandStatistics(
    __pydantic_self__,
    **data: Any
)
```

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

    
Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

    
Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

    

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    update: 'DictStrAny' = None,
    deep: bool = False
) -> 'Model'
```

    
Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

    
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

    
Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### Bounds

```python3
class Bounds(
    __pydantic_self__,
    **data: Any
)
```

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.SpatialInfo

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

    
Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

    
Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

    

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    update: 'DictStrAny' = None,
    deep: bool = False
) -> 'Model'
```

    
Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

    
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

    
Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### ImageData

```python3
class ImageData(
    data: numpy.ndarray,
    mask: numpy.ndarray = NOTHING,
    assets: Union[List, NoneType] = None,
    bounds=None,
    crs: Union[rasterio.crs.CRS, NoneType] = None,
    metadata: Union[Dict, NoneType] = NOTHING,
    band_names: Union[List[str], NoneType] = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | pixel values. | None |
| mask | numpy.ndarray | rasterio mask values. | None |
| assets | list | list of assets used to construct the data values. | None |
| bounds | BoundingBox | bounding box of the data. | None |
| crs | rasterio.crs.CRS | Coordinates Reference System of the bounds. | None |
| metadata | dict | Additional metadata. Defaults to `{}`. | `{}` |
| band_names | list | name of each band. Defaults to `["1", "2", "3"]` for 3 bands image. | `["1", "2", "3"]` for 3 bands image |

#### Static methods

    
#### create_from_list

```python3
def create_from_list(
    data: Sequence[ForwardRef('ImageData')]
)
```

    
Create ImageData from a sequence of ImageData objects.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | sequence | sequence of ImageData. | None |

#### Instance variables

```python3
count
```

Number of band.

```python3
height
```

Height of the data array.

```python3
transform
```

Returns the affine transform.

```python3
width
```

Width of the data array.

#### Methods

    
#### as_masked

```python3
def as_masked(
    self
) -> numpy.ma.core.MaskedArray
```

    
return a numpy masked array.

    
#### data_as_image

```python3
def data_as_image(
    self
) -> numpy.ndarray
```

    
Return the data array reshaped into an image processing/visualization software friendly order.

(bands, rows, columns) -> (rows, columns, bands).

    
#### post_process

```python3
def post_process(
    self,
    in_range: Union[Sequence[Tuple[Union[float, int], Union[float, int]]], NoneType] = None,
    out_dtype: Union[str, numpy.number] = 'uint8',
    color_formula: Union[str, NoneType] = None,
    **kwargs: Any
) -> 'ImageData'
```

    
Post-process image data.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| in_range | tuple | input min/max bounds value to rescale from. | None |
| out_dtype | str | output datatype after rescaling. Defaults to `uint8`. | `uint8` |
| color_formula | str | rio-color formula (see: https://github.com/mapbox/rio-color). | None |
| kwargs | optional | keyword arguments to forward to `rio_tiler.utils.linear_rescale`. | None |

**Returns:**

| Type | Description |
|---|---|
| ImageData | new ImageData object with the updated data. |

    
#### render

```python3
def render(
    self,
    add_mask: bool = True,
    img_format: str = 'PNG',
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType] = None,
    **kwargs
) -> bytes
```

    
Render data to image blob.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| add_mask | bool | add mask to output image. Defaults to True. | True |
| img_format | str | output image format. Defaults to PNG. | PNG |
| colormap | dict or sequence | RGBA Color Table dictionary or sequence. | None |
| kwargs | optional | keyword arguments to forward to `rio_tiler.utils.render`. | None |

**Returns:**

| Type | Description |
|---|---|
| bytes | image. |

### Info

```python3
class Info(
    __pydantic_self__,
    **data: Any
)
```

#### Ancestors (in MRO)

* rio_tiler.models.SpatialInfo
* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

    
Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

    
Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

    

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    update: 'DictStrAny' = None,
    deep: bool = False
) -> 'Model'
```

    
Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

    
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

    
Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### NodataTypes

```python3
class NodataTypes(
    /,
    *args,
    **kwargs
)
```

#### Ancestors (in MRO)

* builtins.str
* enum.Enum

#### Class variables

```python3
Alpha
```

```python3
Empty
```

```python3
Internal
```

```python3
Mask
```

```python3
Nodata
```

```python3
name
```

```python3
value
```

### RioTilerBaseModel

```python3
class RioTilerBaseModel(
    __pydantic_self__,
    **data: Any
)
```

#### Ancestors (in MRO)

* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.Bounds
* rio_tiler.models.BandStatistics

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

    
Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

    
Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

    

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    update: 'DictStrAny' = None,
    deep: bool = False
) -> 'Model'
```

    
Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

    
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

    
Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

### SpatialInfo

```python3
class SpatialInfo(
    __pydantic_self__,
    **data: Any
)
```

#### Ancestors (in MRO)

* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel
* pydantic.utils.Representation

#### Descendants

* rio_tiler.models.Info

#### Class variables

```python3
Config
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: Union[ForwardRef('SetStr'), NoneType] = None,
    **values: Any
) -> 'Model'
```

    
Creates a new model setting __dict__ and __fields_set__ from trusted or pre-validated data.

Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

    
#### from_orm

```python3
def from_orm(
    obj: Any
) -> 'Model'
```

    

    
#### parse_file

```python3
def parse_file(
    path: Union[str, pathlib.Path],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: Any
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: Union[str, bytes],
    *,
    content_type: 'unicode' = None,
    encoding: 'unicode' = 'utf8',
    proto: pydantic.parse.Protocol = None,
    allow_pickle: bool = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}'
) -> 'DictStrAny'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: bool = True,
    ref_template: 'unicode' = '#/definitions/{model}',
    **dumps_kwargs: Any
) -> 'unicode'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: Any
) -> None
```

    
Try to update ForwardRefs on fields based on this Model, globalns and localns.

    
#### validate

```python3
def validate(
    value: Any
) -> 'Model'
```

    

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    update: 'DictStrAny' = None,
    deep: bool = False
) -> 'Model'
```

    
Duplicate a model, optionally choose which fields to include, exclude and change.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | fields to include in new model | None |
| exclude | None | fields to exclude from new model, as with values this takes precedence over include | None |
| update | None | values to change/add in the new model. Note: the data is not validated before creating
the new model: you should trust this data | None |
| deep | None | set to `True` to make a deep copy of the model | None |

**Returns:**

| Type | Description |
|---|---|
| None | new model instance |

    
#### dict

```python3
def dict(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False
) -> 'DictStrAny'
```

    
Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

    
#### json

```python3
def json(
    self,
    *,
    include: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    exclude: Union[ForwardRef('AbstractSetIntStr'), ForwardRef('MappingIntStrAny')] = None,
    by_alias: bool = False,
    skip_defaults: bool = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    encoder: Union[Callable[[Any], Any], NoneType] = None,
    models_as_dict: bool = True,
    **dumps_kwargs: Any
) -> 'unicode'
```

    
Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

`encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.