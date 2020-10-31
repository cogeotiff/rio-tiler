"""tests rio_tiler.io.cogeo.COGReader"""

import os
from io import BytesIO
from typing import Any, Dict

import mercantile
import numpy
import pytest
from rasterio.io import DatasetReader, MemoryFile
from rasterio.vrt import WarpedVRT

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import ExpressionMixingWarning, TileOutsideBounds
from rio_tiler.io import COGReader, GCPCOGReader

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
COG_GCPS = os.path.join(PREFIX, "cog_gcps.tif")


def test_spatial_info_valid():
    """Should work as expected (get spatial info)"""
    with COGReader(COG_NODATA) as cog:
        assert not cog.dataset.closed
        meta = cog.spatial_info
        assert meta["minzoom"] == 4
        assert meta.minzoom == 4
        assert meta.maxzoom == 8
        assert cog.nodata == cog.dataset.nodata
    assert cog.dataset.closed

    cog = COGReader(COG_NODATA)
    assert not cog.dataset.closed
    cog.close()
    assert cog.dataset.closed

    with COGReader(COG_NODATA, minzoom=3) as cog:
        meta = cog.spatial_info
        assert meta.minzoom == 3
        assert meta.maxzoom == 8

    with COGReader(COG_NODATA, maxzoom=12) as cog:
        meta = cog.spatial_info
        assert meta.minzoom == 4
        assert meta.maxzoom == 12

    with COGReader(COG_NODATA, minzoom=3, maxzoom=12) as cog:
        meta = cog.spatial_info
        assert meta.minzoom == 3
        assert meta.maxzoom == 12


def test_bounds_valid():
    """Should work as expected (get bounds)"""
    with COGReader(COG_NODATA) as cog:
        assert len(cog.bounds) == 4


def test_info_valid():
    """Should work as expected (get file info)"""
    with COGReader(COG_SCALE) as cog:
        meta = cog.info()
        assert meta["scale"]
        assert meta.scale
        assert meta.offset
        assert not meta.colormap

    with COGReader(COG_CMAP) as cog:
        assert cog.colormap
        meta = cog.info()
        assert meta["colormap"]
        assert meta.colormap

    with COGReader(COG_NODATA, colormap={1: [0, 0, 0, 0]}) as cog:
        assert cog.colormap
        meta = cog.info()
        assert meta.colormap

    with COGReader(COG_TAGS) as cog:
        meta = cog.info()
        assert meta.bounds
        assert meta.minzoom
        assert meta.maxzoom
        assert meta.band_descriptions
        assert meta.dtype == "int16"
        assert meta.colorinterp == ["gray"]
        assert meta.nodata_type == "Nodata"
        assert meta.scale
        assert meta.offset
        assert meta.band_metadata
        band_meta = meta.band_metadata[0]
        assert band_meta[0] == "band1"
        assert "STATISTICS_MAXIMUM" in band_meta[1]

    with COGReader(COG_ALPHA) as cog:
        meta = cog.info()
        assert meta.nodata_type == "Alpha"

    with COGReader(COG_MASK) as cog:
        meta = cog.info()
        assert meta.nodata_type == "Mask"

    with COGReader(COGEO) as cog:
        meta = cog.info()
        assert meta.nodata_type == "None"

    with COGReader(COG_NODATA) as cog:
        meta = cog.info()
        assert meta.nodata_type == "Nodata"


def test_metadata_valid():
    """Get bounds and get stats for all bands."""
    with COGReader(COGEO) as cog:
        meta = cog.metadata()
        assert len(meta["band_descriptions"]) == 1
        assert len(meta.band_descriptions) == 1
        assert ("band1", "") == meta.band_descriptions[0]

        stats = meta["statistics"]
        assert len(stats.items()) == 1
        assert meta["statistics"]["band1"]["percentiles"]
        b1_stats = meta.statistics["band1"]
        assert b1_stats.percentiles == [1, 6896]

        stats = cog.stats()
        assert len(stats.items()) == 1
        b1_stats = stats["band1"]
        assert b1_stats.percentiles == [1, 6896]

        meta = cog.metadata(pmin=5, pmax=90, hist_options=dict(bins=20), max_size=128)
        stats = meta.statistics
        assert len(stats.items()) == 1
        b1_stats = stats["band1"]
        assert len(b1_stats.histogram[0]) == 20
        assert b1_stats.percentiles == [1, 3776]

    with COGReader(COG_CMAP) as cog:
        assert cog.colormap
        b1_stats = cog.metadata().statistics["band1"]
        assert b1_stats.histogram[1] == list(range(20))


