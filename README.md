# rio-tiler

<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/88133997-77560f00-cbb1-11ea-874c-a8f1d123a9df.jpg" style="max-width: 800px;" alt="rio-tiler"></a>
</p>
<p align="center">
  <em>Rasterio plugin to read web map tiles from raster datasets.</em>
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
$ pip install -U rio-tiler
```

or install from source:

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -U pip
$ pip install -e .
```

## GDAL>=3.0 / PROJ>=6.0 performances issue

`rio-tiler` is often used for dynamic tiling, where we need to perform small tasks involving cropping and reprojecting the input data. Starting with GDAL>=3.0 the project shifted to PROJ>=6, which introduced new ways to store projection metadata (using a SQLite database and/or cloud stored grids). This change introduced a performance regression as mentioned in https://mapserver.gis.umn.edu/id/development/rfc/ms-rfc-126.html:

> using naively the equivalent calls proj_create_crs_to_crs() + proj_trans() would be a major performance killer, since proj_create_crs_to_crs() can take a time in the order of 100 milliseconds in the most complex situations.

We believe the issue reported in [issues/346](https://github.com/cogeotiff/rio-tiler/issues/346) is in fact due to :point_up:.

To get the best performances out of `rio-tiler` we recommend for now to use GDAL **2.4** until a solution can be found in GDAL or in PROJ.

Note: Starting with rasterio 1.2.0, rasterio's wheels are distributed with GDAL 3.2 and thus we recommend using rasterio==1.1.8 if using the default wheels, which include GDAL 2.4.

Links:

- http://rgdal.r-forge.r-project.org/articles/PROJ6_GDAL3.html
- https://mapserver.gis.umn.edu/id/development/rfc/ms-rfc-126.html
- https://github.com/OSGeo/gdal/issues/3470
- https://github.com/OSGeo/gdal/issues/1662

## Overview

`rio-tiler` is a rasterio plugin that aims to ease the creation of [slippy map tiles](https://en.wikipedia.org/wiki/Tiled_web_map) dynamically from any raster source.

```python
from typing import Dict, List

from rio_tiler.io import COGReader
from rio_tiler.models import ImageData, Info, Metadata, ImageStatistics

with COGReader("my-tif.tif") as cog:
    # get info
    info: Info = cog.info()
    assert info.nodata_type
    assert info.band_descriptions

    # get image statistics
    stats: ImageStatistics = cog.stats()
    assert stats.min
    assert stats.max

    # get metadata (info + image statistics)
    meta: Metadata = cog.metadata()
    assert meta.statistics
    assert meta.nodata_type
    assert meta.band_descriptions

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
    values: List = cog.point(lon, lat)
```

## Plugins

#### [**rio-tiler-pds**][rio-tiler-pds]

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds

`rio-tiler` v1 included several helpers for reading popular public datasets (e.g. Sentinel 2, Sentinel 1, Landsat 8, CBERS) from cloud providers. This functionality is now in a [separate plugin][rio-tiler-pds], enabling easier access to more public datasets.

#### [**rio-tiler-mvt**][rio-tiler-mvt]

Create Mapbox Vector Tiles from raster sources

[rio-tiler-mvt]: https://github.com/cogeotiff/rio-tiler-mvt

## Implementations

#### [**rio-viz**][rio-viz]

![](https://user-images.githubusercontent.com/10407788/105772356-0ca2d900-5f30-11eb-85b9-c3da9e12b663.jpg)

[rio-viz]: https://github.com/developmentseed/rio-viz

Visualize Cloud Optimized GeoTIFFs locally in the browser

#### [**titiler**][titiler]

![](https://user-images.githubusercontent.com/10407788/84913491-99c3ac80-b088-11ea-846d-75db9e3ab31c.jpg)

[titiler]: https://github.com/developmentseed/titiler

A lightweight Cloud Optimized GeoTIFF dynamic tile server.

#### [**cogeo-mosaic**][cogeo-mosaic]

![](https://user-images.githubusercontent.com/10407788/73185274-c41dc900-40eb-11ea-8b67-f79c0682c3b0.jpg)

[cogeo-mosaic]: https://github.com/developmentseed/cogeo-mosaic

Create mosaics of Cloud Optimized GeoTIFF based on the [mosaicJSON][mosaicjson_spec] specification.

[mosaicjson_spec]: https://github.com/developmentseed/mosaicjson-spec

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/cogeotiff/rio-tiler/blob/master/CONTRIBUTING.md)

## Authors

The `rio-tiler` project was begun at Mapbox and was transferred to the `cogeotiff` Github organization in January 2019.

See [AUTHORS.txt](https://github.com/cogeotiff/rio-tiler/blob/master/AUTHORS.txt) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/cogeotiff/rio-tiler/blob/master/CHANGES.md).

## License

See [LICENSE](https://github.com/cogeotiff/rio-tiler/blob/master/LICENSE)
