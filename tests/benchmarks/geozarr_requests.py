"""Test HTTP Requests.

uv run pytest tests/benchmarks/geozarr_requests.py -o log_cli=true --log-cli-level=INFO

"""

import pytest
import zarr
from obstore.store import HTTPStore
from zarr.storage import LoggingStore, ObjectStore

from rio_tiler.experimental.zarr import GroupReader

src_path = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/geozarrs/S2C_MSIL2A_20260810T125031_N0512_R095_T26SMJ_20260810T155917.zarr/measurements/reflectance"


@pytest.fixture(autouse=True)
def clear_group_metadata_cache():
    """Clear the GroupReader metadata cache."""
    GroupReader.get_group_metadata.cache_clear()
    GroupReader.list_variables.cache_clear()


@pytest.mark.xfail
def test_info():
    """Info should only do 1 HTTP request."""
    zarr_store = LoggingStore(
        ObjectStore(store=HTTPStore(src_path), read_only=True),
    )
    group = zarr.open_group(
        store=zarr_store, mode="r", zarr_format=3, use_consolidated=True
    )
    with GroupReader(input=group) as src:
        metadata = src.info()

    assert metadata.driver == "GeoZarr"
    assert metadata.bounds[0] == 399965.0
    assert zarr_store.counter["get"] == 1


@pytest.mark.xfail
def test_tile_read():
    """Tile Read tests."""
    zarr_store = LoggingStore(
        ObjectStore(store=HTTPStore(src_path), read_only=True),
    )
    group = zarr.open_group(
        store=zarr_store, mode="r", zarr_format=3, use_consolidated=True
    )
    with GroupReader(input=group) as src:
        img = src.tile(1736, 1567, 12, variables=["b02"], tilesize=256)

    assert img.array.shape == (1, 256, 256)
    # 1 GET for the zarr.json
    # 1 GET for the block c/0/0
    assert zarr_store.counter["get"] == 2
