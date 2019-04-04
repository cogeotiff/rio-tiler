"""rio_tiler.sentinel2: Sentinel-2 processing."""

import os
import re
import multiprocessing
from functools import partial
from concurrent import futures

import numpy as np

import mercantile
import rasterio
from rasterio.crs import CRS
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidSentinelSceneId

SENTINEL_BUCKET = "s3://sentinel-s2-l1c"
SENTINEL_BANDS = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "8A",
    "09",
    "10",
    "11",
    "12",
]

# ref: https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor
MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))


def _sentinel_parse_scene_id(sceneid):
    """Parse Sentinel-2 scene id.

    Attributes
    ----------
    sceneid : str
        Sentinel-2 sceneid.

    Returns
    -------
    out : dict
        dictionary with metadata constructed from the sceneid.

        e.g:
        _sentinel_parse_scene_id('S2A_tile_20170323_07SNC_0')
        {
            "acquisitionDay": "23",
            "acquisitionMonth": "03",
            "acquisitionYear": "2017",
            "key": "tiles/7/S/NC/2017/3/23/0",
            "lat": "S",
            "num": "0",
            "satellite": "A",
            "scene": "S2A_tile_20170323_07SNC_0",
            "sensor": "2",
            "sq": "NC",
            "utm": "07",
        }

    """

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


def bounds(sceneid):
    """
    Retrieve image bounds.

    Attributes
    ----------
    sceneid : str
        Sentinel-2 sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.

    """
    scene_params = _sentinel_parse_scene_id(sceneid)
    sentinel_address = "{}/{}".format(SENTINEL_BUCKET, scene_params["key"])

    with rasterio.open("{}/preview.jp2".format(sentinel_address)) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    info = {"sceneid": sceneid}
    info["bounds"] = list(wgs_bounds)

    return info


def _sentinel_stats(src_path, percentiles=(2, 98), histogram_bins=10):
    """
    src_path : str or PathLike object
        A dataset path or URL. Will be opened in "r" mode.
    """

    with rasterio.open(src_path) as src:
        arr = src.read(indexes=[1], masked=True)
        arr[arr == 0] = np.ma.masked

    return {1: utils._stats(arr, percentiles=percentiles, bins=histogram_bins)}


def metadata(sceneid, pmin=2, pmax=98, **kwargs):
    """
    Retrieve image bounds and band statistics.

    Attributes
    ----------
    sceneid : str
        Sentinel-2 sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.
    kwargs : optional
        These are passed to 'rio_tiler.sentinel2._sentinel_stats'
        e.g: histogram_bins=20'

    Returns
    -------
    out : dict
        Dictionary with image bounds and bands statistics.

    """
    scene_params = _sentinel_parse_scene_id(sceneid)
    sentinel_address = "{}/{}".format(SENTINEL_BUCKET, scene_params["key"])

    dst_crs = CRS({"init": "EPSG:4326"})
    with rasterio.open("{}/preview.jp2".format(sentinel_address)) as src:
        bounds = transform_bounds(
            *[src.crs, dst_crs] + list(src.bounds), densify_pts=21
        )

    info = {"sceneid": sceneid}
    info["bounds"] = {"value": bounds, "crs": dst_crs.to_string()}

    addresses = [
        "{}/preview/B{}.jp2".format(sentinel_address, band) for band in SENTINEL_BANDS
    ]

    _stats_worker = partial(_sentinel_stats, percentiles=(pmin, pmax), **kwargs)
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        responses = executor.map(_stats_worker, addresses)
    info["statistics"] = {
        b: v for b, d in zip(SENTINEL_BANDS, responses) for k, v in d.items()
    }
    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=("04", "03", "02"), tilesize=256):
    """
    Create mercator tile from Sentinel-2 data.

    Attributes
    ----------
    sceneid : str
        Sentinel-2 sceneid.
    tile_x : int
        Mercator tile X index.
    tile_y : int
        Mercator tile Y index.
    tile_z : int
        Mercator tile ZOOM level.
    bands : tuple, str, optional (default: ('04', '03', '02'))
        Bands index for the RGB combination.
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in SENTINEL_BANDS:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    scene_params = _sentinel_parse_scene_id(sceneid)
    sentinel_address = "{}/{}".format(SENTINEL_BUCKET, scene_params["key"])

    sentinel_preview = "{}/preview.jp2".format(sentinel_address)
    with rasterio.open(sentinel_preview) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    if not utils.tile_exists(wgs_bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = ["{}/B{}.jp2".format(sentinel_address, band) for band in bands]

    _tiler = partial(utils.tile_read, bounds=tile_bounds, tilesize=tilesize, nodata=0)
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(_tiler, addresses)))
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

    return np.concatenate(data), mask
