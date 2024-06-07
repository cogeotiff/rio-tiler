# Module rio_tiler.io.rasterio

rio_tiler.io.rasterio: rio-tiler reader built on top Rasterio

## Variables

```python3
WGS84_CRS
```

## Classes

### ImageReader

```python3
class ImageReader(
    input: str,
    dataset: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.io.MemoryFile, rasterio.vrt.WarpedVRT] = None,
    colormap: Dict = None,
    options: rio_tiler.reader.Options = NOTHING
)
```

Non Geo Image Reader

#### Ancestors (in MRO)

* rio_tiler.io.rasterio.Reader
* rio_tiler.io.base.BaseReader
* rio_tiler.io.base.SpatialMixin

#### Instance variables

```python3
maxzoom
```

Return dataset maxzoom.

```python3
minzoom
```

Return dataset minzoom.

#### Methods

    
#### close

```python3
def close(
    self
)
```

Close rasterio dataset.

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: Union[int, NoneType] = None,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    force_binary_mask: bool = True,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Union[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray], NoneType] = None
) -> rio_tiler.models.ImageData
```

Read part of an Image defined by a geojson feature.

    
#### geographic_bounds

```python3
def geographic_bounds(
    ...
)
```

Return dataset bounds in geographic_crs.

    
#### get_maxzoom

```python3
def get_maxzoom(
    self
) -> int
```

Define dataset maximum zoom level.

    
#### get_minzoom

```python3
def get_minzoom(
    self
) -> int
```

Define dataset minimum zoom level.

    
#### info

```python3
def info(
    self
) -> rio_tiler.models.Info
```

Return Dataset info.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: Union[int, NoneType] = None,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    force_binary_mask: bool = True,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Union[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray], NoneType] = None
) -> rio_tiler.models.ImageData
```

Read part of an Image.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top). | None |
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| force_binary_mask | bool | Cast returned mask to binary values (0 or 255). Defaults to `True`. | `True` |
| resampling_method | RIOResampling | RasterIO resampling algorithm. Defaults to `nearest`. | `nearest` |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### point

```python3
def point(
    self,
    x: float,
    y: float,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    unscale: bool = False,
    post_process: Union[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray], NoneType] = None
) -> rio_tiler.models.PointData
```

Read a pixel value from an Image.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | X coordinate. | None |
| lat | float | Y coordinate. | None |
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| None | PointData |

    
#### preview

