"""rio-tiler.io"""

from .base import BaseReader, MultiBandReader, MultiBaseReader  # noqa
from .rasterio import ImageReader, Reader  # noqa
from .stac import STACReader  # noqa
from .xarray import XarrayReader  # noqa

# Keep Compatibility with <4.0
COGReader = Reader
