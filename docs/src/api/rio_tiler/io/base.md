# Module rio_tiler.io.base

rio_tiler.io.base: ABC class for rio-tiler readers.

None

## Classes

### AsyncBaseReader

```python3
class AsyncBaseReader(
    input: Any,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' identifier='WebMercatorQuad'>
)
```

#### Ancestors (in MRO)

* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
geographic_bounds
```

return bounds in WGS84.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    **kwargs: Any
) -> Coroutine[Any, Any, rio_tiler.models.ImageData]
```

    
Read a Dataset for a GeoJSON feature.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### info

```python3
def info(
    self
) -> Coroutine[Any, Any, rio_tiler.models.Info]
```

    
Return Dataset's info.

**Returns:**

| Type | Description |
|---|---|
| rio_tile.models.Info | Dataset info. |

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    **kwargs: Any
) -> Coroutine[Any, Any, rio_tiler.models.ImageData]
```

    
Read a Part of a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    **kwargs: Any
) -> Coroutine[Any, Any, List]
```

    
Read a value from a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |

**Returns:**

| Type | Description |
|---|---|
| list | Pixel value per bands/assets. |

    
#### preview

```python3
def preview(
    self,
    **kwargs: Any
) -> Coroutine[Any, Any, rio_tiler.models.ImageData]
```

    
Read a preview of a Dataset.

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    **kwargs: Any
) -> Coroutine[Any, Any, Dict[str, rio_tiler.models.BandStatistics]]
```

    
Return bands statistics from a dataset.

**Returns:**

| Type | Description |
|---|---|
| Dict[str, rio_tiler.models.BandStatistics] | bands statistics. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    **kwargs: Any
) -> Coroutine[Any, Any, rio_tiler.models.ImageData]
```

    
Read a Map tile from the Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

    
Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |

### BaseReader

```python3
class BaseReader(
    input: Any,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' identifier='WebMercatorQuad'>
)
```

#### Ancestors (in MRO)

* rio_tiler.io.base.SpatialMixin

#### Descendants

* rio_tiler.io.cogeo.COGReader

#### Instance variables

```python3
geographic_bounds
```

return bounds in WGS84.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read a Dataset for a GeoJSON feature.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### info

```python3
def info(
    self
) -> rio_tiler.models.Info
```

    
Return Dataset's info.

**Returns:**

| Type | Description |
|---|---|
| rio_tile.models.Info | Dataset info. |

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read a Part of a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
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

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |

**Returns:**

| Type | Description |
|---|---|
| list | Pixel value per bands/assets. |

    
#### preview

