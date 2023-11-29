"""tests rio_tiler.utils"""

import math
import os
import warnings
from io import BytesIO

import numpy as np
import pytest
import rasterio
from rasterio.crs import CRS
from rasterio.enums import ColorInterp
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.io import MemoryFile

from rio_tiler import colormap, utils
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import RioTilerError
from rio_tiler.expression import parse_expression
from rio_tiler.io import Reader

from .conftest import requires_webp

S3_KEY = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1.tif"
S3_KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
S3_KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"

S3_LOCAL = PREFIX = os.path.join(os.path.dirname(__file__), "fixtures", "my-bucket")
S3_PATH = os.path.join(S3_LOCAL, S3_KEY)
S3_ALPHA_PATH = os.path.join(S3_LOCAL, S3_KEY_ALPHA)
S3_MASK_PATH = os.path.join(S3_LOCAL, S3_KEY_MASK)

KEY_PIX4D = "pix4d/pix4d_alpha_nodata.tif"
PIX4D_PATH = os.path.join(S3_LOCAL, KEY_PIX4D)

COG_DST = os.path.join(os.path.dirname(__file__), "fixtures", "cog_name.tif")
COG_WEB_TILED = os.path.join(os.path.dirname(__file__), "fixtures", "web.tif")
COG_NOWEB = os.path.join(os.path.dirname(__file__), "fixtures", "noweb.tif")
COG_RGB = os.path.join(os.path.dirname(__file__), "fixtures", "cog_rgb.tif")
NOCOG = os.path.join(os.path.dirname(__file__), "fixtures", "nocog.tif")
COGEO = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")
COG_CMAP = os.path.join(os.path.dirname(__file__), "fixtures", "cog_cmap.tif")
COG_NAN = os.path.join(os.path.dirname(__file__), "fixtures", "cog_nodata_nan.tif")


@pytest.fixture(autouse=True)
def testing_env_var(monkeypatch):
    """Set fake env to make sure we don't hit AWS services."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "jqt")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "rde")
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    monkeypatch.setenv("AWS_CONFIG_FILE", "/tmp/noconfigheere")
    monkeypatch.setenv("AWS_SHARED_CREDENTIALS_FILE", "/tmp/noconfighereeither")
    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "EMPTY_DIR")


def test_linear_rescale_valid():
    """Should work as expected (read data band)."""
    data = np.zeros((1, 1), dtype=np.int16) + 1000
    expected_value = np.zeros((1, 1), dtype=np.int16) + 25.5
    assert (
        utils.linear_rescale(data, in_range=(0, 10000), out_range=(0, 255))
        == expected_value
    )


def test_mapzen_elevation_rgb():
    """Should work as expected."""
    arr = np.random.randint(0, 3000, size=(512, 512))
    assert utils.mapzen_elevation_rgb(arr).shape == (3, 512, 512)


def test_get_vrt_transform_valid():
    """Should return correct transform and size."""
    bounds = (
        -11663507.036777973,
        4715018.0897710975,
        -11663487.927520901,
        4715037.199028169,
    )

    with rasterio.open(S3_PATH) as src:
        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, 64, 64
        )
        assert vrt_transform[2] == -11663507.036777973
        assert vrt_transform[5] == 4715037.199028169
        assert vrt_width == 99
        assert vrt_height == 99

        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, 256, 256
        )
        assert vrt_transform[2] == -11663507.036777973
        assert vrt_transform[5] == 4715037.199028169
        assert vrt_width == 256
        assert vrt_height == 256


def test_get_vrt_transform_valid4326():
    """Should return correct transform and size."""
    bounds = (
        -104.77523803710938,
        38.95353532141205,
        -104.77455139160156,
        38.954069293441066,
    )
    with rasterio.open(S3_PATH) as src:
        vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
            src, bounds, 256, 256, dst_crs=WGS84_CRS
        )

    assert vrt_transform[2] == -104.77523803710938
    assert vrt_transform[5] == 38.954069293441066
    assert vrt_width == 420
    assert vrt_height == 326


def test_render_valid_1band():
    """Creates PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(512, 512), dtype=np.uint8)
    assert utils.render(arr)


