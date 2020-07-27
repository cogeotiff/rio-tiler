# Rio-tiler

<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/88133997-77560f00-cbb1-11ea-874c-a8f1d123a9df.jpg" style="max-width: 800px;" alt="rio-tiler"></a>
</p>
<p align="center">
  <em>Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF.</em>
</p>
<p align="center">
  <a href="https://circleci.com/gh/cogeotiff/rio-tiler" target="_blank">
      <img src="https://circleci.com/gh/cogeotiff/rio-tiler.svg?style=svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/cogeotiff/rio-tiler" target="_blank">
      <img src="https://codecov.io/gh/cogeotiff/rio-tiler/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/rio-tiler" target="_blank">
      <img src="https://img.shields.io/pypi/v/rio-tiler?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://anaconda.org/conda-forge/rio-tiler)" target="_blank">
      <img src="https://img.shields.io/conda/v/conda-forge/rio-tiler.svg" alt="Conda Forge">
  </a>
  <a href="https://pypistats.org/packages/rio-tiler" target="_blank">
      <img src="https://img.shields.io/pypi/dm/rio-tiler.svg" alt="Downloads">
  </a>
  <a href="https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE.txt" target="_blank">
      <img src="https://img.shields.io/github/license/cogeotiff/rio-tiler.svg" alt="Downloads">
  </a>
</p>

## Install

You can install rio-tiler using pip

```bash
$ pip install -U pip
$ pip install rio-tiler --pre # version 2.0 is in development
```

or install from source:

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -U pip
$ pip install -e .
```

## Usage

The `rio_tiler` module can create mercator tiles from any raster source supported by Rasterio/GDAL (i.e. local files, http, s3, gcs etc.). Additional method are availables (see [COGReader](#COGReader))

#### Read a tile from a file

```python
from rio_tiler.io import COGReader

with COGReader("http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif") as cog:
    tile, mask = cog.tile(691559, 956905, 21, tilesize=256)

print(tile.shape)
> (3, 256, 256)

print(mask.shape)
> (256, 256)
```

#### Render the array as an image (PNG/JPEG)

```python
from rio_tiler.utils import render

buffer = render(tile, mask=mask) # this returns a buffer (PNG by default)
```

Rescale non-byte data and/or apply colormap

```python
from rio_tiler.colormap import cmap
from rio_tiler.utils import linear_rescale

# Rescale the tile array only where mask is valid and cast it to byte
tile = numpy.where(
    mask,
    linear_rescale(tile, in_range=(0, 1000), out_range=[0, 255]),
    0
).astype(numpy.uint8)

cm = cmap.get("viridis")

buffer = render(tile, mask=mask, colormap=cm)
```

Use creation options to match `mapnik` defaults.

```python
from rio_tiler.utils import render
from rio_tiler.profiles import img_profiles

options = img_profiles.get("webp")
buffer = render(tile, mask=mask, img_format="webp", **options)
```

Write image to file

```python
with open("my.png", "wb") as f:
  f.write(buffer)
```

### COGReader

<details>

```python
class COGReader:
    """
    Cloud Optimized GeoTIFF Reader.

    Examples
    --------
    with COGReader(src_path) as cog:
        cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with WarpedVRT(src_dst, ...) as vrt_dst:
            with COGReader(None, dataset=vrt_dst) as cog:
                cog.tile(...)

    with rasterio.open(src_path) as src_dst:
        with COGReader(None, dataset=src_dst) as cog:
            cog.tile(...)

    Attributes
    ----------
    filepath: str
        Cloud Optimized GeoTIFF path.
    dataset: rasterio.DatasetReader, optional
        Rasterio dataset.

    Properties
    ----------
    minzoom: int
        COG minimum zoom level.
    maxzoom: int
        COG maximum zoom level.
    bounds: tuple[float]
        COG bounds in WGS84 crs.
    center: tuple[float, float, int]
        COG center + minzoom
    colormap: dict
        COG internal colormap.
    info: dict
        General information about the COG (datatype, indexes, ...)

    Methods
    -------
    tile(0, 0, 0, indexes=(1,2,3), expression="B1/B2", tilesize=512, resampling_methods="nearest")
        Read a map tile from the COG.
    part((0,10,0,10), indexes=(1,2,3,), expression="B1/B20", max_size=1024)
        Read part of the COG.
    preview(max_size=1024)
        Read preview of the COG.
    point((10, 10), indexes=1)
        Read a point value from the COG.
    stats(pmin=5, pmax=95)
        Get Raster statistics.
    meta(pmin=5, pmax=95)
        Get info + raster statistics
    """
