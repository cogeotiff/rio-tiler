"""rio_tiler.reader.sentinel2: Sentinel-2 processing."""

from typing import Any, Dict, Sequence, Tuple, Union

import os
import re
import itertools
from collections import OrderedDict

import numpy

import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.utils import tile_exists
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidSentinelSceneId


SENTINEL_L1_BANDS = OrderedDict(
    [
        ("10", ["02", "03", "04", "08"]),
        ("20", ["05", "06", "07", "11", "12", "8A"]),
        ("60", ["01", "09", "10"]),
    ]
)

SENTINEL_L2_BANDS = OrderedDict(
    [
        ("10", ["02", "03", "04", "08"]),
        ("20", ["02", "03", "04", "05", "06", "07", "08", "11", "12", "8A"]),
        (
            "60",
            ["01", "02", "03", "04", "05", "06", "07", "08", "09", "11", "12", "8A"],
        ),
    ]
)

SENTINEL_L2_PRODUCTS = OrderedDict(
    [
        ("10", ["AOT", "WVP"]),
        ("20", ["AOT", "SCL", "WVP"]),
        ("60", ["AOT", "SCL", "WVP"]),
    ]
)


def sentinel2_parser(sceneid: str) -> Dict:
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

    """

    if not re.match("^S2[AB]_L[0-2][A-C]_[0-9]{8}_[0-9]{2}[A-Z]{3}_[0-9]$", sceneid):
        raise InvalidSentinelSceneId("Could not match {}".format(sceneid))

    sentinel_pattern = (
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

    meta: Dict[str, Any] = re.match(
        sentinel_pattern, sceneid, re.IGNORECASE
    ).groupdict()
    meta["scene"] = sceneid

    utm_zone = meta["utm"].lstrip("0")
    grid_square = meta["sq"]
    latitude_band = meta["lat"]
    year = meta["acquisitionYear"]
    month = meta["acquisitionMonth"].lstrip("0")
    day = meta["acquisitionDay"].lstrip("0")
    img_num = meta["num"]

    meta["scheme"] = "s3"
    meta["bucket"] = "sentinel-s2-" + meta["processingLevel"].lower()
    meta["prefix"] = os.path.join(
        "tiles", utm_zone, latitude_band, grid_square, year, month, day, img_num
    )

    if meta["processingLevel"] == "L1C":
        meta["preview_file"] = "preview.jp2"
        meta["preview_prefix"] = ""
        meta["bands"] = list(
            itertools.chain.from_iterable(
                [bands for _, bands in SENTINEL_L1_BANDS.items()]
            )
        )
        meta["valid_bands"] = meta["bands"]
    else:
        meta["preview_file"] = "R60m/TCI.jp2"
        meta["preview_prefix"] = "R60m"
        meta["bands"] = SENTINEL_L2_BANDS["60"]
        meta["valid_bands"] = meta["bands"] + SENTINEL_L2_PRODUCTS["60"]

    return meta


def _l2_prefixed_band(band: str) -> str:
    """Return L2A prefixed bands name."""
    if band in SENTINEL_L2_BANDS["60"]:
        for res, bands in SENTINEL_L2_BANDS.items():
            if band in bands:
                return "R{}m/B{}".format(res, band)
    elif band in SENTINEL_L2_PRODUCTS["60"]:
        for res, bands in SENTINEL_L2_PRODUCTS.items():
            if band in bands:
                return "R{}m/{}".format(res, band)

    raise InvalidBandName("{} is not a valid Sentinel band name".format(band))


def bounds(sceneid: str) -> Dict:
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
    scene_params = sentinel2_parser(sceneid)
    preview_file = "{scheme}://{bucket}/{prefix}/{preview_file}".format(**scene_params)
    with rasterio.open(preview_file) as src_dst:
        bounds = transform_bounds(
            src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
        )

    return dict(sceneid=sceneid, bounds=bounds)


def metadata(
    sceneid: str,
    pmin: float = 2.0,
    pmax: float = 98.0,
    hist_options: Dict = {},
    **kwargs: Any,
) -> Dict:
    """
    Retrieve image bounds and band statistics.

    Attributes
    ----------
        sceneid : str
            Sentinel-2 sceneid.
        pmin : float, optional, (default: 2.)
            Histogram minimum cut.
        pmax : float, optional, (default: 98.)
            Histogram maximum cut.
        hist_options : dict, optional
            Options to forward to numpy.histogram function.
            e.g: {bins=20, range=(0, 1000)}
        kwargs : optional
            These are passed to 'rio_tiler.reader.preview'

    Returns
    -------
        out : dict
            Dictionary with image bounds and bands statistics.

    """
    scene_params = sentinel2_parser(sceneid)
    sentinel_prefix = "{scheme}://{bucket}/{prefix}/{preview_prefix}".format(
        **scene_params
    )
    bands = scene_params["bands"]

    addresses = [f"{sentinel_prefix}/B{band}.jp2" for band in bands]

    responses = reader.multi_metadata(
        addresses,
        indexes=[1],
        nodata=0,
        percentiles=(pmin, pmax),
        hist_options=hist_options,
        **kwargs,
    )
    info: Dict[str, Any] = dict(sceneid=sceneid)
    info["band_descriptions"] = [(ix + 1, b) for ix, b in enumerate(bands)]
    info["bounds"] = responses[0]["bounds"]
    info["statistics"] = {
        b: v for b, d in zip(bands, responses) for k, v in d["statistics"].items()
    }
    return info


def tile(
    sceneid: str,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = ("04", "03", "02"),
    tilesize: int = 256,
    **kwargs: Dict,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
    if isinstance(bands, str):
        bands = (bands,)

    scene_params = sentinel2_parser(sceneid)
    for band in bands:
        if band not in scene_params["valid_bands"]:
            raise InvalidBandName("{} is not a valid Sentinel band name".format(band))

    sentinel_prefix = "{scheme}://{bucket}/{prefix}".format(**scene_params)

    preview_file = os.path.join(sentinel_prefix, scene_params["preview_file"])
    with rasterio.open(preview_file) as src:
        bounds = transform_bounds(
            src.crs, constants.WGS84_CRS, *src.bounds, densify_pts=21
        )
        if not tile_exists(bounds, tile_z, tile_x, tile_y):
            raise TileOutsideBounds(
                "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
            )

    if scene_params["processingLevel"] == "L2A":
        bands = [_l2_prefixed_band(b) for b in bands]
    else:
        bands = ["B{}".format(b) for b in bands]

    addresses = [f"{sentinel_prefix}/{band}.jp2" for band in bands]
    return reader.multi_tile(
        addresses, tile_x, tile_y, tile_z, tilesize=tilesize, nodata=0
    )
