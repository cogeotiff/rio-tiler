"""tests rio_tiler.io.rasterio.Reader"""

import os
from io import BytesIO
from typing import Any, Dict

import morecantile
import numpy
import pytest
import rasterio
from morecantile import TileMatrixSet
from pyproj import CRS
from rasterio import transform
from rasterio.crs import CRS as rioCRS
from rasterio.features import bounds as featureBounds
from rasterio.io import MemoryFile
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds

from rio_tiler.colormap import cmap
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    ExpressionMixingWarning,
    InvalidBufferSize,
    InvalidExpression,
    NoOverviewWarning,
    TileOutsideBounds,
)
from rio_tiler.io import Reader
from rio_tiler.models import BandStatistics
from rio_tiler.utils import create_cutline

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

COGEO = os.path.join(PREFIX, "cog.tif")
COG_WEB = os.path.join(PREFIX, "web.tif")
COG_CMAP = os.path.join(PREFIX, "cog_cmap.tif")
COG_TAGS = os.path.join(PREFIX, "cog_tags.tif")
COG_NODATA = os.path.join(PREFIX, "cog_nodata.tif")
COG_SCALE = os.path.join(PREFIX, "cog_scale.tif")
COG_SCALE_STATS = os.path.join(PREFIX, "cog_scale_stats.tif")
COG_GCPS = os.path.join(PREFIX, "cog_gcps.tif")
COG_DLINE = os.path.join(PREFIX, "cog_dateline.tif")
COG_EARTH = os.path.join(PREFIX, "cog_fullearth.tif")
GEOTIFF = os.path.join(PREFIX, "nocog.tif")
COG_EUROPA = os.path.join(PREFIX, "cog_nonearth.tif")
COG_MARS = os.path.join(PREFIX, "cog_hirise_mars.tif")
COG_INVERTED = os.path.join(PREFIX, "inverted_lat.tif")

KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
COG_ALPHA = os.path.join(PREFIX, "my-bucket", KEY_ALPHA)

KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"
COG_MASK = os.path.join(PREFIX, "my-bucket", KEY_MASK)

KEY_EXTMASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_extmask.tif"
COG_EXTMASK = os.path.join(PREFIX, "my-bucket", KEY_EXTMASK)


def test_spatial_info_valid():
    """Should work as expected (get spatial info)"""
    with Reader(COG_NODATA) as src:
        assert not src.dataset.closed
        assert src.bounds
        assert src.crs
        assert src.minzoom == 5
        assert src.maxzoom == 9
    assert src.dataset.closed

    src = Reader(COG_NODATA)
    assert not src.dataset.closed
    src.close()
    assert src.dataset.closed


def test_bounds_valid():
    """Should work as expected (get bounds)"""
    with Reader(COG_NODATA) as src:
        assert len(src.bounds) == 4


def test_info_valid():
    """Should work as expected (get file info)"""
    with Reader(COG_SCALE) as src:
        meta = src.info()
        assert meta.bounds == src.bounds == src.dataset.bounds
        crs = meta.crs
        assert rioCRS.from_user_input(crs) == src.crs

        assert meta.scales
        assert meta.offsets
        assert not meta.colormap
        assert meta.width
        assert meta.height
        assert meta.count
        assert meta.overviews
        assert meta.driver

    with Reader(COG_CMAP) as src:
        meta = src.info()
        assert meta.bounds == src.bounds == src.dataset.bounds
        crs = meta.crs
        assert rioCRS.from_user_input(crs) == src.crs

        assert src.colormap
        meta = src.info()
        assert meta.colormap

    with Reader(COG_NODATA, colormap={1: (0, 0, 0, 0)}) as src:
        assert src.colormap
        meta = src.info()
        assert meta.colormap
        assert meta.nodata_value

    with Reader(COG_TAGS) as src:
        meta = src.info()
        assert meta.bounds
        assert meta.crs
        assert meta.band_descriptions
        assert meta.dtype == "int16"
        assert meta.colorinterp == ["gray"]
        assert meta.nodata_type == "Nodata"
        assert meta.scales
        assert meta.offsets
        assert meta.band_metadata
        band_meta = meta.band_metadata[0]
        assert band_meta[0] == "b1"
        assert "STATISTICS_MAXIMUM" in band_meta[1]

    with Reader(COG_ALPHA) as src:
        meta = src.info()
        assert meta.nodata_type == "Alpha"

    with Reader(COG_MASK) as src:
        meta = src.info()
        assert meta.nodata_type == "Mask"

    with Reader(COGEO) as src:
        meta = src.info()
        assert meta.nodata_type == "None"

    with Reader(COG_NODATA) as src:
        meta = src.info()
        assert meta.nodata_type == "Nodata"


