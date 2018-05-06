"""tests rio_tiler.utils"""

import os
import pytest

from mock import patch

import numpy as np

from rio_toa import toa_utils

import rasterio
from rio_tiler import utils
from rio_tiler.errors import (RioTilerError,
                              InvalidFormat,
                              InvalidLandsatSceneId,
                              InvalidSentinelSceneId,
                              InvalidCBERSSceneId)

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


def test_landsat_min_max_worker_tir():
    """
    Should work as expected (read data and return histogram cuts)
    """

    assert utils.landsat_min_max_worker('10',
                                        LANDSAT_PATH,
                                        LANDSAT_METADATA['L1_METADATA_FILE'],
                                        2,
                                        98) == [275, 297]


def test_band_min_max_worker():
    """
    Should work as expected (read data and return histogram cuts)
    """

    address = '{}/preview/B04.jp2'.format(SENTINEL_PATH)
    assert utils.band_min_max_worker(address, pmin=2, pmax=98) == [255, 8626]


def test_tile_read_valid():
    """
    Should work as expected (read landsat band)
    """

    address = '{}_B2.TIF'.format(LANDSAT_PATH)
    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr, mask = utils.tile_read(address, bounds, tilesize)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_list_index():
    """
    Should work as expected
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=(1))
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_int_index():
    """
    Should work as expected
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=1)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_rgb():
    """
    Should work as expected (read rgb)
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=(3, 2, 1))
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_alpha():
    """
    Should work as expected (read rgb)
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    arr, mask = utils.tile_read(S3_PATH, bounds, tilesize, indexes=(3, 2, 1), alpha=3)
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_nodata():
    """
    Should work as expected (read landsat band)
    """

    address = '{}_B2.TIF'.format(LANDSAT_PATH)
    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16
    nodata = 255

    arr, mask = utils.tile_read(address, bounds, tilesize, nodata=nodata)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_nodatalpha():
    """
    Should work as expected (read rgb)
    """

    bounds = (-8844681.416934313, 3757032.814272982,
              -8766409.899970293, 3835304.331237001)
    tilesize = 16

    with pytest.raises(RioTilerError):
        utils.tile_read(S3_PATH, bounds, tilesize, indexes=(3, 2, 1), nodata=0, alpha=3)


def test_tile_read_dataset():
    """
    Should work as expected (read rgb)
    """

    address = '{}_B2.TIF'.format(LANDSAT_PATH)
    bounds = (-8844681.416934313, 3757032.814272982, -8766409.899970293, 3835304.331237001)
    tilesize = 16

    with rasterio.open(address) as src:
        arr, mask = utils.tile_read(src, bounds, tilesize)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)
    assert src.closed


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
        'lat': 'S',
        'num': '0',
        'satellite': 'A',
        'scene': 'S2A_tile_20170323_17SNC_0',
        'sensor': '2',
        'sq': 'NC',
        'utm': '17'}

    assert utils.sentinel_parse_scene_id(scene) == expected_content


def test_sentinel_id_valid_strip():
    """
    Should work as expected (parse sentinel scene id)
    """

    scene = 'S2A_tile_20170323_07SNC_0'
    expected_content = {
        'acquisitionDay': '23',
        'acquisitionMonth': '03',
        'acquisitionYear': '2017',
        'key': 'tiles/7/S/NC/2017/3/23/0',
        'lat': 'S',
        'num': '0',
        'satellite': 'A',
        'scene': 'S2A_tile_20170323_07SNC_0',
        'sensor': '2',
        'sq': 'NC',
        'utm': '07'}

    assert utils.sentinel_parse_scene_id(scene) == expected_content


def test_cbers_id_invalid():
    """
    Should raise an error with invalid sceneid
    """

    scene = 'CBERS_4_MUX_20171121_057_094'
    with pytest.raises(InvalidCBERSSceneId):
        utils.cbers_parse_scene_id(scene)


