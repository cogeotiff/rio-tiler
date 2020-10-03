"""rio_tiler.tasks: tools for handling rio-tiler's future tasks."""
import abc
import logging
from concurrent import futures
from typing import Any, Callable, Dict, Generator, Iterable, Sequence, Tuple

import attr
import numpy

from .constants import MAX_THREADS

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


@attr.s
class TaskManager(abc.ABC):
    """Task manager base class"""

    max_threads: int = attr.ib()

    @classmethod
    def create_from_env(cls) -> "TaskManager":
        """Create from environment."""
        if MAX_THREADS == 1:
            return SingleThreadedManager(max_threads=MAX_THREADS)
        else:
            return MultiThreadedManager(max_threads=MAX_THREADS)

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

    max_threads: int = 1

    def create_tasks(
        self, reader: Callable, assets, *args, **kwargs
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
        for ret, asset in tasks:
            try:
                yield ret, asset
            except allowed_exceptions as err:
                logging.info(err)
                pass


@attr.s
class MultiThreadedManager(TaskManager):
    """Multi threaded task management"""

    max_threads: int

    def create_tasks(
        self, reader: Callable, assets, *args, **kwargs
    ) -> Sequence[Tuple[futures.Future, str]]:
        """Create Future Tasks."""
        max_workers = kwargs.pop("threads", None) or self.max_threads
        with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            return [
                (executor.submit(reader, asset, *args, **kwargs), asset)
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


manager: TaskManager = TaskManager.create_from_env()


def multi_arrays(
    assets: Sequence[str],
    reader: Callable,
    *args: Any,
    threads: int = MAX_THREADS,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Multi array."""
    tasks = manager.create_tasks(reader, assets, *args, threads=threads, **kwargs)
    data, masks = zip(*[r for r, _ in manager.filter_tasks(tasks)])
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
    tasks = manager.create_tasks(reader, assets, *args, threads=threads, **kwargs)
    return {asset: val for val, asset in manager.filter_tasks(tasks)}
