"""``pytest`` configuration."""

from io import BytesIO
from typing import Sequence

import numpy
import pytest
import rasterio
from rasterio.crs import CRS
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
        filled: bool = False,
    ):
        max_value = 127 if dtype == "int8" else 255

        # Data
        arr = numpy.zeros((nband, height, width), dtype=dtype) + 1
        if filled:
            arr[:, range(height), range(width)] = max_value
            arr[:, range(height - 1, 0, -1), range(width - 1)] = max_value
            arr[:, :, width // 2] = max_value
            arr[:, height // 2, :] = max_value

        arr[:, 0:128, 0:128] = 0

        # Mask/Alpha
        mask = numpy.zeros((1, height, width), dtype=dtype) + max_value
        mask[:, 0:128, 0:128] = 0

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
            src_profile["nodata"] = 0

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
                        data = numpy.concatenate([arr, mask])
                        ci += [ColorInterp.alpha]

                    else:
                        data = arr

                    mem.colorinterp = ci

                    # Write Data
                    mem.write(data)

                    # Write Mask
                    if nodata_type == "mask":
                        mem.write_mask(mask[0])

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
