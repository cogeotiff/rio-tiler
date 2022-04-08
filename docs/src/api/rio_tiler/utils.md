# Module rio_tiler.utils

rio_tiler.utils: utility functions.

None

## Functions

    
### aws_get_object

```python3
def aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = False,
    client: <function Session.client at 0x15074af70> = None
) -> bytes
```

    
AWS s3 get object content.

    
### create_cutline

```python3
def create_cutline(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    geometry: Dict,
    geometry_crs: rasterio.crs.CRS = None
) -> str
```

    
Create WKT Polygon Cutline for GDALWarpOptions.

Ref: https://gdal.org/api/gdalwarp_cpp.html?highlight=vrt#_CPPv415GDALWarpOptions

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| geometry | dict | GeoJSON feature or GeoJSON geometry. By default the coordinates are considered to be in the dataset CRS. Use `geometry_crs` to set a specific CRS. | None |
| geometry_crs | rasterio.crs.CRS | Input geometry Coordinate Reference System | None |

**Returns:**

| Type | Description |
|---|---|
| str | WKT geometry in form of `POLYGON ((x y, x y, ...))) |

    
### get_array_statistics

```python3
def get_array_statistics(
    data: numpy.ma.core.MaskedArray,
    categorical: bool = False,
    categories: Union[List[float], NoneType] = None,
    percentiles: List[int] = [2, 98],
    **kwargs: Any
) -> List[Dict[Any, Any]]
```

    
Calculate per band array statistics.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ma.MaskedArray | input masked array data to get the statistics from. | None |
| categorical | bool | treat input data as categorical data. Defaults to False. | False |
| categories | list of numbers | list of categories to return value for. | None |
| percentiles | list of numbers | list of percentile values to calculate. Defaults to `[2, 98]`. | `[2, 98]` |
| kwargs | optional | options to forward to `numpy.histogram` function (only applies for non-categorical data). | None |

**Returns:**

| Type | Description |
|---|---|
| None | list of dict |

    
### get_bands_names

```python3
def get_bands_names(
    indexes: Union[Sequence[int], NoneType] = None,
    expression: Union[str, NoneType] = None,
    count: Union[int, NoneType] = None
) -> List[str]
```

    
Define bands names based on expression, indexes or band count.

    
### get_overview_level

```python3
def get_overview_level(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: int,
    width: int,
    dst_crs: rasterio.crs.CRS = CRS.from_epsg(3857)
) -> int
```

    
Return the overview level corresponding to the tile resolution.

Freely adapted from https://github.com/OSGeo/gdal/blob/41993f127e6e1669fbd9e944744b7c9b2bd6c400/gdal/apps/gdalwarp_lib.cpp#L2293-L2362

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| bounds | tuple | Bounding box coordinates in target crs (**dst_crs**). | None |
| height | int | Desired output height of the array for the input bounds. | None |
| width | int | Desired output width of the array for the input bounds. | None |
| dst_crs | rasterio.crs.CRS | Target Coordinate Reference System. Defaults to `epsg:3857`. | `epsg:3857` |

**Returns:**

| Type | Description |
|---|---|
| int | Overview level. |

    
### get_vrt_transform

```python3
def get_vrt_transform(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    dst_crs: rasterio.crs.CRS = CRS.from_epsg(3857),
    window_precision: int = 6
) -> Tuple[affine.Affine, int, int]
```

    
Calculate VRT transform.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT | Rasterio dataset. | None |
| bounds | tuple | Bounding box coordinates in target crs (**dst_crs**). | None |
| height | int | Desired output height of the array for the input bounds. | None |
| width | int | Desired output width of the array for the input bounds. | None |
| dst_crs | rasterio.crs.CRS | Target Coordinate Reference System. Defaults to `epsg:3857`. | `epsg:3857` |

**Returns:**

| Type | Description |
|---|---|
| tuple | VRT transform (affine.Affine), width (int) and height (int) |

    
### has_alpha_band

```python3
def has_alpha_band(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT]
) -> bool
```

    
Check for alpha band or mask in source.

    
### has_mask_band

```python3
def has_mask_band(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT]
) -> bool
```

    
Check for mask band in source.

    
### linear_rescale

```python3
def linear_rescale(
    image: numpy.ndarray,
    in_range: Tuple[Union[float, int], Union[float, int]],
    out_range: Tuple[Union[float, int], Union[float, int]] = (0, 255)
) -> numpy.ndarray
```

    
Apply linear rescaling to a numpy array.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| image | numpy.ndarray | array to rescale. | None |
| in_range | tuple | array min/max value to rescale from. | None |
| out_range | tuple | output min/max bounds to rescale to. Defaults to `(0, 255)`. | `(0, 255)` |

**Returns:**

| Type | Description |
|---|---|
| numpy.ndarray | linear rescaled array. |

    
### mapzen_elevation_rgb

```python3
def mapzen_elevation_rgb(
    data: numpy.ndarray
) -> numpy.ndarray
```

    
Encode elevation value to RGB values compatible with Mapzen tangram.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | Image array to encode.
Returns | None |
| numpy.ndarray | None | Elevation encoded in a RGB array. | None |

    
### non_alpha_indexes

```python3
def non_alpha_indexes(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT]
) -> Tuple
```

    
Return indexes of non-alpha bands.

    
### pansharpening_brovey

```python3
def pansharpening_brovey(
    rgb: numpy.ndarray,
    pan: numpy.ndarray,
    weight: float,
    pan_dtype: str
) -> numpy.ndarray
```

    
Apply Brovey pansharpening method.

Brovey Method: Each resampled, multispectral pixel is
multiplied by the ratio of the corresponding
panchromatic pixel intensity to the sum of all the
multispectral intensities.

Original code from https://github.com/mapbox/rio-pansharpen

    
### render

```python3
def render(
    data: numpy.ndarray,
    mask: Union[numpy.ndarray, NoneType] = None,
    img_format: str = 'PNG',
    colormap: Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType] = None,
    **creation_options: Any
) -> bytes
```

    
Translate numpy.ndarray to image bytes.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| data | numpy.ndarray | Image array to encode. | None |
| mask | numpy.ndarray | Mask array. | None |
| img_format | str | Image format. See: for the list of supported format by GDAL: https://www.gdal.org/formats_list.html. Defaults to `PNG`. | `PNG` |
| colormap | dict or sequence | RGBA Color Table dictionary or sequence. | None |
| creation_options | optional | Image driver creation options to forward to GDAL.
Returns | None |
| bytes | None | image body. | None |

    
### resize_array

```python3
def resize_array(
    data: numpy.ndarray,
    height: int,
    width: int,
    resampling_method: rasterio.enums.Resampling = 'nearest'
) -> numpy.ndarray
```

    
resize array to a given height and width.