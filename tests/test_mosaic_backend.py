"""test Mosaic Backend."""

import os
from contextlib import asynccontextmanager
from typing import Type

import attr
import numpy
import pytest
from async_geotiff import GeoTIFF
from morecantile import TileMatrixSet
from obstore.store import LocalStore
from rasterio.crs import CRS
from rasterio.warp import transform_geom

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.experimental.geotiff import Reader as GeoTIFFReader
from rio_tiler.io import BaseReader, MultiBaseReader, Reader
from rio_tiler.models import PointData
from rio_tiler.mosaic.backend import AsyncBaseBackend, BaseBackend
from rio_tiler.mosaic.methods import defaults
from rio_tiler.types import BBox

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
asset1 = os.path.join(PREFIX, "mosaic_value_1.tif")
asset2 = os.path.join(PREFIX, "mosaic_value_2.tif")
assets = [asset1, asset2]

store = LocalStore(PREFIX)


def test_backend():
    """Test Backend implementation."""

    @attr.s
    class Backend(BaseBackend):
        """Test Backend implementation."""

        input: list[str] = attr.ib()
        tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

        reader: Type[BaseReader] | Type[MultiBaseReader] = attr.ib(default=Reader)
        reader_options: dict = attr.ib(factory=dict)

        bounds: BBox = attr.ib(init=False)
        crs: CRS = attr.ib(init=False)

        minzoom: int = attr.ib(init=False)
        maxzoom: int = attr.ib(init=False)

        def __attrs_post_init__(self):
            """Post Init."""

            def get_metadata(asset):
                with self.reader(asset, tms=self.tms) as src:
                    return src.bounds, src.crs, src.minzoom, src.maxzoom

            metadata = [get_metadata(asset) for asset in self.input]
            crs = {m[1] for m in metadata}
            if len(crs) != 1:
                raise ValueError("Mosaic assets must have the same CRS")
            self.crs = crs.pop()
            self.minzoom = min([m[2] for m in metadata])
            self.maxzoom = max([m[3] for m in metadata])

            minx, miny, maxx, maxy = zip(*[m[0] for m in metadata])
            self.bounds = [min(minx), min(miny), max(maxx), max(maxy)]

        def assets_for_tile(self, x: int, y: int, z: int, **kwargs) -> list[str]:
            """Retrieve assets for tile."""
            return self.input

        def assets_for_point(
            self,
            lng: float,
            lat: float,
            coord_crs: CRS | None = None,
            **kwargs,
        ) -> list[str]:
            """Retrieve assets for point."""
            return self.input

        def assets_for_bbox(
            self,
            left: float,
            bottom: float,
            right: float,
            top: float,
            coord_crs: CRS | None = None,
            **kwargs,
        ) -> list[str]:
            """Retrieve assets for bbox."""
            return self.input

    with Backend(input=assets, reader=Reader) as backend:
        assert backend.bounds == [
            425085.0,
            4978484.791159676,
            778214.785735938,
            5216115.0,
        ]
        assert backend.crs == CRS.from_epsg(32618)
        assert backend.minzoom == 7
        assert backend.maxzoom == 9

        # Full covered tile
        # fully covering mosaic_value_1 an partially covering mosaic_value_2
        x = 150
        y = 182
        z = 9

        img, assets_used = backend.tile(x, y, z, pixel_selection=defaults.MeanMethod)
        assert img.array.shape == (3, 256, 256)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        with pytest.warns(UserWarning):
            img, assets_used = backend.tile(x, y, z, pixel_selection=defaults.MeanMethod)
            bbox = list(backend.tms.bounds(x, y, z))
            img, assets_used = backend.part(
                bbox,
                bounds_crs="epsg:4326",
                dst_crs="epsg:4326",
                max_size=256,
                pixel_selection=defaults.MeanMethod,
            )
        assert img.crs == CRS.from_epsg(4326)
        assert img.array.shape == (3, 147, 211)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        lon, lat = -73.69990294755982, 45.49950291143219
        point_values = backend.point(lon, lat, coord_crs=CRS.from_epsg(4326))
        assert len(point_values) == 2
        assert isinstance(point_values[0][0], str)
        assert isinstance(point_values[0][1], PointData)

        feat = {
            "type": "Polygon",
            "coordinates": [
                [
                    [-74.5312500000003, 45.583289756006614],
                    [-74.5312500000003, 46.073230625408655],
                    [-73.82812500000036, 46.073230625408655],
                    [-73.82812500000036, 45.583289756006614],
                    [-74.5312500000003, 45.583289756006614],
                ]
            ],
        }

        with pytest.warns(
            UserWarning, match="Cannot concatenate images with different sizes"
        ):
            img, assets_used = backend.feature(
                feat,
                shape_crs=CRS.from_epsg(4326),
                max_size=256,
                pixel_selection=defaults.MeanMethod,
            )
        assert img.crs == CRS.from_epsg(4326)
        assert img.array.shape == (3, 147, 211)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        # test with mismatched dst_crs and shape_crs
        feat_utm = transform_geom(CRS.from_epsg(4326), CRS.from_epsg(32618), feat)

        with pytest.warns(
            UserWarning, match="Cannot concatenate images with different sizes"
        ):
            img_utm, _ = backend.feature(
                feat_utm,
                shape_crs=CRS.from_epsg(32618),
                dst_crs=CRS.from_epsg(4326),
                max_size=256,
                pixel_selection=defaults.MeanMethod,
            )
        assert img_utm.crs == CRS.from_epsg(4326)
        assert not img_utm.array.mask.all()

        cpx_shape = {
            "type": "Polygon",
            "coordinates": [
                [
                    [-73.859945763944708, 47.392667290910126],
                    [-74.833824877214042, 46.822591712410997],
                    [-74.746729997165559, 45.801206300933401],
                    [-73.820357182104487, 45.690358271780795],
                    [-72.75146547241863, 45.935807479190139],
                    [-72.878148934307319, 47.09971178529252],
                    [-73.772850883896226, 46.624648803209915],
                    [-73.772850883896226, 46.624648803209915],
                    [-73.796604033000364, 46.885933443355349],
                    [-73.677838287479702, 47.250148396285347],
                    [-73.859945763944708, 47.392667290910126],
                ]
            ],
        }
        with pytest.warns(
            UserWarning, match="Cannot concatenate images with different sizes"
        ):
            img_utm, _ = backend.feature(
                cpx_shape,
                shape_crs=CRS.from_epsg(4326),
                pixel_selection=defaults.MeanMethod,
            )
        assert img_utm.crs == CRS.from_epsg(4326)
        assert not img_utm.array.mask.all()
        assert numpy.unique(img_utm.data).tolist() == [0, 1, 2]


