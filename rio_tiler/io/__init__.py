"""rio-tiler.io"""

from .base import AsyncBaseReader, BaseReader, MultiBandReader, MultiBaseReader
from .rasterio import ImageReader, Reader
from .stac import STACReader
from .xarray import XarrayReader

# Keep Compatibility with <4.0
COGReader = Reader

__all__ = [
    "AsyncBaseReader",
    "BaseReader",
    "MultiBandReader",
    "MultiBaseReader",
    "ImageReader",
    "Reader",
    "STACReader",
    "XarrayReader",
    "COGReader",
]
