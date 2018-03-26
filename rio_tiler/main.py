"""rio_tiler.main: raster processing."""

import mercantile
import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds


def bounds(address):
    """
    Retrieve image bounds.

    Attributes
    ----------
    address : str
        file url.

    Returns
    -------
    out : dict
        dictionary with image bounds.

    """
    with rasterio.open(address) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

    return {'url': address, 'bounds': list(wgs_bounds)}


def tile(address, tile_x, tile_y, tile_z, indexes=None, tilesize=256, nodata=None, alpha=None):
    """
    Create mercator tile from any images.

    Attributes
    ----------
    address : str
        file url.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    indexes : tuple, int, optional (default: (1, 2, 3))
        Bands indexes for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.
    nodata: int or float, optional
        Overwrite nodata value for mask creation.
    alpha: int, optional
        Overwrite alpha band index for mask creation.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    with rasterio.open(address) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, 'epsg:4326'] + list(src.bounds), densify_pts=21)

        indexes = indexes if indexes is not None else src.indexes

        if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
            raise TileOutsideBounds(
                'Tile {}/{}/{} is outside image bounds'.format(tile_z, tile_x, tile_y))

        mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
        tile_bounds = mercantile.xy_bounds(mercator_tile)
        return utils.tile_read(src, tile_bounds, tilesize, indexes=indexes,
                               nodata=nodata, alpha=alpha)
