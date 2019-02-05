=========
Rio-tiler
=========

Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF dataset.

.. image:: https://badge.fury.io/py/rio-tiler.svg
    :target: https://badge.fury.io/py/rio-tiler

.. image:: https://circleci.com/gh/cogeotiff/rio-tiler.svg?style=svg&circle-token=b78bc1a238c21046a855a9c80b441a8f2f9a4478
   :target: https://circleci.com/gh/cogeotiff/rio-tiler

.. image:: https://codecov.io/gh/cogeotiff/rio-tiler/branch/master/graph/badge.svg?token=zuHupC20cG
   :target: https://codecov.io/gh/cogeotiff/rio-tiler

Additional support is provided for the following satellite missions hosted on **AWS Public Dataset**:

* `Sentinel2 <http://sentinel-pds.s3-website.eu-central-1.amazonaws.com>`__ (please read `this <https://github.com/cogeotiff/rio-tiler#Partial-reading-on-Cloud-hosted-dataset>`__)

* `Landsat8 <https://aws.amazon.com/fr/public-datasets/landsat>`__

* `CBERS <https://registry.opendata.aws/cbers/>`__

Rio-tiler supports Python 2.7 and 3.3-3.7.


Install
=======

You can install rio-tiler using pip

.. code-block:: console

    $ pip install -U pip
    $ pip install rio-tiler

or install from source:

.. code-block:: console

    $ git clone https://github.com/cogeotiff/rio-tiler.git
    $ cd rio-tiler
    $ pip install -U pip
    $ pip install -e .

Overview
========

Create tiles using one of these rio_tiler modules: :code:`main`, :code:`sentinel2`, :code:`landsat8`, :code:`cbers`.

The :code:`main` module can create mercator tiles from any raster source supported by Rasterio (i.e. local files, http, s3, gcs etc.). The mission specific modules make it easier to extract tiles from AWS S3 buckets (i.e. only a scene ID is required); They can also be used to return metadata.

Each tilling modules have a method to return image metadata (e.g bounds).

Usage
=====

Read a tile from a file over the internet

.. code-block:: python

   from rio_tiler import main
   tile, mask = main.tile(
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

Create image from tile

.. code-block:: python

  from rio_tiler.utils import array_to_image
  buffer = array_to_img(tile, mask=mask) # this returns a buffer (PNG by default)


Use creation options to match `mapnik` default

.. code-block:: python

  from rio_tiler.utils import array_to_image
  from rio_tiler.profiles import img_profiles
  options = img_profiles["webp"]

  buffer = array_to_img(tile, mask=mask, img_format="webp", **options)

Write image to file

.. code-block:: python

  with open("my.png", "wb") as f:
    f.write(buffer)


Get a Sentinel2 tile and its nodata mask.

.. code-block:: python

   from rio_tiler import sentinel2
   tile, mask = sentinel2.tile('S2A_tile_20170729_19UDP_0', 77, 89, 8)
   print(tile.shape)
   > (3, 256, 256)


Get bounds for a Landsat scene (WGS84).

.. code-block:: python

  from rio_tiler import landsat8
  landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')
  > {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
  >  'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

Get metadata of a Landsat scene (i.e. percentiles (pc) min/max values, histograms, and bounds in WGS84) .

.. code-block:: python

  from rio_tiler import landsat8
  landsat8.metadata('LC08_L1TP_016037_20170813_20170814_01_RT', pmin=5, pmax=95)
  {
    'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT',
    'bounds': {
      'value': (-81.30844102941015, 32.105321365706104,  -78.82036599673634, 34.22863519772504),
      'crs': '+init=EPSG:4326'
    },
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


The primary purpose for calculating minimum and maximum values of an image is to rescale pixel values from their original range (e.g. 0 to 65,535) to the range used by computer screens (i.e. 0 and 255) through a linear transformation.
This will make images look good on display.


Partial reading on Cloud hosted dataset
=======================================

Rio-tiler perform partial reading on local or distant dataset, which is why it will perform best on Cloud Optimized GeoTIFF (COG).
It's important to note that **Sentinel-2 scenes hosted on AWS are not in Cloud Optimized format but in JPEG2000**.
When performing partial reading of JPEG2000 dataset GDAL (rasterio backend library) will need to make a lot of **GET requests** and transfer a lot of data.

**warning**
AWS Sentinel-2 bucket is in *requester-pays* mode which means that each user will pay for GET/LIST requests and data transfer. While this seems acceptable, using rio-tiler to access JPEG2000 dataset (as sentinel-2) can result in a huge AWS bill.

ref: https://medium.com/@_VincentS_/do-you-really-want-people-using-your-data-ec94cd94dc3f

Contribution & Development
==========================

Issues and pull requests are more than welcome.

**dev install**

.. code-block:: console

 $ git clone https://github.com/cogeotiff/rio-tiler.git
 $ cd rio-tiler
 $ pip install -e .[dev]

**Python3.6 only**

This repo is set to use `pre-commit` to run *flake8*, *pydocstring* and *black* ("uncompromising Python code formatter") when commiting new code.

.. code-block:: console

 $ pre-commit install

License
=======

See `LICENSE.txt <LICENSE.txt>`__.

Authors
=======

The rio-tiler project was begun at Mapbox and has been transferred in January 2019.

See `AUTHORS.txt <AUTHORS.txt>`__ for a listing of individual contributors.

Changes
=======

See `CHANGES.txt <CHANGES.txt>`__.


Create an AWS Lambda package
============================

The easiest way to make sure the package will work on AWS is to use docker

.. code-block:: console

    FROM lambci/lambda:build-python3.6
    ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
    RUN pip3 install rio-tiler --no-binary numpy -t /tmp/python -U
    RUN cd /tmp/python && zip -r9q /tmp/package.zip *


Ref: https://github.com/vincentsarago/simple-rio-lambda
