# Module rio_tiler.mosaic.reader

rio_tiler.mosaic: create tile from multiple assets.

None

## Variables

```python3
MAX_THREADS
```

## Functions

    
### mosaic_reader

```python3
def mosaic_reader(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    pixel_selection: Union[Type[rio_tiler.mosaic.methods.base.MosaicMethodBase], rio_tiler.mosaic.methods.base.MosaicMethodBase] = <class 'rio_tiler.mosaic.methods.defaults.FirstMethod'>,
    chunk_size: Union[int, NoneType] = None,
    threads: int = 80,
    **kwargs
) -> Tuple[Tuple[numpy.ndarray, numpy.ndarray], Sequence[str]]
```

    
Merge multiple assets.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| assets | list or tuple | List of tiler compatible asset. | None |
| reader | callable | reader function. The function MUST take asset, *args, **kwargs as arguments,
and MUST return a tuple with tile data and mask
e.g:
def reader(asset: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
    with COGReader(asset) as cog:
        return cog.tile(*args, **kwargs)

def reader(asset: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
    with COGReader(asset) as cog:
        return cog.preview(*args, **kwargs) | None |
| args | Any | additional argument to forward to the reader function. | None |
| pixel_selection | MosaicMethod | Instance of MosaicMethodBase class.
default: "rio_tiler.mosaic.methods.defaults.FirstMethod". | s.FirstMethod |
| chunk_size | int | Control the number of asset to process per loop (default = threads). | threads |
| threads | int | Number of threads to use. If <= 1, runs single threaded without an event
loop. By default reads from the MAX_THREADS environment variable, and if
not found defaults to multiprocessing.cpu_count() * 5. | reads |
| kwargs | dict | tiler specific options. | None |

**Returns:**

| Type | Description |
|---|---|
| tuple of ndarray, sequence of str | Return (tile, mask) data and list of assets used. |