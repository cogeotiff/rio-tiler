"""rio-tiler.reader: low level reader."""

import contextlib
import math
import warnings
from enum import IntEnum
from typing import Callable, Dict, Optional, Sequence, Tuple, TypedDict, Union

import numpy
from affine import Affine
from rasterio import windows
from rasterio.crs import CRS
from rasterio.enums import ColorInterp, MaskFlags, Resampling
from rasterio.io import DatasetReader, DatasetWriter
from rasterio.transform import array_bounds, from_bounds
from rasterio.vrt import WarpedVRT
from rasterio.warp import aligned_target, calculate_default_transform, reproject
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds

from rio_tiler.constants import WGS84_CRS
from rio_tiler.errors import (
    InvalidBufferSize,
    PointOutsideBounds,
    RioTilerError,
    TileOutsideBounds,
)
from rio_tiler.models import ImageData, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import _requested_tile_aligned_with_internal_tile as is_aligned
from rio_tiler.utils import (
    get_vrt_transform,
    has_alpha_band,
    has_mask_band,
    non_alpha_indexes,
)


class Options(TypedDict, total=False):
    """Reader Options."""

    nodata: Optional[NoData]
    reproject_options: Optional[Dict]
    resampling_method: Optional[RIOResampling]
    reproject_method: Optional[WarpResampling]
    unscale: Optional[bool]
    post_process: Optional[Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray]]


def _get_width_height(max_size, dataset_height, dataset_width) -> Tuple[int, int]:
    """Get Output Width/Height based on a max_size and dataset shape."""
    if max(dataset_height, dataset_width) < max_size:
        return dataset_height, dataset_width

    ratio = dataset_height / dataset_width
    if ratio > 1:
        height = max_size
        width = math.ceil(height / ratio)
    else:
        width = max_size
        height = math.ceil(width * ratio)

    return height, width


def _apply_buffer(
    buffer: float,
    bounds: BBox,
    height: int,
    width: int,
) -> Tuple[BBox, int, int]:
    """Apply buffer on bounds."""
    x_res = (bounds[2] - bounds[0]) / width
    y_res = (bounds[3] - bounds[1]) / height

    # apply buffer to bounds
    bounds = (
        bounds[0] - x_res * buffer,
        bounds[1] - y_res * buffer,
        bounds[2] + x_res * buffer,
        bounds[3] + y_res * buffer,
    )

    # new output size
    height += int(buffer * 2)
    width += int(buffer * 2)

    return bounds, height, width


def _read(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    indexes: Sequence[int],
    height: Optional[int] = None,
    width: Optional[int] = None,
    window: Optional[windows.Window] = None,
    nodata: Optional[NoData] = None,
    resampling_method: Resampling = Resampling.nearest,
) -> numpy.ma.MaskedArray:
    data = src_dst.read(
        indexes=indexes,
        window=window,
        out_shape=(len(indexes), height, width) if height and width else None,
        resampling=resampling_method,
        boundless=True,
        masked=True,
    )

    # if data has Nodata then we simply make sure the mask == the nodata
    nodata = nodata if nodata is not None else src_dst.nodata
    if nodata is not None:
        data.mask |= data == nodata

    return data


