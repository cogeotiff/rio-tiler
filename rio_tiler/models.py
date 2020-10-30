"""rio-tiler models."""

from enum import Enum
from typing import Dict, List, Optional, Tuple, Union

from pydantic import BaseModel

NumType = Union[float, int]
BBox = Tuple[NumType, NumType, NumType, NumType]
ColorTuple = Tuple[int, int, int, int]


class NodataTypes(str, Enum):
    """rio-tiler Nodata types."""

    Alpha = "Alpha"
    Mask = "Mask"
    Internal = "Internal"
    Nodata = "Nodata"
    Empty = "None"


class Bounds(BaseModel):
    """Dataset Bounding box"""

    bounds: BBox


class SpatialInfo(Bounds):
    """Dataset SpatialInfo"""

    center: Tuple[NumType, NumType, int]
    minzoom: int
    maxzoom: int


class Info(SpatialInfo):
    """Dataset Info."""

    band_metadata: List[Tuple[str, Dict]]
    band_descriptions: List[Tuple[str, str]]
    dtype: str
    nodata_type: NodataTypes
    colorinterp: Optional[List[str]]
    scale: Optional[float]
    offset: Optional[float]
    colormap: Optional[Dict[int, ColorTuple]]

    class Config:
        """Config for model."""

        extra = "ignore"
        use_enum_values = True


class ImageStatistics(BaseModel):
    """Image statistics"""

    percentiles: List[NumType]
    min: NumType
    max: NumType
    std: NumType
    histogram: List[List[NumType]]


class Metadata(Info):
    """Dataset metadata and statistics."""

    statistics: Dict[str, ImageStatistics]
