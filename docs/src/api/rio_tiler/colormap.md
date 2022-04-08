# Module rio_tiler.colormap

rio-tiler colormap functions and classes.

None

## Variables

```python3
DEFAULT_CMAPS_FILES
```

```python3
EMPTY_COLORMAP
```

```python3
USER_CMAPS_DIR
```

```python3
cmap
```

## Functions

    
### apply_cmap

```python3
def apply_cmap(
    data: numpy.ndarray,
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Apply colormap on data.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | 1D image array to translate to RGB. | None |
| colormap | dict or sequence | GDAL RGBA Color Table dictionary or sequence (for intervals). | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Mask (numpy.ndarray) values. |

**Raises:**

| Type | Description |
|---|---|
| InvalidFormat | If data is not a 1 band dataset (1, col, row). |

    
### apply_discrete_cmap

```python3
def apply_discrete_cmap(
    data: numpy.ndarray,
    colormap: Dict[int, Tuple[int, int, int, int]]
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Apply discrete colormap.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | 1D image array to translate to RGB. | None |
| color_map | dict | Discrete ColorMap dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Alpha band (numpy.ndarray). |

    
### apply_intervals_cmap

```python3
def apply_intervals_cmap(
    data: numpy.ndarray,
    colormap: Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Apply intervals colormap.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | 1D image array to translate to RGB. | None |
| color_map | Sequence | Sequence of intervals and color in form of [([min, max], [r, g, b, a]), ...]. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Alpha band (numpy.ndarray). |

    
### make_lut

```python3
def make_lut(
    colormap: Dict[int, Tuple[int, int, int, int]]
) -> numpy.ndarray
```

    
Create a lookup table numpy.ndarray from a GDAL RGBA Color Table dictionary.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| colormap | dict | GDAL RGBA Color Table dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy.ndarray | colormap lookup table. |

    
### parse_color

```python3
def parse_color(
    rgba: Union[Sequence[int], str]
) -> Tuple[int, int, int, int]
```

    
Parse RGB/RGBA color and return valid rio-tiler compatible RGBA colormap entry.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| rgba | str or list of int | HEX encoded or list RGB or RGBA colors. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | RGBA values. |

## Classes

### ColorMaps

```python3
class ColorMaps(
    data: Dict[str, Union[str, Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]] = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| data | dict | colormaps. Defaults to `rio_tiler.colormap.DEFAULTS_CMAPS`. | `rio_tiler.colormap.DEFAULTS_CMAPS` |

#### Methods

    
#### get

```python3
def get(
    self,
    name: str
) -> Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]
```

    
Fetch a colormap.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| name | str | colormap name.
Returns | None |
| dict | None | colormap dictionary. | None |

    
#### list

```python3
def list(
    self
) -> List[str]
```

    
List registered Colormaps.

Returns
    list: list of colormap names.

    
#### register

```python3
def register(
    self,
    custom_cmap: Dict[str, Union[str, Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]]]],
    overwrite: bool = False
) -> 'ColorMaps'
```

    
Register a custom colormap.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| custom_cmap | dict | custom colormap(s) to register. | None |
| overwrite | bool | Overwrite existing colormap with same key. Defaults to False. | False |