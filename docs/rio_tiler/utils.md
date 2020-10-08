# Module rio_tiler.utils

rio_tiler.utils: utility functions.

None

## Variables

```python3
DataSet
```

## Functions

    
### aws_get_object

```python3
def aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = False,
    client: <function Session.client at 0x7fa527049050> = None
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
| src_dst | rasterio.io.DatasetReader | rasterio.io.DatasetReader object | None |
| geometry | dict | GeoJSON feature or GeoJSON geometry | None |
| geometry_crs | CRS or str | Specify bounds coordinate reference system, default is same as input dataset. | same |

**Returns:**

| Type | Description |
|---|---|
| str | Cutline WKT geometry in form of `POLYGON ((x y, x y, ...))) |

    
### geotiff_options

```python3
def geotiff_options(
    x: int,
    y: int,
    z: int,
    tilesize: int = 256,
    dst_crs: rasterio.crs.CRS = CRS.from_epsg(3857)
) -> Dict
```

    
GeoTIFF options.

Attributes
----------
    x : int
        Mercator tile X index.
    y : int
        Mercator tile Y index.
    z : int
        Mercator tile ZOOM level.
    tilesize : int, optional
        Output tile size. Default is 256.
    dst_crs: CRS, optional
        Target coordinate reference system, default is "epsg:3857".

Returns
-------
    dict

    
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

Attributes
----------
    src_dst : rasterio.io.DatasetReader
        Rasterio io.DatasetReader object
    bounds : list
        Bounds (left, bottom, right, top) in target crs ("dst_crs").
    height : int
        Output height.
    width : int
        Output width.
    dst_crs: CRS or str, optional
        Target coordinate reference system (default "epsg:3857").

Returns
-------
    ovr_idx: Int or None
        Overview level

    
### get_vrt_transform

```python3
def get_vrt_transform(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: Union[int, NoneType] = None,
    width: Union[int, NoneType] = None,
    dst_crs: rasterio.crs.CRS = CRS.from_epsg(3857)
) -> Tuple[affine.Affine, int, int]
```

    
Calculate VRT transform.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader | Rasterio io.DatasetReader object | None |
| bounds | list | Bounds (left, bottom, right, top) in target crs ("dst_crs"). | None |
| height | int | Desired output height of the array for the bounds. | None |
| width | int | Desired output width of the array for the bounds. | None |
| dst_crs | CRS or str | Target coordinate reference system (default "epsg:3857"). | None |

**Returns:**

| Type | Description |
|---|---|
| Affine | Output affine transformation matrix |

    
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
    in_range: Tuple[Union[int, float], Union[int, float]] = (0, 1),
    out_range: Tuple[Union[int, float], Union[int, float]] = (1, 255)
) -> numpy.ndarray
```

    
Linear rescaling.

Attributes
----------
    image : numpy ndarray
        Image array to rescale.
    in_range : list, int, optional, (default: [0,1])
        Image min/max value to rescale.
    out_range : list, int, optional, (default: [1,255])
        output min/max bounds to rescale to.

Returns
-------
    out : numpy ndarray
        returns rescaled image array.

    
### mapzen_elevation_rgb

```python3
def mapzen_elevation_rgb(
    arr: numpy.ndarray
) -> numpy.ndarray
```

    
Encode elevation value to RGB values compatible with Mapzen tangram.

Attributes
----------
    arr : numpy ndarray
        Image array to encode.

Returns
-------
    out : numpy ndarray
        RGB array (3, h, w)

    
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

    
Brovey Method: Each resampled, multispectral pixel is

multiplied by the ratio of the corresponding
panchromatic pixel intensity to the sum of all the
multispectral intensities.

Original code from https://github.com/mapbox/rio-pansharpen

    
### render

```python3
def render(
    tile: numpy.ndarray,
    mask: Union[numpy.ndarray, NoneType] = None,
    img_format: str = 'PNG',
    colormap: Union[Dict, NoneType] = None,
    **creation_options: Any
) -> bytes
```

    
Translate numpy ndarray to image buffer using GDAL.

Usage
-----
    tile, mask = rio_tiler.utils.tile_read(......)
    with open('test.jpg', 'wb') as f:
        f.write(render(tile, mask, img_format="jpeg"))

Attributes
----------
    tile : numpy ndarray
        Image array to encode.
    mask: numpy ndarray, optional
        Mask array
    img_format: str, optional
        Image format to return (default: 'png').
        List of supported format by GDAL: https://www.gdal.org/formats_list.html
    colormap: dict, optional
        GDAL RGBA Color Table dictionary.
    creation_options: dict, optional
        Image driver creation options to pass to GDAL

Returns
-------
    bytes: BytesIO
        Reurn image body.

    
### tile_exists

```python3
def tile_exists(
    bounds: Tuple[float, float, float, float],
    tile_z: int,
    tile_x: int,
    tile_y: int
) -> bool
```

    
Check if a mercatile tile is inside a given bounds.

Attributes
----------
    bounds : list
        WGS84 bounds (left, bottom, right, top).
    z : int
        Mercator tile ZOOM level.
    y : int
        Mercator tile Y index.
    x : int
        Mercator tile Y index.

Returns
-------
    out : boolean
        if True, the z-x-y mercator tile in inside the bounds.