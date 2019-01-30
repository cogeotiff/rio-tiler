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

* Sentinel2_ (please read this_)

.. _Sentinel2: http://sentinel-pds.s3-website.eu-central-1.amazonaws.com .. this: https://github.com/cogeotiff/rio-tiler#Partial-reading-on-Cloud-hosted-dataset

* Landsat8_

.. _Landsat8: https://aws.amazon.com/fr/public-datasets/landsat

* CBERS_

.. _CBERS: https://registry.opendata.aws/cbers/

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

here is how to create an AWS Lambda package on most UNIX machines:

.. code-block:: console

    # On a centos machine
    $ pip install rio-tiler --no-binary numpy -t /tmp/vendored -U
    $ zip -r9q package.zip vendored/*

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

Get metadata of a Landsat scene (i.e. percentinle min and max values, and bounds in WGS84) .

.. code-block:: python

  from rio_tiler import landsat8
  landsat8.metadata('LC08_L1TP_016037_20170813_20170814_01_RT', pmin=5, pmax=95)
  >  {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
  >   'rgbMinMax': {'1': [1245, 5396],
  >    '2': [983, 5384],
  >    '3': [718, 5162],
  >    '4': [470, 5273],
  >    '5': [403, 6440],
  >    '6': [258, 4257],
  >    '7': [151, 2984]},
  >   'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

The primary purpose for calculating minimum and maximum values of an image is to rescale pixel values from their original range (e.g. 0 to 65,535) to the range used by computer screens (i.e. 0 and 255) through a linear transformation.
This will make images look good on display.


Create image from tile

.. code-block:: python

   from rio_tiler.utils import array_to_img
   img = array_to_img(tile, mask=mask) # this returns a pillow image

Convert image into to binary

.. code-block:: python

   from rio_tiler.utils import img_to_buffer
   with open("my.jpg", "wb") as f:
     f.write(img_to_buffer(img, "jpeg", image_options={"quality": 95}))

Partial reading on Cloud hosted dataset
=======================================

Rio-tiler perform partial reading on local or distant dataset, which is why it will perform best on Cloud Optimized GeoTIFF (COG).
It's important to note that **Sentinel-2 scenes hosted on AWS are not in Cloud Optimized format but in JPEG2000**.
When performing partial reading of JPEG2000 dataset GDAL (rasterio backend library) will need to make a lot of **GET requests** and transfer a lot of data.

:warning: AWS Sentinel-2 bucket is in *requester-pays* mode which means that each user will pay for GET/LIST requests and data transfer. While this seems acceptable, using rio-tiler to access JPEG2000 dataset (as sentinel-2) can result in a huge AWS bill.

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
