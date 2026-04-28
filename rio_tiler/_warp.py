"""rio-tiler warping utilities."""

from __future__ import annotations

import numpy
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import Resampling
from rasterio.transform import from_bounds
from rasterio.warp import calculate_default_transform, reproject

from rio_tiler.models import ImageData
from rio_tiler.types import BBox, RIOResampling, WarpResampling
from rio_tiler.utils import resize_array

# Output tile size (in pixels) used to bound intermediate memory during warp.
# Each intermediate chunk is at most (native_res/output_res * _TILE_SIZE)² pixels.
_TILE_SIZE = 2048


def warp(
    img: ImageData,
    *,
    dst_crs: CRS,
    dst_bounds: BBox,
    dst_width: int,
    dst_height: int,
    reproject_method: WarpResampling = "nearest",
    resampling_method: RIOResampling = "nearest",
) -> ImageData:
    """Reproject and resample an ImageData object.

    Step 1 — Reproject (only when src CRS != dst CRS): for each output tile,
    reprojects the corresponding source region to the intermediate (native)
    resolution using `reproject_method` (warp kernel).

    Step 2 — Resample: resamples each intermediate tile to the final tile size
    using `resampling_method`.

    Processing is done tile-by-tile over the output grid so that the peak
    intermediate allocation is bounded by _TILE_SIZE rather than the full
    native resolution extent.
    """
    # Compute native resolution in dst_crs
    dst_transform, _, _ = calculate_default_transform(
        img.crs, dst_crs, img.width, img.height, *img.bounds
    )

    w_res = dst_transform.a  # positive
    h_res = dst_transform.e  # negative (north-up)
    w, s, e, n = dst_bounds
    native_width = max(1, round((e - w) / w_res))
    native_height = max(1, round((s - n) / h_res))

    # Allocate output arrays at the final size (never the full intermediate size)
    dst_data = numpy.zeros((img.count, dst_height, dst_width), dtype=img.array.dtype)
    dst_mask = numpy.zeros((img.count, dst_height, dst_width), dtype=numpy.uint8)

    has_alpha = img.alpha_mask is not None
    if has_alpha:
        alpha_minv, _ = dtype_ranges[str(img.alpha_mask.dtype)]
        dst_alpha: numpy.ndarray = numpy.zeros(
            (dst_height, dst_width), dtype=img.alpha_mask.dtype
        )

    # Pre-compute mask (255 = valid, 0 = masked) from the source masked array
    src_mask = (~img.array.mask * numpy.uint8(255)).astype(numpy.uint8)

    # Iterate over output tiles
    for dst_row in range(0, dst_height, _TILE_SIZE):
        for dst_col in range(0, dst_width, _TILE_SIZE):
            tile_h = min(_TILE_SIZE, dst_height - dst_row)
            tile_w = min(_TILE_SIZE, dst_width - dst_col)

            # Map output tile → intermediate window (proportional)
            inter_row = round(dst_row * native_height / dst_height)
            inter_col = round(dst_col * native_width / dst_width)
            inter_row_end = round((dst_row + tile_h) * native_height / dst_height)
            inter_col_end = round((dst_col + tile_w) * native_width / dst_width)

            # Cap intermediate chunk to avoid huge allocations when downsampling.
            # When native_res << output_res (heavy downsampling), clamp to the
            # output tile size so reproject goes directly to output resolution.
            chunk_h = max(1, min(inter_row_end - inter_row, tile_h))
            chunk_w = max(1, min(inter_col_end - inter_col, tile_w))

            # Derive geographic bounds of this intermediate chunk, then build a
            # transform for the (possibly clamped) chunk size. This is equivalent
            # to GDAL selecting a coarser resolution when the output is much smaller
            # than the native resolution.
            chunk_west = w + inter_col * w_res
            chunk_north = n + inter_row * h_res  # h_res < 0, so this moves south
            chunk_east = w + inter_col_end * w_res
            chunk_south = n + inter_row_end * h_res
            chunk_transform = from_bounds(
                chunk_west, chunk_south, chunk_east, chunk_north, chunk_w, chunk_h
            )

            # Step 1: reproject source → intermediate chunk
            chunk_data = numpy.zeros((img.count, chunk_h, chunk_w), dtype=img.array.dtype)
            chunk_data, _ = reproject(
                img.array.data,
                chunk_data,
                src_transform=img.transform,
                src_crs=img.crs,
                src_nodata=img.nodata,
                dst_crs=dst_crs,
                dst_transform=chunk_transform,
                dst_nodata=img.nodata,
                resampling=Resampling[reproject_method],
            )

            chunk_mask = numpy.zeros((img.count, chunk_h, chunk_w), dtype=numpy.uint8)
            chunk_mask, _ = reproject(
                src_mask,
                chunk_mask,
                src_transform=img.transform,
                src_crs=img.crs,
                dst_transform=chunk_transform,
                dst_crs=dst_crs,
                resampling=Resampling["nearest"],
                dst_nodata=0,
            )

            # Step 2: resample intermediate chunk → output tile
            if (chunk_h, chunk_w) != (tile_h, tile_w):
                chunk_data = resize_array(chunk_data, tile_h, tile_w, resampling_method)
                chunk_mask = resize_array(chunk_mask, tile_h, tile_w, "nearest")

            dst_data[:, dst_row : dst_row + tile_h, dst_col : dst_col + tile_w] = (
                chunk_data
            )
            dst_mask[:, dst_row : dst_row + tile_h, dst_col : dst_col + tile_w] = (
                chunk_mask
            )

            if has_alpha:
                chunk_alpha = numpy.zeros((chunk_h, chunk_w), dtype=img.alpha_mask.dtype)
                chunk_alpha, _ = reproject(
                    img.alpha_mask,
                    chunk_alpha,
                    src_transform=img.transform,
                    src_crs=img.crs,
                    dst_transform=chunk_transform,
                    dst_crs=dst_crs,
                    resampling=Resampling["nearest"],
                    dst_nodata=alpha_minv,
                )
                if (chunk_h, chunk_w) != (tile_h, tile_w):
                    chunk_alpha = resize_array(chunk_alpha, tile_h, tile_w, "nearest")

                dst_alpha[dst_row : dst_row + tile_h, dst_col : dst_col + tile_w] = (
                    chunk_alpha
                )

    return ImageData(
        numpy.ma.MaskedArray(dst_data, mask=~dst_mask.astype(bool)),
        assets=img.assets,
        crs=dst_crs,
        bounds=dst_bounds,
        band_names=img.band_names,
        band_descriptions=img.band_descriptions,
        nodata=img.nodata,
        scales=img.scales,
        offsets=img.offsets,
        metadata=img.metadata,
        dataset_statistics=img.dataset_statistics,
        alpha_mask=dst_alpha if has_alpha else None,
    )