def test_cbers_id_valid():
    """
    Should work as expected (parse cbers scene id)
    """

    scene = 'CBERS_4_MUX_20171121_057_094_L2'
    expected_content = {
        'acquisitionDay': '21',
        'acquisitionMonth': '11',
        'acquisitionYear': '2017',
        'instrument': 'MUX',
        'key': 'CBERS4/MUX/057/094/CBERS_4_MUX_20171121_057_094_L2',
        'path': '057',
        'processingCorrectionLevel': 'L2',
        'row': '094',
        'mission': '4',
        'scene': 'CBERS_4_MUX_20171121_057_094_L2',
        'reference_band': '6',
        'bands': ['5', '6', '7', '8'],
        'rgb': (7, 6, 5),
        'satellite': 'CBERS'}

    assert utils.cbers_parse_scene_id(scene) == expected_content

    scene = 'CBERS_4_AWFI_20171121_057_094_L2'
    expected_content = {
        'acquisitionDay': '21',
        'acquisitionMonth': '11',
        'acquisitionYear': '2017',
        'instrument': 'AWFI',
        'key': 'CBERS4/AWFI/057/094/CBERS_4_AWFI_20171121_057_094_L2',
        'path': '057',
        'processingCorrectionLevel': 'L2',
        'row': '094',
        'mission': '4',
        'scene': 'CBERS_4_AWFI_20171121_057_094_L2',
        'reference_band': '14',
        'bands': ['13', '14', '15', '16'],
        'rgb': (15, 14, 13),
        'satellite': 'CBERS'}

    assert utils.cbers_parse_scene_id(scene) == expected_content

    scene = 'CBERS_4_PAN10M_20171121_057_094_L2'
    expected_content = {
        'acquisitionDay': '21',
        'acquisitionMonth': '11',
        'acquisitionYear': '2017',
        'instrument': 'PAN10M',
        'key': 'CBERS4/PAN10M/057/094/CBERS_4_PAN10M_20171121_057_094_L2',
        'path': '057',
        'processingCorrectionLevel': 'L2',
        'row': '094',
        'mission': '4',
        'scene': 'CBERS_4_PAN10M_20171121_057_094_L2',
        'reference_band': '4',
        'bands': ['2', '3', '4'],
        'rgb': (3, 4, 2),
        'satellite': 'CBERS'}

    assert utils.cbers_parse_scene_id(scene) == expected_content

    scene = 'CBERS_4_PAN5M_20171121_057_094_L2'
    expected_content = {
        'acquisitionDay': '21',
        'acquisitionMonth': '11',
        'acquisitionYear': '2017',
        'instrument': 'PAN5M',
        'key': 'CBERS4/PAN5M/057/094/CBERS_4_PAN5M_20171121_057_094_L2',
        'path': '057',
        'processingCorrectionLevel': 'L2',
        'row': '094',
        'mission': '4',
        'scene': 'CBERS_4_PAN5M_20171121_057_094_L2',
        'reference_band': '1',
        'bands': ['1'],
        'rgb': (1, 1, 1),
        'satellite': 'CBERS'}

    assert utils.cbers_parse_scene_id(scene) == expected_content


def test_array_to_img_valid():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    assert utils.array_to_img(arr)


def test_array_to_img_valid_mask():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.random.randint(0, 1, size=(512, 512), dtype=np.uint8) * 255
    assert utils.array_to_img(arr, mask=mask)


def test_array_to_img_valid_oneband():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    assert utils.array_to_img(arr)


def test_array_to_img_valid_noband():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)
    assert utils.array_to_img(arr)


def test_array_to_img_cast():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.int16)
    assert utils.array_to_img(arr)


def test_array_to_img_colormap():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    utils.array_to_img(arr, color_map=utils.get_colormap())


def test_array_to_img_bands_colormap():
    """Should raise an error with invalid format
    """
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    with pytest.raises(InvalidFormat):
        utils.array_to_img(arr, color_map=True)


