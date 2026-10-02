"""rio-tiler types."""

import sys
from collections.abc import Sequence
from typing import Any, Literal, NotRequired

import numpy

if sys.version_info >= (3, 15):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


NumType = float | int

BBox = tuple[float, float, float, float]
NoData = float | int | str
Indexes = Sequence[int] | int

DataMaskType = tuple[numpy.ndarray, numpy.ndarray]

ColorTuple = tuple[int, int, int, int]  # (red, green, blue, alpha)
IntervalTuple = tuple[NumType, NumType]  # (0, 100)

GDALColorMapType = dict[int, ColorTuple]
"""Continuous ColorMap Dict.

Expects 255 values, or it will be interpreted as a DiscreteColorMap.

Example:
    `{1: (0, 0, 0, 255), ...}`
"""


DiscreteColorMapType = dict[NumType, ColorTuple]
"""Discrete ColorMap, like GDALColorMapType but accept Float.

Matches only exact values for categorical data.

Example:
    `{0.1: (0, 0, 0, 255), ...}`
"""

IntervalColorMapType = Sequence[tuple[IntervalTuple, ColorTuple]]
"""Intervals ColorMap.

Example:
    `[((0, 1), (0, 0, 0, 0)), ...]`
"""

ColorMapType = GDALColorMapType | DiscreteColorMapType | IntervalColorMapType

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
"""RasterIO() resampling method.

ref: <https://gdal.org/api/raster_c_api.html#_CPPv418GDALRIOResampleAlg>
"""

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
"""WarpKernel resampling method.

ref: <https://gdal.org/en/stable/api/gdalwarp_cpp.html#_CPPv415GDALResampleAlg>
"""


class AssetWithOptions(TypedDict, extra_items=True):  # type: ignore[call-arg]
    """Asset with additional options."""

    name: str
    indexes: NotRequired[Indexes]
    expression: NotRequired[str]
    bands: NotRequired[Sequence[str]]


AssetType = str | AssetWithOptions


class AssetInfo(TypedDict):
    """Asset Reader Options."""

    url: Any
    name: str
    media_type: str | None
    reader_options: dict
    method_options: dict
    env: NotRequired[dict]
    metadata: NotRequired[dict]
    dataset_statistics: NotRequired[Sequence[tuple[float, float]]]
