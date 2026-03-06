"""test masks."""

import numpy
import pytest
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.io import MemoryFile

from rio_tiler.io import Reader


def test_mask_bilinear(dataset_fixture):
    """Test mask read with bilinear resampling"""
    _, max_value = dtype_ranges["uint8"]

    # Internal Mask
    with MemoryFile(
        dataset_fixture(
            crs=CRS.from_epsg(32632),
            bounds=(382792.5, 362992.5, 610507.5, 595207.5),
            dtype="uint8",
            nodata_type="mask",
        )
    ) as memfile:
        with memfile.open() as dst:
            with Reader(None, dataset=dst) as src:
                img = src.read(resampling_method="bilinear", max_size=100)
                masknodata = (img.data[0] == 255).astype(numpy.uint8) * 255
                numpy.testing.assert_array_equal(img.mask, masknodata)

                img = src.preview(resampling_method="nearest", max_size=100)
                masknodata = (img.data[0] == 255).astype(numpy.uint8) * max_value
                numpy.testing.assert_array_equal(img.mask, masknodata)

    # Alpha Band
    with MemoryFile(
        dataset_fixture(
            crs=CRS.from_epsg(32632),
            bounds=(382792.5, 362992.5, 610507.5, 595207.5),
            dtype="uint8",
            nodata_type="alpha",
        )
    ) as memfile:
        with memfile.open() as dst:
            with Reader(None, dataset=dst) as src:
                img = src.read(resampling_method="bilinear", max_size=100)

                masknodata = (img.data[0] != 0).astype(numpy.uint8) * 255
                numpy.testing.assert_raises(
                    AssertionError,
                    numpy.testing.assert_array_equal,
                    img.mask,
                    masknodata,
                )
                # because we use `bilinear` resampling
                # we are creating partial values between 0 and 255 in the alpha band
                assert len(numpy.unique(img.mask)) > 2

                # Check that partial transparent pixel are masked
                alpha_mask = img.alpha_mask == 255
                numpy.testing.assert_array_equal(img.array.mask[0], ~alpha_mask)


data_types = list(dtype_ranges.keys())
nodata_type = ["nodata", "alpha", "mask"]


@pytest.mark.parametrize("resampling", ["bilinear", "nearest"])
@pytest.mark.parametrize("data_type", data_types)
@pytest.mark.parametrize("nodata_type", nodata_type)
def test_mask_non_boundless(nodata_type, data_type, resampling, dataset_fixture):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    _, max_value = dtype_ranges[data_type]

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
                assert im.array.data[0, 0, 0] == 1
                assert im.array.data[0, -1, -1] == max_value
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # boundless
                im = src.read(
                    window=((-50, 200), (-50, 200)), resampling_method=resampling
                )
                nodata = im.nodata if im.nodata is not None else 0
                assert im.array.data[0, 0, 0] == nodata
                assert im.array.data[0, -1, -1] == max_value
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # # WarpedVRT - non boundless
                im = src.read(
                    dst_crs="epsg:3857", resampling_method=resampling, max_size=10
                )
                nodata = im.nodata if im.nodata is not None else 0
                assert im.array.data[0, 0, 0] == nodata
                assert im.array.data[0, -1, -1] == max_value
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # WarpedVRT - boundless
                im = src.tile(267, 249, 9, resampling_method=resampling)
                assert im.array.data[0, 0, 0] == nodata
                assert im.array.data[0, -1, -1] == max_value
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]

                # With padding
                im = src.tile(267, 249, 9, resampling_method=resampling, padding=2)
                assert im.array.data[0, 0, 0] == nodata
                assert im.array.data[0, -1, -1] == max_value
                assert im.array.mask[0, 0, 0]
                assert not im.array.mask[0, -1, -1]
