"""rio-tiler types."""

from collections.abc import Sequence
from typing import Any, Literal, TypedDict

import numpy

NumType = float | int

BBox = tuple[float, float, float, float]
NoData = float | int | str
Indexes = Sequence[int] | int

DataMaskType = tuple[numpy.ndarray, numpy.ndarray]

ColorTuple = tuple[int, int, int, int]  # (red, green, blue, alpha)
IntervalTuple = tuple[NumType, NumType]  # (0, 100)

# ColorMap Dict: {1: (0, 0, 0, 255), ...}
GDALColorMapType = dict[int, ColorTuple]

# Discrete Colormap, like GDALColorMapType but accept Float: {0.1: (0, 0, 0, 255), ...}
DiscreteColorMapType = dict[NumType, ColorTuple]

# Intervals ColorMap: [((0, 1), (0, 0, 0, 0)), ...]
IntervalColorMapType = Sequence[tuple[IntervalTuple, ColorTuple]]

ColorMapType = GDALColorMapType | DiscreteColorMapType | IntervalColorMapType

# RasterIO() resampling method.
# ref: https://gdal.org/api/raster_c_api.html#_CPPv418GDALRIOResampleAlg
RIOResampling = Literal[
    "nearest",
    "bilinear",
    "cubic",
    "cubic_spline",
    "lanczos",
    "average",
    "mode",
    "gauss",
    "rms",
]

# WarpKernel resampling method.
# ref: https://gdal.org/en/stable/api/gdalwarp_cpp.html#_CPPv415GDALResampleAlg
WarpResampling = Literal[
    "nearest",
    "bilinear",
    "cubic",
    "cubic_spline",
    "lanczos",
    "average",
    "mode",
    "max",
    "min",
    "med",
    "q1",
    "q3",
    "sum",
    "rms",
]


class AssetInfo(TypedDict, total=False):
    """Asset Reader Options."""

    url: Any
    media_type: str
    env: dict | None
    metadata: dict | None
    dataset_statistics: Sequence[tuple[float, float]] | None
