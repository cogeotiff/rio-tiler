"""rio-tiler types."""

from typing import Any, Dict, Literal, Optional, Sequence, Tuple, TypedDict, Union

import numpy

NumType = Union[float, int]

BBox = Tuple[float, float, float, float]
NoData = Union[float, int, str]
Indexes = Union[Sequence[int], int]

DataMaskType = Tuple[numpy.ndarray, numpy.ndarray]

ColorTuple = Tuple[int, int, int, int]  # (red, green, blue, alpha)
IntervalTuple = Tuple[NumType, NumType]  # (0, 100)

# ColorMap Dict: {1: (0, 0, 0, 255), ...}
GDALColorMapType = Dict[int, ColorTuple]

# Discrete Colormap, like GDALColorMapType but accept Float: {0.1: (0, 0, 0, 255), ...}
DiscreteColorMapType = Dict[NumType, ColorTuple]

# Intervals ColorMap: [((0, 1), (0, 0, 0, 0)), ...]
IntervalColorMapType = Sequence[Tuple[IntervalTuple, ColorTuple]]

ColorMapType = Union[
    GDALColorMapType,
    DiscreteColorMapType,
    IntervalColorMapType,
]

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
# ref: https://gdal.org/api/gdalwarp_cpp.html#_CPPv4N14GDALWarpKernel9eResampleE
WarpResampling = Literal[
    "nearest",
    "bilinear",
    "cubic",
    "cubic_spline",
    "lanczos",
    "average",
    "mode",
    "sum",
    "rms",
]


class AssetInfo(TypedDict, total=False):
    """Asset Reader Options."""

    url: Any
    media_type: str
    env: Optional[Dict]
    metadata: Optional[Dict]
    dataset_statistics: Optional[Sequence[Tuple[float, float]]]
