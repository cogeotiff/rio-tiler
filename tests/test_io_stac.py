"""tests rio_tiler.io.stac"""

import json
import os
from unittest.mock import patch

import pytest
import rasterio

from rio_tiler.errors import (
    ExpressionMixingWarning,
    InvalidAssetName,
    MissingAssets,
    TileOutsideBounds,
)
from rio_tiler.io import STACReader
from rio_tiler.models import BandStatistics

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
STAC_PATH = os.path.join(PREFIX, "stac.json")
STAC_REL_PATH = os.path.join(PREFIX, "stac_relative.json")

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
    # Local path
    with STACReader(STAC_PATH) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 24
        assert stac.bounds
        assert stac.filepath == STAC_PATH
        assert stac.assets == ["red", "green", "blue"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Load from dict
    with STACReader(None, item=item) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 24
        assert not stac.filepath
        assert stac.assets == ["red", "green", "blue"]
    httpx.assert_not_called()
    s3_get.assert_not_called()

    # Exclude red
    with STACReader(STAC_PATH, exclude_assets={"red"}) as stac:
        assert stac.assets == ["green", "blue"]
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

    with open(STAC_PATH, "r") as f:
        httpx.get.return_value = MockResponse(f.read())

    with STACReader("http://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue"]
    httpx.get.assert_called_once()
    s3_get.assert_not_called()
    httpx.mock_reset()

    # S3
    with open(STAC_PATH, "r") as f:
        s3_get.return_value = f.read()

    with STACReader("s3://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue"]
    httpx.assert_not_called()
    s3_get.assert_called_once()
    assert s3_get.call_args[0] == ("somewhereovertherainbow.io", "mystac.json")


@patch("rio_tiler.io.cogeo.rasterio")
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
        assert img.band_names == ["green_1"]

        data, mask = stac.tile(71, 102, 8, assets=("green",))
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)

        img = stac.tile(71, 102, 8, expression="green/red")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        # Note: Here we loose the information about the band
        assert img.band_names == ["green/red"]

        with pytest.warns(ExpressionMixingWarning):
            img = stac.tile(71, 102, 8, assets=("green", "red"), expression="green/red")
            assert img.data.shape == (1, 256, 256)
            assert img.band_names == ["green/red"]

        img = stac.tile(
            71,
            102,
            8,
            assets=("green", "red"),
            asset_indexes={"green": (1, 1,), "red": 1},
        )
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_1", "green_1", "red_1"]

        img = stac.tile(
            71,
            102,
            8,
            assets=("green", "red"),
            asset_expression={"green": "b1*2,b1", "red": "b1*2"},
        )
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.cogeo.rasterio")
def test_part_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    bbox = (-80.477, 33.4453, -79.737, 32.7988)

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.part(bbox, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.part(bbox)

        img = stac.part(bbox, assets="green")
        assert img.data.shape == (1, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_1"]

        data, mask = stac.part(bbox, assets=("green",))
        assert data.shape == (1, 73, 83)
        assert mask.shape == (73, 83)

        img = stac.part(bbox, expression="green/red")
        assert img.data.shape == (1, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green/red"]

        data, mask = stac.part(bbox, assets="green", max_size=30)
        assert data.shape == (1, 27, 30)
        assert mask.shape == (27, 30)

        with pytest.warns(ExpressionMixingWarning):
            img = stac.part(bbox, assets=("green", "red"), expression="green/red")
            assert img.data.shape == (1, 73, 83)
            assert img.band_names == ["green/red"]

        img = stac.part(
            bbox, assets=("green", "red"), asset_indexes={"green": (1, 1,), "red": 1}
        )
        assert img.data.shape == (3, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_1", "green_1", "red_1"]

        img = stac.part(
            bbox,
            assets=("green", "red"),
            asset_expression={"green": "b1*2,b1", "red": "b1*2"},
        )
        assert img.data.shape == (3, 73, 83)
        assert img.mask.shape == (73, 83)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.cogeo.rasterio")
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
        assert img.band_names == ["green_1"]

        data, mask = stac.preview(assets=("green",))
        assert data.shape == (1, 259, 255)
        assert mask.shape == (259, 255)

        img = stac.preview(expression="green/red")
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green/red"]

        with pytest.warns(ExpressionMixingWarning):
            img = stac.preview(assets=("green", "red"), expression="green/red")
            assert img.data.shape == (1, 259, 255)
            assert img.band_names == ["green/red"]

        img = stac.preview(
            assets=("green", "red"), asset_indexes={"green": (1, 1,), "red": 1}
        )
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_1", "green_1", "red_1"]

        img = stac.preview(
            assets=("green", "red"),
            asset_expression={"green": "b1*2,b1", "red": "b1*2"},
        )
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


@patch("rio_tiler.io.cogeo.rasterio")
def test_point_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.point(-80.477, 33.4453, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            stac.point(-80.477, 33.4453)

        data = stac.point(-80.477, 33.4453, assets="green")
        assert len(data) == 1

        data = stac.point(-80.477, 33.4453, assets=("green",))
        assert len(data) == 1

        data = stac.point(-80.477, 33.4453, expression="green/red")
        assert len(data) == 1

        with pytest.warns(ExpressionMixingWarning):
            data = stac.point(
                -80.477, 33.4453, assets=("green", "red"), expression="green/red"
            )
            assert len(data) == 1

        data = stac.point(
            -80.477,
            33.4453,
            assets=("green", "red"),
            asset_indexes={"green": (1, 1), "red": 1},
        )
        assert len(data) == 2
        assert len(data[0]) == 2
        assert len(data[1]) == 1

        data = stac.point(
            -80.477,
            33.4453,
            assets=("green", "red"),
            asset_expression={"green": "b1*2,b1", "red": "b1*2"},
        )
        assert len(data) == 2
        assert len(data[0]) == 2
        assert len(data[1]) == 1


@patch("rio_tiler.io.cogeo.rasterio")
def test_stats_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(InvalidAssetName):
                stac.stats(assets="vert")

        with pytest.warns(DeprecationWarning):
            stats = stac.stats(assets="green")
            assert stats["green"]
            assert stats["green"]["1"]["percentiles"]
            assert stats["green"]["1"].percentiles

        with pytest.warns(DeprecationWarning):
            stats = stac.stats(assets=("green", "red"), hist_options={"bins": 20})
            assert len(stats["green"]["1"]["histogram"][0]) == 20
            assert stats["red"]


@patch("rio_tiler.io.cogeo.rasterio")
def test_statistics_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(MissingAssets):
            stac.statistics()

        with pytest.raises(InvalidAssetName):
            stac.statistics(assets="vert")

        stats = stac.statistics(assets="green")
        assert stats["green"]
        assert isinstance(stats["green"]["1"], BandStatistics)

        stats = stac.statistics(assets=("green", "red"), hist_options={"bins": 20})
        assert len(stats) == 2
        assert len(stats["green"]["1"]["histogram"][0]) == 20

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
        assert isinstance(stats["green"]["1"], BandStatistics)
        assert isinstance(stats["red"]["1"], BandStatistics)


@patch("rio_tiler.io.cogeo.rasterio")
def test_info_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.info(assets="vert")

        meta = stac.info(assets="green")
        assert meta["green"]

        meta = stac.info(assets=("green", "red"))
        assert meta["green"]
        assert meta["red"]


@patch("rio_tiler.io.cogeo.rasterio")
def test_metadata_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(InvalidAssetName):
                stac.metadata(assets="vert")

        with pytest.warns(DeprecationWarning):
            meta = stac.metadata(assets="green")
            assert meta["green"]

        with pytest.warns(DeprecationWarning):
            meta = stac.metadata(assets=("green", "red"))
            assert meta["green"]
            assert meta["red"]


def test_parse_expression():
    """."""
    with STACReader(STAC_PATH) as stac:
        assert sorted(stac.parse_expression("green*red+red/blue+2.0")) == [
            "blue",
            "green",
            "red",
        ]


@patch("rio_tiler.io.cogeo.rasterio")
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
        assert img.band_names == ["green_1"]

        data, mask = stac.feature(feat, assets=("green",))
        assert data.shape == (1, 118, 96)
        assert mask.shape == (118, 96)

        img = stac.feature(feat, expression="green/red")
        assert img.data.shape == (1, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green/red"]

        data, mask = stac.feature(feat, assets="green", max_size=30)
        assert data.shape == (1, 30, 25)
        assert mask.shape == (30, 25)

        with pytest.warns(ExpressionMixingWarning):
            img = stac.feature(feat, assets=("green", "red"), expression="green/red")
            assert img.data.shape == (1, 118, 96)
            assert img.band_names == ["green/red"]

        img = stac.feature(
            feat, assets=("green", "red"), asset_indexes={"green": (1, 1), "red": 1}
        )
        assert img.data.shape == (3, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_1", "green_1", "red_1"]

        img = stac.feature(
            feat,
            assets=("green", "red"),
            asset_expression={"green": "b1*2,b1", "red": "b1*2"},
        )
        assert img.data.shape == (3, 118, 96)
        assert img.mask.shape == (118, 96)
        assert img.band_names == ["green_b1*2", "green_b1", "red_b1*2"]


def test_relative_assets():
    """Should return absolute href for assets"""
    with STACReader(STAC_REL_PATH) as stac:
        for (key, asset) in stac.item.assets.items():
            assert asset.get_absolute_href().startswith(PREFIX)
        assert len(stac.assets) == 5

        for asset in stac.assets:
            assert stac._get_asset_url(asset).startswith(PREFIX)


@patch("rio_tiler.io.stac.aws_get_object")
@patch("rio_tiler.io.stac.httpx")
def test_fetch_stac_client_options(httpx, s3_get):
    # HTTP
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return json.loads(self.data)

    with open(STAC_PATH, "r") as f:
        httpx.get.return_value = MockResponse(f.read())

    with STACReader(
        "http://somewhereovertherainbow.io/mystac.json",
        fetch_options={"auth": ("user", "pass")},
    ) as stac:
        assert stac.assets == ["red", "green", "blue"]
    httpx.get.assert_called_once()
    assert httpx.get.call_args[1]["auth"] == ("user", "pass")
    s3_get.assert_not_called()
    httpx.mock_reset()

    # S3
    with open(STAC_PATH, "r") as f:
        s3_get.return_value = f.read()

    with STACReader(
        "s3://somewhereovertherainbow.io/mystac.json",
        fetch_options={"request_pays": True},
    ) as stac:
        assert stac.assets == ["red", "green", "blue"]
    httpx.assert_not_called()
    s3_get.assert_called_once()
    assert s3_get.call_args[1]["request_pays"]
    assert s3_get.call_args[0] == ("somewhereovertherainbow.io", "mystac.json")
