"""rio_tiler.mosaic: create tile from multiple assets."""

import warnings
from inspect import isclass
from typing import Any, Callable, List, Optional, Sequence, Tuple, Type, Union, cast

import numpy
from rasterio.crs import CRS

from rio_tiler.constants import MAX_THREADS
from rio_tiler.errors import (
    EmptyMosaicError,
    InvalidMosaicMethod,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.models import ImageData, PointData
from rio_tiler.mosaic.methods.base import MosaicMethodBase
from rio_tiler.mosaic.methods.defaults import FirstMethod
from rio_tiler.tasks import create_tasks, filter_tasks
from rio_tiler.types import BBox
from rio_tiler.utils import _chunks, resize_array


def mosaic_reader(  # noqa: C901
    mosaic_assets: Sequence,
    reader: Callable[..., ImageData],
    *args: Any,
    pixel_selection: Union[Type[MosaicMethodBase], MosaicMethodBase] = FirstMethod,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    allowed_exceptions: Tuple = (TileOutsideBounds,),
    **kwargs,
) -> Tuple[ImageData, List]:
    """Merge multiple assets.

    Args:

        mosaic_assets (sequence): List of assets.
        reader (callable): Reader function. The function MUST take `(asset, *args, **kwargs)` as arguments, and MUST return an ImageData.
        args (Any): Argument to forward to the reader function.
        pixel_selection (MosaicMethod, optional): Instance of MosaicMethodBase class. Defaults to `rio_tiler.mosaic.methods.defaults.FirstMethod`.
        chunk_size (int, optional): Control the number of asset to process per loop.
        threads (int, optional): Number of threads to use. If <= 1, runs single threaded without an event loop. By default reads from the MAX_THREADS environment variable, and if not found defaults to multiprocessing.cpu_count() * 5.
        allowed_exceptions (tuple, optional): List of exceptions which will be ignored. Note: `TileOutsideBounds` is likely to be raised and should be included in the allowed_exceptions. Defaults to `(TileOutsideBounds, )`.
        kwargs (optional): Reader callable's keywords options.

    Returns:
        tuple: ImageData and assets (list).

    Examples:
        >>> def reader(asset: str, *args, **kwargs) -> ImageData:
                with Reader(asset) as src:
                    return src.tile(*args, **kwargs)

            x, y, z = 10, 10, 4
            img = mosaic_reader(["cog.tif", "cog2.tif"], reader, x, y, z)

        >>> def reader(asset: str, *args, **kwargs) -> ImageData:
                with Reader(asset) as src:
                    return src.preview(*args, **kwargs)

            img = mosaic_reader(["cog.tif", "cog2.tif"], reader)


    """
    if isclass(pixel_selection):
        pixel_selection = cast(Type[MosaicMethodBase], pixel_selection)

        if issubclass(pixel_selection, MosaicMethodBase):
            pixel_selection = pixel_selection()

    if not isinstance(pixel_selection, MosaicMethodBase):
        raise InvalidMosaicMethod(
            "Mosaic filling algorithm should be an instance of "
            "'rio_tiler.mosaic.methods.base.MosaicMethodBase'"
        )

    if not chunk_size:
        chunk_size = threads if threads > 1 else len(mosaic_assets)

    assets_used: List = []
    crs: Optional[CRS]
    bounds: Optional[BBox]
    band_names: List[str]

    for chunks in _chunks(mosaic_assets, chunk_size):
        tasks = create_tasks(reader, chunks, threads, *args, **kwargs)
        for img, asset in filter_tasks(
            tasks,
            allowed_exceptions=allowed_exceptions,
        ):
            # On the first Image we set the properties
            if len(assets_used) == 0:
                crs = img.crs
                bounds = img.bounds
                band_names = img.band_names
                pixel_selection.cutline_mask = img.cutline_mask
                pixel_selection.width = img.width
                pixel_selection.height = img.height
                pixel_selection.count = img.count

            assert (
                img.count == pixel_selection.count
            ), "Assets HAVE TO have the same number of bands"
            if any(
                [
                    img.width != pixel_selection.width,
                    img.height != pixel_selection.height,
                ]
            ):
                warnings.warn(
                    "Cannot concatenate images with different size. Will resize using fist asset width/heigh",
                    UserWarning,
                )
                h = pixel_selection.height
                w = pixel_selection.width
                pixel_selection.feed(
                    numpy.ma.MaskedArray(
                        resize_array(img.array.data, h, w),
                        mask=resize_array(img.array.mask * 1, h, w).astype("bool"),
                    )
                )

            else:
                pixel_selection.feed(img.array)

            assets_used.append(asset)

            if pixel_selection.is_done and pixel_selection.data is not None:
                return (
                    ImageData(
                        pixel_selection.data,
                        assets=assets_used,
                        crs=crs,
                        bounds=bounds,
                        band_names=band_names,
                    ),
                    assets_used,
                )

    if pixel_selection.data is None:
        raise EmptyMosaicError("Method returned an empty array")

    return (
        ImageData(
            pixel_selection.data,
            assets=assets_used,
            crs=crs,
            bounds=bounds,
            band_names=band_names,
        ),
        assets_used,
    )


def mosaic_point_reader(
    mosaic_assets: Sequence,
    reader: Callable[..., PointData],
    *args: Any,
    pixel_selection: Union[Type[MosaicMethodBase], MosaicMethodBase] = FirstMethod,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    allowed_exceptions: Tuple = (PointOutsideBounds,),
    **kwargs,
) -> Tuple[PointData, List]:
    """Merge multiple assets.

    Args:

        mosaic_assets (sequence): List of assets.
        reader (callable): Reader function. The function MUST take `(asset, *args, **kwargs)` as arguments, and MUST return a PointData object.
        args (Any): Argument to forward to the reader function.
        pixel_selection (MosaicMethod, optional): Instance of MosaicMethodBase class. Defaults to `rio_tiler.mosaic.methods.defaults.FirstMethod`.
        chunk_size (int, optional): Control the number of asset to process per loop.
        threads (int, optional): Number of threads to use. If <= 1, runs single threaded without an event loop. By default reads from the MAX_THREADS environment variable, and if not found defaults to multiprocessing.cpu_count() * 5.
        allowed_exceptions (tuple, optional): List of exceptions which will be ignored. Note: `PointOutsideBounds` is likely to be raised and should be included in the allowed_exceptions. Defaults to `(TileOutsideBounds, )`.
        kwargs (optional): Reader callable's keywords options.

    Returns:
        tuple: PointData and assets (list).

    Examples:
        >>> def reader(asset: str, *args, **kwargs) -> PointData:
                with Reader(asset) as src:
                    return src.point(*args, **kwargs)

            pt = mosaic_point_reader(["cog.tif", "cog2.tif"], reader, 0, 0)

    """
    if isclass(pixel_selection):
        pixel_selection = cast(Type[MosaicMethodBase], pixel_selection)

        if issubclass(pixel_selection, MosaicMethodBase):
            pixel_selection = pixel_selection()

    if not isinstance(pixel_selection, MosaicMethodBase):
        raise InvalidMosaicMethod(
            "Mosaic filling algorithm should be an instance of "
            "'rio_tiler.mosaic.methods.base.MosaicMethodBase'"
        )

    if not chunk_size:
        chunk_size = threads if threads > 1 else len(mosaic_assets)

    assets_used: List = []
    crs: Optional[CRS]
    coordinates: Optional[Tuple[float, float]]
    band_names: List[str]

    for chunks in _chunks(mosaic_assets, chunk_size):
        tasks = create_tasks(reader, chunks, threads, *args, **kwargs)
        for pt, asset in filter_tasks(
            tasks,
            allowed_exceptions=allowed_exceptions,
        ):
            # On the first Image we set the properties
            if len(assets_used) == 0:
                crs = pt.crs
                coordinates = pt.coordinates
                band_names = pt.band_names
                pixel_selection.width = 1
                pixel_selection.height = 1
                pixel_selection.count = pt.count

            assert (
                pt.count == pixel_selection.count
            ), "Assets HAVE TO have the same number of bands"

            assets_used.append(asset)
            pixel_selection.feed(pt.array)

            if pixel_selection.is_done and pixel_selection.data is not None:
                return (
                    PointData(
                        pixel_selection.data,
                        assets=assets_used,
                        crs=crs,
                        coordinates=coordinates,
                        band_names=band_names,
                    ),
                    assets_used,
                )

    if pixel_selection.data is None:
        raise EmptyMosaicError("Method returned an empty array")

    return (
        PointData(
            pixel_selection.data,
            assets=assets_used,
            crs=crs,
            coordinates=coordinates,
            band_names=band_names,
        ),
        assets_used,
    )
