"""tests rio_tiler.utils"""

import json
import math
import os
import warnings
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

import numpy as np
import pytest
import rasterio
import rasterio.env
from rasterio._env import get_gdal_config
from rasterio.crs import CRS
from rasterio.dtypes import dtype_ranges
from rasterio.enums import ColorInterp
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.io import MemoryFile

from rio_tiler import colormap, utils
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidFormat, RioTilerError
from rio_tiler.io import Reader
from rio_tiler.profiles import img_profiles

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


def test_cutline_operator(dataset_fixture):
    """Test rio_tiler.utils.create_cutline with operators."""
    with MemoryFile(
        dataset_fixture(
            crs=CRS.from_epsg(4326),
            bounds=(-175.0, -85, 175.0, 85.0),
            dtype="uint8",
            nodata_type="nodata",
            width=720,
            height=360,
        )
    ) as memfile:
        with memfile.open() as src_dst:
            feat = {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-163.0, -83.0],
                        [163.0, -83.0],
                        [163.0, 83.0],
                        [-163.0, 83.0],
                        [-163.0, -83.0],
                    ]
                ],
            }
            cutline = utils.create_cutline(
                src_dst,
                feat,
                geometry_crs="epsg:4326",
            )
            cutline_mathfloor = utils.create_cutline(
                src_dst,
                feat,
                geometry_crs="epsg:4326",
                op=math.floor,
            )
            assert cutline == cutline_mathfloor

            cutline_npfloor = utils.create_cutline(
                src_dst,
                feat,
                geometry_crs="epsg:4326",
                op=np.floor,
            )
            assert cutline_npfloor == cutline_mathfloor

            cutline_npceil = utils.create_cutline(
                src_dst,
                feat,
                geometry_crs="epsg:4326",
                op=np.ceil,
            )
            assert cutline_npceil != cutline_npfloor


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
    # Make sure the statistics object are JSON serializable
    assert json.dumps(stats[0])

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

    # Totally Masked Array
    arr = np.ma.MaskedArray(data=np.zeros((1, 256, 256), dtype="uint8"), mask=True)
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
    # Make sure the statistics object are JSON serializable
    assert json.dumps(stats[0])
    assert math.isnan(stats[0]["min"])
    assert math.isnan(stats[0]["max"])
    assert math.isnan(stats[0]["max"])
    assert math.isnan(stats[0]["mean"])
    assert stats[0]["count"] == 0
    assert stats[0]["sum"] == 0
    assert math.isnan(stats[0]["std"])
    assert math.isnan(stats[0]["median"])


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
    # same test as https://github.com/isciences/exactextract?tab=readme-ov-file#supported-statistics
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
    assert (
        round(stats[0]["mean"], 4) == 2.5714
    )  # sum of weighted array / sum of weights | 4.5 / 1.75 = 2.57
    assert stats[0]["count"] == 1.75
    assert stats[0]["median"] == 3  # 2 in exactextract
    assert round(stats[0]["std"], 2) == 1.05
    assert stats[0]["valid_percent"] == 100

    stats = utils.get_array_statistics(data)
    assert len(stats) == 1
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 4
    assert stats[0]["mean"] == 2.5
    assert stats[0]["count"] == 4
    assert stats[0]["valid_percent"] == 100

    # same test as https://github.com/isciences/exactextract/blob/0883cd585d9c7b6b4e936aeca4aa84a15adf82d2/python/tests/test_exact_extract.py#L48-L110
    data = np.ma.arange(1, 10, dtype=np.int32).reshape(3, 3)
    coverage = np.array([0.25, 0.5, 0.25, 0.5, 1.0, 0.5, 0.25, 0.5, 0.25]).reshape(3, 3)
    stats = utils.get_array_statistics(data, coverage=coverage, percentiles=[25, 75])
    assert len(stats) == 1
    assert stats[0]["count"] == 4
    assert stats[0]["mean"] == 5
    assert stats[0]["median"] == 5.0
    assert isinstance(stats[0]["median"], float)
    assert stats[0]["min"] == 1
    assert stats[0]["max"] == 9
    # exactextract takes coverage into account, we don't
    assert stats[0]["minority"] == 1  # 1 in exactextract
    assert stats[0]["majority"] == 1  # 5 in exactextract
    assert stats[0]["percentile_25"] == 3.0
    assert stats[0]["percentile_75"] == 6.0
    assert isinstance(stats[0]["percentile_25"], float)
    assert isinstance(stats[0]["percentile_75"], float)
    assert stats[0]["std"] == math.sqrt(5)

    # test correct calculation of valid percent with masked array and coverage array
    data = np.ma.array(
        [[[0, 1], [0, 5]]], mask=[[[True, False], [True, False]]], fill_value=0
    )
    coverage = np.array([[0, 0.5], [0.75, 1]])
    stats = utils.get_array_statistics(data, coverage=coverage)
    assert stats[0]["valid_percent"] == 66.67


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


