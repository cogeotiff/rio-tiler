"""tests rio_tiler.io.cogeo.COGReader"""

import os
import warnings
from io import BytesIO
from typing import Any, Dict

import attr
import morecantile
import numpy
import pytest
import rasterio
from morecantile import TileMatrixSet
from pyproj import CRS
from rasterio import transform
from rasterio.io import MemoryFile
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    AlphaBandWarning,
    ExpressionMixingWarning,
    InvalidBufferSize,
    NoOverviewWarning,
    TileOutsideBounds,
)
from rio_tiler.io import COGReader
from rio_tiler.models import BandStatistics

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

COGEO = os.path.join(PREFIX, "cog.tif")
COG_WEB = os.path.join(PREFIX, "web.tif")
COG_CMAP = os.path.join(PREFIX, "cog_cmap.tif")
COG_TAGS = os.path.join(PREFIX, "cog_tags.tif")
COG_NODATA = os.path.join(PREFIX, "cog_nodata.tif")
COG_SCALE = os.path.join(PREFIX, "cog_scale.tif")
COG_GCPS = os.path.join(PREFIX, "cog_gcps.tif")
COG_DLINE = os.path.join(PREFIX, "cog_dateline.tif")
COG_EARTH = os.path.join(PREFIX, "cog_fullearth.tif")
GEOTIFF = os.path.join(PREFIX, "nocog.tif")
COG_EUROPA = os.path.join(PREFIX, "cog_nonearth.tif")
COG_MARS = os.path.join(PREFIX, "cog_hirise_mars.tif")

KEY_ALPHA = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_alpha.tif"
COG_ALPHA = os.path.join(PREFIX, "my-bucket", KEY_ALPHA)

KEY_MASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_mask.tif"
COG_MASK = os.path.join(PREFIX, "my-bucket", KEY_MASK)

KEY_EXTMASK = "hro_sources/colorado/201404_13SED190110_201404_0x1500m_CL_1_extmask.tif"
COG_EXTMASK = os.path.join(PREFIX, "my-bucket", KEY_EXTMASK)


def test_spatial_info_valid():
    """Should work as expected (get spatial info)"""
    with COGReader(COG_NODATA) as cog:
        assert not cog.dataset.closed
        assert cog.bounds
        assert cog.crs
        assert cog.minzoom == 5
        assert cog.maxzoom == 9
        assert cog.nodata == cog.dataset.nodata
    assert cog.dataset.closed

    cog = COGReader(COG_NODATA)
    assert not cog.dataset.closed
    cog.close()
    assert cog.dataset.closed


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
        assert meta.width
        assert meta.height
        assert meta.count
        assert meta.overviews
        assert meta.driver

    with COGReader(COG_CMAP) as cog:
        assert cog.colormap
        meta = cog.info()
        assert meta["colormap"]
        assert meta.colormap

    with COGReader(COG_NODATA, colormap={1: (0, 0, 0, 0)}) as cog:
        assert cog.colormap
        meta = cog.info()
        assert meta.colormap
        assert meta.nodata_value

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
        assert band_meta[0] == "b1"
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


def test_tile_valid_default():
    """Should return a 3 bands array and a full valid mask."""
    with COGReader(COG_NODATA) as cog:
        # Full tile
        img = cog.tile(43, 24, 7)
        assert img.data.shape == (1, 256, 256)
        assert img.mask.all()
        assert img.band_names == ["b1"]

        # Validate that Tile and Part gives the same result
        tile_bounds = WEB_MERCATOR_TMS.xy_bounds(43, 24, 7)
        data_part, _ = cog.part(
            tile_bounds,
            bounds_crs=WEB_MERCATOR_TMS.crs,
            width=256,
            height=256,
            max_size=None,
        )
        assert numpy.array_equal(img.data, data_part)

        # Partial tile
        data, mask = cog.tile(42, 24, 7)
        assert data.shape == (1, 256, 256)
        assert not mask.all()

        # Expression
        img = cog.tile(43, 24, 7, expression="b1*2;b1-100")
        assert img.data.shape == (2, 256, 256)
        assert img.band_names == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = cog.tile(43, 24, 7, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 256, 256)
        assert img.band_names == ["b1*2"]

        data, mask = cog.tile(43, 24, 7, indexes=1)
        assert data.shape == (1, 256, 256)

        img = cog.tile(
            43,
            24,
            7,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 256, 256)
        assert img.band_names == ["b1", "b1"]

    # We are using a file that is aligned with the grid so no resampling should be involved
    with COGReader(COG_WEB) as cog:
        img = cog.tile(147, 182, 9)
        img_buffer = cog.tile(147, 182, 9, buffer=10)
        assert img_buffer.width == 276
        assert img_buffer.height == 276
        assert not img.bounds == img_buffer.bounds
        assert numpy.array_equal(img.data, img_buffer.data[:, 10:266, 10:266])


