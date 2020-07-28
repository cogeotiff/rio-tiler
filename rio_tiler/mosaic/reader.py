"""rio_tiler.mosaic: create tile from multiple assets."""

import logging
from concurrent import futures
from dataclasses import dataclass
from typing import Any, Callable, Generator, Optional, Sequence, Tuple, Union

import numpy

from ..constants import MAX_THREADS
from ..io.base import BaseReader
from ..utils import _chunks
from .methods.base import MosaicMethodBase
from .methods.defaults import FirstMethod

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
TaskType = Union[Generator[Callable, None, None], Sequence[futures.Future]]


def _filter_tasks(tasks: TaskType):
    """
    Filter tasks to remove Exceptions.

    Attributes
    ----------
    tasks : list or tuple
        Sequence of 'concurrent.futures._base.Future' or 'partial'

    Yields
    ------
    Successful task's result

    """
    for future in tasks:
        try:
            if isinstance(future, futures.Future):
                yield future.result()
            else:
                yield future
        except Exception as err:
            logging.error(err)
            pass


@dataclass
class MosaicReader:
    """
    Mosaic Reader.

    Examples
    --------
    with MosaicReader(assets, reader=COGReader) as mosaic:
        mosaic.tile(...)

    with MosaicReader(assets, reader=STACReader) as mosaic:
        mosaic.tile(...)

    Attributes
    ----------
    assets: str
        Cloud Optimized GeoTIFF path.
    reader: rio_tiler.io.BaseReader, optional
        Rio-tiler reader class.

    Methods
    -------
    tile(0, 0, 0, i**kwargs)
        Return map tile from multiple observation.
    part((0,10,0,10), **kwargs)
        Return array for a specific bbox from multiple observation.
    preview(**kwargs)
        Return a preview from multiple observation.

    """

    assets: Sequence[str]
    reader: BaseReader

    def __enter__(self):
        """Support using with Context Managers."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def tile(self, x: int, y: int, z: int, **kwargs: Any):
        """Get Tile from multiple observation."""

        def _reader(asset, *args: int, **kwargs: Any):
            with self.reader(asset) as src_dst:  # type: ignore
                return src_dst.tile(*args, **kwargs)

        return mosaic_reader(self.assets, _reader, x, y, z, **kwargs)

    def part(self, bbox: Tuple[float, float, float, float], **kwargs: Any):
        """Get Part from multiple observation."""

        def _reader(asset, *args, **kwargs: Any):
            with self.reader(asset) as src_dst:  # type: ignore
                return src_dst.part(*args, **kwargs)

        return mosaic_reader(self.assets, _reader, bbox, **kwargs)

    def preview(self, **kwargs: Any):
        """Get Preview from multiple observation."""

        def _reader(asset, **kwargs):
            with self.reader(asset) as src_dst:
                return src_dst.preview(**kwargs)

        return mosaic_reader(self.assets, _reader, **kwargs)


def mosaic_reader(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    pixel_selection: Optional[MosaicMethodBase] = None,
    chunk_size: Optional[int] = None,
    threads: int = MAX_THREADS,
    **kwargs,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
        Number of threads to use. If <=1, runs single threaded without an event
        loop. By default reads from the MAX_THREADS environment variable, and if
        not found defaults to multiprocessing.cpu_count() * 5.
    kwargs: dict, optional
        tiler specific options.

    Returns
    -------
    tile, mask : tuple of ndarray
        Return tile and mask data.

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

    tasks: TaskType

    for chunks in _chunks(assets, chunk_size):
        if threads:
            with futures.ThreadPoolExecutor(max_workers=threads) as executor:
                tasks = [
                    executor.submit(reader, asset, *args, **kwargs) for asset in chunks
                ]
        else:
            tasks = (reader(asset, *args, **kwargs) for asset in chunks)

        for t, m in _filter_tasks(tasks):
            t = numpy.ma.array(t)
            t.mask = m == 0

            pixel_selection.feed(t)
            if pixel_selection.is_done:
                return pixel_selection.data

    return pixel_selection.data


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
) -> Tuple[numpy.ndarray, numpy.ndarray]:
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
