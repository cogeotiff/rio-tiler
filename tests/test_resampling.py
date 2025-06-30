"""test IO and Warp resampling."""

import os
from typing import get_args

import numpy
import pytest

from rio_tiler.io import Reader
from rio_tiler.types import RIOResampling, WarpResampling

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
COGEO = os.path.join(PREFIX, "cog.tif")


@pytest.mark.parametrize("resampling", get_args(RIOResampling))
def test_read_resampling(resampling):
    """Test read with all resampling."""
    with Reader(COGEO) as src:
        im = src.preview(max_size=64, resampling_method=resampling)
        assert im.data.any()
        # make sure each method returns diff results
        if resampling != "nearest":
            imr = src.preview(
                max_size=64, resampling_method="nearest", dst_crs="epsg:4326"
            )
            assert not numpy.array_equal(imr.array, im.array)


@pytest.mark.parametrize("resampling", get_args(WarpResampling))
def test_warp_resampling(resampling):
    """Test warp with all resampling."""
    with Reader(COGEO) as src:
        im = src.preview(max_size=64, reproject_method=resampling, dst_crs="epsg:4326")
        assert im.data.any()
        # make sure each method returns diff results
        if resampling != "nearest":
            imr = src.preview(
                max_size=64, reproject_method="nearest", dst_crs="epsg:4326"
            )
            assert not numpy.array_equal(imr.array, im.array)


def test_resampling_diff():
    """Test that both `reproject` and `resampling` has influence."""
    # check diff results when using different `reproject_method`
    with Reader(COGEO) as src:
        tile_cubic = src.tile(
            43,
            24,
            7,
            resampling_method="nearest",
            reproject_method="cubic",
        )
        tile_nearest = src.tile(
            43,
            24,
            7,
            resampling_method="nearest",
            reproject_method="nearest",
        )
    assert not numpy.array_equal(tile_cubic.array, tile_nearest.array)

    # check diff results when using different `resampling_method`
    with Reader(COGEO) as src:
        tile_cubic = src.tile(
            43,
            24,
            7,
            resampling_method="cubic",
            reproject_method="nearest",
        )
        tile_nearest = src.tile(
            43,
            24,
            7,
            resampling_method="nearest",
            reproject_method="nearest",
        )
    assert not numpy.array_equal(tile_cubic.array, tile_nearest.array)