def test_tile_valid_default():
    """Should return a 3 bands array and a full valid mask."""
    with COGReader(COG_NODATA) as cog:
        # Full tile
        data, mask = cog.tile(43, 24, 7)
        assert data.shape == (1, 256, 256)
        assert mask.all()

        tile_bounds = mercantile.xy_bounds(43, 24, 7)
        data_part, _ = cog.part(
            tile_bounds, bounds_crs="epsg:3857", width=256, height=256, max_size=None
        )
        assert numpy.array_equal(data, data_part)

        # Partial tile
        data, mask = cog.tile(42, 24, 7)
        assert data.shape == (1, 256, 256)
        assert not mask.all()

        # Expression
        data, mask = cog.tile(43, 24, 7, expression="b1*2,b1-100")
        assert data.shape == (2, 256, 256)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = cog.tile(43, 24, 7, indexes=(1, 2, 3), expression="b1*2")
            assert data.shape == (1, 256, 256)

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

        with pytest.warns(ExpressionMixingWarning):
            pts = cog.point(lon, lat, indexes=(1, 2, 3), expression="b1*2")
            assert len(pts) == 1

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

        data, mask = cog.part(bbox, dst_crs=cog.dataset.crs)
        assert data.shape == (1, 29, 30)

        data, mask = cog.part(bbox, max_size=30)
        assert data.shape == (1, 9, 30)

        data, mask = cog.part(bbox, expression="b1*2,b1-100")
        assert data.shape == (2, 11, 41)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = cog.part(bbox, indexes=(1, 2, 3), expression="b1*2")
            assert data.shape == (1, 11, 41)

        data, mask = cog.part(bbox, indexes=1)
        assert data.shape == (1, 11, 41)

        data, mask = cog.part(bbox, indexes=(1, 1,))
        assert data.shape == (2, 11, 41)


def test_preview_valid():
    """Read preview."""
    with COGReader(COGEO) as cog:
        data, mask = cog.preview(max_size=128)
        assert data.shape == (1, 128, 128)

        data, mask = cog.preview()
        assert data.shape == (1, 1024, 1021)

        data, mask = cog.preview(max_size=128, expression="b1*2,b1-100")
        assert data.shape == (2, 128, 128)

        with pytest.warns(ExpressionMixingWarning):
            data, _ = cog.preview(max_size=128, indexes=(1, 2, 3), expression="b1*2")
            assert data.shape == (1, 128, 128)

        data, mask = cog.preview(max_size=128, indexes=1)
        assert data.shape == (1, 128, 128)

        data, mask = cog.preview(max_size=128, indexes=(1, 1,))
        assert data.shape == (2, 128, 128)


