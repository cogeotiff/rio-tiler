"""tests rio_tiler.io.stac"""

import json
import os
import sys
from typing import Dict, List, Set, Tuple, Type
from unittest.mock import patch

import attr
import morecantile
import numpy
import pytest
import rasterio
import xarray
from morecantile import TileMatrixSet
from rasterio._env import get_gdal_config
from rasterio.crs import CRS

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import (
    AssetAsBandError,
    ExpressionMixingWarning,
    InvalidAssetName,
    InvalidExpression,
    MissingAssets,
    TileOutsideBounds,
)
from rio_tiler.io import BaseReader, Reader, STACReader, XarrayReader
from rio_tiler.io.stac import DEFAULT_VALID_TYPE
from rio_tiler.models import BandStatistics
from rio_tiler.types import AssetInfo

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
STAC_PATH = os.path.join(PREFIX, "stac.json")
STAC_PATH_PROJ = os.path.join(PREFIX, "stac_proj.json")
STAC_REL_PATH = os.path.join(PREFIX, "stac_relative.json")
STAC_GDAL_PATH = os.path.join(PREFIX, "stac_headers.json")
STAC_RASTER_PATH = os.path.join(PREFIX, "stac_raster.json")
STAC_WRONGSTATS_PATH = os.path.join(PREFIX, "stac_wrong_stats.json")
STAC_ALTERNATE_PATH = os.path.join(PREFIX, "stac_alternate.json")
STAC_GRIB_PATH = os.path.join(PREFIX, "stac_grib.json")
STAC_NETCDF_PATH = os.path.join(PREFIX, "stac_netcdf.json")

with open(STAC_PATH) as f:
    item = json.loads(f.read())


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("http://somewhere-over-the-rainbow.io")
    asset = asset.replace("http://somewhere-over-the-rainbow.io", PREFIX)
    return rasterio.open(asset)