def test_render_partial_alpha():
    """Mix Alpha Mask and Alpha from ColorMap"""
    # Partial alpha values
    cm = {
        1: (0, 0, 0, 0),
        500: (100, 100, 100, 50),
        1000: (255, 255, 255, 255),
    }
    data = np.zeros((1, 256, 256), dtype="float32") + 1
    data[0, 0, 0] = 0
    data[0, 1:, 1:] = 1
    data[0, 2:, 2:] = 500
    data[0, 3:, 3:] = 1000

    minv, maxv = dtype_ranges["float32"]
    alpha = np.zeros((1, 256, 256), dtype="float32") + maxv
    alpha[0, 0, 0] = minv

    content = utils.render(
        data,
        mask=alpha[0],
        img_format="PNG",
        colormap=cm,
    )

    with MemoryFile(content) as mem:
        with mem.open() as dst:
            data_converted = dst.read()
            assert dst.count == 4
            assert dst.dtypes == ("uint8", "uint8", "uint8", "uint8")
            assert data[:, 0, 0].tolist() == [0]
            assert data_converted[:, 0, 0].tolist() == [
                0,
                0,
                0,
                0,
            ]  # Masked from Original Mask | set to UINT8 (0)

            assert data[:, 1, 1].tolist() == [1]
            assert data_converted[:, 1, 1].tolist() == [
                0,
                0,
                0,
                0,
            ]  # masked from CMAP

            assert data[:, 2, 2].tolist() == [500]
            assert data_converted[:, 2, 2].tolist() == [
                100,
                100,
                100,
                50,
            ]  # Partially masked from CMAP

            assert data[:, 3, 3].tolist() == [1000]
            assert data_converted[:, 3, 3].tolist() == [
                255,
                255,
                255,
                255,
            ]  # Non-masked from CMAP


def test_inherit_rasterio_env_empty():
    """When there's no rasterio env, inheriting the env should be a no-op."""

    def hasenv() -> bool:
        return rasterio.env.hasenv()

    bare_hasenv = hasenv
    decorated_hasenv = utils.inherit_rasterio_env(hasenv)

    assert decorated_hasenv is bare_hasenv
    assert decorated_hasenv() is False


def test_inherit_rasterio_env_not_empty():
    """When there is a rasterio env, it should be inherited."""

    def hasenv() -> bool:
        return rasterio.env.hasenv()

    bare_hasenv = hasenv

    with rasterio.Env():
        decorated_hasenv = utils.inherit_rasterio_env(hasenv)

    assert bare_hasenv() is False
    assert decorated_hasenv is not bare_hasenv
    assert decorated_hasenv() is True


def test_inherit_rasterio_env_not_empty_separate_thread(monkeypatch):
    """When there is a rasterio env, it should be inherited from separate thread."""

    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):

        @utils.inherit_rasterio_env
        def hasenv(*args: object) -> tuple[bool, str]:
            return (
                rasterio.env.hasenv(),
                get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN"),
            )

        def hasnotenv(*args: object) -> tuple[bool, bool]:
            return (
                rasterio.env.hasenv(),
                get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN"),
            )

    with ThreadPoolExecutor() as exec:
        futures = [
            exec.submit(hasenv, [0]),
            exec.submit(hasnotenv, [0]),
        ]
        resuts = [f.result() for f in futures]
        assert resuts == [
            (True, "FALSE"),
            (False, "something"),
        ]


def _decode_raster(content: bytes):
    """Decode image bytes with rasterio; return (data, profile, colorinterp)."""
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
        with MemoryFile(content) as mem:
            with mem.open() as dst:
                return dst.read(), dst.profile, dst.colorinterp


def test_render_png_roundtrip_uint8():
    """Lossless PNG decode equals input (1-band, 3-band, +mask)."""
    rng = np.random.default_rng(42)
    gray = rng.integers(0, 256, size=(1, 64, 64), dtype=np.uint8)
    rgb = rng.integers(0, 256, size=(3, 64, 64), dtype=np.uint8)
    mask = np.full((64, 64), 255, dtype=np.uint8)
    mask[:10, :10] = 0
    mask[20:30, 20:30] = 128

    data, profile, _ = _decode_raster(utils.render(gray, img_format="PNG"))
    assert profile["driver"] == "PNG"
    assert profile["count"] == 1
    np.testing.assert_array_equal(data[0], gray[0])

    data, profile, color = _decode_raster(utils.render(rgb, mask=mask, img_format="PNG"))
    assert profile["count"] == 4
    assert ColorInterp.alpha in color
    np.testing.assert_array_equal(data[:3], rgb)
    np.testing.assert_array_equal(data[3], mask)

    data, profile, _ = _decode_raster(utils.render(rgb, img_format="PNG"))
    assert profile["count"] == 3
    np.testing.assert_array_equal(data, rgb)


