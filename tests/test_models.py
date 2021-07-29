"""Test rio_tiler.models."""

from io import BytesIO

import numpy
import pytest
import rasterio

from rio_tiler.errors import InvalidDatatypeWarning
from rio_tiler.models import ImageData


def test_imageData_AutoRescaling():
    """Test ImageData auto rescaling."""
    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="float32")).render(img_format="PNG")
        assert len(w.list) == 2  # NotGeoreferencedWarning and InvalidDatatypeWarning

    with pytest.warns(None) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint8")).render(img_format="PNG")
        assert len(w.list) == 1  # only NotGeoreferencedWarning

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="int8")).render(img_format="PNG")

    with pytest.warns(None) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(img_format="PNG")
        assert len(w.list) == 1

    with pytest.warns(None) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(img_format="GTiff")
        assert len(w.list) == 0

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(img_format="jpeg")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((3, 256, 256), dtype="uint16")).render(img_format="WEBP")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((3, 256, 256), dtype="int8")).render(
            img_format="JP2OpenJPEG"
        )


@pytest.mark.parametrize(
    "dtype",
    ["uint8", "int8", "uint16", "int16", "uint32", "int32", "float32", "float64"],
)
def test_imageData_AutoRescalingAllTypes(dtype):
    """Test ImageData auto rescaling."""
    with pytest.warns(None):
        ImageData(numpy.zeros((1, 256, 256), dtype=dtype)).render(img_format="PNG")
        ImageData(numpy.zeros((1, 256, 256), dtype=dtype)).render(img_format="JPEG")
        ImageData(numpy.zeros((3, 256, 256), dtype=dtype)).render(img_format="WEBP")
        ImageData(numpy.zeros((3, 256, 256), dtype=dtype)).render(
            img_format="JP2OPENJPEG"
        )


def test_16bit_PNG():
    """Uint16 Mask value should be between 0 and 65535 for PNG."""
    mask = numpy.zeros((256, 256), dtype="uint16") + 255
    mask[0:10, 0:10] = 0

    with pytest.warns(None):
        img = ImageData(numpy.zeros((1, 256, 256), dtype="uint16"), mask,).render(
            img_format="PNG"
        )

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 2
            assert src.meta["dtype"] == "uint16"
            arr = src.read(2)
            assert arr.min() == 0
            assert arr.max() == 65535

    with pytest.warns(None):
        img = ImageData(numpy.zeros((3, 256, 256), dtype="uint16"), mask,).render(
            img_format="PNG"
        )

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 4
            assert src.meta["dtype"] == "uint16"
            arr = src.read(4)
            assert arr.min() == 0
            assert arr.max() == 65535
