"""tests rio_tiler.utils"""

import os
import pytest

from mock import patch

import numpy as np

from rio_toa import toa_utils

from rio_tiler import utils
from rio_tiler.errors import (InvalidFormat,
                              InvalidLandsatSceneId,
                              InvalidSentinelSceneId)

SENTINEL_SCENE = 'S2A_tile_20170729_19UDP_0'
SENTINEL_BUCKET = os.path.join(os.path.dirname(__file__),
                               'fixtures', 'sentinel-s2-l1c')
SENTINEL_PATH = os.path.join(SENTINEL_BUCKET, 'tiles/19/U/DP/2017/7/29/0/')

LANDSAT_SCENE_C1 = 'LC08_L1TP_016037_20170813_20170814_01_RT'
LANDSAT_BUCKET = os.path.join(os.path.dirname(__file__),
                              'fixtures', 'landsat-pds')
LANDSAT_PATH = os.path.join(LANDSAT_BUCKET,
                            'c1', 'L8', '016', '037',
                            LANDSAT_SCENE_C1, LANDSAT_SCENE_C1)


S3_KEY = 'hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'
S3_LOCAL = PREFIX = os.path.join(os.path.dirname(__file__),
                                 'fixtures', 'my-bucket')
S3_PATH = os.path.join(S3_LOCAL, S3_KEY)

with open('{}_MTL.txt'.format(LANDSAT_PATH), 'r') as f:
    LANDSAT_METADATA = toa_utils._parse_mtl_txt(f.read())


with open('{}_MTL.txt'.format(LANDSAT_PATH), 'r') as f:
    LANDSAT_METADATA_RAW = f.read().encode('utf-8')


def test_landsat_min_max_worker():
    """
    Should work as expected (read data and return histogram cuts)
    """

    assert utils.landsat_min_max_worker('2',
                                        LANDSAT_PATH,
                                        LANDSAT_METADATA['L1_METADATA_FILE'],
                                        2,
                                        98) == [939, 7025]


def test_sentinel_min_max_worker():
    """
    Should work as expected (read data and return histogram cuts)
    """

    address = '{}/preview/B04.jp2'.format(SENTINEL_PATH)
    assert utils.sentinel_min_max_worker(address, pmin=2, pmax=98) == [255, 8626]


def test_tile_band_worker_valid():
    """
    Should work as expected (read landsat band)
    """

    address = '{}_B2.TIF'.format(LANDSAT_PATH)
    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr = utils.tile_band_worker(address, bounds, tilesize)
    assert arr.shape == (16, 16)


def test_tile_band_worker_list_index():
    """
    Should work as expected
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr = utils.tile_band_worker(S3_PATH, bounds, tilesize, indexes=(1))
    assert arr.shape == (16, 16)


def test_tile_band_worker_int_index():
    """
    Should work as expected
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr = utils.tile_band_worker(S3_PATH, bounds, tilesize, indexes=1)
    assert arr.shape == (16, 16)


