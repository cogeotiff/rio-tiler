"""Benchmark."""

import morecantile
import pytest
import rasterio
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.io import MemoryFile

from rio_tiler.io import Reader

benchmark_tiles = {
    "north": {
        "full": morecantile.Tile(x=70, y=17, z=7),
        "masked": morecantile.Tile(x=69, y=16, z=7),
        "boundless": morecantile.Tile(x=68, y=17, z=7),
    },
    "south": {
        "full": morecantile.Tile(x=124, y=108, z=7),
        "masked": morecantile.Tile(x=125, y=109, z=7),
        "boundless": morecantile.Tile(x=122, y=107, z=7),
    },
    "equator": {
        "full": morecantile.Tile(x=537, y=499, z=10),
        "masked": morecantile.Tile(x=535, y=498, z=10),
        "boundless": morecantile.Tile(x=540, y=497, z=10),
    },
    "dateline": {
        "full": morecantile.Tile(x=510, y=168, z=9),
        "masked": morecantile.Tile(x=511, y=169, z=9),
        "boundless": morecantile.Tile(x=1, y=171, z=9),
    },
}

# LC08_L1TP_212004_20190816_20190902_01_T1
north = {
    "bounds": BoundingBox(left=433192.5, bottom=8534992.5, right=707407.5, top=8809207.5),
    "crs": CRS.from_epsg(32633),
}

# LC08_L1GT_054115_20200120_20200120_01_RT
south = {
    "bounds": BoundingBox(
        left=123892.5, bottom=-1521007.5, right=387607.5, top=-1258492.5
    ),
    "crs": CRS.from_epsg(3031),
}

# LC08_L1TP_085024_20170816_20170825_01_T1
dateline = {
    "bounds": BoundingBox(left=570292.5, bottom=5612092.5, right=803107.5, top=5847607.5),
    "crs": CRS.from_epsg(32660),
}

# LC08_L1TP_187057_20151212_20170401_01_T1
equator = {
    "name": "equator",
    "bounds": BoundingBox(left=382792.5, bottom=362992.5, right=610507.5, top=595207.5),
    "crs": CRS.from_epsg(32632),
}

datasets = {
    "north": north,
    "south": south,
    "dateline": dateline,
    "equator": equator,
}


def read_tile(dst, tile):
    """Benchmark rio-tiler.utils._tile_read."""
    # We make sure to not store things in cache.
    with Reader(None, dataset=dst) as src:
        return src.tile(*tile)


data_types = list(dtype_ranges.keys())
nodata_type = ["nodata", "alpha", "mask", "none"]


@pytest.mark.parametrize("tile_name", ["full"])
@pytest.mark.parametrize("dataset_name", ["equator", "dateline"])
@pytest.mark.parametrize("data_type", list(dtype_ranges.keys()))
@pytest.mark.parametrize("nodata_type", ["nodata", "alpha", "mask", "none"])
def test_tile(
    nodata_type, data_type, dataset_name, tile_name, dataset_fixture, benchmark
):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    benchmark.name = f"{data_type}-{nodata_type}"
    benchmark.group = f"{dataset_name} - {tile_name} tile "
    tile = benchmark_tiles[dataset_name][tile_name]

    dst_info = datasets[dataset_name]
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", NUM_THREADS="all"):
        with MemoryFile(
            dataset_fixture(
                crs=dst_info["crs"],
                bounds=list(dst_info["bounds"]),
                dtype=data_type,
                nodata_type=nodata_type,
                width=4000,
                height=4000,
                filled=True,
            )
        ) as memfile:
            with memfile.open() as dst:
                img = benchmark(read_tile, dst, tile)
                assert img.data.dtype == data_type
