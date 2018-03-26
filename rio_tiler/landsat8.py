"""rio_tiler.landsat8: Landsat-8 processing."""

from functools import partial
from concurrent import futures

import numpy as np

import mercantile
from rasterio import Affine
from rasterio import transform

from rio_toa import reflectance, brightness_temp, toa_utils
from rio_pansharpen.worker import pansharpen

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds


LANDSAT_BUCKET = 's3://landsat-pds'


def bounds(sceneid):
    """Retrieve image bounds.

    Attributes
    ----------

    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.

    Returns
    -------
    out : dict
        dictionary with image bounds.
    """

    meta_data = utils.landsat_get_mtl(sceneid).get('L1_METADATA_FILE')

    info = {'sceneid': sceneid}
    info['bounds'] = toa_utils._get_bounds_from_metadata(meta_data['PRODUCT_METADATA'])

    return info


def metadata(sceneid, pmin=2, pmax=98):
    """Retrieve image bounds and histogram info.

    Attributes
    ----------

    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.

    Returns
    -------
    out : dict
        dictionary with image bounds and bands histogram cuts.
    """

    scene_params = utils.landsat_parse_scene_id(sceneid)
    meta_data = utils.landsat_get_mtl(sceneid).get('L1_METADATA_FILE')
    landsat_address = '{}/{}'.format(LANDSAT_BUCKET, scene_params['key'])

    info = {'sceneid': sceneid}
    info['bounds'] = toa_utils._get_bounds_from_metadata(meta_data['PRODUCT_METADATA'])

    bands = ['1', '2', '3', '4', '5', '6', '7', '9', '10', '11']
    _min_max_worker = partial(utils.landsat_min_max_worker,
                              address=landsat_address,
                              metadata=meta_data,
                              pmin=pmin,
                              pmax=pmax)

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        responses = list(executor.map(_min_max_worker, bands))
        info['rgbMinMax'] = dict(zip(bands, responses))

    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=(4, 3, 2), tilesize=256, pan=False):
    """Create mercator tile from Landsat-8 data.

    Attributes
    ----------

    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, int, optional (default: (4, 3, 2))
        Bands index for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.
    pan : boolean, optional (default: False)
        If True, apply pan-sharpening.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array
    """

    if not isinstance(bands, tuple):
        bands = tuple((bands, ))

    scene_params = utils.landsat_parse_scene_id(sceneid)
    meta_data = utils.landsat_get_mtl(sceneid).get('L1_METADATA_FILE')
    landsat_address = '{}/{}'.format(LANDSAT_BUCKET, scene_params['key'])

    wgs_bounds = toa_utils._get_bounds_from_metadata(
        meta_data['PRODUCT_METADATA'])

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            'Tile {}/{}/{} is outside image bounds'.format(
                tile_z, tile_x, tile_y))

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    ms_tile_size = int(tilesize / 2) if pan else tilesize
    addresses = ['{}_B{}.TIF'.format(landsat_address, band) for band in bands]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=ms_tile_size, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        data = np.concatenate(data)
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

        if pan:
            pan_address = '{}_B8.TIF'.format(landsat_address)
            matrix_pan, mask = utils.tile_read(pan_address, tile_bounds, tilesize, nodata=0)

            w, s, e, n = tile_bounds
            pan_transform = transform.from_bounds(w, s, e, n, tilesize, tilesize)
            vis_transform = pan_transform * Affine.scale(2.)
            data = pansharpen(data, vis_transform, matrix_pan, pan_transform,
                              np.int16, 'EPSG:3857', 'EPSG:3857', 0.2,
                              method='Brovey', src_nodata=0)

        sun_elev = meta_data['IMAGE_ATTRIBUTES']['SUN_ELEVATION']

        for bdx, band in enumerate(bands):
            if int(band) > 9:  # TIRS
                multi_rad = meta_data['RADIOMETRIC_RESCALING'].get(
                    'RADIANCE_MULT_BAND_{}'.format(band))

                add_rad = meta_data['RADIOMETRIC_RESCALING'].get(
                    'RADIANCE_ADD_BAND_{}'.format(band))

                k1 = meta_data['TIRS_THERMAL_CONSTANTS'].get(
                    'K1_CONSTANT_BAND_{}'.format(band))

                k2 = meta_data['TIRS_THERMAL_CONSTANTS'].get(
                    'K2_CONSTANT_BAND_{}'.format(band))

                data[bdx] = brightness_temp.brightness_temp(
                    data[bdx], multi_rad, add_rad, k1, k2)

            else:
                multi_reflect = meta_data['RADIOMETRIC_RESCALING'].get(
                    'REFLECTANCE_MULT_BAND_{}'.format(band))

                add_reflect = meta_data['RADIOMETRIC_RESCALING'].get(
                    'REFLECTANCE_ADD_BAND_{}'.format(band))

                data[bdx] = 10000 * reflectance.reflectance(
                    data[bdx], multi_reflect, add_reflect, sun_elev)

        return data, mask