@pytest.mark.asyncio
async def test_async_backend():
    """Test Backend implementation."""

    @asynccontextmanager
    async def reader(src_path: str, *args, **kwargs):
        """Read tile from an asset"""
        geotiff = await GeoTIFF.open(os.path.basename(src_path), store=store)
        async with GeoTIFFReader(input=geotiff) as src:
            yield src

    @attr.s
    class ABackend(AsyncBaseBackend):
        """Test Backend implementation."""

        def __attrs_post_init__(self):
            """Post Init."""
            self.bounds = (
                425085.0,
                4978484.791159676,
                778214.785735938,
                5216115.0,
            )
            self.crs = CRS.from_epsg(32618)
            self.minzoom = 7
            self.maxzoom = 9

        async def assets_for_tile(self, x: int, y: int, z: int, **kwargs) -> list[str]:
            """Retrieve assets for tile."""
            return self.input

        async def assets_for_point(
            self,
            lng: float,
            lat: float,
            coord_crs: CRS | None = None,
            **kwargs,
        ) -> list[str]:
            """Retrieve assets for point."""
            return self.input

        async def assets_for_bbox(
            self,
            xmin: float,
            ymin: float,
            xmax: float,
            ymax: float,
            coord_crs: CRS | None = None,
            **kwargs,
        ) -> list[str]:
            """Retrieve assets for bbox."""
            return self.input

    async with ABackend(input=assets, reader=reader) as backend:
        # Full covered tile
        # fully covering mosaic_value_1 an partially covering mosaic_value_2
        x = 150
        y = 182
        z = 9

        img, assets_used = await backend.tile(
            x, y, z, pixel_selection=defaults.MeanMethod
        )
        assert img.array.shape == (3, 256, 256)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        img, assets_used = await backend.tile(
            x, y, z, pixel_selection=defaults.MeanMethod
        )
        bbox = list(backend.tms.bounds(x, y, z))
        img, assets_used = await backend.part(
            bbox,
            bounds_crs="epsg:4326",
            dst_crs="epsg:4326",
            max_size=256,
            pixel_selection=defaults.MeanMethod,
        )

        assert img.crs == CRS.from_epsg(4326)
        assert img.array.shape == (3, 150, 216)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        lon, lat = -73.69990294755982, 45.49950291143219
        point_values = await backend.point(lon, lat, coord_crs=CRS.from_epsg(4326))
        assert len(point_values) == 2
        assert isinstance(point_values[0][0], str)
        assert isinstance(point_values[0][1], PointData)

        feat = {
            "type": "Polygon",
            "coordinates": [
                [
                    [-74.5312500000003, 45.583289756006614],
                    [-74.5312500000003, 46.073230625408655],
                    [-73.82812500000036, 46.073230625408655],
                    [-73.82812500000036, 45.583289756006614],
                    [-74.5312500000003, 45.583289756006614],
                ]
            ],
        }

        img, assets_used = await backend.feature(
            feat,
            shape_crs=CRS.from_epsg(4326),
            max_size=256,
            pixel_selection=defaults.MeanMethod,
        )
        assert img.crs == CRS.from_epsg(4326)
        assert img.array.shape == (3, 150, 216)
        assert set(assets_used) == {asset1, asset2}
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        # test with mismatched dst_crs and shape_crs
        feat_utm = transform_geom(CRS.from_epsg(4326), CRS.from_epsg(32618), feat)

        img_utm, _ = await backend.feature(
            feat_utm,
            shape_crs=CRS.from_epsg(32618),
            dst_crs=CRS.from_epsg(4326),
            max_size=256,
            pixel_selection=defaults.MeanMethod,
        )
        assert img_utm.crs == CRS.from_epsg(4326)
        assert not img_utm.array.mask.all()

        cpx_shape = {
            "type": "Polygon",
            "coordinates": [
                [
                    [-73.859945763944708, 47.392667290910126],
                    [-74.833824877214042, 46.822591712410997],
                    [-74.746729997165559, 45.801206300933401],
                    [-73.820357182104487, 45.690358271780795],
                    [-72.75146547241863, 45.935807479190139],
                    [-72.878148934307319, 47.09971178529252],
                    [-73.772850883896226, 46.624648803209915],
                    [-73.772850883896226, 46.624648803209915],
                    [-73.796604033000364, 46.885933443355349],
                    [-73.677838287479702, 47.250148396285347],
                    [-73.859945763944708, 47.392667290910126],
                ]
            ],
        }
        img_utm, _ = await backend.feature(
            cpx_shape,
            shape_crs=CRS.from_epsg(4326),
            pixel_selection=defaults.MeanMethod,
        )
        assert img_utm.crs == CRS.from_epsg(4326)
        assert not img_utm.array.mask.all()
        assert numpy.unique(img_utm.data).tolist() == [0, 1, 2]