```

</details>

#### Properties

- **dataset**: Return the rasterio dataset
- **colormap**: Return the dataset's internal colormap
- **minzoom**: Return minimum Mercator Zoom
- **maxzoom**: Return maximum Mercator Zoom
- **bounds**: Return the dataset bounds in WGS84
- **center**: Return the center of the dataset + minzoom
- **spatial_info**: Return the bounds, center and zoom infos
- **info**: Return simple metadata about the dataset

```python
with COGReader("myfile.tif") as cog:
    print(cog.info)
{
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "center": [-101.98868496889182, 23.548959503763047, 3],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [[1, {}]],
    "band_descriptions": [[1,"band1"]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "nodata_type": "Nodata",
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255],
        ...
    }
}
```

#### Methods

- **tile()**: Read map tile from a raster

```python
with COGReader("myfile.tif") as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256)

# With indexes
with COGReader("myfile.tif") as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256, indexes=1)

# With expression
with COGReader("myfile.tif"s) as cog:
    tile, mask = cog.tile(1, 2, 3, tilesize=256, expression="B1/B2")
```

- **part()**: Read part of a raster

```python
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20))

# Limit output size (default is set to 1024)
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), max_size=2000)

# Read high resolution
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), max_size=None)

# With indexes
with COGReader("myfile.tif") as cog:
     data, mask = cog.part((10, 10, 20, 20), indexes=1)

# With expression
with COGReader("myfile.tif") as cog:
    data, mask = cog.part((10, 10, 20, 20), expression="B1/B2")
```

- **preview()**: Read a preview of a raster

```python
with COGReader("myfile.tif") as cog: 
    data, mask = cog.preview()

# With indexes
with COGReader("myfile.tif") as cog: 
    data, mask = cog.preview(indexes=1)

# With expression
with COGReader("myfile.tif") as cog: 
    data, mask = cog.preview(expression="B1+2,B1*4")
```

- **point()**: Read point value of a raster

```python
with COGReader("myfile.tif") as cog: 
    print(cog.point(-100, 25))

# With indexes
with COGReader("myfile.tif") as cog: 
    print(cog.point(-100, 25, indexes=1)) 
[1]

# With expression
with COGReader("myfile.tif") as cog: 
    print(cog.point(-100, 25, expression="B1+2,B1*4"))
[3, 4]
```

- **stats()**: Return image statistics (Min/Max/Stdev)

```python
with COGReader("myfile.tif") as cog:
    print(cog.stats())
{
    "1": {
        "pc": [1, 16],
        "min": 1,
        "max": 18,
        "std": 4.069636227214257,
        "histogram": [
            [...],
            [...]
        ]
    }
}
```

- **metadata()**: Return COG info + statistics

```python
with COGReader("myfile.tif") as cog:
    print(cog.metadata())
{
    "bounds": [-119.05915661478785, 13.102845359730287, -84.91821332299578, 33.995073647795806],
    "center": [-101.98868496889182, 23.548959503763047, 3],
    "minzoom": 3,
    "maxzoom": 12,
    "band_metadata": [[1, {}]],
    "band_descriptions": [[1,"band1"]],
    "dtype": "int8",
    "colorinterp": ["palette"],
    "nodata_type": "Nodata",
    "colormap": {
        "0": [0, 0, 0, 0],
        "1": [0, 61, 0, 255],
        ...
    }
    "statistics" : {
        1: {
            "pc": [1, 16],
            "min": 1,
            "max": 18,
            "std": 4.069636227214257,
            "histogram": [
                [...],
                [...]
            ]
        }
    }
}
```

### STACReader

In rio-tiler v2, we added a `rio_tiler.io.STACReader` to allow tile/metadata fetching of assets withing a STAC item. The STACReader objects has the same properties/methods as the COGReader.

```python
from typing import Dict 
from rio_tiler.io import STACReader

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A", 
    exclude_assets={"thumbnail"} 
) as stac: 
    print(stac.bounds)
    print(stac.assets)

> [23.293255090449595, 31.505183020453355, 24.296453548295318, 32.51147809805106]
> ['overview', 'visual', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12', 'AOT', 'WVP', 'SCL']

# Name of assets to read
assets = ["B01", "B02"]

with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A", 
    exclude_assets={"thumbnail"} 
) as stac:
    tile, mask = stac.tile(145, 103, 8, tilesize=256, assets=assets)

