# rio-tiler

<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/88133997-77560f00-cbb1-11ea-874c-a8f1d123a9df.jpg" style="max-width: 800px;" alt="rio-tiler"></a>
</p>
<p align="center">
  <em>Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF.</em>
</p>
<p align="center">
  <a href="https://github.com/cogeotiff/rio-tiler/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/cogeotiff/rio-tiler/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/cogeotiff/rio-tiler" target="_blank">
      <img src="https://codecov.io/gh/cogeotiff/rio-tiler/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/rio-tiler" target="_blank">
      <img src="https://img.shields.io/pypi/v/rio-tiler?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://anaconda.org/conda-forge/rio-tiler" target="_blank">
      <img src="https://img.shields.io/conda/v/conda-forge/rio-tiler.svg" alt="Conda Forge">
  </a>
  <a href="https://pypistats.org/packages/rio-tiler" target="_blank">
      <img src="https://img.shields.io/pypi/dm/rio-tiler.svg" alt="Downloads">
  </a>
  <a href="https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE.txt" target="_blank">
      <img src="https://img.shields.io/github/license/cogeotiff/rio-tiler.svg" alt="Downloads">
  </a>
  <a href="https://mybinder.org/v2/gh/cogeotiff/rio-tiler/master?filepath=docs%2Fexamples%2F" target="_blank" alt="Binder">
      <img src="https://mybinder.org/badge_logo.svg" alt="Binder">
  </a>
</p>

---

**Documentation**: <a href="https://cogeotiff.github.io/rio-tiler/" target="_blank">https://cogeotiff.github.io/rio-tiler/</a>

**Source Code**: <a href="https://github.com/cogeotiff/rio-tiler" target="_blank">https://github.com/cogeotiff/rio-tiler</a>

---

## Install

You can install `rio-tiler` using pip

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

## Overview

`rio-tiler` is a rasterio plugin which aims to ease the creation of [slippy map tile](https://en.wikipedia.org/wiki/Tiled_web_map) dynamically from any raster data.

```python
from typing import Dict, List

from rio_tiler.io import COGReader
from rio_tiler.models import ImageData

with COGReader("my-tif.tif") as cog:
    # get info
    info: Dict = cog.info()

    # get image statistics
    stats: Dict = cog.stats()

    # get metadata (info + image statistics)
    meta: Dict = cog.metadata()

    # Read data for a mercator tile
    img: ImageData = cog.tile(tile_x, tile_y, tile_zoom, tilesize=256)
    assert img.data
    assert img.mask

    # Read part of a data for a given bbox (size is maxed out to 1024)
    img: ImageData = cog.part([minx, miny, maxx, maxy])

    # Read data for a given geojson polygon (size is maxed out to 1024)
    img: ImageData = cog.feature(geojson_feature)

    # Get a preview (size is maxed out to 1024)
    img: ImageData = cog.preview()

    # Get pixel values for a given lon/lat coordinate
    value: List = cog.point(lon, lat)
```

## Partial reading on Cloud hosted dataset

`rio-tiler` perform partial reading on local or distant dataset, which is why it will perform best on Cloud Optimized GeoTIFF (COG).
It's important to note that **Sentinel-2 scenes hosted on AWS are not in Cloud Optimized format but in JPEG2000**.
When performing partial reading of JPEG2000 dataset GDAL (rasterio backend library) will need to make a lot of **GET requests** and transfer a lot of data.

Ref: [Do you really want people using your data](https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f) blog post.

## Plugins
- [rio-tiler-mvt](https://github.com/cogeotiff/rio-tiler-mvt): Create Mapbox Vector Tile from numpy array (tile/mask)

**Mission Specific tiler**

In `rio-tiler` v2 we choosed to remove the mission specific tilers (Sentinel2, Sentinel1, Landsat8 and CBERS). Those are now in a specific plugin: [**rio-tiler-pds**](https://github.com/cogeotiff/rio-tiler-pds).

## Implementations
- [rio-viz](https://github.com/developmentseed/rio-viz): Visualize Cloud Optimized GeoTIFF in browser locally
- [titiler](https://github.com/developmentseed/titiler): A lightweight Cloud Optimized GeoTIFF dynamic tile server.
- [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic): Create mosaics of Cloud Optimized GeoTIFF based on mosaicJSON specification.

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/cogeotiff/rio-tiler/blob/master/CONTRIBUTING.md)

## Authors

The `rio-tiler` project was begun at Mapbox and has been transferred in January 2019.

See [AUTHORS.txt](https://github.com/cogeotiff/rio-tiler/blob/master/AUTHORS.txt) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/cogeotiff/rio-tiler/blob/master/CHANGES.md).

## License

See [LICENSE.txt](https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE.txt)