def test_render_jpeg_drops_mask_layout():
    """JPEG always drops mask and keeps 3 bands."""
    rgb = np.zeros((3, 32, 32), dtype=np.uint8) + 40
    rgb[0] = 200
    mask = np.zeros((32, 32), dtype=np.uint8)
    data, profile, color = _decode_raster(utils.render(rgb, mask=mask, img_format="JPEG"))
    assert profile["driver"] == "JPEG"
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color
    assert data.shape == (3, 32, 32)


def test_render_jpeg_default_quality_is_gdal_75(monkeypatch):
    """Bare JPEG uses QUALITY=75 (GDAL default), not img_profiles 85."""
    monkeypatch.delenv("RIO_TILER_FAST_ENCODE", raising=False)
    rng = np.random.default_rng(0)
    rgb = rng.integers(0, 256, size=(3, 64, 64), dtype=np.uint8)
    # GDAL path (default) and fast path both use 75 when QUALITY omitted
    bare = utils.render(rgb, img_format="JPEG", fast_encode=False)
    q75 = utils.render(rgb, img_format="JPEG", QUALITY=75, fast_encode=False)
    q85 = utils.render(rgb, img_format="JPEG", QUALITY=85, fast_encode=False)
    assert bare == q75
    assert bare != q85

    bare_fast = utils.render(rgb, img_format="JPEG", fast_encode=True)
    q75_fast = utils.render(rgb, img_format="JPEG", QUALITY=75, fast_encode=True)
    q85_fast = utils.render(rgb, img_format="JPEG", QUALITY=85, fast_encode=True)
    assert bare_fast == q75_fast
    assert bare_fast != q85_fast


@requires_webp
def test_render_webp_gray_expands_to_rgb():
    """WEBP 1-band is expanded to RGB with equal channels."""
    gray = np.full((1, 32, 32), 77, dtype=np.uint8)
    data, profile, _ = _decode_raster(utils.render(gray, img_format="WEBP"))
    assert profile["driver"] == "WEBP"
    assert profile["count"] == 3
    np.testing.assert_array_equal(data[0], data[1])
    np.testing.assert_array_equal(data[1], data[2])


def test_render_colormap_mask_band_count():
    """Colormap without mask omits alpha; with mask includes alpha."""
    arr = np.zeros((1, 16, 16), dtype=np.uint8) + 1
    cm = {0: (0, 0, 0, 0), 1: (255, 0, 0, 255)}

    data, profile, color = _decode_raster(utils.render(arr, colormap=cm))
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color
    np.testing.assert_array_equal(data[:, 0, 0], [255, 0, 0])

    mask = np.full((16, 16), 255, dtype=np.uint8)
    data, profile, color = _decode_raster(
        utils.render(arr, mask=mask, colormap=cm, img_format="PNG")
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color
    np.testing.assert_array_equal(data[:, 0, 0], [255, 0, 0, 255])


def test_render_fast_encode_default_off(monkeypatch):
    """Without opt-in, encode matches explicit fast_encode=False (GDAL path)."""
    monkeypatch.delenv("RIO_TILER_FAST_ENCODE", raising=False)
    rng = np.random.default_rng(1)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)
    bare = utils.render(rgb, img_format="PNG", ZLEVEL=6)
    off = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=False)
    assert bare == off


def test_render_fast_path_matches_gdal_png_decode():
    """Fast encode path and GDAL path decode to the same PNG pixels."""
    rng = np.random.default_rng(7)
    rgb = rng.integers(0, 256, size=(3, 48, 48), dtype=np.uint8)
    mask = np.full((48, 48), 255, dtype=np.uint8)
    mask[:8, :8] = 0
    mask[10:20, 10:20] = 100

    for zlevel in (1, 6):
        fast_bytes = utils.render(
            rgb, mask=mask, img_format="PNG", ZLEVEL=zlevel, fast_encode=True
        )
        gdal_bytes = utils.render(
            rgb, mask=mask, img_format="PNG", ZLEVEL=zlevel, fast_encode=False
        )

        # Raw codec bytes may differ; decoded pixels must match.
        p_data, p_prof, p_ci = _decode_raster(fast_bytes)
        g_data, g_prof, g_ci = _decode_raster(gdal_bytes)
        assert p_prof["count"] == g_prof["count"] == 4
        assert ColorInterp.alpha in p_ci and ColorInterp.alpha in g_ci
        np.testing.assert_array_equal(p_data, g_data)


