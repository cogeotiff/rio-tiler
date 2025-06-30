"""rio-tiler.io"""

from .base import BaseReader, MultiBandReader, MultiBaseReader  # noqa
from .rasterio import ImageReader, Reader  # noqa
from .stac import STACReader  # noqa
from .xarray import DataArrayReader, DatasetReader  # noqa

# Keep Compatibility with <8.0
XarrayReader = DataArrayReader

# Keep Compatibility with <4.0
COGReader = Reader
