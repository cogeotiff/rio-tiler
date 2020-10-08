# Module rio_tiler.io.base

rio_tiler.io.base: ABC class for rio-tiler readers.

None

## Classes

### BaseReader

```python3
class BaseReader(
    
)
```

#### Descendants

* rio_tiler.io.base.MultiBaseReader
* rio_tiler.io.base.MultiBandReader
* rio_tiler.io.cogeo.COGReader

#### Instance variables

```python3
center
```

Dataset center + minzoom.

```python3
spatial_info
```

Return Dataset's spatial info.

#### Methods

    
#### info

```python3
def info(
    self
) -> Dict
```

    
Return Dataset's info.

    
#### metadata

```python3
def metadata(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    **kwargs: Any
) -> Dict
```

    
Return Dataset's statistics and info.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Part of a Dataset.

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    **kwargs: Any
) -> List
```

    
Read a value from a Dataset.

    
#### preview

```python3
def preview(
    self,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Return a preview of a Dataset.

    
#### stats

```python3
def stats(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    **kwargs: Any
) -> Dict
```

    
Return Dataset's statistics.

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Map tile from the Dataset.

### MultiBandReader

```python3
class MultiBandReader(
    reader: Type[rio_tiler.io.base.BaseReader],
    reader_options: Dict = NOTHING
)
```

#### Ancestors (in MRO)

* rio_tiler.io.base.BaseReader

#### Instance variables

```python3
center
```

Dataset center + minzoom.

```python3
spatial_info
```

Return Dataset's spatial info.

#### Methods

    
#### info

```python3
def info(
    self,
    bands: Union[Sequence[str], str] = None,
    *args,
    **kwargs: Any
) -> Dict
```

    
Return metadata from multiple bands

    
#### metadata

```python3
def metadata(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    bands: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict
```

    
Return metadata from multiple bands

    
#### parse_expression

```python3
def parse_expression(
    self,
    expression: str
) -> Tuple
```

    
Parse rio-tiler band math expression.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    band_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read part of multiple bands.

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    band_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> List
```

    
Read a pixel values from multiple bands,

    
#### preview

```python3
def preview(
    self,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    band_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Return a preview from multiple bands.

    
#### stats

```python3
def stats(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    bands: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict
```

    
Return array statistics from multiple bands

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    band_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Mercator Map tile multiple bands.

### MultiBaseReader

```python3
class MultiBaseReader(
    reader: Type[rio_tiler.io.base.BaseReader],
    reader_options: Dict = NOTHING
)
```

#### Ancestors (in MRO)

* rio_tiler.io.base.BaseReader

#### Descendants

* rio_tiler.io.stac.STACReader

#### Instance variables

```python3
center
```

Dataset center + minzoom.

```python3
spatial_info
```

Return Dataset's spatial info.

#### Methods

    
#### info

```python3
def info(
    self,
    assets: Union[Sequence[str], str] = None,
    *args,
    **kwargs: Any
) -> Dict
```

    
Return metadata from multiple assets

    
#### metadata

```python3
def metadata(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    assets: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict
```

    
Return metadata from multiple assets

    
#### parse_expression

```python3
def parse_expression(
    self,
    expression: str
) -> Tuple
```

    
Parse rio-tiler band math expression.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    asset_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read part of multiple assets.

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    asset_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> List
```

    
Read a value from COGs.

    
#### preview

```python3
def preview(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    asset_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Return a preview from multiple assets.

    
#### stats

```python3
def stats(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    assets: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict
```

    
Return array statistics from multiple assets

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = '',
    asset_expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Mercator Map tile multiple assets.