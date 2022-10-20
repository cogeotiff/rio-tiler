"""rio-tiler.reader: low level reader."""

import contextlib
import math
import warnings
from typing import Callable, Dict, Optional, Tuple, TypedDict, Union

import numpy
from affine import Affine
from rasterio import windows
from rasterio.crs import CRS
from rasterio.enums import ColorInterp, Resampling
from rasterio.io import DatasetReader, DatasetWriter
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds

from rio_tiler.constants import WGS84_CRS
from rio_tiler.errors import InvalidBufferSize, PointOutsideBounds, TileOutsideBounds
from rio_tiler.models import ImageData, PointData
from rio_tiler.types import BBox, DataMaskType, Indexes, NoData
from rio_tiler.utils import _requested_tile_aligned_with_internal_tile as is_aligned
from rio_tiler.utils import get_vrt_transform, has_alpha_band, non_alpha_indexes


class Options(TypedDict, total=False):
    """Reader Options."""

    force_binary_mask: Optional[bool]
    nodata: Optional[NoData]
    vrt_options: Optional[Dict]
    resampling_method: Optional[Resampling]
    unscale: Optional[bool]
    post_process: Optional[Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]]


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


def read(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    dst_crs: Optional[CRS] = None,
    height: Optional[int] = None,
    width: Optional[int] = None,
    max_size: Optional[int] = None,
    indexes: Optional[Indexes] = None,
    window: Optional[windows.Window] = None,
    force_binary_mask: bool = True,
    nodata: Optional[NoData] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Resampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
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
        vrt_options (dict, optional): Options to be passed to the rasterio.warp.WarpedVRT class.
        resampling_method (rasterio.enums.Resampling, optional): Rasterio's resampling algorithm. Defaults to `nearest`.
        force_binary_mask (bool, optional): Cast returned mask to binary values (0 or 255). Defaults to `True`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.

    Returns:
        ImageData

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    if max_size and width and height:
        warnings.warn(
            "'max_size' will be ignored with with 'height' and 'width' set.",
            UserWarning,
        )

    resampling = Resampling[resampling_method]
    dst_crs = dst_crs or src_dst.crs
    with contextlib.ExitStack() as ctx:
        # Use WarpedVRT when Re-projection or Nodata or User VRT Option (cutline)
        if (dst_crs != src_dst.crs) or nodata is not None or vrt_options:
            vrt_params = {
                "crs": dst_crs,
                "add_alpha": True,
                "resampling": resampling,
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

            # TODO: Check if we fetch the Overviews when not using transform
            dataset = ctx.enter_context(WarpedVRT(src_dst, **vrt_params))

        else:
            dataset = src_dst

        if max_size and not (width and height):
            height, width = _get_width_height(max_size, dataset.height, dataset.width)

        if indexes is None:
            indexes = non_alpha_indexes(dataset)

        boundless = False
        if window:
            if isinstance(window, tuple):
                window = windows.Window.from_slices(
                    *window, height=dataset.height, width=dataset.width, boundless=True
                )

            (row_start, row_stop), (col_start, col_stop) = window.toranges()
            if (
                min(col_start, row_start) < 0
                or row_stop >= dataset.width
                or col_stop >= dataset.height
            ):
                boundless = True

        if ColorInterp.alpha in dataset.colorinterp:
            # If dataset has an alpha band we need to get the mask using the alpha band index
            # and then split the data and mask values
            alpha_idx = dataset.colorinterp.index(ColorInterp.alpha) + 1
            idx = tuple(indexes) + (alpha_idx,)
            data = dataset.read(
                indexes=idx,
                window=window,
                out_shape=(len(idx), height, width) if height and width else None,
                resampling=resampling,
                boundless=boundless,
            )
            data, mask = data[0:-1], data[-1].astype("uint8")

        else:
            data = dataset.read(
                indexes=indexes,
                window=window,
                out_shape=(len(indexes), height, width) if height and width else None,
                resampling=resampling,
                boundless=boundless,
            )
            mask = dataset.dataset_mask(
                window=window,
                out_shape=(height, width) if height and width else None,
                resampling=resampling,
                boundless=boundless,
            )

        stats = []
        for ix in indexes:
            tags = dataset.tags(ix)
            if all(
                stat in tags for stat in ["STATISTICS_MINIMUM", "STATISTICS_MAXIMUM"]
            ):
                stat_min = float(tags.get("STATISTICS_MINIMUM"))
                stat_max = float(tags.get("STATISTICS_MAXIMUM"))
                stats.append((stat_min, stat_max))

        # We only add dataset statistics if we have them for all the indexes
        dataset_statistics = stats if len(stats) == len(indexes) else None

        if force_binary_mask:
            mask = numpy.where(mask != 0, numpy.uint8(255), numpy.uint8(0))

        if unscale:
            data = data.astype("float32", casting="unsafe")
            numpy.multiply(data, dataset.scales[0], out=data, casting="unsafe")
            numpy.add(data, dataset.offsets[0], out=data, casting="unsafe")

        if post_process:
            data, mask = post_process(data, mask)

        out_bounds = (
            windows.bounds(window, dataset.transform) if window else dataset.bounds
        )

        img = ImageData(
            data,
            mask,
            bounds=out_bounds,
            crs=dataset.crs,
            band_names=[f"b{idx}" for idx in indexes],
            dataset_statistics=dataset_statistics,
        )

    return img


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
    minimum_overlap: Optional[float] = None,
    padding: Optional[int] = None,
    buffer: Optional[float] = None,
    force_binary_mask: bool = True,
    nodata: Optional[NoData] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Resampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
    ] = None,
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
        resampling_method (rasterio.enums.Resampling, optional): Rasterio's resampling algorithm. Defaults to `nearest`.
        force_binary_mask (bool, optional): Cast returned mask to binary values (0 or 255). Defaults to `True`.
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

    if buffer and buffer % 0.5:
        raise InvalidBufferSize(
            "`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
        )

    padding = padding or 0
    dst_crs = dst_crs or src_dst.crs
    if bounds_crs:
        bounds = transform_bounds(bounds_crs, dst_crs, *bounds, densify_pts=21)

    if minimum_overlap:
        src_bounds = transform_bounds(
            src_dst.crs, dst_crs, *src_dst.bounds, densify_pts=21
        )
        x_overlap = max(
            0, min(src_bounds[2], bounds[2]) - max(src_bounds[0], bounds[0])
        )
        y_overlap = max(
            0, min(src_bounds[3], bounds[3]) - max(src_bounds[1], bounds[1])
        )
        cover_ratio = (x_overlap * y_overlap) / (
            (bounds[2] - bounds[0]) * (bounds[3] - bounds[1])
        )

        if cover_ratio < minimum_overlap:
            raise TileOutsideBounds(
                "Dataset covers less than {:.0f}% of tile".format(cover_ratio * 100)
            )

    # Use WarpedVRT when Re-projection or Nodata or User VRT Option (cutline)
    if (dst_crs != src_dst.crs) or nodata is not None or vrt_options:
        window = None
        vrt_transform, vrt_width, vrt_height = get_vrt_transform(
            src_dst,
            bounds,
            height=height,
            width=width,
            dst_crs=dst_crs,
        )

        if max_size and not (width and height):
            height, width = _get_width_height(max_size, vrt_height, vrt_width)

        height = height or vrt_height
        width = width or vrt_width

        if buffer:
            bounds, height, width = _apply_buffer(buffer, bounds, height, width)
            # re-calculate the transform given the new bounds, height and width
            vrt_transform, vrt_width, vrt_height = get_vrt_transform(
                src_dst, bounds, height, width, dst_crs=dst_crs
            )

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
            resampling_method=resampling_method,
            force_binary_mask=force_binary_mask,
            unscale=unscale,
            post_process=post_process,
        )

    # else no re-projection needed
    window = windows.from_bounds(*bounds, transform=src_dst.transform)
    if max_size and not (width and height):
        height, width = _get_width_height(
            max_size, round(window.height), round(window.width)
        )

    height = height or round(window.height)
    width = width or round(window.width)

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
            resampling_method=resampling_method,
            force_binary_mask=force_binary_mask,
            unscale=unscale,
            post_process=post_process,
        )
        return ImageData(
            data=img.data[:, padding:-padding, padding:-padding],
            mask=img.mask[padding:-padding, padding:-padding],
            bounds=bounds,
            crs=img.crs,
            band_names=img.band_names,
            dataset_statistics=img.dataset_statistics,
        )

    return read(
        src_dst,
        indexes=indexes,
        width=width,
        height=height,
        window=window,
        resampling_method=resampling_method,
        force_binary_mask=force_binary_mask,
        unscale=unscale,
        post_process=post_process,
    )


