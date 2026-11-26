"""rio-tiler warping utilities."""

from __future__ import annotations

from collections.abc import Sequence

import numpy
from affine import Affine
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import Resampling
from rasterio.env import get_gdal_config
from rasterio.transform import from_bounds
from rasterio.warp import calculate_default_transform, reproject

from rio_tiler.constants import OVERVIEW_OVERSAMPLING_THRESHOLD
from rio_tiler.models import ImageData
from rio_tiler.types import BBox, RIOResampling, WarpResampling
from rio_tiler.utils import resize_array

# Output tile size (in pixels) used to bound intermediate memory during warp.
# Each intermediate chunk is at most (native_res/output_res * _TILE_SIZE)² pixels.
_TILE_SIZE = 2048


def get_overview_level(
    overview_factors: Sequence[float],
    desired_factor: float,
    resampling_method: RIOResampling = "nearest",
) -> int:
    """Select the overview to read for a downsampling factor, like GDAL does.

    Same rule as GDAL's RasterIO (`GDALBandGetBestOverviewLevel2` in gcore/rasterio.cpp),
    which `rio_tiler.io.Reader` relies on: select the most downsampled overview
    whose downsampling factor is lower than `desired_factor * threshold` (+ epsilon).
    The threshold is `1.2` for `nearest` (an overview slightly coarser than the
    output can be used) and `1.0` for other resampling methods (never upsample a
    coarser overview).

    The threshold can be set with the `RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD`
    environment variable (`rio_tiler.constants.OVERVIEW_OVERSAMPLING_THRESHOLD`).
    When not set, GDAL's value is used: `GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD`
    (environment or `rasterio.Env`) if defined, else the defaults above.

    Args:
        overview_factors (sequence of float): Downsampling factor of each overview,
            relative to the full resolution (e.g `width / overview_width`).
        desired_factor (float): Number of full resolution pixels for one output pixel.
        resampling_method (RIOResampling): Resampling method. Defaults to `nearest`.

    Returns:
        int: overview level, `0` for full resolution or `i` for `overview_factors[i - 1]`.

    """
    # NOTE: rio-tiler setting, else GDAL's setting, else GDAL's defaults
    threshold = OVERVIEW_OVERSAMPLING_THRESHOLD
    if threshold is None:
        threshold = get_gdal_config("GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD")
    if threshold is None:
        threshold = 1.2 if resampling_method == "nearest" else 1.0

    # NOTE: GDAL uses an epsilon because of numerical instability
    epsilon = 0.1

    best_level, best_factor = 0, 0.0
    for i, factor in enumerate(overview_factors):
        if factor >= desired_factor * float(threshold) + epsilon or factor <= best_factor:
            continue

        best_level, best_factor = i + 1, factor
        if abs(desired_factor - factor) < epsilon:
            break

    return best_level


