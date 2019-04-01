"""rio-tiler: mercator utility functions."""

import math
from rasterio.warp import transform_bounds, calculate_default_transform


def _meters_per_pixel(zoom, lat=0.0, tilesize=256):
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


def zoom_for_pixelsize(pixel_size, max_z=24, tilesize=256):
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

    return max_z - 1


def get_zooms(src_dst, lat=0.0, tilesize=256):
    """
    Calculate raster min/max mercator zoom level.

    Parameters
    ----------
    src_dst: rasterio.io.DatasetReader
        Rasterio io.DatasetReader object
    max_z: int, optional (default: 23)
        Max mercator zoom level allowed
    lat: float, optional
        Center latitude of the dataset. This is only needed in case you want to
        apply latitude correction factor to ensure consitent maximum zoom level
        (default: 0.0).
    tilesize: int, optional
        Mercator tile size (default: 256).

    Returns
    -------
    min_zoom, max_zoom: Tuple
        Min/Max Mercator zoom levels.

    """
    dst_affine, w, h = calculate_default_transform(
        src_dst.crs, "epsg:3857", src_dst.width, src_dst.height, *src_dst.bounds
    )

    native_resolution = max(abs(dst_affine[0]), abs(dst_affine[4]))

    # Correction factor for web-mercator projection latitude distortion
    latitude_correction_factor = math.cos(math.radians(lat))
    corrected_resolution = native_resolution * latitude_correction_factor

    max_zoom = zoom_for_pixelsize(corrected_resolution, tilesize=tilesize)

    ovr_resolution = corrected_resolution * max(h, w) / tilesize
    min_zoom = zoom_for_pixelsize(ovr_resolution, tilesize=tilesize)

    return (min_zoom, max_zoom)


def get_mercator_info(src_dst, latitude_correction=False, tilesize=256):
    """Get dataset Min/Max zoom range."""
    bounds = transform_bounds(
        *[src_dst.crs, "epsg:4326"] + list(src_dst.bounds), densify_pts=21
    )
    center = [(bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2]
    lat = center[1] if latitude_correction else 0

    min_zoom, max_zoom = get_zooms(src_dst, lat=lat, tilesize=tilesize)

    return dict(minzoom=min_zoom, maxzoom=max_zoom)
