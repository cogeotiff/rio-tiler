"""rio-tiler models."""

import warnings
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import attr
import numpy
from affine import Affine
from pydantic import BaseModel
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.plot import reshape_as_image
from rasterio.transform import from_bounds
from rio_color.operations import parse_operations
from rio_color.utils import scale_dtype, to_math_type

from .constants import ColorTuple, NumType
from .errors import InvalidDatatypeWarning
from .utils import linear_rescale, render


class NodataTypes(str, Enum):
    """rio-tiler Nodata types."""

    Alpha = "Alpha"
    Mask = "Mask"
    Internal = "Internal"
    Nodata = "Nodata"
    Empty = "None"


class RioTilerBaseModel(BaseModel):
    """Base Model for rio-tiler models."""

    def __getitem__(self, item):
        """Keep `getter` access for compatibility."""
        return self.__dict__[item]


class Bounds(RioTilerBaseModel):
    """Dataset Bounding box"""

    bounds: BoundingBox


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

        extra = "allow"
        use_enum_values = True


class ImageStatistics(RioTilerBaseModel):
    """Image statistics"""

    percentiles: List[NumType]
    min: NumType
    max: NumType
    std: NumType
    histogram: List[List[NumType]]
    valid_percent: float


class Metadata(Info):
    """Dataset metadata and statistics."""

    statistics: Dict[str, ImageStatistics]


def to_coordsbbox(bbox) -> Optional[BoundingBox]:
    """Convert bbox to CoordsBbox nameTuple."""
    return BoundingBox(*bbox) if bbox else None


