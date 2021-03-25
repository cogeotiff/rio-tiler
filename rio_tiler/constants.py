"""rio-tiler constant values."""

import multiprocessing
import os
from typing import Sequence, Tuple, Union

import morecantile
from rasterio.crs import CRS

NumType = Union[float, int]
BBox = Tuple[float, float, float, float]
ColorTuple = Tuple[int, int, int, int]
NoData = Union[float, int, str]
Indexes = Union[Sequence[int], int]

MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))

WEB_MERCATOR_CRS = CRS.from_epsg(3857)
WGS84_CRS = CRS.from_epsg(4326)

WEB_MERCATOR_TMS = morecantile.tms.get("WebMercatorQuad")
