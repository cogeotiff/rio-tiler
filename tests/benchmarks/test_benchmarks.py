"""Benchmark."""

import os

import mercantile
import pytest
import rasterio

from rio_tiler import constants, reader

from . import benchmark_dataset, benchmark_tiles

cog_path = os.path.join(os.path.dirname(__file__), "data")


def read_tile(src_path, tile):
    """Benchmark rio-tiler.utils._tile_read."""
    tile_bounds = mercantile.xy_bounds(tile)
    # We make sure to not store things in cache.
    with rasterio.Env(GDAL_CACHEMAX=0, NUM_THREADS="all"):
        with rasterio.open(src_path) as src_dst:
            return reader.part(
                src_dst,
                tile_bounds,
                256,
                256,
                resampling_method="nearest",
                dst_crs=constants.WEB_MERCATOR_CRS,
            )


@pytest.mark.parametrize("tile_name", ["full", "boundless"])
@pytest.mark.parametrize("dataset_info", benchmark_dataset)
def test_tile(benchmark, dataset_info, tile_name, cloudoptimized_geotiff):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    src_path = cloudoptimized_geotiff(cog_path, **dataset_info)

    name = dataset_info["name"]
    dtype = dataset_info["dtype"]
    nodata_type = dataset_info["nodata_type"]

    benchmark.name = "{}-{}".format(dtype, nodata_type)
    benchmark.group = "{} tile ".format(tile_name)

    tile = benchmark_tiles[name][tile_name]
    data, mask = benchmark(read_tile, src_path, tile)
