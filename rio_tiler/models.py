"""rio-tiler models."""

import itertools
import warnings
from typing import Any, Dict, List, Literal, Optional, Sequence, Tuple, Union

import attr
import numpy
import rasterio
from affine import Affine
from color_operations import parse_operations, scale_dtype, to_math_type
from numpy.typing import NDArray
from pydantic import BaseModel
from rasterio import windows
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import ColorInterp, Resampling
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import rasterize
from rasterio.io import MemoryFile
from rasterio.plot import reshape_as_image
from rasterio.transform import array_bounds, from_bounds
from rasterio.warp import calculate_default_transform, reproject, transform_geom
from typing_extensions import Self

from rio_tiler.colormap import apply_cmap
from rio_tiler.constants import WGS84_CRS
from rio_tiler.errors import InvalidDatatypeWarning, InvalidPointDataError
from rio_tiler.expression import apply_expression, get_expression_blocks
from rio_tiler.types import (
    BBox,
    ColorMapType,
    GDALColorMapType,
    IntervalTuple,
    NoData,
    NumType,
    RIOResampling,
    WarpResampling,
)
from rio_tiler.utils import (
    _validate_shape_input,
    get_array_statistics,
    linear_rescale,
    non_alpha_indexes,
    render,
    resize_array,
)


class Bounds(BaseModel):
    """Dataset Bounding box"""

    bounds: BBox
    crs: str


class Info(Bounds):
    """Dataset Info."""

    band_metadata: List[Tuple[str, Dict]]
    band_descriptions: List[Tuple[str, str]]
    dtype: str
    nodata_type: Literal["Alpha", "Mask", "Internal", "Nodata", "None"]
    colorinterp: Optional[List[str]] = None
    scales: Optional[List[float]] = None
    offsets: Optional[List[float]] = None
    colormap: Optional[GDALColorMapType] = None

    model_config = {"extra": "allow"}


class BandStatistics(BaseModel):
    """Band statistics"""

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

    model_config = {"extra": "allow"}


def to_coordsbbox(bbox) -> Optional[BoundingBox]:
    """Convert bbox to CoordsBbox nameTuple."""
    return BoundingBox(*bbox) if bbox else None


def rescale_image(
    array: numpy.ma.MaskedArray,
    in_range: Sequence[IntervalTuple],
    out_range: Sequence[IntervalTuple] = ((0, 255),),
    out_dtype: Union[str, numpy.number] = "uint8",
) -> numpy.ma.MaskedArray:
    """Rescale image data in-place."""
    if len(array.shape) < 3:
        array = numpy.expand_dims(array, axis=0)

    nbands = array.shape[0]

    if len(in_range) != nbands:
        in_range = ((in_range[0]),) * nbands

    if len(out_range) != nbands:
        out_range = ((out_range[0]),) * nbands

    for bdx in range(nbands):
        array.data[bdx] = numpy.where(
            ~array.mask[bdx],
            linear_rescale(
                array.data[bdx], in_range=in_range[bdx], out_range=out_range[bdx]
            ),
            0,
        )

    return array.astype(out_dtype)


def to_masked(array: numpy.ndarray) -> numpy.ma.MaskedArray:
    """Makes sure we have a MaskedArray."""
    if not numpy.ma.isarray(array):
        array = numpy.ma.asarray(array)

    # when a masked array is totally valid, the mask is set to numpy.ma.nomask
    # https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask
    # doing `array.mask = False` force the creation of the mask array
    if not array.mask.shape:
        array.mask = False

    return array


