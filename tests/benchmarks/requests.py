"""Test HTTP Requests."""

from rasterio.env import GDALVersion
from tilebench import profile

from rio_tiler.io import Reader

dataset_url = "https://titiler-benchmark-public.s3.us-east-1.amazonaws.com/cogs/S2C_33TVF_20260928_0_L2A_B04.tif"

gdal_version = GDALVersion.runtime()


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

    img, stats = get_tile(dataset_url, 2212, 1534, 12)
    assert img.array.shape == (1, 256, 256)
    assert stats["HEAD"]["count"] == 1
    assert stats["GET"]["count"] == 3
    assert stats["GET"]["bytes"] == 1643723
    # The two block requests run in parallel, their order is not stable
    assert sorted(stats["GET"]["ranges"]) == [
        # Header
        "0-32767",
        # The tile overlaps 2 × 2 blocks: (4,4) and (4,5) are consecutive in the
        # file and merged in one request, same for (5,4) and (5,5)
        "31709542-32505212",
        "35836623-36651906",
    ]
    assert stats["WarpKernels"]
