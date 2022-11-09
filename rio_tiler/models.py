"""rio-tiler models."""

import itertools
import warnings
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import attr
import numpy
from affine import Affine
from color_operations import parse_operations, scale_dtype, to_math_type
from pydantic import BaseModel
from rasterio import windows
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import Resampling
from rasterio.plot import reshape_as_image
from rasterio.transform import from_bounds

from rio_tiler.errors import InvalidDatatypeWarning
from rio_tiler.expression import apply_expression, get_expression_blocks
from rio_tiler.types import BBox, ColorMapType, GDALColorMapType, IntervalTuple, NumType
from rio_tiler.utils import linear_rescale, render, resize_array


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
    colormap: Optional[GDALColorMapType]

    class Config:
        """Config for model."""

        extra = "allow"
        use_enum_values = True


class BandStatistics(RioTilerBaseModel):
    """Image statistics"""

    min: float
    max: float
    mean: float
    count: float
    sum: float
    std: float
    median: float
    majority: float
    minority: float
    unique: float
    histogram: List[List[NumType]]
    valid_percent: float
    masked_pixels: float
    valid_pixels: float

    class Config:
        """Config for model."""

        extra = "allow"  # We allow extra values for `percentiles_{}`


def to_coordsbbox(bbox) -> Optional[BoundingBox]:
    """Convert bbox to CoordsBbox nameTuple."""
    return BoundingBox(*bbox) if bbox else None


def rescale_image(
    data: numpy.ndarray,
    mask: numpy.ndarray,
    in_range: Sequence[IntervalTuple],
    out_range: Sequence[IntervalTuple] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = "uint8",
):
    """Rescale image data."""
    if len(data.shape) < 3:
        data = numpy.expand_dims(data, axis=0)

    nbands = data.shape[0]

    if len(in_range) != nbands:
        in_range = ((in_range[0]),) * nbands

    if len(out_range) != nbands:
        out_range = ((out_range[0]),) * nbands

    for bdx in range(nbands):
        data[bdx] = numpy.where(
            mask,
            linear_rescale(data[bdx], in_range=in_range[bdx], out_range=out_range[bdx]),
            0,
        )

    return data.astype(out_dtype)


