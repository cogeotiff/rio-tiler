"""rio_tiler.utils: utility functions."""

import os
import re
import base64
import logging
import datetime
from io import BytesIO

import numpy as np
import numexpr as ne

import mercantile

import rasterio
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling
from rasterio.io import DatasetReader
from rasterio.plot import reshape_as_image
from rio_toa import reflectance, brightness_temp, toa_utils

from rio_tiler import profiles as TileProfiles
from rio_tiler.errors import (RioTilerError,
                              InvalidFormat,
                              InvalidLandsatSceneId,
                              InvalidSentinelSceneId,
                              InvalidCBERSSceneId)

from PIL import Image

# Python 2/3
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


logger = logging.getLogger(__name__)


def landsat_min_max_worker(band, address, metadata, pmin=2, pmax=98,
                           width=1024, height=1024):
    """Retrieve histogram percentage cut for a Landsat-8 scene.

    Attributes
    ----------

    address : Landsat band AWS address
    band : Landsat band number
    metadata : Landsat metadata
    pmin : Histogram minimum cut (default: 2)
    pmax : Histogram maximum cut (default: 98)
    width : int, optional (default: 1024)
        Pixel width for the decimated read.
    height : int, optional (default: 1024)
        Pixel height for the decimated read.

    Returns
    -------
    out : list, int
        returns a list of the min/max histogram cut values.
    """

    if int(band) > 9:  # TIRS
        multi_rad = metadata['RADIOMETRIC_RESCALING'].get(
            'RADIANCE_MULT_BAND_{}'.format(band))

        add_rad = metadata['RADIOMETRIC_RESCALING'].get(
            'RADIANCE_ADD_BAND_{}'.format(band))

        k1 = metadata['TIRS_THERMAL_CONSTANTS'].get(
            'K1_CONSTANT_BAND_{}'.format(band))

        k2 = metadata['TIRS_THERMAL_CONSTANTS'].get(
            'K2_CONSTANT_BAND_{}'.format(band))

        with rasterio.open('{}_B{}.TIF'.format(address, band)) as src:
            arr = src.read(indexes=1,
                           out_shape=(height, width)).astype(src.profile['dtype'])
            arr = brightness_temp.brightness_temp(arr, multi_rad, add_rad, k1, k2)
    else:
        multi_reflect = metadata['RADIOMETRIC_RESCALING'].get(
            'REFLECTANCE_MULT_BAND_{}'.format(band))
        add_reflect = metadata['RADIOMETRIC_RESCALING'].get(
            'REFLECTANCE_ADD_BAND_{}'.format(band))
        sun_elev = metadata['IMAGE_ATTRIBUTES']['SUN_ELEVATION']

        with rasterio.open('{}_B{}.TIF'.format(address, band)) as src:
            arr = src.read(indexes=1,
                           out_shape=(height, width)).astype(src.profile['dtype'])
            arr = 10000 * reflectance.reflectance(arr, multi_reflect, add_reflect,
                                                  sun_elev, src_nodata=0)

    return np.percentile(arr[arr > 0], (pmin, pmax)).astype(np.int).tolist()


def band_min_max_worker(address, pmin=2, pmax=98, width=1024, height=1024):
    """Retrieve histogram percentage cut for a single image band.

    Attributes
    ----------

    address : Image band URL
    pmin : Histogram minimum cut (default: 2)
    pmax : Histogram maximum cut (default: 98)
    width : int, optional (default: 1024)
        Pixel width for the decimated read.
    height : int, optional (default: 1024)
        Pixel height for the decimated read.

    Returns
    -------
    out : list, int
        returns a list of the min/max histogram cut values.
    """

    with rasterio.open(address) as src:
        arr = src.read(indexes=1,
                       out_shape=(height, width)).astype(src.profile['dtype'])

    return np.percentile(arr[arr > 0], (pmin, pmax)).astype(np.int).tolist()


