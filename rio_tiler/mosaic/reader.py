"""rio_tiler.mosaic: create tile from multiple assets."""

import logging
from concurrent import futures
from typing import Any, Callable, Generator, List, Optional, Sequence, Tuple, Union

import numpy

from ..constants import MAX_THREADS
from ..utils import _chunks
from .methods.base import MosaicMethodBase
from .methods.defaults import FirstMethod

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
TaskType = Union[
    Generator[Tuple[Callable, str], None, None], Sequence[Tuple[futures.Future, str]]
]


def _filter_tasks(tasks: TaskType):
    """
    Filter tasks to remove Exceptions.

    Attributes
    ----------
    tasks : list or generator
        Sequence of 'concurrent.futures._base.Future' or 'callable'

    Yields
    ------
    Successful task's result

    """
    for future, asset in tasks:
        try:
            if isinstance(future, futures.Future):
                yield future.result(), asset
            else:
                yield future, asset
        except Exception as err:
            logging.error(err, exc_info=True)
            pass


def _create_tasks(reader: Callable, assets, threads, *args, **kwargs) -> TaskType:
    """Create Future Tasks."""
    tasks: TaskType

    if threads and threads > 1:
        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            return [
                (executor.submit(reader, asset, *args, **kwargs), asset)
                for asset in assets
            ]
    else:
        return ((reader(asset, *args, **kwargs), asset) for asset in assets)


def mosaic_reader(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    pixel_selection: Optional[MosaicMethodBase] = None,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    **kwargs,
) -> Tuple[Tuple[numpy.ndarray, numpy.ndarray], Sequence[str]]:
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
    kwargs: dict, optional
        tiler specific options.

    Returns
    -------
    (tile, mask), assets_used : tuple of ndarray, sequence of str
        Return (tile, mask) data and list of assets used.

    """
    if pixel_selection is None:
        pixel_selection = FirstMethod()

    if not isinstance(pixel_selection, MosaicMethodBase):
        raise Exception(
            "Mosaic filling algorithm should be an instance of"
            "'rio_tiler.mosaic.methods.base.MosaicMethodBase'"
        )

    if not chunk_size:
        chunk_size = threads or len(assets)

    assets_used: List[str] = []

    for chunks in _chunks(assets, chunk_size):
        tasks = _create_tasks(reader, chunks, threads, *args, **kwargs)
        for (t, m), asset in _filter_tasks(tasks):
            assets_used.append(asset)
            t = numpy.ma.array(t)
            t.mask = m == 0

            pixel_selection.feed(t)
            if pixel_selection.is_done:
                return pixel_selection.data, assets_used

    return pixel_selection.data, assets_used


def mosaic_tiler(
    assets: Sequence[str],
    tile_x: int,
    tile_y: int,
    tile_z: int,
    reader: Callable,
    pixel_selection: Optional[MosaicMethodBase] = None,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    **kwargs,
) -> Tuple[Tuple[numpy.ndarray, numpy.ndarray], Sequence[str]]:
    """Wrapper around mosaic_reader from compatibility with previous rio_tiler_mosaic."""
    return mosaic_reader(
        assets,
        reader,
        tile_x,
        tile_y,
        tile_z,
        pixel_selection=pixel_selection,
        chunk_size=chunk_size,
        threads=threads,
        **kwargs,
    )