def test_render_valid_colormap():
    """Creates 'colormaped' PNG image buffer from one band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)
    cmap = colormap.cmap.get("cfastie")
    assert utils.render(arr, mask, colormap=cmap, img_format="jpeg")


def test_render_valid_colormapDict():
    """Create 'colormaped' PNG image buffer from one band array using discrete cmap."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    cmap = {
        1: (255, 255, 255, 255),
        50: (255, 255, 0, 255),
        100: (255, 0, 0, 255),
        150: (0, 0, 255, 255),
    }
    assert utils.render(arr, colormap=cmap)


def test_render_valid_mask():
    """Creates image buffer from 3 bands array and mask."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)
    assert utils.render(arr, mask=mask)
    assert utils.render(arr, mask=mask, img_format="jpeg")


def test_render_valid_options():
    """Creates image buffer with driver options."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8) + 255
    assert utils.render(arr, mask=mask, img_format="png", ZLEVEL=9)


@requires_webp
def test_render_valid_1bandWebp():
    """Creates WEBP image buffer from 1 band array."""
    arr = np.random.randint(0, 255, size=(1, 512, 512), dtype=np.uint8)
    assert utils.render(arr, img_format="WEBP")


def test_aligned_with_internaltile():
    """Check if COG is in WebMercator and aligned with internal tiles."""
    bounds = WEB_MERCATOR_TMS.bounds(43, 25, 7)
    with rasterio.open(COG_DST) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(src_dst, bounds)

    with rasterio.open(NOCOG) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(src_dst, bounds)

    bounds = WEB_MERCATOR_TMS.bounds(147, 182, 9)
    with rasterio.open(COG_NOWEB) as src_dst:
        assert not utils._requested_tile_aligned_with_internal_tile(src_dst, bounds)

    with rasterio.open(COG_WEB_TILED) as src_dst:
        assert utils._requested_tile_aligned_with_internal_tile(src_dst, bounds)


def test_find_non_alpha():
    """Return valid indexes."""
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)

    with rasterio.open(PIX4D_PATH) as src_dst:
        assert utils.non_alpha_indexes(src_dst) == (1, 2, 3)


def test_has_alpha():
    """Check if rasters have alpha bands."""
    with rasterio.open(S3_ALPHA_PATH) as src_dst:
        assert utils.has_alpha_band(src_dst)
        assert not utils.has_mask_band(src_dst)

    with rasterio.open(COG_DST) as src_dst:
        assert not utils.has_alpha_band(src_dst)


def test_has_mask():
    """Should return True."""
    with rasterio.open(S3_MASK_PATH) as src_dst:
        assert utils.has_mask_band(src_dst)
        assert not utils.has_alpha_band(src_dst)

    with rasterio.open(COG_DST) as src_dst:
        assert not utils.has_mask_band(src_dst)


def test_chunck():
    """Should split a list in multiple chunks."""
    chuncks = list(utils._chunks(list(range(10)), 3))
    assert len(chuncks) == 4


def test_div():
    """Should return up rounded value."""
    assert utils._div_round_up(3, 2) == 2
    assert utils._div_round_up(2, 2) == 1


def test_ovr_level():
    """Should return the correct overview level."""
    with rasterio.open(COG_DST) as src_dst:
        # raw/-1: 2667x2658 0: 1329x1334, 1: 665x667, 2: 333x334, 3: 167x167
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 100, 100, dst_crs=src_dst.crs
            )
            == 3
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 200, 200, dst_crs=src_dst.crs
            )
            == 2
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 500, 500, dst_crs=src_dst.crs
            )
            == 1
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 800, 800, dst_crs=src_dst.crs
            )
            == 0
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 1500, 1500, dst_crs=src_dst.crs
            )
            == -1
        )
        assert (
            utils.get_overview_level(
                src_dst, src_dst.bounds, 3000, 3000, dst_crs=src_dst.crs
            )
            == -1
        )


