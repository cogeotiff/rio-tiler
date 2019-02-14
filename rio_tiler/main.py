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
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    return {"url": address, "bounds": list(wgs_bounds)}


def metadata(address, pmin=2, pmax=98, **kwargs):
    """
    Return image bounds and band statistics.

    Attributes
    ----------
    address : str or PathLike object
        A dataset path or URL. Will be opened in "r" mode.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.
    kwargs : optional
        These are passed to 'rio_tiler.utils.raster_get_stats'
        e.g: overview_level=2, dst_crs='epsg:4326'

    Returns
    -------
    out : dict
        Dictionary with image bounds and bands statistics.

    """
    info = {"address": address}
    info.update(utils.raster_get_stats(address, percentiles=(pmin, pmax), **kwargs))
    return info


def tile(address, tile_x, tile_y, tile_z, indexes=None, tilesize=256, nodata=None):
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

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    with rasterio.open(address) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

        indexes = indexes if indexes is not None else src.indexes
        nodata = nodata if nodata is not None else src.nodata

        if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
            raise TileOutsideBounds(
                "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
            )

        mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
        tile_bounds = mercantile.xy_bounds(mercator_tile)
        return utils.tile_read(
            src, tile_bounds, tilesize, indexes=indexes, nodata=nodata
        )