def test_tile_band_worker_rgb():
    """
    Should work as expected (read rgb)
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr = utils.tile_band_worker(S3_PATH, bounds, tilesize, indexes=(3, 2, 1))
    assert arr.shape == (3, 16, 16)


def test_tile_band_worker_nodata():
    """
    Should work as expected (read landsat band)
    """

    address = '{}_B2.TIF'.format(LANDSAT_PATH)
    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16
    nodata = 255

    arr = utils.tile_band_worker(address, bounds, tilesize, nodata=nodata)
    assert arr.shape == (16, 16)


def test_linear_rescale_valid():
    """
    Should work as expected (read data band)
    """

    data = np.zeros((1, 1), dtype=np.int16) + 1000
    expected_value = np.zeros((1, 1), dtype=np.int16) + 25.5
    assert utils.linear_rescale(data,
                                in_range=(0, 10000),
                                out_range=(0, 255)) == expected_value


def test_tile_exists_valid():
    """
    Should work as expected (return true)
    """

    tile = '7-36-50'
    tile_z, tile_x, tile_y = map(int, tile.split('-'))
    bounds = [-78.75, 34.30714385628803, -75.93749999999999, 36.59788913307021]
    assert utils.tile_exists(bounds, tile_z, tile_x, tile_y)


def test_landsat_id_pre_invalid():
    """
    Should raise an error with invalid sceneid
    """

    scene = 'L0300342017083LGN00'
    with pytest.raises(InvalidLandsatSceneId):
        utils.landsat_parse_scene_id(scene)


def test_landsat_id_c1_invalid():
    """
    Should raise an error with invalid sceneid
    """

    scene = 'LC08_005004_20170410_20170414_01_T1'
    with pytest.raises(InvalidLandsatSceneId):
        utils.landsat_parse_scene_id(scene)


def test_landsat_id_pre_valid():
    """
    Should work as expected (parse landsat pre sceneid)
    """

    scene = 'LC80300342017083LGN00'
    expected_content = {
        'acquisitionJulianDay': '083',
        'acquisitionYear': '2017',
        'archiveVersion': '00',
        'date': '2017-03-24',
        'groundStationIdentifier': 'LGN',
        'key': 'L8/030/034/LC80300342017083LGN00/LC80300342017083LGN00',
        'path': '030',
        'row': '034',
        'satellite': '8',
        'scene': 'LC80300342017083LGN00',
        'sensor': 'C'}

    assert utils.landsat_parse_scene_id(scene) == expected_content


def test_landsat_id_c1_valid():
    """
    Should work as expected (parse landsat c1 sceneid)
    """

    scene = 'LC08_L1TP_005004_20170410_20170414_01_T1'
    expected_content = {
        'acquisitionDay': '10',
        'acquisitionMonth': '04',
        'acquisitionYear': '2017',
        'collectionCategory': 'T1',
        'collectionNumber': '01',
        'date': '2017-04-10',
        'key': 'c1/L8/005/004/LC08_L1TP_005004_20170410_\
20170414_01_T1/LC08_L1TP_005004_20170410_20170414_01_T1',
        'path': '005',
        'processingCorrectionLevel': 'L1TP',
        'processingDay': '14',
        'processingMonth': '04',
        'processingYear': '2017',
        'row': '004',
        'satellite': '08',
        'scene': 'LC08_L1TP_005004_20170410_20170414_01_T1',
        'sensor': 'C'}

    assert utils.landsat_parse_scene_id(scene) == expected_content


def test_sentinel_id_invalid():
    """
    Should raise an error with invalid sceneid
    """

    scene = 'S2A_tile_20170323_17SNC'
    with pytest.raises(InvalidSentinelSceneId):
        utils.sentinel_parse_scene_id(scene)


def test_sentinel_id_valid():
    """
    Should work as expected (parse sentinel scene id)
    """

    scene = 'S2A_tile_20170323_17SNC_0'
    expected_content = {
        'acquisitionDay': '23',
        'acquisitionMonth': '03',
        'acquisitionYear': '2017',
        'key': 'tiles/17/S/NC/2017/3/23/0',
        'lat': 'NC',
        'num': '0',
        'satellite': 'A',
        'sensor': '2',
        'sq': 'S',
        'utm': '17'}

    assert utils.sentinel_parse_scene_id(scene) == expected_content


def test_array_to_img_valid_png():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    tileformat = 'png'

    assert utils.array_to_img(arr, tileformat)


def test_array_to_img_valid_jpg():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    tileformat = 'jpg'

    assert utils.array_to_img(arr, tileformat)


def test_array_to_img_valid_oneband():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    assert utils.array_to_img(arr)


def test_array_to_img_valid_noband():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)
    assert utils.array_to_img(arr)


def test_array_to_img_invalid_format():
    """
    Should raise an error with invalid format
    """

    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    tileformat = 'gif'
    with pytest.raises(InvalidFormat):
        utils.array_to_img(arr, tileformat)


@patch('rio_tiler.utils.urlopen')
def test_landsat_get_mtl_valid(urlopen):

    urlopen.return_value.read.return_value = LANDSAT_METADATA_RAW

    meta_data = utils.landsat_get_mtl(LANDSAT_SCENE_C1)
    assert meta_data['L1_METADATA_FILE']['METADATA_FILE_INFO']['LANDSAT_SCENE_ID'] == 'LC80160372017225LGN00'


@patch('rio_tiler.utils.urlopen')
def test_landsat_get_mtl_invalid(urlopen):

    urlopen.return_value.read.return_value = {}
    with pytest.raises(Exception):
        utils.landsat_get_mtl(LANDSAT_SCENE_C1)