@attr.s
class ImageData:
    """Image Data class.

    Attributes:
        data (numpy.ndarray): pixel values.
        mask (numpy.ndarray): rasterio mask values.
        assets (list, optional): list of assets used to construct the data values.
        bounds (BoundingBox, optional): bounding box of the data.
        crs (rasterio.crs.CRS, optional): Coordinates Reference System of the bounds.
        metadata (dict, optional): Additional metadata. Defaults to `{}`.

    """

    data: numpy.ndarray = attr.ib()
    mask: numpy.ndarray = attr.ib()
    assets: Optional[List] = attr.ib(default=None)
    bounds: Optional[BoundingBox] = attr.ib(default=None, converter=to_coordsbbox)
    crs: Optional[CRS] = attr.ib(default=None)
    metadata: Optional[Dict] = attr.ib(factory=dict)

    @data.validator
    def _validate_data(self, attribute, value):
        """ImageData data has to be a 3d array in form of (count, height, width)"""
        if not len(value.shape) == 3:
            raise ValueError(
                "ImageData data has to be an array in form of (count, height, width)"
            )

    @mask.default
    def _default_mask(self):
        return numpy.zeros((self.height, self.width), dtype="uint8") + 255

    def __iter__(self):
        """Allow for variable expansion (``arr, mask = ImageData``)"""
        for i in (self.data, self.mask):
            yield i

    @classmethod
    def create_from_list(cls, data: Sequence["ImageData"]):
        """Create ImageData from a sequence of ImageData objects.

        Args:
            data (sequence): sequence of ImageData.

        """
        arr = numpy.concatenate([img.data for img in data])
        mask = numpy.all([img.mask for img in data], axis=0).astype(numpy.uint8) * 255
        assets = [img.assets[0] for img in data if img.assets]

        bounds_values = [img.bounds for img in data if img.bounds]
        bounds = bounds_values[0] if bounds_values else None

        crs_values = [img.crs for img in data if img.crs]
        crs = crs_values[0] if crs_values else None

        return cls(arr, mask, assets=assets, crs=crs, bounds=bounds)

    def as_masked(self) -> numpy.ma.MaskedArray:
        """return a numpy masked array."""
        data = numpy.ma.array(self.data)
        data.mask = self.mask == 0
        return data

    def data_as_image(self) -> numpy.ndarray:
        """Return the data array reshaped into an image processing/visualization software friendly order.

        (bands, rows, columns) -> (rows, columns, bands).

        """
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

    @property
    def transform(self):
        """Returns the affine transform."""
        return (
            from_bounds(*self.bounds, self.width, self.height)
            if self.bounds
            else Affine.scale(self.width, -self.height)
        )

    def _rescale(
        self,
        data: numpy.ndarray,
        mask: numpy.ndarray,
        in_range: Sequence[Tuple[NumType, NumType]],
        out_range: Sequence[Tuple[NumType, NumType]] = ((0, 255),),
        out_dtype: Union[str, numpy.number] = "uint8",
    ):
        """Rescale data."""
        nbands = data.shape[0]

        if len(in_range) != nbands:
            in_range = ((in_range[0]),) * nbands

        if len(out_range) != nbands:
            out_range = ((out_range[0]),) * nbands

        for bdx in range(nbands):
            data[bdx] = numpy.where(
                mask,
                linear_rescale(
                    data[bdx], in_range=in_range[bdx], out_range=out_range[bdx]
                ),
                0,
            )

        return data.astype(out_dtype)

    def post_process(
        self,
        in_range: Optional[Sequence[Tuple[NumType, NumType]]] = None,
        out_dtype: Union[str, numpy.number] = "uint8",
        color_formula: Optional[str] = None,
        **kwargs: Any,
    ) -> "ImageData":
        """Post-process image data.

        Args:
            in_range (tuple): input min/max bounds value to rescale from.
            out_dtype (str, optional): output datatype after rescaling. Defaults to `uint8`.
            color_formula (str, optional): rio-color formula (see: https://github.com/mapbox/rio-color).
            kwargs (optional): keyword arguments to forward to `rio_tiler.utils.linear_rescale`.

        Returns:
            ImageData: new ImageData object with the updated data.

        Examples:
            >>> img.post_process(in_range=((0, 16000), ))

            >>> img.post_process(color_formula="Gamma RGB 4.1")

        """
        data = self.data.copy()
        mask = self.mask.copy()

        if in_range:
            data = self._rescale(data, mask, in_range, out_dtype=out_dtype, **kwargs)

        if color_formula:
            data[data < 0] = 0
            for ops in parse_operations(color_formula):
                data = scale_dtype(ops(to_math_type(data)), numpy.uint8)

        return ImageData(
            data,
            mask,
            crs=self.crs,
            bounds=self.bounds,
            assets=self.assets,
            metadata=self.metadata,
        )

    def render(
        self,
        add_mask: bool = True,
        img_format: str = "PNG",
        colormap: Optional[Dict] = None,
        **kwargs,
    ) -> bytes:
        """Render data to image blob.

        Args:
            add_mask (bool, optional): add mask to output image. Defaults to `True`.
            img_format (str, optional): output image format. Defaults to `PNG`.
            colormap (dict, optional): GDAL RGBA Color Table dictionary.
            kwargs (optional): keyword arguments to forward to `rio_tiler.utils.render`.

        Returns:
            bytes: image.

        """
        img_format = img_format.upper()

        if img_format == "GTIFF":
            if "transform" not in kwargs:
                kwargs.update({"transform": self.transform})
            if "crs" not in kwargs and self.crs:
                kwargs.update({"crs": self.crs})

        data = self.data.copy()
        datatype_range = (dtype_ranges[str(data.dtype)],)

        if not colormap:
            if img_format in ["PNG"] and data.dtype not in ["uint8", "uint16"]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds.",
                    InvalidDatatypeWarning,
                )
                data = self._rescale(data, self.mask, in_range=datatype_range)

            elif img_format in ["JPEG", "WEBP"] and data.dtype not in ["uint8"]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds.",
                    InvalidDatatypeWarning,
                )
                data = self._rescale(data, self.mask, in_range=datatype_range)

            elif img_format in ["JP2OPENJPEG"] and data.dtype not in [
                "uint8",
                "int16",
                "uint16",
            ]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds.",
                    InvalidDatatypeWarning,
                )
                data = self._rescale(data, self.mask, in_range=datatype_range)

        if add_mask:
            return render(
                data, self.mask, img_format=img_format, colormap=colormap, **kwargs
            )

        return render(data, img_format=img_format, colormap=colormap, **kwargs)