def point(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    coordinates: Tuple[float, float],
    indexes: Optional[Indexes] = None,
    coord_crs: CRS = WGS84_CRS,
    force_binary_mask: bool = True,
    nodata: Optional[NoData] = None,
    vrt_options: Optional[Dict] = None,
    resampling_method: Resampling = "nearest",
    unscale: bool = False,
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
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
        resampling_method (rasterio.enums.Resampling, optional): Rasterio's resampling algorithm. Defaults to `nearest`.
        unscale (bool, optional): Apply 'scales' and 'offsets' on output data value. Defaults to `False`.
        post_process (callable, optional): Function to apply on output data and mask values.

    Returns:
        PointData

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    with contextlib.ExitStack() as ctx:
        # Use WarpedVRT when Re-projection or Nodata or User VRT Option (cutline)
        if nodata is not None or vrt_options:
            vrt_params = {
                "add_alpha": True,
                "resampling": Resampling[resampling_method],
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

        if not (
            (dataset.bounds[0] < lon < dataset.bounds[2])
            and (dataset.bounds[1] < lat < dataset.bounds[3])
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        row, col = dataset.index(lon, lat)
        img = read(
            dataset,
            indexes=indexes,
            window=windows.Window(row_off=row, col_off=col, width=1, height=1),
            resampling_method=resampling_method,
            force_binary_mask=force_binary_mask,
            unscale=unscale,
            post_process=post_process,
        )

    return PointData(
        img.data[:, 0, 0],
        numpy.array([img.mask[0, 0]]),
        coordinates=coordinates,
        crs=coord_crs,
        band_names=img.band_names,
    )