def tile_read(source, bounds, tilesize, indexes=[1], nodata=None, alpha=None):
    """Read data and mask

    Attributes
    ----------
    source : str or rasterio.io.DatasetReader
        input file path or rasterio.io.DatasetReader object
    bounds : Mercator tile bounds to retrieve
    tilesize : Output image size
    indexes : list of ints or a single int, optional, (default: 1)
        If `indexes` is a list, the result is a 3D array, but is
        a 2D array if it is a band index number.
    nodata: int or float, optional (defaults: None)
    alpha: int, optional (defaults: None)
        Force alphaband if not present in the dataset metadata

    Returns
    -------
    out : array, int
        returns pixel value.
    """
    w, s, e, n = bounds

    if alpha is not None and nodata is not None:
        raise RioTilerError('cannot pass alpha and nodata option')

    if isinstance(indexes, int):
        indexes = [indexes]

    out_shape = (len(indexes), tilesize, tilesize)

    vrt_params = dict(
        dst_crs='EPSG:3857',
        resampling=Resampling.bilinear,
        src_nodata=nodata,
        dst_nodata=nodata)

    if isinstance(source, DatasetReader):
        with WarpedVRT(source, **vrt_params) as vrt:
            window = vrt.window(w, s, e, n, precision=21)
            data = vrt.read(window=window,
                            boundless=True,
                            resampling=Resampling.bilinear,
                            out_shape=out_shape,
                            indexes=indexes)

            if nodata is not None:
                mask = np.all(data != nodata, axis=0).astype(np.uint8) * 255
            elif alpha is not None:
                mask = vrt.read(alpha, window=window,
                                out_shape=(tilesize, tilesize),
                                boundless=True,
                                resampling=Resampling.bilinear)
            else:
                mask = vrt.read_masks(1, window=window,
                                      out_shape=(tilesize, tilesize),
                                      boundless=True,
                                      resampling=Resampling.bilinear)
    else:
        with rasterio.open(source) as src:
            with WarpedVRT(src, **vrt_params) as vrt:
                window = vrt.window(w, s, e, n, precision=21)
                data = vrt.read(window=window,
                                boundless=True,
                                resampling=Resampling.bilinear,
                                out_shape=out_shape,
                                indexes=indexes)

                if nodata is not None:
                    mask = np.all(data != nodata, axis=0).astype(np.uint8) * 255
                elif alpha is not None:
                    mask = vrt.read(alpha, window=window,
                                    out_shape=(tilesize, tilesize),
                                    boundless=True,
                                    resampling=Resampling.bilinear)
                else:
                    mask = vrt.read_masks(1, window=window,
                                          out_shape=(tilesize, tilesize),
                                          boundless=True,
                                          resampling=Resampling.bilinear)

    return data, mask


def linear_rescale(image, in_range=(0, 1), out_range=(1, 255)):
    """Linear rescaling

    Attributes
    ----------

    image : numpy ndarray
        Image array to rescale.
    in_range : list, int, optional, (default: [0,1])
        Image min/max value to rescale.
    out_range : list, int, optional, (default: [1,255])
        output min/max bounds to rescale to.

    Returns
    -------
    out : numpy ndarray
        returns rescaled image array.
    """

    imin, imax = in_range
    omin, omax = out_range
    image = np.clip(image, imin, imax) - imin
    image = image / np.float(imax - imin)
    return image * (omax - omin) + omin


def tile_exists(bounds, tile_z, tile_x, tile_y):
    """Check if a mercatile tile is inside a given bounds

    Attributes
    ----------

    bounds : list
        WGS84 bounds (left, bottom, right, top).
    x : int
        Mercator tile Y index.
    y : int
        Mercator tile Y index.
    z : int
        Mercator tile ZOOM level.

    Returns
    -------
    out : boolean
        if True, the z-x-y mercator tile in inside the bounds.
    """

    mintile = mercantile.tile(bounds[0], bounds[3], tile_z)
    maxtile = mercantile.tile(bounds[2], bounds[1], tile_z)

    return (tile_x <= maxtile.x + 1) \
        and (tile_x >= mintile.x) \
        and (tile_y <= maxtile.y + 1) \
        and (tile_y >= mintile.y)


def landsat_get_mtl(sceneid):
    """Get Landsat-8 MTL metadata

    Attributes
    ----------

    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.

    Returns
    -------
    out : dict
        returns a JSON like object with the metadata.
    """

    try:
        scene_params = landsat_parse_scene_id(sceneid)
        meta_file = 'http://landsat-pds.s3.amazonaws.com/{}_MTL.txt'.format(scene_params['key'])
        metadata = str(urlopen(meta_file).read().decode())
        return toa_utils._parse_mtl_txt(metadata)
    except:
        raise Exception('Could not retrieve {} metadata'.format(sceneid))


