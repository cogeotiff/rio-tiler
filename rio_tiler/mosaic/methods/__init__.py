"""rio-tiler.mosaic.methods: Mosaic filling methods."""

from enum import Enum

from .defaults import (
    CountMethod,
    FirstMethod,
    HighestMethod,
    LastBandHighMethod,
    LastBandLowMethod,
    LowestMethod,
    MeanMethod,
    MedianMethod,
    StdevMethod,
)


class PixelSelectionMethod(Enum):
    """rio-tiler.mosaic pixel selection methods"""

    first = FirstMethod
    highest = HighestMethod
    lowest = LowestMethod
    mean = MeanMethod
    median = MedianMethod
    stdev = StdevMethod
    lastbandlow = LastBandLowMethod
    lastbandhight = LastBandHighMethod
    count = CountMethod