def test_cutline():
    """Test rio_tiler.utils.create_cutline."""
    feat = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-52.6025390625, 73.86761239709705],
                    [-52.6025390625, 73.59679245247814],
                    [-51.591796875, 73.60299628304274],
                    [-51.591796875, 73.90420357134279],
                    [-52.4267578125, 74.0437225981325],
                    [-52.6025390625, 73.86761239709705],
                ]
            ],
        },
    }

    feature_bounds = featureBounds(feat)

    with Reader(COGEO) as src:
        cutline = utils.create_cutline(src.dataset, feat, geometry_crs="epsg:4326")
        data, mask = src.part(feature_bounds, vrt_options={"cutline": cutline})
        assert not mask.all()

        cutline = utils.create_cutline(
            src.dataset, feat["geometry"], geometry_crs="epsg:4326"
        )
        data, mask = src.part(feature_bounds, vrt_options={"cutline": cutline})
        assert not mask.all()

    feat_line = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-55.37109374999999, 74.17607298699065],
                [-53.85498046874999, 75.06734898853098],
                [-54.16259765625, 75.11822201684025],
                [-54.228515625, 75.23066741281573],
            ],
        },
    }

    with Reader(COGEO) as src:
        with pytest.raises(RioTilerError):
            utils.create_cutline(src.dataset, feat_line, geometry_crs="epsg:4326")

    feat_mp = {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [7.305908203125, 52.14697334064471],
                    [7.84423828125, 52.14697334064471],
                    [7.84423828125, 52.52958999943304],
                    [7.305908203125, 52.52958999943304],
                    [7.305908203125, 52.14697334064471],
                ]
            ],
            [
                [
                    [9.920654296875, 53.25206880589411],
                    [10.404052734375, 53.25206880589411],
                    [10.404052734375, 53.48804553605622],
                    [9.920654296875, 53.48804553605622],
                    [9.920654296875, 53.25206880589411],
                ]
            ],
        ],
    }

    with Reader(COGEO) as src:
        c = utils.create_cutline(src.dataset, feat_mp, geometry_crs="epsg:4326")
        assert "MULTIPOLYGON" in c

    bad_poly = {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    [7.305908203125, 52.14697334064471],
                    [7.84423828125, 52.14697334064471],
                    [7.84423828125, 52.52958999943304],
                    [7.305908203125, 52.52958999943304],
                    [7.305908203125, 52.14697334064471],
                ]
            ],
        ],
    }

    with Reader(COGEO) as src:
        with pytest.raises(RioTilerError):
            utils.create_cutline(src.dataset, bad_poly, geometry_crs="epsg:4326")

    triangle_over_image_edge = {
        "type": "Polygon",
        "coordinates": [
            [
                [-104.775390888988852, 38.953714348778355],
                [-104.775146720379681, 38.953580769848777],
                [-104.775389629827075, 38.953472856486307],
                [-104.775390888988852, 38.953714348778355],
            ]
        ],
    }

    # Check when using `boundless cutline`
    # https://github.com/cogeotiff/rio-tiler/issues/585
    triangle_bounds = featureBounds(triangle_over_image_edge)
    with Reader(COG_RGB) as src:
        cutline = utils.create_cutline(
            src.dataset, triangle_over_image_edge, geometry_crs="epsg:4326"
        )
        data, mask = src.part(triangle_bounds, vrt_options={"cutline": cutline})
        assert sum(mask[:, 0]) == 0  # first column
        assert sum(mask[0, :]) == 0  # first line
        assert sum(mask[-1, :]) == 0  # last line


