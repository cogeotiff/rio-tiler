"""tests rio_tiler.mercator"""

import os

import pytest
import rasterio

from rio_tiler import mercator

dataset = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")


def test_get_zooms_valid():
    """Should work as expected (return zooms)."""
    with pytest.warns(DeprecationWarning):
        with rasterio.open(dataset) as src_dst:
            minzoom, maxzoom = mercator.get_zooms(src_dst)
            assert minzoom == 4
            assert maxzoom == 8

            minzoom, maxzoom = mercator.get_zooms(src_dst, tilesize=512)
            assert minzoom == 4
            assert maxzoom == 7

            minzoom, maxzoom = mercator.get_zooms(src_dst, ensure_global_max_zoom=True)
            assert minzoom == 6
            assert maxzoom == 10


def test_m_per_pixel_valid():
    """Should work as expected (return resolution for mercator zoom)."""
    with pytest.warns(DeprecationWarning):
        assert round(mercator._meters_per_pixel(12), 4) == 38.2185
        assert round(mercator._meters_per_pixel(12, tilesize=512), 4) == 19.1093


def test_zoom_for_pixelsize_valid():
    """Should work as expected (return mercator zoom)."""
    with pytest.warns(DeprecationWarning):
        res = mercator._meters_per_pixel(12)
        assert mercator.zoom_for_pixelsize(res) == 12
        assert mercator.zoom_for_pixelsize(res, tilesize=512) == 11

        # Return max zoom
        assert mercator.zoom_for_pixelsize(0.00001) == 24