def test_tile_valid_default():
    """Should return a 3 bands array and a full valid mask."""
    with Reader(COG_NODATA) as src:
        # Full tile
        img = src.tile(43, 24, 7)
        assert img.data.shape == (1, 256, 256)
        assert img._mask.all()
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["b1"]  # default to b{idx}

        # Validate that Tile and Part gives the same result
        tile_bounds = WEB_MERCATOR_TMS.xy_bounds(43, 24, 7)
        data_part, _ = src.part(
            tile_bounds,
            bounds_crs=WEB_MERCATOR_TMS.crs,
            width=256,
            height=256,
            max_size=None,
        )
        assert numpy.array_equal(img.data, data_part)

        img = src.tile(43, 24, 7, expression="b1+2")
        assert img.data.shape == (1, 256, 256)
        assert img._mask.all()
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["b1+2"]

        img = src.tile(43, 24, 7, expression="B1+2")
        assert img.data.shape == (1, 256, 256)
        assert img._mask.all()
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["b1+2"]

        # Partial tile
        data, mask = src.tile(42, 24, 7)
        assert data.shape == (1, 256, 256)
        assert not mask.all()

        # Expression
        img = src.tile(43, 24, 7, expression="b1*2;b1-100")
        assert img.data.shape == (2, 256, 256)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.tile(43, 24, 7, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 256, 256)
        assert img.band_descriptions == ["b1*2"]

        data, mask = src.tile(43, 24, 7, indexes=1)
        assert data.shape == (1, 256, 256)

        img = src.tile(
            43,
            24,
            7,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 256, 256)
        assert img.band_descriptions == ["b1", "b1"]

    # We are using a file that is aligned with the grid so no resampling should be involved
    with Reader(COG_WEB) as src:
        img = src.tile(147, 182, 9)
        img_buffer = src.tile(147, 182, 9, buffer=10)
        assert img_buffer.width == 276
        assert img_buffer.height == 276
        assert not img.bounds == img_buffer.bounds
        assert numpy.array_equal(img.data, img_buffer.data[:, 10:266, 10:266])


def test_invalid_expression():
    """Should raise an error with invalid expression."""
    with pytest.raises(InvalidExpression):
        with Reader(COGEO) as src:
            src.preview(expression="somethingwithoutband")


def test_tile_invalid_bounds():
    """Should raise an error with invalid tile."""
    with pytest.raises(TileOutsideBounds):
        with Reader(COGEO) as src:
            src.tile(38, 24, 7)


def test_tile_with_incorrect_float_buffer():
    """should raise InvalidBufferSize."""
    with pytest.raises(InvalidBufferSize):
        with Reader(COGEO) as src:
            src.tile(43, 24, 7, buffer=0.8)


def test_tile_with_int_buffer():
    """should pass without issues."""
    with Reader(COGEO) as src:
        data, mask = src.tile(43, 24, 7, buffer=1)
    assert data.shape == (1, 258, 258)
    assert mask.all()

    with Reader(COGEO) as src:
        data, mask = src.tile(43, 24, 7, buffer=0)
    assert data.shape == (1, 256, 256)
    assert mask.all()


def test_tile_with_correct_float_buffer():
    """should pass without issues."""
    with Reader(COGEO) as src:
        data, mask = src.tile(43, 24, 7, buffer=0.5)
    assert data.shape == (1, 257, 257)
    assert mask.all()


def test_point_valid():
    """Read point."""
    lon = -56.624124590533825
    lat = 73.52687881825946
    with Reader(COG_NODATA) as src:
        pt = src.point(lon, lat)
        assert len(pt.data) == 1
        assert len(pt.mask) == 1
        assert pt.band_names == ["b1"]

        pt = src.point(lon, lat, expression="b1*2;b1-100")
        assert len(pt.data) == 2
        assert len(pt.mask) == 1
        assert pt._mask[0]
        assert pt.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            pt = src.point(lon, lat, indexes=(1, 2, 3), expression="b1*2")
            assert len(pt.data) == 1
            assert pt.band_descriptions == ["b1*2"]

        pt = src.point(lon, lat, indexes=1)
        assert len(pt.data) == 1
        assert pt.band_descriptions == ["b1"]

        pt = src.point(
            lon,
            lat,
            indexes=(
                1,
                1,
            ),
        )
        assert len(pt.data) == 2
        assert pt.band_descriptions == ["b1", "b1"]

        pt = src.point(-59.53, 74.03, indexes=(1, 1, 1))
        assert len(pt.data) == 3
        assert not pt._mask[0]
        assert pt.band_descriptions == ["b1", "b1", "b1"]


