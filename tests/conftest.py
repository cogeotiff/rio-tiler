"""``pytest`` configuration."""

from io import BytesIO
from typing import Sequence

import numpy
import pytest
import rasterio
from rasterio.crs import CRS
from rasterio.enums import ColorInterp
from rasterio.io import MemoryFile
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
        # Data
        arr = numpy.zeros((nband, height, width), dtype=dtype) + 1
        arr[:, 0:128, 0:128] = 0

        # Mask/Alpha
        mask = numpy.zeros((1, height, width), dtype=dtype) + 255
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

                return BytesIO(memfile.read())

    return _dataset
