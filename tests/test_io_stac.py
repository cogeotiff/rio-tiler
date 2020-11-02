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

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
STAC_PATH = os.path.join(PREFIX, "stac.json")

with open(STAC_PATH) as f:
    stac_item = json.loads(f.read())


def mock_rasterio_open(asset):
    """Mock rasterio Open."""
    assert asset.startswith("http://somewhere-over-the-rainbow.io")
    asset = asset.replace("http://somewhere-over-the-rainbow.io", PREFIX)
    return rasterio.open(asset)


@patch("rio_tiler.io.stac.aws_get_object")
@patch("rio_tiler.io.stac.requests")
def test_fetch_stac(requests, s3_get):
    # Local path
    with STACReader(STAC_PATH) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 30
        assert stac.bounds
        assert stac.center
        assert stac.spatial_info
        assert stac.filepath == STAC_PATH
        assert stac.assets == ["red", "green", "blue"]
    requests.assert_not_called()
    s3_get.assert_not_called()

    # Load from dict
    with STACReader(None, item=stac_item) as stac:
        assert stac.minzoom == 0
        assert stac.maxzoom == 30
        assert not stac.filepath
        assert stac.assets == ["red", "green", "blue"]
    requests.assert_not_called()
    s3_get.assert_not_called()

    # Exclude red
    with STACReader(STAC_PATH, exclude_assets={"red"}) as stac:
        assert stac.assets == ["green", "blue"]
    requests.assert_not_called()
    s3_get.assert_not_called()

    # Only include red asset
    with STACReader(STAC_PATH, include_assets={"red"}) as stac:
        assert stac.assets == ["red"]
    requests.assert_not_called()
    s3_get.assert_not_called()

    # Only include png
    with STACReader(STAC_PATH, include_asset_types={"image/png"}) as stac:
        assert "thumbnail" in stac.assets
    requests.assert_not_called()
    s3_get.assert_not_called()

    # Include assets/types
    with STACReader(
        STAC_PATH,
        include_assets={"thumbnail", "overview"},
        include_asset_types={"image/png"},
    ) as stac:
        assert stac.assets == ["thumbnail"]
    requests.assert_not_called()
    s3_get.assert_not_called()

    # No valid assets
    with pytest.raises(MissingAssets):
        with STACReader(STAC_PATH, include_assets={"B1"}) as stac:
            pass
    requests.assert_not_called()
    s3_get.assert_not_called()

    # HTTP
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return json.loads(self.data)

    with open(STAC_PATH, "r") as f:
        requests.get.return_value = MockResponse(f.read())

    with STACReader("http://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue"]
    requests.get.assert_called_once()
    s3_get.assert_not_called()
    requests.mock_reset()

    # S3
    with open(STAC_PATH, "r") as f:
        s3_get.return_value = f.read()

    with STACReader("s3://somewhereovertherainbow.io/mystac.json") as stac:
        assert stac.assets == ["red", "green", "blue"]
    requests.assert_not_called()
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

        data, mask = stac.tile(71, 102, 8, assets="green")
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)

        data, mask = stac.tile(71, 102, 8, assets=("green",))
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)

        data, mask = stac.tile(71, 102, 8, expression="green/red")
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = stac.tile(
                71, 102, 8, assets=("green", "red"), expression="green/red"
            )
            assert data.shape == (1, 256, 256)

        data, mask = stac.tile(
            71, 102, 8, assets=("green", "red"), asset_expression="b1*2,b1"
        )
        assert data.shape == (4, 256, 256)
        assert mask.shape == (256, 256)


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

        data, mask = stac.part(bbox, assets="green")
        assert data.shape == (1, 73, 84)
        assert mask.shape == (73, 84)

        data, mask = stac.part(bbox, assets=("green",))
        assert data.shape == (1, 73, 84)
        assert mask.shape == (73, 84)

        data, mask = stac.part(bbox, expression="green/red")
        assert data.shape == (1, 73, 84)
        assert mask.shape == (73, 84)

        data, mask = stac.part(bbox, assets="green", max_size=30)
        assert data.shape == (1, 27, 30)
        assert mask.shape == (27, 30)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = stac.part(bbox, assets=("green", "red"), expression="green/red")
            assert data.shape == (1, 73, 84)


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

        data, mask = stac.preview(assets="green")
        assert data.shape == (1, 259, 255)
        assert mask.shape == (259, 255)

        data, mask = stac.preview(assets=("green",))
        assert data.shape == (1, 259, 255)
        assert mask.shape == (259, 255)

        data, mask = stac.preview(expression="green/red")
        assert data.shape == (1, 259, 255)
        assert mask.shape == (259, 255)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = stac.preview(assets=("green", "red"), expression="green/red")
            assert data.shape == (1, 259, 255)


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


@patch("rio_tiler.io.cogeo.rasterio")
def test_stats_valid(rio):
    """Should raise or return data."""
    rio.open = mock_rasterio_open

    with STACReader(STAC_PATH) as stac:
        with pytest.raises(InvalidAssetName):
            stac.stats(assets="vert")

        stats = stac.stats(assets="green")
        assert stats["green"]
        assert stats["green"]["1"]["percentiles"]
        assert stats["green"]["1"].percentiles

        stats = stac.stats(assets=("green", "red"), hist_options={"bins": 20})
        assert len(stats["green"]["1"]["histogram"][0]) == 20
        assert stats["red"]


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
        with pytest.raises(InvalidAssetName):
            stac.metadata(assets="vert")

        meta = stac.metadata(assets="green")
        assert meta["green"]

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
