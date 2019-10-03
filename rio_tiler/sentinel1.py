"""rio_tiler.sentinel1: Sentinel-1 processing."""

import os
import re
import json
from functools import partial
from concurrent import futures

import numpy

from boto3.session import Session as boto3_session

import mercantile

import rasterio
from rasterio.vrt import WarpedVRT
from rasterio import transform

from rio_tiler import utils
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidSentinelSceneId

REGION = os.environ.get("AWS_REGION", "eu-central-1")
SENTINEL_BUCKET = "s3://sentinel-s1-l1c"
SENTINEL_BANDS = ["vv", "vh"]


def _aws_get_object(bucket, key, request_pays=True, client=None):
    """AWS s3 get object content."""
    if not client:
        session = boto3_session(region_name=REGION)
        client = session.client("s3")

    params = {"Bucket": bucket, "Key": key}
    if request_pays:
        params["RequestPayer"] = "requester"
    response = client.get_object(**params)
    return response["Body"].read()


def _sentinel_parse_scene_id(sceneid):
    """Parse Sentinel-1 scene id.

    Attributes
    ----------
    sceneid : str
        Sentinel-1 sceneid.

    Returns
    -------
    out : dict
        dictionary with metadata constructed from the sceneid.

        e.g:
        _sentinel_parse_scene_id('S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B')
        {
            "sensor": "1",
            "satellite": "A",
            "beam": "IW",
            "product": "GRD",
            "resolution": "H",
            "processing_level": "1",
            "product_class": "S",
            "polarisation": "DV",
            "startDateTime": "20180716T004042",
            "stopDateTime": "20180716T004107",
            "absolute_orbit": "022812",
            "mission_task": "02792A",
            "product_id": "FD5B",
            "key": "GRD/2018/7/16/IW/DV/S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B",
            "scene": "S1A_IW_GRDH_1SDV_20180716T004042_20180716T004107_022812_02792A_FD5B",
        }

    """
    if not re.match(
        "^S1[AB]_(IW)|(EW)_[A-Z]{3}[FHM]_[0-9][SA][A-Z]{2}_[0-9]{8}T[0-9]{6}_[0-9]{8}T[0-9]{6}_[0-9A-Z]{6}_[0-9A-Z]{6}_[0-9A-Z]{4}$",
        sceneid,
    ):
        raise InvalidSentinelSceneId("Could not match {}".format(sceneid))

    sentinel_pattern = (
        r"^S"
        r"(?P<sensor>\w{1})"
        r"(?P<satellite>[AB]{1})"
        r"_"
        r"(?P<beam>[A-Z]{2})"
        r"_"
        r"(?P<product>[A-Z]{3})"
        r"(?P<resolution>[FHM])"
        r"_"
        r"(?P<processing_level>[0-9])"
        r"(?P<product_class>[SA])"
        r"(?P<polarisation>(SH)|(SV)|(DH)|(DV)|(HH)|(HV)|(VV)|(VH))"
        r"_"
        r"(?P<startDateTime>[0-9]{8}T[0-9]{6})"
        r"_"
        r"(?P<stopDateTime>[0-9]{8}T[0-9]{6})"
        r"_"
        r"(?P<absolute_orbit>[0-9]{6})"
        r"_"
        r"(?P<mission_task>[0-9A-Z]{6})"
        r"_"
        r"(?P<product_id>[0-9A-Z]{4})$"
    )

    meta = re.match(sentinel_pattern, sceneid, re.IGNORECASE).groupdict()
    year = meta["startDateTime"][0:4]
    month = meta["startDateTime"][4:6].strip("0")
    day = meta["startDateTime"][6:8].strip("0")
    meta["key"] = "{}/{}/{}/{}/{}/{}/{}".format(
        meta["product"], year, month, day, meta["beam"], meta["polarisation"], sceneid
    )

    meta["scene"] = sceneid

    return meta


def _get_bounds(scene_info):
    bucket = SENTINEL_BUCKET.replace("s3://", "")
    product_info = json.loads(
        _aws_get_object(bucket, "{}/productInfo.json".format(scene_info["key"]))
    )
    geom = product_info["footprint"]
    xyz = list(zip(*geom["coordinates"][0]))
    return min(xyz[0]), min(xyz[1]), max(xyz[0]), max(xyz[1])


