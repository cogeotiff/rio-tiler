# Module rio_tiler.mosaic.reader

rio_tiler.mosaic: create tile from multiple assets.

None

## Variables

```python3
MAX_THREADS
```

## Functions

    
### mosaic_point_reader

```python3
def mosaic_point_reader(
    mosaic_assets: Sequence,
    reader: Callable[..., rio_tiler.models.PointData],
    *args: Any,
    pixel_selection: Union[Type[rio_tiler.mosaic.methods.base.MosaicMethodBase], rio_tiler.mosaic.methods.base.MosaicMethodBase] = <class 'rio_tiler.mosaic.methods.defaults.FirstMethod'>,
    chunk_size: Optional[int] = None,
    threads: int = 40,
    allowed_exceptions: Tuple = (<class 'rio_tiler.errors.PointOutsideBounds'>,),
    **kwargs
) -> Tuple[rio_tiler.models.PointData, List]
```

    
Merge multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mosaic_assets | sequence | List of assets. | None |
| reader | callable | Reader function. The function MUST take `(asset, *args, **kwargs)` as arguments, and MUST return a PointData object. | None |
| args | Any | Argument to forward to the reader function. | None |
| pixel_selection | MosaicMethod | Instance of MosaicMethodBase class. Defaults to `rio_tiler.mosaic.methods.defaults.FirstMethod`. | `rio_tiler.mosaic.methods.defaults.FirstMethod` |
| chunk_size | int | Control the number of asset to process per loop. | None |
| threads | int | Number of threads to use. If <= 1, runs single threaded without an event loop. By default reads from the MAX_THREADS environment variable, and if not found defaults to multiprocessing.cpu_count() * 5. | None |
| allowed_exceptions | tuple | List of exceptions which will be ignored. Note: `PointOutsideBounds` is likely to be raised and should be included in the allowed_exceptions. Defaults to `(TileOutsideBounds, )`. | `(TileOutsideBounds, )` |
| kwargs | optional | Reader callable's keywords options. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | PointData and assets (list). |

    
### mosaic_reader

```python3
def mosaic_reader(
    mosaic_assets: Sequence,
    reader: Callable[..., rio_tiler.models.ImageData],
    *args: Any,
    pixel_selection: Union[Type[rio_tiler.mosaic.methods.base.MosaicMethodBase], rio_tiler.mosaic.methods.base.MosaicMethodBase] = <class 'rio_tiler.mosaic.methods.defaults.FirstMethod'>,
    chunk_size: Optional[int] = None,
    threads: int = 40,
    allowed_exceptions: Tuple = (<class 'rio_tiler.errors.TileOutsideBounds'>,),
    **kwargs
) -> Tuple[rio_tiler.models.ImageData, List]
```

    
Merge multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| mosaic_assets | sequence | List of assets. | None |
| reader | callable | Reader function. The function MUST take `(asset, *args, **kwargs)` as arguments, and MUST return an ImageData. | None |
| args | Any | Argument to forward to the reader function. | None |
| pixel_selection | MosaicMethod | Instance of MosaicMethodBase class. Defaults to `rio_tiler.mosaic.methods.defaults.FirstMethod`. | `rio_tiler.mosaic.methods.defaults.FirstMethod` |
| chunk_size | int | Control the number of asset to process per loop. | None |
| threads | int | Number of threads to use. If <= 1, runs single threaded without an event loop. By default reads from the MAX_THREADS environment variable, and if not found defaults to multiprocessing.cpu_count() * 5. | None |
| allowed_exceptions | tuple | List of exceptions which will be ignored. Note: `TileOutsideBounds` is likely to be raised and should be included in the allowed_exceptions. Defaults to `(TileOutsideBounds, )`. | `(TileOutsideBounds, )` |
| kwargs | optional | Reader callable's keywords options. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple | ImageData and assets (list). |