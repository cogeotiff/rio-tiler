"""``pytest`` configuration."""

from io import BytesIO
from typing import Sequence

import numpy
import pytest
import rasterio
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import ColorInterp
from rasterio.enums import Resampling as ResamplingEnums
from rasterio.io import MemoryFile
from rasterio.rio.overview import get_maximum_overview_level
from rasterio.shutil import copy
from rasterio.transform import from_bounds

with rasterio.Env() as env:
    drivers = env.drivers()


requires_webp = pytest.mark.skipif(
    "WEBP" not in drivers.keys(), reason="Only relevant if WEBP drivers is supported"
)


@pytest.fixture
def dataset_fixture():
    """raster fixture."""

    def _dataset(
        crs: CRS,
        bounds: Sequence[float],
        dtype: str,
        nodata_type: str,
        nband: int = 3,
        width: int = 256,
        height: int = 256,
    ):
        min_value, max_value = dtype_ranges[dtype]

        arr = numpy.full((nband, height, width), fill_value=max_value, dtype=dtype)
        arr[:, 0 : height // 2, 0 : width // 2] = 1

        # Input Profile
        src_profile = {
            "driver": "GTiff",
            "count": nband,
            "dtype": dtype,
            "height": height,
            "width": width,
            "crs": crs,
            "transform": from_bounds(*bounds, width, height),
        }

        if nodata_type == "nodata":
            src_profile["nodata"] = 1

        elif nodata_type == "alpha":
            src_profile["count"] = nband + 1

        with rasterio.Env(GDAL_TIFF_INTERNAL_MASK=True):
            with MemoryFile() as memfile:
                with memfile.open(**src_profile) as mem:
                    if nband == 3:
                        ci = [ColorInterp.red, ColorInterp.green, ColorInterp.blue]

                    else:
                        ci = [ColorInterp.gray]
                        if nband > 1:
                            ci += [ColorInterp.undefined] * (nband - 1)

                    if nodata_type == "alpha":
                        # Mask/Alpha
                        mask = numpy.full(
                            (1, height, width), fill_value=max_value, dtype=dtype
                        )
                        mask[:, 0 : height // 2, 0 : width // 2] = min_value
                        data = numpy.concatenate([arr, mask])
                        ci += [ColorInterp.alpha]

                    else:
                        data = arr

                    mem.colorinterp = ci

                    # Write Data
                    mem.write(data)

                    # Write Mask
                    if nodata_type == "mask":
                        mask = numpy.zeros((height, width), dtype=dtype) + 1
                        mask[0 : height // 2, 0 : width // 2] = 0
                        mem.write_mask(mask)

                    overview_level = get_maximum_overview_level(
                        mem.width, mem.height, minsize=512
                    )
                    overviews = [2**j for j in range(1, overview_level + 1)]
                    mem.build_overviews(overviews, ResamplingEnums.bilinear)

                    cog_profile = {
                        "interleave": "pixel",
                        "compress": "DEFLATE",
                        "tiled": True,
                        "blockxsize": 512,
                        "blockysize": 512,
                    }

                    with MemoryFile() as cogfile:
                        copy(mem, cogfile.name, copy_src_overviews=True, **cog_profile)
                        return BytesIO(cogfile.read())

    return _dataset
