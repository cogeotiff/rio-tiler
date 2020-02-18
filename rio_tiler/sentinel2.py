"""rio_tiler.sentinel2: Sentinel-2 processing."""

import os
import re
import warnings
import itertools
import multiprocessing
from functools import partial
from concurrent import futures

import numpy as np

import mercantile
import rasterio
from rasterio.crs import CRS
from rasterio.warp import transform_bounds

from rio_tiler import utils
from rio_tiler.errors import (
    DeprecationWarning,
    TileOutsideBounds,
    InvalidBandName,
    InvalidSentinelSceneId,
)

AWS_SENTINEL_BUCKET = "s3://sentinel-s2-"

SENTINEL_L1_BANDS = {
    "10m": ["02", "03", "04", "08"],
    "20m": ["05", "06", "07", "11", "12", "8A"],
    "60m": ["01", "09", "10"],
}

SENTINEL_L2_BANDS = {
    "10m": ["02", "03", "04", "08"],
    "20m": ["02", "03", "04", "05", "06", "07", "08", "11", "12", "8A"],
    "60m": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "11", "12", "8A"],
}

SENTINEL_L2_PRODUCTS = {
    "10m": ["AOT", "WVP"],
    "20m": ["AOT", "SCL", "WVP"],
    "60m": ["AOT", "SCL", "WVP"],
}

# ref: https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor
MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))