@attr.s
class PointData:
    """Point Data class.

    Attributes:
        data (numpy.ndarray): pixel values.
        mask (numpy.ndarray): rasterio mask values.
        band_names (list): name of each band. Defaults to `["1", "2", "3"]` for 3 bands image.
        coordinates (tuple): Point's coordinates.
        crs (rasterio.crs.CRS, optional): Coordinates Reference System of the bounds.
        assets (list, optional): list of assets used to construct the data values.
        metadata (dict, optional): Additional metadata. Defaults to `{}`.

    """

    data: numpy.ndarray = attr.ib()
    mask: numpy.ndarray = attr.ib()
    band_names: List[str] = attr.ib()
    coordinates: Optional[Tuple[float, float]] = attr.ib(default=None)
    crs: Optional[CRS] = attr.ib(default=None)
    assets: Optional[List] = attr.ib(default=None)
    metadata: Optional[Dict] = attr.ib(factory=dict)

    @data.validator
    def _validate_data(self, attribute, value):
        """PointsData data has to be a 1d array."""
        if not len(value.shape) == 1:
            raise ValueError("PointsData data has to be a 1D array")

    @coordinates.validator
    def _validate_coordinates(self, attribute, value):
        """coordinates has to be a 2d list."""
        if value and not len(value) == 2:
            raise ValueError("Coordinates data has to be a 2d list")

    @band_names.default
    def _default_names(self):
        return [f"b{ix + 1}" for ix in range(self.count)]

    @mask.default
    def _default_mask(self):
        return numpy.zeros(self.data.shape[0], dtype="uint8") + 255

    def __iter__(self):
        """Allow for variable expansion."""
        for i in self.data:
            yield i

    @property
    def count(self) -> int:
        """Number of band."""
        return self.data.shape[0]

    @classmethod
    def create_from_list(cls, data: Sequence["PointData"]):
        """Create PointData from a sequence of PointsData objects.

        Args:
            data (sequence): sequence of PointData.

        """
        # validate coordinates
        if all([pt.coordinates or pt.crs or None for pt in data]):
            lon, lat, crs = zip(*[(*(pt.coordinates or []), pt.crs) for pt in data])
            if len(set(lon)) > 1 or len(set(lat)) > 1 or len(set(crs)) > 1:
                raise Exception(
                    "Cannot concatenate points with different coordinates/CRS."
                )

        arr = numpy.concatenate([pt.data for pt in data])
        mask = numpy.concatenate([pt.mask for pt in data])

        assets = list(
            dict.fromkeys(
                itertools.chain.from_iterable([pt.assets for pt in data if pt.assets])
            )
        )

        band_names = list(
            itertools.chain.from_iterable(
                [pt.band_names for pt in data if pt.band_names]
            )
        )

        return cls(
            arr,
            mask,
            assets=assets,
            crs=data[0].crs,
            coordinates=data[0].coordinates,
            band_names=band_names,
        )

    def as_masked(self) -> numpy.ma.MaskedArray:
        """return a numpy masked array."""
        data = numpy.ma.array(self.data)
        data.mask = self.mask == 0
        return data

    def apply_expression(self, expression: str) -> "PointData":
        """Apply expression to the image data."""
        blocks = get_expression_blocks(expression)
        return PointData(
            apply_expression(blocks, self.band_names, self.data),
            self.mask,
            assets=self.assets,
            crs=self.crs,
            coordinates=self.coordinates,
            band_names=blocks,
            metadata=self.metadata,
        )


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
        band_names (list, optional): name of each band. Defaults to `["1", "2", "3"]` for 3 bands image.
        dataset_statistics (list, optional): dataset statistics `[(min, max), (min, max)]`

    """

    data: numpy.ndarray = attr.ib()
    mask: numpy.ndarray = attr.ib()
    assets: Optional[List] = attr.ib(default=None)
    bounds: Optional[BoundingBox] = attr.ib(default=None, converter=to_coordsbbox)
    crs: Optional[CRS] = attr.ib(default=None)
    metadata: Optional[Dict] = attr.ib(factory=dict)
    band_names: List[str] = attr.ib()
    dataset_statistics: Optional[Sequence[Tuple[float, float]]] = attr.ib(default=None)

    @data.validator
    def _validate_data(self, attribute, value):
        """ImageData data has to be a 3d array in form of (count, height, width)"""
        if not len(value.shape) == 3:
            raise ValueError(
                "ImageData data has to be an array in form of (count, height, width)"
            )

    @band_names.default
    def _default_names(self):
        return [f"b{ix + 1}" for ix in range(self.count)]

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
        h, w = zip(*[(img.height, img.width) for img in data])
        if len(set(h)) > 1 or len(set(w)) > 1:
            warnings.warn(
                "Cannot concatenate images with different size. Will resize using max width/heigh",
                UserWarning,
            )
            max_h, max_w = max(h), max(w)
            for img in data:
                if img.height == max_h and img.width == max_w:
                    continue
                img.data = resize_array(img.data, max_h, max_w)
                img.mask = resize_array(img.mask, max_h, max_w)

        arr = numpy.concatenate([img.data for img in data])
        mask = numpy.all([img.mask for img in data], axis=0).astype(numpy.uint8) * 255
        assets = list(
            dict.fromkeys(
                itertools.chain.from_iterable(
                    [img.assets for img in data if img.assets]
                )
            )
        )

        bounds_values = [img.bounds for img in data if img.bounds]
        bounds = bounds_values[0] if bounds_values else None

        crs_values = [img.crs for img in data if img.crs]
        crs = crs_values[0] if crs_values else None

        band_names = list(
            itertools.chain.from_iterable(
                [img.band_names for img in data if img.band_names]
            )
        )

        stats = list(
            itertools.chain.from_iterable(
                [img.dataset_statistics for img in data if img.dataset_statistics]
            )
        )
        dataset_statistics = stats if len(stats) == len(band_names) else None

        return cls(
            arr,
            mask,
            assets=assets,
            crs=crs,
            bounds=bounds,
            band_names=band_names,
            dataset_statistics=dataset_statistics,
        )

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

    def rescale(
        self,
        in_range: Sequence[IntervalTuple],
        out_range: Sequence[IntervalTuple] = ((0, 255),),
        out_dtype: Union[str, numpy.number] = "uint8",
    ):
        """Rescale data in place."""
        self.data = rescale_image(
            self.data.copy(),
            self.mask,
            in_range=in_range,
            out_range=out_range,
            out_dtype=out_dtype,
        )

    def apply_color_formula(self, color_formula: Optional[str]):
        """Apply color-operations formula in place."""
        out = self.data.copy()
        out[out < 0] = 0

        for ops in parse_operations(color_formula):
            out = scale_dtype(ops(to_math_type(out)), numpy.uint8)

        self.data = out

    def apply_expression(self, expression: str) -> "ImageData":
        """Apply expression to the image data."""
        blocks = get_expression_blocks(expression)

        stats = self.dataset_statistics
        if stats:
            res = []
            for prod in itertools.product(*stats):  # type: ignore
                res.append(apply_expression(blocks, self.band_names, numpy.array(prod)))

            stats = list(zip([min(r) for r in zip(*res)], [max(r) for r in zip(*res)]))

        return ImageData(
            apply_expression(blocks, self.band_names, self.data),
            self.mask.copy(),
            assets=self.assets,
            crs=self.crs,
            bounds=self.bounds,
            band_names=blocks,
            metadata=self.metadata,
            dataset_statistics=stats,
        )

    def resize(
        self,
        height: int,
        width: int,
        resampling_method: Resampling = "nearest",
    ) -> "ImageData":
        """Resize data and mask."""
        data = resize_array(self.data, height, width, resampling_method)
        mask = resize_array(self.mask, height, width, resampling_method)

        return ImageData(
            data,
            mask,
            assets=self.assets,
            crs=self.crs,
            bounds=self.bounds,
            band_names=self.band_names,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
        )

    def clip(self, bbox: BBox) -> "ImageData":
        """Clip data and mask to a bbox."""
        row_slice, col_slice = windows.from_bounds(
            *bbox, transform=self.transform
        ).toslices()
        data = self.data[:, row_slice, col_slice]
        mask = self.mask[row_slice, col_slice]

        return ImageData(
            data,
            mask,
            assets=self.assets,
            crs=self.crs,
            bounds=bbox,
            band_names=self.band_names,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
        )

    def post_process(
        self,
        in_range: Optional[Sequence[IntervalTuple]] = None,
        out_dtype: Union[str, numpy.number] = "uint8",
        color_formula: Optional[str] = None,
        **kwargs: Any,
    ) -> "ImageData":
        """Post-process image data.

        Args:
            in_range (tuple): input min/max bounds value to rescale from.
            out_dtype (str, optional): output datatype after rescaling. Defaults to `uint8`.
            color_formula (str, optional): color-ops formula (see: https://github.com/vincentsarago/color-ops).
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
            data = rescale_image(data, mask, in_range, out_dtype=out_dtype, **kwargs)

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
        colormap: Optional[ColorMapType] = None,
        **kwargs,
    ) -> bytes:
        """Render data to image blob.

        Args:
            add_mask (bool, optional): add mask to output image. Defaults to `True`.
            img_format (str, optional): output image format. Defaults to `PNG`.
            colormap (dict or sequence, optional): RGBA Color Table dictionary or sequence.
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
        mask = self.mask.copy()
        datatype_range = self.dataset_statistics or (dtype_ranges[str(data.dtype)],)

        if not colormap:
            if img_format in ["PNG"] and data.dtype not in ["uint8", "uint16"]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds or dataset_statistics.",
                    InvalidDatatypeWarning,
                )
                data = rescale_image(data, mask, in_range=datatype_range)

            elif img_format in ["JPEG", "WEBP"] and data.dtype not in ["uint8"]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds or dataset_statistics.",
                    InvalidDatatypeWarning,
                )
                data = rescale_image(data, mask, in_range=datatype_range)

            elif img_format in ["JP2OPENJPEG"] and data.dtype not in [
                "uint8",
                "int16",
                "uint16",
            ]:
                warnings.warn(
                    f"Invalid type: `{data.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds or dataset_statistics.",
                    InvalidDatatypeWarning,
                )
                data = rescale_image(data, mask, in_range=datatype_range)

        if add_mask:
            return render(
                data, mask, img_format=img_format, colormap=colormap, **kwargs
            )

        return render(data, img_format=img_format, colormap=colormap, **kwargs)