```python3
def preview(
    self,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read a preview of a Dataset.

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

    
Return bands statistics from a dataset.

**Returns:**

| Type | Description |
|---|---|
| Dict[str, rio_tiler.models.BandStatistics] | bands statistics. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read a Map tile from the Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

    
Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |

### MultiBandReader

```python3
class MultiBandReader(
    input: Any,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' identifier='WebMercatorQuad'>,
    reader_options: Dict = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| input | any | input data. | None |
| tms | morecantile.TileMatrixSet | TileMatrixSet grid definition. Defaults to `WebMercatorQuad`. | `WebMercatorQuad` |
| reader_options | dict, option | options to forward to the reader. Defaults to `{}`. | `{}` |
| reader | rio_tiler.io.BaseReader | reader. **Not in __init__**. | None |
| bands | sequence | Band list. **Not in __init__**. | None |

#### Ancestors (in MRO)

* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
geographic_bounds
```

return bounds in WGS84.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge parts defined by geojson feature from multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |
| bands | sequence of str or str | bands to fetch info from. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `self.reader.feature` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### info

```python3
def info(
    self,
    bands: Union[Sequence[str], str] = None,
    *args,
    **kwargs: Any
) -> rio_tiler.models.Info
```

    
Return metadata from multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bands | sequence of str or str | band names to fetch info from. Required keyword argument. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple bands info in form of {"band1": rio_tile.models.Info}. |

    
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
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge parts from multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs. | None |
| bands | sequence of str or str | bands to fetch info from. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the 'self.reader.part' method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> List
```

    
Read a pixel values from multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |
| bands | sequence of str or str | bands to fetch info from. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `self.reader.point` method. | None |

**Returns:**

| Type | Description |
|---|---|
| list | Pixel value per bands. |

    
#### preview

```python3
def preview(
    self,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge previews from multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bands | sequence of str or str | bands to fetch info from. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `self.reader.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: List[int] = [2, 98],
    hist_options: Union[Dict, NoneType] = None,
    max_size: int = 1024,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

    
Return array statistics for multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bands | sequence of str or str | bands to fetch info from. Required keyword argument. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| kwargs | optional | Options to forward to the `self.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple assets statistics in form of {"{band}/{expression}": rio_tiler.models.BandStatistics, ...}. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge Web Map tiles multiple bands.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |
| bands | sequence of str or str | bands to fetch info from. | None |
| expression | str | rio-tiler expression for the band list (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `self.reader.tile` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

    
Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |

### MultiBaseReader

```python3
class MultiBaseReader(
    input: Any,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' identifier='WebMercatorQuad'>,
    reader_options: Dict = NOTHING
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| input | any | input data. | None |
| tms | morecantile.TileMatrixSet | TileMatrixSet grid definition. Defaults to `WebMercatorQuad`. | `WebMercatorQuad` |
| reader_options | dict, option | options to forward to the reader. Defaults to `{}`. | `{}` |
| reader | rio_tiler.io.BaseReader | reader. **Not in __init__**. | None |
| assets | sequence | Asset list. **Not in __init__**. | None |

#### Ancestors (in MRO)

* rio_tiler.io.base.SpatialMixin

#### Descendants

* rio_tiler.io.stac.STACReader

#### Instance variables

```python3
geographic_bounds
```

return bounds in WGS84.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge parts defined by geojson feature from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.feature` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### info

```python3
def info(
    self,
    assets: Union[Sequence[str], str] = None,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.Info]
```

    
Return metadata from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. Required keyword argument. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple assets info in form of {"asset1": rio_tile.models.Info}. |

    
#### merged_statistics

```python3
def merged_statistics(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: List[int] = [2, 98],
    hist_options: Union[Dict, NoneType] = None,
    max_size: int = 1024,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

    
Return array statistics for multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| kwargs | optional | Options to forward to the `self.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| Dict[str, rio_tiler.models.BandStatistics] | bands statistics. |

    
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
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge parts from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.part` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> List
```

    
Read pixel value from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.point` method. | None |

**Returns:**

| Type | Description |
|---|---|
| list | Pixel values per assets. |

    
#### preview

```python3
def preview(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge previews from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.preview` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    assets: Union[Sequence[str], str] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> Dict[str, Dict[str, rio_tiler.models.BandStatistics]]
```

    
Return array statistics for multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | sequence of str or str | assets to fetch info from. | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.statistics` method. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Multiple assets statistics in form of {"asset1": {"1": rio_tiler.models.BandStatistics, ...}}. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    assets: Union[Sequence[str], str] = None,
    expression: Union[str, NoneType] = None,
    asset_indexes: Union[Dict[str, Union[Sequence[int], int]], NoneType] = None,
    asset_expression: Union[Dict[str, str], NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

    
Read and merge Wep Map tiles from multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |
| assets | sequence of str or str | assets to fetch info from. | None |
| expression | str | rio-tiler expression for the asset list (e.g. asset1/asset2+asset3). | None |
| asset_indexes | dict | Band indexes for each asset (e.g {"asset1": 1, "asset2": (1, 2,)}). | None |
| asset_expression | dict | rio-tiler expression for each asset (e.g. {"asset1": "b1/b2+b3", "asset2": ...}). | None |
| kwargs | optional | Options to forward to the `self.reader.tile` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and tile spatial info. |

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

    
Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |

### SpatialMixin

```python3
class SpatialMixin(
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' identifier='WebMercatorQuad'>
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| tms | morecantile.TileMatrixSet | TileMatrixSet grid definition. Defaults to `WebMercatorQuad`. | `WebMercatorQuad` |
| minzoom | int | Dataset Min Zoom level. **Not in __init__**. | None |
| maxzoom | int | Dataset Max Zoom level. **Not in __init__**. | None |
| bounds | tuple | Dataset bounds (left, bottom, right, top). **Not in __init__**. | None |
| crs | rasterio.crs.CRS | Dataset crs. **Not in __init__**. | None |
| geographic_crs | rasterio.crs.CRS | CRS to use as geographic coordinate system. Defaults to WGS84. **Not in __init__**. | WGS84. **Not in __init__** |

#### Descendants

* rio_tiler.io.base.BaseReader
* rio_tiler.io.base.AsyncBaseReader
* rio_tiler.io.base.MultiBaseReader
* rio_tiler.io.base.MultiBandReader

#### Instance variables

```python3
geographic_bounds
```

return bounds in WGS84.

#### Methods

    
#### tile_exists

```python3
def tile_exists(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int
) -> bool
```

    
Check if a tile intersects the dataset bounds.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |

**Returns:**

| Type | Description |
|---|---|
| bool | True if the tile intersects the dataset bounds. |