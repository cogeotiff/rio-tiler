
## Mosaic

![](https://user-images.githubusercontent.com/10407788/57467798-30505800-7251-11e9-9bde-6f50801dc851.png)

The goal of rio_tiler.mosaic submodule is to create tiles from multiple observations. 

Because user might want to choose which pixel goes on top of the tile, this plugin comes with 5 differents `pixel selection` algorithms:
- **First**: takes the first pixel received
- **Highest**: loop though all the assets and return the highest value 
- **Lowest**: loop though all the assets and return the lowest value
- **Mean**: compute the mean value of the whole stack
- **Median**: compute the median value of the whole stack

### API

`rio_tiler.mosaic.mosaic_reader(assets, tiler, *args* pixel_selection=None, chunk_size=None, Threads=10, **kwargs)`

Inputs:
- assets : list, tuple of rio-tiler compatible assets (url or sceneid)
- tiler: Rio-tiler's tiler function (e.g rio_tiler.landsat8.tile) 
- *args: tiler specific arguments.
- pixel_selection : optional **pixel selection** algorithm (default: "first"). 
- chunk_size: optional, control the number of asset to process per loop.
- **kwargs: tiler specific keyword arguments.

Returns:
- tile, mask : tuple of ndarray Return tile and mask data.

#### Examples

```python
from rio_tiler.io import COGReader
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.mosaic.methods import defaults


def tiler(src_path: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
    with COGReader(src_path) as cog:
        return cog.tile(*args, **kwargs)

assets = ["mytif1.tif", "mytif2.tif", "mytif3.tif"]
tile = (1000, 1000, 9)
x, y, z = tile

# Use Default First value method
mosaic_reader(assets, tiler, x, y, z)

# Use Highest value: defaults.HighestMethod()
mosaic_reader(
    assets,
    tiler,
    x,
    y,
    z,
    pixel_selection=defaults.HighestMethod()
)

# Use Lowest value: defaults.LowestMethod()
mosaic_reader(
    assets,
    tiler,
    x,
    y,
    z,
    pixel_selection=defaults.LowestMethod()
)
```

### The `MosaicMethod` interface

the `rio_tiler.mosaic.methods.base.MosaicMethodBase` class defines an abstract 
interface for all `pixel selection` methods allowed by `rio_tiler.mosaic.mosaic_reader`. its methods and properties are:

- `is_done`: property, returns a boolean indicating if the process is done filling the tile
- `data`: property, returns the output **tile** and **mask** numpy arrays
- `feed(tile: numpy.ma.ndarray)`: method, update the tile

The MosaicMethodBase class is not intended to be used directly but as an abstract base class, a template for concrete implementations.

#### Writing your own Pixel Selection method

The rules for writing your own `pixel selection algorithm` class are as follows:

- Must inherit from MosaicMethodBase
- Must provide concrete implementations of all the above methods.

See [rio_tiler.mosaic.methods.defaults](/rio_tiler/mosaic/methods/defaults.py) classes for examples.

#### Smart Multi-Threading 

When dealing with an important number of image, you might not want to process the whole stack, especially if the pixel selection method stops when the tile is filled. To allow better optimization, `rio_tiler.mosaic.mosaic_reader` is fetching the tiles in parallel (threads) but to limit the number of files we also embeded the fetching in a loop (creating 2 level of processing): 

```python
assets = ["1.tif", "2.tif", "3.tif", "4.tif", "5.tif", "6.tif"]

# 1st level loop - Creates chuncks of assets
for chunks in _chunks(assets, chunk_size):
    
    # 2nd level loop - Uses threads for process each `chunck`
    with futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_tasks = [executor.submit(_tiler, asset) for asset in chunks]
```
By default the chunck_size is equal to the number or threads (or the number of assets if no threads=0)

#### More on threading

The number of threads used can be set in the function call with the `threads=` options. By default it will be equal to `multiprocessing.cpu_count() * 5` or to the MAX_THREADS environment variable.
In some case, threading can slow down your application. You can set threads to `0` to run the tiler in a loop without using a ThreadPool.
