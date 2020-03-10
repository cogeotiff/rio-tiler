"""rio_tiler.io.cogeo: raster processing."""

from typing import Any, Dict, Tuple

import numpy

import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.mercator import get_zooms


def spatial_info(address: str) -> Dict:
    """
    Return COGEO spatial info.

    Attributes
    ----------
    address : str or PathLike object
        A dataset path or URL. Will be opened in "r" mode.

    Returns
    -------
    out : dict.

    """
    with rasterio.open(address) as src_dst:
        minzoom, maxzoom = get_zooms(src_dst)
        bounds = transform_bounds(
            src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
        )
        center = [(bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2, minzoom]

    return dict(
        address=address, bounds=bounds, center=center, minzoom=minzoom, maxzoom=maxzoom
    )


def bounds(address: str) -> Dict:
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
    with rasterio.open(address) as src_dst:
        bounds = transform_bounds(
            src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
        )
    return dict(address=address, bounds=bounds)


def metadata(
    address: str,
    pmin: float = 2.0,
    pmax: float = 98.0,
    hist_options: Dict = {},
    **kwargs: Any,
) -> Dict:
    """
    Return image statistics.

    Attributes
    ----------
        address : str or PathLike object
            A dataset path or URL. Will be opened in "r" mode.
        pmin : int, optional, (default: 2)
            Histogram minimum cut.
        pmax : int, optional, (default: 98)
            Histogram maximum cut.
        hist_options : dict, optional
            Options to forward to numpy.histogram function.
            e.g: {bins=20, range=(0, 1000)}
        kwargs : optional
            These are passed to 'rio_tiler.reader.preview'

    Returns
    -------
        out : dict
            Dictionary with image bounds and bands statistics.

    """
    with rasterio.open(address) as src_dst:
        meta = reader.metadata(
            src_dst, percentiles=(pmin, pmax), hist_options=hist_options, **kwargs
        )

    return dict(address=address, **meta)


def tile(
    address: str,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    tilesize: int = 256,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
    tilesize : int, optional (default: 256)
        Output image size.
    kwargs: dict, optional
        These will be passed to the 'rio_tiler.reader.tile' function.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    with rasterio.open(address) as src_dst:
        return reader.tile(src_dst, tile_x, tile_y, tile_z, tilesize, **kwargs)
