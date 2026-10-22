"""Profiles for zarr-python Array Readers.

Run with:

    uv run pytest tests/profiles/zarr_array_profiles.py -s

"""

import logging
from typing import cast

import pytest
import zarr
from affine import Affine
from obstore.store import HTTPStore
from pyinstrument import Profiler
from rasterio.crs import CRS
from zarr.storage import LoggingStore, ObjectStore

from rio_tiler.experimental.zarr import ArrayReader, AsyncArrayReader

src_path = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance"
array_path = "r10m/b04"

# Spatial metadata is stored on the `r10m` group, not on the arrays
array_options = {
    "crs": CRS.from_epsg(32626),
    "transform": Affine(10.0, 0.0, 399965.0, 0.0, -10.0, 4400035.0),
    "spatial_dims": ["y", "x"],
}

# zoom 14 is close to the native 10m resolution
tile = (6944, 6268, 14)


def _store() -> LoggingStore:
    """Remote store counting the calls made by zarr."""
    return LoggingStore(
        ObjectStore(store=HTTPStore(src_path), read_only=True),
        log_level="WARNING",
        log_handler=logging.NullHandler(),
    )


def _print_profile(title: str, profiler: Profiler, store: LoggingStore):
    print(f"\n=== {title} ===")
    print(f"store calls: {dict(store.counter)}")
    print(profiler.output_text(unicode=True, color=False, short_mode=True))


def test_sync_array_reader():
    """profile ArrayReader on a remote zarr Array."""
    store = _store()

    profiler = Profiler()
    with profiler:
        group = zarr.open_group(store=store, mode="r")
        array = cast(zarr.Array, group[array_path])
        with ArrayReader(input=array, **array_options) as src:
            img = src.tile(*tile)

    assert img.array.shape == (1, 256, 256)
    _print_profile("ArrayReader.tile", profiler, store)


@pytest.mark.asyncio
async def test_async_array_reader():
    """profile AsyncArrayReader on a remote zarr Array."""
    store = _store()

    profiler = Profiler(async_mode="enabled")
    with profiler:
        group = await zarr.api.asynchronous.open_group(store=store, mode="r")
        array = cast(zarr.AsyncArray, await group.getitem(array_path))
        async with AsyncArrayReader(input=array, **array_options) as src:
            img = await src.tile(*tile)

    assert img.array.shape == (1, 256, 256)
    _print_profile("AsyncArrayReader.tile", profiler, store)
