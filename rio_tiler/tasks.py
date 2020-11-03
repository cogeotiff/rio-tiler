"""rio_tiler.tasks: tools for handling rio-tiler's future tasks."""

from concurrent import futures
from functools import partial
from typing import Any, Callable, Dict, Generator, Optional, Sequence, Tuple, Union

from .constants import MAX_THREADS
from .logger import logger
from .models import ImageData

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
    if allowed_exceptions is None:
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
    reader: Callable[..., ImageData],
    *args: Any,
    threads: int = MAX_THREADS,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any,
) -> ImageData:
    """Multi array."""
    tasks = create_tasks(reader, assets, threads, *args, **kwargs)
    return ImageData.create_from_list(
        [data for data, _ in filter_tasks(tasks, allowed_exceptions=allowed_exceptions)]
    )


def multi_values(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any,
) -> Dict:
    """Multi Values."""
    tasks = create_tasks(reader, assets, threads, *args, **kwargs)
    return {
        asset: val
        for val, asset in filter_tasks(tasks, allowed_exceptions=allowed_exceptions)
    }
