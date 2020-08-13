## Using `rio-tiler` with Mosaics

![](https://user-images.githubusercontent.com/10407788/57467798-30505800-7251-11e9-9bde-6f50801dc851.png)

The `rio-tiler-mosaic` library has been moved into `rio-tiler`. The goal of the
`rio_tiler.mosaic` module is to create a mercator tile from _multiple_
observations. This is useful when a source image doesn't fill the entire
mercator tile of interest.

Often when creating a mercator tile from multiple assets, there will be portions
of overlap where a pixel could be chosen from multiple datasets. To handle this,
the `rio-tiler.mosaic` module provides _pixel selection methods_ which define
how to handle these cases for each pixel:

- **First**: select value from the first non-missing asset
- **Highest**: loop though all the assets and return the highest value
- **Lowest**: loop though all the assets and return the lowest value
- **Mean**: compute the mean value of the whole stack
- **Median**: compute the median value of the whole stack

### API

`rio_tiler.mosaic.mosaic_reader(assets, tiler, *args* pixel_selection=None, chunk_size=None, Threads=10, **kwargs)`

Inputs:

- assets : list, tuple of rio-tiler compatible assets (url or sceneid)
- tiler: Callable that returns a tuple of `numpy.array` (e.g `tile, mask = rio_tiler.reader.tile(x, y, z, **kwargs)`)
- *args: tiler specific arguments.
- pixel_selection : optional **pixel selection** algorithm (default: "first").
- chunk_size: optional, control the number of asset to process per loop.
- **kwargs: tiler specific keyword arguments.

Returns:
- (tile, mask), assets_used : tuple of ndarray Return (tile and mask) data and the list of used assets.

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
        future_tasks = [(executor.submit(_tiler, asset), asset) for asset in chunks]
```
By default the chunck_size is equal to the number or threads (or the number of assets if no threads=0)

#### More on threading

The number of threads used can be set in the function call with the `threads=` options. By default it will be equal to `multiprocessing.cpu_count() * 5` or to the MAX_THREADS environment variable.
In some case, threading can slow down your application. You can set threads to `0` or `1` to run the tiler in a loop without using a ThreadPool.

Benchmark:
```
--------------------------------- benchmark '1images': 6 tests ---------------------------------
Name (time in ms)         Min                Max               Mean             Median
------------------------------------------------------------------------------------------------
1images-0threads      64.3108 (1.0)      66.9192 (1.0)      65.0202 (1.0)      64.9370 (1.0)
1images-4threads      69.0893 (1.07)     70.9919 (1.06)     69.6718 (1.07)     69.5102 (1.07)
1images-1threads      69.4884 (1.08)     71.8967 (1.07)     70.0853 (1.08)     69.9804 (1.08)
1images-5threads      69.5552 (1.08)     75.5498 (1.13)     71.7882 (1.10)     70.9849 (1.09)
1images-3threads      69.7684 (1.08)     74.4098 (1.11)     70.6282 (1.09)     70.2353 (1.08)
1images-2threads      69.9258 (1.09)     73.8798 (1.10)     70.8861 (1.09)     70.3682 (1.08)
------------------------------------------------------------------------------------------------

----------------------------------- benchmark '5images': 6 tests -----------------------------------
Name (time in ms)          Min                 Max                Mean              Median
----------------------------------------------------------------------------------------------------
5images-5threads      104.1609 (1.0)      123.4442 (1.0)      110.4130 (1.0)      110.0683 (1.0)
5images-4threads      160.0952 (1.54)     170.7994 (1.38)     163.6062 (1.48)     161.8923 (1.47)
5images-3threads      161.2354 (1.55)     172.0363 (1.39)     165.1222 (1.50)     164.6513 (1.50)
5images-2threads      214.2413 (2.06)     220.7737 (1.79)     217.7740 (1.97)     217.9166 (1.98)
5images-0threads      228.2062 (2.19)     242.9397 (1.97)     231.9848 (2.10)     229.2843 (2.08)
5images-1threads      248.6630 (2.39)     251.8809 (2.04)     250.5195 (2.27)     251.2667 (2.28)
----------------------------------------------------------------------------------------------------
```
ref: https://github.com/cogeotiff/rio-tiler/issues/207#issuecomment-665958838

As mentioned in #207, using ThreadPool with 1 thread is always slower than not using thread.