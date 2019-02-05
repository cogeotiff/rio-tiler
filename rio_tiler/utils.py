"""rio_tiler.utils: utility functions."""

import os
import re
import math
import base64
import logging
import warnings
import datetime
from io import BytesIO

import numpy as np
import numexpr as ne

import mercantile

import rasterio
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT
from rasterio.enums import Resampling, MaskFlags, ColorInterp
from rasterio.io import DatasetReader
from rasterio.plot import reshape_as_image
from rasterio import transform
from rasterio.warp import calculate_default_transform, transform_bounds
from rio_toa import reflectance, brightness_temp, toa_utils

from rio_tiler import profiles as TileProfiles
from rio_tiler.errors import (
    InvalidFormat,
    InvalidLandsatSceneId,
    InvalidSentinelSceneId,
    InvalidCBERSSceneId,
    DeprecationWarning,
    NoOverviewWarning,
)

from PIL import Image

# Python 2/3
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


logger = logging.getLogger(__name__)


def landsat_min_max_worker(
    band, address, metadata, pmin=2, pmax=98, width=1024, height=1024
):
    """
    Retrieve histogram percentage cut for a Landsat-8 scene.

    Attributes
    ----------
    address : Landsat band AWS address
    band : Landsat band number
    metadata : Landsat metadata
    pmin : Histogram minimum cut (default: 2)
    pmax : Histogram maximum cut (default: 98)
    width : int, optional (default: 1024)
        Pixel width for the decimated read.
    height : int, optional (default: 1024)
        Pixel height for the decimated read.

    Returns
    -------
    out : list, int
        returns a list of the min/max histogram cut values.

    """
    warnings.warn(
        "'rio_tiler.utils.landsat_min_max_worker' will be deprecated in 1.0",
        DeprecationWarning,
    )
    if band in ["10", "11"]:  # TIRS
        multi_rad = metadata["RADIOMETRIC_RESCALING"].get(
            "RADIANCE_MULT_BAND_{}".format(band)
        )

        add_rad = metadata["RADIOMETRIC_RESCALING"].get(
            "RADIANCE_ADD_BAND_{}".format(band)
        )

        k1 = metadata["TIRS_THERMAL_CONSTANTS"].get("K1_CONSTANT_BAND_{}".format(band))

        k2 = metadata["TIRS_THERMAL_CONSTANTS"].get("K2_CONSTANT_BAND_{}".format(band))

        with rasterio.open("{}_B{}.TIF".format(address, band)) as src:
            arr = src.read(indexes=1, out_shape=(height, width)).astype(
                src.profile["dtype"]
            )
            arr = brightness_temp.brightness_temp(arr, multi_rad, add_rad, k1, k2)
    else:
        multi_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            "REFLECTANCE_MULT_BAND_{}".format(band)
        )
        add_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            "REFLECTANCE_ADD_BAND_{}".format(band)
        )
        sun_elev = metadata["IMAGE_ATTRIBUTES"]["SUN_ELEVATION"]

        with rasterio.open("{}_B{}.TIF".format(address, band)) as src:
            arr = src.read(indexes=1, out_shape=(height, width)).astype(
                src.profile["dtype"]
            )
            arr = 10000 * reflectance.reflectance(
                arr, multi_reflect, add_reflect, sun_elev, src_nodata=0
            )

    return np.percentile(arr[arr > 0], (pmin, pmax)).astype(np.int).tolist()


def band_min_max_worker(address, pmin=2, pmax=98, width=1024, height=1024):
    """
    Retrieve histogram percentage cut for a single image band.

    Attributes
    ----------
    address : Image band URL
    pmin : Histogram minimum cut (default: 2)
    pmax : Histogram maximum cut (default: 98)
    width : int, optional (default: 1024)
        Pixel width for the decimated read.
    height : int, optional (default: 1024)
        Pixel height for the decimated read.

    Returns
    -------
    out : list, int
        returns a list of the min/max histogram cut values.

    """
    warnings.warn(
        "'rio_tiler.utils.band_min_max_worker' will be deprecated in 1.0",
        DeprecationWarning,
    )
    with rasterio.open(address) as src:
        arr = src.read(indexes=1, out_shape=(height, width)).astype(
            src.profile["dtype"]
        )

    return np.percentile(arr[arr > 0], (pmin, pmax)).astype(np.int).tolist()