def test_tile_invalid_bounds():
    """Should raise an error with invalid tile."""
    with pytest.raises(TileOutsideBounds):
        with COGReader(COGEO) as cog:
            cog.tile(38, 24, 7)


def test_tile_with_incorrect_float_buffer():
    with pytest.raises(InvalidBufferSize):
        with COGReader(COGEO) as cog:
            cog.tile(43, 24, 7, buffer=0.8)


def test_tile_with_int_buffer():
    with COGReader(COGEO) as cog:
        data, mask = cog.tile(43, 24, 7, buffer=1)
    assert data.shape == (1, 258, 258)
    assert mask.all()

    with COGReader(COGEO) as cog:
        data, mask = cog.tile(43, 24, 7, buffer=0)
    assert data.shape == (1, 256, 256)
    assert mask.all()


def test_tile_with_correct_float_buffer():
    with COGReader(COGEO) as cog:
        data, mask = cog.tile(43, 24, 7, buffer=0.5)
    assert data.shape == (1, 257, 257)
    assert mask.all()


def test_point_valid():
    """Read point."""
    lon = -56.624124590533825
    lat = 73.52687881825946
    with COGReader(COG_NODATA) as cog:
        pts = cog.point(lon, lat)
        assert len(pts) == 1

        pts = cog.point(lon, lat, expression="b1*2;b1-100")
        assert len(pts) == 2

        with pytest.warns(ExpressionMixingWarning):
            pts = cog.point(lon, lat, indexes=(1, 2, 3), expression="b1*2")
            assert len(pts) == 1

        pts = cog.point(lon, lat, indexes=1)
        assert len(pts) == 1

        pts = cog.point(
            lon,
            lat,
            indexes=(
                1,
                1,
            ),
        )
        assert len(pts) == 2


def test_area_valid():
    """Read part of an image."""
    bbox = (
        -56.624124590533825,
        73.50183615350426,
        -56.530950796449005,
        73.52687881825946,
    )
    with COGReader(COG_NODATA) as cog:
        img = cog.part(bbox)
        assert img.data.shape == (1, 11, 40)
        assert img.band_names == ["b1"]

        data, mask = cog.part(bbox, dst_crs=cog.dataset.crs)
        assert data.shape == (1, 28, 30)

        data, mask = cog.part(bbox, max_size=30)
        assert data.shape == (1, 9, 30)

        img = cog.part(bbox, expression="b1*2;b1-100")
        assert img.data.shape == (2, 11, 40)
        assert img.band_names == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = cog.part(bbox, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 11, 40)
            assert img.band_names == ["b1*2"]

        data, mask = cog.part(bbox, indexes=1)
        assert data.shape == (1, 11, 40)

        img = cog.part(
            bbox,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 11, 40)
        assert img.band_names == ["b1", "b1"]


def test_preview_valid():
    """Read preview."""
    with COGReader(COGEO) as cog:
        img = cog.preview(max_size=128)
        assert img.data.shape == (1, 128, 128)
        assert img.band_names == ["b1"]

        data, mask = cog.preview()
        assert data.shape == (1, 1024, 1021)

        img = cog.preview(max_size=128, expression="b1*2;b1-100")
        assert img.data.shape == (2, 128, 128)
        assert img.band_names == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = cog.preview(max_size=128, indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 128, 128)
            assert img.band_names == ["b1*2"]

        data, mask = cog.preview(max_size=128, indexes=1)
        assert data.shape == (1, 128, 128)

        img = cog.preview(
            max_size=128,
            indexes=(
                1,
                1,
            ),
        )
        assert img.data.shape == (2, 128, 128)
        assert img.band_names == ["b1", "b1"]


