# Module rio_tiler.io.stac

rio_tiler.io.stac: STAC reader.

None

## Variables

```python3
DEFAULT_VALID_TYPE
```

## Functions

    
### fetch

```python3
def fetch(
    filepath: str
) -> Dict
```

    
Fetch items.

## Classes

### STACReader

```python3
class STACReader(
    filepath: str,
    item: Dict = None,
    minzoom: int = 0,
    maxzoom: int = 30,
    include_assets: Union[Set[str], NoneType] = None,
    exclude_assets: Union[Set[str], NoneType] = None,
    include_asset_types: Set[str] = {'image/tiff; application=geotiff', 'image/jp2', 'application/x-hdf5', 'application/x-hdf', 'image/x.geotiff', 'image/tiff', 'image/tiff; application=geotiff; profile=cloud-optimized', 'image/vnd.stac.geotiff; cloud-optimized=true'},
    exclude_asset_types: Union[Set[str], NoneType] = None,
    reader: Type[rio_tiler.io.base.BaseReader] = <class 'rio_tiler.io.cogeo.COGReader'>,
    reader_options: Dict = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| filepath | str | STAC Item path, URL or S3 URL. | None |
| item | Dict | STAC Item dict. | None |
| minzoom | int | Set minzoom for the tiles. | None |
| minzoom | int | Set maxzoom for the tiles. | None |
| include_assets | Set | Only accept some assets. | None |
| exclude_assets | Set | Exclude some assets. | None |
| include_asset_types | Set | Only include some assets base on their type | None |
| include_asset_types | Set | Exclude some assets base on their type | None |
| reader | BaseReader | rio-tiler Reader (default is set to rio_tiler.io.COGReader) | set |
| reader_options | dict | additional option to forward to the Reader (default is {}). | is |
| Properties | None | None | None |
| ---------- | None | None | None |
| bounds | tuple[float] | STAC bounds in WGS84 crs. | None |
| center | tuple[float, float, int] | STAC item center + minzoom | None |
| spatial_info | dict | STAC spatial info (zoom, bounds and center) | None |
| Methods | None | None | None |
| ------- | None | None | None |
| tile(0, 0, 0, assets="B01", expression="B01/B02") | None | Read a map tile from the COG. | None |
| part((0,10,0,10), assets="B01", expression="B1/B20", max_size=1024) | None | Read part of the COG. | None |
| preview(assets="B01", max_size=1024) | None | Read preview of the COG. | None |
| point((10, 10), assets="B01") | None | Read a point value from the COG. | None |
| stats(assets="B01", pmin=5, pmax=95) | None | Get Raster statistics. | None |
| info(assets="B01") | None | Get Assets raster info. | None |
| metadata(assets="B01", pmin=5, pmax=95) | None | info + stats | None |

#### Ancestors (in MRO)

* rio_tiler.io.base.MultiBaseReader
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