def test_area_valid():
    """Read part of an image."""
    bbox = (
        -56.624124590533825,
        73.50183615350426,
        -56.530950796449005,
        73.52687881825946,
    )
    with Reader(COG_NODATA) as src:
        img = src.part(bbox)
        assert img.data.shape == (1, 11, 40)
        assert img.band_names == ["b1"]

        data, mask = src.part(bbox, dst_crs=src.dataset.crs)
        assert data.shape == (1, 28, 30)

        data, mask = src.part(bbox, max_size=30)
        assert data.shape == (1, 9, 30)

        img = src.part(bbox, expression="b1*2;b1-100")
        assert img.data.shape == (2, 11, 40)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.part(bbox, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 11, 40)
            assert img.band_descriptions == ["b1*2"]

        data, mask = src.part(bbox, indexes=1)
        assert data.shape == (1, 11, 40)

        img = src.part(
            bbox,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 11, 40)
        assert img.band_names == ["b1", "b2"]
        assert img.band_descriptions == ["b1", "b1"]


def test_preview_valid():
    """Read preview."""
    with Reader(COGEO) as src:
        img = src.preview(max_size=128)
        assert img.data.shape == (1, 128, 128)
        assert img.band_descriptions == ["b1"]

        data, mask = src.preview()
        assert data.shape == (1, 1024, 1021)

        img = src.preview(max_size=128, expression="b1*2;b1-100")
        assert img.data.shape == (2, 128, 128)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.preview(max_size=128, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 128, 128)
            assert img.band_descriptions == ["b1*2"]

        data, mask = src.preview(max_size=128, indexes=1)
        assert data.shape == (1, 128, 128)

        img = src.preview(
            max_size=128,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 128, 128)
        assert img.band_names == ["b1", "b2"]
        assert img.band_descriptions == ["b1", "b1"]


def test_statistics():
    """tests statistics method."""
    with Reader(COGEO) as src:
        stats = src.statistics()
        assert len(stats) == 1
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].percentile_2
        assert stats["b1"].percentile_98

    with Reader(COGEO) as src:
        stats = src.statistics(percentiles=[3])
        assert stats["b1"].percentile_3

    with Reader(COGEO) as src:
        stats = src.statistics(percentiles=[3])
        assert stats["b1"].percentile_3

    with Reader(COG_CMAP) as src:
        stats = src.statistics(categorical=True)
        assert stats["b1"].histogram[1] == [
            1.0,
            3.0,
            4.0,
            5.0,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
        ]

        stats = src.statistics(categorical=True, categories=[1, 3])
        assert stats["b1"].histogram[1] == [
            1.0,
            3.0,
        ]

    # make sure kwargs are passed to `preview`
    with Reader(COGEO) as src:
        stats = src.statistics(width=100, height=100, max_size=None)
        assert stats["b1"].count == 10000.0

    # Check results for expression
    with Reader(COGEO) as src:
        stats = src.statistics(expression="b1;b1*2")
        assert stats["b1"]
        assert stats["b1"].description == "b1"
        assert stats["b2"]
        assert stats["b2"].description == "b1*2"
        assert stats["b1"].min == stats["b2"].min / 2

    with Reader(COG_TAGS) as src:
        stats = src.statistics()
        assert len(stats) == 1
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].percentile_2
        assert stats["b1"].percentile_98


def test_Reader_Options():
    """Set options in reader."""
    with Reader(COGEO, options={"nodata": 1}) as src:
        assert src.info().nodata_value == 1
        assert src.info().nodata_type == "Nodata"

    with Reader(COGEO) as src:
        assert src.info().nodata_type == "None"

    with Reader(COGEO, options={"nodata": 1}) as src:
        _, mask = src.tile(43, 25, 7)
        assert not mask.all()

    # read cog using default Nearest
    with Reader(COGEO, options={"nodata": 1}) as src:
        data_default, _ = src.tile(43, 25, 7)

    # read cog using bilinear
    with Reader(COGEO, options={"nodata": 1, "resampling_method": "bilinear"}) as src:
        data, _ = src.tile(43, 25, 7)
        assert not numpy.array_equal(data_default, data)

    with Reader(COG_SCALE, options={"unscale": True}) as src:
        p = src.point(310000, 4100000, coord_crs=src.dataset.crs)
        numpy.testing.assert_allclose(p.data, [1000.892, 2008.917], atol=1e-03)

        # applies correctly when passing indexes=[...]
        p = src.point(310000, 4100000, coord_crs=src.dataset.crs, indexes=[2])
        numpy.testing.assert_allclose(p.data, [2008.917], atol=1e-03)

        # passing unscale in method should overwrite the defaults
        p = src.point(310000, 4100000, coord_crs=src.dataset.crs, unscale=False)
        numpy.testing.assert_equal(p.data, [8917, 8917])

    cutline = "POLYGON ((13 1685, 1010 6, 2650 967, 1630 2655, 13 1685))"
    with Reader(COGEO, options={"vrt_options": {"cutline": cutline}}) as src:
        _, mask = src.preview()
        assert not mask.all()

    def callback(data):
        data = data * 2
        data.mask = False  # set mask to False
        return data

    with Reader(COGEO, options={"nodata": 1, "post_process": callback}) as src:
        data_init, _ = src.tile(43, 25, 7, post_process=None)
        data, mask = src.tile(43, 25, 7)
        assert mask.all()
        assert data[0, 0, 0] == data_init[0, 0, 0] * 2

    lon = -56.624124590533825
    lat = 73.52687881825946
    with Reader(COG_NODATA, options={"post_process": callback}) as src:
        pt = src.point(lon, lat)

    with Reader(COG_NODATA) as src:
        pt_init = src.point(lon, lat)
    assert pt.data[0] == pt_init.data[0] * 2