def test_statistics():
    """tests statistics method."""
    with COGReader(COGEO) as cog:
        stats = cog.statistics()
        assert len(stats) == 1
        assert isinstance(stats["b1"], BandStatistics)
        assert stats["b1"].percentile_2
        assert stats["b1"].percentile_98

    with COGReader(COGEO) as cog:
        stats = cog.statistics(percentiles=[3])
        assert stats["b1"].percentile_3

    with COGReader(COGEO) as cog:
        stats = cog.statistics(percentiles=[3])
        assert stats["b1"].percentile_3

    with COGReader(COG_CMAP) as cog:
        stats = cog.statistics(categorical=True)
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

        stats = cog.statistics(categorical=True, categories=[1, 3])
        assert stats["b1"].histogram[1] == [
            1.0,
            3.0,
        ]

    # make sure kwargs are passed to `preview`
    with COGReader(COGEO) as cog:
        stats = cog.statistics(width=100, height=100, max_size=None)
        assert stats["b1"].count == 10000.0

    # Check results for expression
    with COGReader(COGEO) as cog:
        stats = cog.statistics(expression="b1;b1*2")
        assert stats["b1"]
        assert stats["b1*2"]
        assert stats["b1"].min == stats["b1*2"].min / 2


def test_COGReader_Options():
    """Set options in reader."""
    with COGReader(COGEO, nodata=1) as cog:
        assert cog.nodata == 1

    with COGReader(COGEO) as cog:
        assert not cog.nodata
        assert cog.info().nodata_type == "None"

    with COGReader(COGEO, nodata=1) as cog:
        _, mask = cog.tile(43, 25, 7)
        assert not mask.all()

    # read cog using default Nearest
    with COGReader(COGEO, nodata=1) as cog:
        data_default, _ = cog.tile(43, 25, 7)

    # read cog using bilinear
    with COGReader(COGEO, nodata=1, resampling_method="bilinear") as cog:
        data, _ = cog.tile(43, 25, 7)
        assert not numpy.array_equal(data_default, data)

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
    with COGReader(COG_GCPS, nodata=0) as cog:
        assert cog.bounds
        assert cog.nodata == 0
        assert isinstance(cog.dataset, WarpedVRT)

        assert cog.minzoom == 7
        assert cog.maxzoom == 10

        metadata = cog.info()
        assert len(metadata.band_metadata) == 1
        assert metadata.band_descriptions == [("b1", "")]

        tile_z = 8
        tile_x = 183
        tile_y = 120
        data, mask = cog.tile(tile_x, tile_y, tile_z)
        assert data.shape == (1, 256, 256)
        assert mask.shape == (256, 256)
    assert cog.dataset.closed
    assert cog.dataset.src_dataset.closed

    # Pass dataset (should be a WarpedVRT)
    with rasterio.open(COG_GCPS) as dst:
        with WarpedVRT(
            dst,
            src_crs=dst.gcps[1],
            src_transform=transform.from_gcps(dst.gcps[0]),
        ) as vrt:
            with COGReader(None, dataset=vrt, nodata=0) as cog:
                assert cog.bounds
                assert cog.nodata == 0
                assert isinstance(cog.dataset, WarpedVRT)

                assert cog.minzoom == 7
                assert cog.maxzoom == 10

                metadata = cog.info()
                assert len(metadata.band_metadata) == 1
                assert metadata.band_descriptions == [("b1", "")]

                tile_z = 8
                tile_x = 183
                tile_y = 120
                data, mask = cog.tile(tile_x, tile_y, tile_z)
                assert data.shape == (1, 256, 256)
                assert mask.shape == (256, 256)

            assert not cog.dataset.closed
            assert not cog.dataset.src_dataset.closed

        assert cog.dataset.closed
    assert cog.dataset.src_dataset.closed


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
        assert numpy.array_equal(arr[0:1], img.data)
        assert numpy.array_equal(arr[1], img.mask)

        img = cog.tile(43, 24, 7)
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
        img = cog.part(bbox)
        assert img.data.shape == (1, 11, 40)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == WGS84_CRS
        assert img.bounds == bbox

        img = cog.part(bbox, dst_crs=cog.dataset.crs)
        assert img.data.shape == (1, 28, 30)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == cog.dataset.crs
        assert not img.bounds == bbox

        img = cog.preview(max_size=128)
        assert img.data.shape == (1, 128, 128)
        meta = parse_img(img.render(img_format="GTiff"))
        assert meta["crs"] == cog.dataset.crs
        # Bounds should be the same but VRT might introduce some rounding issue
        for x, y in zip(img.bounds, cog.dataset.bounds):
            assert round(x, 5) == round(y, 5)
        # assert img.bounds == cog.dataset.bounds


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

    with COGReader(COG_NODATA) as cog:
        img = cog.feature(feature, max_size=1024)
        assert img.data.shape == (1, 348, 1024)
        assert img.band_names == ["b1"]

        img = cog.feature(feature, dst_crs=cog.dataset.crs, max_size=1024)
        assert img.data.shape == (1, 1024, 869)

        img = cog.feature(feature, max_size=30)
        assert img.data.shape == (1, 11, 30)

        img = cog.feature(feature, expression="b1*2;b1-100", max_size=1024)
        assert img.data.shape == (2, 348, 1024)
        assert img.band_names == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = cog.feature(
                feature, indexes=(1, 2, 3), expression="b1*2", max_size=1024
            )
            assert img.data.shape == (1, 348, 1024)
            assert img.band_names == ["b1*2"]

        img = cog.feature(feature, indexes=1, max_size=1024)
        assert img.data.shape == (1, 348, 1024)

        img = cog.feature(
            feature,
            indexes=(
                1,
                1,
            ),
            max_size=1024,
        )
        assert img.data.shape == (2, 348, 1024)
        assert img.band_names == ["b1", "b1"]

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

        img = cog.feature(mask_feat, max_size=1024)
        assert not img.mask.all()

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
        img = cog.feature(outside_mask_feature, max_size=1024)
        assert not img.mask.all()


