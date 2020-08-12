"""rio_tiler.mosaic: create tile from multiple assets."""

from typing import Any, Callable, List, Optional, Sequence, Tuple

import numpy

from ..constants import MAX_THREADS
from ..errors import TileOutsideBounds
from ..tasks import create_tasks, filter_tasks
from ..utils import _chunks
from .methods.base import MosaicMethodBase
from .methods.defaults import FirstMethod


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
        tasks = create_tasks(reader, chunks, threads, *args, **kwargs)
        for (t, m), asset in filter_tasks(
            tasks, allowed_exceptions=(TileOutsideBounds,)
        ):
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
