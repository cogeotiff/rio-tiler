"""tests rio_tiler.base"""

import os

import pytest

from rio_tiler.errors import TileOutsideBounds
from rio_tiler.io import COGReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"

COG_ALPHA = os.path.join(PREFIX, "my-bucket", KEY_ALPHA)
COG_MASK = os.path.join(PREFIX, "my-bucket", KEY_MASK)

COGEO = os.path.join(PREFIX, "cog.tif")
COG_CMAP = os.path.join(PREFIX, "cog_cmap.tif")
COG_TAGS = os.path.join(PREFIX, "cog_tags.tif")
COG_NODATA = os.path.join(PREFIX, "cog_nodata.tif")
COG_SCALE = os.path.join(PREFIX, "cog_scale.tif")


def test_spatial_info_valid():
    """Should work as expected (get spatial info)"""
    with COGReader(COG_NODATA) as cog:
        meta = cog.spatial_info()
    assert meta.get("minzoom")
    assert meta.get("maxzoom")
    assert meta.get("center")
    assert len(meta.get("bounds")) == 4


def test_bounds_valid():
    """Should work as expected (get bounds)"""
    with COGReader(COG_NODATA) as cog:
        assert len(cog.bounds) == 4


def test_info_valid():
    """Should work as expected (get file info)"""
    with COGReader(COG_SCALE) as cog:
        meta = cog.info
    assert meta.get("scale")
    assert meta.get("offset")

    with COGReader(COG_CMAP) as cog:
        assert cog.colormap
        meta = cog.info
    assert meta.get("colormap")

    with COGReader(COG_TAGS) as cog:
        meta = cog.info
    assert meta.get("bounds")
    assert meta.get("minzoom")
    assert meta.get("maxzoom")
    assert meta.get("band_descriptions")
    assert meta.get("dtype") == "int16"
    assert meta.get("colorinterp") == ["gray"]
    assert meta.get("nodata_type") == "Nodata"
    assert meta.get("scale")
    assert meta.get("offset")
    assert meta.get("band_metadata")
    bmeta = meta.get("band_metadata")[0][1]
    assert bmeta.get("STATISTICS_MAXIMUM")
    assert bmeta.get("STATISTICS_MEAN")
    assert bmeta.get("STATISTICS_MINIMUM")

    with COGReader(COG_ALPHA) as cog:
        meta = cog.info
    assert meta.get("nodata_type") == "Alpha"

    with COGReader(COG_MASK) as cog:
        meta = cog.info
    assert meta.get("nodata_type") == "Mask"

    with COGReader(COGEO) as cog:
        meta = cog.info
    assert meta.get("nodata_type") == "None"

    with COGReader(COG_NODATA) as cog:
        meta = cog.info
    assert meta.get("nodata_type") == "Nodata"


def test_metadata_valid():
    """Get bounds and get stats for all bands."""
    with COGReader(COGEO) as cog:
        meta = cog.metadata()
    assert len(meta["band_descriptions"]) == 1
    assert (1, "band1") == meta["band_descriptions"][0]
    assert len(meta["statistics"].items()) == 1
    assert meta["statistics"][1]["pc"] == [1, 6896]

    with COGReader(COGEO) as cog:
        meta = cog.stats()
    assert len(meta.items()) == 1
    assert meta[1]["pc"] == [1, 6896]

    with COGReader(COGEO) as cog:
        meta = cog.metadata(pmin=5, pmax=90, hist_options=dict(bins=20), max_size=128)
    assert len(meta["statistics"].items()) == 1
    assert len(meta["statistics"][1]["histogram"][0]) == 20
    assert meta["statistics"][1]["pc"] == [1, 3776]

    with COGReader(COG_CMAP) as cog:
        assert cog.colormap
        meta = cog.metadata()
        assert meta["statistics"][1]["histogram"][1] == list(range(20))


def test_tile_valid_default():
    """Should return a 3 bands array and a full valid mask."""
    with COGReader(COG_NODATA) as cog:
        # Full tile
        data, mask = cog.tile(43, 24, 7)
        assert data.shape == (1, 256, 256)
        assert mask.all()

        # Partial tile
        data, mask = cog.tile(42, 24, 7)
        assert data.shape == (1, 256, 256)
        assert not mask.all()

        # Expression
        data, mask = cog.tile(43, 24, 7, expression="b1*2,b1-100")
        assert data.shape == (2, 256, 256)

        data, mask = cog.tile(43, 24, 7, indexes=1)
        assert data.shape == (1, 256, 256)

        data, mask = cog.tile(43, 24, 7, indexes=(1, 1,))
        assert data.shape == (2, 256, 256)


def test_tile_invalid_bounds():
    """Should raise an error with invalid tile."""
    with pytest.raises(TileOutsideBounds):
        with COGReader(COGEO) as cog:
            cog.tile(38, 24, 7)


def test_point_valid():
    """Read point."""
    lon = -56.624124590533825
    lat = 73.52687881825946
    with COGReader(COG_NODATA) as cog:
        pts = cog.point(lon, lat)
        assert len(pts) == 1

        pts = cog.point(lon, lat, expression="b1*2,b1-100")
        assert len(pts) == 2

        pts = cog.point(lon, lat, indexes=1)
        assert len(pts) == 1

        pts = cog.point(lon, lat, indexes=(1, 1,))
        assert len(pts) == 2


def test_area_valid():
    """Read part of an image."""
    bbox = (
        -56.624124590533825,
        73.52687881825946,
        -56.530950796449005,
        73.50183615350426,
    )
    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox)
    assert data.shape == (1, 11, 41)

    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox, dst_crs=cog.dataset.crs)
    assert data.shape == (1, 29, 30)

    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox, max_size=30)
    assert data.shape == (1, 9, 30)

    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox, expression="b1*2,b1-100")
    assert data.shape == (2, 11, 41)

    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox, indexes=1)
    assert data.shape == (1, 11, 41)

    with COGReader(COG_NODATA) as cog:
        data, mask = cog.part(bbox, indexes=(1, 1,))
    assert data.shape == (2, 11, 41)


def test_preview_valid():
    """Read preview."""
    with COGReader(COGEO) as cog:
        data, mask = cog.preview(max_size=128)
    assert data.shape == (1, 128, 128)

    with COGReader(COGEO) as cog:
        data, mask = cog.preview()
    assert data.shape == (1, 1024, 1021)

    with COGReader(COGEO) as cog:
        data, mask = cog.preview(max_size=128, expression="b1*2,b1-100")
    assert data.shape == (2, 128, 128)

    with COGReader(COGEO) as cog:
        data, mask = cog.preview(max_size=128, indexes=1)
    assert data.shape == (1, 128, 128)

    with COGReader(COGEO) as cog:
        data, mask = cog.preview(max_size=128, indexes=(1, 1,))
    assert data.shape == (2, 128, 128)
