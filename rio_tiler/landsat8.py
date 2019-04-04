"""rio_tiler.landsat8: Landsat-8 processing."""

import os
import re
import warnings
import datetime
import multiprocessing
from functools import partial
from concurrent import futures

import numpy as np

import mercantile

import rasterio
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds
from rio_toa import reflectance, brightness_temp, toa_utils

from rio_tiler import utils
from rio_tiler.errors import (
    TileOutsideBounds,
    InvalidBandName,
    InvalidLandsatSceneId,
    NoOverviewWarning,
)

# Python 2/3
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


LANDSAT_BUCKET = "s3://landsat-pds"
LANDSAT_BANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# ref: https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor
MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))


def _landsat_get_mtl(sceneid):
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
    scene_params = _landsat_parse_scene_id(sceneid)
    meta_file = "http://landsat-pds.s3.amazonaws.com/{}_MTL.txt".format(
        scene_params["key"]
    )
    metadata = str(urlopen(meta_file).read().decode())
    return toa_utils._parse_mtl_txt(metadata)


def _landsat_parse_scene_id(sceneid):
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


def _landsat_stats(
    band,
    address_prefix,
    metadata,
    overview_level=None,
    max_size=1024,
    percentiles=(2, 98),
    dst_crs=CRS({"init": "EPSG:4326"}),
    histogram_bins=10,
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
    histogram_bins: int, optional
        Defines the number of equal-width histogram bins (default: 10).

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

    stats = {band: utils._stats(arr, percentiles=percentiles, bins=histogram_bins)}

    return {
        "bounds": {
            "value": bounds,
            "crs": dst_crs.to_string() if isinstance(dst_crs, CRS) else dst_crs,
        },
        "statistics": stats,
    }


def bounds(sceneid):
    """
    Retrieve image bounds.

    Attributes
    ----------
    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.

    Returns
    -------
    out : dict
        dictionary with image bounds.

    """
    meta_data = _landsat_get_mtl(sceneid).get("L1_METADATA_FILE")

    info = {"sceneid": sceneid}
    info["bounds"] = toa_utils._get_bounds_from_metadata(meta_data["PRODUCT_METADATA"])

    return info


def metadata(sceneid, pmin=2, pmax=98, **kwargs):
    """
    Retrieve image bounds and band statistics.

    Attributes
    ----------
    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.
    kwargs : optional
        These are passed to 'rio_tiler.landsat8._landsat_stats'
        e.g: histogram_bins=20, dst_crs='epsg:4326'

    Returns
    -------
    out : dict
        Dictionary with bounds and bands statistics.

    """
    scene_params = _landsat_parse_scene_id(sceneid)
    meta_data = _landsat_get_mtl(sceneid).get("L1_METADATA_FILE")
    path_prefix = "{}/{}".format(LANDSAT_BUCKET, scene_params["key"])

    info = {"sceneid": sceneid}

    _stats_worker = partial(
        _landsat_stats,
        address_prefix=path_prefix,
        metadata=meta_data,
        overview_level=1,
        percentiles=(pmin, pmax),
        **kwargs
    )

    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        responses = list(executor.map(_stats_worker, LANDSAT_BANDS))

    info["bounds"] = [
        r["bounds"] for b, r in zip(LANDSAT_BANDS, responses) if b == "8"
    ][0]

    info["statistics"] = {
        b: v
        for b, d in zip(LANDSAT_BANDS, responses)
        for k, v in d["statistics"].items()
    }
    return info


def tile(
    sceneid, tile_x, tile_y, tile_z, bands=("4", "3", "2"), tilesize=256, pan=False
):
    """
    Create mercator tile from Landsat-8 data.

    Attributes
    ----------
    sceneid : str
        Landsat sceneid. For scenes after May 2017,
        sceneid have to be LANDSAT_PRODUCT_ID.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, str, optional (default: ("4", "3", "2"))
        Bands index for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.
    pan : boolean, optional (default: False)
        If True, apply pan-sharpening.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in LANDSAT_BANDS:
            raise InvalidBandName("{} is not a valid Landsat band name".format(band))

    scene_params = _landsat_parse_scene_id(sceneid)
    meta_data = _landsat_get_mtl(sceneid).get("L1_METADATA_FILE")
    landsat_address = "{}/{}".format(LANDSAT_BUCKET, scene_params["key"])

    wgs_bounds = toa_utils._get_bounds_from_metadata(meta_data["PRODUCT_METADATA"])

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = ["{}_B{}.TIF".format(landsat_address, band) for band in bands]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=tilesize, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        data = np.concatenate(data)
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

        if pan:
            pan_address = "{}_B8.TIF".format(landsat_address)
            matrix_pan, mask = utils.tile_read(
                pan_address, tile_bounds, tilesize, nodata=0
            )
            data = utils.pansharpening_brovey(data, matrix_pan, 0.2, matrix_pan.dtype)

        sun_elev = meta_data["IMAGE_ATTRIBUTES"]["SUN_ELEVATION"]

        for bdx, band in enumerate(bands):
            if int(band) > 9:  # TIRS
                multi_rad = meta_data["RADIOMETRIC_RESCALING"].get(
                    "RADIANCE_MULT_BAND_{}".format(band)
                )

                add_rad = meta_data["RADIOMETRIC_RESCALING"].get(
                    "RADIANCE_ADD_BAND_{}".format(band)
                )

                k1 = meta_data["TIRS_THERMAL_CONSTANTS"].get(
                    "K1_CONSTANT_BAND_{}".format(band)
                )

                k2 = meta_data["TIRS_THERMAL_CONSTANTS"].get(
                    "K2_CONSTANT_BAND_{}".format(band)
                )

                data[bdx] = brightness_temp.brightness_temp(
                    data[bdx], multi_rad, add_rad, k1, k2
                )

            else:
                multi_reflect = meta_data["RADIOMETRIC_RESCALING"].get(
                    "REFLECTANCE_MULT_BAND_{}".format(band)
                )

                add_reflect = meta_data["RADIOMETRIC_RESCALING"].get(
                    "REFLECTANCE_ADD_BAND_{}".format(band)
                )

                data[bdx] = 10000 * reflectance.reflectance(
                    data[bdx], multi_reflect, add_reflect, sun_elev
                )

        return data, mask
