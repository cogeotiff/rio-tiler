"""``pytest`` configuration."""

import os

import numpy
import pytest
import rasterio
from rasterio.enums import ColorInterp
from rasterio.io import MemoryFile
from rasterio.shutil import copy
from rasterio.transform import from_bounds

with rasterio.Env() as env:
    drivers = env.drivers()


requires_webp = pytest.mark.skipif(
    "WEBP" not in drivers.keys(), reason="Only relevant if WEBP drivers is supported"
)


@pytest.fixture
def cloudoptimized_geotiff():
    """Create CloudOptimized GeoTIFF fixture."""

    def _cloudoptimized_geotiff(
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
        fout = "{}/{}-{}-{}-{}b.tif".format(output_dir, name, dtype, nodata_type, nband)
        if os.path.exists(fout):
            return fout

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        # Data
        arr = numpy.random.randint(1, 255, size=(nband, y_size, x_size)).astype(dtype)

        arr[:, 0:500, 0:500] = 0

        # Mask
        mask = numpy.zeros((1, y_size, x_size), dtype=dtype) + 255
        mask[:, 0:500, 0:500] = 0

        # Input Profile
        src_profile = dict(
            driver="GTiff",
            count=nband,
            dtype=dtype,
            height=y_size,
            width=x_size,
            crs=crs,
            transform=from_bounds(*bounds, x_size, y_size),
        )
        if nodata_type in ["nodata", "mask"]:
            src_profile["nodata"] = 0
        elif nodata_type == "alpha":
            src_profile["count"] = nband + 1

        gdal_config = dict(
            GDAL_NUM_THREADS="ALL_CPUS",
            GDAL_TIFF_INTERNAL_MASK=True,
            GDAL_TIFF_OVR_BLOCKSIZE="128",
        )
        with rasterio.Env(**gdal_config):
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

                    # Write Data
                    mem.write(data)

                    # Write Mask
                    if nodata_type == "mask":
                        mem.write_mask(mask.astype("uint8"))

                    output_profile = {
                        "driver": "COG",
                        "blocksize": tilesize,
                        "compress": "DEFLATE",
                    }
                    copy(mem, fout, **output_profile)

        return fout

    return _cloudoptimized_geotiff
