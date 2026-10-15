"""rio-tiler experimental utilities."""

from __future__ import annotations

import asyncio
from collections.abc import Callable

import rasterio


async def run_sync[**P, T](func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    """Run a blocking function in a worker thread to avoid blocking the event loop.

    rasterio's GDAL environment is thread-local, so options from an active
    `rasterio.Env` are re-applied in the worker thread.
    """
    if not rasterio.env.hasenv():
        return await asyncio.to_thread(func, *args, **kwargs)

    options = rasterio.env.getenv()

    def _run() -> T:
        with rasterio.Env(**options):
            return func(*args, **kwargs)

    return await asyncio.to_thread(_run)
