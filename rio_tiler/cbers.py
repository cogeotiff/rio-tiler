"""rio_tiler.cbers: cbers processing."""

from functools import partial
from concurrent import futures

import numpy as np

import mercantile
import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds

CBERS_BUCKET = 's3://cbers-pds'


def bounds(sceneid):
    """Retrieve image bounds.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.
    """

    scene_params = utils.cbers_parse_scene_id(sceneid)
    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/{}_BAND{}.tif'.format(cbers_address, sceneid,
                                                 scene_params['reference_band'])) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    info = {'sceneid': sceneid}
    info['bounds'] = list(wgs_bounds)

    return info


def metadata(sceneid, pmin=2, pmax=98):
    """Retrieve image bounds and histogram info.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.

    Returns
    -------
    out : dict
        dictionary with image bounds and bands histogram cuts.
    """

    scene_params = utils.cbers_parse_scene_id(sceneid)
    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/{}_BAND{}.tif'.format(cbers_address, sceneid,
                                                 scene_params['reference_band'])) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    info = {'sceneid': sceneid, 'bounds': list(wgs_bounds)}

    bands = scene_params['bands']
    addresses = ['{}/{}_BAND{}.tif'.format(cbers_address, sceneid, band) for band in bands]
    _min_max_worker = partial(utils.band_min_max_worker, pmin=pmin, pmax=pmax)
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        responses = list(executor.map(_min_max_worker, addresses))
        info['rgbMinMax'] = dict(zip(bands, responses))

    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=None, tilesize=256):
    """Create mercator tile from CBERS data.

    Attributes
    ----------

    sceneid : str
        CBERS sceneid.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, int, optional (default: None)
        Bands index for the RGB combination. If None uses default
        defined for the instrument
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array
    """

    scene_params = utils.cbers_parse_scene_id(sceneid)

    if not bands:
        bands = scene_params['rgb']
    
    if not isinstance(bands, tuple):
        bands = tuple((bands, ))

    cbers_address = '{}/{}'.format(CBERS_BUCKET, scene_params['key'])

    with rasterio.open('{}/{}_BAND{}.tif'.format(cbers_address, sceneid,
                                                 scene_params['reference_band'])) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds('Tile {}/{}/{} is outside image bounds'.format(
            tile_z, tile_x, tile_y))

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = ['{}/{}_BAND{}.tif'.format(cbers_address, sceneid, band) for band in bands]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=tilesize, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

    return np.concatenate(data), mask
