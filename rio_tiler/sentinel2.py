"""rio_tiler.sentinel2: Sentinel-2 processing."""

from functools import partial
from concurrent import futures

import numpy as np

import mercantile
import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds

SENTINEL_BUCKET = 's3://sentinel-s2-l1c'


def bounds(sceneid):
    """Retrieve image bounds.

    Attributes
    ----------

    sceneid : str
        Sentinel-2 sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.
    """

    scene_params = utils.sentinel_parse_scene_id(sceneid)
    sentinel_address = '{}/{}'.format(SENTINEL_BUCKET, scene_params['key'])

    with rasterio.open('{}/preview.jp2'.format(sentinel_address)) as src:
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
        Sentinel-2 sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.

    Returns
    -------
    out : dict
        dictionary with image bounds and bands histogram cuts.
    """

    scene_params = utils.sentinel_parse_scene_id(sceneid)
    sentinel_address = '{}/{}'.format(SENTINEL_BUCKET, scene_params['key'])

    with rasterio.open('{}/preview.jp2'.format(sentinel_address)) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    info = {'sceneid': sceneid, 'bounds': list(wgs_bounds)}

    bands = ['01', '02', '03', '04', '05', '06', '07', '08', '8A', '09', '10', '11', '12']
    addresses = ['{}/preview/B{}.jp2'.format(sentinel_address, band) for band in bands]
    _min_max_worker = partial(utils.band_min_max_worker, pmin=pmin, pmax=pmax)
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        responses = list(executor.map(_min_max_worker, addresses))
        info['rgbMinMax'] = dict(zip(bands, responses))

    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=('04', '03', '02'), tilesize=256):
    """Create mercator tile from Sentinel-2 data.

    Attributes
    ----------

    sceneid : str
        Sentinel-2 sceneid.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, str, optional (default: ('04', '03', '02'))
        Bands index for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array
    """

    if not isinstance(bands, tuple):
        bands = tuple((bands, ))

    scene_params = utils.sentinel_parse_scene_id(sceneid)
    sentinel_address = '{}/{}'.format(SENTINEL_BUCKET, scene_params['key'])

    sentinel_preview = '{}/preview.jp2'.format(sentinel_address)
    with rasterio.open(sentinel_preview) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds('Tile {}/{}/{} is outside image bounds'.format(
            tile_z, tile_x, tile_y))

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = ['{}/B{}.jp2'.format(sentinel_address, band) for band in bands]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=tilesize, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

    return np.concatenate(data), mask
