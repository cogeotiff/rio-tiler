"""rio_tiler.mosaic: create tile from multiple assets."""

from inspect import isclass
from typing import Any, Callable, List, Optional, Sequence, Tuple, Type, Union, cast

from rasterio.crs import CRS

from ..constants import MAX_THREADS, BBox
from ..errors import EmptyMosaicError, InvalidMosaicMethod, TileOutsideBounds
from ..models import ImageData
from ..tasks import create_tasks, filter_tasks
from ..utils import _chunks
from .methods.base import MosaicMethodBase
from .methods.defaults import FirstMethod


def mosaic_reader(
    assets: Sequence[str],
    reader: Callable[..., ImageData],
    *args: Any,
    pixel_selection: Union[Type[MosaicMethodBase], MosaicMethodBase] = FirstMethod,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    allowed_exceptions: Tuple = (TileOutsideBounds,),
    **kwargs,
) -> Tuple[ImageData, List[str]]:
    """
    Merge multiple assets.

    Attributes
    ----------
    assets: list or tuple
        List of tiler compatible asset.
    reader: callable
        reader function. The function MUST take asset, *args, **kwargs as arguments,
        and MUST return a tuple with tile data and mask
        e.g:
        def reader(asset: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
            with COGReader(asset) as cog:
                return cog.tile(*args, **kwargs)

        def reader(asset: str, *args, **kwargs) -> Tuple[numpy.ndarray, numpy.ndarray]:
            with COGReader(asset) as cog:
                return cog.preview(*args, **kwargs)
    args: Any
        additional argument to forward to the reader function.
    pixel_selection: MosaicMethod, optional
        Instance of MosaicMethodBase class.
        default: "rio_tiler.mosaic.methods.defaults.FirstMethod".
    chunk_size: int, optional
        Control the number of asset to process per loop (default = threads).
    threads: int, optional
        Number of threads to use. If <= 1, runs single threaded without an event
        loop. By default reads from the MAX_THREADS environment variable, and if
        not found defaults to multiprocessing.cpu_count() * 5.
    allowed_exceptions: Tuple, optional
        List of exceptions which will be ignored. Default is set to `(TileOutsideBounds,)`.
        Note: `TileOutsideBounds` is likely to be raised and should be included in the allowed_exceptions.
    kwargs: dict, optional
        tiler specific options.

    Returns
    -------
    (tile, mask), assets_used : tuple of ndarray, sequence of str
        Return (tile, mask) data and list of assets used.

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
        chunk_size = threads if threads > 1 else len(assets)

    assets_used: List[str] = []
    crs: Optional[CRS] = None
    bounds: Optional[BBox] = None

    for chunks in _chunks(assets, chunk_size):
        tasks = create_tasks(reader, chunks, threads, *args, **kwargs)
        for img, asset in filter_tasks(tasks, allowed_exceptions=allowed_exceptions,):
            if isinstance(img, tuple):
                img = ImageData(*img)

            crs = img.crs
            bounds = img.bounds

            assets_used.append(asset)
            pixel_selection.feed(img.as_masked())

            if pixel_selection.is_done:
                data, mask = pixel_selection.data
                return (
                    ImageData(data, mask, assets=assets_used, crs=crs, bounds=bounds),
                    assets_used,
                )

    data, mask = pixel_selection.data
    if data is None:
        raise EmptyMosaicError("Method returned an empty array")

    return (
        ImageData(data, mask, assets=assets_used, crs=crs, bounds=bounds),
        assets_used,
    )