def test_cog_with_internal_gcps():
    """Make sure file gets re-projected using gcps."""
    with Reader(COG_GCPS) as src:
        assert isinstance(src.dataset, WarpedVRT)
        assert src.bounds
        assert src.minzoom == 7
        assert src.maxzoom == 10

        metadata = src.info()
        assert metadata.nodata_type == "Alpha"
        assert len(metadata.band_metadata) == 2
        assert metadata.band_descriptions == [("b1", "b1"), ("b2", "b2")]
        assert metadata.colorinterp == ["gray", "alpha"]

        # The topleft corner should be masked
        assert src.preview(indexes=1).array.mask[0, 0, 0]

        tile_z = 8
        tile_x = 183
        tile_y = 120
        data, mask = src.tile(tile_x, tile_y, tile_z)
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)
    assert src.dataset.closed
    assert src.dataset.src_dataset.closed

    # Pass dataset (should be a WarpedVRT)
    # Do not infer mask/alpha in the VRT
    with rasterio.open(COG_GCPS) as dst:
        with WarpedVRT(
            dst,
            src_crs=dst.gcps[1],
            src_transform=transform.from_gcps(dst.gcps[0]),
        ) as vrt:
            with Reader(None, dataset=vrt) as src:
                assert src.bounds
                assert isinstance(src.dataset, WarpedVRT)
                assert src.minzoom == 7
                assert src.maxzoom == 10

                metadata = src.info()
                assert metadata.nodata_type == "None"
                assert len(metadata.band_metadata) == 1
                assert metadata.band_descriptions == [("b1", "b1")]
                assert metadata.colorinterp == ["gray"]

                # The topleft corner is not masked because we didn't add mask
                assert not src.preview(indexes=1).array.mask[0, 0, 0]

                tile_z = 8
                tile_x = 183
                tile_y = 120
                data, mask = src.tile(tile_x, tile_y, tile_z)
                assert data.shape == (1, 256, 256)
                assert mask.shape == (256, 256)

            assert not src.dataset.closed
            assert not src.dataset.src_dataset.closed

        assert src.dataset.closed
    assert src.dataset.src_dataset.closed


def parse_img(content: bytes) -> Dict[Any, Any]:
    """Read tile image and return metadata."""
    with MemoryFile(content) as mem:
        with mem.open() as dst:
            return dst.meta


def test_imageData_output():
    """Test ImageData output."""
    with Reader(COG_NODATA) as src:
        img = src.tile(43, 24, 7)
        assert img.data.shape == (1, 256, 256)
        assert img._mask.all()
        assert img.count == 1
        assert img.data_as_image().shape == (256, 256, 1)

        assert numpy.array_equal(~img.array.mask[0], img._mask)

        assert img.crs == WEB_MERCATOR_TMS.crs
        assert img.bounds == WEB_MERCATOR_TMS.xy_bounds(43, 24, 7)

        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["driver"] == "GTiff"
        assert meta["crs"] == WEB_MERCATOR_TMS.crs
        assert meta["transform"]
        assert meta["count"] == 2

        res = img.render(img_format="NPY")
        arr = numpy.load(BytesIO(res))
        assert numpy.array_equal(arr[0:1], img.data)
        assert numpy.array_equal(arr[1], img.mask)

        img = src.tile(43, 24, 7)
        assert img.data.dtype == "uint16"

        imgc = img.post_process(color_formula="Gamma R 3.1")
        assert imgc.data.dtype == "uint8"

        imgr = img.post_process(in_range=((img.data.min(), img.data.max()),))
        assert not numpy.array_equal(img.data, imgr.data)
        assert imgr.data.dtype == "uint8"
        assert imgr.data.min() == 0
        assert imgr.data.max() == 255
        assert imgr.bounds == img.bounds
        assert imgr.crs == img.crs
        assert imgr.assets == img.assets

        imgc = imgr.post_process(color_formula="Gamma R 3.1")
        assert not numpy.array_equal(imgc.data, imgr.data)
        assert imgc.data.dtype == "uint8"
        assert imgc.bounds == img.bounds
        assert imgc.crs == img.crs
        assert imgc.assets == img.assets

        imgrc = img.post_process(
            in_range=((img.data.min(), img.data.max()),), color_formula="Gamma R 3.1"
        )
        assert numpy.array_equal(imgc.data, imgrc.data)

        bbox = (
            -56.624124590533825,
            73.50183615350426,
            -56.530950796449005,
            73.52687881825946,
        )
        img = src.part(bbox)
        assert img.data.shape == (1, 11, 40)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == WGS84_CRS
        assert img.bounds == bbox

        img = src.part(bbox, dst_crs=src.dataset.crs)
        assert img.data.shape == (1, 28, 30)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == src.dataset.crs
        assert not img.bounds == bbox

        img = src.preview(max_size=128)
        assert img.data.shape == (1, 128, 128)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == src.dataset.crs
        # Bounds should be the same but VRT might introduce some rounding issue
        for x, y in zip(img.bounds, src.dataset.bounds):
            assert round(x, 5) == round(y, 5)
        # assert img.bounds == src.dataset.bounds


