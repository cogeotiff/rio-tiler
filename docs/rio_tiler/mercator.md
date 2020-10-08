# Module rio_tiler.mercator

rio-tiler: mercator utility functions.

None

## Functions

    
### get_zooms

```python3
def get_zooms(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    ensure_global_max_zoom: bool = False,
    tilesize: int = 256
) -> Tuple[int, int]
```

    
Calculate raster min/max mercator zoom level.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader | Rasterio io.DatasetReader object | None |
| ensure_global_max_zoom | bool | Apply latitude correction factor to ensure max_zoom equality for global
datasets covering different latitudes (default: False). | False |
| tilesize | int | Mercator tile size (default: 256). | 256 |

**Returns:**

| Type | Description |
|---|---|
| Tuple | Min/Max Mercator zoom levels. |

    
### zoom_for_pixelsize

```python3
def zoom_for_pixelsize(
    pixel_size: float,
    max_z: int = 24,
    tilesize: int = 256
) -> int
```

    
Get mercator zoom level corresponding to a pixel resolution.

Freely adapted from
https://github.com/OSGeo/gdal/blob/b0dfc591929ebdbccd8a0557510c5efdb893b852/gdal/swig/python/scripts/gdal2tiles.py#L294

Parameters
----------
    pixel_size: float
        Pixel size
    max_z: int, optional (default: 24)
        Max mercator zoom level allowed
    tilesize: int, optional
        Mercator tile size (default: 256).

Returns
-------
    Mercator zoom level corresponding to the pixel resolution