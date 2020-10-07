"""rio-tiler TMS."""

from collections import namedtuple
from typing import Dict, Type

import mercantile
from rasterio.crs import CRS
from rasterio.transform import from_bounds

from .constants import WEB_MERCATOR_CRS
from .mercator import zoom_for_pixelsize

try:
    import morecantile
    from morecantile import Tile, TileMatrixSet

    default_tms = morecantile.tms.get("WebMercatorQuad")  # noqa

except ImportError:

    Tile = namedtuple("Tile", ["x", "y", "z"])  # type: ignore
    CoordsBbox = namedtuple("CoordsBbox", ["xmin", "ymin", "xmax", "ymax"])
    Coords = namedtuple("Coords", ["x", "y"])

    class WebMercatorQuad:
        """TileMatrixSet like object for WebMercator TMS."""

        @property
        def crs(self) -> CRS:
            """crs."""
            return WEB_MERCATOR_CRS

        def xy_bounds(self, *tile: Tile) -> CoordsBbox:
            """Return the bounding box of the (x, y, z) tile in WebMercator projection."""
            return mercantile.xy_bounds(*tile)

        def bounds(self, *tile: Tile) -> CoordsBbox:
            """Return the bounding box of the (x, y, z) tile in WGS84 projection."""
            return mercantile.bounds(*tile)

        def zoom_for_res(self, res: float, max_z: int = 24) -> int:
            """Get TMS zoom level corresponding to a specific resolution."""
            return zoom_for_pixelsize(res, max_z, tilesize=256)

    TileMatrixSet = Type[WebMercatorQuad]  # type: ignore

    default_tms = WebMercatorQuad()  # noqa


def geotiff_options(
    x: int, y: int, z: int, tilesize: int = 256, tms: TileMatrixSet = default_tms,
) -> Dict:
    """GeoTIFF options."""
    bounds = tms.xy_bounds(morecantile.Tile(x=x, y=y, z=z))
    dst_transform = from_bounds(*bounds, tilesize, tilesize)
    return dict(crs=tms.crs, transform=dst_transform)