def read(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    dst_crs: Optional[CRS] = None,
    dst_bounds: Optional[BBox] = None,
    height: Optional[int] = None,
    width: Optional[int] = None,
    max_size: Optional[int] = None,
    indexes: Optional[Indexes] = None,
    window: Optional[windows.Window] = None,
    nodata: Optional[NoData] = None,
    buffer: Optional[float] = None,
    padding: Optional[int] = None,
    reproject_options: Optional[Dict] = None,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray]
    ] = None,
) -> ImageData:
    """Low level read function.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system.
        height (int, optional): Output height of the image.
        width (int, optional): Output width of the image.
        max_size (int, optional): Limit output size image if not width and height.
        indexes (sequence of int or int, optional): Band indexes.
        window (rasterio.windows.Window, optional): Window to read.
        nodata (int or float, optional): Overwrite dataset internal nodata value.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.
        reproject_options (dict, optional): Options to be passed to the rasterio.warp.reproject function.

    Returns:
        ImageData

    """
    reproject_options = reproject_options or {}
    padding = padding or 0
    buffer = buffer or 0

    if dst_bounds and window:
        raise RioTilerError("Can't use `bounds` and `window` together.")

    if buffer % 0.5:
        raise InvalidBufferSize(
            "`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
        )

    if isinstance(indexes, int):
        indexes = (indexes,)

    if max_size and width and height:
        warnings.warn(
            "'max_size' will be ignored with with 'height' and 'width' set.",
            UserWarning,
        )

    io_resampling = Resampling[resampling_method]
    warp_resampling = Resampling[reproject_method]

    if indexes is None:
        indexes = non_alpha_indexes(src_dst)

    if window and isinstance(window, tuple):
        window = windows.Window.from_slices(
            *window, height=src_dst.height, width=src_dst.width, boundless=True
        )

    dst_crs = dst_crs or src_dst.crs

    src_transform = src_dst.transform
    src_width = src_dst.width
    src_height = src_dst.height
    src_bounds = src_dst.bounds
    if dst_bounds:
        src_bounds = dst_bounds
        if dst_crs != src_dst.crs:
            src_bounds = transform_bounds(
                dst_crs, src_dst.crs, *dst_bounds, densify_pts=21
            )
        window = windows.from_bounds(*src_bounds, transform=src_dst.transform)
        src_width = max(1, window.width)
        src_height = max(1, window.height)
        src_transform = windows.transform(window, src_dst.transform)

    elif window:
        src_width = max(1, window.width)
        src_height = max(1, window.height)
        src_bounds = windows.bounds(window, src_dst.transform)
        src_transform = windows.transform(window, src_dst.transform)

    dst_crs = dst_crs or src_dst.crs
    # Case 1: Input projection != Output projection
    if dst_crs != src_dst.crs:
        # 1. get output transform from input bounds
        dst_transform, dst_width, dst_height = calculate_default_transform(
            src_dst.crs,
            dst_crs,
            src_width,
            src_height,
            *src_bounds,
        )

        dst_bounds = dst_bounds or array_bounds(dst_height, dst_width, dst_transform)

        # adjust dataset virtual output shape/transform
        w, s, e, n = dst_bounds
        dst_width = max(1, round((e - w) / dst_transform.a))
        dst_height = max(1, round((s - n) / dst_transform.e))
        dst_transform = from_bounds(w, s, e, n, dst_width, dst_height)

        # 2. adjust output size based on max_size if
        # - not input width/height
        # - max_size < dst_width and dst_height
        if (
            max_size
            and not (width and height)
            and max_size < max(dst_width, dst_height)
        ):
            height, width = _get_width_height(max_size, dst_height, dst_width)

        if buffer:
            w = width or dst_width
            h = height or dst_height

            # 2.1 new output bounds and shape
            dst_bounds, height, width = _apply_buffer(buffer, dst_bounds, h, w)

            # 2.2 update window / bounds
            src_bounds = dst_bounds
            if dst_crs != src_dst.crs:
                src_bounds = transform_bounds(
                    dst_crs, src_dst.crs, *dst_bounds, densify_pts=21
                )
            window = windows.from_bounds(*src_bounds, transform=src_dst.transform)

        # TODO: Padding

        # 3. if fixed output width/height, we need to
        # calculate input read size corresponding to the output size
        if height and width:
            src_transform, _, _ = calculate_default_transform(
                dst_crs,
                src_dst.crs,
                width,
                height,
                *dst_bounds,
            )

            w, s, e, n = src_bounds
            src_width = max(1, round((e - w) / src_transform.a))
            src_height = max(1, round((s - n) / src_transform.e))
            src_transform = from_bounds(w, s, e, n, src_width, src_height)

        # 4. read input data from dataset
        values = _read(
            src_dst,
            indexes=indexes,
            height=round(src_height),
            width=round(src_width),
            window=window,
            nodata=nodata,
            resampling_method=io_resampling,
        )

        height = height or dst_height
        width = width or dst_width

        # 5. adjust output transform
        dst_transform = from_bounds(*dst_bounds, width, height)

        # 6. re-project input array to output projection/shape
        count, _, _ = values.shape
        output_data = numpy.empty((count, height, width), dtype=values.dtype)
        reproject(
            values,
            output_data,
            src_transform=src_transform,
            dst_transform=dst_transform,
            src_crs=src_dst.crs,
            dst_crs=dst_crs,
            src_nodata=nodata,
            dst_nodata=nodata,
            resampling=warp_resampling,
            **reproject_options,
        )
        mask = values.mask
        if not mask.shape:
            mask = numpy.zeros(values.shape, dtype="uint8") != 0

        # 7. re-project input mask to output projection/shape
        output_mask = numpy.empty(output_data.shape, dtype=numpy.uint8)
        reproject(
            mask * 255,
            output_mask,
            src_transform=src_transform,
            dst_transform=dst_transform,
            src_crs=src_dst.crs,
            dst_crs=dst_crs,
            resampling=Resampling.nearest,
            src_nodata=255,
            dst_nodata=255,
            **reproject_options,
        )

        # 8. construct output masked Array
        data = numpy.ma.MaskedArray(output_data, mask=output_mask != 0)

    # Case 2: No re-projection
    else:
        if max_size and not (width and height):
            height, width = _get_width_height(max_size, src_height, src_width)

        height = height or src_height
        width = width or src_width

        dst_bounds = src_bounds
        if buffer:
            dst_bounds, height, width = _apply_buffer(buffer, src_bounds, height, width)
            window = windows.from_bounds(*dst_bounds, transform=src_dst.transform)

        if padding > 0 and not is_aligned(src_dst, src_bounds, bounds_crs=src_dst.crs):
            # For Padding we also use the buffer approach for non-VRT dataset
            pad_bounds, height, width = _apply_buffer(
                padding, src_bounds, height, width
            )
            window_pad = windows.from_bounds(*pad_bounds, transform=src_dst.transform)

            data = _read(
                src_dst,
                indexes=indexes,
                height=round(height),
                width=round(width),
                window=window_pad,
                nodata=nodata,
                resampling_method=io_resampling,
            )
            data = data[:, padding:-padding, padding:-padding]

        else:
            data = _read(
                src_dst,
                indexes=indexes,
                height=round(height),
                width=round(width),
                window=window,
                nodata=nodata,
                resampling_method=io_resampling,
            )

    stats = []
    for ix in indexes:
        tags = src_dst.tags(ix)
        if all(stat in tags for stat in ["STATISTICS_MINIMUM", "STATISTICS_MAXIMUM"]):
            stat_min = float(tags.get("STATISTICS_MINIMUM"))
            stat_max = float(tags.get("STATISTICS_MAXIMUM"))
            stats.append((stat_min, stat_max))

    # We only add dataset statistics if we have them for all the indexes
    dataset_statistics = stats if len(stats) == len(indexes) else None

    if unscale:
        data = data.astype("float32", casting="unsafe")
        numpy.multiply(data, src_dst.scales[0], out=data, casting="unsafe")
        numpy.add(data, src_dst.offsets[0], out=data, casting="unsafe")

    if post_process:
        data = post_process(data)

    return ImageData(
        data,
        bounds=dst_bounds,
        crs=dst_crs,
        band_names=[f"b{idx}" for idx in indexes],
        dataset_statistics=dataset_statistics,
        metadata=src_dst.tags(),
    )


