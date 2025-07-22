"""Test rio_tiler.models."""

import warnings
from io import BytesIO

import numpy
import pytest
import rasterio
from rasterio.crs import CRS
from rasterio.errors import NotGeoreferencedWarning
from rasterio.io import MemoryFile

from rio_tiler.errors import (
    InvalidDatatypeWarning,
    InvalidFormat,
    InvalidPointDataError,
)
from rio_tiler.models import ImageData, PointData


def test_imageData_AutoRescaling():
    """Test ImageData auto rescaling."""
    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="float32")).render(img_format="PNG")
        assert len(w.list) == 1

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        ImageData(numpy.zeros((1, 256, 256), dtype="uint8")).render(img_format="PNG")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="int8")).render(img_format="PNG")

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(img_format="GTiff")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(img_format="jpeg")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((3, 256, 256), dtype="uint16")).render(img_format="WEBP")

    with pytest.warns(InvalidDatatypeWarning) as w:
        ImageData(numpy.zeros((3, 256, 256), dtype="int8")).render(
            img_format="JP2OpenJPEG"
        )

    # Make sure that we do not rescale uint16 data when there is a colormap
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        cm = {1: (0, 0, 0, 255), 1000: (255, 255, 255, 255)}
        ImageData(numpy.zeros((1, 256, 256), dtype="uint16")).render(
            img_format="JPEG", colormap=cm
        )


