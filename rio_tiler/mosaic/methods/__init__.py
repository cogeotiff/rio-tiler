"""rio-tiler.mosaic.methods: Mosaic filling methods."""

import warnings
from enum import Enum, EnumMeta

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


class _DeprecatedMemberMeta(EnumMeta):
    def __getattr__(cls, name: str):
        if name == "lastbandhight":
            warnings.warn(
                "'lastbandhight' is a typo and will be removed in a future version, "
                "use 'lastbandhigh' instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            return cls.lastbandhigh
        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")

    def __getitem__(cls, name: str):
        if name == "lastbandhight":
            warnings.warn(
                "'lastbandhight' is a typo and will be removed in a future version, "
                "use 'lastbandhigh' instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            return cls.lastbandhigh
        return super().__getitem__(name)


class PixelSelectionMethod(Enum, metaclass=_DeprecatedMemberMeta):
    """rio-tiler.mosaic pixel selection methods"""

    first = FirstMethod
    highest = HighestMethod
    lowest = LowestMethod
    mean = MeanMethod
    median = MedianMethod
    stdev = StdevMethod
    lastbandlow = LastBandLowMethod
    lastbandhigh = LastBandHighMethod
    count = CountMethod


__all__ = [
    "PixelSelectionMethod",
    "CountMethod",
    "FirstMethod",
    "HighestMethod",
    "LastBandHighMethod",
    "LastBandLowMethod",
    "LowestMethod",
    "MeanMethod",
    "MedianMethod",
    "StdevMethod",
]
