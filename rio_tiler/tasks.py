"""rio_tiler.tasks: tools for handling rio-tiler's future tasks."""

from concurrent import futures
from functools import partial
from typing import Any, Callable, Dict, Generator, Optional, Sequence, Tuple, Union

import numpy

from .constants import MAX_THREADS
from .logger import logger

TaskType = Sequence[Tuple[Union[futures.Future, Callable], str]]


def filter_tasks(
    tasks: TaskType, allowed_exceptions: Optional[Tuple] = None,
) -> Generator:
    """
    Filter tasks to remove Exceptions.

    Attributes
    ----------
    tasks: list
        Sequence of 'concurrent.futures._base.Future' or 'Callable'
    allowed_exceptions: Tuple, optional
        List of exceptions which won't be raised.

    Yields
    ------
    Successful task's result

    """
    if not allowed_exceptions:
        allowed_exceptions = ()

    for (future, asset) in tasks:
        try:
            if isinstance(future, futures.Future):
                yield future.result(), asset
            else:
                yield future(), asset
        except allowed_exceptions as err:
            logger.info(err)
            pass


def create_tasks(reader: Callable, assets, threads, *args, **kwargs) -> TaskType:
    """Create Future Tasks."""
    if threads and threads > 1:
        logger.debug(f"Running tasks in ThreadPool with max_workers={threads}")
        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            return [
                (executor.submit(reader, asset, *args, **kwargs), asset)
                for asset in assets
            ]
    else:
        logger.debug(f"Running tasks outside ThreadsPool (max_workers={threads})")
        return [(partial(reader, asset, *args, **kwargs), asset) for asset in assets]


def multi_arrays(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Multi array."""
    tasks = create_tasks(reader, assets, threads, *args, **kwargs)
    data, masks = zip(*[r for r, _ in filter_tasks(tasks)])
    data = numpy.concatenate(data)
    mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255
    return data, mask


def multi_values(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    **kwargs: Any,
) -> Dict:
    """Multi Values."""
    tasks = create_tasks(reader, assets, threads, *args, **kwargs)
    return {asset: val for val, asset in filter_tasks(tasks)}
