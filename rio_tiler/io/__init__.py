"""rio-tiler.io"""

from .base import BaseReader, MultiBandReader, MultiBaseReader
from .rasterio import ImageReader, Reader
from .stac import STACReader
from .xarray import XarrayReader

# Keep Compatibility with <4.0
COGReader = Reader

__all__ = [
    "BaseReader",
    "MultiBandReader",
    "MultiBaseReader",
    "ImageReader",
    "Reader",
    "STACReader",
    "XarrayReader",
    "COGReader",
]
