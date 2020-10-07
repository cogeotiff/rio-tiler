"""tests rio_tiler.io.BandFileReader"""

import os
import pathlib
from typing import Dict, Type

import attr
import pytest

from rio_tiler.errors import ExpressionMixingWarning, MissingBands
from rio_tiler.io import BaseReader, COGReader, MultiBandReader
from rio_tiler.tms import TileMatrixSet, default_tms

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")


@attr.s
class BandFileReader(MultiBandReader):
    """Test MultiBand"""

    path: str = attr.ib()
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: TileMatrixSet = attr.ib(default=default_tms)

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
        meta = cog.spatial_info
        assert meta.get("minzoom")
        assert meta.get("maxzoom")
        assert meta.get("center")
        assert len(meta.get("bounds")) == 4

        assert sorted(cog.parse_expression("b1/b2")) == ["b1", "b2"]

        with pytest.raises(MissingBands):
            cog.info()

        meta = cog.info(bands="b1")
        assert meta["band_descriptions"] == [(1, "b1")]

        meta = cog.info(bands=("b1", "b2"))
        assert meta["band_descriptions"] == [(1, "b1"), (2, "b2")]

        with pytest.raises(MissingBands):
            cog.stats()

        meta = cog.stats(bands="b1", hist_options={"bins": 20})
        assert meta["b1"]

        meta = cog.stats(bands=("b1", "b2"))
        assert meta["b1"]
        assert meta["b2"]

        with pytest.raises(MissingBands):
            cog.metadata()

        meta = cog.metadata(bands="b1")
        assert meta["statistics"]["b1"]

        meta = cog.metadata(bands=("b1", "b2"))
        assert meta["statistics"]["b1"]
        assert meta["statistics"]["b2"]
        assert meta["band_descriptions"] == [(1, "b1"), (2, "b2")]

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