def test_tiling_ignores_padding_if_web_friendly_internal_tiles_exist():
    """Ignore Padding when COG is aligned."""
    with COGReader(COG_WEB) as cog:
        img = cog.tile(147, 182, 9, padding=0, resampling_method="bilinear")
        img2 = cog.tile(147, 182, 9, padding=100, resampling_method="bilinear")
        assert numpy.array_equal(img.data, img2.data)

    with COGReader(COGEO) as cog:
        img = cog.tile(43, 24, 7, padding=0, resampling_method="bilinear")
        img2 = cog.tile(43, 24, 7, padding=100, resampling_method="bilinear")
        assert not numpy.array_equal(img.data, img2.data)


def test_tile_read_alpha():
    """Read masked area."""
    # non-boundless tile covering the alpha masked part
    with COGReader(COG_ALPHA) as cog:
        with pytest.warns(AlphaBandWarning):
            nb = cog.dataset.count
            img = cog.tile(876432, 1603670, 22)
            assert (
                not nb == img.count
            )  # rio-tiler removes the alpha band from the `data` array
            assert img.data.shape == (3, 256, 256)
            assert not img.mask.all()


def test_tile_read_mask():
    """Read masked area."""
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR"):
        # non-boundless tile covering the masked part
        with COGReader(COG_MASK) as cog:
            img = cog.tile(876431, 1603669, 22, tilesize=16)
            assert img.data.shape == (3, 16, 16)
            assert img.mask.shape == (16, 16)
            assert not img.mask.all()

            # boundless tile covering the masked part
            img = cog.tile(876431, 1603668, 22, tilesize=256)
            assert img.data.shape == (3, 256, 256)
            assert not img.mask.all()


def test_tile_read_extmask():
    """Read masked area."""
    # non-boundless tile covering the masked part
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="TRUE"):
        with COGReader(COG_EXTMASK) as cog:
            img = cog.tile(876431, 1603669, 22)
            assert img.data.shape == (3, 256, 256)
            assert img.mask.shape == (256, 256)
            assert not img.mask.all()


def test_dateline():
    """Read tile from data crossing the antimeridian."""
    with COGReader(COG_DLINE) as cog:
        img = cog.tile(0, 84, 8, tilesize=64)
        assert img.data.shape == (1, 64, 64)

        img = cog.tile(255, 84, 8, tilesize=64)
        assert img.data.shape == (1, 64, 64)


def test_fullEarth():
    """Should read tile for COG spanning the whole earth."""
    with COGReader(COG_EARTH) as cog:
        img = cog.tile(1, 42, 7, tilesize=64)
        assert img.data.shape == (1, 64, 64)

        img = cog.tile(127, 42, 7, tilesize=64)
        assert img.data.shape == (1, 64, 64)

    with COGReader(
        COG_EARTH, tms=morecantile.tms.get("EuropeanETRS89_LAEAQuad")
    ) as cog:
        img = cog.tile(0, 0, 1, tilesize=64)
        assert img.data.shape == (1, 64, 64)


