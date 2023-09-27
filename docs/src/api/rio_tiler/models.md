# Module rio_tiler.models

rio-tiler models.

None

## Variables

```python3
WGS84_CRS
```

```python3
dtype_ranges
```

## Functions

    
### masked_and_3d

```python3
def masked_and_3d(
    array: numpy.ndarray
) -> numpy.ma.core.MaskedArray
```

    
Makes sure we have a 3D array and mask

    
### rescale_image

```python3
def rescale_image(
    array: numpy.ma.core.MaskedArray,
    in_range: Sequence[Tuple[Union[float, int], Union[float, int]]],
    out_range: Sequence[Tuple[Union[float, int], Union[float, int]]] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = 'uint8'
) -> numpy.ma.core.MaskedArray
```

    
Rescale image data in-place.

    
### to_coordsbbox

```python3
def to_coordsbbox(
    bbox
) -> Optional[rasterio.coords.BoundingBox]
```

    
Convert bbox to CoordsBbox nameTuple.

    
### to_masked

```python3
def to_masked(
    array: numpy.ndarray
) -> numpy.ma.core.MaskedArray
```

    
Makes sure we have a MaskedArray.

## Classes

### BandStatistics

```python3
class BandStatistics(
    __pydantic_self__,
    **data: 'Any'
)
```

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

    
Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of
`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

    
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class
`Model` with 2 type variables and a concrete model `Model[str, int]`,
the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

    
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.
If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to raise an exception on invalid fields. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    

#### Instance variables

```python3
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping
specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping
specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values
in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.
If mode is 'json', the dictionary will only contain JSON serializable types.
If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that are unset or None from the output. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

    
Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### Bounds

```python3
class Bounds(
    __pydantic_self__,
    **data: 'Any'
)
```

#### Ancestors (in MRO)

* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel

#### Descendants

* rio_tiler.models.SpatialInfo

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

    
Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of
`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

    
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class
`Model` with 2 type variables and a concrete model `Model[str, int]`,
the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

    
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.
If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to raise an exception on invalid fields. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    

#### Instance variables

```python3
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping
specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping
specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values
in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.
If mode is 'json', the dictionary will only contain JSON serializable types.
If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that are unset or None from the output. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

    
Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### ImageData

