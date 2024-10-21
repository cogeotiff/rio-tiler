"""Test HTTP Requests."""

import pytest
from rasterio.env import GDALVersion
from tilebench import profile

from rio_tiler.io import Reader

dataset_url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/15/T/VK/2023/10/S2B_15TVK_20231008_0_L2A/TCI.tif"

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
    def info(src_path: str):
        with Reader(src_path) as src_dst:
            return src_dst.info()

    info, stats = info(dataset_url)
    assert info.bounds

    print(stats)
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
    def tile(src_path: str, x: int, y: int, z: int):
        with Reader(src_path) as src_dst:
            return src_dst.tile(x, y, z, tilesize=256)

    img, stats = tile(
        dataset_url,
        493,
        741,
        11,
    )
    assert img.array.shape == (3, 256, 256)

    print(stats)
    assert stats["HEAD"]["count"] == 1
    assert stats["GET"]["count"] == 3
    assert stats["GET"]["bytes"] == 2293760
    assert stats["GET"]["ranges"] == [
        "0-32767",
        "9011200-10158079",
        "11075584-12189695",
    ]
    assert stats["WarpKernels"]
