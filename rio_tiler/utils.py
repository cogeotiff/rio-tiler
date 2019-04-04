"""rio_tiler.utils: utility functions."""

import os
import re
import math
import logging
import warnings

import numpy as np
import numexpr as ne

import mercantile

import rasterio
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling, MaskFlags, ColorInterp
from rasterio.io import DatasetReader, MemoryFile
from rasterio import transform
from rasterio.warp import calculate_default_transform, transform_bounds

from rio_tiler.mercator import get_zooms

from rio_tiler.errors import NoOverviewWarning

logger = logging.getLogger(__name__)


def _chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


def _stats(arr, percentiles=(2, 98), **kwargs):
    """Calculate array statistics."""
    sample, edges = np.histogram(arr[~arr.mask], **kwargs)
    return {
        "pc": np.percentile(arr[~arr.mask], percentiles).astype(arr.dtype).tolist(),
        "min": arr.min().item(),
        "max": arr.max().item(),
        "std": arr.std().item(),
        "histogram": [sample.tolist(), edges.tolist()],
    }


def raster_get_stats(
    src_path,
    indexes=None,
    nodata=None,
    overview_level=None,
    max_size=1024,
    percentiles=(2, 98),
    dst_crs=CRS({"init": "EPSG:4326"}),
    histogram_bins=10,
):
    """
    Retrieve dataset statistics.

    Attributes
    ----------
    src_path : str or PathLike object
        A dataset path or URL. Will be opened in "r" mode.
    indexes : tuple, list, int, optional
        Dataset band indexes.
    nodata, int, optional
        Custom nodata value if not preset in dataset.
    overview_level : int, optional
        Overview (decimation) level to fetch.
    max_size: int, optional
        Maximum size of dataset to retrieve
        (will be used to calculate the overview level to fetch).
    percentiles : tulple, optional
        Percentile or sequence of percentiles to compute,
        which must be between 0 and 100 inclusive (default: (2, 98)).
    dst_crs: CRS or dict
        Target coordinate reference system (default: EPSG:4326).
    histogram_bins: int, optional
        Defines the number of equal-width histogram bins (default: 10).

    Returns
    -------
    out : dict
        bounds, mercator zoom range, band descriptions
        and band statistics: (percentiles), min, max, stdev, histogram

        e.g.
        {
            'bounds': {
                'value': (145.72265625, 14.853515625, 145.810546875, 14.94140625),
                'crs': '+init=EPSG:4326'
            },
            'minzoom': 8,
            'maxzoom': 12,
            'band_descriptions': [(1, 'red'), (2, 'green'), (3, 'blue'), (4, 'nir')]
            'statistics': {
                1: {
                    'pc': [38, 147],
                    'min': 20,
                    'max': 180,
                    'std': 28.123562304138662,
                    'histogram': [
                        [1625, 219241, 28344, 15808, 12325, 10687, 8535, 7348, 4656, 1208],
                        [20.0, 36.0, 52.0, 68.0, 84.0, 100.0, 116.0, 132.0, 148.0, 164.0, 180.0]
                    ]
                }
                ...
                3: {...}
                4: {...}
            }
        }
    """
    if isinstance(indexes, int):
        indexes = [indexes]
    elif isinstance(indexes, tuple):
        indexes = list(indexes)

    with rasterio.open(src_path) as src_dst:
        levels = src_dst.overviews(1)
        width = src_dst.width
        height = src_dst.height
        indexes = indexes if indexes else src_dst.indexes
        nodata = nodata if nodata is not None else src_dst.nodata
        bounds = transform_bounds(
            *[src_dst.crs, dst_crs] + list(src_dst.bounds), densify_pts=21
        )

        minzoom, maxzoom = get_zooms(src_dst)

        def _get_descr(ix):
            """Return band description."""
            name = src_dst.descriptions[ix - 1]
            if not name:
                name = "band{}".format(ix)
            return name

        band_descriptions = [(ix, _get_descr(ix)) for ix in indexes]

        if len(levels):
            if overview_level:
                decim = levels[overview_level]
            else:
                # determine which zoom level to read
                for ii, decim in enumerate(levels):
                    if max(width // decim, height // decim) < max_size:
                        break
        else:
            decim = 1
            warnings.warn(
                "Dataset has no overviews, reading the full dataset", NoOverviewWarning
            )

        out_shape = (len(indexes), height // decim, width // decim)

        vrt_params = dict(add_alpha=True, resampling=Resampling.bilinear)
        if has_alpha_band(src_dst):
            vrt_params.update(dict(add_alpha=False))

        if nodata is not None:
            vrt_params.update(dict(nodata=nodata, add_alpha=False, src_nodata=nodata))

        with WarpedVRT(src_dst, **vrt_params) as vrt:
            arr = vrt.read(out_shape=out_shape, indexes=indexes, masked=True)
            stats = {
                indexes[b]: _stats(arr[b], percentiles=percentiles, bins=histogram_bins)
                for b in range(arr.shape[0])
                if vrt.colorinterp[b] != ColorInterp.alpha
            }

    return {
        "bounds": {
            "value": bounds,
            "crs": dst_crs.to_string() if isinstance(dst_crs, CRS) else dst_crs,
        },
        "minzoom": minzoom,
        "maxzoom": maxzoom,
        "band_descriptions": band_descriptions,
        "statistics": stats,
    }


def get_vrt_transform(src_dst, bounds, bounds_crs="epsg:3857"):
    """
    Calculate VRT transform.

    Attributes
    ----------
    src_dst : rasterio.io.DatasetReader
        Rasterio io.DatasetReader object
    bounds : list
        Bounds (left, bottom, right, top)
    bounds_crs : str
        Coordinate reference system string (default "epsg:3857")

    Returns
    -------
    vrt_transform: Affine
        Output affine transformation matrix
    vrt_width, vrt_height: int
        Output dimensions

    """
    dst_transform, _, _ = calculate_default_transform(
        src_dst.crs, bounds_crs, src_dst.width, src_dst.height, *src_dst.bounds
    )
    w, s, e, n = bounds
    vrt_width = math.ceil((e - w) / dst_transform.a)
    vrt_height = math.ceil((s - n) / dst_transform.e)

    vrt_transform = transform.from_bounds(w, s, e, n, vrt_width, vrt_height)

    return vrt_transform, vrt_width, vrt_height


def has_alpha_band(src_dst):
    """Check for alpha band or mask in source."""
    if (
        any([MaskFlags.alpha in flags for flags in src_dst.mask_flag_enums])
        or ColorInterp.alpha in src_dst.colorinterp
    ):
        return True
    return False


def _tile_read(
    src_dst, bounds, tilesize, indexes=None, nodata=None, resampling_method="bilinear"
):
    """
    Read data and mask.

    Attributes
    ----------
    src_dst : rasterio.io.DatasetReader
        rasterio.io.DatasetReader object
    bounds : list
        Mercator tile bounds (left, bottom, right, top)
    tilesize : int
        Output image size
    indexes : list of ints or a single int, optional, (defaults: None)
        If `indexes` is a list, the result is a 3D array, but is
        a 2D array if it is a band index number.
    nodata: int or float, optional (defaults: None)
    resampling_method : str, optional (default: "bilinear")
         Resampling algorithm

    Returns
    -------
    out : array, int
        returns pixel value.

    """
    if isinstance(indexes, int):
        indexes = [indexes]
    elif isinstance(indexes, tuple):
        indexes = list(indexes)

    vrt_params = dict(
        add_alpha=True, crs="epsg:3857", resampling=Resampling[resampling_method]
    )

    vrt_transform, vrt_width, vrt_height = get_vrt_transform(src_dst, bounds)
    vrt_params.update(dict(transform=vrt_transform, width=vrt_width, height=vrt_height))

    indexes = indexes if indexes is not None else src_dst.indexes
    out_shape = (len(indexes), tilesize, tilesize)

    nodata = nodata if nodata is not None else src_dst.nodata
    if nodata is not None:
        vrt_params.update(dict(nodata=nodata, add_alpha=False, src_nodata=nodata))

    if has_alpha_band(src_dst):
        vrt_params.update(dict(add_alpha=False))

    with WarpedVRT(src_dst, **vrt_params) as vrt:
        data = vrt.read(
            out_shape=out_shape,
            indexes=indexes,
            resampling=Resampling[resampling_method],
        )
        mask = vrt.dataset_mask(out_shape=(tilesize, tilesize))

        return data, mask


def tile_read(source, bounds, tilesize, **kwargs):
    """
    Read data and mask.

    Attributes
    ----------
    source : str or rasterio.io.DatasetReader
        input file path or rasterio.io.DatasetReader object
    bounds : list
        Mercator tile bounds (left, bottom, right, top)
    tilesize : int
        Output image size
    kwargs: dict, optional
        These will be passed to the _tile_read function.

    Returns
    -------
    out : array, int
        returns pixel value.

    """
    if isinstance(source, DatasetReader):
        return _tile_read(source, bounds, tilesize, **kwargs)
    else:
        with rasterio.open(source) as src_dst:
            return _tile_read(src_dst, bounds, tilesize, **kwargs)


def linear_rescale(image, in_range=(0, 1), out_range=(1, 255)):
    """
    Linear rescaling.

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
    """
    Check if a mercatile tile is inside a given bounds.

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

    return (
        (tile_x <= maxtile.x + 1)
        and (tile_x >= mintile.x)
        and (tile_y <= maxtile.y + 1)
        and (tile_y >= mintile.y)
    )


def _apply_discrete_colormap(arr, cmap):
    """
    Apply discrete colormap.

    Attributes
    ----------
    arr : numpy.ndarray
        1D image array to convert.
    color_map: dict
        Discrete ColorMap dictionary
        e.g:
        {
            1: [255, 255, 255],
            2: [255, 0, 0]
        }

    Returns
    -------
    arr: numpy.ndarray

    """
    res = np.zeros((arr.shape[1], arr.shape[2], 3), dtype=np.uint8)
    for k, v in cmap.items():
        res[arr[0] == k] = v
    return np.transpose(res, [2, 0, 1])


def array_to_image(
    arr, mask=None, img_format="png", color_map=None, **creation_options
):
    """
    Translate numpy ndarray to image buffer using GDAL.

    Usage
    -----
    tile, mask = rio_tiler.utils.tile_read(......)
    with open('test.jpg', 'wb') as f:
        f.write(array_to_image(tile, mask, img_format="jpeg"))

    Attributes
    ----------
    arr : numpy ndarray
        Image array to encode.
    mask: numpy ndarray, optional
        Mask array
    img_format: str, optional
        Image format to return (default: 'png').
        List of supported format by GDAL: https://www.gdal.org/formats_list.html
    color_map: numpy.ndarray or dict, optional
        color_map can be either a (256, 3) array or RGB triplet
        (e.g. [[255, 255, 255],...]) mapping each 1D pixel value rescaled
        from 0 to 255
        OR
        it can be a dictionary of discrete values
        (e.g. { 1.3: [255, 255, 255], 2.5: [255, 0, 0]}) mapping any pixel value to a triplet
    creation_options: dict, optional
        Image driver creation options to pass to GDAL

    Returns
    -------
    bytes

    """
    img_format = img_format.lower()

    if len(arr.shape) < 3:
        arr = np.expand_dims(arr, axis=0)

    if color_map is not None and isinstance(color_map, dict):
        arr = _apply_discrete_colormap(arr, color_map)
    elif color_map is not None:
        arr = np.transpose(color_map[arr][0], [2, 0, 1]).astype(np.uint8)

    # WEBP doesn't support 1band dataset so we must hack to create a RGB dataset
    if img_format == "webp" and arr.shape[0] == 1:
        arr = np.repeat(arr, 3, axis=0)

    if mask is not None and img_format != "jpeg":
        nbands = arr.shape[0] + 1
    else:
        nbands = arr.shape[0]

    output_profile = dict(
        driver=img_format,
        dtype=arr.dtype,
        count=nbands,
        height=arr.shape[1],
        width=arr.shape[2],
    )
    output_profile.update(creation_options)

    with MemoryFile() as memfile:
        with memfile.open(**output_profile) as dst:
            dst.write(arr, indexes=list(range(1, arr.shape[0] + 1)))

            # Use Mask as an alpha band
            if mask is not None and img_format != "jpeg":
                dst.write(mask.astype(arr.dtype), indexes=nbands)

        return memfile.read()


def get_colormap(name="cfastie", format="pil"):
    """
    Return Pillow or GDAL compatible colormap array.

    Attributes
    ----------
    name : str, optional
        Colormap name (default: cfastie)
    format: str, optional
        Compatiblity library, should be "pil" or "gdal" (default: pil).

    Returns
    -------
    colormap : list or numpy.array
        Color map list in a Pillow friendly format
        more info: http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#PIL.Image.Image.putpalette
        or
        Color map array in GDAL friendly format

    """
    cmap_file = os.path.join(os.path.dirname(__file__), "cmap", "{0}.txt".format(name))
    with open(cmap_file) as cmap:
        lines = cmap.read().splitlines()
        colormap = [
            list(map(int, line.split())) for line in lines if not line.startswith("#")
        ][1:]

    cmap = list(np.array(colormap).flatten())
    if format.lower() == "pil":
        return cmap
    elif format.lower() == "gdal":
        return np.array(list(_chunks(cmap, 3)))
    else:
        raise Exception("Unsupported {} colormap format".format(format))


def mapzen_elevation_rgb(arr):
    """
    Encode elevation value to RGB values compatible with Mapzen tangram.

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
    r = arr / 256
    g = arr % 256
    b = (arr * 256) % 256
    return np.stack([r, g, b]).astype(np.uint8)


def expression(sceneid, tile_x, tile_y, tile_z, expr=None, **kwargs):
    """
    Apply expression on data.

    Attributes
    ----------
    sceneid : str
        Landsat id, Sentinel id, CBERS ids or file url.

    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    expr : str, required
        Expression to apply (e.g '(B5+B4)/(B5-B4)')
        Band name should start with 'B'.

    Returns
    -------
    out : ndarray
        Returns processed pixel value.

    """
    if not expr:
        raise Exception("Missing expression")

    bands_names = tuple(set(re.findall(r"b(?P<bands>[0-9A]{1,2})", expr)))
    rgb = expr.split(",")

    if sceneid.startswith("L"):
        from rio_tiler.landsat8 import tile as l8_tile

        arr, mask = l8_tile(
            sceneid, tile_x, tile_y, tile_z, bands=bands_names, **kwargs
        )
    elif sceneid.startswith("S2"):
        from rio_tiler.sentinel2 import tile as s2_tile

        arr, mask = s2_tile(
            sceneid, tile_x, tile_y, tile_z, bands=bands_names, **kwargs
        )
    elif sceneid.startswith("CBERS"):
        from rio_tiler.cbers import tile as cbers_tile

        arr, mask = cbers_tile(
            sceneid, tile_x, tile_y, tile_z, bands=bands_names, **kwargs
        )
    else:
        from rio_tiler.main import tile as main_tile

        bands = tuple(map(int, bands_names))
        arr, mask = main_tile(sceneid, tile_x, tile_y, tile_z, indexes=bands, **kwargs)

    ctx = {}
    for bdx, b in enumerate(bands_names):
        ctx["b{}".format(b)] = arr[bdx]

    return (
        np.array(
            [np.nan_to_num(ne.evaluate(bloc.strip(), local_dict=ctx)) for bloc in rgb]
        ),
        mask,
    )


def pansharpening_brovey(rgb, pan, weight, pan_dtype):
    """
    Brovey Method: Each resampled, multispectral pixel is
    multiplied by the ratio of the corresponding
    panchromatic pixel intensity to the sum of all the
    multispectral intensities.

    Original code from https://github.com/mapbox/rio-pansharpen
    """

    def _calculateRatio(rgb, pan, weight):
        return pan / ((rgb[0] + rgb[1] + rgb[2] * weight) / (2 + weight))

    with np.errstate(invalid="ignore", divide="ignore"):
        ratio = _calculateRatio(rgb, pan, weight)
        return np.clip(ratio * rgb, 0, np.iinfo(pan_dtype).max).astype(pan_dtype)
