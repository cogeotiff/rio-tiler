"""``pytest`` configuration."""

import os

import pytest

import numpy

from rasterio.io import MemoryFile
from rasterio.transform import from_bounds
from rasterio.enums import ColorInterp

from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles


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

        profile_options = {"blockxsize": tilesize, "blockysize": tilesize}
        output_profile = cog_profiles.get("deflate")
        output_profile.update(profile_options)

        arr = numpy.random.randint(1, 255, size=(nband, y_size, x_size)).astype(
            numpy.uint8
        )
        arr[:, 0:500, 0:500] = 0

        mask = numpy.zeros((1, y_size, x_size), dtype=numpy.uint8) + 255
        mask[:, 0:500, 0:500] = 0

        w, s, e, n = bounds
        src_profile = dict(
            driver="GTiff",
            count=nband,
            dtype="uint8",
            height=y_size,
            width=x_size,
            crs=crs,
            transform=from_bounds(w, s, e, n, x_size, y_size),
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

                cog_translate(
                    mem,
                    fout,
                    output_profile,
                    config=gdal_config,
                    in_memory=True,
                    dtype=dtype,
                    quiet=True,
                    add_mask=True if nodata_type == "mask" else False,
                )

        return fout

    return _cloudoptimized_geotiff
