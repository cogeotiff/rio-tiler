"""tests rio_tiler.io.BandFileReader"""

import os
import pathlib
from typing import Dict, Type

import attr
import morecantile
import pytest

from rio_tiler.errors import ExpressionMixingWarning, MissingBands
from rio_tiler.io import BaseReader, COGReader, MultiBandReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

default_tms = morecantile.tms.get("WebMercatorQuad")


@attr.s
class BandFileReader(MultiBandReader):
    """Test MultiBand"""

    path: str = attr.ib()
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: morecantile.TileMatrixSet = attr.ib(default=default_tms)

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.bands = sorted(
            [p.stem.split("_")[1] for p in pathlib.Path(self.path).glob("*scene_*.tif")]
        )
        with self.reader(self._get_band_url(self.bands[0])) as cog:
            self.bounds = cog.bounds
            self.minzoom = cog.minzoom
            self.maxzoom = cog.maxzoom

    def _get_band_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.path, f"scene_{band}.tif")


def test_MultiBandReader():
    """Should work as expected."""
    with BandFileReader(PREFIX) as cog:
        assert cog.bands == ["b1", "b2"]
        assert cog.spatial_info

        assert sorted(cog.parse_expression("b1/b2")) == ["b1", "b2"]

        with pytest.raises(MissingBands):
            cog.info()

        meta = cog.info(bands="b1")
        assert meta.band_descriptions == [("b1", "")]

        meta = cog.info(bands=("b1", "b2"))
        assert meta.band_descriptions == [("b1", ""), ("b2", "")]

        with pytest.raises(MissingBands):
            cog.stats()

        meta = cog.stats(bands="b1", hist_options={"bins": 20})
        assert meta["b1"]

        meta = cog.stats(bands=("b1", "b2"))
        assert meta["b1"]
        assert meta["b2"]

        with pytest.raises(MissingBands):
            with pytest.warns(DeprecationWarning):
                cog.metadata()

        with pytest.warns(DeprecationWarning):
            meta = cog.metadata(bands="b1")
            assert meta.statistics["b1"]

        with pytest.warns(DeprecationWarning):
            meta = cog.metadata(bands=("b1", "b2"))
            assert meta.statistics["b1"]
            assert meta.statistics["b2"]
            assert meta.band_descriptions == [("b1", ""), ("b2", "")]

        with pytest.raises(MissingBands):
            cog.tile(238, 218, 9)

        tile, _ = cog.tile(238, 218, 9, bands="b1")
        assert tile.shape == (1, 256, 256)

        with pytest.warns(ExpressionMixingWarning):
            tile, _ = cog.tile(238, 218, 9, bands="b1", expression="b1*2")
        assert tile.shape == (1, 256, 256)

        with pytest.raises(MissingBands):
            cog.part((-11.5, 24.5, -11.0, 25.0))

        tile, _ = cog.part((-11.5, 24.5, -11.0, 25.0), bands="b1")
        assert tile.any()

        with pytest.warns(ExpressionMixingWarning):
            tile, _ = cog.part(
                (-11.5, 24.5, -11.0, 25.0), bands="b1", expression="b1*2"
            )
        assert tile.any()

        with pytest.raises(MissingBands):
            cog.preview()

        tile, _ = cog.preview(bands="b1")
        assert tile.any()

        with pytest.warns(ExpressionMixingWarning):
            tile, _ = cog.preview(bands="b1", expression="b1*2")
        assert tile.any()

        with pytest.raises(MissingBands):
            cog.point(-11.5, 24.5)

        assert cog.point(-11.5, 24.5, bands="b1")

        with pytest.warns(ExpressionMixingWarning):
            assert cog.point(-11.5, 24.5, bands="b1", expression="b1*2")

        feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-12.03826904296875, 24.87646991083154],
                        [-12.14263916015625, 24.831610355586918],
                        [-12.1563720703125, 24.709410369765177],
                        [-12.1673583984375, 24.484648999654034],
                        [-11.898193359375, 24.472150437226865],
                        [-11.6729736328125, 24.542126388899305],
                        [-11.47247314453125, 24.79920167537382],
                        [-12.03826904296875, 24.87646991083154],
                    ]
                ],
            },
        }
        with pytest.raises(MissingBands):
            cog.feature(feat)

        img = cog.feature(feat, bands="b1")
        assert img.data.any()
        assert not img.mask.all()

        with pytest.warns(ExpressionMixingWarning):
            cog.feature(feat, bands="b1", expression="b1*2")