def test_read():
    """Should read the entire dataset."""
    with COGReader(COGEO) as cog:
        img = cog.read()
        assert numpy.array_equal(img.data, cog.dataset.read(indexes=(1,)))
        assert img.width == cog.dataset.width
        assert img.height == cog.dataset.height
        assert img.count == cog.dataset.count

        with pytest.warns(ExpressionMixingWarning):
            img = cog.read(indexes=(1, 2, 3), expression="b1*2")
            assert img.data.shape == (1, 2667, 2658)

        img = cog.read(indexes=1)
        assert img.data.shape == (1, 2667, 2658)

        img = cog.read(
            indexes=(
                1,
                1,
            )
        )
        assert img.data.shape == (2, 2667, 2658)


def test_no_overviews():
    """Should warns when no overviews are found."""
    with pytest.warns(NoOverviewWarning):
        with COGReader(GEOTIFF):
            pass


def test_nonearthbody():
    """COGReader should work with non-earth dataset."""
    EUROPA_SPHERE = CRS.from_proj4("+proj=longlat +R=1560800 +no_defs")

    with pytest.warns(UserWarning):
        with COGReader(COG_EUROPA) as cog:
            assert cog.minzoom == 0
            assert cog.maxzoom == 24

    # Warns because of zoom level in WebMercator can't be defined
    with pytest.warns(UserWarning) as warnings:
        with COGReader(COG_EUROPA, geographic_crs=EUROPA_SPHERE) as cog:
            assert cog.info()
            assert len(warnings) == 2

            img = cog.read()
            assert numpy.array_equal(img.data, cog.dataset.read(indexes=(1,)))
            assert img.width == cog.dataset.width
            assert img.height == cog.dataset.height
            assert img.count == cog.dataset.count

            img = cog.preview()
            assert img.bounds == cog.bounds

            part = cog.part(cog.bounds, bounds_crs=cog.crs)
            assert part.bounds == cog.bounds

            lon = (cog.bounds[0] + cog.bounds[2]) / 2
            lat = (cog.bounds[1] + cog.bounds[3]) / 2
            assert cog.point(lon, lat, coord_crs=cog.crs)[0] is not None

    with pytest.warns(UserWarning) as warnings:
        europa_crs = CRS.from_authority("ESRI", 104915)
        tms = TileMatrixSet.custom(
            crs=europa_crs,
            extent=europa_crs.area_of_use.bounds,
            matrix_scale=[2, 1],
        )

    with COGReader(COG_EUROPA, tms=tms, geographic_crs=EUROPA_SPHERE) as cog:
        assert cog.info()
        assert cog.minzoom == 4
        assert cog.maxzoom == 6

        # Get Tile covering the UL corner
        bounds = transform_bounds(cog.crs, tms.rasterio_crs, *cog.bounds)
        t = tms._tile(bounds[0], bounds[1], cog.minzoom)
        img = cog.tile(t.x, t.y, t.z)

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
        geographic_crs=MARS2000_SPHERE,
    )

    @attr.s
    class MarsReader(COGReader):
        """Use custom geographic CRS."""

        geographic_crs: rasterio.crs.CRS = attr.ib(
            init=False,
            default=rasterio.crs.CRS.from_proj4("+proj=longlat +R=3396190 +no_defs"),
        )

    with warnings.catch_warnings():
        with MarsReader(COG_MARS, tms=mars_tms) as cog:
            assert cog.geographic_bounds[0] > -180

    with warnings.catch_warnings():
        with COGReader(
            COG_MARS,
            tms=mars_tms,
            geographic_crs=rasterio.crs.CRS.from_proj4(
                "+proj=longlat +R=3396190 +no_defs"
            ),
        ) as cog:
            assert cog.geographic_bounds[0] > -180


def test_tms_tilesize_and_zoom():
    """Test the influence of tms tilesize on COG zoom levels."""
    with COGReader(COG_NODATA) as cog:
        assert cog.minzoom == 5
        assert cog.maxzoom == 9

    tms_128 = TileMatrixSet.custom(
        WEB_MERCATOR_TMS.xy_bbox,
        WEB_MERCATOR_TMS.crs,
        title="mercator with 64 tilesize",
        tile_width=64,
        tile_height=64,
    )
    with COGReader(COG_NODATA, tms=tms_128) as cog:
        assert cog.minzoom == 5
        assert cog.maxzoom == 11

    tms_2048 = TileMatrixSet.custom(
        WEB_MERCATOR_TMS.xy_bbox,
        WEB_MERCATOR_TMS.crs,
        title="mercator with 2048 tilesize",
        tile_width=2048,
        tile_height=2048,
    )
    with COGReader(COG_NODATA, tms=tms_2048) as cog:
        print(cog.minzoom, cog.maxzoom)
        assert cog.minzoom == 5
        assert cog.maxzoom == 6