@patch("rio_tiler.io.stac.aws_get_object")
@patch("rio_tiler.io.stac.httpx")
def test_fetch_stac(httpx, s3_get):
    """Test STACReader."""
    # Local path
    with STACReader(STAC_PATH) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 24
        assert stac.bounds
        assert stac.input == STAC_PATH
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    with STACReader(STAC_PATH, tms=morecantile.tms.get("GNOSISGlobalGrid")) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 28
        assert stac.bounds

    with STACReader(STAC_PATH, minzoom=4, maxzoom=8) as stac:
        assert stac.minzoom == 4
        assert stac.maxzoom == 8
        assert stac.bounds

    # Load from dict
    with STACReader(None, item=item) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 24
        assert not stac.input
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Exclude red
    with STACReader(STAC_PATH, exclude_assets={"red"}) as stac:
        assert stac.assets == ["green", "blue", "lowres"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Only include red asset
    with STACReader(STAC_PATH, include_assets={"red"}) as stac:
        assert stac.assets == ["red"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Only include png
    with STACReader(STAC_PATH, include_asset_types={"image/png"}) as stac:
        assert "thumbnail" in stac.assets
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Include assets/types
    with STACReader(
        STAC_PATH,
        include_assets={"thumbnail", "overview"},
        include_asset_types={"image/png"},
    ) as stac:
        assert stac.assets == ["thumbnail"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # No valid assets
    with pytest.raises(MissingAssets):
        with STACReader(STAC_PATH, include_assets={"B1"}) as stac:
            pass
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # HTTP
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return json.loads(self.data)

        def raise_for_status(self):
            return True

    with open(STAC_PATH, "r") as f:
        httpx.get.return_value = MockResponse(f.read())

    with STACReader("http://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.get.assert_called_once()
    s3_get.assert_not_called()
    httpx.mock_reset()

    # S3
    with open(STAC_PATH, "r") as f:
        s3_get.return_value = f.read()

    with STACReader("s3://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.assert_not_called()
    s3_get.assert_called_once()
    assert s3_get.call_args[0] == ("somewhereovertherainbow.io", "mystac.json")


@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9 or higher")
def test_projection_extension():
    """Test STAC with the projection extension."""
    with STACReader(STAC_PATH_PROJ) as stac:
        assert stac.minzoom == 6
        assert stac.maxzoom == 7
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)

    with STACReader(STAC_PATH_PROJ, minzoom=4, maxzoom=8) as stac:
        assert stac.minzoom == 4
        assert stac.maxzoom == 8
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)


@patch("rio_tiler.io.rasterio.rasterio")
def test_tile_valid(rio):
    """Should raise or return tiles."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(TileOutsideBounds):
            stac.tile(701, 102, 8, assets="green")

        with pytest.raises(InvalidAssetName):
            stac.tile(71, 102, 8, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.tile(71, 102, 8)

        img = stac.tile(71, 102, 8, assets="green")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1"]

        img = stac.tile(71, 102, 8, assets=("green",))
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1"]

        img = stac.tile(71, 102, 8, assets=("green", "red"))
        assert img.data.shape == (2, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1", "red_b1"]

        img = stac.tile(71, 102, 8, expression="green_b1/red_b1")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1/red_b1"]

        with pytest.warns(ExpressionMixingWarning):
            img = stac.tile(
                71, 102, 8, assets=("green", "red"), expression="green_b1/red_b1"
            )
            assert img.data.shape == (1, 256, 256)
            assert img.band_names == ["green_b1/red_b1"]

        img = stac.tile(
            71,
            102,
            8,
            assets=("green", "red"),
            asset_indexes={
                "green": (
                    1,
                    1,
                ),
                "red": 1,
            },
        )
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1", "green_b1", "red_b1"]

        # check backward compatibility for `indexes`
        img = stac.tile(
            71,
            102,
            8,
            assets=("green", "red"),
            indexes=(1, 1),
        )
        assert img.data.shape == (4, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1", "green_b1", "red_b1", "red_b1"]

        # check that indexes and asset_indexes are not conflicting
        img = stac.tile(
            71,
            102,
            8,
            assets=("green", "red"),
            indexes=None,
            asset_indexes={
                "green": (1,),
                "red": 1,
            },
        )
        assert img.data.shape == (2, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1", "red_b1"]

        img = stac.tile(71, 102, 8, expression="green_b1*2;green_b1;red_b1*2")
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]

        # Should raise KeyError because of missing band 2
        with pytest.raises(InvalidExpression):
            img = stac.tile(
                71,
                102,
                8,
                expression="green_b1/red_b2",
                asset_indexes={"green": 1, "red": 1},
            )


@patch("rio_tiler.io.rasterio.rasterio")
def test_part_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    bbox = (-80.477, 32.7988, -79.737, 33.4453)

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.part(bbox, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.part(bbox)

        img = stac.part(bbox, assets="green")
        assert img.data.shape == (1, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1"]

        img = stac.part(bbox, assets=("green",))
        assert img.data.shape == (1, 73, 83)
        assert img.mask.shape == (73, 83)

        img = stac.part(bbox, expression="green_b1/red_b1")
        assert img.data.shape == (1, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1/red_b1"]

        img = stac.part(bbox, assets="green", max_size=30)
        assert img.data.shape == (1, 27, 30)
        assert img.mask.shape == (27, 30)

        with pytest.warns(ExpressionMixingWarning):
            img = stac.part(bbox, assets=("green", "red"), expression="green_b1/red_b1")
            assert img.data.shape == (1, 73, 83)
            assert img.band_names == ["green_b1/red_b1"]

        img = stac.part(
            bbox,
            assets=("green", "red"),
            asset_indexes={
                "green": (
                    1,
                    1,
                ),
                "red": 1,
            },
        )
        assert img.data.shape == (3, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1", "green_b1", "red_b1"]

        img = stac.part(bbox, assets=("green", "red"), indexes=1)
        assert img.data.shape == (2, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1", "red_b1"]

        img = stac.part(bbox, expression="green_b1*2;green_b1;red_b1*2")
        assert img.data.shape == (3, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.rasterio.rasterio")
def test_preview_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.preview(assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.preview()

        img = stac.preview(assets="green")
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1"]

        img = stac.preview(assets=("green",))
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)

        img = stac.preview(expression="green_b1/red_b1")
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1/red_b1"]

        with pytest.warns(ExpressionMixingWarning):
            img = stac.preview(assets=("green", "red"), expression="green_b1/red_b1")
            assert img.data.shape == (1, 259, 255)
            assert img.band_names == ["green_b1/red_b1"]

        img = stac.preview(
            assets=("green", "red"),
            asset_indexes={
                "green": (
                    1,
                    1,
                ),
                "red": 1,
            },
        )
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1", "green_b1", "red_b1"]

        img = stac.preview(assets=("green", "red"), indexes=1)
        assert img.data.shape == (2, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1", "red_b1"]

        img = stac.preview(expression="green_b1*2;green_b1;red_b1*2")
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.rasterio.rasterio")
def test_point_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.point(-80.477, 33.4453, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.point(-80.477, 33.4453)

        pt = stac.point(-80.477, 33.4453, assets="green")
        assert len(pt.data) == 1
        assert pt.band_names == ["green_b1"]

        pt = stac.point(-80.477, 33.4453, assets=("green",))
        assert len(pt.data) == 1
        assert pt.band_names == ["green_b1"]

        pt = stac.point(-80.477, 33.4453, assets=("green", "red"))
        assert len(pt.data) == 2
        assert numpy.array_equal(pt.data, numpy.array([7994, 7003]))
        assert pt.band_names == ["green_b1", "red_b1"]

        pt = stac.point(-80.477, 33.4453, expression="green_b1/red_b1")
        assert len(pt.data) == 1
        assert numpy.array_equal(pt.data, numpy.array([7994 / 7003]))
        assert pt.band_names == ["green_b1/red_b1"]

        with pytest.warns(ExpressionMixingWarning):
            pt = stac.point(
                -80.477, 33.4453, assets=("green", "red"), expression="green_b1/red_b1"
            )
            assert len(pt.data) == 1
            assert pt.band_names == ["green_b1/red_b1"]

        pt = stac.point(
            -80.477,
            33.4453,
            assets=("green", "red"),
            asset_indexes={"green": (1, 1), "red": 1},
        )
        assert len(pt.data) == 3
        assert len(pt.mask) == 1
        assert numpy.array_equal(pt.data, numpy.array([7994, 7994, 7003]))
        assert pt.band_names == ["green_b1", "green_b1", "red_b1"]

        pt = stac.point(-80.477, 33.4453, assets=("green", "red"), indexes=1)
        assert len(pt.data) == 2
        assert numpy.array_equal(pt.data, numpy.array([7994, 7003]))
        assert pt.band_names == ["green_b1", "red_b1"]

        pt = stac.point(-80.477, 33.4453, expression="green_b1*2;green_b1;red_b1*2")
        assert len(pt.data) == 3
        assert len(pt.mask) == 1
        assert pt.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.rasterio.rasterio")
def test_statistics_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.warns(UserWarning):
            stats = stac.statistics()
            assert stats["red"]
            assert stats["green"]
            assert stats["blue"]

        with pytest.raises(InvalidAssetName):
            stac.statistics(assets="vert")

        stats = stac.statistics(assets="green")
        assert stats["green"]
        assert isinstance(stats["green"]["b1"], BandStatistics)

        stats = stac.statistics(assets=("green", "red"), hist_options={"bins": 20})
        assert len(stats) == 2
        assert len(stats["green"]["b1"].histogram[0]) == 20

        # Check that asset_expression is passed
        stats = stac.statistics(
            assets=("green", "red"), asset_expression={"green": "b1*2", "red": "b1+100"}
        )
        assert stats["green"]
        assert isinstance(stats["green"]["b1*2"], BandStatistics)
        assert isinstance(stats["red"]["b1+100"], BandStatistics)

        # Check that asset_indexes is passed
        stats = stac.statistics(
            assets=("green", "red"), asset_indexes={"green": 1, "red": 1}
        )
        assert stats["green"]
        assert isinstance(stats["green"]["b1"], BandStatistics)
        assert isinstance(stats["red"]["b1"], BandStatistics)

        # Check that asset_indexes is passed
        stats = stac.statistics(assets=("green", "red"), indexes=1)
        assert stats["green"]
        assert isinstance(stats["green"]["b1"], BandStatistics)
        assert isinstance(stats["red"]["b1"], BandStatistics)


@patch("rio_tiler.io.rasterio.rasterio")
def test_merged_statistics_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.warns(UserWarning):
            stats = stac.merged_statistics()
            assert len(stats) == 4
            assert isinstance(stats["red_b1"], BandStatistics)
            assert stats["red_b1"]
            assert stats["green_b1"]
            assert stats["blue_b1"]

        with pytest.raises(InvalidAssetName):
            stac.merged_statistics(assets="vert")

        stats = stac.merged_statistics(assets="green")
        assert isinstance(stats["green_b1"], BandStatistics)

        stats = stac.merged_statistics(assets=("green", "red"), hist_options={"bins": 20})
        assert len(stats) == 2
        assert len(stats["green_b1"].histogram[0]) == 20
        assert len(stats["red_b1"].histogram[0]) == 20

        stats = stac.merged_statistics(expression="green_b1*2;green_b1;red_b1+100")
        assert isinstance(stats["green_b1*2"], BandStatistics)
        assert isinstance(stats["red_b1+100"], BandStatistics)

        # Check that asset_indexes is passed
        stats = stac.merged_statistics(
            assets=("green", "red"), asset_indexes={"green": 1, "red": 1}
        )
        assert isinstance(stats["green_b1"], BandStatistics)
        assert isinstance(stats["red_b1"], BandStatistics)


@patch("rio_tiler.io.rasterio.rasterio")
def test_info_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.info(assets="vert")

        with pytest.warns(UserWarning):
            meta = stac.info()
            assert meta["red"]
            assert meta["green"]
            assert meta["blue"]

        meta = stac.info(assets="green")
        assert meta["green"]

        meta = stac.info(assets=("green", "red"))
        assert meta["green"]
        assert meta["red"]


def test_parse_expression():
    """Parse assets expressions."""
    with STACReader(STAC_PATH) as stac:
        assert sorted(
            stac.parse_expression("green_b1*red_b1+red_b1/blue_b1+2.0;red_b1")
        ) == [
            "blue",
            "green",
            "red",
        ]

    # make sure we match full word only
    with STACReader(STAC_PATH) as stac:
        assert sorted(
            stac.parse_expression("greenish_b1*red_b1+red_b1/blue_b1+2.0;red_b1")
        ) == ["blue", "red"]

    # make sure we match full word only
    with STACReader(STAC_PATH) as stac:
        assert sorted(
            stac.parse_expression("green_b10foo*red_b1+red_b1/blue_b1+2.0;red_b1")
        ) == ["blue", "red"]

    # raise exception in no assets
    with pytest.raises(InvalidExpression):
        with STACReader(STAC_PATH) as stac:
            stac.parse_expression("greenfoo*redfoo", asset_as_band=True)

    with pytest.raises(InvalidExpression):
        with STACReader(STAC_PATH) as stac:
            stac.parse_expression("greenfoo_b1*2")


@patch("rio_tiler.io.rasterio.rasterio")
def test_feature_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    feat = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-80.013427734375, 33.03169299978312],
                    [-80.3045654296875, 32.588477769459146],
                    [-80.05462646484375, 32.42865847084369],
                    [-79.45037841796875, 32.6093028087336],
                    [-79.47235107421875, 33.43602551072033],
                    [-79.89532470703125, 33.47956309444182],
                    [-80.1068115234375, 33.37870592138779],
                    [-80.30181884765625, 33.27084277265288],
                    [-80.0628662109375, 33.146750228776455],
                    [-80.013427734375, 33.03169299978312],
                ]
            ],
        },
    }

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.feature(feat, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.feature(feat)

        img = stac.feature(feat, assets="green")
        assert img.data.shape == (1, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1"]

        img = stac.feature(feat, assets=("green",))
        assert img.data.shape == (1, 118, 96)
        assert img.mask.shape == (118, 96)

        img = stac.feature(feat, expression="green_b1/red_b1")
        assert img.data.shape == (1, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1/red_b1"]

        img = stac.feature(feat, assets="green", max_size=30)
        assert img.data.shape == (1, 30, 25)
        assert img.mask.shape == (30, 25)

        with pytest.warns(ExpressionMixingWarning):
            img = stac.feature(
                feat, assets=("green", "red"), expression="green_b1/red_b1"
            )
            assert img.data.shape == (1, 118, 96)
            assert img.band_names == ["green_b1/red_b1"]

        img = stac.feature(
            feat, assets=("green", "red"), asset_indexes={"green": (1, 1), "red": 1}
        )
        assert img.data.shape == (3, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1", "green_b1", "red_b1"]

        img = stac.feature(feat, assets=("green", "red"), indexes=1)
        assert img.data.shape == (2, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1", "red_b1"]

        img = stac.feature(feat, expression="green_b1*2;green_b1;red_b1*2")
        assert img.data.shape == (3, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]

        # NOTE: This tests fails every odd time. There is something weird happening with catch_warnings
        # with pytest.warns(
        #     UserWarning,
        #     match="Cannot concatenate images with different size. Will resize using max width/heigh",
        # ):
        img = stac.feature(feat, assets=("blue", "lowres"))
        assert img.data.shape == (2, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["blue_b1", "lowres_b1"]


def test_relative_assets():
    """Should return absolute href for assets"""
    with STACReader(STAC_REL_PATH) as stac:
        for _key, asset in stac.item.assets.items():
            assert asset.get_absolute_href().startswith(PREFIX)
        assert len(stac.assets) == 5

        for asset in stac.assets:
            assert stac._get_asset_info(asset)["url"].startswith(PREFIX)


@patch("rio_tiler.io.stac.aws_get_object")
@patch("rio_tiler.io.stac.httpx")
def test_fetch_stac_client_options(httpx, s3_get):
    """test options forwarding."""

    # HTTP
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return json.loads(self.data)

        def raise_for_status(self):
            return True

    with open(STAC_PATH, "r") as f:
        httpx.get.return_value = MockResponse(f.read())

    with STACReader(
        "http://somewhereovertherainbow.io/mystac.json",
        fetch_options={
            "auth": ("user", "pass"),
            "headers": {"Authorization": "Bearer token"},
        },
    ) as stac:
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.get.assert_called_once()
    assert httpx.get.call_args[1]["auth"] == ("user", "pass")
    assert httpx.get.call_args[1]["headers"] == {"Authorization": "Bearer token"}
    s3_get.assert_not_called()

    with STACReader(
        "http://somewhereovertherainbow.io/mystac.json",
        fetch_options={
            "auth": ("user", "pass"),
            "headers": {"Authorization": "Bearer token"},
        },
    ) as stac:
        assert stac.assets == ["red", "green", "blue", "lowres"]

    # Check if it was cached
    assert httpx.get.call_count == 1
    s3_get.assert_not_called()

    # S3
    with open(STAC_PATH, "r") as f:
        s3_get.return_value = f.read()

    with STACReader(
        "s3://somewhereovertherainbow.io/mystac.json",
        fetch_options={"request_pays": True},
    ) as stac:
        assert stac.assets == ["red", "green", "blue", "lowres"]
    httpx.assert_not_called()
    s3_get.assert_called_once()
    assert s3_get.call_args[1]["request_pays"]
    assert s3_get.call_args[0] == ("somewhereovertherainbow.io", "mystac.json")


@patch("rio_tiler.io.rasterio.rasterio")
def test_img_dataset_stats(rio):
    """Make sure dataset statistics are forwarded."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        img = stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]

        img = stac.preview(expression="green_b1/red_b1")
        assert img.dataset_statistics == [(6883 / 65035, 62785 / 6101)]


@attr.s
class CustomReader(Reader):
    """Custom Reader for STAC."""

    def __attrs_post_init__(self):
        """Post Init."""
        assert get_gdal_config("GDAL_INGESTED_BYTES_AT_OPEN") == 50000
        super().__attrs_post_init__()


def test_gdal_env_setting():
    """Test Env settings."""
    with STACReader(STAC_GDAL_PATH, reader=CustomReader) as stac:
        assert not get_gdal_config("GDAL_INGESTED_BYTES_AT_OPEN") == 50000
        assert stac.preview(assets=["red", "green", "blue"])


@patch("rio_tiler.io.rasterio.rasterio")
def test_asset_as_band(rio):
    """Validate use of asset as band option."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        img = stac.tile(71, 102, 8, assets="green", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green"]

        # Can't use asset_as_band with multiple bands
        with pytest.raises(AssetAsBandError):
            stac.tile(71, 102, 8, assets="green", indexes=(1, 1), asset_as_band=True)

        img = stac.tile(71, 102, 8, expression="green/red", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green/red"]

        bbox = (-80.477, 32.7988, -79.737, 33.4453)
        img = stac.part(bbox, assets="green", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green"]

        with pytest.raises(AssetAsBandError):
            stac.part(bbox, assets="green", indexes=(1, 1), asset_as_band=True)

        img = stac.part(bbox, expression="green/red", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green/red"]

        img = stac.preview(assets="green", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green"]

        with pytest.raises(AssetAsBandError):
            stac.preview(assets="green", indexes=(1, 1), asset_as_band=True)

        img = stac.preview(expression="green/red", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green/red"]

        pt = stac.point(-80.477, 33.4453, assets="green", asset_as_band=True)
        assert len(pt.data) == 1
        assert len(pt.mask) == 1
        assert pt.band_names == ["green"]

        with pytest.raises(AssetAsBandError):
            stac.point(
                -80.477, 33.4453, assets="green", indexes=(1, 1), asset_as_band=True
            )

        pt = stac.point(-80.477, 33.4453, expression="green/red", asset_as_band=True)
        assert len(pt.data) == 1
        assert pt.band_names == ["green/red"]

        feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-80.013427734375, 33.03169299978312],
                        [-80.3045654296875, 32.588477769459146],
                        [-80.05462646484375, 32.42865847084369],
                        [-79.45037841796875, 32.6093028087336],
                        [-79.47235107421875, 33.43602551072033],
                        [-79.89532470703125, 33.47956309444182],
                        [-80.1068115234375, 33.37870592138779],
                        [-80.30181884765625, 33.27084277265288],
                        [-80.0628662109375, 33.146750228776455],
                        [-80.013427734375, 33.03169299978312],
                    ]
                ],
            },
        }
        img = stac.feature(feat, assets="green", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green"]

        with pytest.raises(AssetAsBandError):
            stac.feature(feat, assets="green", indexes=(1, 1), asset_as_band=True)

        img = stac.feature(feat, expression="green/red", asset_as_band=True)
        assert img.count == 1
        assert img.band_names == ["green/red"]


@patch("rio_tiler.io.rasterio.rasterio")
def test_metadata_from_stac(rio):
    """Make sure dataset statistics are forwarded from the raster extension."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_RASTER_PATH) as stac:
        info = stac._get_asset_info("green")
        assert info["dataset_statistics"] == [(6883, 62785)]
        assert info["metadata"]
        assert "raster:bands" in info["metadata"]

        img = stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]
        assert img.metadata["red"]["raster:bands"]
        assert img.metadata["green"]

        img = stac.preview(expression="green_b1/red_b1")
        assert img.dataset_statistics == [(6883 / 65035, 62785 / 6101)]
        assert img.metadata["red"]["raster:bands"]
        assert img.metadata["green"]


@patch("rio_tiler.io.rasterio.rasterio")
def test_expression_with_wrong_stac_stats(rio):
    """Should raise or return tiles."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_WRONGSTATS_PATH) as stac:
        img = stac.tile(451, 76, 9, assets="goodstat")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["goodstat_b1"]

        img = stac.tile(
            451, 76, 9, expression="where((goodstat>0.5),1,0)", asset_as_band=True
        )
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["where((goodstat>0.5),1,0)"]

        img = stac.tile(451, 76, 9, assets=("wrongstat",))
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["wrongstat_b1"]

        asset_info = stac._get_asset_info("wrongstat")
        url = asset_info["url"]
        with stac.reader(url, tms=stac.tms, **stac.reader_options) as src:
            img = src.tile(451, 76, 9, expression="where((b1>0.5),1,0)")
            assert img.data.shape == (1, 256, 256)
            assert img.mask.shape == (256, 256)
            assert img.band_names == ["where((b1>0.5),1,0)"]

        with pytest.warns(UserWarning):
            img = stac.tile(
                451,
                76,
                9,
                expression="where((wrongstat>0.5),1,0)",
                asset_as_band=True,
            )


@patch("rio_tiler.io.rasterio.rasterio")
def test_default_assets(rio):
    """Should raise or return tiles."""
    rio.open = mock_rasterio_open

    bbox = (-80.477, 32.7988, -79.737, 33.4453)

    feat = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-80.013427734375, 33.03169299978312],
                    [-80.3045654296875, 32.588477769459146],
                    [-80.05462646484375, 32.42865847084369],
                    [-79.45037841796875, 32.6093028087336],
                    [-79.47235107421875, 33.43602551072033],
                    [-79.89532470703125, 33.47956309444182],
                    [-80.1068115234375, 33.37870592138779],
                    [-80.30181884765625, 33.27084277265288],
                    [-80.0628662109375, 33.146750228776455],
                    [-80.013427734375, 33.03169299978312],
                ]
            ],
        },
    }

    with STACReader(STAC_PATH, default_assets=["green"]) as stac:
        with pytest.warns(UserWarning):
            img = stac.tile(71, 102, 8)
            assert img.data.shape == (1, 256, 256)
            assert img.mask.shape == (256, 256)
            assert img.band_names == ["green_b1"]

        with pytest.warns(UserWarning):
            pt = stac.point(-80.477, 33.4453)
            assert len(pt.data) == 1
            assert pt.band_names == ["green_b1"]

        with pytest.warns(UserWarning):
            img = stac.preview()
            assert img.data.shape == (1, 259, 255)
            assert img.mask.shape == (259, 255)
            assert img.band_names == ["green_b1"]

        with pytest.warns(UserWarning):
            img = stac.part(bbox)
            assert img.data.shape == (1, 73, 83)
            assert img.mask.shape == (73, 83)
            assert img.band_names == ["green_b1"]

        with pytest.warns(UserWarning):
            img = stac.feature(feat)
            assert img.data.shape == (1, 118, 96)
            assert img.mask.shape == (118, 96)
            assert img.band_names == ["green_b1"]


def test_netcdf_reader():
    """Should use the correct reader depending on the media type."""

    @attr.s
    class NetCDFReader(XarrayReader):
        """Reader: Open NetCDF file and access DataArray."""

        src_path: str = attr.ib()
        variable: str = attr.ib()

        tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

        ds: xarray.Dataset = attr.ib(init=False)
        input: xarray.DataArray = attr.ib(init=False)

        _dims: List = attr.ib(init=False, factory=list)

        def __attrs_post_init__(self):
            """Set bounds and CRS."""
            self.ds = xarray.open_dataset(self.src_path, decode_coords="all")
            da = self.ds[self.variable]

            # Make sure we have a valid CRS
            crs = da.rio.crs or "epsg:4326"
            da = da.rio.write_crs(crs)

            if "time" in da.dims:
                da = da.isel(time=0)

            self.input = da

            super().__attrs_post_init__()

    valid_types = {
        "image/tiff; application=geotiff",
        "application/x-netcdf",
    }

    @attr.s
    class CustomSTACReader(STACReader):
        include_asset_types: Set[str] = attr.ib(default=valid_types)

        def _get_reader(self, asset_info: AssetInfo) -> Tuple[Type[BaseReader], Dict]:
            """Get Asset Reader."""
            asset_type = asset_info.get("media_type", None)
            if asset_type and asset_type in [
                "application/x-netcdf",
            ]:
                return NetCDFReader, {}

            return Reader, {}

    with CustomSTACReader(STAC_NETCDF_PATH) as stac:
        assert stac.assets == ["geotiff", "netcdf"]
        info = stac._get_asset_info("netcdf")
        assert info["media_type"] == "application/x-netcdf"
        assert stac._get_reader(info) == (NetCDFReader, {})

        info = stac._get_asset_info("geotiff")
        assert info["media_type"] == "image/tiff; application=geotiff"
        assert stac._get_reader(info) == (Reader, {})

    with CustomSTACReader(
        STAC_NETCDF_PATH, reader_options={"variable": "dataset"}
    ) as stac:
        info = stac.info(assets=["netcdf"])
        assert info["netcdf"].crs

        img = stac.preview(assets=["netcdf"])
        assert img.band_names == ["netcdf_dataset"]


@patch("rio_tiler.io.stac.STAC_ALTERNATE_KEY", "s3")
def test_alternate_assets():
    """Should return the alternate key"""
    with STACReader(STAC_ALTERNATE_PATH) as stac:
        assert stac._get_asset_info("red")["url"].startswith("s3://")
        # fall back to href when alternate doesn't exist
        assert stac._get_asset_info("blue")["url"].startswith("http://")


def test_vrt_string_assets():
    """Should work with VRT connection string"""
    VALID_TYPE = {
        *DEFAULT_VALID_TYPE,
        "application/wmo-GRIB2",
    }

    with STACReader(STAC_GRIB_PATH, include_asset_types=VALID_TYPE) as stac:
        assert stac.assets == ["asset"]
        info = stac._get_asset_info("asset")
        assert info["url"]

        info_vrt = stac._get_asset_info("vrt://asset")
        # without any option there is no need to use the vrt prefix
        assert info["url"] == info_vrt["url"]

        info_vrt = stac._get_asset_info("vrt://asset?bands=1")
        assert not info["url"] == info_vrt["url"]
        assert info_vrt["url"].startswith("vrt://") and info_vrt["url"].endswith(
            "?bands=1"
        )

        with pytest.raises(InvalidAssetName):
            stac._get_asset_info("vrt://somthing?bands=1")

        with pytest.raises(InvalidAssetName):
            stac._get_asset_info("vrt://?bands=1")

        info = stac.info(assets="vrt://asset?bands=1")
        assert info["vrt://asset?bands=1"]
        assert len(info["vrt://asset?bands=1"].band_metadata) == 1

        info = stac.info(assets="vrt://asset?bands=1,2")
        assert info["vrt://asset?bands=1,2"]
        assert len(info["vrt://asset?bands=1,2"].band_metadata) == 2

        img = stac.preview(assets="vrt://asset?bands=1")
        assert img.count == 1