def landsat_parse_scene_id(sceneid):
    """Parse Landsat-8 scene id

    Author @perrygeo - http://www.perrygeo.com
    """

    pre_collection = r'(L[COTEM]8\d{6}\d{7}[A-Z]{3}\d{2})'
    collection_1 = r'(L[COTEM]08_L\d{1}[A-Z]{2}_\d{6}_\d{8}_\d{8}_\d{2}_(T1|T2|RT))'
    if not re.match('^{}|{}$'.format(pre_collection, collection_1), sceneid):
        raise InvalidLandsatSceneId('Could not match {}'.format(sceneid))

    precollection_pattern = (
        r'^L'
        r'(?P<sensor>\w{1})'
        r'(?P<satellite>\w{1})'
        r'(?P<path>[0-9]{3})'
        r'(?P<row>[0-9]{3})'
        r'(?P<acquisitionYear>[0-9]{4})'
        r'(?P<acquisitionJulianDay>[0-9]{3})'
        r'(?P<groundStationIdentifier>\w{3})'
        r'(?P<archiveVersion>[0-9]{2})$')

    collection_pattern = (
        r'^L'
        r'(?P<sensor>\w{1})'
        r'(?P<satellite>\w{2})'
        r'_'
        r'(?P<processingCorrectionLevel>\w{4})'
        r'_'
        r'(?P<path>[0-9]{3})'
        r'(?P<row>[0-9]{3})'
        r'_'
        r'(?P<acquisitionYear>[0-9]{4})'
        r'(?P<acquisitionMonth>[0-9]{2})'
        r'(?P<acquisitionDay>[0-9]{2})'
        r'_'
        r'(?P<processingYear>[0-9]{4})'
        r'(?P<processingMonth>[0-9]{2})'
        r'(?P<processingDay>[0-9]{2})'
        r'_'
        r'(?P<collectionNumber>\w{2})'
        r'_'
        r'(?P<collectionCategory>\w{2})$')

    meta = None
    for pattern in [collection_pattern, precollection_pattern]:
        match = re.match(pattern, sceneid, re.IGNORECASE)
        if match:
            meta = match.groupdict()
            break

    if meta.get('acquisitionJulianDay'):
        date = datetime.datetime(int(meta['acquisitionYear']), 1, 1) \
            + datetime.timedelta(int(meta['acquisitionJulianDay']) - 1)

        meta['date'] = date.strftime('%Y-%m-%d')
    else:
        meta['date'] = '{}-{}-{}'.format(
            meta['acquisitionYear'], meta['acquisitionMonth'],
            meta['acquisitionDay'])

    collection = meta.get('collectionNumber', '')
    if collection != '':
        collection = 'c{}'.format(int(collection))

    meta['key'] = os.path.join(collection, 'L8', meta['path'], meta['row'],
                               sceneid, sceneid)

    meta['scene'] = sceneid

    return meta


def sentinel_parse_scene_id(sceneid):
    """Parse Sentinel-2 scene id"""

    if not re.match('^S2[AB]_tile_[0-9]{8}_[0-9]{2}[A-Z]{3}_[0-9]$', sceneid):
        raise InvalidSentinelSceneId('Could not match {}'.format(sceneid))

    sentinel_pattern = (
        r'^S'
        r'(?P<sensor>\w{1})'
        r'(?P<satellite>[AB]{1})'
        r'_tile_'
        r'(?P<acquisitionYear>[0-9]{4})'
        r'(?P<acquisitionMonth>[0-9]{2})'
        r'(?P<acquisitionDay>[0-9]{2})'
        r'_'
        r'(?P<utm>[0-9]{2})'
        r'(?P<lat>\w{1})'
        r'(?P<sq>\w{2})'
        r'_'
        r'(?P<num>[0-9]{1})$')

    meta = None
    match = re.match(sentinel_pattern, sceneid, re.IGNORECASE)
    if match:
        meta = match.groupdict()

    utm_zone = meta['utm'].lstrip("0")
    grid_square = meta['sq']
    latitude_band = meta['lat']
    year = meta['acquisitionYear']
    month = meta['acquisitionMonth'].lstrip("0")
    day = meta['acquisitionDay'].lstrip("0")
    img_num = meta['num']

    meta['key'] = 'tiles/{}/{}/{}/{}/{}/{}/{}'.format(
        utm_zone, latitude_band, grid_square, year, month, day, img_num)

    meta['scene'] = sceneid

    return meta


def cbers_parse_scene_id(sceneid):
    """Parse CBERS scene id"""

    if not re.match('^CBERS_4_\w+_[0-9]{8}_[0-9]{3}_[0-9]{3}_L[0-9]$', sceneid):
        raise InvalidCBERSSceneId('Could not match {}'.format(sceneid))

    cbers_pattern = (
        r'(?P<satellite>\w+)_'
        r'(?P<mission>[0-9]{1})'
        r'_'
        r'(?P<instrument>\w+)'
        r'_'
        r'(?P<acquisitionYear>[0-9]{4})'
        r'(?P<acquisitionMonth>[0-9]{2})'
        r'(?P<acquisitionDay>[0-9]{2})'
        r'_'
        r'(?P<path>[0-9]{3})'
        r'_'
        r'(?P<row>[0-9]{3})'
        r'_'
        r'(?P<processingCorrectionLevel>L[0-9]{1})$')

    meta = None
    match = re.match(cbers_pattern, sceneid, re.IGNORECASE)
    if match:
        meta = match.groupdict()

    path = meta['path']
    row = meta['row']
    instrument = meta['instrument']
    meta['key'] = 'CBERS4/{}/{}/{}/{}'.format(instrument, path, row, sceneid)

    meta['scene'] = sceneid

    instrument_params = {
        'MUX': {
            'reference_band':'6',
            'bands': ['5', '6', '7', '8'],
            'rgb': (7, 6, 5)
        },
        'AWFI': {
            'reference_band': '14',
            'bands': ['13', '14', '15', '16'],
            'rgb': (15, 14, 13)
        },
        'PAN10M': {
            'reference_band': '4',
            'bands': ['2', '3', '4'],
            'rgb': (3, 4, 2)
        },
        'PAN5M': {
            'reference_band': '1',
            'bands': ['1'],
            'rgb': (1, 1, 1)
        }
    }
    meta['reference_band'] = instrument_params[instrument]['reference_band']
    meta['bands'] = instrument_params[instrument]['bands']
    meta['rgb'] = instrument_params[instrument]['rgb']
    
    return meta