def test_feature_valid():
    """Read from feature."""
    feature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-56.4697265625, 74.17307693616263],
                    [-57.667236328125, 73.53462847039683],
                    [-57.59033203125, 73.13451013251789],
                    [-56.195068359375, 72.94865294642922],
                    [-54.964599609375, 72.96797135377102],
                    [-53.887939453125, 73.84623016391944],
                    [-53.97583007812499, 74.0165183926664],
                    [-54.73388671875, 74.23289305339864],
                    [-55.54687499999999, 74.2269213699517],
                    [-56.129150390625, 74.21497138945001],
                    [-56.2060546875, 74.21198251594369],
                    [-56.4697265625, 74.17307693616263],
                ]
            ],
        },
    }

    with Reader(COG_NODATA) as src:
        img = src.feature(feature, max_size=1024)
        assert img.data.shape == (1, 348, 1024)
        assert img.band_names == ["b1"]

        img = src.feature(feature, dst_crs=src.dataset.crs, max_size=1024)
        assert img.data.shape == (1, 1024, 869)

        img = src.feature(feature, max_size=30)
        assert img.data.shape == (1, 11, 30)

        img = src.feature(feature, expression="b1*2;b1-100", max_size=1024)
        assert img.data.shape == (2, 348, 1024)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.feature(
                feature, indexes=(1, 2, 3), expression="b1*2", max_size=1024
            )
            assert img.data.shape == (1, 348, 1024)
            assert img.band_descriptions == ["b1*2"]

        img = src.feature(feature, indexes=1, max_size=1024)
        assert img.data.shape == (1, 348, 1024)

        img = src.feature(
            feature,
            indexes=(
                1,
                1,
            ),
            max_size=1024,
        )
        assert img.data.shape == (2, 348, 1024)
        assert img.band_descriptions == ["b1", "b1"]

        # feature overlaping on mask area
        mask_feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-54.45922851562499, 73.05143929453952],
                        [-55.052490234375, 72.79658820490461],
                        [-55.61279296874999, 72.46203877644956],
                        [-53.8330078125, 72.36244812858165],
                        [-54.45922851562499, 73.05143929453952],
                    ]
                ],
            },
        }

        img = src.feature(mask_feat, max_size=1024)
        assert not img._mask.all()

        outside_mask_feature = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-57.3486328125, 72.25226599952339],
                        [-57.041015625, 72.1279362810559],
                        [-56.722412109375, 72.06038062953813],
                        [-54.86572265625, 72.07052969916067],
                        [-54.613037109375, 72.63665259171732],
                        [-56.14013671875, 72.90995232978632],
                        [-57.3486328125, 72.25226599952339],
                    ]
                ],
            },
        }
        img = src.feature(outside_mask_feature, max_size=1024)
        assert not img._mask.all()


def test_equality_part_feature():
    """Make sure the `feature` method returns the same thing as part+cutline."""
    with Reader(COG_NODATA) as src:
        feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-57.3486328125, 72.25226599952339],
                        [-57.041015625, 72.1279362810559],
                        [-56.722412109375, 72.06038062953813],
                        [-54.86572265625, 72.07052969916067],
                        [-54.613037109375, 72.63665259171732],
                        [-56.14013671875, 72.90995232978632],
                        [-57.3486328125, 72.25226599952339],
                    ]
                ],
            },
        }
        img_feat = src.feature(feat)

        cutline = create_cutline(src.dataset, feat, geometry_crs="epsg:4326")
        bbox = featureBounds(feat)
        img_part = src.part(bbox, vrt_options={"cutline": cutline})

        assert img_feat.mask[0, 0] == img_part.mask[0, 0]
        assert img_feat.mask[200, 200] == img_part.mask[200, 200]

        # NOTE: both mask are almost equal but except pixel on the top of the image
        # I would assume this is due to rounding issue or reprojection of the cutline by GDAL
        # After some debugging locally I found out the rasterized mask is more precise
        # numpy.testing.assert_array_equal(img_part.mask, img_feat.mask)
        # NOTE reply: can this rounding be fixed with a different operator passed to rasterio rowcol?

        # Re-Projection
        img_feat = src.feature(feat, dst_crs="epsg:3857")

        cutline = create_cutline(src.dataset, feat, geometry_crs="epsg:4326")
        bbox = featureBounds(feat)
        img_part = src.part(bbox, vrt_options={"cutline": cutline}, dst_crs="epsg:3857")

        assert img_feat.mask[0, 0] == img_part.mask[0, 0]
        assert img_feat.mask[200, 200] == img_part.mask[200, 200]


