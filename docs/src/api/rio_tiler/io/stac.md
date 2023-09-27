# Module rio_tiler.io.stac

rio_tiler.io.stac: STAC reader.

None

## Variables

```python3
DEFAULT_VALID_TYPE
```

```python3
WGS84_CRS
```

## Functions

    
### aws_get_object

```python3
def aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = False,
    client: 'boto3_session.client' = None
) -> bytes
```

    
AWS s3 get object content.

    
### fetch

```python3
def fetch(
    filepath: str,
    **kwargs: Any
) -> Dict
```

    
Fetch STAC items.

A LRU cache is set on top of this function.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| filepath | str | STAC item URL. | None |
| kwargs | any | additional options to pass to client. | None |

**Returns:**

| Type | Description |
|---|---|
| dict | STAC Item content. |

## Classes

### STACReader

```python3
class STACReader(
    input: str,
    item: Union[NoneType, Dict, pystac.item.Item] = None,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>,
    minzoom: int = NOTHING,
    maxzoom: int = NOTHING,
    geographic_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    include_assets: Optional[Set[str]] = None,
    exclude_assets: Optional[Set[str]] = None,
    include_asset_types: Set[str] = {'image/tiff; profile=cloud-optimized; application=geotiff', 'image/tiff; application=geotiff', 'image/x.geotiff', 'image/tiff; application=geotiff; profile=cloud-optimized', 'image/vnd.stac.geotiff; cloud-optimized=true', 'application/x-hdf', 'image/jp2', 'application/x-hdf5', 'image/tiff'},
    exclude_asset_types: Optional[Set[str]] = None,
    reader: Type[rio_tiler.io.base.BaseReader] = <class 'rio_tiler.io.rasterio.Reader'>,
    reader_options: Dict = NOTHING,
    fetch_options: Dict = NOTHING,
    ctx: Any = <class 'rasterio.env.Env'>
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| input | str | STAC Item path, URL or S3 URL. | None |
| item | dict or pystac.Item, STAC | Stac Item. | None |
| tms | morecantile.TileMatrixSet | TileMatrixSet grid definition. Defaults to `WebMercatorQuad`. | `WebMercatorQuad` |
| minzoom | int | Set minzoom for the tiles. | None |
| maxzoom | int | Set maxzoom for the tiles. | None |
| geographic_crs | rasterio.crs.CRS | CRS to use as geographic coordinate system. Defaults to WGS84. | WGS84 |
| include_assets | set of string | Only Include specific assets. | None |
| exclude_assets | set of string | Exclude specific assets. | None |
| include_asset_types | set of string | Only include some assets base on their type. | None |
| exclude_asset_types | set of string | Exclude some assets base on their type. | None |
| reader | rio_tiler.io.BaseReader | rio-tiler Reader. Defaults to `rio_tiler.io.Reader`. | `rio_tiler.io.Reader` |
| reader_options | dict | Additional option to forward to the Reader. Defaults to `{}`. | `{}` |
| fetch_options | dict | Options to pass to `rio_tiler.io.stac.fetch` function fetching the STAC Items. Defaults to `{}`. | `{}` |

#### Ancestors (in MRO)

* rio_tiler.io.base.MultiBaseReader
* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
geographic_bounds
```

Return dataset bounds in geographic_crs.

#### Methods

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    assets: Union[Sequence[str], str] = None,
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_as_band: bool = False,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    categorical: bool = False,
    categories: Optional[List[float]] = None,
    percentiles: Optional[List[int]] = None,
    hist_options: Optional[Dict] = None,
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
    expression: str,
    asset_as_band: bool = False
) -> Tuple
```

    
Parse rio-tiler band math expression.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    assets: Union[Sequence[str], str] = None,
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_as_band: bool = False,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_as_band: bool = False,
    **kwargs: Any
) -> rio_tiler.models.PointData
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
| kwargs | optional | Options to forward to the `self.reader.point` method. | None |

**Returns:**

| Type | Description |
|---|---|
| None | PointData |

    
#### preview

```python3
def preview(
    self,
    assets: Union[Sequence[str], str] = None,
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_as_band: bool = False,
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
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_expression: Optional[Dict[str, str]] = None,
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
    expression: Optional[str] = None,
    asset_indexes: Optional[Dict[str, Union[Sequence[int], int]]] = None,
    asset_as_band: bool = False,
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