def array_to_img(arr, mask=None, color_map=None):
    """Convert an array to an base64 encoded img

    Attributes
    ----------
    arr : numpy ndarray
        Image array to encode.
    Mask: numpy ndarray
        Mask
    color_map: numpy array
        ColorMap array (see: utils.get_colormap)

    Returns
    -------
    img : object
        Pillow image
    """
    if arr.dtype != np.uint8:
        logger.error('Data casted to UINT8')
        arr = arr.astype(np.uint8)

    if len(arr.shape) >= 3:
        arr = reshape_as_image(arr)
        arr = arr.squeeze()

    if len(arr.shape) != 2 and color_map:
        raise InvalidFormat('Cannot apply colormap on a multiband image')

    mode = 'L' if len(arr.shape) == 2 else 'RGB'

    img = Image.fromarray(arr, mode=mode)
    if color_map:
        img.putpalette(color_map)

    if mask is not None:
        mask_img = Image.fromarray(mask.astype(np.uint8))
        img.putalpha(mask_img)

    return img


def b64_encode_img(img, tileformat):
    """Convert a Pillow image to an base64 encoded string
    Attributes
    ----------
    img : object
        Pillow image
    tileformat : str
        Image format to return (Accepted: "jpg" or "png")

    Returns
    -------
    out : str
        base64 encoded image.
    """
    params = TileProfiles.get(tileformat)

    if tileformat == 'jpeg':
        img = img.convert('RGB')

    sio = BytesIO()
    img.save(sio, tileformat.upper(), **params)
    sio.seek(0)
    return base64.b64encode(sio.getvalue()).decode()


def get_colormap(name='cfastie'):
    """Read color map file

    Attributes
    ----------
    name : str
        colormap name (default: cfastie)

    Returns
    -------
    colormap : list
        Color map array in a Pillow friendly format
        more info: http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#PIL.Image.Image.putpalette
    """
    cmap_file = os.path.join(os.path.dirname(__file__), 'cmap', '{0}.txt'.format(name))
    with open(cmap_file) as cmap:
        lines = cmap.read().splitlines()
        colormap = [list(map(int, line.split())) for line in lines if not line.startswith('#')][1:]

    return list(np.array(colormap).flatten())


def mapzen_elevation_rgb(arr):
    """Encode elevation value to RGB values compatible with Mapzen tangram

    Attributes
    ----------
    arr : numpy ndarray
        Image array to encode.

    Returns
    -------
    out : numpy ndarray
        RGB array (3, h, w)
    """
    arr = np.clip(arr + 32768.0, 0.0, 65535.0)
    r = (arr / 256)
    g = (arr % 256)
    b = ((arr * 256) % 256)
    return np.stack([r, g, b]).astype(np.uint8)


def expression(sceneid, tile_x, tile_y, tile_z, expr, **kwargs):
    """
    """
    bands_names = tuple(set(re.findall(r'b(?P<bands>[0-9A]{1,2})', expr)))
    rgb = expr.split(',')

    if sceneid.startswith('L'):
        from rio_tiler.landsat8 import tile
        arr, mask = tile(sceneid,  tile_x, tile_y, tile_z, bands=bands_names, **kwargs)
    elif sceneid.startswith('S2'):
        from rio_tiler.sentinel2 import tile
        arr, mask = tile(sceneid,  tile_x, tile_y, tile_z, bands=bands_names, **kwargs)
    elif sceneid.startswith('CBERS'):
        from rio_tiler.cbers import tile
        arr, mask = tile(sceneid,  tile_x, tile_y, tile_z, bands=bands_names, **kwargs)
    else:
        from rio_tiler.main import tile
        bands = tuple(map(int, bands_names))
        arr, mask = tile(sceneid,  tile_x, tile_y, tile_z, indexes=bands, **kwargs)

    ctx = {}
    for bdx, b in enumerate(bands_names):
        ctx['b{}'.format(b)] = arr[bdx]

    return np.array([np.nan_to_num(ne.evaluate(bloc.strip(), local_dict=ctx)) for bloc in rgb]), mask