def test_b64_encode_img_valid_jpg():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(4, 512, 512), dtype=np.uint8)
    img = utils.array_to_img(arr)
    assert utils.b64_encode_img(img, 'jpeg')


def test_b64_encode_img_valid_png():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(4, 512, 512), dtype=np.uint8)
    img = utils.array_to_img(arr)
    assert utils.b64_encode_img(img, 'png')

def test_b64_encode_img_valid_webp():
    """Should work as expected
    """
    arr = np.random.randint(0, 255, size=(4, 512, 512), dtype=np.uint8)
    img = utils.array_to_img(arr)
    assert utils.b64_encode_img(img, 'webp')


def test_array_to_img_invalid_format():
    """Should raise an error with invalid format
    """
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    img = utils.array_to_img(arr)
    with pytest.raises(InvalidFormat):
        utils.b64_encode_img(img, 'gif')


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


def test_get_colormap_valid():
    assert len(utils.get_colormap()) == 768  # 3 x256


def test_mapzen_elevation_rgb():
    """
    Should work as expected
    """

    arr = np.random.randint(0, 3000, size=(512, 512))
    assert utils.mapzen_elevation_rgb(arr).shape == (3, 512, 512)


@patch('rio_tiler.landsat8.tile')
def test_expression_ndvi(landsat_tile):
    """
    Should work as expected
    """

    landsat_tile.return_value = [
        np.random.randint(0, 255, size=(2, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255]

    expr = '(b5 - b4) / (b5 + b4)'

    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = 'LC08_L1TP_016037_20170813_20170814_01_RT'
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)
    assert len(landsat_tile.call_args[1].get('bands')) == 2


@patch('rio_tiler.sentinel2.tile')
def test_expression_sentinel2(sentinel2):
    """
    Should work as expected
    """

    sentinel2.return_value = [
        np.random.randint(0, 255, size=(2, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255]

    expr = '(b8A - b12) / (b8A + b12)'

    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = 'S2A_tile_20170323_17SNC_0'
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)
    assert sorted(list(sentinel2.call_args[1].get('bands'))) == ['12', '8A']


@patch('rio_tiler.landsat8.tile')
def test_expression_landsat_rgb(landsat_tile):
    """
    Should work as expected
    """

    landsat_tile.return_value = [
        np.random.randint(0, 255, size=(3, 256, 256), dtype=np.uint8),
        np.random.randint(0, 1, size=(256, 256), dtype=np.uint8) * 255]

    expr = 'b5*0.8, b4*1.1, b3*0.8'
    tile_z = 8
    tile_x = 71
    tile_y = 102

    sceneid = 'LC08_L1TP_016037_20170813_20170814_01_RT'
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (3, 512, 512)
    mask.shape == (512, 512)
    assert len(landsat_tile.call_args[1].get('bands')) == 3


def test_expression_main_ratio():
    """
    Should work as expected
    """

    expr = '(b4 - b3) / (b4 + b3)'
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), 'fixtures')
    sceneid = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif'.format(prefix)
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (1, 256, 256)
    mask.shape == (256, 256)


def test_expression_main_rgb():
    """
    Should work as expected
    """

    expr = 'b1*0.8, b2*1.1, b3*0.8'
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), 'fixtures')
    sceneid = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif'.format(prefix)
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr)
    data.shape == (3, 256, 256)
    mask.shape == (256, 256)


def test_expression_main_kwargs():
    """
    Should work as expected
    """

    expr = '(b4 - b3) / (b4 + b3)'
    tile_z = 19
    tile_x = 109554
    tile_y = 200458

    prefix = os.path.join(os.path.dirname(__file__), 'fixtures')
    sceneid = '{}/my-bucket/hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif'.format(prefix)
    data, mask = utils.expression(sceneid, tile_x, tile_y, tile_z, expr, tilesize=512)
    data.shape == (1, 512, 512)
    mask.shape == (512, 512)
