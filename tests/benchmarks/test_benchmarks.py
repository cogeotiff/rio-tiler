"""Benchmark."""

import os
import pytest

import rasterio
import mercantile
from rio_tiler import utils

from . import benchmark_dataset, benchmark_tiles

cog_path = os.path.join(os.path.dirname(__file__), "data")


def read_tile(src_path, tile):
    """Benchmark rio-tiler.utils._tile_read."""
    tile_bounds = mercantile.xy_bounds(tile)

    # We make sure to not store things in cache.
    with rasterio.Env(GDAL_CACHEMAX=0):
        with rasterio.open(src_path) as src_dst:
            return utils._tile_read(src_dst, tile_bounds, 256)


@pytest.mark.parametrize("tile_name", ["full", "boundless"])
@pytest.mark.parametrize("dataset_info", benchmark_dataset)
def test_read_tile_1band(benchmark, dataset_info, tile_name, benchmark_fixtures):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    name = dataset_info["name"]
    dtype = dataset_info["dtype"]
    nodata_type = dataset_info["nodata_type"]
    nbands = dataset_info.get("nbands", 1)

    benchmark.group = "{}-{}-{}".format(name, dtype, nodata_type)
    fin = "{}/{}-{}-{}-{}b.tif".format(cog_path, name, dtype, nodata_type, nbands)
    tile = benchmark_tiles[name]["full"]
    data, mask = benchmark(read_tile, fin, tile)