# flake8: noqa: C901
def part(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: BBox,
    height: Optional[int] = None,
    width: Optional[int] = None,
    max_size: Optional[int] = None,
    dst_crs: Optional[CRS] = None,
    bounds_crs: Optional[CRS] = None,
    indexes: Optional[Indexes] = None,
    nodata: Optional[NoData] = None,
    minimum_overlap: Optional[float] = None,
    buffer: Optional[float] = None,
    padding: Optional[int] = None,
    reproject_options: Optional[Dict] = None,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray]
    ] = None,
) -> ImageData:
    """Read part of a dataset.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        bounds (tuple): Output bounds (left, bottom, right, top). By default the coordinates are considered to be in `bounds_crs` or `dst_crs` or `src_dst.crs`.
        height (int, optional): Output height of the image.
        width (int, optional): Output width of the image.
        max_size (int, optional): Limit output size image if not width and height.
        dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system.
        bounds_crs (rasterio.crs.CRS, optional): Overwrite bounds Coordinate Reference System.
        indexes (sequence of int or int, optional): Band indexes.
        minimum_overlap (float, optional): Minimum % overlap for which to raise an error with dataset not covering enough of the tile.
        padding (int, optional): Padding to apply to each bbox edge. Helps reduce resampling artefacts along edges. Defaults to `0`.
        buffer (float, optional): Buffer to apply to each bbox edge. Defaults to `0.`.
        nodata (int or float, optional): Overwrite dataset internal nodata value.
        vrt_options (dict, optional): Options to be passed to the rasterio.warp.WarpedVRT class.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.

    Returns:
        ImageData

    """
    if max_size and width and height:
        warnings.warn(
            "'max_size' will be ignored with with 'height' and 'width' set.",
            UserWarning,
        )

    # Bounds CRS default to:
    # 1. user input
    # 2. dst_crs
    # 3. dataset crs
    bounds_crs = bounds_crs or dst_crs or src_dst.crs
    dst_crs = dst_crs or src_dst.crs

    src_bounds = bounds
    if bounds_crs and bounds_crs != src_dst.crs:
        src_bounds = transform_bounds(
            bounds_crs, src_dst.crs, *src_bounds, densify_pts=21
        )

    dst_bounds = bounds
    if bounds_crs and bounds_crs != dst_crs:
        dst_bounds = transform_bounds(bounds_crs, dst_crs, *dst_bounds, densify_pts=21)

    if minimum_overlap:
        w, s, e, n = src_bounds
        x_overlap = max(
            0,
            min(src_dst.bounds[2], e) - max(src_dst.bounds[0], w),
        )
        y_overlap = max(
            0,
            min(src_dst.bounds[3], n) - max(src_dst.bounds[1], s),
        )
        cover_ratio = (x_overlap * y_overlap) / ((w - e) * (n - s))

        if cover_ratio < minimum_overlap:
            raise TileOutsideBounds(
                "Dataset covers less than {:.0f}% of tile".format(cover_ratio * 100)
            )

    return read(
        src_dst,
        dst_crs=dst_crs,
        dst_bounds=dst_bounds,
        indexes=indexes,
        width=width,
        height=height,
        max_size=max_size,
        nodata=nodata,
        buffer=buffer,
        padding=padding,
        reproject_options=reproject_options,
        resampling_method=resampling_method,
        reproject_method=reproject_method,
        unscale=unscale,
        post_process=post_process,
    )


