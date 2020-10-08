# Module rio_tiler.io.cogeo

rio_tiler.io.cogeo: raster processing.

None

## Functions

    
### multi_info

```python3
def multi_info(
    assets: Sequence[str]
) -> List
```

    
Assemble multiple COGReader.info.

    
### multi_metadata

```python3
def multi_metadata(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> List
```

    
Assemble multiple COGReader.metadata.

    
### multi_part

```python3
def multi_part(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Assemble multiple COGReader.part.

    
### multi_point

```python3
def multi_point(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> List
```

    
Assemble multiple COGReader.point.

    
### multi_preview

```python3
def multi_preview(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Assemble multiple COGReader.preview.

    
### multi_stats

```python3
def multi_stats(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> List
```

    
Assemble multiple COGReader.stats.

    
### multi_tile

```python3
def multi_tile(
    assets: Sequence[str],
    *args: Any,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Assemble multiple tiles.

## Classes

### COGReader

```python3
class COGReader(
    filepath: str,
    dataset: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.io.MemoryFile, rasterio.vrt.WarpedVRT] = None,
    minzoom: int = None,
    maxzoom: int = None,
    colormap: Dict = None,
    nodata: Union[float, int, str, NoneType] = None,
    unscale: Union[bool, NoneType] = None,
    resampling_method: Union[rasterio.enums.Resampling, NoneType] = None,
    vrt_options: Union[Dict, NoneType] = None,
    post_process: Union[Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]], NoneType] = None
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| filepath | str | Cloud Optimized GeoTIFF path. | None |
| dataset | rasterio.DatasetReader | Rasterio dataset. | None |
| Properties | None | None | None |
| ---------- | None | None | None |
| minzoom | int | COG minimum zoom level. | None |
| maxzoom | int | COG maximum zoom level. | None |
| bounds | tuple[float] | COG bounds in WGS84 crs. | None |
| center | tuple[float, float, int] | COG center + minzoom | None |
| colormap | dict | COG internal colormap. | None |
| info | dict | General information about the COG (datatype, indexes, ...) | None |
| Methods | None | None | None |
| ------- | None | None | None |
| tile(0, 0, 0, indexes=(1,2,3), expression="B1/B2", tilesize=512, resampling_methods="nearest") | None | Read a map tile from the COG. | None |
| part((0,10,0,10), indexes=(1,2,3,), expression="B1/B20", max_size=1024) | None | Read part of the COG. | None |
| preview(max_size=1024) | None | Read preview of the COG. | None |
| point((10, 10), indexes=1) | None | Read a point value from the COG. | None |
| stats(pmin=5, pmax=95) | None | Get Raster statistics. | None |
| meta(pmin=5, pmax=95) | None | Get info + raster statistics | None |

#### Ancestors (in MRO)

* rio_tiler.io.base.BaseReader

#### Descendants

* rio_tiler.io.cogeo.GCPCOGReader

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

    
#### close

```python3
def close(
    self
)
```

    
Close rasterio dataset.

    
#### info

```python3
def info(
    self
) -> Dict
```

    
Return COG info.

    
#### metadata