@attr.s
class PointData:
    """Point Data class.

    Attributes:
        array (numpy.ma.MaskedArray): pixel values.
        band_names (list): name of each band. Defaults to `["1", "2", "3"]` for 3 bands image.
        coordinates (tuple): Point's coordinates.
        crs (rasterio.crs.CRS, optional): Coordinates Reference System of the bounds.
        assets (list, optional): list of assets used to construct the data values.
        metadata (dict, optional): Additional metadata. Defaults to `{}`.

    """

    array: numpy.ma.MaskedArray = attr.ib(converter=to_masked)
    band_names: List[str] = attr.ib(kw_only=True)
    coordinates: Optional[Tuple[float, float]] = attr.ib(default=None, kw_only=True)
    crs: Optional[CRS] = attr.ib(default=None, kw_only=True)
    assets: Optional[List] = attr.ib(default=None, kw_only=True)
    metadata: Optional[Dict] = attr.ib(factory=dict, kw_only=True)
    nodata: Optional[NoData] = attr.ib(default=None, kw_only=True)
    scales: Optional[List[NumType]] = attr.ib(kw_only=True)
    offsets: Optional[List[NumType]] = attr.ib(kw_only=True)
    pixel_location: Optional[Tuple[NumType, NumType]] = attr.ib(
        default=None, kw_only=True
    )

    @array.validator
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

    @scales.default
    def _default_scales(self):
        return [1.0] * self.count

    @offsets.default
    def _default_offsets(self):
        return [0.0] * self.count

    @property
    def data(self) -> numpy.ndarray:
        """Return data part of the masked array."""
        return self.array.data

    @property
    def _mask(self):
        """Return `inverted/merged` mask from data array."""
        return numpy.array([numpy.logical_and.reduce(~self.array.mask)])

    @property
    def mask(self) -> numpy.ndarray:
        """Return Mask in form of rasterio dataset mask."""
        minv, maxv = dtype_ranges[str(self.array.dtype)]
        return numpy.where(self._mask, maxv, minv).astype(self.array.dtype)

    def __iter__(self):
        """Allow for variable expansion."""
        for i in self.array.data:
            yield i

    @property
    def count(self) -> int:
        """Number of band."""
        return self.array.shape[0]

    @classmethod
    def create_from_list(cls, data: Sequence["PointData"]) -> Self:
        """Create PointData from a sequence of PointsData objects.

        Args:
            data (sequence): sequence of PointData.

        """
        if not data:
            raise InvalidPointDataError("Empty PointData list.")

        # validate coordinates
        if all(pt.coordinates or pt.crs or None for pt in data):
            lon, lat, crs = zip(*[(*(pt.coordinates or []), pt.crs) for pt in data])
            if len(set(lon)) > 1 or len(set(lat)) > 1 or len(set(crs)) > 1:
                raise InvalidPointDataError(
                    "Cannot concatenate points with different coordinates/CRS."
                )

        arr = numpy.ma.concatenate([pt.array for pt in data])

        assets = list(
            dict.fromkeys(
                itertools.chain.from_iterable([pt.assets for pt in data if pt.assets])
            )
        )

        band_names = list(
            itertools.chain.from_iterable([pt.band_names for pt in data if pt.band_names])
        )

        scales = list(itertools.chain.from_iterable([pt.scales for pt in data]))

        offsets = list(itertools.chain.from_iterable([pt.offsets for pt in data]))

        metadata = dict(
            itertools.chain.from_iterable(
                [pt.metadata.items() for pt in data if pt.metadata]
            )
        )

        return cls(
            arr,
            assets=assets,
            band_names=band_names,
            offsets=offsets,
            scales=scales,
            coordinates=data[0].coordinates,
            crs=data[0].crs,
            metadata=metadata,
        )

    def apply_expression(self, expression: str) -> "PointData":
        """Apply expression to the image data."""
        blocks = get_expression_blocks(expression)

        data = apply_expression(blocks, self.band_names, self.array)
        # Using numexpr do not preserve mask info
        data.mask = False

        return PointData(
            data,
            assets=self.assets,
            crs=self.crs,
            coordinates=self.coordinates,
            band_names=blocks,
            metadata=self.metadata,
            pixel_location=self.pixel_location,
        )