def point(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    coordinates: Tuple[float, float],
    indexes: Optional[Indexes] = None,
    coord_crs: CRS = WGS84_CRS,
    nodata: Optional[NoData] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray]
    ] = None,
) -> PointData:
    """Read a pixel value for a point.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        coordinates (tuple): Coordinates in form of (X, Y).
        indexes (sequence of int or int, optional): Band indexes.
        coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
        nodata (int or float, optional): Overwrite dataset internal nodata value.
        vrt_options (dict, optional): Options to be passed to the rasterio.warp.WarpedVRT class.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.

    Returns:
        PointData

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    lon, lat = coordinates
    if coord_crs != src_dst.crs:
        xs, ys = transform_coords(coord_crs, src_dst.crs, [lon], [lat])
        lon, lat = xs[0], ys[0]

    if not (
        (src_dst.bounds[0] < lon < src_dst.bounds[2])
        and (src_dst.bounds[1] < lat < src_dst.bounds[3])
    ):
        raise PointOutsideBounds("Point is outside dataset bounds")

    row, col = src_dst.index(lon, lat)
    img = read(
        src_dst,
        indexes=indexes,
        window=windows.Window(row_off=row, col_off=col, width=1, height=1),
        resampling_method=resampling_method,
        nodata=nodata,
        unscale=unscale,
        post_process=post_process,
    )

    return PointData(
        img.array[:, 0, 0],
        coordinates=coordinates,
        crs=coord_crs,
        band_names=img.band_names,
        metadata=src_dst.tags(),
    )
