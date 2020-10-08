# Module rio_tiler.colormap

rio-tiler colormap functions.

None

## Variables

```python3
EMPTY_COLORMAP
```

```python3
cmap
```

## Functions

    
### apply_cmap

```python3
def apply_cmap(
    data: numpy.ndarray,
    colormap: Dict
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Apply colormap on tile data.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy ndarray | 1D image array to translate to RGB. | None |
| colormap | dict | GDAL RGBA Color Table dictionary. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy.ndarray | RGB data. |

    
### apply_discrete_cmap

```python3
def apply_discrete_cmap(
    data: numpy.ndarray,
    colormap: Dict
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Apply discrete colormap.

Note: This method is not used by default and left
      to users to use within custom render methods.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy ndarray | 1D image array to translate to RGB. | None |
| color_map | dict | Discrete ColorMap dictionary
e.g:
{
    1: [255, 255, 255],
    2: [255, 0, 0]
} | None |

**Returns:**

| Type | Description |
|---|---|
| numpy.ndarray | None |

    
### make_lut

```python3
def make_lut(
    colormap: Dict
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
| numpy.ndarray | colormap lookup table |

## Classes

### ColorMaps

```python3
class ColorMaps(
    
)
```

#### Methods

    
#### get

```python3
def get(
    self,
    name: str
) -> Dict
```

    
Fetch a colormap.

    
#### list

```python3
def list(
    self
) -> List[str]
```

    
List registered Colormaps.

    
#### register

```python3
def register(
    self,
    name: str,
    custom_cmap: Union[Dict, str],
    force: bool = False
)
```

    
Register a custom colormap.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| name | str | Name of the colormap. | None |
| custom_cmap | dict or str | A dict or a path to a numpy file | None |
| force | bool | Overwrite existing colormap with same key (default: False) | False |