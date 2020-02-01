"""``pytest`` configuration."""

import os

import pytest

import numpy

import rasterio
from rasterio.io import MemoryFile
from rasterio.transform import from_bounds
from rasterio.enums import ColorInterp

from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles

with rasterio.Env() as env:
    drivers = env.drivers()


requires_webp = pytest.mark.skipif(
    "WEBP" not in drivers.keys(), reason="Only relevant if WEBP drivers is supported"
)


def create_cog(
    output_dir,
    name,
    crs,
    bounds,
    dtype,
    nodata_type,
    tilesize=256,
    nband=1,
    x_size=2000,
    y_size=2000,
):
    """Create COG fixture."""
    fout = "{}/{}-{}-{}-{}b.tif".format(output_dir, name, dtype, nodata_type, nband)
    if os.path.exists(fout):
        return fout

    profile_options = {"blockxsize": tilesize, "blockysize": tilesize}
    output_profile = cog_profiles.get("deflate")
    output_profile.update(profile_options)

    arr = numpy.random.randint(1, 255, size=(nband, y_size, x_size)).astype(numpy.uint8)
    arr[:, 0:500, 0:500] = 0

    mask = numpy.zeros((1, y_size, x_size), dtype=numpy.uint8) + 255
    mask[:, 0:500, 0:500] = 0

    kwargs = dict(count=nband)
    if nodata_type in ["nodata", "mask"]:
        kwargs.update(dict(nodata=0))
    elif nodata_type == "alpha":
        kwargs.update(dict(count=nband + 1))

    src_profile = dict(
        driver="GTiff",
        dtype="uint8",
        height=y_size,
        width=x_size,
        crs=crs,
        transform=from_bounds(*bounds, x_size, y_size),
        **kwargs,
    )

    gdal_config = dict(
        GDAL_NUM_THREADS="ALL_CPUS",
        GDAL_TIFF_INTERNAL_MASK=True,
        GDAL_TIFF_OVR_BLOCKSIZE="128",
    )

    with MemoryFile() as memfile:
        with memfile.open(**src_profile) as mem:
            ci = [ColorInterp.gray]
            if nband > 1:
                ci += [ColorInterp.undefined] * (nband - 1)

            if nodata_type == "alpha":
                data = numpy.concatenate([arr, mask])
                ci += [ColorInterp.alpha]
            else:
                data = arr

            mem.colorinterp = ci
            mem.write(data)

            kwargs = {"add_mask": True} if nodata_type == "mask" else {}
            cog_translate(
                mem,
                fout,
                output_profile,
                config=gdal_config,
                in_memory=True,
                dtype=dtype,
                quiet=True,
                **kwargs,
            )

    return fout


@pytest.fixture()
def benchmark_fixtures():
    """Create benchmark fixtures."""
    from .benchmarks import benchmark_dataset

    print("Creating Benchmark dataset...")
    databench_dir = os.path.join(os.path.dirname(__file__), "benchmarks", "data")

    if not os.path.isdir(databench_dir):
        os.mkdir(databench_dir)

    for dataset in benchmark_dataset:
        create_cog(databench_dir, **dataset)
