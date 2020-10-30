"""rio-tiler models."""

from enum import Enum
from typing import Dict, List, Optional, Tuple

import attr
import numpy
from pydantic import BaseModel
from rasterio.plot import reshape_as_image
from rio_color.operations import parse_operations
from rio_color.utils import scale_dtype, to_math_type

from .constants import BBox, ColorTuple, NumType
from .utils import _chunks, linear_rescale, render


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


@attr.s
class ImageData:
    """Image Data class."""

    data: numpy.ndarray = attr.ib()
    mask: numpy.ndarray = attr.ib()
    assets: Optional[List[str]] = attr.ib(default=None)

    def __iter__(self):
        """Allow for variable expansion (``arr, mask = ImageData``)"""
        for i in (self.data, self.mask):
            yield i

    def as_masked(self):
        """return a numpy masked array."""
        data = numpy.ma.array(self.data)
        data.mask = self.mask == 0
        return data

    def data_as_image(self) -> numpy.ndarray:
        """return a numpy masked array."""
        return reshape_as_image(self.data)

    @property
    def width(self) -> int:
        """Width of the data array."""
        return self.data.shape[2]

    @property
    def height(self) -> int:
        """Height of the data array."""
        return self.data.shape[1]

    @property
    def count(self) -> int:
        """Number of band."""
        return self.data.shape[0]

    def post_process(
        self,
        in_range: Optional[Tuple[NumType, NumType]] = None,
        out_range: Optional[Tuple[NumType, NumType]] = None,
        color_formula: Optional[str] = None,
    ):
        """Post-process image data."""
        if in_range:
            rescale_arr = tuple(_chunks(in_range, 2))
            if len(rescale_arr) != self.count:
                rescale_arr = ((rescale_arr[0]),) * self.count

            for bdx in range(self.count):
                self.data[bdx] = numpy.where(
                    self.mask,
                    linear_rescale(
                        self.data[bdx], in_range=rescale_arr[bdx], out_range=out_range
                    ),
                    0,
                )
            self.data = self.data.astype(numpy.uint8)

        if color_formula:
            self.data[self.data < 0] = 0
            for ops in parse_operations(color_formula):
                self.data = scale_dtype(ops(to_math_type(self.data)), numpy.uint8)

    def render(self, add_mask: bool = True, **kwargs) -> bytes:
        """Render data to image blob."""
        return (
            render(self.data, self.mask, **kwargs)
            if add_mask
            else render(self.data, **kwargs)
        )
