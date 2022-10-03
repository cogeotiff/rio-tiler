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
        assert len(w.list) == 1

    with pytest.warns(None) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint8")).render(img_format="PNG")
        assert len(w.list) == 0

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="int8")).render(img_format="PNG")

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

    # Make sure that we do not rescale uint16 data when there is a colormap
    with pytest.warns(None) as w:
        cm = {1: (0, 0, 0, 255), 1000: (255, 255, 255, 255)}
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(
            img_format="JPEG", colormap=cm
        )
        assert len(w.list) == 0


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
    mask[10:11, 10:11] = 100

    with pytest.warns(None):
        img = ImageData(
            numpy.zeros((1, 256, 256), dtype="uint16"),
            mask,
        ).render(img_format="PNG")

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 2
            assert src.meta["dtype"] == "uint16"
            arr = src.read(2)
            assert arr.min() == 0
            assert arr.max() == 65535
            assert (arr[0:10, 0:10] == 0).all()
            assert (arr[10:11, 10:11] == 25700).all()
            assert (arr[11:, 11:] == 65535).all()

    with pytest.warns(None):
        img = ImageData(
            numpy.zeros((3, 256, 256), dtype="uint16"),
            mask,
        ).render(img_format="PNG")

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 4
            assert src.meta["dtype"] == "uint16"
            arr = src.read(4)
            assert arr.min() == 0
            assert arr.max() == 65535
            assert (arr[0:10, 0:10] == 0).all()
            assert (arr[10:11, 10:11] == 25700).all()
            assert (arr[11:, 11:] == 65535).all()


def test_merge_with_diffsize():
    """Make sure we raise a warning"""
    mask = numpy.zeros((256, 256), dtype="uint16") + 255
    mask[0:10, 0:10] = 0
    mask[10:11, 10:11] = 100

    with pytest.warns(UserWarning):
        img1 = ImageData(numpy.zeros((1, 256, 256)))
        img2 = ImageData(numpy.zeros((1, 128, 128)))
        img = ImageData.create_from_list([img1, img2])

    assert img.count == 2
    assert img.width == 256
    assert img.height == 256

    with pytest.warns(None) as w:
        img1 = ImageData(numpy.zeros((1, 256, 256)))
        img2 = ImageData(numpy.zeros((1, 256, 256)))
        img = ImageData.create_from_list([img1, img2])
    assert len(w) == 0


def test_apply_expression():
    """Apply expression"""
    img = ImageData(numpy.zeros((2, 256, 256)))
    img2 = img.apply_expression("b1+b2")
    assert img.count == 2
    assert img.width == 256
    assert img.height == 256
    assert img.band_names == ["b1", "b2"]
    assert img2.count == 1
    assert img2.width == 256
    assert img2.height == 256
    assert img2.band_names == ["b1+b2"]


def test_dataset_statistics():
    """Make statistics are preserved on expression"""
    data = numpy.zeros((2, 256, 256), dtype="uint8")
    data[0, 0:10, 0:10] = 0
    data[0, 10:11, 10:11] = 100
    data[1, 0:10, 0:10] = 100
    data[1, 10:11, 10:11] = 200
    img = ImageData(data, dataset_statistics=[(0, 100), (0, 200)])

    img2 = img.apply_expression("b1+b2")
    assert img2.dataset_statistics == [(0, 300)]

    img2 = img.apply_expression("b1+b2;b1*b2;b1/b1")
    assert img2.dataset_statistics == [(0, 300), (0, 20000), (0, 1)]
    assert img2.data[0].min() == 0
    assert img2.data[0].max() == 300
    assert img2.data[1].min() == 0
    assert img2.data[1].max() == 20000
    assert img2.data[2].min() == 0
    assert img2.data[2].max() == 1