@pytest.mark.parametrize(
    "dtype",
    ["uint8", "int8", "uint16", "int16", "uint32", "int32", "float32", "float64"],
)
def test_imageData_AutoRescalingAllTypes(dtype):
    """Test ImageData auto rescaling."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # Some InvalidDatatypeWarning will be emitted
        ImageData(numpy.zeros((1, 256, 256), dtype=dtype)).render(img_format="PNG")
        ImageData(numpy.zeros((1, 256, 256), dtype=dtype)).render(img_format="JPEG")
        ImageData(numpy.zeros((3, 256, 256), dtype=dtype)).render(img_format="WEBP")
        ImageData(numpy.zeros((3, 256, 256), dtype=dtype)).render(
            img_format="JP2OPENJPEG"
        )


def test_16bit_PNG():
    """Uint16 Mask value should be between 0 and 65535 for PNG."""
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:10, 0:10] = True

    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
        arr = numpy.ma.MaskedArray(numpy.zeros((1, 256, 256), dtype="uint16"))
        arr.mask = mask.copy()
        img = ImageData(arr).render(img_format="PNG")

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 2
            assert src.meta["dtype"] == "uint16"
            arr = src.read(2)
            assert arr.min() == 0
            assert arr.max() == 65535
            assert (arr[0:10, 0:10] == 0).all()
            assert (arr[11:, 11:] == 65535).all()

    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
        arr = numpy.ma.MaskedArray(numpy.zeros((3, 256, 256), dtype="uint16"))
        arr.mask = mask.copy()
        img = ImageData(arr).render(img_format="PNG")

        with rasterio.open(BytesIO(img)) as src:
            assert src.count == 4
            assert src.meta["dtype"] == "uint16"
            arr = src.read(4)
            assert arr.min() == 0
            assert arr.max() == 65535
            assert (arr[0:10, 0:10] == 0).all()
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

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        img1 = ImageData(numpy.zeros((1, 256, 256)))
        img2 = ImageData(numpy.zeros((1, 256, 256)))
        img = ImageData.create_from_list([img1, img2])


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

    data = numpy.zeros((1, 256, 256), dtype="int16")
    data[0, 0:10, 0:10] = 0
    data[0, 10:11, 10:11] = 1

    with pytest.warns(InvalidDatatypeWarning):
        img = ImageData(data, dataset_statistics=[(0, 1)]).render(img_format="PNG")
        with MemoryFile(img) as mem:
            with mem.open() as dst:
                arr = dst.read(indexes=1)
                assert arr.min() == 0
                assert arr.max() == 255

    with pytest.warns(InvalidDatatypeWarning):
        img = ImageData(data).render(img_format="PNG")

        with MemoryFile(img) as mem:
            with mem.open() as dst:
                arr = dst.read(indexes=1)
                assert not arr.min() == 0
                assert not arr.max() == 255


def test_resize():
    """Resize ImageData and check original image"""
    data = numpy.zeros((3, 1024, 1024), dtype="uint8")
    img = ImageData(data)

    img_r = img.resize(256, 256)
    assert img_r.count == 3
    assert img_r.width == 256
    assert img_r.height == 256
    assert img.width == 1024
    assert img.height == 1024
    assert img_r.mask.shape == (256, 256)
    assert img.mask.shape == (1024, 1024)


def test_clip():
    """Resize ImageData and check original image"""
    data = numpy.zeros((3, 1024, 1024), dtype="int16")
    data[:, :, :] = 32767
    img = ImageData(data, crs="epsg:4326", bounds=(-180, -90, 180, 90))

    img_c = img.clip((-100, -50, 100, 50))
    assert img_c.count == 3
    assert img_c.bounds == (-100, -50, 100, 50)

    img.rescale(((0, 32767),))
    assert img.width == 1024
    assert img.height == 1024
    assert img.mask.shape == (1024, 1024)
    assert img.array.dtype == "uint8"

    # make sure the clipped image didn't change
    assert img_c.array.dtype == "int16"


def test_point_data():
    """Test Point Data Model."""
    pt = PointData(numpy.zeros((3), dtype="uint16"))
    assert pt.count == 3
    assert pt.data.shape == (3,)
    assert pt.mask.shape == (1,)
    assert pt._mask.tolist() == [True]
    assert pt.band_names == ["b1", "b2", "b3"]

    with pytest.raises(ValueError):
        PointData(numpy.zeros((3, 3)))

    with pytest.raises(ValueError):
        PointData(numpy.zeros((3), dtype="uint16"), coordinates=(0,))

    for p in PointData(numpy.zeros((3), dtype="uint16")):
        assert p == 0

    pt1 = PointData(numpy.array([1, 2]))
    pt2 = pt1.apply_expression("b1+b2")
    assert pt1.count == 2
    assert pt1.band_names == ["b1", "b2"]
    assert pt2.count == 1
    assert pt2.band_names == ["b1+b2"]

    pts = PointData.create_from_list([pt1, pt2])
    assert pts.data.tolist() == [1, 2, 3]
    assert pts.band_names == ["b1", "b2", "b1+b2"]
    assert pts._mask.tolist() == [True]

    pts = PointData.create_from_list(
        [
            PointData(numpy.ma.MaskedArray([1], [0])),
            PointData(numpy.ma.MaskedArray([1], [1])),
        ]
    )
    assert pts.array.mask.tolist() == [False, True]
    assert pts._mask.tolist() == [False]

    pts = PointData.create_from_list(
        [
            PointData(numpy.ma.MaskedArray([1], [0])),
            PointData(numpy.ma.MaskedArray([1], [0])),
        ]
    )
    assert pts.array.mask.tolist() == [False, False]
    assert pts._mask.tolist() == [True]

    pts = PointData.create_from_list(
        [
            PointData(numpy.ma.MaskedArray([1], [1])),
            PointData(numpy.ma.MaskedArray([1], [1])),
        ]
    )
    assert pts.array.mask.tolist() == [True, True]
    assert pts._mask.tolist() == [False]

    with pytest.raises(InvalidPointDataError):
        PointData.create_from_list([])

    with pytest.raises(InvalidPointDataError):
        PointData.create_from_list(
            [
                PointData(numpy.ma.MaskedArray([1]), coordinates=(0, 0)),
                PointData(numpy.ma.MaskedArray([1]), coordinates=(0, 1)),
            ]
        )

    with pytest.raises(InvalidPointDataError):
        PointData.create_from_list(
            [
                PointData(
                    numpy.ma.MaskedArray([1]),
                    coordinates=(0, 0),
                    crs=CRS.from_epsg(3857),
                ),
                PointData(
                    numpy.ma.MaskedArray([1]),
                    coordinates=(0, 0),
                    crs=CRS.from_epsg(4326),
                ),
            ]
        )


def test_image_apply_colormap():
    """Apply colormap to the data."""
    cm = {0: (0, 0, 0, 255), 1: (255, 255, 255, 255)}
    im = ImageData(numpy.zeros((1, 256, 256), dtype="uint8")).apply_colormap(cm)
    assert im.data.shape == (3, 256, 256)
    assert im.data[:, 0, 0].tolist() == [0, 0, 0]
    assert im.mask[0, 0] == 255
    assert im._mask.all()

    cm = {0: (0, 0, 0, 255), 1: (255, 255, 255, 255)}
    data = numpy.zeros((1, 256, 256), dtype="uint8") + 1
    data[0, 0, 0] = 0

    im = ImageData(data)
    assert im.array.data.shape == (1, 256, 256)
    assert im.array.mask.shape == (1, 256, 256)

    im = im.apply_colormap(cm)
    # data[0, 1, 1] is 1 so after colormap it should be 255,255,255 and mask should be 255
    assert im.data[:, 1, 1].tolist() == [255, 255, 255]
    assert im.array.data.shape == (3, 256, 256)
    assert im.array.mask.shape == (3, 256, 256)
    assert im.mask[1, 1] == 255

    # data[0, 0, 0] is 0 so after colormap it should be 0,0,0 and mask should be 255 (based on the colormap Alpha value)
    assert im.data[:, 0, 0].tolist() == [0, 0, 0]
    assert im.mask[0, 0] == 255

    # Case 1
    # both input data has masked values
    cm = {0: (0, 0, 0, 255), 1: (255, 255, 255, 255)}
    arr = numpy.zeros((1, 256, 256), dtype="uint8") + 1
    arr[0, 0, 0] = 0

    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0, 0, 0] = True

    im = ImageData(numpy.ma.MaskedArray(arr, mask=mask)).apply_colormap(cm)
    assert im.data[:, 0, 0].tolist() == [0, 0, 0]
    assert im.array.mask[:, 1, 1].tolist() == [False, False, False]
    assert im.mask[1, 1] == 255

    assert im.array.mask[:, 0, 0].tolist() == [True, True, True]
    assert im.mask[0, 0] == 0

    # Case 2
    # both input data and colormaped data has masked values
    cm = {0: (255, 255, 255, 0), 1: (255, 255, 255, 255)}
    arr = numpy.zeros((1, 256, 256), dtype="uint8") + 1
    arr[0, 0, 0] = 0

    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0, 0, 0] = True
    im = ImageData(numpy.ma.MaskedArray(arr, mask=mask)).apply_colormap(cm)
    assert im.data[:, 0, 0].tolist() == [255, 255, 255]
    assert im.array.mask[:, 0, 0].tolist() == [True, True, True]
    assert im.mask[0, 0] == 0

    assert im.array.mask[:, 1, 1].tolist() == [False, False, False]
    assert im.mask[1, 1] == 255

    # Case 3
    # colormaped data has masked values
    cm = {0: (255, 255, 255, 0), 1: (255, 255, 255, 255)}
    arr = numpy.zeros((1, 256, 256), dtype="uint8") + 1
    arr[0, 0, 0] = 0

    mask = numpy.zeros((1, 256, 256), dtype="bool")
    im = ImageData(numpy.ma.MaskedArray(arr, mask=mask)).apply_colormap(cm)
    assert im.data[:, 0, 0].tolist() == [255, 255, 255]
    assert im.array.mask[:, 0, 0].tolist() == [True, True, True]
    assert im.mask[0, 0] == 0

    assert im.array.mask[:, 1, 1].tolist() == [False, False, False]
    assert im.mask[1, 1] == 255


def test_image_apply_colormap_partial():
    """Apply colormap with partial transparency."""
    cm = {
        0: (255, 255, 255, 0),  # masked
        1: (255, 255, 255, 50),  # partially masked
        2: (255, 255, 255, 255),  # not masked
    }

    arr = numpy.zeros((1, 256, 256), dtype="uint8") + 2
    arr[0, 1, 1] = 1
    arr[0, 0, 0] = 0

    # Full Valid data
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    im = ImageData(numpy.ma.MaskedArray(arr, mask=mask)).apply_colormap(cm)
    assert im.data[:, 0, 0].tolist() == [255, 255, 255]
    assert im.array.mask[:, 0, 0].tolist() == [True, True, True]
    assert im.mask[0, 0] == 0

    # Partial transparency is considered as a `masked` value
    assert im.array.mask[:, 1, 1].tolist() == [True, True, True]
    # But mask has partial alpha value
    assert im.mask[1, 1] == 50

    assert im.array.mask[:, 2, 2].tolist() == [False, False, False]
    assert im.mask[2, 2] == 255


def test_image_from_bytes():
    """Create ImageData from bytes."""
    im = ImageData(numpy.zeros((1, 256, 256), dtype="uint8"))
    assert im.data.shape == (1, 256, 256)

    im_r = ImageData.from_bytes(im.render(img_format="PNG", add_mask=True))
    assert im_r.data.shape == (1, 256, 256)
    assert im._mask.all()

    data = numpy.zeros((1, 256, 256), dtype="uint8")
    data[0:100, 0:100] = 1
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:10, 0:10] = True
    img = ImageData(numpy.ma.MaskedArray(data, mask=mask))

    im = ImageData.from_bytes(img.render(img_format="PNG", add_mask=True))
    assert im.data.shape == (1, 256, 256)
    assert not im._mask.all()

    im = ImageData.from_bytes(img.render(img_format="PNG", add_mask=False))
    assert im.data.shape == (1, 256, 256)
    assert im._mask.all()

    im = ImageData.from_bytes(img.render(img_format="JPEG", add_mask=False))
    assert im.data.shape == (1, 256, 256)
    assert im._mask.all()


def test_2d_image():
    """Create Image Data from 2d array."""
    data = numpy.zeros((256, 256))
    im = ImageData(data)
    assert im.count == 1
    assert im.width == 256
    assert im.height == 256
    assert im._mask.all()


def test_apply_color_formula():
    """Test Apply color_formula."""
    data = numpy.random.randint(0, 16000, (3, 256, 256)).astype("uint16")
    img = ImageData(data)
    assert img.data.dtype == "uint16"

    img.apply_color_formula(
        "gamma b 1.85, gamma rg 1.95, sigmoidal rgb 35 0.13, saturation 1.15"
    )
    assert img.data.dtype == "uint8"
    assert img.count == 3
    assert img.width == 256
    assert img.height == 256


def test_imagedata_coverage():
    """test coverage array."""
    im = ImageData(
        numpy.ma.array((1, 2, 3, 4)).reshape((1, 2, 2)),
        crs="epsg:4326",
        bounds=(-180, -90, 180, 90),
    )
    poly = {
        "type": "Polygon",
        "coordinates": [
            [[-90.0, -45.0], [90.0, -45.0], [90.0, 45.0], [-90.0, 45.0], [-90.0, -45.0]]
        ],
    }
    coverage = im.get_coverage_array(poly)
    assert numpy.unique(coverage).tolist() == [0.25]

    coverage = im.get_coverage_array({"type": "Feature", "geometry": poly})
    assert numpy.unique(coverage).tolist() == [0.25]

    # non-default CRS
    poly = {
        "type": "Polygon",
        "coordinates": [
            [
                (-10018754.171394622, -5621521.486192066),
                (10018754.171394622, -5621521.486192066),
                (10018754.171394622, 5621521.486192066),
                (-10018754.171394622, 5621521.486192066),
                (-10018754.171394622, -5621521.486192066),
            ]
        ],
    }

    coverage = im.get_coverage_array(poly, shape_crs="epsg:3857")
    assert numpy.unique(coverage).tolist() == [0.25]

    coverage = im.get_coverage_array(
        {"type": "Feature", "geometry": poly}, shape_crs="epsg:3857"
    )
    assert numpy.unique(coverage).tolist() == [0.25]

    # polygon with diagonal cut - requires higher cover_scale
    im = ImageData(
        numpy.ma.array((1, 2, 3, 4)).reshape((1, 2, 2)),
        crs="epsg:4326",
        bounds=(-180, -90, 180, 90),
    )
    poly = {
        "type": "Polygon",
        "coordinates": [[[-90.0, -45.0], [90.0, -45.0], [-90.0, 45.0], [-90.0, -45.0]]],
    }

    coverage = im.get_coverage_array(poly, cover_scale=1000)
    assert numpy.round(numpy.unique(coverage), decimals=3).tolist() == [0, 0.125, 0.25]


def test_image_encoding_error():
    """Test ImageData error when using bad data array shape."""
    with pytest.raises(InvalidFormat):
        ImageData(numpy.zeros((5, 256, 256), dtype="uint8")).render(img_format="PNG")


def test_image_reproject():
    """Test basic reproject functionality."""
    data = numpy.zeros((1, 256, 256), dtype="uint8")
    data[0:256, 0:256] = 1
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:100, 0:100] = True

    # Create test image with WGS84 CRS
    src_crs = CRS.from_epsg(4326)
    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
        crs=src_crs,
        bounds=(-95, 43, -92, 45),
        metadata={"test": "value"},
        band_names=["band1"],
    )

    # Test re-projection to Web Mercator
    dst_crs = CRS.from_epsg(3857)

    reprojected = img.reproject(dst_crs)
    assert reprojected.crs == dst_crs
    assert reprojected.count == 1
    assert reprojected.width != 256
    assert reprojected.height != 256
    assert reprojected.array[0, 0, 0].data == 0
    assert reprojected.array.data[0, -10, -10] == 1
    assert reprojected.array.mask.shape[0] == 1
    assert reprojected.array.mask[0, 0, 0]
    assert not reprojected.array.mask[0, -10, -10]
    assert reprojected.metadata == img.metadata
    assert reprojected.band_names == img.band_names

    # Test no re-projection when CRS is the same
    same_crs = img.reproject(src_crs)
    assert same_crs.crs == src_crs
    assert same_crs.transform == img.transform
    numpy.testing.assert_array_equal(same_crs.array, img.array)

    # Test with different resampling method
    reprojected_bilinear = img.reproject(dst_crs, reproject_method="bilinear")
    with numpy.testing.assert_raises(AssertionError):
        numpy.testing.assert_array_equal(reprojected_bilinear.array, img.array)

    # With MultiBands
    data = numpy.zeros((3, 256, 256), dtype="uint8")
    data[:, 0:256, 0:256] = 1
    mask = numpy.zeros((3, 256, 256), dtype="bool")
    mask[:, 0:100, 0:100] = True

    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
        crs=src_crs,
        bounds=(-95, 43, -92, 45),
    )

    reprojected = img.reproject(dst_crs)
    assert reprojected.crs == dst_crs
    assert reprojected.count == 3
    assert reprojected.width != 256
    assert reprojected.height != 256
    assert reprojected.array.data[:, 0, 0].tolist() == [0, 0, 0]
    assert reprojected.array.data[:, -10, -10].tolist() == [1, 1, 1]
    assert reprojected.array.mask.shape[0] == 3
    assert reprojected.array.mask[:, 0, 0].tolist() == [True, True, True]
    assert reprojected.array.mask[:, -10, -10].tolist() == [False, False, False]


def test_imageData_to_raster(tmp_path):
    """Test ImageData to raster"""
    ImageData(numpy.zeros((1, 256, 256), dtype="float32")).to_raster(tmp_path / "img.tif")
    with rasterio.open(tmp_path / "img.tif") as src:
        assert src.count == 2
        assert src.profile["driver"] == "GTiff"

    ImageData(numpy.zeros((1, 256, 256), dtype="float32")).to_raster(
        tmp_path / "img.tif", driver="GTiff"
    )
    with rasterio.open(tmp_path / "img.tif") as src:
        assert src.count == 2
        assert src.profile["driver"] == "GTiff"

    # case insensitive GTiff
    ImageData(numpy.zeros((1, 256, 256), dtype="float32")).to_raster(
        tmp_path / "img.tif", driver="gtiff"
    )
    with rasterio.open(tmp_path / "img.tif") as src:
        assert src.count == 2
        assert src.profile["driver"] == "GTiff"

    ImageData(numpy.zeros((1, 256, 256), dtype="float32")).to_raster(
        tmp_path / "img.tif", driver="GTiff", nodata=0
    )
    with rasterio.open(tmp_path / "img.tif") as src:
        assert src.count == 1
        assert src.profile["driver"] == "GTiff"
        assert src.profile["nodata"] == 0

    ImageData(numpy.zeros((3, 256, 256), dtype="uint8")).to_raster(
        tmp_path / "img.tif", driver="PNG"
    )
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
        with rasterio.open(tmp_path / "img.tif") as src:
            assert src.count == 4
            assert src.profile["driver"] == "PNG"


def test_image_post_process():
    """Test post_process functionality."""
    data = numpy.zeros((3, 256, 256), dtype="int16")
    data[:, 100:256, 100:256] = 32767
    mask = numpy.zeros((3, 256, 256), dtype="bool")
    mask[0:50, 0:50] = True

    cf = "gamma b 1.85, gamma rg 1.95, sigmoidal rgb 35 0.13, saturation 1.15"

    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
    )
    img_p = img.post_process(color_formula=cf)
    assert img_p.array.dtype == "uint8"
    assert img.array.dtype == "int16"

    img_p = img.post_process(in_range=((0, 32767),))
    assert img_p.array.dtype == "uint8"
    assert img.array.dtype == "int16"


def test_image_rescale():
    """Test basic rescale functionality."""
    data = numpy.zeros((1, 256, 256), dtype="int16")
    data[:, 100:256, 100:256] = 32767
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:50, 0:50] = True

    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
    )
    img.rescale(((0, 32767),))
    assert img.array[0, 255, 255] == 255
    assert img.array[0, 60, 60] == 0


def test_mask_values():
    """test mask values."""
    data = numpy.zeros((1, 256, 256), dtype="int16")
    data[:, 100:256, 100:256] = 32767
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:50, 0:50] = True
    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
    )
    assert img.mask[0, 0] == -32768
    assert img.mask[255, 255] == 32767
    with pytest.warns(InvalidDatatypeWarning) as w:
        img.render(img_format="PNG")
        assert len(w.list) == 1

    data = numpy.zeros((1, 256, 256), dtype="uint16")
    data[:, 100:256, 100:256] = 65535
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0:50, 0:50] = True
    img = ImageData(
        numpy.ma.MaskedArray(data=data, mask=mask),
    )
    assert img.mask[0, 0] == 0
    assert img.mask[255, 255] == 65535
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        img.render(img_format="PNG")


def test_alpha_band():
    """Test ImageData with Alpha Band"""
    arr = numpy.zeros((1, 256, 256), dtype="uint8")
    arr[0, 50:100, :] = 50
    arr[0, 100:150, :] = 100
    arr[0, 150:200, :] = 150
    arr[0, 200:, :] = 200

    # Full Valid data
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0, 0:100, 0:100] = True

    data = numpy.ma.MaskedArray(arr, mask=mask)

    # Invalid shape
    with pytest.raises(ValueError):
        ImageData(
            data,
            alpha_mask=numpy.zeros((512, 512), dtype="uint8"),
        )

    # Invalid Datatype
    with pytest.raises(ValueError):
        ImageData(
            data,
            alpha_mask=numpy.zeros((256, 256), dtype="uint16"),
        )

    # Alpha mask with partial transparency
    alpha = numpy.zeros((256, 256), dtype="uint8") + 255
    alpha[0:100, 0:100] = 0
    alpha[0:50, 0:50] = 150  # Partial transparency

    im = ImageData(data, alpha_mask=alpha, bounds=(-180, -90, 180, 90))
    numpy.testing.assert_array_equal(im.mask, im.alpha_mask)

    imr = im.resize(100, 100)
    assert imr.alpha_mask.shape == (100, 100)

    imr = im.clip((0, 0, 180, 90))
    assert imr.array.shape == (1, 128, 128)
    assert imr.alpha_mask.shape == (128, 128)

    # ColorFormula/Rescale
    data = numpy.random.randint(0, 16000, (3, 256, 256)).astype("uint16")
    alpha = numpy.zeros((256, 256), dtype="uint16") + 65535
    alpha[0:100, 0:100] = 30000  # Partial transparency
    alpha[0:50, 0:50] = 0
    im = ImageData(data, alpha_mask=alpha)
    imp = im.post_process(
        color_formula="gamma b 1.85, gamma rg 1.95, sigmoidal rgb 35 0.13, saturation 1.15"
    )
    assert imp.alpha_mask.dtype == "uint8"
    assert imp.alpha_mask[0, 0] == 0
    assert imp.alpha_mask[50, 50] == 116
    assert imp.alpha_mask[100, 100] == 255

    imp = im.post_process(in_range=((0, 30000),))
    assert imp.alpha_mask.dtype == "uint8"
    assert imp.alpha_mask[0, 0] == 0
    assert imp.alpha_mask[50, 50] == 116
    assert imp.alpha_mask[100, 100] == 255

    # ColorMap
    cm = {
        0: (255, 255, 255, 0),  # transparent
        50: (255, 0, 255, 50),  # partially transparent
        100: (255, 255, 0, 255),  # not transparent
        150: (255, 0, 0, 255),  # not transparent
        200: (0, 255, 255, 255),  # not transparent
    }
    arr = numpy.zeros((1, 256, 256), dtype="uint8") + 200
    arr[0, 0:50, :] = 0
    arr[0, 50:100, :] = 50
    arr[0, 100:150, :] = 100
    arr[0, 150:200, :] = 150
    mask = numpy.zeros((1, 256, 256), dtype="bool")
    mask[0, 0:10, 0:10] = True
    data = numpy.ma.MaskedArray(arr, mask=mask)
    alpha = numpy.zeros((256, 256), dtype="uint8")
    im = ImageData(data, alpha_mask=alpha)

    # alpha will be ignored when applying colormap
    with pytest.warns(UserWarning):
        im_colormaped = im.apply_colormap(cm)

    # make sure array is still masked
    assert im_colormaped.array.mask[0, 0, 0]
    assert im_colormaped.mask[0, 0] == 0

    # full transparency from alpha result in masked value
    assert im_colormaped.array.mask[0, 20, 20]
    # full transparency from alpha
    assert im_colormaped.mask[20, 20] == 0

    # partial transparency from alpha result in masked value
    assert im_colormaped.array.mask[0, 50, 20]
    # partial transparency from alpha
    assert im_colormaped.mask[50, 20] == 50

    # no transparency
    assert not im_colormaped.array.mask[0, 100, 20]
    assert im_colormaped.mask[100, 20] == 255
