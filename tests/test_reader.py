"""tests rio_tiler.reader"""

import os

import numpy
import pytest
import rasterio
from numpy.testing import assert_array_almost_equal
from rasterio.warp import transform_bounds

from rio_tiler import constants, reader
from rio_tiler.errors import PointOutsideBounds, TileOutsideBounds

S3_KEY = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif"
S3_KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
S3_KEY_NODATA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_nodata.tif"
S3_KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"
S3_KEY_EXTMASK = (
    "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_extmask.tif"
)

S3_LOCAL = PREFIX = os.path.join(os.path.dirname(__file__), "fixtures", "my-bucket")
S3_PATH = os.path.join(S3_LOCAL, S3_KEY)
S3_ALPHA_PATH = os.path.join(S3_LOCAL, S3_KEY_ALPHA)
S3_NODATA_PATH = os.path.join(S3_LOCAL, S3_KEY_NODATA)
S3_MASK_PATH = os.path.join(S3_LOCAL, S3_KEY_MASK)
S3_EXTMASK_PATH = os.path.join(S3_LOCAL, S3_KEY_EXTMASK)

KEY_PIX4D = "pix4d/pix4d_alpha_nodata.tif"
PIX4D_PATH = os.path.join(S3_LOCAL, KEY_PIX4D)

COG = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")
COG_SCALE = os.path.join(os.path.dirname(__file__), "fixtures", "cog_scale.tif")
COG_CMAP = os.path.join(os.path.dirname(__file__), "fixtures", "cog_cmap.tif")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_tile_read_valid():
    """Should work as expected (read landsat band)."""
    # Tile 7-43-24 - Full tile
    bounds = [
        -6574807.42497772,
        12210356.646387195,
        -6261721.357121638,
        12523442.714243278,
    ]
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(
            src_dst, bounds, 16, 16, dst_crs=constants.WEB_MERCATOR_CRS
        )
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)

    # Read bounds at full resolution
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(src_dst, bounds, dst_crs=constants.WEB_MERCATOR_CRS)
    assert arr.shape == (1, 893, 893)
    assert mask.shape == (893, 893)

    # set max_size for the returned array
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(
            src_dst, bounds, max_size=50, dst_crs=constants.WEB_MERCATOR_CRS
        )
    assert arr.shape == (1, 50, 50)
    assert mask.shape == (50, 50)

    # If max_size is bigger than actual size, there is no effect
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(
            src_dst, bounds, max_size=1000, dst_crs=constants.WEB_MERCATOR_CRS
        )
    assert arr.shape == (1, 893, 893)
    assert mask.shape == (893, 893)

    # Incompatible max_size with height and width
    with pytest.warns(UserWarning):
        with rasterio.open(COG) as src_dst:
            arr, mask = reader.part(
                src_dst,
                bounds,
                max_size=50,
                width=25,
                height=25,
                dst_crs=constants.WEB_MERCATOR_CRS,
            )
    assert arr.shape == (1, 25, 25)
    assert mask.shape == (25, 25)


def test_resampling_returns_different_results():
    """Make sure resampling works."""
    bounds = [
        -6574807.42497772,
        12210356.646387195,
        -6261721.357121638,
        12523442.714243278,
    ]
    with rasterio.open(COG) as src_dst:
        arr, _ = reader.part(
            src_dst, bounds, 16, 16, dst_crs=constants.WEB_MERCATOR_CRS
        )
        arr2, _ = reader.part(
            src_dst,
            bounds,
            16,
            16,
            dst_crs=constants.WEB_MERCATOR_CRS,
            resampling_method="bilinear",
        )
        assert not numpy.array_equal(arr, arr2)

        arr, _ = reader.part(
            src_dst, bounds, 16, 16, dst_crs=constants.WEB_MERCATOR_CRS
        )
        arr2, _ = reader.part(
            src_dst,
            bounds,
            16,
            16,
            dst_crs=constants.WEB_MERCATOR_CRS,
            reproject_method="bilinear",
        )
        assert not numpy.array_equal(arr, arr2)


def test_resampling_with_diff_padding_returns_different_results():
    """Test result is different with different padding."""
    bounds = [
        -6574807.42497772,
        12210356.646387195,
        -6261721.357121638,
        12523442.714243278,
    ]
    with rasterio.open(COG) as src_dst:
        arr, _ = reader.part(
            src_dst,
            bounds,
            32,
            32,
            nodata=0,
            dst_crs=constants.WEB_MERCATOR_CRS,
            resampling_method="bilinear",
        )
        arr2, _ = reader.part(
            src_dst,
            bounds,
            32,
            32,
            nodata=0,
            padding=10,
            dst_crs=constants.WEB_MERCATOR_CRS,
            resampling_method="bilinear",
        )

    assert not numpy.array_equal(arr, arr2)


