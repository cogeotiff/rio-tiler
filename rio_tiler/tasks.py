"""rio_tiler.tasks: tools for handling rio-tiler's future tasks."""
import abc
import logging
from concurrent import futures
from typing import Any, Callable, Dict, Generator, Iterable, Optional, Sequence, Tuple

import attr
import numpy

from .constants import MAX_THREADS

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


@attr.s
class TaskManager(abc.ABC):
    """Task manager base class"""

    threads: int = attr.ib(init=False)

    @classmethod
    def create(cls, threads) -> "TaskManager":
        """Create from environment."""
        if threads <= 1:
            return SingleThreadedManager(threads=threads)
        else:
            return MultiThreadedManager(threads=threads)

    @abc.abstractmethod
    def create_tasks(self, reader: Callable, assets, *args, **kwargs) -> Iterable:
        """Create Future Tasks."""
        ...

    @abc.abstractmethod
    def filter_tasks(self, tasks: Iterable, allowed_exceptions: Tuple = ()) -> Iterable:
        """Filter tasks to remove Exceptions."""


@attr.s
class SingleThreadedManager(TaskManager):
    """Single threaded task management"""

    threads: int = attr.ib(default=1)

    def create_tasks(
        self, reader: Callable, assets, *args, threads: Optional[int] = None, **kwargs
    ) -> Generator[Tuple[Callable, str], None, None]:
        """Create Future Tasks."""
        return ((reader(asset, *args, **kwargs), asset) for asset in assets)

    def filter_tasks(
        self, tasks: Iterable, allowed_exceptions: Tuple = ()
    ) -> Generator:
        """
        Filter tasks to remove Exceptions.

        Attributes
        ----------
        tasks: iterable of 'callable'
            Iterable of 'concurrent.futures._base.Future' or 'callable'
        allowed_exceptions: Tuple, optional
            List of exceptions which won't be raised.

        Yields
        ------
        Successful task's result

        """
        while True:
            try:
                ret, asset = next(tasks)  # type: ignore
                yield ret, asset
            except allowed_exceptions as err:
                logging.info(err)
                pass
            except StopIteration:
                break


@attr.s
class MultiThreadedManager(TaskManager):
    """Multi threaded task management"""

    threads: int = attr.ib()

    def create_tasks(
        self, reader: Callable, assets, *args, threads: Optional[int] = None, **kwargs
    ) -> Sequence[Tuple[futures.Future, str]]:
        """Create Future Tasks."""
        max_workers = threads or self.threads
        with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            return [
                (executor.submit(reader, asset, *args, **kwargs), asset,)
                for asset in assets
            ]

    def filter_tasks(
        self, tasks: Iterable, allowed_exceptions: Tuple = ()
    ) -> Generator:
        """
        Filter tasks to remove Exceptions.

        Attributes
        ----------
        tasks: iterable
            Iterable of 'concurrent.futures._base.Future'
        allowed_exceptions: Tuple, optional
            List of exceptions which won't be raised.

        Yields
        ------
        Successful task's result

        """
        for future, asset in tasks:
            try:
                yield future.result(), asset
            except allowed_exceptions as err:
                logger.info(err)


def multi_arrays(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Multi array."""
    task_manager = TaskManager.create(threads=threads)
    tasks = task_manager.create_tasks(reader, assets, *args, **kwargs)

    data, masks = zip(*[r for r, _ in task_manager.filter_tasks(tasks)])
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
    task_manager = TaskManager.create(threads=threads)
    tasks = task_manager.create_tasks(reader, assets, *args, **kwargs)

    return {asset: val for val, asset in task_manager.filter_tasks(tasks)}