def test_parse_expression():
    """test parsing rio-tiler expression."""
    assert sorted(parse_expression("b1*b11+b3,b1*b2+B4")) == [1, 2, 3, 4, 11]
    assert sorted(parse_expression("b1*b11+b3,b1*b2+B4", cast=False)) == [
        "1",
        "11",
        "2",
        "3",
        "4",
    ]


def test_render_numpy():
    """Save data to numpy binary."""
    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)

    res = utils.render(arr, mask=mask, img_format="npy")
    arr_res = np.load(BytesIO(res))
    assert arr_res.shape == (4, 512, 512)
    np.array_equal(arr, arr_res[0:3])
    np.array_equal(mask, arr_res[-1])

    res = utils.render(arr, img_format="npy")
    arr_res = np.load(BytesIO(res))
    assert arr_res.shape == (3, 512, 512)
    np.array_equal(arr, arr_res)

    res = utils.render(arr, img_format="npz")
    arr_res = np.load(BytesIO(res))
    assert arr_res.files == ["data"]
    assert arr_res["data"].shape == (3, 512, 512)
    np.array_equal(arr, arr_res["data"])

    res = utils.render(arr, mask, img_format="npz")
    arr_res = np.load(BytesIO(res))
    assert arr_res.files == ["data", "mask"]
    assert arr_res["data"].shape == (3, 512, 512)
    assert arr_res["mask"].shape == (512, 512)
    np.array_equal(arr, arr_res["data"])
    np.array_equal(mask, arr_res["mask"])


def test_get_array_statistics():
    """Should return a valid dict with array statistics."""
    with rasterio.open(COGEO) as src:
        arr = src.read(
            indexes=[1],
            masked=True,
            out_shape=(src.count, int(src.height / 10), int(src.width / 10)),
        )

    stats = utils.get_array_statistics(arr)
    assert len(stats) == 1
    assert list(stats[0]) == [
        "min",
        "max",
        "mean",
        "count",
        "sum",
        "std",
        "median",
        "majority",
        "minority",
        "unique",
        "percentile_2",
        "percentile_98",
        "histogram",
        "valid_pixels",
        "masked_pixels",
        "valid_percent",
    ]

    stats = utils.get_array_statistics(arr, percentiles=[2, 3, 4])
    assert "percentile_2" in stats[0]
    assert "percentile_3" in stats[0]
    assert "percentile_4" in stats[0]

    with rasterio.open(COG_CMAP) as src:
        arr = src.read(
            masked=True,
            out_shape=(src.count, int(src.height / 10), int(src.width / 10)),
        )

    stats = utils.get_array_statistics(arr, categorical=True)
    assert len(stats) == 1
    assert len(stats[0]["histogram"][0]) == stats[0]["unique"]
    assert len(stats[0]["histogram"][1]) == stats[0]["unique"]

    # histogram return only the categories passed
    stats = utils.get_array_statistics(arr, categorical=True, categories=[1, 10, 12])
    assert len(stats[0]["histogram"][0]) == 3
    assert len(stats[0]["histogram"][1]) == 3

    # test if providing a category not in the data (1000000)
    stats = utils.get_array_statistics(
        arr, categorical=True, categories=[1, 10, 12, 1000000]
    )
    assert len(stats[0]["histogram"][0]) == 4
    assert len(stats[0]["histogram"][1]) == 4
    assert stats[0]["histogram"][0][3] == 0.0  # there is no value 1000000

    # COG_NAN has nodata value set to 0.0 but also contains NaN values
    with rasterio.open(COG_NAN) as src:
        arr = src.read(
            masked=True,
            out_shape=(src.count, int(src.height / 10), int(src.width / 10)),
        )
    stats = utils.get_array_statistics(arr)
    assert not math.isnan(stats[0]["min"])
    assert not math.isnan(stats[0]["max"])
    assert not math.isnan(stats[0]["max"])


