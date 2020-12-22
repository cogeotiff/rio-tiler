"""rio-tiler constant values."""

import multiprocessing
import os
from typing import Tuple, Union

import morecantile
from rasterio.crs import CRS

NumType = Union[float, int]
BBox = Tuple[float, float, float, float]
ColorTuple = Tuple[int, int, int, int]

MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))

WEB_MERCATOR_CRS = CRS.from_epsg(3857)
WEB_MERCATOR_OPP_CRS = CRS.from_string(
    '+proj=merc +lon_0=180 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 "\
    "+towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
)
WEB_MERCATOR_COORD_WIDTH = 20026376.39 * 2

WGS84_CRS = CRS.from_epsg(4326)
WGS84_COORD_LEFT = -180
WGS84_COORD_RIGHT = 180
WGS84_COORD_WIDTH = WGS84_COORD_RIGHT - WGS84_COORD_LEFT

WEB_MERCATOR_TMS = morecantile.tms.get("WebMercatorQuad")