@pytest.mark.parametrize("env_val", ["1", "true", "TRUE", "yes", "on"])
def test_render_fast_encode_env(monkeypatch, env_val):
    """RIO_TILER_FAST_ENCODE enables fast path; kwarg overrides env."""
    rng = np.random.default_rng(3)
    rgb = rng.integers(0, 256, size=(3, 24, 24), dtype=np.uint8)

    monkeypatch.delenv("RIO_TILER_FAST_ENCODE", raising=False)
    default_bytes = utils.render(rgb, img_format="PNG", ZLEVEL=6)
    gdal_bytes = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=False)
    assert default_bytes == gdal_bytes

    monkeypatch.setenv("RIO_TILER_FAST_ENCODE", env_val)
    env_on = utils.render(rgb, img_format="PNG", ZLEVEL=6)
    explicit_on = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=True)
    # Both should be fast path when backends exist; decode-equal either way
    e_data, _, _ = _decode_raster(env_on)
    x_data, _, _ = _decode_raster(explicit_on)
    g_data, _, _ = _decode_raster(gdal_bytes)
    np.testing.assert_array_equal(e_data, g_data)
    np.testing.assert_array_equal(x_data, g_data)

    # Explicit False wins over env
    env_overridden = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=False)
    assert env_overridden == gdal_bytes


def test_render_fast_encode_env_falsy_ignored(monkeypatch):
    """Unrecognized / falsy env values keep the GDAL default path."""
    rng = np.random.default_rng(4)
    rgb = rng.integers(0, 256, size=(3, 16, 16), dtype=np.uint8)
    gdal_bytes = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=False)

    for env_val in ["0", "false", "off", "", "maybe"]:
        monkeypatch.setenv("RIO_TILER_FAST_ENCODE", env_val)
        assert utils.render(rgb, img_format="PNG", ZLEVEL=6) == gdal_bytes


def test_render_fast_encode_unsupported_options_use_gdal():
    """Unknown creation options force GDAL instead of silently ignoring them."""
    rng = np.random.default_rng(5)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)

    # WORLDFILE is a real GDAL option the fast path does not implement
    gdal = utils.render(
        rgb, img_format="PNG", ZLEVEL=6, WORLDFILE="YES", fast_encode=False
    )
    fast = utils.render(
        rgb, img_format="PNG", ZLEVEL=6, WORLDFILE="YES", fast_encode=True
    )
    assert fast == gdal

    # JPEG progressive not mapped by fast path
    gdal_j = utils.render(
        rgb, img_format="JPEG", QUALITY=75, PROGRESSIVE="ON", fast_encode=False
    )
    fast_j = utils.render(
        rgb, img_format="JPEG", QUALITY=75, PROGRESSIVE="ON", fast_encode=True
    )
    assert fast_j == gdal_j


def test_render_fast_encode_jpeg_layout():
    """Fast JPEG: drop mask; gray stays 1-band; RGB stays 3-band."""
    rgb = np.zeros((3, 32, 32), dtype=np.uint8) + 40
    rgb[0] = 200
    mask = np.zeros((32, 32), dtype=np.uint8)
    data, profile, color = _decode_raster(
        utils.render(rgb, mask=mask, img_format="JPEG", fast_encode=True)
    )
    assert profile["driver"] == "JPEG"
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color
    assert data.shape == (3, 32, 32)

    gray = np.full((1, 32, 32), 90, dtype=np.uint8)
    data, profile, _ = _decode_raster(
        utils.render(gray, img_format="JPEG", fast_encode=True)
    )
    assert profile["count"] == 1
    assert data.shape == (1, 32, 32)

    # Gray + mask: JPEG drops mask, stays 1-band
    mask = np.zeros((32, 32), dtype=np.uint8)
    mask[:4, :4] = 0
    data, profile, color = _decode_raster(
        utils.render(gray, mask=mask, img_format="JPEG", fast_encode=True)
    )
    assert profile["count"] == 1
    assert ColorInterp.alpha not in color
    assert data.shape == (1, 32, 32)


def test_render_fast_encode_jpeg_four_band_cmyk_parity():
    """4-band JPEG must fall back to GDAL CMYK, byte-identical, in fast mode.

    The fast path cannot emit GDAL's 4-band CMYK JPEG, so it must bail to
    GDAL and produce byte-identical output. This locks the contract so a
    future change cannot silently switch 4-band JPEG to 3-band RGB.
    """
    rgba = np.zeros((4, 32, 32), dtype=np.uint8)
    rgba[0] = 200
    rgba[3] = 255
    gdal = utils.render(rgba, img_format="JPEG", fast_encode=False)
    fast = utils.render(rgba, img_format="JPEG", fast_encode=True)
    assert fast == gdal
    data, profile, _ = _decode_raster(gdal)
    assert profile["driver"] == "JPEG"