def _stats(arr, percentiles=(2, 98)):
    """Calculate array statistics."""
    sample, edges = np.histogram(arr[~arr.mask])
    return {
        "pc": np.percentile(arr[~arr.mask], percentiles).astype(arr.dtype).tolist(),
        "min": arr.min().item(),
        "max": arr.max().item(),
        "std": arr.std().item(),
        "histogram": [sample.tolist(), edges.tolist()],
    }


def landsat_get_stats(
    band,
    address_prefix,
    metadata,
    overview_level=None,
    max_size=1024,
    percentiles=(2, 98),
    dst_crs=CRS({"init": "EPSG:4326"}),
):
    """
    Retrieve landsat dataset statistics.

    Attributes
    ----------
    band : str
        Landsat band number
    address_prefix : str
        A Landsat AWS S3 dataset prefix.
    metadata : dict
        Landsat metadata
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

    Returns
    -------
    out : dict
        (percentiles), min, max, stdev, histogram for each band,
        e.g.
        {
            "4": {
                'pc': [15, 121],
                'min': 1,
                'max': 162,
                'std': 27.22067722127997,
                'histogram': [
                    [102934, 135489, 20981, 13548, 11406, 8799, 7351, 5622, 2985, 662]
                    [1., 17.1, 33.2, 49.3, 65.4, 81.5, 97.6, 113.7, 129.8, 145.9, 162.]
                ]
            }
        }
    """
    src_path = "{}_B{}.TIF".format(address_prefix, band)
    with rasterio.open(src_path) as src:
        levels = src.overviews(1)
        width = src.width
        height = src.height
        bounds = transform_bounds(
            *[src.crs, dst_crs] + list(src.bounds), densify_pts=21
        )

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

        out_shape = (height // decim, width // decim)
        vrt_params = dict(
            nodata=0, add_alpha=False, src_nodata=0, init_dest_nodata=False
        )
        with WarpedVRT(src, **vrt_params) as vrt:
            arr = vrt.read(out_shape=out_shape, indexes=[1], masked=True)

    if band in ["10", "11"]:  # TIRS
        multi_rad = metadata["RADIOMETRIC_RESCALING"].get(
            "RADIANCE_MULT_BAND_{}".format(band)
        )
        add_rad = metadata["RADIOMETRIC_RESCALING"].get(
            "RADIANCE_ADD_BAND_{}".format(band)
        )
        k1 = metadata["TIRS_THERMAL_CONSTANTS"].get("K1_CONSTANT_BAND_{}".format(band))
        k2 = metadata["TIRS_THERMAL_CONSTANTS"].get("K2_CONSTANT_BAND_{}".format(band))

        arr = brightness_temp.brightness_temp(arr, multi_rad, add_rad, k1, k2)
    else:
        multi_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            "REFLECTANCE_MULT_BAND_{}".format(band)
        )
        add_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            "REFLECTANCE_ADD_BAND_{}".format(band)
        )
        sun_elev = metadata["IMAGE_ATTRIBUTES"]["SUN_ELEVATION"]

        arr = 10000 * reflectance.reflectance(
            arr, multi_reflect, add_reflect, sun_elev, src_nodata=0
        )

    stats = {band: _stats(arr, percentiles=percentiles)}

    return {
        "bounds": {
            "value": bounds,
            "crs": dst_crs.to_string() if isinstance(dst_crs, CRS) else dst_crs,
        },
        "statistics": stats,
    }


