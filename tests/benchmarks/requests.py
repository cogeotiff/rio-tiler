"""Test HTTP Requests."""

import pytest
from rasterio.env import GDALVersion
from tilebench import profile

from rio_tiler.io import Reader

dataset_url = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_26SMJ_20260810_0_L2A_B04.tif"

gdal_version = GDALVersion.runtime()


@pytest.mark.xfail
def test_info():
    """Info should only GET the header."""

    @profile(
        kernels=True,
        config={
            "GDAL_HTTP_MERGE_CONSECUTIVE_RANGES": "YES",
            "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
            "GDAL_INGESTED_BYTES_AT_OPEN": 32768,
        },
        quiet=True,
        add_to_return=True,
    )
    def get_info(src_path: str):
        with Reader(input=src_path, options={}) as src_dst:
            return src_dst.info()

    metadata, stats = get_info(dataset_url)
    assert metadata.driver == "GTiff"
    assert metadata.bounds[0] == 399960.0
    assert stats["HEAD"]["count"] == 1
    assert stats["GET"]["count"] == 1
    assert stats["GET"]["bytes"] == 32768
    assert stats["GET"]["ranges"] == ["0-32767"]
    assert not stats["WarpKernels"]


@pytest.mark.xfail
def test_tile_read():
    """Tile Read tests."""

    @profile(
        kernels=True,
        config={
            "GDAL_HTTP_MERGE_CONSECUTIVE_RANGES": "YES",
            "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",
            "GDAL_INGESTED_BYTES_AT_OPEN": 32768,
            "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": ".tif",
            "CPL_VSIL_CURL_NON_CACHED": f"/vsicurl/{dataset_url}",
        },
        quiet=True,
        add_to_return=True,
    )
    def get_tile(src_path: str, x: int, y: int, z: int):
        with Reader(input=src_path, options={}) as src_dst:
            return src_dst.tile(x, y, z, tilesize=256)

    img, stats = get_tile(dataset_url, 1736, 1567, 12)
    assert img.array.shape == (1, 256, 256)
    assert stats["HEAD"]["count"] == 1
    assert stats["GET"]["count"] == 3
    assert stats["GET"]["bytes"] == 677661
    assert stats["GET"]["ranges"] == [
        # Header
        "0-32767",
        # To construct the tile we need to fetch the following blocks
        # We can't merge the request because they are not consecutive
        # Block 1
        "50341499-50714262",
        # Block 2
        "53732093-54004221",
    ]
    assert stats["WarpKernels"]