def masked_and_3d(array: numpy.ndarray) -> numpy.ma.MaskedArray:
    """Makes sure we have a 3D array and mask"""
    if not numpy.ma.isarray(array):
        array = numpy.ma.asarray(array)

    if len(array.shape) < 3:
        array = numpy.expand_dims(array, axis=0)

    # when a masked array is totally valid, the mask is set to numpy.ma.nomask
    # https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask
    # doing `array.mask = False` force the creation of the mask array
    if not array.mask.shape:
        array.mask = False

    return array


@attr.s
class ImageData:
    """Image Data class.

    Attributes:
        array (numpy.ma.MaskedArray): image values.
        assets (list, optional): list of assets used to construct the data values.
        bounds (BoundingBox, optional): bounding box of the data.
        crs (rasterio.crs.CRS, optional): Coordinates Reference System of the bounds.
        metadata (dict, optional): Additional metadata. Defaults to `{}`.
        band_names (list, optional): name of each band. Defaults to `["1", "2", "3"]` for 3 bands image.
        dataset_statistics (list, optional): dataset statistics `[(min, max), (min, max)]`

    Note: `mask` should be considered as `PER_BAND` so shape should be similar as the data

    """

    array: numpy.ma.MaskedArray = attr.ib(converter=masked_and_3d)
    assets: Optional[List] = attr.ib(default=None, kw_only=True)
    bounds: Optional[BoundingBox] = attr.ib(
        default=None, converter=to_coordsbbox, kw_only=True
    )
    crs: Optional[CRS] = attr.ib(default=None, kw_only=True)
    metadata: Optional[Dict] = attr.ib(factory=dict, kw_only=True)
    nodata: Optional[NoData] = attr.ib(default=None, kw_only=True)
    scales: Optional[List[NumType]] = attr.ib(kw_only=True)
    offsets: Optional[List[NumType]] = attr.ib(kw_only=True)
    band_names: Optional[List[str]] = attr.ib(kw_only=True)
    dataset_statistics: Optional[Sequence[Tuple[float, float]]] = attr.ib(
        default=None, kw_only=True
    )
    cutline_mask: Optional[numpy.ndarray] = attr.ib(default=None)
    alpha_mask: Optional[numpy.ndarray] = attr.ib(default=None)

    @band_names.default
    def _default_names(self):
        return [f"b{ix + 1}" for ix in range(self.count)]

    @scales.default
    def _default_scales(self):
        return [1.0] * self.count

    @offsets.default
    def _default_offsets(self):
        return [0.0] * self.count

    @alpha_mask.validator
    def _check_alpha_mask(self, attribute, value):
        """Make sure alpha mask has valid shame and datatype."""
        if value is not None:
            if (
                len(value.shape) != 2
                or value.shape[0] != self.height
                or value.shape[1] != self.width
            ):
                raise ValueError(
                    f"Invalide shape {value.shape} for AlphaMask, should be of shape {self.height}x{self.width}"
                )

            if not value.dtype == self.array.dtype:
                raise ValueError(
                    f"Invalide dtype {value.dtype} for AlphaMask, should be of {self.array.dtype}"
                )

    @property
    def data(self) -> numpy.ndarray:
        """Return data part of the masked array."""
        return self.array.data

    @property
    def mask(self) -> numpy.ndarray:
        """Return Mask in form of rasterio dataset mask."""
        # NOTE: if available we return the alpha_mask
        if self.alpha_mask is not None:
            return self.alpha_mask

        minv, maxv = dtype_ranges[str(self.array.dtype)]
        return numpy.where(self._mask, maxv, minv).astype(self.array.dtype)

    @property
    def _mask(self):
        """Return `inverted/merged` mask from data array."""
        return numpy.logical_or.reduce(~self.array.mask)

    def __iter__(self):
        """Allow for variable expansion (``arr, mask = ImageData``)"""
        for i in (self.array.data, self.mask):
            yield i

    @classmethod
    def from_bytes(cls, data: bytes) -> Self:
        """Create ImageData from bytes.

        Args:
            data (bytes): raster dataset as bytes.

        """
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            with MemoryFile(data) as m:
                with m.open() as dataset:
                    indexes = non_alpha_indexes(dataset)
                    if ColorInterp.alpha in dataset.colorinterp:
                        alpha_idx = dataset.colorinterp.index(ColorInterp.alpha) + 1
                        idx = tuple(indexes) + (alpha_idx,)
                        array = dataset.read(indexes=idx)

                        mask = ~array[-1].astype("bool")
                        array = numpy.ma.MaskedArray(array[0:-1])
                        array.mask = mask

                    else:
                        array = dataset.read(indexes=indexes, masked=True)

                    stats = []
                    for ix in indexes:
                        tags = dataset.tags(ix)
                        if all(
                            stat in tags
                            for stat in ["STATISTICS_MINIMUM", "STATISTICS_MAXIMUM"]
                        ):
                            stat_min = float(tags.get("STATISTICS_MINIMUM"))
                            stat_max = float(tags.get("STATISTICS_MAXIMUM"))
                            stats.append((stat_min, stat_max))

                    dataset_statistics = stats if len(stats) == len(indexes) else None

                    return cls(
                        array,
                        crs=dataset.crs,
                        bounds=dataset.bounds,
                        band_names=[
                            dataset.descriptions[ix - 1] or f"b{idx}" for idx in indexes
                        ],
                        dataset_statistics=dataset_statistics,
                        nodata=dataset.nodata,
                        scales=list(dataset.scales),
                        offsets=list(dataset.offsets),
                        metadata=dataset.tags(),
                    )

    @classmethod
    def create_from_list(cls, data: Sequence["ImageData"]) -> Self:
        """Create ImageData from a sequence of ImageData objects.

        Args:
            data (sequence): sequence of ImageData.

        """
        h, w = zip(*[(img.height, img.width) for img in data])

        # Get cutline mask at highest resolution.
        max_h, max_w = max(h), max(w)
        cutline_mask = next(
            img.cutline_mask for img in data if img.height == max_h and img.width == max_w
        )

        if len(set(h)) > 1 or len(set(w)) > 1:
            warnings.warn(
                "Cannot concatenate images with different size. Will resize using max width/heigh",
                UserWarning,
            )
            for img in data:
                if img.height == max_h and img.width == max_w:
                    continue
                arr = numpy.ma.MaskedArray(
                    resize_array(img.array.data, max_h, max_w),
                    mask=resize_array(img.array.mask * 1, max_h, max_w).astype("bool"),
                )
                img.array = arr

        arr = numpy.ma.concatenate([img.array for img in data])

        assets = list(
            dict.fromkeys(
                itertools.chain.from_iterable([img.assets for img in data if img.assets])
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

        scales = list(itertools.chain.from_iterable([img.scales for img in data]))

        offsets = list(itertools.chain.from_iterable([img.offsets for img in data]))

        stats = list(
            itertools.chain.from_iterable(
                [img.dataset_statistics for img in data if img.dataset_statistics]
            )
        )
        dataset_statistics = stats if len(stats) == len(band_names) else None

        metadata = dict(
            itertools.chain.from_iterable(
                [img.metadata.items() for img in data if img.metadata]
            )
        )

        return cls(
            arr,
            assets=assets,
            crs=crs,
            bounds=bounds,
            band_names=band_names,
            dataset_statistics=dataset_statistics,
            cutline_mask=cutline_mask,
            metadata=metadata,
            scales=scales,
            offsets=offsets,
        )

    def data_as_image(self) -> numpy.ndarray:
        """Return the data array reshaped into an image processing/visualization software friendly order.

        (bands, rows, columns) -> (rows, columns, bands).

        """
        return reshape_as_image(self.array)

    @property
    def width(self) -> int:
        """Width of the data array."""
        return self.array.shape[2]

    @property
    def height(self) -> int:
        """Height of the data array."""
        return self.array.shape[1]

    @property
    def count(self) -> int:
        """Number of band."""
        return self.array.shape[0]

    @property
    def transform(self) -> Affine:
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
    ) -> Self:
        """Rescale data in place."""
        self.array = rescale_image(
            self.array,
            in_range=in_range,
            out_range=out_range,
            out_dtype=out_dtype,
        )
        if self.alpha_mask is not None:
            self.alpha_mask = linear_rescale(
                self.alpha_mask,
                in_range=dtype_ranges[str(self.alpha_mask.dtype)],
                out_range=dtype_ranges[out_dtype],
            ).astype(out_dtype)

        # reset scales/offsets
        self.scales = [1.0] * self.count
        self.offsets = [0.0] * self.count

        return self

    def apply_color_formula(self, color_formula: Optional[str]) -> Self:
        """Apply color-operations formula in place."""
        out = self.array.data
        out[out < 0] = 0

        for ops in parse_operations(color_formula):
            out = scale_dtype(ops(to_math_type(out)), numpy.uint8)

        data = numpy.ma.MaskedArray(out)
        data.mask = self.array.mask
        self.array = data

        # NOTE: we need to rescale the alpha mask if not in Uint8
        if self.alpha_mask is not None and self.alpha_mask.dtype != "uint8":
            self.alpha_mask = linear_rescale(
                self.alpha_mask, in_range=dtype_ranges[str(self.alpha_mask.dtype)]
            ).astype("uint8")

        # reset scales/offsets
        self.scales = [1.0] * self.count
        self.offsets = [0.0] * self.count

        return self

    def apply_colormap(self, colormap: ColorMapType) -> "ImageData":
        """Apply colormap to the image data."""
        data, alpha = apply_cmap(self.array.data, colormap)

        array = numpy.ma.MaskedArray(data)

        # `inValid/Valid` values for colormaped datatype (e.g 0 for uint8)
        invalid, valid = dtype_ranges[str(alpha.dtype)]

        # Combine both dataset mask and alpha from colormap
        array.mask = numpy.bitwise_or(alpha != valid, ~self._mask)

        if self.alpha_mask is not None:
            warnings.warn(
                "Alpha Mask value ignored from the input ImageData object when applying colormap.",
                UserWarning,
            )

        return ImageData(
            array,
            assets=self.assets,
            crs=self.crs,
            bounds=self.bounds,
            metadata=self.metadata,
            # NOTE: make sure masked part from initial data are also masked in alpha band
            alpha_mask=numpy.where(~self._mask, invalid, alpha),
        )

    def apply_expression(self, expression: str) -> "ImageData":
        """Apply expression to the image data."""
        blocks = get_expression_blocks(expression)

        stats = self.dataset_statistics
        if stats:
            res = []
            for prod in itertools.product(*stats):  # type: ignore
                res.append(apply_expression(blocks, self.band_names, numpy.array(prod)))

            stats = list(
                zip(
                    [min(r) for r in zip(*res)],
                    [max(r) for r in zip(*res)],
                )
            )

        data = apply_expression(blocks, self.band_names, self.array.copy())
        # NOTE: We use dataset mask when mixing bands
        data.mask = numpy.logical_or.reduce(self.array.mask)

        return ImageData(
            data,
            assets=self.assets,
            crs=self.crs,
            bounds=self.bounds,
            band_names=blocks,
            metadata=self.metadata,
            dataset_statistics=stats,
            alpha_mask=self.alpha_mask,
        )

    def resize(
        self,
        height: int,
        width: int,
        resampling_method: RIOResampling = "nearest",
    ) -> "ImageData":
        """Resize data and mask."""
        data = resize_array(self.array.data, height, width, resampling_method)
        mask = resize_array(self.array.mask * 1, height, width, resampling_method).astype(
            "bool"
        )
        alpha_mask = self.alpha_mask
        if alpha_mask is not None:
            alpha_mask = resize_array(alpha_mask.copy(), height, width, resampling_method)

        return ImageData(
            numpy.ma.MaskedArray(data, mask=mask),
            assets=self.assets,
            crs=self.crs,
            bounds=self.bounds,
            band_names=self.band_names,
            nodata=self.nodata,
            scales=self.scales,
            offsets=self.offsets,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
            alpha_mask=alpha_mask,
        )

    def clip(self, bbox: BBox) -> "ImageData":
        """Clip data and mask to a bbox."""
        row_slice, col_slice = windows.from_bounds(
            *bbox, transform=self.transform
        ).toslices()

        return ImageData(
            self.array[:, row_slice, col_slice].copy(),
            assets=self.assets,
            crs=self.crs,
            bounds=bbox,
            band_names=self.band_names,
            nodata=self.nodata,
            scales=self.scales,
            offsets=self.offsets,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
            alpha_mask=self.alpha_mask[row_slice, col_slice].copy()
            if self.alpha_mask is not None
            else None,
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
        img = ImageData(
            self.array.copy(),
            crs=self.crs,
            bounds=self.bounds,
            assets=self.assets,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
            alpha_mask=self.alpha_mask.copy() if self.alpha_mask is not None else None,
        )

        if in_range:
            img.rescale(in_range, out_dtype=out_dtype, **kwargs)

        if color_formula:
            img.apply_color_formula(color_formula)

        return img

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

        array = self.array.copy()
        mask = self.mask

        datatype_range = self.dataset_statistics or (dtype_ranges[str(array.dtype)],)

        if not colormap:
            format_dtypes = {
                "PNG": ["uint8", "uint16"],
                "JPEG": ["uint8"],
                "WEBP": ["uint8"],
                "JP2OPENJPEG": ["uint8", "int16", "uint16"],
            }
            valid_dtypes = format_dtypes.get(img_format, [])
            if valid_dtypes and array.dtype not in valid_dtypes:
                warnings.warn(
                    f"Invalid type: `{array.dtype}` for the `{img_format}` driver. Data will be rescaled using min/max type bounds or dataset_statistics.",
                    InvalidDatatypeWarning,
                )
                array = rescale_image(array, in_range=datatype_range)
                if mask is not None:
                    mask = linear_rescale(mask, in_range=dtype_ranges[str(array.dtype)])

        if add_mask:
            return render(
                array.data,
                mask,
                img_format=img_format,
                colormap=colormap,
                **kwargs,
            )

        return render(array.data, img_format=img_format, colormap=colormap, **kwargs)

    def to_raster(self, dst_path: str, *, driver: str = "GTIFF", **kwargs: Any) -> None:
        """Save ImageData array to file."""
        if driver.upper() == "GTIFF":
            if "transform" not in kwargs:
                kwargs.update({"transform": self.transform})
            if "crs" not in kwargs and self.crs:
                kwargs.update({"crs": self.crs})

        write_nodata = self.nodata is not None
        count, height, width = self.array.shape

        output_profile = {
            "dtype": self.array.dtype,
            "count": count if write_nodata else count + 1,
            "height": height,
            "width": width,
            "nodata": self.nodata,
        }
        output_profile.update(kwargs)

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            with rasterio.open(dst_path, "w", driver=driver, **output_profile) as dst:
                dst.write(self.data, indexes=list(range(1, count + 1)))

                # Use Mask as an alpha band
                if not write_nodata:
                    if ColorInterp.alpha not in dst.colorinterp:
                        dst.colorinterp = *dst.colorinterp[:-1], ColorInterp.alpha
                    dst.write(self.mask.astype(self.array.dtype), indexes=count + 1)

        return

    def statistics(
        self,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: Optional[List[int]] = None,
        hist_options: Optional[Dict] = None,
        coverage: Optional[numpy.ndarray] = None,
    ) -> Dict[str, BandStatistics]:
        """Return statistics from ImageData."""
        hist_options = hist_options or {}

        stats = get_array_statistics(
            self.array,
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            coverage=coverage,
            **hist_options,
        )

        return {
            f"{self.band_names[ix]}": BandStatistics(**stats[ix])
            for ix in range(len(stats))
        }

    def get_coverage_array(
        self,
        shape: Dict,
        shape_crs: CRS = WGS84_CRS,
        cover_scale: int = 10,
    ) -> NDArray[numpy.floating]:
        """Get Coverage array for a Geometry.

        Args:
            shape (Dict): GeoJSON geometry or Feature.
            shape_crs (rasterio.crs.CRS): Coordinates Reference System of shape.
            cover_scale (int, optional):
                Scale used when generating coverage estimates of each
                raster cell by vector feature. Coverage is generated by
                rasterizing the feature at a finer resolution than the raster then using a summation to aggregate
                to the raster resolution and dividing by the square of cover_scale
                to get coverage value for each cell. Increasing cover_scale
                will increase the accuracy of coverage values; three orders
                magnitude finer resolution (cover_scale=1000) is usually enough to
                get coverage estimates with <1% error in individual edge cells coverage
                estimates, though much smaller values (e.g., cover_scale=10) are often
                sufficient (<10% error) and require less memory.

        Returns:
            numpy.array: percent coverage.

        Note: code adapted from https://github.com/perrygeo/python-rasterstats/pull/136 by @sgoodm

        """
        shape = _validate_shape_input(shape)

        if self.crs != shape_crs:
            shape = transform_geom(shape_crs, self.crs, shape)

        cover_array = rasterize(
            [(shape, 1)],
            out_shape=(self.height * cover_scale, self.width * cover_scale),
            transform=self.transform * Affine.scale(1 / cover_scale),
            all_touched=True,
            fill=0,
            dtype="uint8",
        )
        cover_array = cover_array.reshape(
            (self.height, cover_scale, self.width, cover_scale)
        ).astype("float32")

        return cover_array.sum(-1).sum(1) / (cover_scale**2)

    def reproject(
        self,
        dst_crs: CRS,
        resolution: Optional[Tuple[float, float]] = None,
        reproject_method: WarpResampling = "nearest",
    ) -> "ImageData":
        """Reproject data and mask."""
        dst_transform, w, h = calculate_default_transform(
            self.crs,
            dst_crs,
            self.width,
            self.height,
            *self.bounds,
            resolution=resolution,
        )

        destination = numpy.ma.masked_array(
            numpy.zeros((self.count, h, w), dtype=self.array.dtype),
        )
        destination, _ = reproject(
            self.array,
            destination,
            src_transform=self.transform,
            src_crs=self.crs,
            dst_transform=dst_transform,
            dst_crs=dst_crs,
            resampling=Resampling[reproject_method],
        )

        alpha_mask = self.alpha_mask
        if self.alpha_mask is not None:
            alpha_mask = numpy.ma.masked_array(
                numpy.zeros((h, w), dtype=self.alpha_mask.dtype),
            )
            alpha_mask, _ = reproject(
                self.alpha_mask,
                alpha_mask,
                src_transform=self.transform,
                src_crs=self.crs,
                dst_transform=dst_transform,
                dst_crs=dst_crs,
                resampling=Resampling[reproject_method],
            )

        bounds = array_bounds(h, w, dst_transform)

        return ImageData(
            destination,
            assets=self.assets,
            crs=dst_crs,
            bounds=bounds,
            band_names=self.band_names,
            nodata=self.nodata,
            scales=self.scales,
            offsets=self.offsets,
            metadata=self.metadata,
            dataset_statistics=self.dataset_statistics,
            alpha_mask=alpha_mask,
        )