def test_tiling_ignores_padding_if_web_friendly_internal_tiles_exist():
    """Ignore Padding when COG is aligned."""
    with Reader(COG_WEB) as src:
        img = src.tile(147, 182, 9, padding=0, resampling_method="bilinear")
        img2 = src.tile(147, 182, 9, padding=100, resampling_method="bilinear")
        assert numpy.array_equal(img.data, img2.data)

    with Reader(COGEO) as src:
        img = src.tile(43, 24, 7, padding=0, resampling_method="bilinear")
        img2 = src.tile(43, 24, 7, padding=100, resampling_method="bilinear")
        assert not numpy.array_equal(img.data, img2.data)


def test_tile_read_alpha():
    """Read masked area."""
    # non-boundless tile covering the alpha masked part
    with Reader(COG_ALPHA) as src:
        nb = src.dataset.count
        img = src.tile(876432, 1603670, 22)
        assert (
            not nb == img.count
        )  # rio-tiler removes the alpha band from the `data` array
        assert img.data.shape == (3, 256, 256)
        assert not img._mask.all()


def test_tile_read_mask():
    """Read masked area."""
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR"):
        # non-boundless tile covering the masked part
        with Reader(COG_MASK) as src:
            img = src.tile(876431, 1603669, 22, tilesize=16)
            assert img.data.shape == (3, 16, 16)
            assert img.mask.shape == (16, 16)
            assert not img._mask.all()

            # boundless tile covering the masked part
            img = src.tile(876431, 1603668, 22, tilesize=256)
            assert img.data.shape == (3, 256, 256)
            assert not img._mask.all()


def test_tile_read_extmask():
    """Read masked area."""
    # non-boundless tile covering the masked part
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="TRUE"):
        with Reader(COG_EXTMASK) as src:
            img = src.tile(876431, 1603669, 22)
            assert img.data.shape == (3, 256, 256)
            assert img.mask.shape == (256, 256)
            assert not img._mask.all()


def test_dateline():
    """Read tile from data crossing the antimeridian."""
    with Reader(COG_DLINE) as src:
        img = src.tile(0, 84, 8, tilesize=64)
        assert img.data.shape == (1, 64, 64)

        img = src.tile(255, 84, 8, tilesize=64)
        assert img.data.shape == (1, 64, 64)


def test_fullEarth():
    """Should read tile for COG spanning the whole earth."""
    with Reader(COG_EARTH) as src:
        img = src.tile(1, 42, 7, tilesize=64)
        assert img.data.shape == (1, 64, 64)

        img = src.tile(127, 42, 7, tilesize=64)
        assert img.data.shape == (1, 64, 64)

    with Reader(COG_EARTH, tms=morecantile.tms.get("EuropeanETRS89_LAEAQuad")) as src:
        img = src.tile(0, 0, 1, tilesize=64)
        assert img.data.shape == (1, 64, 64)


def test_read():
    """Should read the entire dataset."""
    with Reader(COGEO) as src:
        img = src.read()
        assert numpy.array_equal(img.data, src.dataset.read(indexes=(1,)))
        assert img.width == src.dataset.width
        assert img.height == src.dataset.height
        assert img.count == src.dataset.count

        with pytest.warns(ExpressionMixingWarning):
            img = src.read(indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 2667, 2658)

        img = src.read(indexes=1)
        assert img.data.shape == (1, 2667, 2658)

        img = src.read(
            indexes=(
                1,
                1,
            )
        )
        assert img.data.shape == (2, 2667, 2658)


def test_no_overviews():
    """Should warns when no overviews are found."""
    with pytest.warns(NoOverviewWarning):
        with Reader(GEOTIFF):
            pass


