# Module rio_tiler.reader

rio-tiler.reader: low level reader.

None

## Variables

```python3
WGS84_CRS
```

## Functions

    
### part

```python3
def part(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: Optional[int] = None,
    width: Optional[int] = None,
    max_size: Optional[int] = None,
    dst_crs: Optional[rasterio.crs.CRS] = None,
    bounds_crs: Optional[rasterio.crs.CRS] = None,
    indexes: Union[Sequence[int], int, NoneType] = None,
    minimum_overlap: Optional[float] = None,
    padding: Optional[int] = None,
    buffer: Optional[float] = None,
    force_binary_mask: bool = True,
    nodata: Union[float, int, str, NoneType] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    reproject_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'sum', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Optional[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray]] = None
) -> rio_tiler.models.ImageData
```

    
Read part of a dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| bounds | tuple | Output bounds (left, bottom, right, top). By default the coordinates are considered to be in either the dataset CRS or in the `dst_crs` if set. Use `bounds_crs` to set a specific CRS. | None |
| height | int | Output height of the image. | None |
| width | int | Output width of the image. | None |
| max_size | int | Limit output size image if not width and height. | None |
| dst_crs | rasterio.crs.CRS | Target coordinate reference system. | None |
| bounds_crs | rasterio.crs.CRS | Overwrite bounds Coordinate Reference System. | None |
| indexes | sequence of int or int | Band indexes. | None |
| minimum_overlap | float | Minimum % overlap for which to raise an error with dataset not covering enough of the tile. | None |
| padding | int | Padding to apply to each bbox edge. Helps reduce resampling artefacts along edges. Defaults to `0`. | `0` |
| buffer | float | Buffer to apply to each bbox edge. Defaults to `0.`. | `0.` |
| nodata | int or float | Overwrite dataset internal nodata value. | None |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| resampling_method | RIOResampling | RasterIO resampling algorithm. Defaults to `nearest`. | `nearest` |
| reproject_method | WarpResampling | WarpKernel resampling algorithm. Defaults to `nearest`. | `nearest` |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| None | ImageData |

    
### point

```python3
def point(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    coordinates: Tuple[float, float],
    indexes: Union[Sequence[int], int, NoneType] = None,
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    force_binary_mask: bool = True,
    nodata: Union[float, int, str, NoneType] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    reproject_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'sum', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Optional[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray]] = None
) -> rio_tiler.models.PointData
```

    
Read a pixel value for a point.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| coordinates | tuple | Coordinates in form of (X, Y). | None |
| indexes | sequence of int or int | Band indexes. | None |
| coord_crs | rasterio.crs.CRS | Coordinate Reference System of the input coords. Defaults to `epsg:4326`. | `epsg:4326` |
| nodata | int or float | Overwrite dataset internal nodata value. | None |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| resampling_method | RIOResampling | RasterIO resampling algorithm. Defaults to `nearest`. | `nearest` |
| reproject_method | WarpResampling | WarpKernel resampling algorithm. Defaults to `nearest`. | `nearest` |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| None | PointData |

    
### read

```python3
def read(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    dst_crs: Optional[rasterio.crs.CRS] = None,
    height: Optional[int] = None,
    width: Optional[int] = None,
    max_size: Optional[int] = None,
    indexes: Union[Sequence[int], int, NoneType] = None,
    window: Optional[rasterio.windows.Window] = None,
    force_binary_mask: bool = True,
    nodata: Union[float, int, str, NoneType] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'] = 'nearest',
    reproject_method: Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'sum', 'rms'] = 'nearest',
    unscale: bool = False,
    post_process: Optional[Callable[[numpy.ma.core.MaskedArray], numpy.ma.core.MaskedArray]] = None
) -> rio_tiler.models.ImageData
```

    
Low level read function.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| dst_crs | rasterio.crs.CRS | Target coordinate reference system. | None |
| height | int | Output height of the image. | None |
| width | int | Output width of the image. | None |
| max_size | int | Limit output size image if not width and height. | None |
| indexes | sequence of int or int | Band indexes. | None |
| window | rasterio.windows.Window | Window to read. | None |
| nodata | int or float | Overwrite dataset internal nodata value. | None |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| resampling_method | RIOResampling | RasterIO resampling algorithm. Defaults to `nearest`. | `nearest` |
| reproject_method | WarpResampling | WarpKernel resampling algorithm. Defaults to `nearest`. | `nearest` |
| force_binary_mask | bool | Cast returned mask to binary values (0 or 255). Defaults to `True`. | `True` |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| None | ImageData |

## Classes

### Options

```python3
class Options(
    /,
    *args,
    **kwargs
)
```

#### Ancestors (in MRO)

* builtins.dict

#### Methods

    
#### clear

```python3
def clear(
    ...
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    ...
)
```

    
D.copy() -> a shallow copy of D

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None,
    /
)
```

    
Create a new dictionary with keys from iterable and values set to value.

    
#### get

```python3
def get(
    self,
    key,
    default=None,
    /
)
```

    
Return the value for key if key is in the dictionary, else default.

    
#### items

```python3
def items(
    ...
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    ...
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    ...
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, default is returned if given, otherwise KeyError is raised

    
#### popitem

```python3
def popitem(
    self,
    /
)
```

    
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None,
    /
)
```

    
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

    
#### update

```python3
def update(
    ...
)
```

    
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.

If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]

    
#### values

```python3
def values(
    ...
)
```

    
D.values() -> an object providing a view on D's values