=========
Rio-tiler
=========

Rasterio plugin to serve tiles from AWS S3 hosted files.

.. image:: https://circleci.com/gh/mapbox/rio-tiler.svg?style=svg&circle-token=b78bc1a238c21046a855a9c80b441a8f2f9a4478
   :target: https://circleci.com/gh/mapbox/rio-tiler

.. image:: https://codecov.io/gh/mapbox/rio-tiler/branch/master/graph/badge.svg?token=zuHupC20cG
   :target: https://codecov.io/gh/mapbox/rio-tiler

Get mercator tile from Landsat, sentinel or other AWS hosted rasters.

Rio-tiler supports Python 2.7 and 3.3-3.6.


Install
=======

.. code-block:: console

    $ pip install -U pip
    $ pip install rio-tiler

Or install from source:

.. code-block:: console

    $ git clone https://github.com/mapbox/rio-tiler.git
    $ cd rio-tiler
    $ pip install -U pip
    $ pip install -e .


Or if you want to create an AWS Lambda package using rasterio wheels:

.. code-block:: console

    # On a centos machine
    $ pip install rio-tiler --no-binary numpy -t /tmp/vendored -U
    $ zip -r9q package.zip vendored/*

API Overview
============

rio_tiler.landsat8
------------------

The ``landsat8`` module processes data hosted on the `Landsat 8 AWS Public Dataset <https://aws.amazon.com/fr/public-datasets/landsat/>`_.

- **landsat8.bounds**

    Get WGS84 bounds for a Landsat scene.

    ``Input``:
      - sceneid: Landsat product id (or scene id for scene < 1st May 2017)

    ``Output``:
      - dictionary:
          - bounds: (minX, minY, maxX, maxY) (list)
          - sceneid: scene id (string)

      .. code-block:: python

          >>> from rio_tiler import landsat8
          >>> landsat8.bounds('LC08_L1TP_016037_20170813_20170814_01_RT')
          {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
          'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

- **landsat8.metadata**

    Get WGS84 bounds and cumulative histogram cuts for each bands for a Landsat scene.

    ``Input``:
      - sceneid: Landsat product id (or scene id for scene < 1st May 2017)
      - pmin: Histogram cut minimum value in percent (default: 2)
      - pmax: Histogram cut maximum value in percent (default: 98)

    ``Output``:
      - dictionary:
          - bounds: (minX, minY, maxX, maxY) (list)
          - sceneid: scene id (string)
          - rgbMinMax: Min/Max DN values for the linear rescaling (dictionary)

        .. code-block:: python

          >>> from rio_tiler import landsat8
          >>> landsat8.metadata('LC08_L1TP_016037_20170813_20170814_01_RT', pmin=5, pmax=95)
          {'bounds': [-81.30836, 32.10539, -78.82045, 34.22818],
           'rgbMinMax': {'1': [1245, 5396],
            '2': [983, 5384],
            '3': [718, 5162],
            '4': [470, 5273],
            '5': [403, 6440],
            '6': [258, 4257],
            '7': [151, 2984]},
           'sceneid': 'LC08_L1TP_016037_20170813_20170814_01_RT'}

- **landsat8.tile**

    Return base64 encoded image corresponding to a mercator tile

    ``Input``:
      - sceneid : Landsat product id (or scene id for scene < 1st May 2017)
      - x: Mercator tile X index
      - y: Mercator tile Y index
      - z: Mercator tile ZOOM level
      - rgb: Bands index for the RGB combination (default: (4, 3, 2))
      - tilesize: Output image size (default: 256)
      - pan: If True, apply pan-sharpening (default: False)

    ``Output``:
      - numpy ndarray of the image data

      .. code-block:: python

        >>> from rio_tiler import landsat8
        >>> tile = landsat8.tile('LC08_L1TP_016037_20170813_20170814_01_RT', 71, 102, 8)
        >>> tile.shape
        (3, 256, 256)


rio_tiler.sentinel2
-------------------

The ``sentinel2`` module processes data hosted on the `Sentinel 2 AWS Public Dataset <http://sentinel-pds.s3-website.eu-central-1.amazonaws.com>`_.

- **sentinel2.bounds**

    Get WGS84 bounds for a Landsat scene.

    ``Input``:
      - sceneid: Sentinel scene id (`S2{A|B}_tile_{YYYYMMDD}_{utm_zone}{latitude_band}{grid_square}_{img_number}`)

    ``Output``:
      - dictionary:
          - bounds: (minX, minY, maxX, maxY) (list)
          - sceneid: scene id (string)

    .. code-block:: python

      >>> from rio_tiler import sentinel2
      >>> sentinel2.bounds('S2A_tile_20170729_19UDP_0')
      {'bounds': [-70.36082319774495, 47.75776333620836, -68.8677615795376, 48.75301295078041],
       'sceneid': 'S2A_tile_20170729_19UDP_0'}

- **sentinel2.metadata**

    Get WGS84 bounds and cumulative histogram cuts for each bands for a Sentinel scene.

    ``Input``:
      - sceneid: Sentinel scene id (`S2{A|B}_tile_{YYYYMMDD}_{utm_zone}{latitude_band}{grid_square}_{img_number}`)
      - pmin: Histogram cut minimum value in percent (default: 2)
      - pmax: Histogram cut maximum value in percent (default: 98)

    ``Output``:
      - dictionary:
          - bounds: (minX, minY, maxX, maxY) (list)
          - sceneid: scene id (string)
          - rgbMinMax: Min/Max DN values for the linear rescaling (dictionary)

    .. code-block:: python

      >>> from rio_tiler import sentinel2
      >>> sentinel2.metadata('S2A_tile_20170729_19UDP_0', pmin=5, pmax=95)
      {'sceneid': 'S2A_tile_20170729_19UDP_0',
      'bounds': [-70.36082319774495, 47.75776333620836, -68.8677615795376, 48.75301295078041],
      'rgbMinMax': {
          '01': [1088, 8237],
          '02': [740, 8288],
          '03': [488, 7977],
          '04': [255, 8626],
          '05': [210, 8877],
          '06': [172, 9079],
          '07': [150, 9263],
          '08': [122, 9163],
          '8A': [107, 9360],
          '09': [53, 5926],
          '10': [6, 546],
          '11': [15, 5658],
          '12': [8, 4009]}}

- **sentinel2.tile**

    Return base64 encoded image corresponding to a mercator tile

    ``Input``:
      - sceneid : Sentinel scene id (`S2{A|B}_tile_{YYYYMMDD}_{utm_zone}{latitude_band}{grid_square}_{img_number}`)
      - x: Mercator tile X index
      - y: Mercator tile Y index
      - z: Mercator tile ZOOM level
      - rgb: Bands index for the RGB combination (default: (04, 03, 02))
      - tilesize: Output image size (default: 256)

    ``Output``:
      - numpy ndarray of the image data

    .. code-block:: python

        >>> from rio_tiler import sentinel2
        >>> sentinel2.tile('S2A_tile_20170729_19UDP_0', 77, 89, 8, 'png')
        >>> tile.shape
        (3, 256, 256)


rio_tiler.aws
-------------

The `aws` module can process any raster hosted on AWS S3.

- **aws.bounds**

    Get WGS84 bounds for a scene.

    ``Input``:
      - bucket: AWS S3 bucket name where the raster is stored
      - key: AWS S3 key

    ``Output``:
      - dictionary:
          - bounds: (minX, minY, maxX, maxY) (list)
          - bucket: bucket name
          - key: AWS key

    .. code-block:: python

      >>> from rio_tiler import aws
      >>> aws.bounds('my-bucket', 'data/my-raster.tif')
      {'bounds': [-104.77532797841498, 38.95344940972065, -104.77466477631017, 38.95376633047638],
       'bucket': 'my-bucket'
       'key': 'data/my-raster.tif'}

- **aws.tile**

    Return base64 encoded image corresponding to a mercator tile

    ``Input``:
      - bucket: bucket name
      - key: AWS key
      - x: Mercator tile X index
      - y: Mercator tile Y index
      - z: Mercator tile ZOOM level
      - rgb: Band index to read (default: (1, 2, 3))
      - tilesize: Output image size (default: 256)

    ``Output``:
      - numpy ndarray of the image data

    .. code-block:: python

        >>> from rio_tiler import aws
        >>> aws.tile('my-bucket', 'data/my-raster.tif', 77, 89, 8)
        >>> tile.shape
        (3, 256, 256)


Convert ``tile`` output to image
=================================

rio_tiler.utils.array_to_img
----------------------------

  ``Input``:
    - numpy **nuint8** ndarray
    - mask **nuint8** array

  ``Output``:
    - Pillow Image object


  .. code-block:: python

    >>> from rio_tiler import landsat8
    >>> from rio_tiler.utils import array_to_img, b64_encode_img
    >>> tile, mask = landsat8.tile('LC08_L1TP_016037_20170813_20170814_01_RT', 71, 102, 8)
    >>> # convert the data to an image object
    >>> img = array_to_img(tile, mask=mask) # this returns a pillow image


rio_tiler.utils.b64_encode_img
------------------------------

  ``Input``:
    - img Pillow image
    - tileformat: Image format to return ("jpg" or "png")

  ``Output``:
    - base64 encoded image PNG or JPEG (string)


  .. code-block:: python

    >>> from rio_tiler import landsat8
    >>> from rio_tiler.utils import array_to_img, b64_encode_img
    >>> tile, mask = landsat8.tile('LC08_L1TP_016037_20170813_20170814_01_RT', 71, 102, 8)
    >>> img = array_to_img(tile, mask=mask) # this returns a pillow image
    >>> str_img = b64_encode_img(img, 'jpeg')
    'iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAEAAElEQVR4AQAggN9/AAAAAAA....


License
-------

See `LICENSE.txt <LICENSE.txt>`__.

Authors
-------

See `AUTHORS.txt <AUTHORS.txt>`__.

Changes
-------

See `CHANGES.txt <CHANGES.txt>`__.
