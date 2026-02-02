"""tests rio_tiler.io.BandFileReader"""

import os
import pathlib
from typing import Dict, Optional, Sequence, Type

import attr
import morecantile
import pytest

from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.errors import ExpressionMixingWarning, InvalidExpression, MissingBands
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

    default_bands: Optional[Sequence[str]] = attr.ib(default=None)

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
            [p.stem.split("_")[1] for p in pathlib.Path(self.input).glob("*scene_*.tif")]
        )
        with self.reader(self._get_band_url(self.bands[0])) as src:
            self.bounds = src.bounds
            self.crs = src.crs
            self.minzoom = src.minzoom
            self.maxzoom = src.maxzoom

    def _get_band_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.input, f"scene_{band}.tif")


def test_MultiBandReader():
    """Should work as expected."""
    with BandFileReader(PREFIX) as src:
        assert src.bands == ["band1", "band2"]
        assert src.minzoom is not None
        assert src.maxzoom is not None
        assert src.bounds
        assert src.bounds
        assert src.crs

        assert sorted(src.parse_expression("band1/band2")) == ["band1", "band2"]

        with pytest.raises(InvalidExpression):
            src.parse_expression("band19/band30")

        with pytest.warns(UserWarning):
            meta = src.info()
        assert meta.band_descriptions == [("band1", "b1"), ("band2", "b1")]

        meta = src.info(bands="band1")
        assert meta.band_descriptions == [("band1", "b1")]

        meta = src.info(bands=("band1", "band2"))
        assert meta.band_descriptions == [("band1", "b1"), ("band2", "b1")]

        with pytest.warns(UserWarning):
            stats = src.statistics()
            assert stats["b1"].description == "band1"
            assert stats["b2"].description == "band2"

        stats = src.statistics(bands="band1")
        assert "b1" in stats
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].description == "band1"

        stats = src.statistics(bands=("band1", "band2"))
        assert stats["b1"].description == "band1"
        assert stats["b2"].description == "band2"

        stats = src.statistics(expression="band1;band1+band2;band1-100")
        assert stats["b1"].description == "band1"
        assert stats["b2"].description == "band1+band2"
        assert stats["b3"].description == "band1-100"

        with pytest.raises(MissingBands):
            src.tile(238, 218, 9)

        img = src.tile(238, 218, 9, bands="band1")
        assert img.data.shape == (1, 256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.tile(238, 218, 9, bands="band1", expression="band1*2")
        assert img.data.shape == (1, 256, 256)
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["band1*2"]

        with pytest.raises(MissingBands):
            src.part((-11.5, 24.5, -11.0, 25.0))

        img = src.part((-11.5, 24.5, -11.0, 25.0), bands="band1")
        assert img.data.any()
        assert img.band_descriptions == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.part(
                (-11.5, 24.5, -11.0, 25.0), bands="band1", expression="band1*2"
            )
        assert img.data.any()
        assert img.band_descriptions == ["band1*2"]

        with pytest.raises(MissingBands):
            src.preview()

        img = src.preview(bands="band1")
        assert img.data.any()
        assert img.band_descriptions == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.preview(bands="band1", expression="band1*2")
        assert img.data.any()
        assert img.band_descriptions == ["band1*2"]

        with pytest.raises(MissingBands):
            src.point(-11.5, 24.5)

        pt = src.point(-11.5, 24.5, bands="band1")
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["band1"]
        assert len(pt.mask) == 1

        pt = src.point(-11.5, 24.5, bands=("band1", "band2"))
        assert len(pt.data) == 2
        assert pt.band_descriptions == ["band1", "band2"]
        assert len(pt.mask) == 1

        pt = src.point(-11.5, 24.5, expression="band1/band2")
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["band1/band2"]

        with pytest.warns(ExpressionMixingWarning):
            assert src.point(-11.5, 24.5, bands="band1", expression="band1*2")

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
            src.feature(feat)

        img = src.feature(feat, bands="band1")
        assert img.data.any()
        assert not img._mask.all()
        assert img.band_descriptions == ["band1"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.feature(feat, bands="band1", expression="band1*2")
            assert img.band_descriptions == ["band1*2"]

        img = src.preview(bands=("band1", "band2"))
        assert img.metadata
        assert img.metadata["band1"]
        assert img.metadata["band2"]


def test_MultiBandReader_default_bands():
    """Should work as expected."""
    with BandFileReader(PREFIX, default_bands=["band1"]) as src:
        assert src.bands == ["band1", "band2"]

        with pytest.warns(UserWarning):
            img = src.tile(238, 218, 9)
            assert img.data.shape == (1, 256, 256)
            assert img.band_descriptions == ["band1"]

        with pytest.warns(UserWarning):
            img = src.part((-11.5, 24.5, -11.0, 25.0))
            assert img.band_descriptions == ["band1"]

        with pytest.warns(UserWarning):
            img = src.preview()
            assert img.band_descriptions == ["band1"]

        with pytest.warns(UserWarning):
            pt = src.point(-11.5, 24.5)
            assert len(pt.data) == 1
            assert pt.band_descriptions == ["band1"]

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
        with pytest.warns(UserWarning):
            img = src.feature(feat)
            assert img.band_descriptions == ["band1"]
