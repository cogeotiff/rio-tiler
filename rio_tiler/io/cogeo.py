"""rio_tiler.io.cogeo: raster processing."""

from typing import Any, Dict, Tuple

import numpy

import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.utils import has_alpha_band, has_mask_band
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


def info(address: str) -> Dict:
    """
    Return simple metadata about the file.

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

        def _get_descr(ix):
            """Return band description."""
            name = src_dst.descriptions[ix - 1]
            if not name:
                name = "band{}".format(ix)
            return name

        band_descriptions = [(ix, _get_descr(ix)) for ix in src_dst.indexes]
        tags = [(ix, src_dst.tags(ix)) for ix in src_dst.indexes]

        other_meta = dict()
        if src_dst.scales[0] and src_dst.offsets[0]:
            other_meta.update(dict(scale=src_dst.scales[0]))
            other_meta.update(dict(offset=src_dst.offsets[0]))

        if has_alpha_band(src_dst):
            nodata_type = "Alpha"
        elif has_mask_band(src_dst):
            nodata_type = "Mask"
        elif src_dst.nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        try:
            cmap = src_dst.colormap(1)
            other_meta.update(dict(colormap=cmap))
        except ValueError:
            pass

        return dict(
            address=address,
            bounds=bounds,
            center=center,
            minzoom=minzoom,
            maxzoom=maxzoom,
            band_metadata=tags,
            band_descriptions=band_descriptions,
            dtype=src_dst.meta["dtype"],
            colorinterp=[src_dst.colorinterp[ix - 1].name for ix in src_dst.indexes],
            nodata_type=nodata_type,
            **other_meta,
        )


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
