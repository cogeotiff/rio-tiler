"""rio_tiler.io.sentinel1: Sentinel-1 processing."""

from typing import Any, Dict, Sequence, Tuple, Union

import os
import re
import json
from concurrent import futures

import numpy

from boto3.session import Session as boto3_session

import rasterio
from rasterio import transform
from rasterio.vrt import WarpedVRT

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.errors import InvalidBandName, InvalidSentinelSceneId

REGION = os.environ.get("AWS_REGION", "eu-central-1")
SENTINEL_BANDS = ["vv", "vh"]


def _aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = True,
    client: boto3_session.client = None,
) -> bytes:
    """AWS s3 get object content."""
    if not client:
        session = boto3_session(region_name=REGION)
        client = session.client("s3")

    params = {"Bucket": bucket, "Key": key}
    if request_pays:
        params["RequestPayer"] = "requester"

    response = client.get_object(**params)

    return response["Body"].read()


def sentinel1_parser(sceneid: str) -> Dict:
    """
    Parse Sentinel-1 scene id.

    Attributes
    ----------
        sceneid : str
            Sentinel-1 sceneid.

    Returns
    -------
        out : dict
            dictionary with metadata constructed from the sceneid.

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

    meta: Dict[str, Any] = re.match(
        sentinel_pattern, sceneid, re.IGNORECASE
    ).groupdict()

    meta["scene"] = sceneid
    year = meta["startDateTime"][0:4]
    month = meta["startDateTime"][4:6].strip("0")
    day = meta["startDateTime"][6:8].strip("0")

    meta["scheme"] = "s3"
    meta["bucket"] = "sentinel-s1-l1c"
    meta["prefix"] = os.path.join(
        meta["product"], year, month, day, meta["beam"], meta["polarisation"], sceneid
    )

    return meta


def _get_bounds(scene_info: Dict) -> Tuple[float, float, float, float]:
    bucket, prefix = scene_info["bucket"], scene_info["prefix"]
    product_info = json.loads(_aws_get_object(bucket, f"{prefix}/productInfo.json"))

    xyz = list(zip(*product_info["footprint"]["coordinates"][0]))
    return min(xyz[0]), min(xyz[1]), max(xyz[0]), max(xyz[1])


def bounds(sceneid: str) -> Dict:
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
    scene_params = sentinel1_parser(sceneid)
    return dict(sceneid=sceneid, bounds=_get_bounds(scene_params))


def metadata(
    sceneid: str,
    pmin: float = 2.0,
    pmax: float = 98.0,
    bands: Union[Sequence[str], str] = None,
    hist_options: Dict = {},
    **kwargs,
) -> Dict:
    """
    Retrieve image bounds and band statistics.

    Attributes
    ----------
        sceneid : str
            Sentinel-1 sceneid.
        pmin : float, optional, (default: 2.)
            Histogram minimum cut.
        pmax : float, optional, (default: 98.)
            Histogram maximum cut.
        bands: tuple, str, required
            Bands name (e.g vv, vh).
        kwargs : optional
            These are passed to 'rio_tiler.utils._stats'
            e.g: bins=20, range=(0, 1000)

    Returns
    -------
        out : dict
            Dictionary with image bounds and bands statistics.

    """
    if not bands:
        raise InvalidBandName("bands is required")

    if isinstance(bands, str):
        bands = (bands,)

    for band in bands:
        if band not in SENTINEL_BANDS:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    scene_params = sentinel1_parser(sceneid)
    sentinel_prefix = "{scheme}://{bucket}/{prefix}/measurement".format(**scene_params)

    def worker(band: str):
        asset = "{}/{}-{}.tiff".format(
            sentinel_prefix, scene_params["beam"].lower(), band
        )
        with rasterio.open(asset) as src_dst:
            with WarpedVRT(
                src_dst,
                src_crs=src_dst.gcps[1],
                src_transform=transform.from_gcps(src_dst.gcps[0]),
                src_nodata=0,
            ) as vrt_dst:
                return reader.metadata(
                    vrt_dst,
                    percentiles=(pmin, pmax),
                    hist_options=hist_options,
                    **kwargs,
                )

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        responses = list(executor.map(worker, bands))

    info = dict(
        sceneid=sceneid,
        bounds=responses[0]["bounds"],
        band_descriptions=[(ix + 1, b) for ix, b in enumerate(bands)],
    )

    info["statistics"] = {
        b: v for b, d in zip(bands, responses) for _, v in d["statistics"].items()
    }
    return info


def tile(
    sceneid: str,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = None,
    tilesize: int = 256,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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

    if isinstance(bands, str):
        bands = (bands,)

    for band in bands:
        if band not in SENTINEL_BANDS:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    scene_params = sentinel1_parser(sceneid)
    sentinel_prefix = "{scheme}://{bucket}/{prefix}/measurement".format(**scene_params)

    def worker(band: str):
        asset = "{}/{}-{}.tiff".format(
            sentinel_prefix, scene_params["beam"].lower(), band
        )
        with rasterio.open(asset) as src_dst:
            with WarpedVRT(
                src_dst,
                src_crs=src_dst.gcps[1],
                src_transform=transform.from_gcps(src_dst.gcps[0]),
                src_nodata=0,
            ) as vrt_dst:
                return reader.tile(
                    vrt_dst, tile_x, tile_y, tile_z, tilesize=tilesize, **kwargs
                )

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(worker, bands)))
        data = numpy.concatenate(data)
        mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255

    return data, mask
