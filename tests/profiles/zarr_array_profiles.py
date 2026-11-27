"""Profiles for zarr-python Array Readers.

Run with:

    uv run pytest tests/profiles/zarr_array_profiles.py -s

=== GroupReader.tile ===
store calls: {'read_only': 1, '_ensure_open': 1, 'get': 2}
1.254 test_sync_group_reader  tests/profiles/zarr_array_profiles.py:92
├─ 0.663 open_group  zarr/api/synchronous.py:496
│     [4 frames hidden]  zarr, concurrent, threading
│        0.663 lock.acquire  <built-in>
└─ 0.592 GroupReader.tile  rio_tiler/io/zarr.py:3846
   └─ 0.592 GroupReader.part  rio_tiler/io/zarr.py:3910
      └─ 0.592 _part  rio_tiler/io/zarr.py:3955
         └─ 0.578 ArrayReader.part  rio_tiler/io/zarr.py:1432
            └─ 0.567 ArrayReader._read  rio_tiler/io/zarr.py:1734
               └─ 0.567 Array.get_orthogonal_selection  zarr/core/array.py:3103
                     [4 frames hidden]  zarr, concurrent, threading
                        0.567 lock.acquire  <built-in>

=== AsyncGroupReader.tile ===
store calls: {'read_only': 1, '_ensure_open': 1, 'get': 2}
1.266 Handle._run  asyncio/events.py:92
├─ 0.664 test_async_group_reader  tests/profiles/zarr_array_profiles.py:106
│  └─ 0.663 open_group  zarr/api/asynchronous.py:814
│        [13 frames hidden]  zarr, functools
│           0.613 ObjectStore.get  zarr/storage/_obstore.py:97
│           └─ 0.613 [await]  zarr/storage/_obstore.py
├─ 0.444 _fetch_group  zarr/core/_coalesce.py:38
│  └─ 0.444 ObjectStore.get  zarr/storage/_obstore.py:97
│     └─ 0.444 [await]  zarr/storage/_obstore.py
└─ 0.138 run  zarr/core/common.py:133
      [7 frames hidden]  zarr

"""

import logging

import pytest
import zarr
from obstore.store import HTTPStore
from pyinstrument import Profiler
from zarr.storage import LoggingStore, ObjectStore

from rio_tiler.io.zarr import AsyncGroupReader, GroupReader

src_path = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260928T095031_N0513_R079_T33TVF_20260928T130916.zarr/measurements/reflectance"

# zoom 14 is close to the native 10m resolution
tile = (8849, 6139, 14)


@pytest.fixture(autouse=True)
def clear_group_metadata_cache():
    """Clear the (shared) group metadata caches so each profile starts cold."""
    AsyncGroupReader.get_group_metadata.cache_clear()
    AsyncGroupReader.list_variables.cache_clear()
    GroupReader.get_group_metadata.cache_clear()
    GroupReader.list_variables.cache_clear()
    yield


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


# def test_sync_array_reader():
#     """profile ArrayReader on a remote zarr Array."""
#     # Spatial metadata is stored on the `r10m` group, not on the arrays
#     array_options = {
#         "crs": CRS.from_epsg(32633),
#         "transform": Affine(10.0, 0.0, 399965.0, 0.0, -10.0, 4600015.0),
#         "spatial_dims": ["y", "x"],
#     }

#     store = _store()
#     profiler = Profiler()
#     with profiler:
#         group = zarr.open_group(store=store, mode="r", zarr_format=3)
#         array = cast(zarr.Array, group[array_path])
#         with ArrayReader(input=array, **array_options) as src:
#             img = src.tile(*tile)

#     assert img.array.shape == (1, 256, 256)
#     _print_profile("ArrayReader.tile", profiler, store)


# @pytest.mark.asyncio
# async def test_async_array_reader():
#     """profile AsyncArrayReader on a remote zarr Array."""
#     # Spatial metadata is stored on the `r10m` group, not on the arrays
#     array_options = {
#         "crs": CRS.from_epsg(32633),
#         "transform": Affine(10.0, 0.0, 399965.0, 0.0, -10.0, 4600015.0),
#         "spatial_dims": ["y", "x"],
#     }

#     store = _store()
#     profiler = Profiler(async_mode="enabled")
#     with profiler:
#         group = await zarr.api.asynchronous.open_group(store=store, mode="r", zarr_format=3)
#         array = cast(zarr.AsyncArray, await group.getitem(array_path))
#         async with AsyncArrayReader(input=array, **array_options) as src:
#             img = await src.tile(*tile)

#     assert img.array.shape == (1, 256, 256)
#     _print_profile("AsyncArrayReader.tile", profiler, store)


def test_sync_group_reader():
    """profile GroupReader on a remote zarr Group."""
    store = _store()

    profiler = Profiler()
    with profiler:
        group = zarr.open_group(store=store, mode="r", zarr_format=3)
        with GroupReader(input=group) as src:
            img = src.tile(*tile, variables=["b04"])

    assert img.array.shape == (1, 256, 256)
    _print_profile("GroupReader.tile", profiler, store)


@pytest.mark.asyncio
async def test_async_group_reader():
    """profile AsyncGroupReader on a remote zarr Group."""
    store = _store()

    profiler = Profiler(async_mode="enabled")
    with profiler:
        group = await zarr.api.asynchronous.open_group(
            store=store, mode="r", zarr_format=3
        )
        async with AsyncGroupReader(input=group) as src:
            img = await src.tile(*tile, variables=["b04"])

    assert img.array.shape == (1, 256, 256)
    _print_profile("AsyncGroupReader.tile", profiler, store)
