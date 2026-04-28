"""test for async STAC Reader."""

import json
import os
from contextlib import asynccontextmanager
from typing import Any

import attr
import numpy
import pystac
import pytest
from async_geotiff import GeoTIFF
from obstore.store import LocalStore
from rasterio.crs import CRS

from rio_tiler.errors import InvalidAssetName, MissingAssets, TileOutsideBounds
from rio_tiler.experimental.async_stac import AsyncSTACReader as STACReader
from rio_tiler.experimental.geotiff import Reader as GeoTIFFReader
from rio_tiler.models import BandStatistics
from rio_tiler.types import AssetWithOptions

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
STAC_PATH = os.path.join(PREFIX, "stac.json")
STAC_PATH_PROJ = os.path.join(PREFIX, "stac_proj.json")
STAC_PATH_PROJ_2_0 = os.path.join(PREFIX, "stac_proj_2_0.json")
STAC_PATH_PROJ_2_0_ASSETS = os.path.join(PREFIX, "stac_proj_2_0_assets.json")
STAC_GDAL_PATH = os.path.join(PREFIX, "stac_headers.json")
STAC_RASTER_V1_PATH = os.path.join(PREFIX, "stac_raster_v1.json")
STAC_RASTER_PATH = os.path.join(PREFIX, "stac_raster.json")

pytestmark = pytest.mark.asyncio


@asynccontextmanager
async def reader(url: str, *args: Any, prefetch: int = 32768, **kwargs: Any):
    """Async context manager for STACReader."""
    assert url.startswith("http://somewhere-over-the-rainbow.io")
    url = url.replace("http://somewhere-over-the-rainbow.io", "")

    store = LocalStore(PREFIX)
    geotiff = await GeoTIFF.open(url, store=store, prefetch=prefetch)
    async with GeoTIFFReader(geotiff, *args, **kwargs) as src:
        yield src