def bounds(sceneid):
    """
    Retrieve image bounds.

    Attributes
    ----------
    sceneid : str
        Sentinel-1 sceneid.

    Returns
    -------
    out : dict
        dictionary with image bounds.

    """
    scene_params = _sentinel_parse_scene_id(sceneid)
    return {"sceneid": sceneid, "bounds": list(_get_bounds(scene_params))}


def metadata(sceneid, pmin=2, pmax=98, bands=None, **kwargs):
    """
    Retrieve image bounds and band statistics.

    Attributes
    ----------
    sceneid : str
        Sentinel-1 sceneid.
    pmin : int, optional, (default: 2)
        Histogram minimum cut.
    pmax : int, optional, (default: 98)
        Histogram maximum cut.
    bands: tuple, str, required
        Bands name (e.g vv, vh).
    kwargs : optional
        These are passed to 'rio_tiler.sentinel1._stats'
        e.g: histogram_bins=20'

    Returns
    -------
    out : dict
        Dictionary with image bounds and bands statistics.

    """
    if not bands:
        raise InvalidBandName("bands is required")

    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in SENTINEL_BANDS:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    scene_params = _sentinel_parse_scene_id(sceneid)
    sentinel_address = "{}/{}/measurement".format(SENTINEL_BUCKET, scene_params["key"])

    addresses = [
        "{}/{}-{}.tiff".format(sentinel_address, scene_params["beam"].lower(), band)
        for band in bands
    ]

    def _s1_metadata(src_path, percentiles, **kwarg):
        with rasterio.open(src_path) as src_dst:
            with WarpedVRT(
                src_dst,
                src_crs=src_dst.gcps[1],
                src_transform=transform.from_gcps(src_dst.gcps[0]),
                src_nodata=0,
            ) as vrt_dst:
                return utils.raster_get_stats(vrt_dst, percentiles=percentiles, **kwarg)

    _stats_worker = partial(_s1_metadata, percentiles=(pmin, pmax), **kwargs)
    with futures.ThreadPoolExecutor() as executor:
        responses = list(executor.map(_stats_worker, addresses))

    info = {
        "sceneid": sceneid,
        "bounds": responses[0]["bounds"],
        "minzoom": responses[0]["minzoom"],
        "maxzoom": responses[0]["maxzoom"],
    }

    info["statistics"] = {
        b: v for b, d in zip(bands, responses) for k, v in d["statistics"].items()
    }
    return info


def tile(sceneid, tile_x, tile_y, tile_z, bands=None, tilesize=256, **kwargs):
    """
    Create mercator tile from Sentinel-1 data.

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
    bands: tuple, str, required
        Bands name (e.g vv, vh).
    tilesize : int, optional (default: 256)
        Output image size.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    if not bands:
        raise InvalidBandName("bands is required")

    if not isinstance(bands, tuple):
        bands = tuple((bands,))

    for band in bands:
        if band not in SENTINEL_BANDS:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    scene_params = _sentinel_parse_scene_id(sceneid)
    sentinel_address = "{}/{}/measurement".format(SENTINEL_BUCKET, scene_params["key"])

    mercator_tile = mercantile.Tile(x=tile_x, y=tile_y, z=tile_z)
    tile_bounds = mercantile.xy_bounds(mercator_tile)

    addresses = [
        "{}/{}-{}.tiff".format(sentinel_address, scene_params["beam"].lower(), band)
        for band in bands
    ]

    def _s1_tiler(src_path):
        with rasterio.open(src_path) as src_dst:
            with WarpedVRT(
                src_dst,
                src_crs=src_dst.gcps[1],
                src_transform=transform.from_gcps(src_dst.gcps[0]),
                src_nodata=0,
            ) as vrt_dst:
                if not utils.tile_exists(vrt_dst.bounds, tile_z, tile_x, tile_y):
                    raise TileOutsideBounds(
                        "Tile {}/{}/{} is outside image bounds".format(
                            tile_z, tile_x, tile_y
                        )
                    )

                return utils._tile_read(vrt_dst, bounds=tile_bounds, tilesize=tilesize)

    with futures.ThreadPoolExecutor() as executor:
        data, masks = zip(*list(executor.map(_s1_tiler, addresses)))
        mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255

    return numpy.concatenate(data), mask
