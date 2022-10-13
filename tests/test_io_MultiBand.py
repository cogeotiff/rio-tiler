"""tests rio_tiler.io.BandFileReader"""

import os
import pathlib
from typing import Dict, Type

import attr
import morecantile
import pytest

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import ExpressionMixingWarning, MissingBands
from rio_tiler.io import BaseReader, MultiBandReader, Reader
from rio_tiler.models import BandStatistics

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")


@attr.s
class BandFileReader(MultiBandReader):
    """Test MultiBand"""

    input: str = attr.ib()
    tms: morecantile.TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: Type[BaseReader] = attr.ib(init=False, default=Reader)
    reader_options: Dict = attr.ib(factory=dict)

    minzoom: int = attr.ib()
    maxzoom: int = attr.ib()

    @minzoom.default
    def _minzoom(self):
        return self.tms.minzoom

    @maxzoom.default
    def _maxzoom(self):
        return self.tms.maxzoom

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.bands = sorted(
            [
                p.stem.split("_")[1]
                for p in pathlib.Path(self.input).glob("*scene_*.tif")
            ]
        )
        with self.reader(self._get_band_url(self.bands[0])) as cog:
            self.bounds = cog.bounds
            self.crs = cog.crs
            self.minzoom = cog.minzoom
            self.maxzoom = cog.maxzoom

    def _get_band_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.input, f"scene_{band}.tif")


def test_MultiBandReader():
    """Should work as expected."""
    with BandFileReader(PREFIX) as cog:
        assert cog.bands == ["band1", "band2"]
        assert cog.minzoom is not None
        assert cog.maxzoom is not None
        assert cog.bounds
        assert cog.bounds
        assert cog.crs

        assert sorted(cog.parse_expression("band1/band2")) == ["band1", "band2"]

        with pytest.warns(UserWarning):
            meta = cog.info()
        assert meta.band_descriptions == [("band1", ""), ("band2", "")]

        meta = cog.info(bands="band1")
        assert meta.band_descriptions == [("band1", "")]

        meta = cog.info(bands=("band1", "band2"))
        assert meta.band_descriptions == [("band1", ""), ("band2", "")]

        with pytest.warns(UserWarning):
            stats = cog.statistics()
            assert stats["band1"]
            assert stats["band2"]

        stats = cog.statistics(bands="band1")
        assert "band1" in stats
        assert isinstance(stats["band1"], BandStatistics)

        stats = cog.statistics(bands=("band1", "band2"))
        assert stats["band1"]
        assert stats["band2"]

        stats = cog.statistics(expression="band1;band1+band2;band1-100")
        assert stats["band1"]
        assert stats["band1+band2"]
        assert stats["band1-100"]

        with pytest.raises(MissingBands):
            cog.tile(238, 218, 9)

        tile = cog.tile(238, 218, 9, bands="band1")
        assert tile.data.shape == (1, 256, 256)
        assert tile.band_names == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            tile = cog.tile(238, 218, 9, bands="band1", expression="band1*2")
        assert tile.data.shape == (1, 256, 256)
        assert tile.band_names == ["band1*2"]

        with pytest.raises(MissingBands):
            cog.part((-11.5, 24.5, -11.0, 25.0))

        tile = cog.part((-11.5, 24.5, -11.0, 25.0), bands="band1")
        assert tile.data.any()
        assert tile.band_names == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            tile = cog.part(
                (-11.5, 24.5, -11.0, 25.0), bands="band1", expression="band1*2"
            )
        assert tile.data.any()
        assert tile.band_names == ["band1*2"]

        with pytest.raises(MissingBands):
            cog.preview()

        tile = cog.preview(bands="band1")
        assert tile.data.any()
        assert tile.band_names == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            tile = cog.preview(bands="band1", expression="band1*2")
        assert tile.data.any()
        assert tile.band_names == ["band1*2"]

        with pytest.raises(MissingBands):
            cog.point(-11.5, 24.5)

        pt = cog.point(-11.5, 24.5, bands="band1")
        assert len(pt.data) == 1
        assert pt.band_names == ["band1"]

        pt = cog.point(-11.5, 24.5, bands=("band1", "band2"))
        assert len(pt.data) == 2
        assert pt.band_names == ["band1", "band2"]

        pt = cog.point(-11.5, 24.5, expression="band1/band2")
        assert len(pt.data) == 1
        assert pt.band_names == ["band1/band2"]

        with pytest.warns(ExpressionMixingWarning):
            assert cog.point(-11.5, 24.5, bands="band1", expression="band1*2")

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

        img = cog.feature(feat, bands="band1")
        assert img.data.any()
        assert not img.mask.all()
        assert img.band_names == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            img = cog.feature(feat, bands="band1", expression="band1*2")
            assert img.band_names == ["band1*2"]
