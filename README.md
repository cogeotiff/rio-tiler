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
      <img src="https://codecov.io/gh/cogeotiff/rio-tiler/branch/main/graph/badge.svg" alt="Coverage">
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
  <a href="https://github.com/cogeotiff/rio-tiler/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/cogeotiff/rio-tiler.svg" alt="Downloads">
  </a>
  <a href="https://mybinder.org/v2/gh/cogeotiff/rio-tiler/main?filepath=docs%2Fexamples%2F" target="_blank" alt="Binder">
      <img src="https://mybinder.org/badge_logo.svg" alt="Binder">
  </a>
</p>

---

**Documentation**: <a href="https://cogeotiff.github.io/rio-tiler/" target="_blank">https://cogeotiff.github.io/rio-tiler/</a>

**Source Code**: <a href="https://github.com/cogeotiff/rio-tiler" target="_blank">https://github.com/cogeotiff/rio-tiler</a>

---

## Description

`rio-tiler` was initially designed to create [slippy map
tiles](https://en.wikipedia.org/wiki/Tiled_web_map) from large raster data
sources and render these tiles dynamically on a web map. Since `rio-tiler` v2.0, we added many more helper methods to read
data and metadata from any raster source supported by Rasterio/GDAL.
This includes local and remote files via HTTP, AWS S3, Google Cloud Storage,
etc.

At the low level, `rio-tiler` is *just* a wrapper around the [rasterio](https://github.com/rasterio/rasterio) and [GDAL](https://github.com/osgeo/gdal) libraries.

## Features

- Read any dataset supported by GDAL/Rasterio

    ```python
    from rio_tiler.io import Reader

    with Reader("my.tif") as image:
        print(image.dataset)  # rasterio opened dataset
        img = image.read()    # similar to rasterio.open("my.tif").read() but returns a rio_tiler.models.ImageData object
    ```

- User friendly `tile`, `part`, `feature`, `point` reading methods

    ```python
    from rio_tiler.io import Reader

    with Reader("my.tif") as image:
        img = image.tile(x, y, z)            # read mercator tile z-x-y
        img = image.part(bbox)               # read the data intersecting a bounding box
        img = image.feature(geojson_feature) # read the data intersecting a geojson feature
        img = image.point(lon,lat)           # get pixel values for a lon/lat coordinates
    ```

- Enable property assignment (e.g nodata) on data reading

    ```python
    from rio_tiler.io import Reader

    with Reader("my.tif") as image:
        img = image.tile(x, y, z, nodata=-9999) # read mercator tile z-x-y
    ```

- [STAC](https://github.com/radiantearth/stac-spec) support

    ```python
    from rio_tiler.io import STACReader

    with STACReader("item.json") as stac:
        print(stac.assets)  # available asset
        img = stac.tile(  # read tile for asset1 and indexes 1,2,3
            x,
            y,
            z,
            assets="asset1",
            indexes=(1, 2, 3),  # same as asset_indexes={"asset1": (1, 2, 3)},
        )

        # Merging data from different assets
        img = stac.tile(  # create an image from assets 1,2,3 using their first band
            x,
            y,
            z,
            assets=("asset1", "asset2", "asset3",),
            asset_indexes={"asset1": 1, "asset2": 1, "asset3": 1},
        )
    ```

- [Xarray](https://xarray.dev) support **(>=4.0)**

    ```python
    import xarray
    from rio_tiler.io import XarrayReader

    ds = xarray.open_dataset(
        "https://pangeo.blob.core.windows.net/pangeo-public/daymet-rio-tiler/na-wgs84.zarr/",
        engine="zarr",
        decode_coords="all",
        consolidated=True,
    )
    da = ds["tmax"]
    with XarrayReader(da) as dst:
        print(dst.info())
        img = dst.tile(1, 1, 2)
    ```
    *Note: The XarrayReader needs optional dependencies to be installed `pip install rio-tiler["xarray"]`.*

- Non-Geo Image support **(>=4.0)**

    ```python
    from rio_tiler.io import ImageReader

    with ImageReader("image.jpeg") as src:
        im = src.tile(0, 0, src.maxzoom)  # read top-left `tile`
        im = src.part((0, 100, 100, 0))  # read top-left 100x100 pixels
        pt = src.point(0, 0)  # read pixel value
    ```

    *Note: `ImageReader` is also compatible with proper geo-referenced raster datasets.*

- [Mosaic](https://cogeotiff.github.io/rio-tiler/mosaic/) (merging or stacking)

    ```python
    from rio_tiler.io import Reader
    from rio_tiler.mosaic import mosaic_reader

    def reader(file, x, y, z, **kwargs):
        with Reader(file) as image:
            return image.tile(x, y, z, **kwargs)

    img, assets = mosaic_reader(["image1.tif", "image2.tif"], reader, x, y, z)
    ```

- Native support for multiple TileMatrixSet via [morecantile](https://developmentseed.org/morecantile/)

    ```python
    import morecantile
    from rio_tiler.io import Reader

    # Use EPSG:4326 (WGS84) grid
    wgs84_grid = morecantile.tms.get("WorldCRS84Quad")
    with Reader("my.tif", tms=wgs84_grid) as src:
        img = src.tile(1, 1, 1)
    ```

## Install

You can install `rio-tiler` using pip

```bash
$ python -m pip install -U pip
$ python -m pip install -U rio-tiler
```

or install from source:

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ python -m pip install -U pip
$ python -m pip install -e .
```

## Plugins

#### [**rio-tiler-pds**][rio-tiler-pds]

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds

`rio-tiler` v1 included several helpers for reading popular public datasets (e.g. Sentinel 2, Sentinel 1, Landsat 8, CBERS) from cloud providers. This functionality is now in a [separate plugin][rio-tiler-pds], enabling easier access to more public datasets.

#### [**rio-tiler-mvt**][rio-tiler-mvt]

Create Mapbox Vector Tiles from raster sources

[rio-tiler-mvt]: https://github.com/cogeotiff/rio-tiler-mvt

## Implementations

[**titiler**][titiler]: A lightweight Cloud Optimized GeoTIFF dynamic tile server.

[**cogeo-mosaic**][cogeo-mosaic]: Create mosaics of Cloud Optimized GeoTIFF based on the [mosaicJSON][mosaicjson_spec] specification.

[titiler]: https://github.com/developmentseed/titiler
[cogeo-mosaic]: https://github.com/developmentseed/cogeo-mosaic
[mosaicjson_spec]: https://github.com/developmentseed/mosaicjson-spec

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/cogeotiff/rio-tiler/blob/main/CONTRIBUTING.md)

## Authors

The `rio-tiler` project was begun at Mapbox and was transferred to the `cogeotiff` Github organization in January 2019.

See [AUTHORS.txt](https://github.com/cogeotiff/rio-tiler/blob/main/AUTHORS.txt) for a listing of individual contributors.

## Changes

See [CHANGES.md](https://github.com/cogeotiff/rio-tiler/blob/main/CHANGES.md).

## License

See [LICENSE](https://github.com/cogeotiff/rio-tiler/blob/main/LICENSE)
