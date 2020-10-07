"""rio-tiler: mercator utility functions."""

import math
from typing import Tuple, Union

from rasterio.io import DatasetReader, DatasetWriter
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform, transform_bounds

from . import constants


def _meters_per_pixel(zoom: int, lat: float = 0.0, tilesize: int = 256) -> float:
    """
    Return the pixel resolution for a given mercator tile zoom and lattitude.

    Parameters
    ----------
        zoom: int
            Mercator zoom level
        lat: float, optional
            Latitude in decimal degree (default: 0)
        tilesize: int, optional
            Mercator tile size (default: 256).

    Returns
    -------
        Pixel resolution in meters

    """
    return (math.cos(lat * math.pi / 180.0) * 2 * math.pi * 6378137) / (
        tilesize * 2 ** zoom
    )


def zoom_for_pixelsize(pixel_size: float, max_z: int = 24, tilesize: int = 256) -> int:
    """
    Get mercator zoom level corresponding to a pixel resolution.

    Freely adapted from
    https://github.com/OSGeo/gdal/blob/b0dfc591929ebdbccd8a0557510c5efdb893b852/gdal/swig/python/scripts/gdal2tiles.py#L294

    Parameters
    ----------
        pixel_size: float
            Pixel size
        max_z: int, optional (default: 24)
            Max mercator zoom level allowed
        tilesize: int, optional
            Mercator tile size (default: 256).

    Returns
    -------
        Mercator zoom level corresponding to the pixel resolution

    """
    for z in range(max_z):
        if pixel_size > _meters_per_pixel(z, 0, tilesize=tilesize):
            return max(0, z - 1)  # We don't want to scale up

    return max_z


def get_zooms(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    ensure_global_max_zoom: bool = False,
    tilesize: int = 256,
) -> Tuple[int, int]:
    """
    Calculate raster min/max mercator zoom level.

    Parameters
    ----------
    src_dst: rasterio.io.DatasetReader
        Rasterio io.DatasetReader object
    ensure_global_max_zoom: bool, optional
        Apply latitude correction factor to ensure max_zoom equality for global
        datasets covering different latitudes (default: False).
    tilesize: int, optional
        Mercator tile size (default: 256).

    Returns
    -------
    min_zoom, max_zoom: Tuple
        Min/Max Mercator zoom levels.

    """
    bounds = transform_bounds(
        src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
    )
    center = [(bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2]
    lat = center[1] if ensure_global_max_zoom else 0

    dst_affine, w, h = calculate_default_transform(
        src_dst.crs,
        constants.WEB_MERCATOR_CRS,
        src_dst.width,
        src_dst.height,
        *src_dst.bounds,
    )

    mercator_resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))

    # Correction factor for web-mercator projection latitude scale change
    latitude_correction_factor = math.cos(math.radians(lat))
    adjusted_resolution = mercator_resolution * latitude_correction_factor

    max_zoom = zoom_for_pixelsize(adjusted_resolution, tilesize=tilesize)

    overview_level = get_maximum_overview_level(w, h, minsize=tilesize)
    ovr_resolution = adjusted_resolution * (2 ** overview_level)
    min_zoom = zoom_for_pixelsize(ovr_resolution, tilesize=tilesize)

    return (min_zoom, max_zoom)
