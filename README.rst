=========
Rio-tiler
=========

Rasterio plugin to create mercator tiles from raster sources.

.. image:: https://circleci.com/gh/mapbox/rio-tiler.svg?style=svg&circle-token=b78bc1a238c21046a855a9c80b441a8f2f9a4478
   :target: https://circleci.com/gh/mapbox/rio-tiler

.. image:: https://codecov.io/gh/mapbox/rio-tiler/branch/master/graph/badge.svg?token=zuHupC20cG
   :target: https://codecov.io/gh/mapbox/rio-tiler

Additional support is provided for the following satellite missions:

* Sentinel 2
* Landsat 8
* CBERS

Rio-tiler supports Python 2.7 and 3.3-3.6.


Install
=======

You can install rio-tiler using pip

.. code-block:: console

    $ pip install -U pip
    $ pip install rio-tiler

or install from source:

.. code-block:: console

    $ git clone https://github.com/mapbox/rio-tiler.git
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

The :code:`main` module can create mercator tiles from any raster source supported by Rasterio (i.e. local files, http, etc.). The mission specific modules make it easier to extract tiles from AWS S3 buckets (i.e. only a scene ID is required); They can also be used to return metadata.

All of the tiling modules can return the original image bounds.

Usage
=====

Get a Sentinel2 tile and its mask (if any).

.. code-block:: python

   from rio_tiler import sentinel2
   tile, mask = sentinel2.tile('S2A_tile_20170729_19UDP_0', 77, 89, 8)
   tile.shape
   # (3, 256, 256)

Create image from tile

.. code-block:: python

   from rio_tiler.utils import array_to_img
   img = array_to_img(tile, mask=mask) # this returns a pillow image

Convert image into base64 encoded string (PNG or JPEG)

.. code-block:: python

   from rio_tiler.utils import b64_encode_img
   str_img = b64_encode_img(img, 'jpeg')

Get bounds for a Landsat scene (WGS84).

.. code-block:: python

   from rio_tiler import landsat8
   landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')
   # {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
   #  'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

Get metadata of a Landsat scene (i.e. percentinle min and max values, and bounds in WGS84) .

.. code-block:: python

   from rio_tiler import landsat8
   landsat8.metadata('LC08_L1TP_016037_20170813_20170814_01_RT', pmin=5, pmax=95)
   #  {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
   #   'rgbMinMax': {'1': [1245, 5396],
   #    '2': [983, 5384],
   #    '3': [718, 5162],
   #    '4': [470, 5273],
   #    '5': [403, 6440],
   #    '6': [258, 4257],
   #    '7': [151, 2984]},
   #   'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

The primary purpose for calculating minimum and maximum values of an image is to rescale pixel values from their original range (e.g. 0 to 65,535) to the range used by computer screens (i.e. 0 and 255) through a linear transformation. This will make images look good on display.

The Datasets
------------

* Sentinel2_
* Landsat8_
* CBERS_

.. _Sentinel2: http://sentinel-pds.s3-website.eu-central-1.amazonaws.com
.. _Landsat8: https://aws.amazon.com/fr/public-datasets/landsat
.. _CBERS: https://registry.opendata.aws/cbers/

License
-------

See `LICENSE.txt <LICENSE.txt>`__.

Authors
-------

See `AUTHORS.txt <AUTHORS.txt>`__.

Changes
-------

See `CHANGES.txt <CHANGES.txt>`__.
