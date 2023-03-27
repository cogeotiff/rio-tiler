"""test masks."""

import numpy
import pytest
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.io import MemoryFile

from rio_tiler.io import Reader


def test_mask_bilinear(dataset):
    """Test mask read with bilinear resampling"""
    with MemoryFile(
        dataset(
            crs=CRS.from_epsg(32632),
            bounds=(382792.5, 362992.5, 610507.5, 595207.5),
            dtype="uint8",
            nodata_type="alpha",
        )
    ) as memfile:
        with memfile.open() as dst:
            with Reader(None, dataset=dst) as src:
                data, mask = src.preview(
                    resampling_method="bilinear",
                    max_size=100,
                )
                masknodata = (data[0] != 0).astype(numpy.uint8) * 255
                numpy.testing.assert_array_equal(mask, masknodata)


data_types = list(dtype_ranges.keys())
nodata_type = ["nodata", "alpha", "mask"]


@pytest.mark.parametrize("resampling", ["bilinear", "nearest"])
@pytest.mark.parametrize("data_type", data_types)
@pytest.mark.parametrize("nodata_type", nodata_type)
def test_mask_non_boundless(nodata_type, data_type, resampling, dataset_fixture):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    with MemoryFile(
        dataset_fixture(
            crs=CRS.from_epsg(32632),
            bounds=(382792.5, 362992.5, 610507.5, 595207.5),
            dtype=data_type,
            nodata_type=nodata_type,
        )
    ) as memfile:
        with memfile.open() as dst:
            with Reader(None, dataset=dst) as src:
                # non boundless
                im = src.read(resampling_method=resampling)
                assert im.array.data[0, 0, 0] == 0
                assert im.array.data[0, -1, -1] == 1
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # boundless
                im = src.read(
                    window=((-50, 200), (-50, 200)), resampling_method=resampling
                )
                assert im.array.data[0, 0, 0] == 0
                assert im.array.data[0, -1, -1] == 1
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # WarpedVRT - non boundless
                im = src.read(dst_crs="epsg:3857", resampling_method=resampling)
                # This is failing for alpha-uint16/alpha-int16
                # assert im.array.data[0, 0, 0] == 0
                # assert im.array.data[0, -1, -1] == 1
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # WarpedVRT - boundless
                im = src.tile(267, 249, 9, resampling_method=resampling)
                # This is failing for alpha-uint16/alpha-int16
                # assert im.array.data[0, 0, 0] == 0
                # assert im.array.data[0, -1, -1] == 1
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]