def test_resize_array():
    """make sure we resize well."""
    arr = np.zeros((3, 256, 256), dtype="uint8")
    arr_r = utils.resize_array(arr, 512, 256)
    assert arr_r.shape == (3, 512, 256)
    assert arr_r.dtype == np.uint8

    arr = np.zeros((256, 256), dtype="uint8")
    arr_r = utils.resize_array(arr, 512, 512)
    assert arr_r.shape == (512, 512)
    assert arr_r.dtype == np.uint8


def test_render_colorinterp():
    """Save data to numpy binary."""

    def parse(content):
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            with MemoryFile(content) as mem:
                with mem.open() as dst:
                    return dst.profile, dst.colorinterp

    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint8)
    mask = np.zeros((512, 512), dtype=np.uint8)

    profile, color = parse(utils.render(arr, mask=mask, img_format="PNG"))
    assert profile["driver"] == "PNG"
    assert profile["count"] == 4
    assert ColorInterp.alpha in color

    profile, color = parse(utils.render(arr, mask=mask, img_format="JPEG"))
    assert profile["driver"] == "JPEG"
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color

    profile, color = parse(utils.render(arr, mask=mask, img_format="WEBP"))
    assert profile["driver"] == "WEBP"
    assert profile["count"] == 4
    assert ColorInterp.alpha in color

    profile, color = parse(utils.render(arr, mask=mask, img_format="GTiff"))
    assert profile["driver"] == "GTiff"
    assert profile["count"] == 4
    # by default GDAL will assign red,green,blue,alpha for uint8+4bands dataset
    assert ColorInterp.alpha in color
    assert ColorInterp.red in color

    arr = np.random.randint(0, 255, size=(3, 512, 512), dtype=np.uint16)
    mask = np.zeros((512, 512), dtype=np.uint8)
    profile, color = parse(utils.render(arr, mask=mask, img_format="GTiff"))
    assert profile["driver"] == "GTiff"
    assert profile["count"] == 4
    assert ColorInterp.alpha in color
    assert ColorInterp.red not in color
    assert ColorInterp.gray in color


def test_get_array_statistics_coverage():
    """Test statistics with coverage array."""
    # Data Array
    # 1, 2
    # 3, 4
    data = np.ma.array((1, 2, 3, 4)).reshape((1, 2, 2))

    # Coverage Array
    # 0.5, 0
    # 1, 0.25
    coverage = np.array((0.5, 0, 1, 0.25)).reshape((2, 2))

    stats = utils.get_array_statistics(data, coverage=coverage)
    assert len(stats) == 1
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 4
    assert stats[0]["mean"] == 1.125  # (1 * 0.5 + 2 * 0.0 + 3 * 1.0 + 4 * 0.25) / 4
    assert stats[0]["count"] == 1.75

    stats = utils.get_array_statistics(data)
    assert len(stats) == 1
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 4
    assert stats[0]["mean"] == 2.5
    assert stats[0]["count"] == 4


def test_get_vrt_transform_world_file(dataset_fixture):
    """Should return correct transform and size."""
    bounds = (
        -17811118.526923772,
        -6446275.841017159,
        17811118.526923772,
        6446275.841017159,
    )
    with MemoryFile(
        dataset_fixture(
            crs=CRS.from_epsg(4326),
            bounds=(-180.0, -90, 180.0, 90.0),
            dtype="uint8",
            nodata_type="nodata",
            width=720,
            height=360,
        )
    ) as memfile:
        with memfile.open() as src_dst:
            # adjusting latitudes
            # with pytest.warns(UserWarning):
            vrt_transform, vrt_width, vrt_height = utils.get_vrt_transform(
                src_dst,
                bounds,
                dst_crs="epsg:3857",
            )

    assert vrt_transform[2] == -17811118.526923772
    assert vrt_transform[5] == 6446275.841017159
    assert vrt_width == 501  # 59 without the latitude adjust patch
    assert vrt_height == 181  # 21 without the latitude adjust patch
