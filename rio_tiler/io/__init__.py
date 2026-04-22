"""rio-tiler.io"""

from .base import (
    AsyncBaseReader,
    AsyncMultiBaseReader,
    BaseReader,
    MultiBandReader,
    MultiBaseReader,
)
from .rasterio import ImageReader, Reader
from .stac import AsyncSTACReader, STACReader
from .xarray import XarrayReader

# Keep Compatibility with <4.0
COGReader = Reader

__all__ = [
    "AsyncBaseReader",
    "AsyncMultiBaseReader",
    "AsyncSTACReader",
    "BaseReader",
    "MultiBandReader",
    "MultiBaseReader",
    "ImageReader",
    "Reader",
    "STACReader",
    "XarrayReader",
    "COGReader",
]