def raster_get_stats(
    src_path,
    indexes=None,
    nodata=None,
    overview_level=None,
    max_size=1024,
    percentiles=(2, 98),
    dst_crs=CRS({"init": "EPSG:4326"}),
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

    Returns
    -------
    out : dict
        bounds and band statistics: (percentiles), min, max, stdev, histogram

        e.g.
        {
            'bounds': {
                'value': (145.72265625, 14.853515625, 145.810546875, 14.94140625),
                'crs': '+init=EPSG:4326'
            },
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

    with rasterio.open(src_path) as src:
        levels = src.overviews(1)
        width = src.width
        height = src.height
        indexes = indexes if indexes else src.indexes
        bounds = transform_bounds(
            *[src.crs, dst_crs] + list(src.bounds), densify_pts=21
        )

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
        if has_alpha_band(src):
            vrt_params.update(dict(add_alpha=False))

        if nodata is not None:
            vrt_params.update(
                dict(
                    nodata=nodata,
                    add_alpha=False,
                    src_nodata=nodata,
                    init_dest_nodata=False,
                )
            )

        with WarpedVRT(src, **vrt_params) as vrt:
            arr = vrt.read(out_shape=out_shape, indexes=indexes, masked=True)
            stats = {
                indexes[b]: _stats(arr[b], percentiles=percentiles)
                for b in range(arr.shape[0])
                if vrt.colorinterp[b] != ColorInterp.alpha
            }

    return {
        "bounds": {
            "value": bounds,
            "crs": dst_crs.to_string() if isinstance(dst_crs, CRS) else dst_crs,
        },
        "statistics": stats,
    }


def get_vrt_transform(src, bounds, bounds_crs="epsg:3857"):
    """
    Calculate VRT transform.

    Attributes
    ----------
    src : rasterio.io.DatasetReader
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
        src.crs, bounds_crs, src.width, src.height, *src.bounds
    )
    w, s, e, n = bounds
    vrt_width = math.ceil((e - w) / dst_transform.a)
    vrt_height = math.ceil((s - n) / dst_transform.e)

    vrt_transform = transform.from_bounds(w, s, e, n, vrt_width, vrt_height)

    return vrt_transform, vrt_width, vrt_height


def has_alpha_band(src):
    """Check for alpha band or mask in source."""
    if (
        any([MaskFlags.alpha in flags for flags in src.mask_flag_enums])
        or ColorInterp.alpha in src.colorinterp
    ):
        return True
    return False


def tile_read(source, bounds, tilesize, indexes=[1], nodata=None):
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
    indexes : list of ints or a single int, optional, (default: 1)
        If `indexes` is a list, the result is a 3D array, but is
        a 2D array if it is a band index number.
    nodata: int or float, optional (defaults: None)

    Returns
    -------
    out : array, int
        returns pixel value.

    """
    if isinstance(indexes, int):
        indexes = [indexes]

    vrt_params = dict(add_alpha=True, crs="epsg:3857", resampling=Resampling.bilinear)

    if nodata is not None:
        vrt_params.update(
            dict(
                nodata=nodata,
                add_alpha=False,
                src_nodata=nodata,
                init_dest_nodata=False,
            )
        )

    out_shape = (len(indexes), tilesize, tilesize)

    if isinstance(source, DatasetReader):
        vrt_transform, vrt_width, vrt_height = get_vrt_transform(source, bounds)
        vrt_params.update(
            dict(transform=vrt_transform, width=vrt_width, height=vrt_height)
        )

        if has_alpha_band(source):
            vrt_params.update(dict(add_alpha=False))

        with WarpedVRT(source, **vrt_params) as vrt:
            data = vrt.read(
                out_shape=out_shape, resampling=Resampling.bilinear, indexes=indexes
            )
            mask = vrt.dataset_mask(out_shape=(tilesize, tilesize))

    else:
        with rasterio.open(source) as src:
            vrt_transform, vrt_width, vrt_height = get_vrt_transform(src, bounds)
            vrt_params.update(
                dict(transform=vrt_transform, width=vrt_width, height=vrt_height)
            )

            if has_alpha_band(src):
                vrt_params.update(dict(add_alpha=False))

            with WarpedVRT(src, **vrt_params) as vrt:
                data = vrt.read(
                    out_shape=out_shape, resampling=Resampling.bilinear, indexes=indexes
                )
                mask = vrt.dataset_mask(out_shape=(tilesize, tilesize))

    return data, mask


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


def landsat_get_mtl(sceneid):
    """
    Get Landsat-8 MTL metadata.

    Attributes
    ----------
    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.

    Returns
    -------
    out : dict
        returns a JSON like object with the metadata.

    """
    scene_params = landsat_parse_scene_id(sceneid)
    meta_file = "http://landsat-pds.s3.amazonaws.com/{}_MTL.txt".format(
        scene_params["key"]
    )
    metadata = str(urlopen(meta_file).read().decode())
    return toa_utils._parse_mtl_txt(metadata)


def landsat_parse_scene_id(sceneid):
    """
    Parse Landsat-8 scene id.

    Author @perrygeo - http://www.perrygeo.com

    """
    pre_collection = r"(L[COTEM]8\d{6}\d{7}[A-Z]{3}\d{2})"
    collection_1 = r"(L[COTEM]08_L\d{1}[A-Z]{2}_\d{6}_\d{8}_\d{8}_\d{2}_(T1|T2|RT))"
    if not re.match("^{}|{}$".format(pre_collection, collection_1), sceneid):
        raise InvalidLandsatSceneId("Could not match {}".format(sceneid))

    precollection_pattern = (
        r"^L"
        r"(?P<sensor>\w{1})"
        r"(?P<satellite>\w{1})"
        r"(?P<path>[0-9]{3})"
        r"(?P<row>[0-9]{3})"
        r"(?P<acquisitionYear>[0-9]{4})"
        r"(?P<acquisitionJulianDay>[0-9]{3})"
        r"(?P<groundStationIdentifier>\w{3})"
        r"(?P<archiveVersion>[0-9]{2})$"
    )

    collection_pattern = (
        r"^L"
        r"(?P<sensor>\w{1})"
        r"(?P<satellite>\w{2})"
        r"_"
        r"(?P<processingCorrectionLevel>\w{4})"
        r"_"
        r"(?P<path>[0-9]{3})"
        r"(?P<row>[0-9]{3})"
        r"_"
        r"(?P<acquisitionYear>[0-9]{4})"
        r"(?P<acquisitionMonth>[0-9]{2})"
        r"(?P<acquisitionDay>[0-9]{2})"
        r"_"
        r"(?P<processingYear>[0-9]{4})"
        r"(?P<processingMonth>[0-9]{2})"
        r"(?P<processingDay>[0-9]{2})"
        r"_"
        r"(?P<collectionNumber>\w{2})"
        r"_"
        r"(?P<collectionCategory>\w{2})$"
    )

    meta = None
    for pattern in [collection_pattern, precollection_pattern]:
        match = re.match(pattern, sceneid, re.IGNORECASE)
        if match:
            meta = match.groupdict()
            break

    if meta.get("acquisitionJulianDay"):
        date = datetime.datetime(
            int(meta["acquisitionYear"]), 1, 1
        ) + datetime.timedelta(int(meta["acquisitionJulianDay"]) - 1)

        meta["date"] = date.strftime("%Y-%m-%d")
    else:
        meta["date"] = "{}-{}-{}".format(
            meta["acquisitionYear"], meta["acquisitionMonth"], meta["acquisitionDay"]
        )

    collection = meta.get("collectionNumber", "")
    if collection != "":
        collection = "c{}".format(int(collection))

    meta["key"] = os.path.join(
        collection, "L8", meta["path"], meta["row"], sceneid, sceneid
    )

    meta["scene"] = sceneid

    return meta


def sentinel_parse_scene_id(sceneid):
    """Parse Sentinel-2 scene id."""
    if not re.match("^S2[AB]_tile_[0-9]{8}_[0-9]{2}[A-Z]{3}_[0-9]$", sceneid):
        raise InvalidSentinelSceneId("Could not match {}".format(sceneid))

    sentinel_pattern = (
        r"^S"
        r"(?P<sensor>\w{1})"
        r"(?P<satellite>[AB]{1})"
        r"_tile_"
        r"(?P<acquisitionYear>[0-9]{4})"
        r"(?P<acquisitionMonth>[0-9]{2})"
        r"(?P<acquisitionDay>[0-9]{2})"
        r"_"
        r"(?P<utm>[0-9]{2})"
        r"(?P<lat>\w{1})"
        r"(?P<sq>\w{2})"
        r"_"
        r"(?P<num>[0-9]{1})$"
    )

    meta = None
    match = re.match(sentinel_pattern, sceneid, re.IGNORECASE)
    if match:
        meta = match.groupdict()

    utm_zone = meta["utm"].lstrip("0")
    grid_square = meta["sq"]
    latitude_band = meta["lat"]
    year = meta["acquisitionYear"]
    month = meta["acquisitionMonth"].lstrip("0")
    day = meta["acquisitionDay"].lstrip("0")
    img_num = meta["num"]

    meta["key"] = "tiles/{}/{}/{}/{}/{}/{}/{}".format(
        utm_zone, latitude_band, grid_square, year, month, day, img_num
    )

    meta["scene"] = sceneid

    return meta


def cbers_parse_scene_id(sceneid):
    """Parse CBERS scene id."""
    if not re.match(r"^CBERS_4_\w+_[0-9]{8}_[0-9]{3}_[0-9]{3}_L[0-9]$", sceneid):
        raise InvalidCBERSSceneId("Could not match {}".format(sceneid))

    cbers_pattern = (
        r"(?P<satellite>\w+)_"
        r"(?P<mission>[0-9]{1})"
        r"_"
        r"(?P<instrument>\w+)"
        r"_"
        r"(?P<acquisitionYear>[0-9]{4})"
        r"(?P<acquisitionMonth>[0-9]{2})"
        r"(?P<acquisitionDay>[0-9]{2})"
        r"_"
        r"(?P<path>[0-9]{3})"
        r"_"
        r"(?P<row>[0-9]{3})"
        r"_"
        r"(?P<processingCorrectionLevel>L[0-9]{1})$"
    )

    meta = None
    match = re.match(cbers_pattern, sceneid, re.IGNORECASE)
    if match:
        meta = match.groupdict()

    path = meta["path"]
    row = meta["row"]
    instrument = meta["instrument"]
    meta["key"] = "CBERS4/{}/{}/{}/{}".format(instrument, path, row, sceneid)

    meta["scene"] = sceneid

    instrument_params = {
        "MUX": {
            "reference_band": "6",
            "bands": ["5", "6", "7", "8"],
            "rgb": ("7", "6", "5"),
        },
        "AWFI": {
            "reference_band": "14",
            "bands": ["13", "14", "15", "16"],
            "rgb": ("15", "14", "13"),
        },
        "PAN10M": {
            "reference_band": "4",
            "bands": ["2", "3", "4"],
            "rgb": ("3", "4", "2"),
        },
        "PAN5M": {"reference_band": "1", "bands": ["1"], "rgb": ("1", "1", "1")},
    }
    meta["reference_band"] = instrument_params[instrument]["reference_band"]
    meta["bands"] = instrument_params[instrument]["bands"]
    meta["rgb"] = instrument_params[instrument]["rgb"]

    return meta


def array_to_img(arr, mask=None, color_map=None):
    """
    Convert an array to a base64 encoded img.

    Attributes
    ----------
    arr : numpy ndarray
        Image array to encode.
    Mask: numpy ndarray
        Mask
    color_map: numpy array
        ColorMap array (see: utils.get_colormap)

    Returns
    -------
    img : object
        Pillow image

    """
    if arr.dtype != np.uint8:
        logger.error("Data casted to UINT8")
        arr = arr.astype(np.uint8)

    if len(arr.shape) >= 3:
        arr = reshape_as_image(arr)
        arr = arr.squeeze()

    if len(arr.shape) != 2 and color_map:
        raise InvalidFormat("Cannot apply colormap on a multiband image")

    mode = "L" if len(arr.shape) == 2 else "RGB"

    img = Image.fromarray(arr, mode=mode)
    if color_map:
        img.putpalette(color_map)

    if mask is not None:
        mask_img = Image.fromarray(mask.astype(np.uint8))
        img.putalpha(mask_img)

    return img


def img_to_buffer(img, image_format, image_options={}):
    """
    Convert a Pillow image to io buffer.

    Attributes
    ----------
    img : object
        Pillow image
    image_format : str
        Image file formats
    image_options : dict
        Pillow image format options.
        See https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

    Returns
    -------
    buffer

    """
    if image_format == "jpeg":
        img = img.convert("RGB")

    sio = BytesIO()
    img.save(sio, image_format.upper(), **image_options)
    sio.seek(0)
    return sio.getvalue()


def b64_encode_img(img, tileformat):
    """
    Convert a Pillow image to an base64 encoded string.

    Attributes
    ----------
    img : object
        Pillow image
    tileformat : str
        Image format to return (Accepted: "jpg" or "png")

    Returns
    -------
    out : str
        base64 encoded image.

    """
    params = TileProfiles.get(tileformat)

    if tileformat == "jpeg":
        img = img.convert("RGB")

    sio = BytesIO()
    img.save(sio, tileformat.upper(), **params)
    sio.seek(0)
    return base64.b64encode(sio.getvalue()).decode()


def get_colormap(name="cfastie"):
    """
    Read colormap file.

    Attributes
    ----------
    name : str
        colormap name (default: cfastie)

    Returns
    -------
    colormap : list
        Color map array in a Pillow friendly format
        more info: http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#PIL.Image.Image.putpalette

    """
    cmap_file = os.path.join(os.path.dirname(__file__), "cmap", "{0}.txt".format(name))
    with open(cmap_file) as cmap:
        lines = cmap.read().splitlines()
        colormap = [
            list(map(int, line.split())) for line in lines if not line.startswith("#")
        ][1:]

    return list(np.array(colormap).flatten())


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


def expression(sceneid, tile_x, tile_y, tile_z, expr, **kwargs):
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
    expr : str
        Expression to apply (e.g '(B5+B4)/(B5-B4)')
        Band name should start with 'B'.

    Returns
    -------
    out : ndarray
        Returns processed pixel value.

    """
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
