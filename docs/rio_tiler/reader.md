# Module rio_tiler.reader

rio-tiler.reader: image utility functions.

None

## Functions

    
### metadata

```python3
def metadata(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Union[Tuple[float, float, float, float], NoneType] = None,
    indexes: Union[Sequence[int], int, NoneType] = None,
    max_size: int = 1024,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    percentiles: Tuple[float, float] = (2.0, 98.0),
    hist_options: Union[Dict, NoneType] = None,
    **kwargs: Any
) -> Dict
```

    
Retrieve metadata and statistics from an image.

Attributes
----------
    src_dst : rasterio.io.DatasetReader
        rasterio.io.DatasetReader object
    bounds : tuple, optional
        Bounding box coordinates from which to calculate image statistics.
    max_size : int
        `max_size` of the longest dimension, respecting
        bounds X/Y aspect ratio.
    indexes : list of ints or a single int, optional
        Band indexes.
    bounds_crs: CRS or str, optional
        Specify bounds coordinate reference system, default WGS84/EPSG4326.
    percentiles: tuple, optional
        Tuple of Min/Max percentiles to compute. Default is (2, 98).
    hist_options : dict, optional
        Options to forward to numpy.histogram function.
    kwargs : Any, optional
        Additional options to forward to part or preview

Returns
-------
    dict

    
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

    
Read part of an image.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader | rasterio.io.DatasetReader object | None |
| bounds | tuple | Output bounds (left, bottom, right, top) in target crs ("dst_crs"). | None |
| height | int | Output height of the array. | None |
| width | int | Output width of the array. | None |
| padding | int | Padding to apply to each edge of the tile when retrieving data
    to assist in reducing resampling artefacts along edges. | None |
| dst_crs | CRS or str | Target coordinate reference system, default is "epsg:3857". | is |
| bounds_crs | CRS or str | Overwrite bounds coordinate reference system, default is equal
    to the output CRS (dst_crs). | equal |
| minimum_tile_cover | float | Minimum % overlap for which to raise an error with dataset not
    covering enought of the tile. | None |
| vrt_options | dict | These will be passed to the rasterio.warp.WarpedVRT class. | None |
| max_size | int | Limit output size array if not widht and height. | None |
| kwargs | Any | Additional options to forward to reader._read() | None |

**Returns:**

| Type | Description |
|---|---|
| numpy ndarray | None |

    
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

    
Read point value

Attributes
----------
    src_dst : rasterio.io.DatasetReader
        rasterio.io.DatasetReader object
    coordinates : tuple
        (X, Y) coordinates.
    indexes : list of ints or a single int, optional
        Band indexes
    coord_crs : rasterio.crs.CRS, optional
        (X, Y) coordinate system. Default is WGS84/EPSG:4326.
    nodata: int or float, optional
    unscale, bool, optional
        If True, apply scale and offset to the data.
        Default is set to False.
    masked : bool
        Whether to mask samples that fall outside the extent of the dataset.
        Default is set to True.
    vrt_options: dict, optional
        These will be passed to the rasterio.warp.WarpedVRT class.

Returns
-------
    point : list
        List of pixel values per bands indexes.

    
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

    
Read image and resample to low resolution.

Attributes
----------
    src_dst : rasterio.io.DatasetReader
        rasterio.io.DatasetReader object
    max_size : int
        `max_size` of the longest dimension, respecting
        bounds X/Y aspect ratio.
    height: int, optional
        output height of the data
    width: int, optional
        output width of the data
    kwargs : Any, optional
        Additional options to forward to reader._read()

Returns
-------
    data : numpy ndarray
    mask: numpy array

    
### stats

```python3
def stats(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    bounds: Union[Tuple[float, float, float, float], NoneType] = None,
    indexes: Union[Sequence[int], int, NoneType] = None,
    max_size: int = 1024,
    bounds_crs: rasterio.crs.CRS = CRS.from_epsg(4326),
    percentiles: Tuple[float, float] = (2.0, 98.0),
    hist_options: Union[Dict, NoneType] = None,
    **kwargs: Any
) -> Dict
```

    
Retrieve statistics from an image.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| src_dst | rasterio.io.DatasetReader | rasterio.io.DatasetReader object | None |
| bounds | tuple | Bounding box coordinates from which to calculate image statistics. | None |
| max_size | int | `max_size` of the longest dimension, respecting
bounds X/Y aspect ratio. | None |
| indexes | list of ints or a single int | Band indexes. | None |
| bounds_crs | CRS or str | Specify bounds coordinate reference system, default WGS84/EPSG4326. | WGS84 |
| percentiles | tuple | Tuple of Min/Max percentiles to compute. Default is (2, 98). | is |
| hist_options | dict | Options to forward to numpy.histogram function. | None |
| kwargs | Any | Additional options to forward to part or preview | None |

**Returns:**

| Type | Description |
|---|---|
| dict | None |

    
### tile

```python3
def tile(
    src_dst: Union[rasterio.io.DatasetReader, rasterio.io.DatasetWriter, rasterio.vrt.WarpedVRT],
    x: int,
    y: int,
    z: int,
    tilesize: int = 256,
    **kwargs
) -> Tuple[numpy.ndarray, numpy.ndarray]
```

    
Read mercator tile from an image.

Attributes
----------
    src_dst : rasterio.io.DatasetReader
        rasterio.io.DatasetReader object
    x : int
        Mercator tile X index.
    y : int
        Mercator tile Y index.
    z : int
        Mercator tile ZOOM level.
    tilesize : int, optional
        Output tile size. Default is 256.
    kwargs : Any, optional
        Additional options to forward to part()

Returns
-------
    data : numpy ndarray
    mask: numpy array