@requires_webp
def test_render_fast_encode_webp_layout():
    """Fast WEBP: gray expands to RGB; mask becomes alpha (4 bands)."""
    gray = np.full((1, 32, 32), 77, dtype=np.uint8)
    data, profile, _ = _decode_raster(
        utils.render(gray, img_format="WEBP", fast_encode=True)
    )
    assert profile["driver"] == "WEBP"
    assert profile["count"] == 3
    np.testing.assert_array_equal(data[0], data[1])
    np.testing.assert_array_equal(data[1], data[2])

    rgb = np.zeros((3, 32, 32), dtype=np.uint8) + 10
    mask = np.full((32, 32), 255, dtype=np.uint8)
    mask[:4, :4] = 0
    data, profile, color = _decode_raster(
        utils.render(rgb, mask=mask, img_format="WEBP", fast_encode=True)
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color

    # 4-band RGBA without separate mask stays 4-band
    rng = np.random.default_rng(18)
    rgba = rng.integers(0, 256, size=(4, 32, 32), dtype=np.uint8)
    data, profile, color = _decode_raster(
        utils.render(rgba, img_format="WEBP", fast_encode=True)
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color


def test_render_fast_encode_colormap_mask_band_count():
    """Fast path keeps colormap ± mask band-count contract."""
    arr = np.zeros((1, 16, 16), dtype=np.uint8) + 1
    cm = {0: (0, 0, 0, 0), 1: (255, 0, 0, 255)}

    data, profile, color = _decode_raster(
        utils.render(arr, colormap=cm, fast_encode=True)
    )
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color
    np.testing.assert_array_equal(data[:, 0, 0], [255, 0, 0])

    mask = np.full((16, 16), 255, dtype=np.uint8)
    data, profile, color = _decode_raster(
        utils.render(arr, mask=mask, colormap=cm, img_format="PNG", fast_encode=True)
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color
    np.testing.assert_array_equal(data[:, 0, 0], [255, 0, 0, 255])


@requires_webp
def test_render_fast_encode_colormap_webp():
    """Fast path: colormap + WEBP keeps band-count contract (3 vs 4)."""
    arr = np.zeros((1, 16, 16), dtype=np.uint8) + 1
    cm = {0: (0, 0, 0, 0), 1: (255, 0, 0, 255)}

    # Colormap without mask → 3-band (no alpha)
    data, profile, color = _decode_raster(
        utils.render(arr, colormap=cm, img_format="WEBP", fast_encode=True)
    )
    assert profile["driver"] == "WEBP"
    assert profile["count"] == 3
    assert ColorInterp.alpha not in color

    # Colormap + partial mask (with transparent pixels) → 4-band
    mask = np.full((16, 16), 255, dtype=np.uint8)
    mask[:4, :4] = 0
    data, profile, color = _decode_raster(
        utils.render(arr, mask=mask, colormap=cm, img_format="WEBP", fast_encode=True)
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color

    # Decode-equal to GDAL for both cases
    for m in (None, mask):
        f_data, _, _ = _decode_raster(
            utils.render(arr, mask=m, colormap=cm, img_format="WEBP", fast_encode=True)
        )
        g_data, _, _ = _decode_raster(
            utils.render(arr, mask=m, colormap=cm, img_format="WEBP", fast_encode=False)
        )
        np.testing.assert_array_equal(f_data, g_data)


def test_render_fast_encode_img_profiles_honored():
    """Explicit img_profiles options are honored on the fast path."""
    rng = np.random.default_rng(8)
    rgb = rng.integers(0, 256, size=(3, 48, 48), dtype=np.uint8)

    jpeg_prof = img_profiles["jpeg"]  # quality 85
    bare_fast = utils.render(rgb, img_format="JPEG", fast_encode=True)
    profile_fast = utils.render(rgb, img_format="JPEG", fast_encode=True, **jpeg_prof)
    assert bare_fast != profile_fast
    assert profile_fast == utils.render(
        rgb, img_format="JPEG", QUALITY=85, fast_encode=True
    )

    png_raw = img_profiles["pngraw"]  # zlevel 1
    fast_z1 = utils.render(rgb, img_format="PNG", fast_encode=True, **png_raw)
    gdal_z1 = utils.render(rgb, img_format="PNG", fast_encode=False, **png_raw)
    f_data, _, _ = _decode_raster(fast_z1)
    g_data, _, _ = _decode_raster(gdal_z1)
    np.testing.assert_array_equal(f_data, g_data)


def test_render_fast_encode_four_band_rgba_png():
    """4-band uint8 without separate mask encodes as RGBA on fast path."""
    rng = np.random.default_rng(9)
    rgba = rng.integers(0, 256, size=(4, 24, 24), dtype=np.uint8)
    fast = utils.render(rgba, img_format="PNG", fast_encode=True)
    gdal = utils.render(rgba, img_format="PNG", fast_encode=False)
    f_data, f_prof, _ = _decode_raster(fast)
    g_data, g_prof, _ = _decode_raster(gdal)
    assert f_prof["count"] == g_prof["count"] == 4
    np.testing.assert_array_equal(f_data, g_data)


def test_render_fast_encode_png_roundtrip_uint8():
    """Fast-path lossless PNG decode equals input (1-band, 3-band, +mask)."""
    rng = np.random.default_rng(42)
    gray = rng.integers(0, 256, size=(1, 64, 64), dtype=np.uint8)
    rgb = rng.integers(0, 256, size=(3, 64, 64), dtype=np.uint8)
    mask = np.full((64, 64), 255, dtype=np.uint8)
    mask[:10, :10] = 0
    mask[20:30, 20:30] = 128

    data, profile, _ = _decode_raster(
        utils.render(gray, img_format="PNG", fast_encode=True)
    )
    assert profile["driver"] == "PNG"
    assert profile["count"] == 1
    np.testing.assert_array_equal(data[0], gray[0])

    data, profile, color = _decode_raster(
        utils.render(rgb, mask=mask, img_format="PNG", fast_encode=True)
    )
    assert profile["count"] == 4
    assert ColorInterp.alpha in color
    np.testing.assert_array_equal(data[:3], rgb)
    np.testing.assert_array_equal(data[3], mask)

    data, profile, _ = _decode_raster(
        utils.render(rgb, img_format="PNG", fast_encode=True)
    )
    assert profile["count"] == 3
    np.testing.assert_array_equal(data, rgb)


def test_render_fast_encode_default_off_all_formats(monkeypatch):
    """Bare render matches fast_encode=False for PNG/JPEG/WEBP (GDAL path)."""
    monkeypatch.delenv("RIO_TILER_FAST_ENCODE", raising=False)
    rng = np.random.default_rng(12)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)
    gray = rng.integers(0, 256, size=(1, 32, 32), dtype=np.uint8)

    assert utils.render(rgb, img_format="PNG") == utils.render(
        rgb, img_format="PNG", fast_encode=False
    )
    assert utils.render(rgb, img_format="JPEG") == utils.render(
        rgb, img_format="JPEG", fast_encode=False
    )
    assert utils.render(gray, img_format="WEBP") == utils.render(
        gray, img_format="WEBP", fast_encode=False
    )


def test_render_fast_encode_invalid_format_still_raises():
    """Invalid shapes still raise InvalidFormat with fast_encode on or off."""
    bad = np.zeros((5, 32, 32), dtype=np.uint8)
    with pytest.raises(InvalidFormat):
        utils.render(bad, img_format="PNG", fast_encode=False)
    with pytest.raises(InvalidFormat):
        utils.render(bad, img_format="PNG", fast_encode=True)

    with pytest.raises(InvalidFormat):
        utils.render(np.zeros((1, 8, 8), dtype=np.uint8), img_format="NOTADRIVER")


def test_render_fast_encode_non_uint8_bails_to_gdal():
    """Non-uint8 dtypes must bypass the fast path and use GDAL identically.

    The fast path only handles uint8. For uint16/float32/etc. it must bail
    out immediately (dtype check) so GDAL is used with zero overhead —
    fast_encode=True must produce byte-identical output to fast_encode=False.
    """
    rng = np.random.default_rng(21)

    # uint16 1-band PNG (stays uint16 through GDAL)
    u16 = rng.integers(0, 65536, size=(1, 32, 32), dtype=np.uint16)
    assert utils.render(u16, img_format="PNG", fast_encode=True) == utils.render(
        u16, img_format="PNG", fast_encode=False
    )

    # uint16 1-band PNG + mask (mask rescaled to 0-65535)
    mask = np.full((32, 32), 255, dtype=np.uint8)
    mask[:4, :4] = 0
    assert utils.render(
        u16, mask=mask, img_format="PNG", fast_encode=True
    ) == utils.render(u16, mask=mask, img_format="PNG", fast_encode=False)

    # NPY accepts any dtype — fast path must bail, output identical
    f32 = (rng.random((3, 16, 16), dtype=np.float32) * 1000).astype(np.float32)
    assert utils.render(f32, img_format="NPY", fast_encode=True) == utils.render(
        f32, img_format="NPY", fast_encode=False
    )


def test_render_fast_encode_without_backends(monkeypatch):
    """fast_encode=True falls back to GDAL when imagecodecs is missing."""
    import builtins

    real_import = builtins.__import__

    def _block_imagecodecs(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "imagecodecs" or name.startswith("imagecodecs."):
            raise ImportError(f"blocked {name}")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", _block_imagecodecs)

    rng = np.random.default_rng(13)
    rgb = rng.integers(0, 256, size=(3, 24, 24), dtype=np.uint8)
    gdal = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=False)
    fast = utils.render(rgb, img_format="PNG", ZLEVEL=6, fast_encode=True)
    assert fast == gdal


@requires_webp
@pytest.mark.parametrize("lossless_val", ["TRUE", "true", "YES", "ON", "1", True])
def test_render_fast_encode_webp_lossless_truthy(lossless_val):
    """Fast WEBP honors GDAL-style truthy LOSSLESS strings as lossless."""
    rng = np.random.default_rng(15)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)

    fast = utils.render(rgb, img_format="WEBP", LOSSLESS=lossless_val, fast_encode=True)
    gdal = utils.render(rgb, img_format="WEBP", LOSSLESS=lossless_val, fast_encode=False)
    # Lossless output is deterministic and backend-independent for the same
    # pixels; decode-equal guards the contract even if raw bytes differ.
    f_data, _, _ = _decode_raster(fast)
    g_data, _, _ = _decode_raster(gdal)
    np.testing.assert_array_equal(f_data, g_data)

    # Lossless must not match lossy output for non-trivial input
    lossy = utils.render(rgb, img_format="WEBP", LOSSLESS=False, fast_encode=True)
    assert fast != lossy


@requires_webp
@pytest.mark.parametrize("lossless_val", ["FALSE", "false", "NO", "OFF", "0", False])
def test_render_fast_encode_webp_lossless_falsy(lossless_val):
    """Fast WEBP honors GDAL-style falsy LOSSLESS strings as lossy.

    Regression: ``bool("FALSE")`` is ``True`` in Python, so string values must
    be interpreted explicitly (not via ``bool()``).
    """
    rng = np.random.default_rng(16)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)

    fast = utils.render(rgb, img_format="WEBP", LOSSLESS=lossless_val, fast_encode=True)
    gdal = utils.render(rgb, img_format="WEBP", LOSSLESS=lossless_val, fast_encode=False)
    # Both should be lossy; decode-equal confirms the fast path did not
    # accidentally produce lossless output.
    f_data, _, _ = _decode_raster(fast)
    g_data, _, _ = _decode_raster(gdal)
    np.testing.assert_array_equal(f_data, g_data)

    # Lossy must not match lossless output for non-trivial input
    lossless = utils.render(rgb, img_format="WEBP", LOSSLESS=True, fast_encode=True)
    assert fast != lossless


@requires_webp
def test_render_fast_encode_webp_img_profiles():
    """img_profiles['webp'] (quality 75, lossless False) honored on fast path."""
    rng = np.random.default_rng(17)
    rgb = rng.integers(0, 256, size=(3, 32, 32), dtype=np.uint8)

    webp_prof = img_profiles["webp"]  # quality 75, lossless False
    fast = utils.render(rgb, img_format="WEBP", fast_encode=True, **webp_prof)
    gdal = utils.render(rgb, img_format="WEBP", fast_encode=False, **webp_prof)
    f_data, _, _ = _decode_raster(fast)
    g_data, _, _ = _decode_raster(gdal)
    np.testing.assert_array_equal(f_data, g_data)

    # Explicit lossless via profile must differ from default lossy
    lossless_prof = {**webp_prof, "lossless": True}
    fast_lossless = utils.render(
        rgb, img_format="WEBP", fast_encode=True, **lossless_prof
    )
    assert fast != fast_lossless


def test_render_fast_encode_real_cog_png_jpeg():
    """Real COG through ImageData.render: fast path decode-equals GDAL (PNG)
    and matches layout (JPEG). Covers masked arrays, add_mask, and GTIFF bypass.
    """
    with Reader(COG_RGB) as src:
        img = src.preview()

    # PNG (lossless): decoded pixels must match exactly
    png_off = img.render(img_format="PNG", ZLEVEL=6, fast_encode=False)
    png_on = img.render(img_format="PNG", ZLEVEL=6, fast_encode=True)
    p_off, p_prof_off, p_ci_off = _decode_raster(png_off)
    p_on, p_prof_on, p_ci_on = _decode_raster(png_on)
    assert p_prof_on["count"] == p_prof_off["count"] == 4
    assert ColorInterp.alpha in p_ci_on and ColorInterp.alpha in p_ci_off
    np.testing.assert_array_equal(p_on, p_off)

    # JPEG (lossy): layout must match (count, shape, no alpha)
    j_off, j_prof_off, j_ci_off = _decode_raster(
        img.render(img_format="JPEG", fast_encode=False)
    )
    j_on, j_prof_on, j_ci_on = _decode_raster(
        img.render(img_format="JPEG", fast_encode=True)
    )
    assert j_prof_on["count"] == j_prof_off["count"] == 3
    assert ColorInterp.alpha not in j_ci_on and ColorInterp.alpha not in j_ci_off
    assert j_on.shape == j_off.shape

    # add_mask=False: no alpha band
    nm_off, nm_prof_off, _ = _decode_raster(
        img.render(img_format="PNG", add_mask=False, fast_encode=False)
    )
    nm_on, nm_prof_on, _ = _decode_raster(
        img.render(img_format="PNG", add_mask=False, fast_encode=True)
    )
    assert nm_prof_on["count"] == nm_prof_off["count"] == 3
    np.testing.assert_array_equal(nm_on, nm_off)

    # GTIFF: fast path must bail (not PNG/JPEG/WEBP); byte-identical
    assert img.render(img_format="GTIFF", fast_encode=True) == img.render(
        img_format="GTIFF", fast_encode=False
    )


def test_render_fast_encode_rescaled_output_equality():
    """uint16/int16 COG rescaled to uint8 in ImageData.render then fast-encoded.

    This is the most common TiTiler path: non-byte data → rescale → encode.
    The rescaled uint8 output must decode-equal between fast and GDAL paths.
    """
    # uint16 1-band (cog.tif) — rescaled to uint8 via dataset type bounds
    with Reader(COGEO) as src:
        img = src.preview(max_size=256)
    assert img.array.dtype == np.uint16

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        png_off = img.render(img_format="PNG", fast_encode=False)
        png_on = img.render(img_format="PNG", fast_encode=True)
    off_data, off_prof, _ = _decode_raster(png_off)
    on_data, on_prof, _ = _decode_raster(png_on)
    assert off_prof["count"] == on_prof["count"]
    np.testing.assert_array_equal(on_data, off_data)

    # int16 2-band (cog_scale.tif) with nodata — masked array + rescale
    with Reader(
        os.path.join(os.path.dirname(__file__), "fixtures", "cog_scale.tif")
    ) as src:
        img = src.preview()
    assert img.array.dtype == np.int16
    assert np.ma.is_masked(img.array)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        png_off = img.render(img_format="PNG", fast_encode=False)
        png_on = img.render(img_format="PNG", fast_encode=True)
    off_data, off_prof, _ = _decode_raster(png_off)
    on_data, on_prof, _ = _decode_raster(png_on)
    assert off_prof["count"] == on_prof["count"]
    np.testing.assert_array_equal(on_data, off_data)


@pytest.mark.parametrize(
    "fmt,option,bad_val,clamped_val",
    [
        ("JPEG", "QUALITY", 0, 1),
        ("JPEG", "QUALITY", -5, 1),
        ("JPEG", "QUALITY", 200, 100),
        ("PNG", "ZLEVEL", -1, 0),
        ("PNG", "ZLEVEL", 99, 9),
    ],
)
def test_render_fast_encode_clamps_out_of_range_options(
    fmt, option, bad_val, clamped_val
):
    """Fast path clamps out-of-range QUALITY/ZLEVEL instead of raising.

    GDAL rejects these with InvalidFormat; the fast path clamps silently.
    This is a deliberate divergence: clamped output must match the output
    at the clamped (in-range) value.
    """
    rng = np.random.default_rng(22)
    rgb = rng.integers(0, 256, size=(3, 16, 16), dtype=np.uint8)

    bad = utils.render(rgb, img_format=fmt, **{option: bad_val}, fast_encode=True)
    clamped = utils.render(rgb, img_format=fmt, **{option: clamped_val}, fast_encode=True)
    assert bad == clamped


def test_render_fast_encode_gtiff_bypass():
    """GTIFF (and other non-PNG/JPEG/WEBP formats) bypass the fast path entirely."""
    rng = np.random.default_rng(23)
    rgb = rng.integers(0, 256, size=(3, 16, 16), dtype=np.uint8)

    # GTIFF: not in {PNG, JPEG, WEBP} → _render_uint8_fast returns None
    assert utils.render(rgb, img_format="GTIFF", fast_encode=True) == utils.render(
        rgb, img_format="GTIFF", fast_encode=False
    )

    # NPY: not in {PNG, JPEG, WEBP} → bypass
    assert utils.render(rgb, img_format="NPY", fast_encode=True) == utils.render(
        rgb, img_format="NPY", fast_encode=False
    )

    # JP2OPENJPEG: not in {PNG, JPEG, WEBP} → bypass
    assert utils.render(rgb, img_format="JP2OPENJPEG", fast_encode=True) == utils.render(
        rgb, img_format="JP2OPENJPEG", fast_encode=False
    )


def test_render_fast_encode_thread_safety():
    """Concurrent fast_encode renders from multiple threads must all succeed.

    TiTiler runs threaded/async; the import-inside-function pattern and
    imagecodecs/Pillow encoders must be safe under concurrent access.
    """
    import secrets
    from concurrent.futures import ThreadPoolExecutor, as_completed

    mask = np.full((64, 64), 255, dtype=np.uint8)
    mask[:8, :8] = 0

    def render_one(_):
        rng = np.random.default_rng(int.from_bytes(secrets.token_bytes(8), "big"))
        data = rng.integers(0, 256, size=(3, 64, 64), dtype=np.uint8)
        return utils.render(data, mask=mask, img_format="PNG", ZLEVEL=6, fast_encode=True)

    results = []
    errors = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(render_one, i) for i in range(64)]
        for f in as_completed(futures):
            try:
                results.append(f.result())
            except Exception as exc:
                errors.append(exc)

    assert not errors
    assert len(results) == 64
    # Spot-check a few outputs are valid 4-band PNGs
    for b in results[:5]:
        data, prof, ci = _decode_raster(b)
        assert prof["driver"] == "PNG"
        assert prof["count"] == 4
        assert ColorInterp.alpha in ci