```python3
def preview(
    self,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: int = 1024,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Return a preview of a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| kwargs | optional | Options to forward to the `self.read` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### read

```python3
def read(
    self,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read the Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `rio_tiler.reader.read` function. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: Union[List[int], NoneType] = None,
    hist_options: Union[Dict, NoneType] = None,
    max_size: int = 1024,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

Return bands statistics from a dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| kwargs | optional | Options to forward to `self.read`. | None |

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
    tilesize: int = 256,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    force_binary_mask: bool = True,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Union[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray], NoneType] = None
) -> rio_tiler.models.ImageData
```

Read a Web Map tile from an Image.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |
| tilesize | int | Output image size. Defaults to `256`. | `256` |
| indexes | int or sequence of int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| force_binary_mask | bool | Cast returned mask to binary values (0 or 255). Defaults to `True`. | `True` |
| resampling_method | RIOResampling | RasterIO resampling algorithm. Defaults to `nearest`. | `nearest` |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

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

### LocalTileMatrixSet

```python3
class LocalTileMatrixSet(
    width: int,
    height: int,
    tile_size: int = 256
)
```

Fake TMS for non-geo image.

#### Methods

    
#### xy_bounds

```python3
def xy_bounds(
    self,
    *tile: morecantile.commons.Tile
) -> morecantile.commons.BoundingBox
```

Return the bounding box of the (x, y, z) tile

### Reader

```python3
class Reader(
    input: str,
    dataset: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.io.MemoryFile, rasterio.vrt.WarpedVRT] = None,
    tms: morecantile.models.TileMatrixSet = <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>,
    geographic_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    colormap: Dict = None,
    options: rio_tiler.reader.Options = NOTHING
)
```

Rasterio Reader.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| input | str | dataset path. | None |
| dataset | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| tms | morecantile.TileMatrixSet | TileMatrixSet grid definition. Defaults to `WebMercatorQuad`. | `WebMercatorQuad` |
| geographic_crs | rasterio.crs.CRS | CRS to use as geographic coordinate system. Defaults to WGS84. | WGS84 |
| colormap | dict | Overwrite internal colormap. | None |
| options | dict | Options to forward to low-level reader methods. | None |

#### Ancestors (in MRO)

* rio_tiler.io.base.BaseReader
* rio_tiler.io.base.SpatialMixin

#### Descendants

* rio_tiler.io.rasterio.ImageReader

#### Instance variables

```python3
maxzoom
```

Return dataset maxzoom.

```python3
minzoom
```

Return dataset minzoom.

#### Methods

    
#### close

```python3
def close(
    self
)
```

Close rasterio dataset.

    
#### feature

```python3
def feature(
    self,
    shape: Dict,
    dst_crs: Union[rasterio.crs.CRS, NoneType] = None,
    shape_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: Union[int, NoneType] = None,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    buffer: Union[float, int, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read part of a Dataset defined by a geojson feature.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| shape | dict | Valid GeoJSON feature. | None |
| dst_crs | rasterio.crs.CRS | Overwrite target coordinate reference system. | None |
| shape_crs | rasterio.crs.CRS | Input geojson coordinate reference system. Defaults to `epsg:4326`. | `epsg:4326` |
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| buffer | int or float | Buffer on each side of the given aoi. It must be a multiple of `0.5`. Output **image size** will be expanded to `output imagesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258). | None |
| kwargs | optional | Options to forward to the `Reader.part` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### geographic_bounds

```python3
def geographic_bounds(
    ...
)
```

Return dataset bounds in geographic_crs.

    
#### get_maxzoom

```python3
def get_maxzoom(
    self
) -> int
```

Define dataset maximum zoom level.

    
#### get_minzoom

```python3
def get_minzoom(
    self
) -> int
```

Define dataset minimum zoom level.

    
#### info

```python3
def info(
    self
) -> rio_tiler.models.Info
```

Return Dataset info.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    dst_crs: Union[rasterio.crs.CRS, NoneType] = None,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: Union[int, NoneType] = None,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    buffer: Union[float, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read part of a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | Output bounds (left, bottom, right, top) in target crs ("dst_crs"). | None |
| dst_crs | rasterio.crs.CRS | Overwrite target coordinate reference system. | None |
| bounds_crs | rasterio.crs.CRS | Bounds Coordinate Reference System. Defaults to `epsg:4326`. | `epsg:4326` |
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| buffer | float | Buffer on each side of the given aoi. It must be a multiple of `0.5`. Output **image size** will be expanded to `output imagesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258). | None |
| kwargs | optional | Options to forward to the `rio_tiler.reader.part` function. | None |

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
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.PointData
```

Read a pixel value from a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| lon | float | Longitude. | None |
| lat | float | Latitude. | None |
| coord_crs | rasterio.crs.CRS | Coordinate Reference System of the input coords. Defaults to `epsg:4326`. | `epsg:4326` |
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `rio_tiler.reader.point` function. | None |

**Returns:**

| Type | Description |
|---|---|
| None | PointData |

    
#### preview

```python3
def preview(
    self,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    max_size: int = 1024,
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Return a preview of a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| kwargs | optional | Options to forward to the `self.read` method. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### read

```python3
def read(
    self,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read the Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | sequence of int or int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| kwargs | optional | Options to forward to the `rio_tiler.reader.read` function. | None |

**Returns:**

| Type | Description |
|---|---|
| rio_tiler.models.ImageData | ImageData instance with data, mask and input spatial info. |

    
#### statistics

```python3
def statistics(
    self,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: Union[List[int], NoneType] = None,
    hist_options: Union[Dict, NoneType] = None,
    max_size: int = 1024,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    **kwargs: Any
) -> Dict[str, rio_tiler.models.BandStatistics]
```

Return bands statistics from a dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| max_size | int | Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024. | 1024 |
| kwargs | optional | Options to forward to `self.read`. | None |

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
    tilesize: int = 256,
    indexes: Union[Sequence[int], int, NoneType] = None,
    expression: Union[str, NoneType] = None,
    buffer: Union[float, NoneType] = None,
    **kwargs: Any
) -> rio_tiler.models.ImageData
```

Read a Web Map tile from a Dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Tile's horizontal index. | None |
| tile_y | int | Tile's vertical index. | None |
| tile_z | int | Tile's zoom level index. | None |
| tilesize | int | Output image size. Defaults to `256`. | `256` |
| indexes | int or sequence of int | Band indexes. | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3). | None |
| buffer | float | Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258). | None |
| kwargs | optional | Options to forward to the `Reader.part` method. | None |

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