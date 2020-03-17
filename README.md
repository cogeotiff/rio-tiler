# Rio-tiler

Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF dataset.

[![Packaging status](https://badge.fury.io/py/rio-tiler.svg)](https://badge.fury.io/py/rio-tiler)
[![CircleCI](https://circleci.com/gh/cogeotiff/rio-tiler.svg?style=svg)](https://circleci.com/gh/cogeotiff/rio-tiler)
[![codecov](https://codecov.io/gh/cogeotiff/rio-tiler/branch/master/graph/badge.svg?token=zuHupC20cG)](https://codecov.io/gh/cogeotiff/rio-tiler)

Additional support is provided for the following satellite missions hosted on **AWS Public Dataset**:

- [Sentinel2](https://registry.opendata.aws/sentinel-2/) (**requester-pays**) (please read [this](https://github.com/cogeotiff/rio-tiler#Partial-reading-on-Cloud-hosted-dataset))
- [Sentinel1](https://registry.opendata.aws/sentinel-1/) (**requester-pays**)
- [Landsat8](https://aws.amazon.com/fr/public-datasets/landsat)
- [CBERS](https://registry.opendata.aws/cbers/)  (**requester-pays**)

**Starting with version 2.0 rio-tiler only supports Python>=3.**


## Install

You can install rio-tiler using pip

```bash
$ pip install -U pip
$ pip install rio-tiler
```

or install from source:

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -U pip
$ pip install -e .
```

## Overview

Create tiles using one of these rio_tiler `io` submodules: `cogeo`, `sentinel2`, `sentinel1`, `landsat8`, `cbers`.

The `rio_tiler.io.cogeo` module can create mercator tiles from any raster source supported by Rasterio (i.e. local files, http, s3, gcs etc.). The mission specific modules make it easier to extract tiles from AWS S3 buckets (i.e. only a scene ID is required); They can also be used to return metadata.

Each tilling modules have a method to return image metadata (e.g bounds).

## Usage

Read a tile from a file over the internet

```python
from rio_tiler.io import cogeo

tile, mask = cogeo.tile(
  'http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif',
  691559,
  956905,
  21,
  tilesize=256
)
print(tile.shape)
> (3, 256, 256)

print(mask.shape)
> (256, 256)
```

Create image from tile

```python
from rio_tiler.utils import array_to_image

buffer = array_to_image(tile, mask=mask) # this returns a buffer (PNG by default)
```

Use creation options to match `mapnik` default

```python
from rio_tiler.utils import array_to_image
from rio_tiler.profiles import img_profiles

options = img_profiles["webp"]
buffer = array_to_image(tile, mask=mask, img_format="webp", **options)
```

Write image to file

```python
with open("my.png", "wb") as f:
  f.write(buffer)
```

Get a Sentinel2 tile and its nodata mask.

```python
from rio_tiler.io import sentinel2

tile, mask = sentinel2.tile('S2A_L1C_20170729_19UDP_0', 77, 89, 8)
print(tile.shape)
> (3, 256, 256)
```

Get bounds for a Landsat scene (WGS84).

```python
from rio_tiler.io import landsat8

landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')
> {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
>  'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}
```

Get metadata of a Landsat scene (i.e. percentiles (pc) min/max values, histograms, and bounds in WGS84) .

```python
from rio_tiler.io import landsat8

landsat8.metadata('LC08_L1TP_016037_20170813_20170814_01_RT', pmin=5, pmax=95)
{
  'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT',
  'bounds':(-81.30844102941015, 32.105321365706104,  -78.82036599673634, 34.22863519772504),
  'statistics': {
    '1': {
      'pc': [1251.297607421875, 5142.0126953125],
      'min': -1114.7020263671875,
      'max': 11930.634765625,
      'std': 1346.6463388957156,
      'histogram': [
        [1716, 257951, 174296, 36184, 20828, 11783, 6862, 2941, 635, 99],
        [-1114.7020263671875, 189.83164978027344, 1494.3653564453125, 2798.89892578125, 4103.4326171875, 5407.96630859375, 6712.5, 8017.03369140625, 9321.5673828125, 10626.1015625, 11930.634765625]
      ]
    },
    ...
    ...
    '11': {
      'pc': [278.3393859863281, 293.4466247558594],
      'min': 147.27650451660156,
      'max': 297.4621276855469,
      'std': 7.660112832018338,
      'histogram': [
        [207, 201, 204, 271, 350, 944, 1268, 2383, 43085, 453084],
        [147.27650451660156, 162.29507446289062, 177.31362915039062, 192.33218383789062, 207.3507537841797, 222.36932373046875, 237.38787841796875, 252.40643310546875, 267.42498779296875, 282.4435729980469, 297.4621276855469]
      ]
    }
  }
}
```

The primary purpose for calculating minimum and maximum values of an image is to rescale pixel values from their original range (e.g. 0 to 65,535) to the range used by computer screens (i.e. 0 and 255) through a linear transformation.
This will make images look good on display.

#### Working with STAC items 

`rio_tiler.reader` submodule has `multi_*` functions (tile, preview, point, metadata) allowing to fetch and merge info 
from multiple dataset (think about multiple bands stored in separated files).

```python
from typing import Dict 
from rio_tiler import reader

item: Dict = ... # a STAC Items

# Name of assets to read
names = ["red", "green", "blue"]

assets = [item["assets"][name]["href"] for name in names]

tile, mask = reader.multi_tile(assets, x, y, z, tilesize=256)

print(tile.shape)
> (3, 256, 256)
```

## Requester-pays Buckets 

On AWS, `sentinel2`, `sentinel1`, and `cbers` dataset are stored in a `requester-pays` bucket, meaning the cost of GET, LIST requests will be charged to the users. For rio-tiler to work with those buckets, you'll need to set `AWS_REQUEST_PAYER="requester"` in your environement.

## Partial reading on Cloud hosted dataset

Rio-tiler perform partial reading on local or distant dataset, which is why it will perform best on Cloud Optimized GeoTIFF (COG).
It's important to note that **Sentinel-2 scenes hosted on AWS are not in Cloud Optimized format but in JPEG2000**.
When performing partial reading of JPEG2000 dataset GDAL (rasterio backend library) will need to make a lot of **GET requests** and transfer a lot of data.

Ref: [Do you really want people using your data](https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f) blog post.

## Contribution & Development

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/cogeotiff/rio-tiler.git
$ cd rio-tiler
$ pip install -e .[dev]
```

**Python3.6 only**

This repo is set to use `pre-commit` to run *flake8*, *pydocstring* and *black* ("uncompromising Python code formatter") when commiting new code.

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


## Create an AWS Lambda package

The easiest way to make sure the package will work on AWS is to use docker

```dockerfile
FROM lambci/lambda:build-python3.6

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 CFLAGS="--std=c99"

RUN pip3 install rio-tiler --no-binary numpy -t /tmp/python -U

RUN cd /tmp/python && zip -r9q /tmp/package.zip *
```

Ref: https://github.com/vincentsarago/simple-rio-lambda


## Plugins
- [rio-tiler-mosaic](https://github.com/cogeotiff/rio-tiler-mosaic)
- [rio-tiler-mvt](https://github.com/cogeotiff/rio-tiler-mvt)

## Implementations
- [remotepixel-tiler](https://github.com/RemotePixel/remotepixel-tiler)
- [CosmiQ/solaris](https://github.com/CosmiQ/solaris)
- [lambda-tiler](https://github.com/vincentsarago/lambda-tiler)
- [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic)
