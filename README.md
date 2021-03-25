# rio-tiler

<p align="center">
  <img src="https://user-images.githubusercontent.com/10407788/88133997-77560f00-cbb1-11ea-874c-a8f1d123a9df.jpg" style="max-width: 800px;" alt="rio-tiler"></a>
</p>
<p align="center">
  <em>User friendly Rasterio plugin to read raster datasets.</em>
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

## Description

`rio-tiler` was initialy designed to create [slippy map
tiles](https://en.wikipedia.org/wiki/Tiled_web_map) from large raster data
sources and render these tiles dynamically on a web map. With `rio-tiler` v2.0 we added many more helper methods to read
data and metadata from any raster source supported by Rasterio/GDAL.
This includes local files and via HTTP, AWS S3, Google Cloud Storage,
etc.

At the low level, `rio-tiler` is *just* a wrapper around the [rasterio.vrt.WarpedVRT](https://github.com/mapbox/rasterio/blob/5b76d05fb374e64602166d6cd880c38424fad39b/rasterio/vrt.py#L15) class, which can be useful for doing reprojection and/or property overriding (e.g nodata value).

## Features

- Read any dataset supported by GDAL/Rasterio

    ```python
    from rio_tiler.io import COGReader

    with COGReader("my.tif") as image:
        print(image.dataset)  # rasterio opened dataset
        img = image.read()    # similar to rasterio.open("my.tif").read() but returns a rio_tiler.models.ImageData object
    ```

- User friendly `tile`, `part`, `feature`, `point` reading methods

    ```python
    from rio_tiler.io import COGReader

    with COGReader("my.tif") as image:
        img = image.tile(x, y, z)            # read mercator tile z-x-y
        img = image.part(bbox)               # read the data intersecting a bounding box
        img = image.feature(geojson_feature) # read the data intersecting a geojson feature
        img = image.point(lon,lat)           # get pixel values for a lon/lat coordinates
    ```

- Enable property assignement (e.g nodata) on data reading

    ```python
    from rio_tiler.io import COGReader

    with COGReader("my.tif") as image:
        img = image.tile(x, y, z, nodata=-9999) # read mercator tile z-x-y
    ```

- [STAC](https://github.com/radiantearth/stac-spec) support

    ```python
    from rio_tiler.io import STACReader

    with STACReader("item.json") as stac:
        print(stac.assets)  # available asset
        img = stac.tile(x, y, z, assets="asset1", indexes=(1, 2, 3))  # read tile for asset1 and indexes 1,2,3
        img = stac.tile(x, y, z, assets=("asset1", "asset2", "asset3",), indexes=(1,))  # create an image from assets 1,2,3 using their first band
    ```

- [Mosaic](https://cogeotiff.github.io/rio-tiler/mosaic/) (merging or stacking)

    ```python
    from rio_tiler.io import COGReader
    from rio_tiler.mosaic import mosaic_reader

    def reader(file, x, y, z, **kwargs):
        with COGReader("my.tif") as image:
            return image.tile(x, y, z, **kwargs)

    img, assets = mosaic_reader(["image1.tif", "image2.tif"], reader, x, y, z)
    ```

- Native support for multiple TileMatrixSet via [morecantile](https://developmentseed.org/morecantile/)

    ```python
    import morecantile
    from rio_tiler.io import COGReader

    # Use EPSG:4326 (WGS84) grid
    wgs84_grid = morecantile.tms.get("WorldCRS84Quad")
    with COGReader("my.tif", tms=wgs84_grid) as cog:
        img = cog.tile(1, 1, 1)
    ```

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

#### GDAL>=3.0 / PROJ>=6.0 performances issue

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


## Plugins

#### [**rio-tiler-pds**][rio-tiler-pds]

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds

`rio-tiler` v1 included several helpers for reading popular public datasets (e.g. Sentinel 2, Sentinel 1, Landsat 8, CBERS) from cloud providers. This functionality is now in a [separate plugin][rio-tiler-pds], enabling easier access to more public datasets.

#### [**rio-tiler-mvt**][rio-tiler-mvt]

Create Mapbox Vector Tiles from raster sources

[rio-tiler-mvt]: https://github.com/cogeotiff/rio-tiler-mvt

## Implementations

[**rio-viz**][rio-viz]: Visualize Cloud Optimized GeoTIFFs locally in the browser

[**titiler**][titiler]: A lightweight Cloud Optimized GeoTIFF dynamic tile server.

[**cogeo-mosaic**][cogeo-mosaic]: Create mosaics of Cloud Optimized GeoTIFF based on the [mosaicJSON][mosaicjson_spec] specification.

[rio-viz]: https://github.com/developmentseed/rio-viz
[titiler]: https://github.com/developmentseed/titiler
[cogeo-mosaic]: https://github.com/developmentseed/cogeo-mosaic
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