def _sentinel_parse_scene_id(sceneid):
    """
    Parse Sentinel-2 scene id.

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
    old_sceneid = "S2[AB]_tile_[0-9]{8}_[0-9]{2}[A-Z]{3}_[0-9]"
    new_sceneid = "S2[AB]_L[0-2][A-C]_[0-9]{8}_[0-9]{2}[A-Z]{3}_[0-9]"
    if not re.match("^{}|{}$".format(old_sceneid, new_sceneid), sceneid):
        raise InvalidSentinelSceneId("Could not match {}".format(sceneid))

    if re.match(old_sceneid, sceneid):
        warnings.warn(
            "Old Sentinel-2 scene id will be deprecated starting in rio-tiler v2.0.0"
            "Processing level is set to L1A.",
            DeprecationWarning,
        )

    sentinel_pattern_old = (
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

    sentinel_pattern_new = (
        r"^S"
        r"(?P<sensor>\w{1})"
        r"(?P<satellite>[AB]{1})"
        r"_"
        r"(?P<processingLevel>L[0-2][ABC])"
        r"_"
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
    for pattern in [sentinel_pattern_old, sentinel_pattern_new]:
        match = re.match(pattern, sceneid, re.IGNORECASE)
        if match:
            meta = match.groupdict()
            break

    if not meta.get("processingLevel"):
        meta["processingLevel"] = "L1C"

    utm_zone = meta["utm"].lstrip("0")
    grid_square = meta["sq"]
    latitude_band = meta["lat"]
    year = meta["acquisitionYear"]
    month = meta["acquisitionMonth"].lstrip("0")
    day = meta["acquisitionDay"].lstrip("0")
    img_num = meta["num"]

    meta["scene"] = sceneid
    meta["aws_bucket"] = AWS_SENTINEL_BUCKET + meta["processingLevel"].lower()
    meta["aws_prefix"] = "tiles/{}/{}/{}/{}/{}/{}/{}".format(
        utm_zone, latitude_band, grid_square, year, month, day, img_num
    )
    meta["key"] = meta["aws_prefix"]  # Will be deprecated in rio-tiler v2.0.0

    if meta["processingLevel"] == "L1C":
        meta["preview_file"] = "preview.jp2"
        meta["preview_prefix"] = "preview"
        meta["bands"] = list(
            itertools.chain.from_iterable(
                [bands for _, bands in SENTINEL_L1_BANDS.items()]
            )
        )
        meta["valid_bands"] = meta["bands"]
    else:
        meta["preview_file"] = "R60m/TCI.jp2"
        meta["preview_prefix"] = "R60m"
        meta["bands"] = SENTINEL_L2_BANDS["60m"]
        meta["valid_bands"] = meta["bands"] + SENTINEL_L2_PRODUCTS["60m"]

    return meta


def _l2_prefixed_band(band):
    """Return L2A prefixed bands name."""
    if band in SENTINEL_L2_BANDS["60m"]:
        for res, bands in SENTINEL_L2_BANDS.items():
            if band in bands:
                return "R{}/B{}".format(res, band)
    elif band in SENTINEL_L2_PRODUCTS["60m"]:
        for res, bands in SENTINEL_L2_PRODUCTS.items():
            if band in bands:
                return "R{}/{}".format(res, band)
    else:
        raise InvalidBandName("{} is not a valid Sentinel band name".format(band))


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
    preview_file = os.path.join(
        scene_params["aws_bucket"],
        scene_params["aws_prefix"],
        scene_params["preview_file"],
    )
    with rasterio.open(preview_file) as src:
        wgs_bounds = transform_bounds(
            *[src.crs, "epsg:4326"] + list(src.bounds), densify_pts=21
        )

    info = {"sceneid": sceneid}
    info["bounds"] = list(wgs_bounds)

    return info


def _sentinel_stats(
    src_path, percentiles=(2, 98), histogram_bins=10, histogram_range=None
):
    """
    src_path : str or PathLike object
        A dataset path or URL. Will be opened in "r" mode.
    """

    with rasterio.open(src_path) as src:
        arr = src.read(indexes=[1], masked=True)
        arr[arr == 0] = np.ma.masked

    params = {}
    if histogram_bins:
        params.update(dict(bins=histogram_bins))
    if histogram_range:
        params.update(dict(range=histogram_range))

    return {1: utils._stats(arr, percentiles=percentiles, **params)}


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
    path_prefix = os.path.join(scene_params["aws_bucket"], scene_params["aws_prefix"])
    preview_file = os.path.join(path_prefix, scene_params["preview_file"])

    dst_crs = CRS({"init": "EPSG:4326"})
    with rasterio.open(preview_file) as src:
        bounds = transform_bounds(
            *[src.crs, dst_crs] + list(src.bounds), densify_pts=21
        )

    info = {"sceneid": sceneid}
    info["bounds"] = {"value": bounds, "crs": dst_crs.to_string()}

    addresses = [
        "{}/{}/B{}.jp2".format(path_prefix, scene_params["preview_prefix"], band)
        for band in scene_params["bands"]
    ]
    _stats_worker = partial(_sentinel_stats, percentiles=(pmin, pmax), **kwargs)
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        responses = executor.map(_stats_worker, addresses)

    info["statistics"] = {
        b: v for b, d in zip(scene_params["bands"], responses) for k, v in d.items()
    }
    return info


def tile(
    sceneid, tile_x, tile_y, tile_z, bands=("04", "03", "02"), tilesize=256, **kwargs
):
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
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.utils._tile_read' function.

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    scene_params = _sentinel_parse_scene_id(sceneid)

    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in scene_params["valid_bands"]:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    preview_file = os.path.join(
        scene_params["aws_bucket"],
        scene_params["aws_prefix"],
        scene_params["preview_file"],
    )
    with rasterio.open(preview_file) as src:
        bounds = transform_bounds(src.crs, "epsg:4326", *src.bounds, densify_pts=21)

    if not utils.tile_exists(bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    path_prefix = os.path.join(scene_params["aws_bucket"], scene_params["aws_prefix"])
    if scene_params["processingLevel"] == "L2A":
        bands = [_l2_prefixed_band(b) for b in bands]
    else:
        bands = ["B{}".format(b) for b in bands]

    def _read_tile(path):
        with rasterio.open(path) as src_dst:
            return utils.tile_read(
                src_dst, bounds=tile_bounds, tilesize=tilesize, nodata=0, **kwargs
            )

    addresses = ["{}/{}.jp2".format(path_prefix, band) for band in bands]
    with futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(_read_tile, addresses)))
        mask = np.all(masks, axis=0).astype(np.uint8) * 255

    return np.concatenate(data), mask
