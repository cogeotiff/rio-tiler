"""rio_tiler.cbers: cbers processing."""

import os
import re
import multiprocessing
from functools import partial
from concurrent import futures

import numpy as np

import mercantile
import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidCBERSSceneId

CBERS_BUCKET = "s3://cbers-pds"
CBERS_BANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "13", "14", "15", "16"]

# ref: https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor
MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))


def _cbers_parse_scene_id(sceneid):
    """Parse CBERS scene id.

    Attributes
    ----------
    sceneid : str
        CBERS sceneid.

    Returns
    -------
    out : dict
        dictionary with metadata constructed from the sceneid.

        e.g:
        _cbers_parse_scene_id('CBERS_4_PAN5M_20171121_057_094_L2')
        {
            "acquisitionDay": "21",
            "acquisitionMonth": "11",
            "acquisitionYear": "2017",
            "instrument": "PAN5M",
            "key": "CBERS4/PAN5M/057/094/CBERS_4_PAN5M_20171121_057_094_L2",
            "path": "057",
            "processingCorrectionLevel": "L2",
            "row": "094",
            "mission": "4",
            "scene": "CBERS_4_PAN5M_20171121_057_094_L2",
            "reference_band": "1",
            "bands": ["1"],
            "rgb": ("1", "1", "1"),
            "satellite": "CBERS",
        }

    """
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


def bounds(sceneid):
    """
    Retrieve image bounds.

    Attributes
    ----------
    sceneid : str
        CBERS sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.

    """
    scene_params = _cbers_parse_scene_id(sceneid)
    cbers_address = "{}/{}".format(CBERS_BUCKET, scene_params["key"])

    with rasterio.open(
        "{}/{}_BAND{}.tif".format(
            cbers_address, sceneid, scene_params["reference_band"]
        )
    ) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    info = {"sceneid": sceneid}
    info["bounds"] = list(wgs_bounds)

    return info


def metadata(sceneid, pmin=2, pmax=98, **kwargs):
    """
    Return band bounds and statistics.

    Attributes
    ----------
    sceneid : str
        CBERS sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.
    kwargs : optional
        These are passed to 'rio_tiler.utils.raster_get_stats'
        e.g: histogram_bins=20, dst_crs='epsg:4326'

    Returns
    -------
    out : dict
        Dictionary with bounds and bands statistics.

    """
    scene_params = _cbers_parse_scene_id(sceneid)
    cbers_address = "{}/{}".format(CBERS_BUCKET, scene_params["key"])
    bands = scene_params["bands"]
    ref_band = scene_params["reference_band"]

    info = {"sceneid": sceneid}

    addresses = [
        "{}/{}_BAND{}.tif".format(cbers_address, sceneid, band) for band in bands
    ]
    _stats_worker = partial(
        utils.raster_get_stats,
        indexes=[1],
        nodata=0,
        overview_level=2,
        percentiles=(pmin, pmax),
        **kwargs
    )
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        responses = list(executor.map(_stats_worker, addresses))

    info["bounds"] = [r["bounds"] for b, r in zip(bands, responses) if b == ref_band][0]
    info["statistics"] = {
        b: v for b, d in zip(bands, responses) for k, v in d["statistics"].items()
    }
    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=None, tilesize=256):
    """
    Create mercator tile from CBERS data.

    Attributes
    ----------
    sceneid : str
        CBERS sceneid.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, int, optional (default: None)
        Bands index for the RGB combination. If None uses default
        defined for the instrument
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    scene_params = _cbers_parse_scene_id(sceneid)

    if not bands:
        bands = scene_params["rgb"]

    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in scene_params["bands"]:
            raise InvalidBandName(
                "{} is not a valid band name for {} CBERS instrument".format(
                    band, scene_params["instrument"]
                )
            )

    cbers_address = "{}/{}".format(CBERS_BUCKET, scene_params["key"])

    with rasterio.open(
        "{}/{}_BAND{}.tif".format(
            cbers_address, sceneid, scene_params["reference_band"]
        )
    ) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = [
        "{}/{}_BAND{}.tif".format(cbers_address, sceneid, band) for band in bands
    ]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=tilesize, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

    return np.concatenate(data), mask
