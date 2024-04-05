"""rio_tiler.tasks: tools for handling rio-tiler's future tasks."""

from concurrent import futures
from functools import partial
from typing import Any, Callable, Dict, Generator, Optional, Sequence, Tuple, Union

from rio_tiler.constants import MAX_THREADS
from rio_tiler.logger import logger
from rio_tiler.models import ImageData, PointData

TaskType = Sequence[Tuple[Union[futures.Future, Callable], Any]]


def filter_tasks(
    tasks: TaskType,
    allowed_exceptions: Optional[Tuple] = None,
) -> Generator:
    """Filter Tasks to remove Exceptions.

    Args:
        tasks (sequence): Sequence of 'concurrent.futures._base.Future' or 'Callable'
        allowed_exceptions (tuple, optional): List of exceptions which won't be raised.

    Yields:
        Task results.

    """
    if allowed_exceptions is None:
        allowed_exceptions = ()

    for future, asset in tasks:
        try:
            if isinstance(future, futures.Future):
                yield future.result(), asset
            else:
                yield future(), asset
        except allowed_exceptions as err:
            logger.info(err)
            pass


def create_tasks(
    reader: Callable, asset_list: Sequence, threads: int, *args, **kwargs
) -> TaskType:
    """Create Future Tasks."""
    if threads and threads > 1:
        logger.debug(f"Running tasks in ThreadPool with max_workers={threads}")
        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            return [
                (executor.submit(reader, asset, *args, **kwargs), asset)
                for asset in asset_list
            ]
    else:
        logger.debug(f"Running tasks outside ThreadsPool (max_workers={threads})")
        return [(partial(reader, asset, *args, **kwargs), asset) for asset in asset_list]


def multi_arrays(
    asset_list: Sequence,
    reader: Callable[..., ImageData],
    *args: Any,
    threads: int = MAX_THREADS,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any,
) -> ImageData:
    """Merge arrays returned from tasks."""
    tasks = create_tasks(reader, asset_list, threads, *args, **kwargs)
    return ImageData.create_from_list(
        [data for data, _ in filter_tasks(tasks, allowed_exceptions=allowed_exceptions)]
    )


def multi_points(
    asset_list: Sequence,
    reader: Callable[..., PointData],
    *args: Any,
    threads: int = MAX_THREADS,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any,
) -> PointData:
    """Merge points returned from tasks."""
    tasks = create_tasks(reader, asset_list, threads, *args, **kwargs)
    return PointData.create_from_list(
        [data for data, _ in filter_tasks(tasks, allowed_exceptions=allowed_exceptions)]
    )


def multi_values(
    asset_list: Sequence,
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    allowed_exceptions: Optional[Tuple] = None,
    **kwargs: Any,
) -> Dict:
    """Merge values returned from tasks."""
    tasks = create_tasks(reader, asset_list, threads, *args, **kwargs)
    return {
        asset: val
        for val, asset in filter_tasks(tasks, allowed_exceptions=allowed_exceptions)
    }
