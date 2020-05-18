"""rio_tiler.cbers: cbers processing."""

from typing import Any, Dict, Sequence, Tuple, Union

import re

import numpy

import rasterio
from rasterio.warp import transform_bounds

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.utils import tile_exists
from rio_tiler.errors import TileOutsideBounds, InvalidBandName, InvalidCBERSSceneId


def cbers_parser(sceneid: str) -> Dict:
    """Parse CBERS scene id.

    Attributes
    ----------
        sceneid : str
            CBERS sceneid.

    Returns
    -------
        out : dict
            dictionary with metadata constructed from the sceneid.

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

    meta: Dict[str, Any] = re.match(cbers_pattern, sceneid, re.IGNORECASE).groupdict()
    meta["scene"] = sceneid

    instrument = meta["instrument"]
    instrument_params = {
        "MUX": {
            "reference_band": "6",
            "bands": ("5", "6", "7", "8"),
            "rgb": ("7", "6", "5"),
        },
        "AWFI": {
            "reference_band": "14",
            "bands": ("13", "14", "15", "16"),
            "rgb": ("15", "14", "13"),
        },
        "PAN10M": {
            "reference_band": "4",
            "bands": ("2", "3", "4"),
            "rgb": ("3", "4", "2"),
        },
        "PAN5M": {"reference_band": "1", "bands": ("1"), "rgb": ("1", "1", "1")},
    }
    meta["reference_band"] = instrument_params[instrument]["reference_band"]
    meta["bands"] = instrument_params[instrument]["bands"]
    meta["rgb"] = instrument_params[instrument]["rgb"]

    meta["scheme"] = "s3"
    meta["bucket"] = "cbers-pds"
    meta["prefix"] = "CBERS4/{instrument}/{path}/{row}/{scene}".format(**meta)

    return meta


def bounds(sceneid: str) -> Dict:
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
    scene_params = cbers_parser(sceneid)
    cbers_prefix = "{scheme}://{bucket}/{prefix}/{scene}".format(**scene_params)

    with rasterio.open(
        "{}_BAND{}.tif".format(cbers_prefix, scene_params["reference_band"])
    ) as src:
        bounds = transform_bounds(
            src.crs, constants.WGS84_CRS, *src.bounds, densify_pts=21
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
    Return band bounds and statistics.

    Attributes
    ----------
        sceneid : str
            CBERS sceneid.
        pmin : int, optional, (default: 2)
            Histogram minimum cut.
        pmax : int, optional, (default: 98)
            Histogram maximum cut.
        hist_options : dict, optional
            Options to forward to numpy.histogram function.
            e.g: {bins=20, range=(0, 1000)}
        kwargs : optional
            These are passed to 'rio_tiler.reader.preview'

    Returns
    -------
        out : dict
            Dictionary with bounds and bands statistics.

    """
    scene_params = cbers_parser(sceneid)
    cbers_prefix = "{scheme}://{bucket}/{prefix}/{scene}".format(**scene_params)

    bands = scene_params["bands"]
    addresses = [f"{cbers_prefix}_BAND{band}.tif" for band in bands]

    responses = reader.multi_metadata(
        addresses,
        indexes=[1],
        nodata=0,
        percentiles=(pmin, pmax),
        hist_options=hist_options,
        **kwargs,
    )

    info: Dict[str, Any] = dict(sceneid=sceneid)
    info["instrument"] = scene_params["instrument"]
    info["band_descriptions"] = [(ix + 1, b) for ix, b in enumerate(bands)]

    info["bounds"] = [
        r["bounds"]
        for b, r in zip(bands, responses)
        if b == scene_params["reference_band"]
    ][0]
    info["statistics"] = {b: d["statistics"][1] for b, d in zip(bands, responses)}
    return info


def tile(
    sceneid: str,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = None,
    tilesize: int = 256,
    **kwargs: Dict,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
        bands : tuple or list or str, optional
            Bands index for the RGB combination. If None uses default
            defined for the instrument
        tilesize : int, optional
            Output image size. Default is 256
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.tile' function.

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    if isinstance(bands, str):
        bands = (bands,)

    scene_params = cbers_parser(sceneid)

    if not bands:
        bands = scene_params["rgb"]

    for band in bands:
        if band not in scene_params["bands"]:
            raise InvalidBandName(
                "{} is not a valid band name for {} CBERS instrument".format(
                    band, scene_params["instrument"]
                )
            )

    cbers_prefix = "{scheme}://{bucket}/{prefix}/{scene}".format(**scene_params)
    with rasterio.open(
        "{}_BAND{}.tif".format(cbers_prefix, scene_params["reference_band"])
    ) as src_dst:
        bounds = transform_bounds(
            src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
        )

    if not tile_exists(bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    addresses = [f"{cbers_prefix}_BAND{band}.tif" for band in bands]
    return reader.multi_tile(
        addresses, tile_x, tile_y, tile_z, tilesize=tilesize, nodata=0
    )
