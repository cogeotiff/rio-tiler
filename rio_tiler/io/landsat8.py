"""rio_tiler.io.landsat8: Landsat-8 processing."""

from typing import Any, Dict, Sequence, Tuple, Union

import os
import re
import datetime
from concurrent import futures

from urllib.request import urlopen

import numpy

import rasterio
from rasterio.warp import transform_bounds
from rio_toa import reflectance, brightness_temp, toa_utils

from rio_tiler import reader
from rio_tiler import constants
from rio_tiler.utils import _stats as raster_stats, tile_exists, pansharpening_brovey
from rio_tiler.errors import (
    TileOutsideBounds,
    InvalidBandName,
    InvalidLandsatSceneId,
)

LANDSAT_BANDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "QA"]


def landsat_parser(sceneid: str) -> Dict:
    """
    Parse Landsat-8 scene id.

    Author @perrygeo - http://www.perrygeo.com

    Attributes
    ----------
        sceneid : str
            Landsat sceneid.

    Returns
    -------
        out : dict
            dictionary with metadata constructed from the sceneid.

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

    for pattern in [collection_pattern, precollection_pattern]:
        match = re.match(pattern, sceneid, re.IGNORECASE)
        if match:
            meta: Dict[str, Any] = match.groupdict()
            break

    meta["scene"] = sceneid
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

    meta["scheme"] = "s3"
    meta["bucket"] = "landsat-pds"
    meta["prefix"] = os.path.join(collection, "L8", meta["path"], meta["row"], sceneid)

    return meta


def _landsat_get_mtl(sceneid: str) -> Dict:
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
    scene_params = landsat_parser(sceneid)
    meta_file = "http://{bucket}.s3.amazonaws.com/{prefix}/{scene}_MTL.txt".format(
        **scene_params
    )
    metadata = str(urlopen(meta_file).read().decode())
    return toa_utils._parse_mtl_txt(metadata)


def _convert(arr: numpy.ndarray, band: str, metadata: Dict) -> numpy.ndarray:
    """Convert DN to TOA or Temp."""
    if band in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # OLI
        multi_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            f"REFLECTANCE_MULT_BAND_{band}"
        )
        add_reflect = metadata["RADIOMETRIC_RESCALING"].get(
            f"REFLECTANCE_ADD_BAND_{band}"
        )
        sun_elev = metadata["IMAGE_ATTRIBUTES"]["SUN_ELEVATION"]

        arr = 10000 * reflectance.reflectance(
            arr, multi_reflect, add_reflect, sun_elev, src_nodata=0
        )

    elif band in ["10", "11"]:  # TIRS
        multi_rad = metadata["RADIOMETRIC_RESCALING"].get(f"RADIANCE_MULT_BAND_{band}")
        add_rad = metadata["RADIOMETRIC_RESCALING"].get(f"RADIANCE_ADD_BAND_{band}")
        k1 = metadata["TIRS_THERMAL_CONSTANTS"].get(f"K1_CONSTANT_BAND_{band}")
        k2 = metadata["TIRS_THERMAL_CONSTANTS"].get(f"K2_CONSTANT_BAND_{band}")

        arr = brightness_temp.brightness_temp(arr, multi_rad, add_rad, k1, k2)

    # TODO
    # elif band == "QA":

    return arr


def bounds(sceneid: str) -> Dict:
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
    meta: Dict = _landsat_get_mtl(sceneid)["L1_METADATA_FILE"]

    return dict(
        sceneid=sceneid,
        bounds=toa_utils._get_bounds_from_metadata(meta["PRODUCT_METADATA"]),
    )


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
            Landsat sceneid. For scenes after May 2017,
            sceneid have to be LANDSAT_PRODUCT_ID.
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
    scene_params = landsat_parser(sceneid)
    meta: Dict = _landsat_get_mtl(sceneid)["L1_METADATA_FILE"]

    landsat_prefix = "{scheme}://{bucket}/{prefix}/{scene}".format(**scene_params)

    def worker(band: str):
        asset = f"{landsat_prefix}_B{band}.TIF"

        if band == "QA":
            nodata = 1
            resamp = "nearest"
        else:
            nodata = 0
            resamp = "bilinear"

        with rasterio.open(asset) as src_dst:
            bounds = transform_bounds(
                src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
            )
            data, mask = reader.preview(
                src_dst, nodata=nodata, resampling_method=resamp, **kwargs
            )

        if band != "QA":
            data = data.astype("float32", casting="unsafe")
            data = _convert(data, band, meta)

        data = numpy.ma.array(data)
        data.mask = mask == 0

        statistics = raster_stats(data, percentiles=(pmin, pmax), **hist_options)
        return dict(bounds=bounds, statistics=statistics)

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        responses = list(executor.map(worker, LANDSAT_BANDS))

    info: Dict[str, Any] = dict(sceneid=sceneid)
    info["band_descriptions"] = [(ix + 1, b) for ix, b in enumerate(LANDSAT_BANDS)]
    info["bounds"] = [
        r["bounds"] for b, r in zip(LANDSAT_BANDS, responses) if b == "8"
    ][0]

    info["statistics"] = {b: d["statistics"] for b, d in zip(LANDSAT_BANDS, responses)}
    return info


def tile(
    sceneid: str,
    tile_x: int,
    tile_y: int,
    tile_z: int,
    bands: Union[Sequence[str], str] = ["4", "3", "2"],
    tilesize: int = 256,
    pan: bool = False,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.utils._tile_read' function.

    Returns
    -------
    data : numpy ndarray
    mask: numpy array

    """
    if isinstance(bands, str):
        bands = (bands,)

    for band in bands:
        if band not in LANDSAT_BANDS:
            raise InvalidBandName("{} is not a valid Landsat band name".format(band))

    scene_params = landsat_parser(sceneid)

    meta: Dict = _landsat_get_mtl(sceneid)["L1_METADATA_FILE"]

    landsat_prefix = "{scheme}://{bucket}/{prefix}/{scene}".format(**scene_params)

    bounds = toa_utils._get_bounds_from_metadata(meta["PRODUCT_METADATA"])
    if not tile_exists(bounds, tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            "Tile {}/{}/{} is outside image bounds".format(tile_z, tile_x, tile_y)
        )

    def worker(band: str):
        asset = f"{landsat_prefix}_B{band}.TIF"

        if band == "QA":
            nodata = 1
            resamp = "nearest"
        else:
            nodata = 0
            resamp = "bilinear"

        with rasterio.open(asset) as src_dst:
            tile, mask = reader.tile(
                src_dst,
                tile_x,
                tile_y,
                tile_z,
                tilesize=tilesize,
                nodata=nodata,
                resampling_method=resamp,
            )

        return tile, mask

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(worker, bands)))
        data = numpy.concatenate(data)
        mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255

        if pan:
            pan_data, mask = worker("8")
            data = pansharpening_brovey(data, pan_data, 0.2, pan_data.dtype)

        if bands[0] != "QA" or len(bands) != 1:
            data = data.astype("float32", casting="unsafe")
            for bdx, band in enumerate(bands):
                data[bdx] = _convert(data[bdx], band, meta)

        return data, mask