print(tile.shape)
> (2, 256, 256)

# With expression
with STACReader(
    "https://1tqdbvsut9.execute-api.us-west-2.amazonaws.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_34SGA_20200318_0_L2A", 
    exclude_assets={"thumbnail"} 
) as stac:
    tile, mask = stac.tile(145, 103, 8, tilesize=256, expression="B01/B02")

print(tile.shape)
> (1, 256, 256)
```

## Working with multiple assets

#### Mosaic

Starting in rio-tiler 2.0, we've transfered the [rio-tiler-mosaic](https://github.com/cogeotiff/rio-tiler-mosaic) plugin to be a rio-tiler submodule.

```python
from rio_tiler.io import COGReader
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.mosaic.methods import defaults


def tiler(src_path: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
    with COGReader(src_path) as cog:
        return cog.tile(*args, **kwargs)

assets = ["mytif1.tif", "mytif2.tif", "mytif3.tif"]
tile, mask = mosaic_reader(assets, tiler, 1, 1, 1)
```

You can also 

Learn more about `rio_tiler.mosaic` in [doc/mosaic.md](doc/mosaic.md).

Notebook: [WorkingWithMosaic](Notebook/Using-rio-tiler-mosaic.ipynb)

#### Merge assets

`rio_tiler.io.cogeo` submodule has `multi_*` functions (tile, part, preview, point, metadata, info, stats) allowing to fetch and merge info/data 
from multiple dataset (think about multiple bands stored in separated files).

```python
from typing import Dict 
from rio_tiler.io.cogeo import multi_tile

assets = ["b1.tif", "b2.tif", "b3.tif"]
tile, mask = multi_tile(assets, x, y, z, tilesize=256)

print(tile.shape)
> (3, 256, 256)

# Others
metadata = multi_info(assets)
stats = multi_stats(assets, pmin=2, pmax=98, ...)
metadata = multi_metadata(assets, pmin=2, pmax=98, ...)
values = multi_points(assets, lon, lat, ...)
data, mask = multi_part(assets, bbox, ...)
data, mask = multi_preview(assets, ...)
```

## Partial reading on Cloud hosted dataset

Rio-tiler perform partial reading on local or distant dataset, which is why it will perform best on Cloud Optimized GeoTIFF (COG).
It's important to note that **Sentinel-2 scenes hosted on AWS are not in Cloud Optimized format but in JPEG2000**.
When performing partial reading of JPEG2000 dataset GDAL (rasterio backend library) will need to make a lot of **GET requests** and transfer a lot of data.

Ref: [Do you really want people using your data](https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f) blog post.


## Create an AWS Lambda package

The easiest way to make sure the package will work on AWS is to use docker

```dockerfile
FROM lambci/lambda:build-python3.7

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 CFLAGS="--std=c99"

RUN pip3 install rio-tiler --no-binary numpy -t /tmp/python -U

RUN cd /tmp/python && zip -r9q /tmp/package.zip *
```

Ref: https://github.com/vincentsarago/simple-rio-lambda


## Mission Specific tiler
In rio-tiler v2 we choosed to remove the mission specific tilers (Sentinel2, Sentinel1, Landsat8 and CBERS). Those are now in a specific plugin: [rio-tiler-pds](https://github.com/cogeotiff/rio-tiler-pds).

## Plugins
- [rio-tiler-mvt](https://github.com/cogeotiff/rio-tiler-mvt): Create Mapbox Vector Tile from numpy array (tile/mask)
- [rio-tiler-crs](https://github.com/cogeotiff/rio-tiler-crs): Create Map Tiles using other TileMatrixSets
- [rio-viz](https://github.com/developmentseed/rio-viz): Visualize Cloud Optimized GeoTIFF in browser locally

## Implementations
- [CosmiQ/solaris](https://github.com/CosmiQ/solaris)
- [cogeo-tiler](https://github.com/developmentseed/cogeo-tiler)
- [titiler](https://github.com/developmentseed/titiler)


## Contribution & Development

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -e .[dev]
```

**Python3.7 only**

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
$ pre-commit install
```

## License

See [LICENSE.txt](https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE.txt)

## Authors

The rio-tiler project was begun at Mapbox and has been transferred in January 2019.

See [AUTHORS.txt](https://github.com/cogeotiff/rio-tiler/blob/master/AUTHORS.txt) for a listing of individual contributors.

## Changes

See [CHANGES.txt](https://github.com/cogeotiff/rio-tiler/blob/master/CHANGES.txt).