def test_nonearthbody():
    """Reader should work with non-earth dataset."""
    EUROPA_SPHERE = CRS.from_proj4("+proj=longlat +R=1560800 +no_defs")

    with Reader(COG_EUROPA) as src:
        with pytest.warns(
            UserWarning,
            match="Cannot determine minzoom based on dataset information, will default to TMS minzoom.",
        ):
            assert src.minzoom == 0

        with pytest.warns(
            UserWarning,
            match="Cannot determine maxzoom based on dataset information, will default to TMS maxzoom.",
        ):
            assert src.maxzoom == 24

    # Warns because of zoom level in WebMercator can't be defined
    with Reader(COG_EUROPA) as src:
        assert src.info()
        meta = src.info()
        assert meta.bounds == src.bounds == src.dataset.bounds
        crs = meta.crs
        assert rioCRS.from_user_input(crs) == src.crs

        assert src.get_geographic_bounds(EUROPA_SPHERE)

        img = src.read()
        assert numpy.array_equal(img.data, src.dataset.read(indexes=(1,)))
        assert img.width == src.dataset.width
        assert img.height == src.dataset.height
        assert img.count == src.dataset.count

        img = src.preview()
        assert img.bounds == src.bounds

        part = src.part(src.bounds, bounds_crs=src.crs)
        assert part.bounds == src.bounds

        lon = (src.bounds[0] + src.bounds[2]) / 2
        lat = (src.bounds[1] + src.bounds[3]) / 2
        assert src.point(lon, lat, coord_crs=src.crs).data[0] is not None

    europa_crs = CRS.from_authority("ESRI", 104915)
    tms = TileMatrixSet.custom(
        crs=europa_crs,
        extent=europa_crs.area_of_use.bounds,
        matrix_scale=[2, 1],
    )

    with Reader(COG_EUROPA, tms=tms) as src:
        assert src.info()
        assert src.minzoom == 4
        assert src.maxzoom == 6

        # Get Tile covering the UL corner
        bounds = transform_bounds(src.crs, tms.rasterio_crs, *src.bounds)
        t = tms._tile(bounds[0], bounds[1], src.minzoom)
        img = src.tile(t.x, t.y, t.z)

        assert img.height == 256
        assert img.width == 256
        assert img.crs == tms.rasterio_crs


def test_nonearth_custom():
    """Test Custom geographic_crs."""
    MARS2000_SPHERE = CRS.from_proj4("+proj=longlat +R=3396190 +no_defs")
    MARS_MERCATOR = CRS.from_proj4(
        "+proj=merc +R=3396190 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +no_defs"
    )

    mars_tms = TileMatrixSet.custom(
        [
            -179.9999999999996,
            -85.05112877980656,
            179.9999999999996,
            85.05112877980656,
        ],
        MARS_MERCATOR,
        extent_crs=MARS2000_SPHERE,
        title="Web Mercator Mars",
    )

    with Reader(COG_MARS, tms=mars_tms) as src:
        assert src.get_geographic_bounds(MARS2000_SPHERE)[0] > -180
        assert src.get_geographic_bounds(mars_tms.rasterio_geographic_crs)[0] > -180


def test_tms_tilesize_and_zoom():
    """Test the influence of tms tilesize on COG zoom levels."""
    with Reader(COG_NODATA) as src:
        assert src.minzoom == 5
        assert src.maxzoom == 9

    tms_128 = TileMatrixSet.custom(
        WEB_MERCATOR_TMS.xy_bbox,
        CRS.from_epsg(3857),
        title="mercator with 64 tilesize",
        tile_width=64,
        tile_height=64,
    )
    with Reader(COG_NODATA, tms=tms_128) as src:
        assert src.minzoom == 5
        assert src.maxzoom == 11

    tms_2048 = TileMatrixSet.custom(
        WEB_MERCATOR_TMS.xy_bbox,
        CRS.from_epsg(3857),
        title="mercator with 2048 tilesize",
        tile_width=2048,
        tile_height=2048,
    )
    with Reader(COG_NODATA, tms=tms_2048) as src:
        assert src.minzoom == 5
        assert src.maxzoom == 6


def test_metadata_img():
    """Check metadata in ImageData."""
    with Reader(COG_TAGS) as src:
        img = src.preview()
        assert img.dataset_statistics
        assert img.metadata
        assert img.band_names == ["b1"]
        assert img.band_descriptions == ["Green"]

        stats = src.statistics()
        assert "b1" in stats
        assert stats["b1"].description == "Green"

        img = src.preview(expression="b1*2")
        assert img.band_descriptions == ["Green*2"]


