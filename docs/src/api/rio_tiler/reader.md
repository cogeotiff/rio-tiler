# Module rio_tiler.reader

rio-tiler.reader: low level reader.

None

## Functions

    
### part

```python3
def part(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    padding: int = 0,
    dst_crs: Union[rasterio.crs.CRS, NoneType] = None,
    bounds_crs: Union[rasterio.crs.CRS, NoneType] = None,
    minimum_overlap: Union[float, NoneType] = None,
    vrt_options: Union[Dict, NoneType] = None,
    max_size: Union[int, NoneType] = None,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read part of a dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| bounds | tuple | Output bounds (left, bottom, right, top). By default the coordinates are considered to be in either the dataset CRS or in the `dst_crs` if set. Use `bounds_crs` to set a specific CRS. | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| padding | int | Padding to apply to each edge of the tile when retrieving data to assist in reducing resampling artefacts along edges. Defaults to `0`. | `0` |
| dst_crs | rasterio.crs.CRS | Target coordinate reference system. | None |
| bounds_crs | rasterio.crs.CRS | Overwrite bounds Coordinate Reference System. | None |
| minimum_overlap | float | Minimum % overlap for which to raise an error with dataset not covering enough of the tile. | None |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| max_size | int | Limit output size array if not width and height. | None |
| kwargs | optional | Additional options to forward to `rio_tiler.reader.read`. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Mask (numpy.ndarray) values. |

    
### point

```python3
def point(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    coordinates: Tuple[float, float],
    indexes: Union[Sequence[int], int, NoneType] = None,
    coord_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    masked: bool = True,
    nodata: Union[float, int, str, NoneType] = None,
    unscale: bool = False,
    resampling_method: rasterio.enums.Resampling = 'nearest',
    vrt_options: Union[Dict, NoneType] = None,
    post_process: Union[Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]], NoneType] = None
) -> List
```

    
Read a pixel value for a point.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| coordinates | tuple | Coordinates in form of (X, Y). | None |
| indexes | sequence of int or int | Band indexes. | None |
| coord_crs | rasterio.crs.CRS | Coordinate Reference System of the input coords. Defaults to `epsg:4326`. | `epsg:4326` |
| masked | bool | Mask samples that fall outside the extent of the dataset. Defaults to `True`. | `True` |
| nodata | int or float | Overwrite dataset internal nodata value. | None |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| resampling_method | rasterio.enums.Resampling | Rasterio's resampling algorithm. Defaults to `nearest`. | `nearest` |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| list | Pixel value per band indexes. |

    
### preview

```python3
def preview(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    max_size: int = 1024,
    height: int = None,
    width: int = None,
    **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read decimated version of a dataset.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| max_size | int | Limit output size array if not width and height. Defaults to `1024`. | `1024` |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| kwargs | optional | Additional options to forward to `rio_tiler.reader.read`. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Mask (numpy.ndarray) values. |

    
### read

```python3
def read(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    indexes: Union[Sequence[int], int, NoneType] = None,
    window: Union[rasterio.windows.Window, NoneType] = None,
    force_binary_mask: bool = True,
    nodata: Union[float, int, str, NoneType] = None,
    unscale: bool = False,
    resampling_method: rasterio.enums.Resampling = 'nearest',
    vrt_options: Union[Dict, NoneType] = None,
    post_process: Union[Callable[[numpy.ndarray, numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]], NoneType] = None
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Low level read function.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| indexes | sequence of int or int | Band indexes. | None |
| window | rasterio.windows.Window | Window to read. | None |
| force_binary_mask | bool | Cast returned mask to binary values (0 or 255). Defaults to `True`. | `True` |
| nodata | int or float | Overwrite dataset internal nodata value. | None |
| unscale | bool | Apply 'scales' and 'offsets' on output data value. Defaults to `False`. | `False` |
| resampling_method | rasterio.enums.Resampling | Rasterio's resampling algorithm. Defaults to `nearest`. | `nearest` |
| vrt_options | dict | Options to be passed to the rasterio.warp.WarpedVRT class. | None |
| post_process | callable | Function to apply on output data and mask values. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | Data (numpy.ndarray) and Mask (numpy.ndarray) values. |