```python3
class ImageData(
    array: numpy.ndarray,
    cutline_mask: Optional[numpy.ndarray] = None,
    *,
    assets: Optional[List] = None,
    bounds=None,
    crs: Optional[rasterio.crs.CRS] = None,
    metadata: Optional[Dict] = NOTHING,
    band_names: List[str] = NOTHING,
    dataset_statistics: Optional[Sequence[Tuple[float, float]]] = None
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| array | numpy.ma.MaskedArray | image values. | None |
| assets | list | list of assets used to construct the data values. | None |
| bounds | BoundingBox | bounding box of the data. | None |
| crs | rasterio.crs.CRS | Coordinates Reference System of the bounds. | None |
| metadata | dict | Additional metadata. Defaults to `{}`. | `{}` |
| band_names | list | name of each band. Defaults to `["1", "2", "3"]` for 3 bands image. | `["1", "2", "3"]` for 3 bands image |
| dataset_statistics | list | dataset statistics `[(min, max), (min, max)]`
Note: `mask` should be considered as `PER_BAND` so shape should be similar as the data | None |

#### Static methods

    
#### create_from_list

```python3
def create_from_list(
    data: Sequence[ForwardRef('ImageData')]
) -> 'ImageData'
```

    
Create ImageData from a sequence of ImageData objects.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | sequence | sequence of ImageData. | None |

    
#### from_array

```python3
def from_array(
    arr: numpy.ndarray
) -> 'ImageData'
```

    
Create ImageData from a numpy array.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| arr | numpy.ndarray | Numpy array or Numpy masked array. | None |

    
#### from_bytes

```python3
def from_bytes(
    data: bytes
) -> 'ImageData'
```

    
Create ImageData from bytes.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | bytes | raster dataset as bytes. | None |

#### Instance variables

```python3
count
```

Number of band.

```python3
data
```

Return data part of the masked array.

```python3
height
```

Height of the data array.

```python3
mask
```

Return Mask in form of rasterio dataset mask.

```python3
transform
```

Returns the affine transform.

```python3
width
```

Width of the data array.

#### Methods

    
#### apply_color_formula

```python3
def apply_color_formula(
    self,
    color_formula: Optional[str]
)
```

    
Apply color-operations formula in place.

    
#### apply_colormap

```python3
def apply_colormap(
    self,
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]
) -> 'ImageData'
```

    
Apply colormap to the image data.

    
#### apply_expression

```python3
def apply_expression(
    self,
    expression: str
) -> 'ImageData'
```

    
Apply expression to the image data.

    
#### as_masked

```python3
def as_masked(
    self
) -> numpy.ma.core.MaskedArray
```

    
return a numpy masked array.

    
#### clip

```python3
def clip(
    self,
    bbox: Tuple[float, float, float, float]
) -> 'ImageData'
```

    
Clip data and mask to a bbox.

    
#### data_as_image

```python3
def data_as_image(
    self
) -> numpy.ndarray
```

    
Return the data array reshaped into an image processing/visualization software friendly order.

(bands, rows, columns) -> (rows, columns, bands).

    
#### get_coverage_array

```python3
def get_coverage_array(
    self,
    shape: Dict,
    shape_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    cover_scale: int = 10
) -> numpy.ndarray[typing.Any, numpy.dtype[numpy.floating]]
```

    
cover_scale: int, optional

Scale used when generating coverage estimates of each
    raster cell by vector feature. Coverage is generated by
    rasterizing the feature at a finer resolution than the raster then using a summation to aggregate
    to the raster resolution and dividing by the square of cover_scale
    to get coverage value for each cell. Increasing cover_scale
    will increase the accuracy of coverage values; three orders
    magnitude finer resolution (cover_scale=1000) is usually enough to
    get coverage estimates with <1% error in individual edge cells coverage
    estimates, though much smaller values (e.g., cover_scale=10) are often
    sufficient (<10% error) and require less memory.

Note: code adapted from https://github.com/perrygeo/python-rasterstats/pull/136 by @sgoodm

    
#### post_process

```python3
def post_process(
    self,
    in_range: Optional[Sequence[Tuple[Union[float, int], Union[float, int]]]] = None,
    out_dtype: Union[str, numpy.number] = 'uint8',
    color_formula: Optional[str] = None,
    **kwargs: Any
) -> 'ImageData'
```

    
Post-process image data.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| in_range | tuple | input min/max bounds value to rescale from. | None |
| out_dtype | str | output datatype after rescaling. Defaults to `uint8`. | `uint8` |
| color_formula | str | color-ops formula (see: https://github.com/vincentsarago/color-ops). | None |
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
| add_mask | bool | add mask to output image. Defaults to `True`. | `True` |
| img_format | str | output image format. Defaults to `PNG`. | `PNG` |
| colormap | dict or sequence | RGBA Color Table dictionary or sequence. | None |
| kwargs | optional | keyword arguments to forward to `rio_tiler.utils.render`. | None |

**Returns:**

| Type | Description |
|---|---|
| bytes | image. |

    
#### rescale

```python3
def rescale(
    self,
    in_range: Sequence[Tuple[Union[float, int], Union[float, int]]],
    out_range: Sequence[Tuple[Union[float, int], Union[float, int]]] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = 'uint8'
)
```

    
Rescale data in place.

    
#### resize

```python3
def resize(
    self,
    height: int,
    width: int,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest'
) -> 'ImageData'
```

    
Resize data and mask.

    
#### statistics

```python3
def statistics(
    self,
    categorical: bool = False,
    categories: Optional[List[float]] = None,
    percentiles: Optional[List[int]] = None,
    hist_options: Optional[Dict] = None,
    coverage: Optional[numpy.ndarray] = None
) -> Dict[str, rio_tiler.models.BandStatistics]
```

    
Return statistics from ImageData.

### Info

```python3
class Info(
    __pydantic_self__,
    **data: 'Any'
)
```

#### Ancestors (in MRO)

* rio_tiler.models.SpatialInfo
* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

    
Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of
`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

    
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class
`Model` with 2 type variables and a concrete model `Model[str, int]`,
the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

    
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.
If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to raise an exception on invalid fields. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    