```python3
def metadata(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    **kwargs: Any
) -> Dict
```

    
Return COG info and statistics.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    dst_crs: Union[rasterio.crs.CRS, NoneType] = None,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    max_size: int = 1024,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read part of a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | bounds to read (left, bottom, right, top) in "bounds_crs". | None |
| dst_crs | CRS or str | Target coordinate reference system, default is the bbox CRS. | the |
| bounds_crs | CRS or str | bounds coordinate reference system, default is "epsg:4326" | is |
| max_size | int | Limit output size array, default is 1024. | 1024. |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.part' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> List
```

    
Read a value from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| address | str | file url. | None |
| lon | float | Longitude | None |
| lat | float | Latittude. | None |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.point' function. | None |

**Returns:**

| Type | Description |
|---|---|
| list | List of pixel values per bands indexes. |

    
#### preview

```python3
def preview(
    self,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Return a preview of a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.preview' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

    
#### stats

```python3
def stats(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    hist_options: Union[Dict, NoneType] = None,
    **kwargs: Any
) -> Dict
```

    
Return bands statistics from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| pmin | float, optional, (default: 2) | Histogram minimum cut. | None |
| pmax | float, optional, (default: 98) | Histogram maximum cut. | None |
| hist_options | dict | Options to forward to numpy.histogram function.
e.g: {bins=20, range=(0, 1000)} | None |
| kwargs | optional | These are passed to 'rio_tiler.reader.stats' | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Dictionary with bands statistics. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    tilesize: int = 256,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Mercator Map tile from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Mercator tile X index. | None |
| tile_y | int | Mercator tile Y index. | None |
| tile_z | int | Mercator tile ZOOM level. | None |
| tilesize | int, optional (default: 256) | Output image size. | None |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.part' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

### GCPCOGReader

```python3
class GCPCOGReader(
    filepath: str,
    dataset: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.io.MemoryFile, rasterio.vrt.WarpedVRT] = None,
    minzoom: int = None,
    maxzoom: int = None,
    colormap: Dict = None,
    nodata: Union[float, int, str, NoneType] = None,
    unscale: Union[bool, NoneType] = None,
    resampling_method: Union[rasterio.enums.Resampling, NoneType] = None,
    vrt_options: Union[Dict, NoneType] = None,
    post_process: Union[Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]], NoneType] = None
)
```

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| src_dataset | DatasetReader | rasterio openned dataset. | None |
| dataset | WarpedVRT | rasterio WarpedVRT dataset. | None |

#### Ancestors (in MRO)

* rio_tiler.io.cogeo.COGReader
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

    
#### close

```python3
def close(
    self
)
```

    
Close rasterio dataset.

    
#### info

```python3
def info(
    self
) -> Dict
```

    
Return COG info.

    
#### metadata

```python3
def metadata(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    **kwargs: Any
) -> Dict
```

    
Return COG info and statistics.

    
#### part

```python3
def part(
    self,
    bbox: Tuple[float, float, float, float],
    dst_crs: Union[rasterio.crs.CRS, NoneType] = None,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    max_size: int = 1024,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read part of a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| bbox | tuple | bounds to read (left, bottom, right, top) in "bounds_crs". | None |
| dst_crs | CRS or str | Target coordinate reference system, default is the bbox CRS. | the |
| bounds_crs | CRS or str | bounds coordinate reference system, default is "epsg:4326" | is |
| max_size | int | Limit output size array, default is 1024. | 1024. |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.part' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

    
#### point

```python3
def point(
    self,
    lon: float,
    lat: float,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> List
```

    
Read a value from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| address | str | file url. | None |
| lon | float | Longitude | None |
| lat | float | Latittude. | None |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.point' function. | None |

**Returns:**

| Type | Description |
|---|---|
| list | List of pixel values per bands indexes. |

    
#### preview

```python3
def preview(
    self,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Return a preview of a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.preview' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

    
#### stats

```python3
def stats(
    self,
    pmin: float = 2.0,
    pmax: float = 98.0,
    hist_options: Union[Dict, NoneType] = None,
    **kwargs: Any
) -> Dict
```

    
Return bands statistics from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| pmin | float, optional, (default: 2) | Histogram minimum cut. | None |
| pmax | float, optional, (default: 98) | Histogram maximum cut. | None |
| hist_options | dict | Options to forward to numpy.histogram function.
e.g: {bins=20, range=(0, 1000)} | None |
| kwargs | optional | These are passed to 'rio_tiler.reader.stats' | None |

**Returns:**

| Type | Description |
|---|---|
| dict | Dictionary with bands statistics. |

    
#### tile

```python3
def tile(
    self,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    tilesize: int = 256,
    indexes: Union[int, Sequence, NoneType] = None,
    expression: Union[str, NoneType] = '',
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read a Mercator Map tile from a COG.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| tile_x | int | Mercator tile X index. | None |
| tile_y | int | Mercator tile Y index. | None |
| tile_z | int | Mercator tile ZOOM level. | None |
| tilesize | int, optional (default: 256) | Output image size. | None |
| indexes | int or sequence of int | Band indexes (e.g. 1 or (1, 2, 3)) | None |
| expression | str | rio-tiler expression (e.g. b1/b2+b3) | None |
| kwargs | dict | These will be passed to the 'rio_tiler.reader.part' function. | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |