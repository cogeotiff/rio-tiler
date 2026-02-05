"""Benchmark."""

import os
from datetime import datetime
from unittest.mock import patch

import morecantile
import numpy
import pytest
import rasterio
import xarray
from rasterio.coords import BoundingBox
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.io import MemoryFile

from rio_tiler.io import Reader, STACReader, XarrayReader
from rio_tiler.io.stac import fetch
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.mosaic.methods.defaults import FirstMethod, MeanMethod

stac_item = "https://stac.eoapi.dev/collections/MAXAR_afghanistan_earthquake22/items/42_120200201121_10300100D4928800"
_ = fetch(stac_item)  # Cache the STAC Item for the benchmarks.

asset1 = os.path.join(os.path.dirname(__file__), "..", "fixtures", "mosaic_value_1.tif")
asset2 = os.path.join(os.path.dirname(__file__), "..", "fixtures", "mosaic_value_2.tif")
assets = [asset2, asset1]

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


@pytest.mark.parametrize("dataset_name", ["equator", "dateline"])
@pytest.mark.parametrize("data_type", list(dtype_ranges.keys()))
@pytest.mark.parametrize("nodata_type", ["nodata", "alpha", "mask", "none"])
def test_tile(nodata_type, data_type, dataset_name, dataset_fixture, benchmark):
    """Benchmark Reader.tile method."""
    benchmark.name = f"{dataset_name}-{data_type}-{nodata_type}"
    benchmark.fullname = f"{dataset_name}-{data_type}-{nodata_type}"
    benchmark.group = dataset_name

    def _tile(dst, tile):
        with Reader(None, dataset=dst) as src:
            return src.tile(*tile)

    tile = benchmark_tiles[dataset_name]["full"]
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
                img = benchmark(_tile, dst, tile)
                assert img.data.dtype == data_type


@pytest.mark.parametrize("threads", [1, 10])
@patch("rio_tiler.io.stac.STAC_ALTERNATE_KEY", "public")
def test_stac(threads, benchmark):
    """Benchmark STACReader."""
    benchmark.name = "STACReader" if threads == 1 else "STACReader-With-Threads"
    benchmark.fullname = "STACReader" if threads == 1 else "STACReader-With-Threads"
    benchmark.group = "STACReader" if threads == 1 else "STACReader-With-Threads"

    def _tile():
        with STACReader(stac_item) as src:
            return src.tile(
                11365, 6592, 14, assets=["visual", "ms_analytic"], threads=threads
            )

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", NUM_THREADS="all"):
        _ = benchmark(_tile)


def test_xarray(benchmark):
    """Benchmark XarrayReader."""
    benchmark.name = "XarrayReader"
    benchmark.fullname = "XarrayReader"
    benchmark.group = "XarrayReader"

    arr = numpy.arange(0.0, 1000 * 500 * 3, dtype="float32").reshape(3, 500, 1000)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.linspace(-177.5, 177.5, 1000),
            "y": numpy.linspace(87.5, -87.5, 500),
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})
    data.rio.write_crs("epsg:4326", inplace=True)

    def _tile():
        with XarrayReader(data) as dst:
            _ = dst.tile(0, 0, 1)

    _ = benchmark(_tile)


@pytest.mark.parametrize("threads", [1, 10])
@pytest.mark.parametrize("method", [FirstMethod, MeanMethod])
def test_mosaic(method, threads, benchmark):
    """Benchmark mosaic_reader."""
    benchmark.name = (
        f"Mosaic-{method.__name__}"
        if threads == 1
        else f"Mosaic-{method.__name__}-With-Threads"
    )
    benchmark.fullname = (
        f"Mosaic-{method.__name__}"
        if threads == 1
        else f"Mosaic-{method.__name__}-With-Threads"
    )
    benchmark.group = (
        f"Mosaic-{method.__name__}"
        if threads == 1
        else f"Mosaic-{method.__name__}-With-Threads"
    )

    def _tile():
        def _reader(asset, *args, **kwargs):
            with Reader(asset) as src:
                return src.tile(*args, **kwargs)

        # Full covered tile
        # Tile 9-150-182 fully covering mosaic_value_1 an partially covering mosaic_value_2
        return mosaic_reader(
            assets * 3, _reader, 150, 182, 9, threads=threads, pixel_selection=method()
        )

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", NUM_THREADS="all"):
        _ = benchmark(_tile)