def test_feature_statistics():
    """Test feature statistics method implemented in titiler."""
    # square
    square = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": [
                [
                    [-56.85853679288809, 73.6870721652219],
                    [-56.85853679288809, 73.18595963998644],
                    [-54.97274279983506, 73.18595963998644],
                    [-54.97274279983506, 73.6870721652219],
                    [-56.85853679288809, 73.6870721652219],
                ]
            ],
            "type": "Polygon",
        },
    }

    square_crs = {
        "type": "Polygon",
        "coordinates": [
            [
                [442337.0, 8175239.0],
                [517915.0, 8175239.0],
                [517915.0, 8134628.0],
                [442337.0, 8134628.0],
                [442337.0, 8175239.0],
            ]
        ],
    }

    # Case 1 - image should be aligned with the bounds
    # because we reproject to the shape crs
    with Reader(COGEO) as src:
        image = src.feature(
            square,
            dst_crs=WGS84_CRS,
            shape_crs=WGS84_CRS,
        )
        coverage_array = image.get_coverage_array(
            square,
            shape_crs=WGS84_CRS,
        )
        stats = image.statistics(coverage=coverage_array)
        assert numpy.unique(coverage_array).tolist() == [1.0]

    # Case 2 - image not aligned with bounds because we align the
    # bounds to the reprojected dataset
    with Reader(COGEO) as src:
        image = src.feature(
            square,
            dst_crs=WGS84_CRS,
            shape_crs=WGS84_CRS,
            align_bounds_with_dataset=True,
        )
        coverage_array = image.get_coverage_array(
            square,
            shape_crs=WGS84_CRS,
        )
        stats_align = image.statistics(coverage=coverage_array)
        assert not numpy.unique(coverage_array).tolist() == [1.0]

        assert stats["b1"].mean != stats_align["b1"].mean

    # Case 3 - square geometry in dataset CRS
    with Reader(COGEO) as src:
        image = src.feature(
            square_crs,
            dst_crs=src.crs,
            shape_crs=src.crs,
        )
        coverage_array = image.get_coverage_array(
            square_crs,
            shape_crs=src.crs,
        )
        stats = image.statistics(coverage=coverage_array)
        assert numpy.unique(coverage_array).tolist() == [1.0]

    # Case 4 - square geometry in dataset CRS but aligned with dataset
    with Reader(COGEO) as src:
        image = src.feature(
            square_crs,
            dst_crs=src.crs,
            shape_crs=src.crs,
            align_bounds_with_dataset=True,
        )
        coverage_array = image.get_coverage_array(
            square_crs,
            shape_crs=src.crs,
        )
        stats_align = image.statistics(coverage=coverage_array)
        assert not numpy.unique(coverage_array).tolist() == [1.0]

        assert stats["b1"].mean != stats_align["b1"].mean


def test_inverted_latitude():
    """Test working with inverted Latitude."""
    with pytest.warns(UserWarning):
        with Reader(COG_INVERTED) as src:
            assert (
                src.get_geographic_bounds(WGS84_CRS)[1]
                < src.get_geographic_bounds(WGS84_CRS)[3]
            )

    with pytest.warns(UserWarning):
        with Reader(COG_INVERTED) as src:
            _ = src.tile(0, 0, 0)


def test_int16_colormap():
    """Should raise a warning about invalid data type for applying colormap.

    ref: https://github.com/developmentseed/titiler/issues/1023
    """
    data = os.path.join(PREFIX, "cog_int16.tif")
    color_map = cmap.get("viridis")

    with Reader(data) as src:
        info = src.info()
        assert info.dtype == "int16"
        assert info.nodata_type == "Nodata"
        assert info.nodata_value == -32768

        img = src.preview()
        assert img._mask.any()

        with pytest.warns(UserWarning):
            im = img.apply_colormap(color_map)

            # make sure we keep the nodata part masked
            assert not im._mask.all()


def test_titiler_issue_1163_warpedVrt():
    """When using GCPs we are creating a WarpedVRT we should still be able
    to perform `boundless` part read.
    """
    with Reader(COG_GCPS) as src:
        assert isinstance(src.dataset, WarpedVRT)
        assert src.dataset.crs == "epsg:4326"

        img = src.part(
            (75.0, 9.0, 77.0, 10.0), bounds_crs="epsg:4326", width=500, height=500
        )
        assert img.statistics()["b1"].valid_percent


def test_unscale_stats():
    """check if scale/offset were applied on stats."""
    with Reader(COG_SCALE_STATS) as src:
        img = src.read(unscale=True)
        assert img.scales == [1.0, 1.0]
        assert img.offsets == [0.0, 0.0]
        stats = img.statistics()
        minb1, maxb1 = stats["b1"].min, stats["b1"].max

        assert pytest.approx(img.dataset_statistics[0][0]) == pytest.approx(minb1)
        assert pytest.approx(img.dataset_statistics[0][1]) == pytest.approx(maxb1)

        img = src.read()
        assert img.scales == [0.0001, 0.001]
        assert img.offsets == [1000.0, 2000.0]
        stats = img.statistics()
        minb1, maxb1 = stats["b1"].min, stats["b1"].max

        assert pytest.approx(img.dataset_statistics[0][0]) == pytest.approx(minb1)
        assert pytest.approx(img.dataset_statistics[0][1]) == pytest.approx(maxb1)


def test_custom_tms():
    """Test tile size per TMS matrix"""
    tms = morecantile.tms.get("WebMercatorQuad").model_dump()
    tms["tileMatrices"][0]["tileHeight"] = 512
    tms["tileMatrices"][0]["tileWidth"] = 512
    web_mercator = morecantile.TileMatrixSet.model_validate(tms)
    with Reader(COGEO, tms=web_mercator) as src:
        tile = src.tile(0, 0, 0)
        assert tile.data.shape == (1, 512, 512)

        tile = src.tile(0, 0, 1)
        assert tile.data.shape == (1, 256, 256)