def get_downsampling_factor(
    *,
    output_bounds: BBox,
    output_crs: CRS,
    output_width: int,
    output_height: int,
    dataset_crs: CRS,
    dataset_transform: Affine,
    dataset_width: int,
    dataset_height: int,
    dataset_bounds: BBox,
) -> float:
    """Number of full resolution pixels for one output pixel, like `rio_tiler.io.Reader` computes it.

    - same CRS: the window (in dataset pixels) is read with an `out_shape`
    - different CRS: a WarpedVRT at the dataset resolution in the output CRS
      (`rio_tiler.utils.get_vrt_transform`) is read with an `out_shape`

    GDAL uses the least reduced axis.

    """
    w, s, e, n = output_bounds
    if output_crs != dataset_crs:
        native_transform, _, _ = calculate_default_transform(
            dataset_crs, output_crs, dataset_width, dataset_height, *dataset_bounds
        )
        x_size = max(1, round((e - w) / abs(native_transform.a)))
        y_size = max(1, round((n - s) / abs(native_transform.e)))
    else:
        x_size = (e - w) / abs(dataset_transform.a)
        y_size = (n - s) / abs(dataset_transform.e)

    return min(x_size / output_width, y_size / output_height)


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

    The source pixels are warped directly onto the output grid, in a single
    resampling pass (like GDAL's WarpedVRT when the output resolution is finer
    than the dataset resolution). The kernel matches `rio_tiler.io.Reader`:

    - `reproject_method` when src CRS != dst CRS (WarpedVRT kernel)
    - `resampling_method` when src CRS == dst CRS (RasterIO kernel)

    When the kernel isn't supported by the warper (`gauss`), we fall back to
    two steps: reproject to the intermediate (native) resolution using
    `reproject_method`, then resize to the output size using `resampling_method`.

    Processing is done tile-by-tile over the output grid so that the peak
    intermediate allocation is bounded by _TILE_SIZE rather than the full
    native resolution extent.
    """
    # NOTE: Select the warp kernel, like rio_tiler.io.Reader does:
    # - CRS change: GDAL's WarpedVRT warps with `reproject_method`
    #   (`resampling_method` is not used because the warp goes directly onto
    #   the output grid, in a single pass)
    # - same CRS: no WarpedVRT, GDAL's RasterIO resamples with `resampling_method`
    warp_method: WarpResampling = reproject_method

    # NOTE: if no reprojection is needed then we define the warp method based on the resampling method
    # NOTE: `gauss` is a RasterIO-only method (not supported by GDAL's warper),
    # so we keep `reproject_method` for the warp and use `gauss` in a second (resize) step.
    if (img.crs == dst_crs) and resampling_method != "gauss":
        warp_method = resampling_method

    # Compute native resolution in dst_crs
    dst_transform, _, _ = calculate_default_transform(
        img.crs, dst_crs, img.width, img.height, *img.bounds
    )

    w_res = dst_transform.a  # positive
    h_res = dst_transform.e  # negative (north-up)
    w, s, e, n = dst_bounds
    native_width = max(1, round((e - w) / w_res))
    native_height = max(1, round((s - n) / h_res))

    # NOTE: N-D data (*leading, height, width) are warped as (prod(leading), height, width)
    leading = img.array.shape[:-2]
    src_array = img.array.reshape((-1, img.height, img.width))
    count = src_array.shape[0]

    # NOTE: `rasterio.warp.reproject` merges the band masks of a masked source
    # into a single validity band, where a pixel is invalid if ANY band is masked
    # (the pixel is then nodata in all bands). rio-tiler (and GDAL's WarpedVRT)
    # considers a pixel valid if ANY band is valid, so we only mask the pixels
    # where ALL the bands are masked and re-apply the per-band nodata after the warp.
    src_mask = numpy.logical_and.reduce(numpy.ma.getmaskarray(src_array), axis=0)
    src_array = numpy.ma.MaskedArray(
        src_array.data,
        mask=numpy.broadcast_to(src_mask, src_array.shape),
    )

    # Allocate output arrays at the final size (never the full intermediate size)
    dst_data = numpy.zeros((count, dst_height, dst_width), dtype=img.array.dtype)
    dst_mask = numpy.zeros((count, dst_height, dst_width), dtype=numpy.uint8)

    has_alpha = img.alpha_mask is not None
    dst_alpha: numpy.ndarray | None = None
    if has_alpha:
        alpha_minv, _ = dtype_ranges[str(img.alpha_mask.dtype)]
        dst_alpha = numpy.zeros((dst_height, dst_width), dtype=img.alpha_mask.dtype)

    # Iterate over output tiles
    for dst_row in range(0, dst_height, _TILE_SIZE):
        for dst_col in range(0, dst_width, _TILE_SIZE):
            tile_h = min(_TILE_SIZE, dst_height - dst_row)
            tile_w = min(_TILE_SIZE, dst_width - dst_col)

            single_pass = not ((img.crs == dst_crs) and resampling_method == "gauss")
            if single_pass:
                # Warp directly onto the output tile grid
                chunk_h, chunk_w = tile_h, tile_w
                chunk_transform = from_bounds(
                    *dst_bounds, dst_width, dst_height
                ) * Affine.translation(dst_col, dst_row)

            else:
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
                # to GDAL selecting a coarser resolution when the output is much
                # smaller than the native resolution.
                chunk_west = w + inter_col * w_res
                chunk_north = n + inter_row * h_res  # h_res < 0, moves south
                chunk_east = w + inter_col_end * w_res
                chunk_south = n + inter_row_end * h_res
                chunk_transform = from_bounds(
                    chunk_west, chunk_south, chunk_east, chunk_north, chunk_w, chunk_h
                )

            # Step 1: reproject source → intermediate chunk
            # Destination must start fully masked: GDAL skips chunks with no
            # source pixels, leaving the initial alpha (mask) untouched.
            data = numpy.ma.masked_array(
                numpy.zeros((count, chunk_h, chunk_w), dtype=img.array.dtype),
                mask=True,
            )
            data, _ = reproject(
                src_array,
                data,
                src_transform=img.transform,
                src_crs=img.crs,
                dst_crs=dst_crs,
                dst_transform=chunk_transform,
                resampling=Resampling[warp_method],
            )

            chunk_data = data.data
            chunk_mask = (~numpy.ma.getmaskarray(data) * numpy.uint8(255)).astype(
                numpy.uint8
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

    out_mask = ~dst_mask.astype(bool)

    # Re-apply the per-band nodata mask (like `rio_tiler.reader.read`)
    if img.nodata is not None:
        if numpy.isnan(img.nodata):
            out_mask |= numpy.isnan(dst_data)
        else:
            out_mask |= dst_data == img.nodata

    return ImageData(
        numpy.ma.MaskedArray(
            dst_data.reshape((*leading, dst_height, dst_width)),
            mask=out_mask.reshape((*leading, dst_height, dst_width)),
        ),
        dimensions=img.dimensions,
        band_names=img.band_names,
        band_descriptions=img.band_descriptions,
        bounds=dst_bounds,
        crs=dst_crs,
        assets=img.assets,
        metadata=img.metadata,
        nodata=img.nodata,
        dataset_statistics=img.dataset_statistics,
        alpha_mask=dst_alpha if has_alpha else None,
    )
