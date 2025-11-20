"""test Mosaic Backend."""

import os
from typing import Type

import attr
import pytest
from morecantile import TileMatrixSet
from rasterio.crs import CRS

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.io import BaseReader, MultiBandReader, MultiBaseReader, Reader
from rio_tiler.mosaic.backend import BaseBackend
from rio_tiler.mosaic.methods import defaults
from rio_tiler.types import BBox

asset1 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_value_1.tif")
asset2 = os.path.join(os.path.dirname(__file__), "fixtures", "mosaic_value_2.tif")
assets = [asset1, asset2]


def test_backend():
    """Test Backend implementation."""

    @attr.s
    class Backend(BaseBackend):
        """Test Backend implementation."""

        input: list[str] = attr.ib()
        tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

        reader: Type[BaseReader] | Type[MultiBaseReader] | Type[MultiBandReader] = (
            attr.ib(default=Reader)
        )
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
        assert set(assets_used) == set(asset1, asset2)
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
        assert set(assets_used) == set(asset1, asset2)
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"

        lon, lat = -73.69990294755982, 45.49950291143219
        point_values = backend.point(lon, lat, coord_crs=CRS.from_epsg(4326))
        assert len(point_values) == 2

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

        img, assets_used = backend.feature(
            feat,
            shape_crs=CRS.from_epsg(4326),
            max_size=256,
            pixel_selection=defaults.MeanMethod,
        )
        assert img.crs == CRS.from_epsg(4326)
        assert img.array.shape == (3, 147, 211)
        assert set(assets_used) == set(asset1, asset2)
        assert "timings" in img.metadata
        assert img.metadata["timings"][0][0] == "search"
        assert img.metadata["timings"][1][0] == "mosaicking"