# # This is NOT TRUE, padding affects the whole array not just the border.
# def test_tile_padding_only_effects_edge_pixels():
#     """Adding tile padding should effect edge pixels only."""
#     bounds = [
#         -6574807.42497772,
#         12210356.646387195,
#         -6261721.357121638,
#         12523442.714243278
#     ]
#     with rasterio.open(COG) as src_dst:
#         arr, _ = reader.part(src_dst, bounds, 32, 32, nodata=0)
#         arr2, _ = reader.part(src_dst, bounds, 32, 32, nodata=0, padding=2)
#     assert not np.array_equal(arr[0][0], arr2[0][0])
#     assert np.array_equal(arr[0][5:-5][5:-5], arr2[0][5:-5][5:-5])


def test_tile_read_invalidResampling():
    """Should raise an error on invalid resampling method name."""
    bounds = [
        -6574807.42497772,
        12210356.646387195,
        -6261721.357121638,
        12523442.714243278,
    ]
    with pytest.raises(KeyError):
        with rasterio.open(COG) as src_dst:
            reader.part(src_dst, bounds, 16, 16, resampling_method="jacques")


def test_tile_read_tuple_index():
    """Should work as expected"""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=(1,))
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_int_index():
    """Should work as expected."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=1)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_bgr():
    """Should work as expected (read rgb)"""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    with rasterio.open(S3_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, 16, 16, indexes=(3, 2, 1))
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)


def test_tile_read_nodata():
    """Should work as expected when forcing nodata value."""
    # Partial Tile 7-42-24
    bounds = [
        -6887893.4928338025,
        12210356.646387195,
        -6574807.424977721,
        12523442.714243278,
    ]
    tilesize = 16
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, nodata=1)
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)
    assert not mask.all()


def test_tile_read_nodata_and_alpha():
    """Should work as expected when forcing nodata value"""
    bounds = (
        13604568.04230881,
        -333876.9395496497,
        13605791.034761373,
        -332653.9470970885,
    )

    tilesize = 16
    with rasterio.open(PIX4D_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, indexes=[1, 2, 3])
    assert arr.shape == (3, 16, 16)
    assert mask.shape == (16, 16)
    assert not mask.all()


def test_tile_read_dataset_nodata():
    """Should work as expected (read rgb)"""
    # non-boundless tile covering the nodata part 22-876431-1603670
    bounds = (
        -11663535.70066358,
        4715027.644399633,
        -11663526.146035044,
        4715037.199028169,
    )
    tilesize = 16
    with rasterio.open(S3_NODATA_PATH) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize)
    assert arr.shape == (3, 16, 16)
    assert not mask.all()


def test_tile_read_not_covering_the_whole_tile():
    """Should raise an error when dataset doesn't cover more than 50% of the tile."""
    bounds = (
        -11271098.442818949,
        12210356.646387195,
        -10958012.374962866,
        12523442.714243278,
    )
    tilesize = 16
    with pytest.raises(TileOutsideBounds):
        with rasterio.open(COG) as src_dst:
            reader.part(src_dst, bounds, tilesize, tilesize, minimum_overlap=0.6)


# See https://github.com/cogeotiff/rio-tiler/issues/105#issuecomment-492268836
def test_tile_read_validMask():
    """Dataset mask should be the same as the actual mask."""
    bounds = [
        -6887893.4928338025,
        12210356.646387195,
        -6574807.424977721,
        12523442.714243278,
    ]
    tilesize = 128
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(src_dst, bounds, tilesize, tilesize, nodata=1)

    masknodata = (arr[0] != 1).astype(numpy.uint8) * 255
    numpy.testing.assert_array_equal(mask, masknodata)


