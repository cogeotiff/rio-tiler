"""test VSIReader."""

import os

import numpy
import pytest

from rio_tiler.experimental.vsifile import VSIReader
from rio_tiler.io import Reader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
COGEO = os.path.join(PREFIX, "cog.tif")


def test_vsireader():
    """Test Reader using VSIFile handler."""
    pytest.importorskip("vsifile")

    # VSIReader doesn't take dataset as input
    with pytest.raises(TypeError):
        with VSIReader(COGEO, dataset="cog"):
            pass

    with VSIReader(COGEO) as vsi, Reader(COGEO) as src:
        assert vsi.bounds == src.bounds
        assert vsi.crs == src.crs
        assert vsi.info().model_dump() == src.info().model_dump()

        img_vsi = vsi.preview()
        img_src = src.preview()
        assert numpy.array_equal(img_vsi.array, img_src.array)
