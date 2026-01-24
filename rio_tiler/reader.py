"""rio-tiler.reader: low level reader."""

import contextlib
import math
import warnings
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict, cast

import numpy
import rasterio
from affine import Affine
from rasterio import windows
from rasterio.crs import CRS
from rasterio.enums import ColorInterp, Resampling
from rasterio.io import DatasetReader, DatasetWriter
from rasterio.transform import array_bounds, rowcol
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds

from rio_tiler.constants import WGS84_CRS
from rio_tiler.errors import InvalidBufferSize, PointOutsideBounds, TileOutsideBounds
from rio_tiler.models import ImageData, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import _get_width_height, _missing_size
from rio_tiler.utils import _requested_tile_aligned_with_internal_tile as is_aligned
from rio_tiler.utils import (
    _round_window,
    cast_to_sequence,
    get_vrt_transform,
    has_alpha_band,
    non_alpha_indexes,
)


class Options(TypedDict, total=False):
    """Reader Options."""

    nodata: NoData | None
    vrt_options: dict | None
    resampling_method: RIOResampling | None
    reproject_method: WarpResampling | None
    unscale: bool | None
    post_process: Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray] | None


def _get_block_windows(
    dataset: DatasetReader,
    window: windows.Window,
) -> list[tuple[windows.Window, tuple[int, int]]]:
    """
    Calculate which internal COG blocks overlap with the requested window.

    Returns list of (block_window, (row_offset, col_offset)) tuples.
    """
    # Get the block size for band 1 (assuming all bands have same block size)
    block_height, block_width = dataset.block_shapes[0]

    # Calculate block indices that overlap with window
    col_start = int(window.col_off // block_width)
    col_end = int(math.ceil((window.col_off + window.width) / block_width))
    row_start = int(window.row_off // block_height)
    row_end = int(math.ceil((window.row_off + window.height) / block_height))

    block_windows = []
    for block_row in range(row_start, row_end):
        for block_col in range(col_start, col_end):
            # Calculate the window for this block
            block_window = windows.Window(
                col_off=block_col * block_width,
                row_off=block_row * block_height,
                width=block_width,
                height=block_height,
            )

            # Intersect with the requested window
            intersection = windows.intersection(block_window, window)
            if intersection.width > 0 and intersection.height > 0:
                # Calculate offset within output array
                out_row = int(intersection.row_off - window.row_off)
                out_col = int(intersection.col_off - window.col_off)
                block_windows.append((intersection, (out_row, out_col)))

    return block_windows


def _read_block_thread_safe(
    dataset_path: str,
    block_window: windows.Window,
    indexes: tuple[int, ...],
    out_dtype: str | numpy.dtype | None = None,
    resampling: str = "nearest",
) -> numpy.ma.MaskedArray:
    """Read a single block from the dataset using a fresh connection (thread-safe)."""
    # Open a fresh connection for thread safety - rasterio datasets are NOT thread-safe
    with rasterio.open(dataset_path) as dataset:
        return dataset.read(
            indexes=indexes,
            window=block_window,
            resampling=Resampling[resampling],
            out_dtype=out_dtype,
            masked=True,
        )


def _parallel_block_read(
    dataset: DatasetReader,
    window: windows.Window,
    indexes: tuple[int, ...],
    out_dtype: str | numpy.dtype | None = None,
    resampling_method: str = "nearest",
    max_workers: int = 8,
) -> numpy.ma.MaskedArray:
    """
    Read a window from a COG using parallel block reads.

    This function identifies which internal COG blocks overlap with the
    requested window and reads them in parallel using a thread pool.
    Each thread opens its own dataset connection for thread safety.

    Args:
        dataset: Open rasterio dataset (used for metadata only)
        window: Window to read
        indexes: Band indexes to read
        out_dtype: Output data type
        resampling_method: Resampling method
        max_workers: Maximum number of parallel reads

    Returns:
        numpy.ma.MaskedArray with the requested data
    """
    # Get the dataset path for thread-safe reads
    dataset_path = dataset.name

    # Get blocks that overlap with window
    block_windows = _get_block_windows(dataset, window)

    # If only one block, just read directly (no parallelism overhead)
    if len(block_windows) <= 1:
        return dataset.read(
            indexes=indexes,
            window=window,
            resampling=Resampling[resampling_method],
            out_dtype=out_dtype,
            masked=True,
        )

    # Prepare output array
    out_height = int(window.height)
    out_width = int(window.width)

    # Determine dtype
    dtype = out_dtype or dataset.dtypes[0]
    output = numpy.ma.zeros((len(indexes), out_height, out_width), dtype=dtype)
    output.mask = numpy.ones_like(output, dtype=bool)

    def read_and_place(
        block_info: tuple[windows.Window, tuple[int, int]]
    ) -> tuple[numpy.ma.MaskedArray, tuple[int, int, int, int]]:
        block_window, (out_row, out_col) = block_info

        # Read the block using a fresh connection (thread-safe)
        data = _read_block_thread_safe(
            dataset_path, block_window, indexes, out_dtype, resampling_method
        )

        return data, (
            out_row,
            out_col,
            int(block_window.height),
            int(block_window.width),
        )

    # Read blocks in parallel
    with ThreadPoolExecutor(
        max_workers=min(max_workers, len(block_windows))
    ) as executor:
        futures = {executor.submit(read_and_place, bw): bw for bw in block_windows}

        for future in as_completed(futures):
            data, (row, col, h, w) = future.result()
            # Clip to output bounds
            out_h = min(h, out_height - row)
            out_w = min(w, out_width - col)
            output[:, row : row + out_h, col : col + out_w] = data[:, :out_h, :out_w]
            output.mask[:, row : row + out_h, col : col + out_w] = data.mask[
                :, :out_h, :out_w
            ]

    return output


def _apply_buffer(
    buffer: float,
    bounds: BBox,
    height: int,
    width: int,
) -> tuple[BBox, int, int]:
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


def read(
    src_dst: DatasetReader | DatasetWriter | WarpedVRT,
    dst_crs: CRS | None = None,
    height: int | None = None,
    width: int | None = None,
    max_size: int | None = None,
    indexes: Indexes | None = None,
    window: windows.Window | None = None,
    nodata: NoData | None = None,
    vrt_options: dict | None = None,
    out_dtype: str | numpy.dtype | None = None,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    unscale: bool = False,
    post_process: Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray] | None = None,
    max_workers: int | None = None,
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
        vrt_options (dict, optional): Options to be passed to the rasterio.warp.WarpedVRT class.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.
        max_workers (int, optional): Maximum number of parallel workers for block reads.
            When set and > 1, reads spanning multiple internal COG blocks will be
            parallelized for improved performance, especially with remote COGs.

    Returns:
        ImageData

    """
    indexes = cast_to_sequence(indexes)

    if max_size and (width or height):
        warnings.warn(
            "'max_size' will be ignored with with 'height' or 'width' set.",
            UserWarning,
        )
        max_size = None

    io_resampling = Resampling[resampling_method]
    warp_resampling = Resampling[reproject_method]

    nodata = nodata if nodata is not None else src_dst.nodata

    dst_crs = dst_crs or src_dst.crs
    with contextlib.ExitStack() as ctx:
        # Use WarpedVRT when Re-projection or User VRT Option (cutline)
        if (dst_crs != src_dst.crs) or vrt_options:
            vrt_params = {
                "crs": dst_crs,
                "add_alpha": True,
                "resampling": warp_resampling,
                "dtype": src_dst.dtypes[0],
            }

            if nodata is not None:
                vrt_params.update(
                    {
                        "nodata": nodata,
                        "add_alpha": False,
                        "src_nodata": nodata,
                    }
                )

            if has_alpha_band(src_dst):
                vrt_params.update({"add_alpha": False})

            if vrt_options:
                vrt_params.update(**vrt_options)

            # TODO: Check if we fetch the Overviews when not using transform
            dataset = ctx.enter_context(WarpedVRT(src_dst, **vrt_params))

        else:
            dataset = src_dst

        if indexes is None:
            indexes = non_alpha_indexes(dataset)

        max_height, max_width = dataset.height, dataset.width

        boundless = False
        if window:
            if isinstance(window, tuple):
                window = windows.Window.from_slices(
                    *window, height=dataset.height, width=dataset.width, boundless=True
                )

            (row_start, row_stop), (col_start, col_stop) = window.toranges()
            if (
                min(col_start, row_start) < 0
                or col_stop >= dataset.width
                or row_stop >= dataset.height
            ):
                boundless = True

            max_height, max_width = window.height, window.width

        if max_size:
            height, width = _get_width_height(max_size, max_height, max_width)

        elif _missing_size(width, height):
            ratio = max_height / max_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        if ColorInterp.alpha in dataset.colorinterp and nodata is None:
            # If dataset has an alpha band we need to get the mask using the alpha band index
            # and then split the data and mask values
            alpha_idx = dataset.colorinterp.index(ColorInterp.alpha) + 1

            # Read Data and Mask separately
            # Special case (see https://github.com/rasterio/rasterio/issues/2798)
            if dataset.dtypes[alpha_idx - 1] != dataset.dtypes[indexes[0] - 1]:
                values = dataset.read(
                    indexes=indexes,
                    window=window,
                    out_shape=(
                        (len(indexes), height, width) if height and width else None
                    ),
                    resampling=io_resampling,
                    boundless=boundless,
                    out_dtype=out_dtype,
                )
                mask = dataset.read(
                    indexes=(alpha_idx,),
                    window=window,
                    out_shape=(1, height, width) if height and width else None,
                    resampling=io_resampling,
                    boundless=boundless,
                    out_dtype=out_dtype,
                )
                data = numpy.ma.MaskedArray(values)
                data.mask = ~mask.astype("bool")

            else:
                idx = tuple(indexes) + (alpha_idx,)
                values = dataset.read(
                    indexes=idx,
                    window=window,
                    out_shape=(len(idx), height, width) if height and width else None,
                    resampling=io_resampling,
                    boundless=boundless,
                    out_dtype=out_dtype,
                )
                mask = ~values[-1].astype("bool")
                data = numpy.ma.MaskedArray(values[0:-1])
                data.mask = mask

        else:
            # Check if we should use parallel block reads
            use_parallel = False
            if (
                max_workers
                and max_workers > 1
                and window
                and not boundless
                and not (height and width)  # No resampling needed
                and isinstance(src_dst, DatasetReader)  # Not a VRT
                and hasattr(src_dst, "block_shapes")
            ):
                # Check if window spans multiple blocks
                block_h, block_w = src_dst.block_shapes[0]
                blocks_x = math.ceil(window.width / block_w)
                blocks_y = math.ceil(window.height / block_h)
                if blocks_x * blocks_y > 1:
                    use_parallel = True

            if use_parallel:
                # Use parallel block reads for better performance
                data = _parallel_block_read(
                    src_dst,
                    window=window,
                    indexes=tuple(indexes),
                    out_dtype=out_dtype,
                    resampling_method=resampling_method,
                    max_workers=max_workers,
                )
            else:
                data = dataset.read(
                    indexes=indexes,
                    window=window,
                    out_shape=(len(indexes), height, width) if height and width else None,
                    resampling=io_resampling,
                    boundless=boundless,
                    masked=True,
                    fill_value=nodata,
                    out_dtype=out_dtype,
                )

            # if data has Nodata then we simply make sure the mask == the nodata
            if nodata is not None:
                if numpy.isnan(nodata):
                    data.mask = numpy.isnan(data.data)
                else:
                    data.mask = data.data == nodata

        stats = []
        for ix in indexes:
            tags = dataset.tags(ix)
            if all(stat in tags for stat in ["STATISTICS_MINIMUM", "STATISTICS_MAXIMUM"]):
                stat_min = float(tags.get("STATISTICS_MINIMUM"))
                stat_max = float(tags.get("STATISTICS_MAXIMUM"))
                stats.append((stat_min, stat_max))

        # We only add dataset statistics if we have them for all the indexes
        dataset_statistics = stats if len(stats) == len(indexes) else None

        scales = numpy.array(dataset.scales)[numpy.array(indexes) - 1]
        offsets = numpy.array(dataset.offsets)[numpy.array(indexes) - 1]
        if unscale:
            data = cast(
                numpy.ma.MaskedArray,
                data.astype("float32", casting="unsafe"),
            )

            numpy.multiply(data, scales.reshape((-1, 1, 1)), out=data, casting="unsafe")
            numpy.add(data, offsets.reshape((-1, 1, 1)), out=data, casting="unsafe")

            # apply scale/offsets to stats
            if dataset_statistics:
                stats_array = numpy.array(dataset_statistics)
                numpy.multiply(
                    stats_array,
                    scales.reshape((-1, 1)),
                    out=stats_array,
                    casting="unsafe",
                )
                numpy.add(
                    stats_array,
                    offsets.reshape((-1, 1)),
                    out=stats_array,
                    casting="unsafe",
                )
                dataset_statistics = [tuple(s) for s in stats_array.tolist()]

            scales = numpy.zeros(len(indexes)) + 1.0
            offsets = numpy.zeros(len(indexes))

        if post_process:
            data = post_process(data)

        out_bounds = (
            windows.bounds(window, dataset.transform) if window else dataset.bounds
        )

        return ImageData(
            data,
            bounds=out_bounds,
            crs=dataset.crs,
            band_names=[f"b{idx}" for idx in indexes],
            band_descriptions=[dataset.descriptions[ix - 1] or "" for idx in indexes],
            dataset_statistics=dataset_statistics,
            metadata=dataset.tags(),
            nodata=nodata,
            scales=scales.tolist(),
            offsets=offsets.tolist(),
        )


# flake8: noqa: C901
def part(
    src_dst: DatasetReader | DatasetWriter | WarpedVRT,
    bounds: BBox,
    height: int | None = None,
    width: int | None = None,
    max_size: int | None = None,
    dst_crs: CRS | None = None,
    bounds_crs: CRS | None = None,
    indexes: Indexes | None = None,
    minimum_overlap: float | None = None,
    padding: int | None = None,
    buffer: float | None = None,
    nodata: NoData | None = None,
    vrt_options: dict | None = None,
    out_dtype: str | numpy.dtype | None = None,
    align_bounds_with_dataset: bool = False,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    unscale: bool = False,
    post_process: Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray] | None = None,
    max_workers: int | None = None,
) -> ImageData:
    """Read part of a dataset.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        bounds (tuple): Output bounds (left, bottom, right, top). By default the coordinates are considered to be in either the dataset CRS or in the `dst_crs` if set. Use `bounds_crs` to set a specific CRS.
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
        align_bounds_with_dataset (bool): Align input bounds with dataset transform. Defaults to `False`.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.
        max_workers (int, optional): Maximum number of parallel workers for block reads.
            When set and > 1, reads spanning multiple internal COG blocks will be
            parallelized for improved performance, especially with remote COGs.

    Returns:
        ImageData

    """
    if max_size and (width or height):
        warnings.warn(
            "'max_size' will be ignored with with 'height' or 'width' set.",
            UserWarning,
        )
        max_size = None

    if buffer and buffer % 0.5:
        raise InvalidBufferSize(
            "`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
        )

    padding = padding or 0
    dst_crs = dst_crs or src_dst.crs
    if bounds_crs and bounds_crs != dst_crs:
        bounds = transform_bounds(bounds_crs, dst_crs, *bounds, densify_pts=21)

    if minimum_overlap:
        src_bounds = transform_bounds(
            src_dst.crs, dst_crs, *src_dst.bounds, densify_pts=21
        )
        x_overlap = max(0, min(src_bounds[2], bounds[2]) - max(src_bounds[0], bounds[0]))
        y_overlap = max(0, min(src_bounds[3], bounds[3]) - max(src_bounds[1], bounds[1]))
        cover_ratio = (x_overlap * y_overlap) / (
            (bounds[2] - bounds[0]) * (bounds[3] - bounds[1])
        )

        if cover_ratio < minimum_overlap:
            raise TileOutsideBounds(
                "Dataset covers less than {:.0f}% of tile".format(cover_ratio * 100)
            )

    # Use WarpedVRT when Re-projection or User VRT Option (cutline)
    if (dst_crs != src_dst.crs) or vrt_options or isinstance(src_dst, WarpedVRT):
        window = None
        vrt_transform, vrt_width, vrt_height = get_vrt_transform(
            src_dst,
            bounds,
            height,
            width,
            dst_crs=dst_crs,
            align_bounds_with_dataset=align_bounds_with_dataset,
        )
        bounds = array_bounds(vrt_height, vrt_width, vrt_transform)

        if max_size:
            height, width = _get_width_height(max_size, vrt_height, vrt_width)

        elif _missing_size(width, height):
            ratio = vrt_height / vrt_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        height = height or vrt_height
        width = width or vrt_width

        if buffer:
            bounds, height, width = _apply_buffer(buffer, bounds, height, width)

            # re-calculate the transform given the new bounds, height and width
            vrt_transform, vrt_width, vrt_height = get_vrt_transform(
                src_dst,
                bounds,
                height,
                width,
                dst_crs=dst_crs,
                align_bounds_with_dataset=align_bounds_with_dataset,
            )
            bounds = array_bounds(vrt_height, vrt_width, vrt_transform)

        if padding > 0 and not is_aligned(src_dst, bounds, bounds_crs=dst_crs):
            vrt_transform = vrt_transform * Affine.translation(-padding, -padding)
            window = windows.Window(
                col_off=padding, row_off=padding, width=vrt_width, height=vrt_height
            )
            vrt_height = vrt_height + 2 * padding
            vrt_width = vrt_width + 2 * padding

        vrt_params = {
            "crs": dst_crs,
            "transform": vrt_transform,
            "width": vrt_width,
            "height": vrt_height,
            "dtype": src_dst.dtypes[0],
        }
        if vrt_options:
            vrt_params.update(**vrt_options)

        return read(
            src_dst,
            indexes=indexes,
            width=width,
            height=height,
            window=window,
            nodata=nodata,
            vrt_options=vrt_params,
            out_dtype=out_dtype,
            resampling_method=resampling_method,
            reproject_method=reproject_method,
            unscale=unscale,
            post_process=post_process,
            max_workers=max_workers,
        )

    # else no re-projection needed
    window = windows.from_bounds(*bounds, transform=src_dst.transform)
    if align_bounds_with_dataset:
        window = _round_window(window)
        bounds = windows.bounds(window, src_dst.transform)

    if max_size:
        height, width = _get_width_height(
            max_size, round(window.height), round(window.width)
        )

    elif _missing_size(width, height):
        ratio = window.height / window.width
        if width:
            height = math.ceil(width * ratio)
        else:
            width = math.ceil(height / ratio)

    height = height or max(1, round(window.height))
    width = width or max(1, round(window.width))

    if buffer:
        bounds, height, width = _apply_buffer(buffer, bounds, height, width)
        window = windows.from_bounds(*bounds, transform=src_dst.transform)

    if padding > 0 and not is_aligned(src_dst, bounds, bounds_crs=dst_crs):
        # For Padding we also use the buffer approach for non-VRT dataset
        pad_bounds, height, width = _apply_buffer(padding, bounds, height, width)
        window = windows.from_bounds(*pad_bounds, transform=src_dst.transform)

        img = read(
            src_dst,
            indexes=indexes,
            width=width,
            height=height,
            window=window,
            nodata=nodata,
            out_dtype=out_dtype,
            resampling_method=resampling_method,
            reproject_method=reproject_method,
            unscale=unscale,
            post_process=post_process,
            max_workers=max_workers,
        )

        return ImageData(
            img.array[:, padding:-padding, padding:-padding],
            bounds=bounds,
            crs=img.crs,
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            nodata=img.nodata,
            scales=img.scales,
            offsets=img.offsets,
            dataset_statistics=img.dataset_statistics,
            metadata=img.metadata,
        )

    return read(
        src_dst,
        indexes=indexes,
        width=width,
        height=height,
        window=window,
        nodata=nodata,
        out_dtype=out_dtype,
        resampling_method=resampling_method,
        reproject_method=reproject_method,
        unscale=unscale,
        post_process=post_process,
        max_workers=max_workers,
    )


def point(
    src_dst: DatasetReader | DatasetWriter | WarpedVRT,
    coordinates: tuple[float, float],
    indexes: Indexes | None = None,
    coord_crs: CRS = WGS84_CRS,
    nodata: NoData | None = None,
    vrt_options: dict | None = None,
    out_dtype: str | numpy.dtype | None = None,
    resampling_method: RIOResampling = "nearest",
    reproject_method: WarpResampling = "nearest",
    interpolate: bool = False,
    unscale: bool = False,
    post_process: Callable[[numpy.ma.MaskedArray], numpy.ma.MaskedArray] | None = None,
) -> PointData:
    """Read a pixel value for a point.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        coordinates (tuple): Coordinates in form of (X, Y).
        indexes (sequence of int or int, optional): Band indexes.
        coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
        nodata (int or float, optional): Overwrite dataset internal nodata value.
        vrt_options (dict, optional): Options to be passed to the rasterio.warp.WarpedVRT class.
        resampling_method (RIOResampling, optional): RasterIO resampling algorithm. Only used when `interpolate=True`. Defaults to `nearest`.
        reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
        interpolate (bool, optional): Interpolate pixels around the coordinates. Defaults to `False`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.

    Returns:
        PointData

    """
    indexes = cast_to_sequence(indexes)

    with contextlib.ExitStack() as ctx:
        # Use WarpedVRT when User provided Nodata or VRT Option (cutline)
        if nodata is not None or vrt_options:
            vrt_params = {
                "add_alpha": True,
                "resampling": Resampling[reproject_method],
                "dtype": src_dst.dtypes[0],
            }
            nodata = nodata if nodata is not None else src_dst.nodata
            if nodata is not None:
                vrt_params.update(
                    {"nodata": nodata, "add_alpha": False, "src_nodata": nodata}
                )

            if has_alpha_band(src_dst):
                vrt_params.update({"add_alpha": False})

            if vrt_options:
                vrt_params.update(**vrt_options)

            dataset = ctx.enter_context(WarpedVRT(src_dst, **vrt_params))

        else:
            dataset = src_dst

        lon, lat = coordinates
        if coord_crs != dataset.crs:
            xs, ys = transform_coords(coord_crs, dataset.crs, [lon], [lat])
            lon, lat = xs[0], ys[0]

        dataset_min_lon, dataset_min_lat, dataset_max_lon, dataset_max_lat = (
            dataset.bounds
        )
        # check if latitude is inverted
        if dataset_min_lat > dataset_max_lat:
            warnings.warn(
                "BoundingBox of the dataset is inverted (minLat > maxLat).",
                UserWarning,
            )

        dataset_min_lat, dataset_max_lat = (
            min(dataset_min_lat, dataset_max_lat),
            max(dataset_min_lat, dataset_max_lat),
        )
        if not (
            (dataset_min_lon < lon < dataset_max_lon)
            and (dataset_min_lat < lat < dataset_max_lat)
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        if interpolate:
            # Ref: https://github.com/cogeotiff/rio-tiler/issues/793
            # https://github.com/OSGeo/gdal/blob/a3d68b069e6b3676ba437faca5dca6ae2076ce24/swig/python/gdal-utils/osgeo_utils/samples/gdallocationinfo.py#L185-L197
            rows, cols = rowcol(dataset.transform, xs=[lon], ys=[lat], op=lambda x: x)
            row, col = float(rows[0]), float(cols[0])
            row_off, col_off = row - 0.5, col - 0.5

        else:
            if resampling_method != "nearest":
                warnings.warn(
                    f"{resampling_method} resampling will be ignored when `interpolate=False`.",
                    UserWarning,
                )

            row, col = dataset.index(lon, lat)
            row_off, col_off = row, col

        window = windows.Window(row_off=row_off, col_off=col_off, width=1, height=1)

        img = read(
            dataset,
            indexes=indexes,
            window=window,
            out_dtype=out_dtype,
            resampling_method=resampling_method,
            unscale=unscale,
            post_process=post_process,
        )

        return PointData(
            img.array[:, 0, 0],
            band_names=img.band_names,
            band_descriptions=img.band_descriptions,
            coordinates=coordinates,
            crs=coord_crs,
            pixel_location=(col, row),
            nodata=img.nodata,
            scales=img.scales,
            offsets=img.offsets,
            metadata=img.metadata,
        )