def test_tile_read_crs():
    """Read tile using different target CRS and bounds CRS."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )
    tilesize = 16
    with rasterio.open(S3_PATH) as src_dst:
        # Test target CRS with input bounds in bounds_crs
        arr, mask = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            indexes=(3, 2, 1),
            dst_crs=constants.WGS84_CRS,
            bounds_crs=constants.WEB_MERCATOR_CRS,
        )
        assert arr.shape == (3, 16, 16)
        assert mask.shape == (16, 16)

        # Test target CRS with input bounds in target CRS
        bounds = (
            -104.7750663757324,
            38.95353532141203,
            -104.77489471435543,
            38.95366881479646,
        )
        arr_crs, _ = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            indexes=(3, 2, 1),
            dst_crs=constants.WGS84_CRS,
        )

        assert numpy.array_equal(arr, arr_crs)


def test_tile_read_vrt_option():
    """Should work as expected (read landsat band)."""
    bounds = [
        -6887893.4928338025,
        12210356.646387195,
        -6574807.424977721,
        12523442.714243278,
    ]
    tilesize = 16
    with rasterio.open(COG) as src_dst:
        arr, mask = reader.part(
            src_dst,
            bounds,
            tilesize,
            tilesize,
            vrt_options={"source_extra": 10, "num_threads": 10},
        )
    assert arr.shape == (1, 16, 16)
    assert mask.shape == (16, 16)


def test_point():
    """Read point values"""
    with rasterio.open(COG) as src_dst:
        pt = reader.point(
            src_dst,
            [-53.54620193828792, 73.28439084323475],
            coord_crs="epsg:4326",
            indexes=1,
            nodata=1,
        )
        assert pt.data == numpy.array([1])
        assert pt.mask == numpy.array([0])
        assert pt.band_names == ["b1"]

    with rasterio.open(COG_SCALE) as src_dst:
        pt = reader.point(src_dst, [310000, 4100000], coord_crs=src_dst.crs, indexes=1)
        assert pt.data == numpy.array([8917])
        assert pt.mask == numpy.array([255])
        assert pt.band_names == ["b1"]

        pt = reader.point(src_dst, [310000, 4100000], coord_crs=src_dst.crs)
        assert pt.data == numpy.array([8917])
        assert pt.band_names == ["b1"]

        with pytest.raises(PointOutsideBounds):
            reader.point(src_dst, [810000, 4100000], coord_crs=src_dst.crs)

    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        # Test with COG + Alpha Band
        assert reader.point(src_dst, [-104.77519499, 38.95367054]).data[0]
        assert (
            reader.point(src_dst, [-104.77519499, 38.95367054]).mask[0] == 0
        )  # Masked


def test_part_with_buffer():
    """Make sure buffer works as expected."""
    bounds = [
        -6574807.42497772,
        12210356.646387195,
        -6261721.357121638,
        12523442.714243278,
    ]
    # Read part at full resolution
    with rasterio.open(COG) as src_dst:
        img_no_buffer = reader.part(src_dst, bounds, dst_crs=constants.WEB_MERCATOR_CRS)

    x_size = img_no_buffer.width
    y_size = img_no_buffer.height

    x_res = (bounds[2] - bounds[0]) / x_size
    y_res = (bounds[3] - bounds[1]) / y_size

    nx = x_size + 4
    ny = y_size + 4

    # apply a 2 pixel buffer
    bounds_with_buffer = (
        bounds[0] - x_res * 2,
        bounds[1] - y_res * 2,
        bounds[2] + x_res * 2,
        bounds[3] + y_res * 2,
    )
    with rasterio.open(COG) as src_dst:
        img = reader.part(
            src_dst,
            bounds_with_buffer,
            height=ny,
            width=nx,
            dst_crs=constants.WEB_MERCATOR_CRS,
        )
        assert img.width == nx
        assert img.height == ny

    with rasterio.open(COG) as src_dst:
        imgb = reader.part(
            src_dst, bounds, buffer=2, dst_crs=constants.WEB_MERCATOR_CRS
        )
        assert imgb.width == nx
        assert imgb.height == ny

    assert numpy.array_equal(img.data, imgb.data)
    assert img.bounds == imgb.bounds

    # No resampling is involved. Because we read the full resolution data
    # all arrays should be equal
    numpy.array_equal(img_no_buffer.data, imgb.data[:, 2:-2, 2:-2])
    numpy.array_equal(img_no_buffer.data, img.data[:, 2:-2, 2:-2])


def test_read():
    """Test reader.read function."""
    with rasterio.open(COG) as src:
        img = reader.read(src)
        assert img.width == src.width
        assert img.height == src.height
        assert img.count == src.count
        assert img.bounds == src.bounds
        assert img.crs == src.crs

    with rasterio.open(COG) as src:
        with pytest.warns(UserWarning):
            img = reader.read(src, max_size=1000, width=100, height=100)
        assert img.width == 100
        assert img.height == 100
        assert img.count == src.count
        assert img.bounds == src.bounds
        assert img.crs == src.crs

    with rasterio.open(COG) as src:
        img = reader.read(src, width=100, height=100)
        assert img.width == 100
        assert img.height == 100
        assert img.count == src.count
        assert img.bounds == src.bounds
        assert img.crs == src.crs

    with rasterio.open(COG) as src:
        img = reader.read(src, max_size=100)
        assert max(img.width, img.height) == 100
        assert img.count == src.count
        assert img.bounds == src.bounds
        assert img.crs == src.crs

    with rasterio.open(COG) as src:
        img = reader.read(src, dst_crs="epsg:3857")
        assert not img.width == src.width
        assert not img.height == src.height
        assert img.count == src.count
        assert not img.bounds == src.bounds
        assert not img.crs == src.crs

    with rasterio.open(COG) as src:
        img = reader.read(src)
        assert img.mask.all()

    with rasterio.open(COG) as src:
        img = reader.read(src, nodata=1)
        assert not img.mask.all()

    with rasterio.open(COG) as src:
        img = reader.read(src, window=((0, 100), (0, 100)))
        assert img.width == 100
        assert img.height == 100
        assert img.count == src.count
        assert not img.bounds == src.bounds
        assert img.crs == src.crs

    # Boundless Read
    with rasterio.open(COG) as src:
        img = reader.read(src, window=((-10, 100), (-10, 100)))
        assert img.width == 110
        assert img.height == 110
        assert img.count == src.count
        assert not img.bounds == src.bounds
        assert img.crs == src.crs

    with rasterio.open(COG) as src:
        img = reader.read(src, window=((0, 4000), (0, 4000)))
        assert img.width == 4000
        assert img.height == 4000
        assert img.count == src.count
        assert not img.bounds == src.bounds
        assert img.crs == src.crs

    # Can't use boundless window with WarpedVRT
    with rasterio.open(COG) as src:
        with pytest.raises(ValueError):
            reader.read(src, window=((0, 4000), (0, 4000)), dst_crs="epsg:3857")

    # Unscale Dataset
    with rasterio.open(COG_SCALE) as src:
        assert not src.dtypes[0] == numpy.float32
        img = reader.read(src, unscale=True)
        assert img.data.dtype == numpy.float32

    # Dataset with Alpha using WarpedVRT
    with rasterio.open(S3_ALPHA_PATH) as src:
        img = reader.read(src, dst_crs="epsg:3857")
        assert not img.mask.all()


def test_part_no_VRT():
    """Test reader.part function without VRT."""
    bounds = [
        -56.6015625,
        73.0001215118412,
        -51.67968749999999,
        74.23886253330774,
    ]  # boundless part
    # Read part at full resolution
    with rasterio.open(COG) as src_dst:

        bounds_dst_crs = transform_bounds(
            "epsg:4326", src_dst.crs, *bounds, densify_pts=21
        )

        img = reader.part(src_dst, bounds, bounds_crs="epsg:4326")
        assert img.height == 1453
        assert img.width == 1613
        assert img.mask[0, 0] == 255
        assert img.mask[-1, -1] == 0  # boundless
        assert img.bounds == bounds_dst_crs

        # Use bbox in Image CRS
        img_crs = reader.part(src_dst, bounds_dst_crs)
        assert img.height == 1453
        assert img.width == 1613
        assert img_crs.mask[0, 0] == 255
        assert img_crs.mask[-1, -1] == 0  # boundless
        assert img.bounds == bounds_dst_crs

        # MaxSize
        img = reader.part(src_dst, bounds, bounds_crs="epsg:4326", max_size=1024)
        assert img.height < 1024
        assert img.width == 1024
        assert img.mask[0, 0] == 255
        assert img.mask[-1, -1] == 0  # boundless
        assert img.bounds == bounds_dst_crs

        # Width/Height
        img = reader.part(
            src_dst,
            bounds,
            bounds_crs="epsg:4326",
            width=100,
            height=100,
        )
        assert img.height == 100
        assert img.width == 100
        assert img.mask[0, 0] == 255
        assert img.mask[-1, -1] == 0  # boundless
        assert img.bounds == bounds_dst_crs

        # Buffer
        img = reader.part(src_dst, bounds, bounds_crs="epsg:4326", buffer=1)
        assert img.height == 1455
        assert img.width == 1615
        assert img.mask[0, 0] == 255
        assert img.mask[-1, -1] == 0  # boundless
        assert not img.bounds == bounds_dst_crs

        # Padding
        img = reader.part(src_dst, bounds, bounds_crs="epsg:4326")
        img_pad = reader.part(src_dst, bounds, bounds_crs="epsg:4326", padding=1)
        assert img_pad.height == 1453
        assert img_pad.width == 1613
        assert img_pad.mask[0, 0] == 255
        assert img_pad.mask[-1, -1] == 0  # boundless
        assert img_pad.bounds == bounds_dst_crs
        # Padding should not have any influence when not doing any rescaling/reprojection
        numpy.array_equal(img_pad.data, img.data)

        # Read bbox smaller than one pixel
        bounds_small = [bounds[0], bounds[1], bounds[0] + 1e-6, bounds[1] + 1e-6]
        bounds_small_dst_crs = transform_bounds("epsg:4326", src_dst.crs, *bounds_small)
        img_small = reader.part(src_dst, bounds_small, bounds_crs="epsg:4326")
        assert img_small.height == 1
        assert img_small.width == 1
        assert_array_almost_equal(img_small.bounds, bounds_small_dst_crs)
