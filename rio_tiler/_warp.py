"""rio-tiler warping utilities."""

from __future__ import annotations

import numpy
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.transform import from_bounds
from rasterio.warp import reproject

from rio_tiler.models import ImageData
from rio_tiler.types import BBox, WarpResampling


def warp(
    img: ImageData,
    *,
    dst_crs: CRS,
    dst_bounds: BBox,
    dst_width: int,
    dst_height: int,
    reproject_method: WarpResampling = "nearest",
) -> ImageData:
    """Reproject data and mask.

    In the async reader we can't use the rasterio/GDAL WarpedVRT to handle reprojection/resampling,
    so we need to do it manually with `rasterio.warp.reproject`.

    """
    dst_transform = from_bounds(*dst_bounds, dst_width, dst_height)

    destination = numpy.zeros((img.count, dst_height, dst_width), dtype=img.array.dtype)
    destination, _ = reproject(
        img.array,
        destination,
        src_transform=img.transform,
        src_crs=img.crs,
        src_nodata=img.nodata,
        dst_crs=dst_crs,
        dst_transform=dst_transform,
        dst_nodata=img.nodata,
        resampling=Resampling[reproject_method],
    )

    # rasterio doesn't handle masked arrays really well
    # ref: https://github.com/rasterio/rasterio/pull/3531
    mask = ~img.array.mask * numpy.uint8(255)
    alpha_mask = numpy.zeros((img.count, dst_height, dst_width), dtype=numpy.uint8)
    alpha_mask, _ = reproject(
        mask,
        alpha_mask,
        src_transform=img.transform,
        src_crs=img.crs,
        dst_transform=dst_transform,
        dst_crs=dst_crs,
        resampling=Resampling["nearest"],
        src_nodata=0,
        dst_nodata=0,
    )

    return ImageData(
        numpy.ma.MaskedArray(destination, mask=~alpha_mask.astype(bool)),
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
    )