def test_COGReader_Options():
    """Set options in reader."""
    with COGReader(COGEO, nodata=1) as cog:
        assert cog.nodata == 1
        b1_stats = cog.metadata().statistics["band1"]
        assert b1_stats.percentiles == [2720, 6896]
        assert cog.info().nodata_type == "Nodata"

    with COGReader(COGEO) as cog:
        assert not cog.nodata
        assert cog.info().nodata_type == "None"

    with COGReader(COGEO, nodata=1) as cog:
        _, mask = cog.tile(43, 25, 7)
        assert not mask.all()

    with COGReader(COGEO, nodata=1, resampling_method="bilinear") as cog:
        data, _ = cog.tile(43, 25, 7)
        assert data[0, 100, 100] == 3774  # 3776 with nearest

    with COGReader(COG_SCALE, unscale=True) as cog:
        p = cog.point(310000, 4100000, coord_crs=cog.dataset.crs)
        assert round(p[0], 3) == 1000.892

        # passing unscale in method should overwrite the defaults
        p = cog.point(310000, 4100000, coord_crs=cog.dataset.crs, unscale=False)
        assert p[0] == 8917

    cutline = "POLYGON ((13 1685, 1010 6, 2650 967, 1630 2655, 13 1685))"
    with COGReader(COGEO, vrt_options={"cutline": cutline}) as cog:
        _, mask = cog.preview()
        assert not mask.all()

    def callback(data, mask):
        mask.fill(255)
        data = data * 2
        return data, mask

    with COGReader(COGEO, nodata=1, post_process=callback) as cog:
        data_init, _ = cog.tile(43, 25, 7, post_process=None)
        data, mask = cog.tile(43, 25, 7)
        assert mask.all()
        assert data[0, 0, 0] == data_init[0, 0, 0] * 2

    lon = -56.624124590533825
    lat = 73.52687881825946
    with COGReader(COG_NODATA, post_process=callback) as cog:
        pts = cog.point(lon, lat)

    with COGReader(COG_NODATA) as cog:
        pts_init = cog.point(lon, lat)
    assert pts[0] == pts_init[0] * 2


def test_cog_with_internal_gcps():
    """Make sure file gets re-projected using gcps."""
    with GCPCOGReader(COG_GCPS, nodata=0) as cog:
        assert cog.bounds
        assert cog.nodata == 0
        assert isinstance(cog.src_dataset, DatasetReader)
        assert isinstance(cog.dataset, WarpedVRT)

        assert cog.minzoom == 6
        assert cog.maxzoom == 9

        metadata = cog.info()
        assert len(metadata.band_metadata) == 1
        assert metadata.band_descriptions == [("band1", "")]
        b1_stats = cog.stats()["band1"]
        assert b1_stats.max == 623

        tile_z = 8
        tile_x = 183
        tile_y = 120
        data, mask = cog.tile(tile_x, tile_y, tile_z)
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)


def parse_img(content: bytes) -> Dict[Any, Any]:
    """Read tile image and return metadata."""
    with MemoryFile(content) as mem:
        with mem.open() as dst:
            return dst.meta


def test_imageData_output():
    """Test ImageData output."""
    with COGReader(COG_NODATA) as cog:
        img = cog.tile(43, 24, 7)
        assert img.data.shape == (1, 256, 256)
        assert img.mask.all()
        assert img.count == 1
        assert img.data_as_image().shape == (256, 256, 1)

        assert numpy.array_equal(~img.as_masked().mask[0] * 255, img.mask)

        assert img.crs == WEB_MERCATOR_TMS.crs
        assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(43, 24, 7)

        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["driver"] == "GTiff"
        assert meta["crs"] == WEB_MERCATOR_TMS.crs
        assert meta["transform"]
        assert meta["count"] == 2

        res = img.render(img_format="NPY")
        arr = numpy.load(BytesIO(res))
        numpy.array_equal(arr[0], img.data)
        numpy.array_equal(arr[1], img.mask)

        img = cog.tile(43, 24, 7)
        assert img.data.dtype == "uint16"
        img.post_process(in_range=(img.data.min(), img.data.max()))
        assert img.data.dtype == "uint16"
        assert img.data.min() == 0
        assert img.data.max() == 255

        img.post_process(color_formula="Gamma R 3.1")
        assert img.data.dtype == "uint8"

        bbox = (
            -56.624124590533825,
            73.52687881825946,
            -56.530950796449005,
            73.50183615350426,
        )
        img = cog.part(bbox)
        assert img.data.shape == (1, 11, 41)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == WGS84_CRS
        assert img.bounds == bbox

        img = cog.part(bbox, dst_crs=cog.dataset.crs)
        assert img.data.shape == (1, 29, 30)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == cog.dataset.crs
        assert not img.bounds == bbox

        img = cog.preview(max_size=128)
        assert img.data.shape == (1, 128, 128)
        assert img.bounds == cog.dataset.bounds
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == cog.dataset.crs