#### Instance variables

```python3
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping
specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping
specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values
in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.
If mode is 'json', the dictionary will only contain JSON serializable types.
If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that are unset or None from the output. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

    
Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### PointData

```python3
class PointData(
    array: numpy.ndarray,
    *,
    band_names: List[str] = NOTHING,
    coordinates: Optional[Tuple[float, float]] = None,
    crs: Optional[rasterio.crs.CRS] = None,
    assets: Optional[List] = None,
    metadata: Optional[Dict] = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| array | numpy.ma.MaskedArray | pixel values. | None |
| band_names | list | name of each band. Defaults to `["1", "2", "3"]` for 3 bands image. | `["1", "2", "3"]` for 3 bands image |
| coordinates | tuple | Point's coordinates. | None |
| crs | rasterio.crs.CRS | Coordinates Reference System of the bounds. | None |
| assets | list | list of assets used to construct the data values. | None |
| metadata | dict | Additional metadata. Defaults to `{}`. | `{}` |

#### Static methods

    
#### create_from_list

```python3
def create_from_list(
    data: Sequence[ForwardRef('PointData')]
)
```

    
Create PointData from a sequence of PointsData objects.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | sequence | sequence of PointData. | None |

#### Instance variables

```python3
count
```

Number of band.

```python3
data
```

Return data part of the masked array.

```python3
mask
```

Return Mask in form of rasterio dataset mask.

#### Methods

    
#### apply_expression

```python3
def apply_expression(
    self,
    expression: str
) -> 'PointData'
```

    
Apply expression to the image data.

    
#### as_masked

```python3
def as_masked(
    self
) -> numpy.ma.core.MaskedArray
```

    
return a numpy masked array.

### RioTilerBaseModel

```python3
class RioTilerBaseModel(
    __pydantic_self__,
    **data: 'Any'
)
```

#### Ancestors (in MRO)

* pydantic.main.BaseModel

#### Descendants

* rio_tiler.models.Bounds
* rio_tiler.models.BandStatistics

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

    
Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of
`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

    
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class
`Model` with 2 type variables and a concrete model `Model[str, int]`,
the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

    
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.
If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to raise an exception on invalid fields. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    

#### Instance variables

```python3
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping
specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping
specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values
in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.
If mode is 'json', the dictionary will only contain JSON serializable types.
If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that are unset or None from the output. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

    
Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.

### SpatialInfo

```python3
class SpatialInfo(
    __pydantic_self__,
    **data: 'Any'
)
```

#### Ancestors (in MRO)

* rio_tiler.models.Bounds
* rio_tiler.models.RioTilerBaseModel
* pydantic.main.BaseModel

#### Descendants

* rio_tiler.models.Info

#### Class variables

```python3
model_config
```

```python3
model_fields
```

#### Static methods

    
#### construct

```python3
def construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    

    
#### from_orm

```python3
def from_orm(
    obj: 'Any'
) -> 'Model'
```

    

    
#### model_construct

```python3
def model_construct(
    _fields_set: 'set[str] | None' = None,
    **values: 'Any'
) -> 'Model'
```

    
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.
Behaves as if `Config.extra = 'allow'` was set since it adds all passed values

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| _fields_set | None | The set of field names accepted for the Model instance. | None |
| values | None | Trusted or pre-validated data dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A new instance of the `Model` class with validated data. |

    
#### model_json_schema

```python3
def model_json_schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>,
    mode: 'JsonSchemaMode' = 'validation'
) -> 'dict[str, Any]'
```

    
Generates a JSON schema for a model class.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| by_alias | None | Whether to use attribute aliases or not. | None |
| ref_template | None | The reference template. | None |
| schema_generator | None | To override the logic used to generate the JSON schema, as a subclass of
`GenerateJsonSchema` with your desired modifications | None |
| mode | None | The mode in which to generate the schema. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The JSON schema for the given model class. |

    
#### model_parametrized_name

```python3
def model_parametrized_name(
    params: 'tuple[type[Any], ...]'
) -> 'str'
```

    
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| params | None | Tuple of types of the class. Given a generic class
`Model` with 2 type variables and a concrete model `Model[str, int]`,
the value `(str, int)` would be passed to `params`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | String representing the new class where `params` are passed to `cls` as type variables. |

**Raises:**

| Type | Description |
|---|---|
| TypeError | Raised when trying to generate concrete names for non-generic models. |

    
#### model_rebuild

```python3
def model_rebuild(
    *,
    force: 'bool' = False,
    raise_errors: 'bool' = True,
    _parent_namespace_depth: 'int' = 2,
    _types_namespace: 'dict[str, Any] | None' = None
) -> 'bool | None'
```

    
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| force | None | Whether to force the rebuilding of the model schema, defaults to `False`. | None |
| raise_errors | None | Whether to raise errors, defaults to `True`. | None |
| _parent_namespace_depth | None | The depth level of the parent namespace, defaults to 2. | None |
| _types_namespace | None | The types namespace, defaults to `None`. | None |

**Returns:**

| Type | Description |
|---|---|
| None | Returns `None` if the schema is already "complete" and rebuilding was not required.
If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`. |

    
#### model_validate

