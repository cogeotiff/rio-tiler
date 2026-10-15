"""test rio_tiler.experimental._utils."""

import threading

import pytest
import rasterio
from rasterio.env import getenv, hasenv

from rio_tiler.experimental._utils import run_sync


@pytest.mark.asyncio
async def test_run_sync():
    """Should run the function in a worker thread."""

    def _func(a, b=1):
        return a + b, threading.get_ident()

    res, ident = await run_sync(_func, 1, b=2)
    assert res == 3
    assert ident != threading.get_ident()


@pytest.mark.asyncio
async def test_run_sync_env():
    """Should forward the rasterio environment to the worker thread."""

    def _func():
        return getenv() if hasenv() else None

    assert await run_sync(_func) is None

    with rasterio.Env(GDAL_NUM_THREADS="2"):
        options = await run_sync(_func)
    assert options["GDAL_NUM_THREADS"] == "2"