@attr.s
class AsyncSTACReader(STACReader):
    """Custom Async STAC Reader."""

    def _get_options(
        self,
        asset: AssetWithOptions,
        metadata: pystac.Asset,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        method_options: dict[str, Any] = {}
        reader_options: dict[str, Any] = {}

        if head := metadata.extra_fields.get("file:header_size"):
            reader_options["prefetch"] = head

        # Indexes
        if indexes := asset.get("indexes"):
            method_options["indexes"] = indexes
        # Expression
        if expr := asset.get("expression"):
            method_options["expression"] = expr
        # Bands
        if bands := asset.get("bands"):
            stac_bands = (
                metadata.extra_fields.get("bands")
                or metadata.extra_fields.get("eo:bands")  # V1.0
            )
            if not stac_bands:
                raise ValueError(
                    "Asset does not have 'bands' metadata, unable to use 'bands' option"
                )

            # There is no standard for precedence between 'eo:common_name' and 'name'
            # in STAC specification, so we will use 'eo:common_name' if it exists,
            # otherwise fallback to 'name', and if not exist use the band index as last resource.
            common_to_variable = {
                b.get("eo:common_name") or b.get("common_name") or b.get("name") or ix: ix
                for ix, b in enumerate(stac_bands, 1)
            }
            band_indexes: list[int] = []
            for b in bands:
                if idx := common_to_variable.get(b):
                    band_indexes.append(idx)
                else:
                    raise ValueError(
                        f"Band '{b}' not found in asset metadata, unable to use 'bands' option"
                    )

                method_options["indexes"] = band_indexes

        return reader_options, method_options


async def test_projection_extension():
    """Test STAC with the projection extension."""
    item = json.loads(open(STAC_PATH_PROJ).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        assert stac.minzoom == 6
        assert stac.maxzoom == 7
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)

    item = json.loads(open(STAC_PATH_PROJ_2_0).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        assert stac.minzoom == 6
        assert stac.maxzoom == 7
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)

    item = json.loads(open(STAC_PATH_PROJ_2_0_ASSETS).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        assert stac.minzoom == 6
        assert stac.maxzoom == 7
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)

    item = json.loads(open(STAC_PATH_PROJ).read())
    async with AsyncSTACReader(input=item, reader=reader, minzoom=4, maxzoom=8) as stac:
        assert stac.minzoom == 4
        assert stac.maxzoom == 8
        assert stac.bounds
        assert stac.crs == CRS.from_epsg(32617)


async def test_tile_valid():
    """Should raise or return tiles."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(TileOutsideBounds):
            await stac.tile(701, 102, 8, assets="green")

        with pytest.raises(InvalidAssetName):
            await stac.tile(71, 102, 8, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            await stac.tile(71, 102, 8)

        img = await stac.tile(71, 102, 8, assets="green")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green_b1"]

        imge = await stac.tile(71, 102, 8, assets={"name": "green", "expression": "b1*2"})
        assert imge.band_descriptions == ["green_b1*2"]
        numpy.array_equal(imge.array, img.array * 2)

        imge = await stac.tile(
            71, 102, 8, assets={"name": "green", "expression": "b1*2"}, asset_as_band=True
        )
        # NOTE: We can't keep track of the sub-expression in band description when asset_as_band=True
        assert imge.band_descriptions == ["green"]
        numpy.array_equal(imge.array, img.array * 2)

        img = await stac.tile(71, 102, 8, assets=("green",))
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green_b1"]

        img = await stac.tile(71, 102, 8, assets="green", asset_as_band=True)
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green"]

        img = await stac.tile(71, 102, 8, assets=("green", "red"))
        assert img.data.shape == (2, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1", "b2"]
        assert img.band_descriptions == ["green_b1", "red_b1"]

        img = await stac.tile(71, 102, 8, assets=("green", "red"), expression="b1/b2")
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green_b1/red_b1"]

        img = await stac.tile(
            71, 102, 8, assets=("green", "red"), expression="b1/b2", asset_as_band=True
        )
        assert img.data.shape == (1, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green/red"]

        img = await stac.tile(
            71,
            102,
            8,
            assets=(
                {"name": "green", "indexes": [1, 1]},
                {"name": "red", "indexes": [1]},
            ),
        )
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_names == ["b1", "b2", "b3"]
        assert img.band_descriptions == ["green_b1", "green_b1", "red_b1"]

        img = await stac.tile(
            71,
            102,
            8,
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
        )
        assert img.data.shape == (3, 256, 256)
        assert img.mask.shape == (256, 256)
        assert img.band_descriptions == ["green_b1*2", "green_b1", "red_b1*2"]


async def test_part_valid():
    """Should raise or return data."""
    bbox = (-80.477, 32.7988, -79.737, 33.4453)
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.part(bbox, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            await stac.part(bbox)

        img = await stac.part(bbox, assets="green")
        assert img.data.shape == (1, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green_b1"]

        img = await stac.part(bbox, assets="green", asset_as_band=True)
        assert img.data.shape == (1, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green"]

        img = await stac.part(bbox, assets=("green",))
        assert img.data.shape == (1, 74, 85)
        assert img.mask.shape == (74, 85)

        img = await stac.part(bbox, assets=["green", "red"], expression="b1/b2")
        assert img.data.shape == (1, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green_b1/red_b1"]

        img = await stac.part(
            bbox, assets=["green", "red"], expression="b1/b2", asset_as_band=True
        )
        assert img.data.shape == (1, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green/red"]

        img = await stac.part(bbox, assets="green", max_size=30)
        assert img.data.shape == (1, 27, 30)
        assert img.mask.shape == (27, 30)
        assert img.band_descriptions == ["green_b1"]

        img = await stac.part(
            bbox,
            assets=(
                {"name": "green", "indexes": [1, 1]},
                {"name": "red", "indexes": [1]},
            ),
        )
        assert img.data.shape == (3, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green_b1", "green_b1", "red_b1"]

        img = await stac.part(
            bbox,
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
        )
        assert img.data.shape == (3, 74, 85)
        assert img.mask.shape == (74, 85)
        assert img.band_descriptions == ["green_b1*2", "green_b1", "red_b1*2"]


async def test_preview_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.preview(assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            await stac.preview()

        img = await stac.preview(assets="green")
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green_b1"]

        img = await stac.preview(assets="green", asset_as_band=True)
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["green"]

        img = await stac.preview(assets=("green",))
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)

        img = await stac.preview(assets=("green", "red"), expression="b1/b2")
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_descriptions == ["green_b1/red_b1"]

        img = await stac.preview(
            assets=("green", "red"), expression="b1/b2", asset_as_band=True
        )
        assert img.data.shape == (1, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_descriptions == ["green/red"]

        img = await stac.preview(
            assets=(
                {"name": "green", "indexes": [1, 1]},
                {"name": "red", "indexes": [1]},
            ),
        )
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_descriptions == ["green_b1", "green_b1", "red_b1"]

        img = await stac.preview(
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
        )
        assert img.data.shape == (3, 259, 255)
        assert img.mask.shape == (259, 255)
        assert img.band_descriptions == ["green_b1*2", "green_b1", "red_b1*2"]


async def test_point_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.point(-80.477, 33.4453, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            await stac.point(-80.477, 33.4453)

        pt = await stac.point(-80.477, 33.4453, assets="green")
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["green_b1"]

        pt = await stac.point(-80.477, 33.4453, assets="green", asset_as_band=True)
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["green"]

        pt = await stac.point(-80.477, 33.4453, assets=("green",))
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["green_b1"]

        pt = await stac.point(-80.477, 33.4453, assets=("green", "red"))
        assert len(pt.data) == 2
        assert numpy.array_equal(pt.data, numpy.array([7994, 7003]))
        assert pt.band_descriptions == ["green_b1", "red_b1"]

        pt = await stac.point(
            -80.477, 33.4453, assets=("green", "red"), expression="b1/b2"
        )
        assert len(pt.data) == 1
        assert numpy.array_equal(pt.data, numpy.array([7994 / 7003]))
        assert pt.band_descriptions == ["green_b1/red_b1"]

        pt = await stac.point(
            -80.477,
            33.4453,
            assets=("green", "red"),
            expression="b1/b2",
            asset_as_band=True,
        )
        assert pt.band_descriptions == ["green/red"]

        pt = await stac.point(
            -80.477,
            33.4453,
            assets=(
                {"name": "green", "indexes": [1, 1]},
                {"name": "red", "indexes": [1]},
            ),
        )
        assert len(pt.data) == 3
        assert len(pt.mask) == 1
        assert numpy.array_equal(pt.data, numpy.array([7994, 7994, 7003]))
        assert pt.band_descriptions == ["green_b1", "green_b1", "red_b1"]

        pt = await stac.point(
            -80.477,
            33.4453,
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
        )
        assert len(pt.data) == 3
        assert len(pt.mask) == 1
        assert pt.band_descriptions == ["green_b1*2", "green_b1", "red_b1*2"]


async def test_statistics_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.statistics(assets="vert")

        stats = await stac.statistics(assets="green")
        assert stats["green"]
        assert isinstance(stats["green"]["b1"], BandStatistics)
        assert stats["green"]["b1"].description == "b1"

        stats = await stac.statistics(assets=("green", "red"), hist_options={"bins": 20})
        assert len(stats) == 2
        assert len(stats["green"]["b1"].histogram[0]) == 20

        # Check that asset_expression is passed
        stats = await stac.statistics(
            assets=(
                {"name": "green", "expression": "b1*2"},
                {"name": "red", "expression": "b1+100"},
            ),
        )
        assert stats["green|expression=b1*2"]
        assert isinstance(stats["green|expression=b1*2"]["b1"], BandStatistics)
        assert stats["green|expression=b1*2"]["b1"].description == "b1*2"
        assert isinstance(stats["red|expression=b1+100"]["b1"], BandStatistics)
        assert stats["red|expression=b1+100"]["b1"].description == "b1+100"

        stats = await stac.statistics(
            assets=(
                {"name": "green", "indexes": 1},
                {"name": "red", "indexes": 1},
            ),
        )
        assert stats["green|indexes=1"]
        assert isinstance(stats["green|indexes=1"]["b1"], BandStatistics)
        assert isinstance(stats["red|indexes=1"]["b1"], BandStatistics)

        stats = await stac.statistics(
            assets={"name": "green", "indexes": [1]},
        )
        assert stats["green|indexes=[1]"]


async def test_merged_statistics_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.merged_statistics(assets="vert")

        stats = await stac.merged_statistics(assets="green")
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].description == "green_b1"

        stats = await stac.merged_statistics(
            assets=("green", "red"), hist_options={"bins": 20}
        )
        assert len(stats) == 2
        assert len(stats["b1"].histogram[0]) == 20
        assert len(stats["b2"].histogram[0]) == 20

        stats = await stac.merged_statistics(
            assets=("green", "red"),
            expression="b1*2;b1;b2+100",
        )
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].description == "green_b1*2"
        assert stats["b3"].description == "red_b1+100"

        stats = await stac.merged_statistics(
            assets=("green", "red"),
            expression="b1*2;b1;b2+100",
            asset_as_band=True,
        )
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].description == "green*2"
        assert stats["b3"].description == "red+100"


async def test_info_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.info(assets="vert")

        with pytest.warns(UserWarning):
            meta = await stac.info()
            assert meta["red"]
            assert meta["green"]
            assert meta["blue"]

        meta = await stac.info(assets="green")
        assert meta["green"]

        meta = await stac.info(assets=("green", "red"))
        assert meta["green"]
        assert meta["red"]


async def test_feature_valid():
    """Should raise or return data."""
    item = json.loads(open(STAC_PATH).read())

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

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        with pytest.raises(InvalidAssetName):
            await stac.feature(feat, assets="vert")

        # missing asset/expression
        with pytest.raises(MissingAssets):
            await stac.feature(feat)

        img = await stac.feature(feat, assets="green")
        assert img.data.shape == (1, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green_b1"]

        img = await stac.feature(feat, assets="green", asset_as_band=True)
        assert img.data.shape == (1, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green"]

        img = await stac.feature(feat, assets=("green",))
        assert img.data.shape == (1, 123, 102)
        assert img.mask.shape == (123, 102)

        img = await stac.feature(feat, assets=["green", "red"], expression="b1/b2")
        assert img.data.shape == (1, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green_b1/red_b1"]

        img = await stac.feature(
            feat, assets=["green", "red"], expression="b1/b2", asset_as_band=True
        )
        assert img.band_descriptions == ["green/red"]

        img = await stac.feature(feat, assets="green", max_size=30)
        assert img.data.shape == (1, 30, 25)
        assert img.mask.shape == (30, 25)

        img = await stac.feature(
            feat,
            assets=(
                {"name": "green", "indexes": [1, 1]},
                {"name": "red", "indexes": [1]},
            ),
        )
        assert img.data.shape == (3, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green_b1", "green_b1", "red_b1"]

        img = await stac.feature(
            feat,
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
        )
        assert img.data.shape == (3, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green_b1*2", "green_b1", "red_b1*2"]

        img = await stac.feature(
            feat,
            assets=(
                {"name": "green", "indexes": [1]},
                {"name": "red", "indexes": [1]},
            ),
            expression="b1*2;b1;b2*2",
            asset_as_band=True,
        )
        assert img.data.shape == (3, 123, 102)
        assert img.mask.shape == (123, 102)
        assert img.band_descriptions == ["green*2", "green", "red*2"]


async def test_img_dataset_stats():
    """Make sure dataset statistics are forwarded."""
    item = json.loads(open(STAC_PATH).read())

    async with AsyncSTACReader(input=item, reader=reader) as stac:
        img = await stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]

        img = await stac.preview(
            assets=[{"name": "green"}, {"name": "red"}],
        )
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]

        img = await stac.preview(
            assets=[{"name": "green", "indexes": [1, 1, 1]}, {"name": "red"}],
        )
        assert img.dataset_statistics == [
            (6883, 62785),
            (6883, 62785),
            (6883, 62785),
            (6101, 65035),
        ]

        img = await stac.preview(
            assets=[{"name": "green", "expression": "b1"}, {"name": "red"}],
        )
        assert img.dataset_statistics == [
            (6883.0, 62785.0),
            (6101.0, 65035.0),
        ]

        img = await stac.preview(assets=["green", "red"], expression="b1/b2")
        assert img.dataset_statistics == [(6883 / 65035, 62785 / 6101)]


async def test_metadata_from_stac():
    """Make sure dataset statistics are forwarded from the raster extension."""
    item = json.loads(open(STAC_RASTER_V1_PATH).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        info = stac._get_asset_info("green")
        assert info["dataset_statistics"] == [(6883, 62785)]
        assert info["metadata"]
        assert "raster:bands" in info["metadata"]

        img = await stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]
        assert img.metadata["red"]["raster:bands"]
        assert img.metadata["green"]

        img = await stac.preview(assets=[{"name": "green", "indexes": [1, 1]}])
        assert img.dataset_statistics == [(6883, 62785), (6883, 62785)]

        img = await stac.preview(assets=["green", "red"], expression="b1/b2")
        assert img.dataset_statistics == [(6883 / 65035, 62785 / 6101)]
        assert img.metadata["red"]["raster:bands"]
        assert img.metadata["green"]

    item = json.loads(open(STAC_RASTER_PATH).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        info = stac._get_asset_info("green")
        assert info["dataset_statistics"] == [(6883, 62785)]
        assert info["metadata"]
        assert "bands" in info["metadata"]

        img = await stac.preview(assets=("green", "red"))
        assert img.dataset_statistics == [(6883, 62785), (6101, 65035)]

        img = await stac.preview(assets=[{"name": "green", "indexes": [1, 1]}])
        assert img.dataset_statistics == [(6883, 62785), (6883, 62785)]

        img = await stac.preview(assets=[{"name": "green", "bands": ["green"]}])
        assert img.dataset_statistics == [(6883, 62785)]


async def test_reader_setting():
    """Test Env settings."""
    item = json.loads(open(STAC_GDAL_PATH).read())
    async with AsyncSTACReader(input=item, reader=reader) as stac:
        info = stac._get_asset_info("red")
        assert info["reader_options"]["prefetch"] == 50000

        info = await stac.info(assets="red")
        assert info["red"]