```python3
def model_validate(
    obj: 'Any',
    *,
    strict: 'bool | None' = None,
    from_attributes: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate a pydantic model instance.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| obj | None | The object to validate. | None |
| strict | None | Whether to raise an exception on invalid fields. | None |
| from_attributes | None | Whether to extract data from object attributes. | None |
| context | None | Additional context to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated model instance. |

**Raises:**

| Type | Description |
|---|---|
| ValidationError | If the object could not be validated. |

    
#### model_validate_json

```python3
def model_validate_json(
    json_data: 'str | bytes | bytearray',
    *,
    strict: 'bool | None' = None,
    context: 'dict[str, Any] | None' = None
) -> 'Model'
```

    
Validate the given JSON data against the Pydantic model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| json_data | None | The JSON data to validate. | None |
| strict | None | Whether to enforce types strictly. | None |
| context | None | Extra variables to pass to the validator. | None |

**Returns:**

| Type | Description |
|---|---|
| None | The validated Pydantic model. |

**Raises:**

| Type | Description |
|---|---|
| ValueError | If `json_data` is not a JSON string. |

    
#### parse_file

```python3
def parse_file(
    path: 'str | Path',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### parse_obj

```python3
def parse_obj(
    obj: 'Any'
) -> 'Model'
```

    

    
#### parse_raw

```python3
def parse_raw(
    b: 'str | bytes',
    *,
    content_type: 'str | None' = None,
    encoding: 'str' = 'utf8',
    proto: '_deprecated_parse.Protocol | None' = None,
    allow_pickle: 'bool' = False
) -> 'Model'
```

    

    
#### schema

```python3
def schema(
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}'
) -> 'typing.Dict[str, Any]'
```

    

    
#### schema_json

```python3
def schema_json(
    *,
    by_alias: 'bool' = True,
    ref_template: 'str' = '#/$defs/{model}',
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### update_forward_refs

```python3
def update_forward_refs(
    **localns: 'Any'
) -> 'None'
```

    

    
#### validate

```python3
def validate(
    value: 'Any'
) -> 'Model'
```

    

#### Instance variables

```python3
model_computed_fields
```

Get the computed fields of this model instance.

```python3
model_extra
```

Get extra fields set during validation.

```python3
model_fields_set
```

Returns the set of fields that have been set on this model instance.

#### Methods

    
#### copy

```python3
def copy(
    self: 'Model',
    *,
    include: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None,
    update: 'typing.Dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| include | None | Optional set or mapping
specifying which fields to include in the copied model. | None |
| exclude | None | Optional set or mapping
specifying which fields to exclude in the copied model. | None |
| update | None | Optional dictionary of field-value pairs to override field values
in the copied model. | None |
| deep | None | If True, the values of fields that are Pydantic models will be deep copied. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A copy of the model with included, excluded and updated fields as specified. |

    
#### dict

```python3
def dict(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False
) -> 'typing.Dict[str, Any]'
```

    

    
#### json

```python3
def json(
    self,
    *,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    encoder: 'typing.Callable[[Any], Any] | None' = PydanticUndefined,
    models_as_dict: 'bool' = PydanticUndefined,
    **dumps_kwargs: 'Any'
) -> 'str'
```

    

    
#### model_copy

```python3
def model_copy(
    self: 'Model',
    *,
    update: 'dict[str, Any] | None' = None,
    deep: 'bool' = False
) -> 'Model'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#model_copy

Returns a copy of the model.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| update | None | Values to change/add in the new model. Note: the data is not validated
before creating the new model. You should trust this data. | None |
| deep | None | Set to `True` to make a deep copy of the model. | None |

**Returns:**

| Type | Description |
|---|---|
| None | New model instance. |

    
#### model_dump

```python3
def model_dump(
    self,
    *,
    mode: "Literal['json', 'python'] | str" = 'python',
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'dict[str, Any]'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mode | None | The mode in which `to_python` should run.
If mode is 'json', the dictionary will only contain JSON serializable types.
If mode is 'python', the dictionary may contain any Python objects. | None |
| include | None | A list of fields to include in the output. | None |
| exclude | None | A list of fields to exclude from the output. | None |
| by_alias | None | Whether to use the field's alias in the dictionary key if defined. | None |
| exclude_unset | None | Whether to exclude fields that are unset or None from the output. | None |
| exclude_defaults | None | Whether to exclude fields that are set to their default value from the output. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None` from the output. | None |
| round_trip | None | Whether to enable serialization and deserialization round-trip support. | None |
| warnings | None | Whether to log warnings when invalid fields are encountered. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A dictionary representation of the model. |

    
#### model_dump_json

```python3
def model_dump_json(
    self,
    *,
    indent: 'int | None' = None,
    include: 'IncEx' = None,
    exclude: 'IncEx' = None,
    by_alias: 'bool' = False,
    exclude_unset: 'bool' = False,
    exclude_defaults: 'bool' = False,
    exclude_none: 'bool' = False,
    round_trip: 'bool' = False,
    warnings: 'bool' = True
) -> 'str'
```

    
Usage docs: https://docs.pydantic.dev/2.2/usage/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indent | None | Indentation to use in the JSON output. If None is passed, the output will be compact. | None |
| include | None | Field(s) to include in the JSON output. Can take either a string or set of strings. | None |
| exclude | None | Field(s) to exclude from the JSON output. Can take either a string or set of strings. | None |
| by_alias | None | Whether to serialize using field aliases. | None |
| exclude_unset | None | Whether to exclude fields that have not been explicitly set. | None |
| exclude_defaults | None | Whether to exclude fields that have the default value. | None |
| exclude_none | None | Whether to exclude fields that have a value of `None`. | None |
| round_trip | None | Whether to use serialization/deserialization between JSON and class instance. | None |
| warnings | None | Whether to show any warnings that occurred during serialization. | None |

**Returns:**

| Type | Description |
|---|---|
| None | A JSON string representation of the model. |

    
#### model_post_init

```python3
def model_post_init(
    self,
    _BaseModel__context: 'Any'
) -> 'None'
```

    
Override this method to perform additional initialization after `__init__` and `model_construct`.

This is useful if you want to do some validation that requires the entire model to be initialized.