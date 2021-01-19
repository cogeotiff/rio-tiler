# rio-tiler

<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/88133997-77560f00-cbb1-11ea-874c-a8f1d123a9df.jpg" style="max-width: 800px;" alt="rio-tiler"></a>
</p>
<p align="center">
  <em>Rasterio plugin to read Web Map tiles from raster datasets.</em>
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

`rio-tiler` is a rasterio plugin that aims to ease the creation of [slippy map tiles](https://en.wikipedia.org/wiki/Tiled_web_map) dynamically from any raster source.

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

## Partial reading on cloud-hosted datasets

When the output image size is smaller than the input image size, `rio-tiler`
performs a _partial read_ on the raster source, minimizing the amount of bytes
that must be read. Because of this, performance will be optimal when the source
format permits efficient partial reads. In general, Cloud Optimized GeoTIFF
(COG) sources will provide best performance.

Some non-COG formats are relatively inefficient. For example, older Sentinel 2
scenes on AWS are stored in the JPEG2000 format. This file format requires many
more requests, so it will be both [slower and more
expensive][vincent_s2_jp2_cost] than reading the newer Sentinel 2 source in COG
format because the underlying GDAL library will need to make many more GET
requests.

[vincent_s2_jp2_cost]: https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f

## `rio-tiler` Plugins

#### [`rio-tiler-pds`][rio-tiler-pds]

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds

`rio-tiler` v1 included several helpers for reading popular public datasets (e.g. Sentinel 2, Sentinel 1, Landsat 8, CBERS) from cloud providers. This functionality is now in a [separate plugin][rio-tiler-pds], enabling easier access to more public datasets.

#### [`rio-tiler-mvt`][rio-tiler-mvt]

Create Mapbox Vector Tiles from raster sources

[rio-tiler-mvt]: https://github.com/cogeotiff/rio-tiler-mvt

## `rio-tiler` Implementations

- [rio-viz](https://github.com/developmentseed/rio-viz): Visualize Cloud Optimized GeoTIFF in browser locally
- [titiler](https://github.com/developmentseed/titiler): A lightweight Cloud Optimized GeoTIFF dynamic tile server.
- [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic): Create mosaics of Cloud Optimized GeoTIFF based on mosaicJSON specification.

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/cogeotiff/rio-tiler/blob/master/CONTRIBUTING.md)

## Authors

The `rio-tiler` project was begun at Mapbox and was transferred to the `cogeotiff` Github organization in January 2019.

See [AUTHORS.txt](https://github.com/cogeotiff/rio-tiler/blob/master/AUTHORS.txt) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/cogeotiff/rio-tiler/blob/master/CHANGES.md).

## License

See [LICENSE](https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE)
