"""rio-tiler types."""

from typing import Dict, Optional, Sequence, Tuple, TypedDict, Union

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

# Intervals ColorMap: [((0, 1), (0, 0, 0, 0)), ...]
IntervalColorMapType = Sequence[Tuple[IntervalTuple, ColorTuple]]

ColorMapType = Union[
    GDALColorMapType,
    IntervalColorMapType,
]


class AssetInfo(TypedDict, total=False):
    """Asset Reader Options."""

    url: str
    env: Optional[Dict]
