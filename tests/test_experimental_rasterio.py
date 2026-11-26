"""test for experimental rasterio Reader."""

import os
import warnings

import numpy
import pytest
import rasterio
from rasterio.vrt import WarpedVRT

from rio_tiler.errors import (
    ExpressionMixingWarning,
    InvalidBufferSize,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.experimental.rasterio import Reader as ExpReader
from rio_tiler.io import Reader
from rio_tiler.models import BandStatistics

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")


def _path(name: str) -> str:
    return os.path.join(PREFIX, name)


@pytest.mark.parametrize(
    "src_path,nodata",
    [
        ("cog.tif", None),
        ("cog_nodata.tif", 1),
        ("cog_cmap.tif", 0),
        ("nocog.tif", None),
    ],
)
def test_reader(src_path, nodata):
    """tests reader init."""
    with ExpReader(_path(src_path)) as src, Reader(_path(src_path)) as sync_src:
        assert src.bounds == sync_src.bounds
        assert src.crs == sync_src.crs
        assert src.transform == sync_src.transform
        assert src.height == sync_src.height
        assert src.width == sync_src.width
        assert src.dataset.nodata == nodata
        assert src.colormap == sync_src.colormap


def test_reader_gcps():
    """Dataset with GCPS are opened through a WarpedVRT."""
    with ExpReader(_path("cog_gcps.tif")) as src:
        assert isinstance(src.dataset, WarpedVRT)
        img = src.preview(max_size=128)
        assert max(img.width, img.height) == 128


def test_get_decimation(monkeypatch):
    """Overview decimation selection (GDAL's rule).

    Select the most downsampled overview whose factor is < desired * threshold + 0.1,
    with threshold = 1.2 for `nearest` and 1.0 for other resampling methods.
    """
    with ExpReader(_path("cog.tif")) as src:
        assert src.dataset.overviews(1) == [2, 4, 8, 16]
        # upsampling or full resolution
        assert src._get_decimation(0.5) == 1
        assert src._get_decimation(1) == 1
        assert src._get_decimation(2) == 2
        assert src._get_decimation(1000) == 16

        # nearest: an overview up to ~1.2x coarser than the output can be used
        assert src._get_decimation(1.4) == 1  # 2 >= 1.4 * 1.2 + 0.1
        assert src._get_decimation(1.6) == 2  # 2 < 1.6 * 1.2 + 0.1
        assert src._get_decimation(3.5) == 4  # 4 < 3.5 * 1.2 + 0.1

        # other methods: never use an overview coarser than the output
        assert src._get_decimation(1.6, "bilinear") == 1
        assert src._get_decimation(1.95, "bilinear") == 2  # 2 < 1.95 + 0.1
        assert src._get_decimation(3.5, "cubic") == 2

        # GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD overrides the threshold
        with rasterio.Env(GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD="2"):
            assert src._get_decimation(3.5, "cubic") == 4

        # RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD (read at import) takes precedence
        monkeypatch.setattr("rio_tiler._warp.OVERVIEW_OVERSAMPLING_THRESHOLD", 1.0)
        assert src._get_decimation(1.6) == 1  # 2 >= 1.6 * 1.0 + 0.1
        with rasterio.Env(GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD="2"):
            assert src._get_decimation(3.5, "cubic") == 2

    # No overviews
    with ExpReader(_path("nocog.tif")) as src:
        assert src.dataset.overviews(1) == []
        assert src._get_decimation(1000) == 1


@pytest.mark.parametrize(
    "src_path",
    [
        "cog.tif",
        "cog_nodata.tif",
        "cog_cmap.tif",
        "rgb.tif",
        "cog_rgb_mask.tif",
        "cog_rgba.tif",
        "cog_scale_epsg4326.tif",
        "red.tif",
    ],
)
def test_reader_info(src_path):
    """info is inherited from the rasterio Reader."""
    with ExpReader(_path(src_path)) as src, Reader(_path(src_path)) as sync_src:
        assert src.info() == sync_src.info()


def test_reader_point():
    """tests point() method."""
    with ExpReader(_path("cog.tif")) as src, Reader(_path("cog.tif")) as sync_src:
        pt = src.point(-60, 73)
        sync_pt = sync_src.point(-60, 73)
        assert len(pt.data) == 1
        assert pt.band_names == ["b1"]
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)
        assert pt.band_descriptions == sync_pt.band_descriptions
        assert pt.pixel_location == sync_pt.pixel_location
        assert pt.assets == sync_pt.assets

        pt = src.point(-60, 73, indexes=[1, 1, 1])
        sync_pt = sync_src.point(-60, 73, indexes=[1, 1, 1])
        assert len(pt.data) == 3
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)
        assert pt.band_descriptions == sync_pt.band_descriptions

        pt = src.point(-60, 73, expression="b1*2;b1-100")
        sync_pt = sync_src.point(-60, 73, expression="b1*2;b1-100")
        assert pt.band_descriptions == ["b1*2", "b1-100"]
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

        with pytest.warns(ExpressionMixingWarning):
            pt = src.point(-60, 73, indexes=(1, 1, 1), expression="b1*2")
            assert pt.band_descriptions == ["b1*2"]

        with pytest.raises(PointOutsideBounds):
            src.point(-180, 0)

        # Point in dataset CRS
        x = (src.bounds[0] + src.bounds[2]) / 2
        y = (src.bounds[1] + src.bounds[3]) / 2
        pt = src.point(x, y, coord_crs=src.crs)
        sync_pt = sync_src.point(x, y, coord_crs=sync_src.crs)
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

    with (
        ExpReader(_path("cog_nodata.tif")) as src,
        Reader(_path("cog_nodata.tif")) as sync_src,
    ):
        pt = src.point(-59.53, 74.03, indexes=(1, 1, 1))
        sync_pt = sync_src.point(-59.53, 74.03, indexes=(1, 1, 1))
        assert not pt._mask[0]
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

        # nodata override
        val = int(pt.data[0])
        pt = src.point(-59.53, 74.03, nodata=val)
        sync_pt = sync_src.point(-59.53, 74.03, nodata=val)
        assert not pt._mask[0]
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

    # Test coordinates
    with (
        ExpReader(_path("dataset_2d.tif")) as src,
        Reader(_path("dataset_2d.tif")) as sync_src,
    ):
        for coords in [(0, 0), (0.15, 0.15)]:
            pt = src.point(*coords)
            sync_pt = sync_src.point(*coords)
            numpy.testing.assert_array_equal(sync_pt.array, pt.array)
            assert pt.pixel_location == sync_pt.pixel_location

    with (
        ExpReader(_path("cog_scale_epsg4326.tif")) as src,
        Reader(_path("cog_scale_epsg4326.tif")) as sync_src,
    ):
        pt = src.point(127, 37)
        sync_pt = sync_src.point(127, 37)
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

        pt = src.point(127, 37, unscale=True)
        sync_pt = sync_src.point(127, 37, unscale=True)
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

    # `unscale` from options
    with (
        ExpReader(_path("cog_scale_epsg4326.tif"), options={"unscale": True}) as src,
        Reader(_path("cog_scale_epsg4326.tif"), options={"unscale": True}) as sync_src,
    ):
        numpy.testing.assert_array_equal(
            sync_src.point(127, 37).array, src.point(127, 37).array
        )


def test_reader_point_interpolate():
    """point() with interpolate=True."""
    with ExpReader(_path("cog.tif")) as src, Reader(_path("cog.tif")) as sync_src:
        pt = src.point(-60, 73, interpolate=True, resampling_method="bilinear")
        sync_pt = sync_src.point(-60, 73, interpolate=True, resampling_method="bilinear")
        numpy.testing.assert_array_equal(sync_pt.array, pt.array)

        with pytest.warns(UserWarning, match="resampling will be ignored"):
            src.point(-60, 73, resampling_method="bilinear")

        # Points within half a pixel of the dataset edges
        res = abs(src.transform.a)
        y = (src.bounds[1] + src.bounds[3]) / 2
        for x in [src.bounds[0] + 0.1 * res, src.bounds[2] - 0.1 * res]:
            pt = src.point(
                x,
                y,
                coord_crs=src.crs,
                interpolate=True,
                resampling_method="bilinear",
            )
            assert len(pt.data) == 1


def test_reader_point_rgba_out_dtype():
    """Alpha mask should still be valid when using out_dtype."""
    with ExpReader(_path("cog_rgba.tif")) as src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        lon, lat = (w + e) / 2, (s + n) / 2

        pt = src.point(lon, lat)
        assert pt.array.dtype == numpy.uint8
        assert not pt.array.mask.any()

        pt32 = src.point(lon, lat, out_dtype="float32")
        assert pt32.array.dtype == numpy.float32
        assert not pt32.array.mask.any()
        numpy.testing.assert_array_equal(pt.data, pt32.data)


def test_reader_read():
    """read() returns the full resolution dataset."""
    for src_path in ["cog.tif", "cog_nodata.tif", "cog_rgba.tif"]:
        with ExpReader(_path(src_path)) as src, Reader(_path(src_path)) as sync_src:
            img = src.read()
            sync_img = sync_src.read()
            assert img.bounds == sync_img.bounds
            assert img.crs == sync_img.crs
            assert img.band_names == sync_img.band_names
            assert img.assets == sync_img.assets
            numpy.testing.assert_array_equal(img.array.data, sync_img.array.data)
            numpy.testing.assert_array_equal(img.array.mask, sync_img.array.mask)

    with ExpReader(_path("cog.tif")) as src, Reader(_path("cog.tif")) as sync_src:
        img = src.read(expression="b1*2;b1-100")
        sync_img = sync_src.read(expression="b1*2;b1-100")
        assert img.band_descriptions == ["b1*2", "b1-100"]
        numpy.testing.assert_array_equal(img.array, sync_img.array)


def test_reader_preview():
    """Read preview."""
    with (
        ExpReader(_path("cog_ovr.tif")) as src,
        Reader(_path("cog_ovr.tif")) as sync_src,
    ):
        img = src.preview()
        sync_img = sync_src.preview()
        assert img.array.shape == (1, 1024, 1021)
        assert img.band_descriptions == ["b1"]
        assert img.assets == sync_img.assets
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        img = src.preview(max_size=128)
        sync_img = sync_src.preview(max_size=128)
        assert img.array.shape == (1, 128, 128)
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        img = src.preview(max_size=None)
        sync_img = sync_src.preview(max_size=None)
        assert img.array.shape == (1, 2667, 2658)
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        img = src.preview(dst_crs="epsg:4326")
        sync_img = sync_src.preview(dst_crs="epsg:4326")
        assert img.array.shape == (1, 278, 1024)
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        img = src.preview(dst_crs="epsg:4326", max_size=512)
        sync_img = sync_src.preview(dst_crs="epsg:4326", max_size=512)
        assert img.array.shape == (1, 139, 512)
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        img = src.preview(max_size=128, expression="b1*2;b1-100")
        sync_img = sync_src.preview(max_size=128, expression="b1*2;b1-100")
        assert img.array.shape == (2, 128, 128)
        assert img.band_descriptions == ["b1*2", "b1-100"]
        numpy.testing.assert_array_equal(img.array, sync_img.array)

        with pytest.warns(ExpressionMixingWarning):
            img = src.preview(max_size=128, indexes=(1, 2, 3), expression="b1*2")
            assert img.array.shape == (1, 128, 128)
            assert img.band_descriptions == ["b1*2"]

    with (
        ExpReader(_path("cog_scale_epsg4326.tif")) as src,
        Reader(_path("cog_scale_epsg4326.tif")) as sync_src,
    ):
        img = src.preview(max_size=128)
        sync_img = sync_src.preview(max_size=128)
        numpy.testing.assert_array_equal(sync_img.array, img.array)

        img = src.preview(max_size=128, unscale=True)
        sync_img = sync_src.preview(max_size=128, unscale=True)
        numpy.testing.assert_array_equal(sync_img.array, img.array)
        assert img.dataset_statistics == sync_img.dataset_statistics

    with ExpReader(_path("red.tif")) as src:
        img = src.preview(max_size=128)
        assert img.dataset_statistics == [(6101.0, 65035.0)]


def test_reader_stats():
    """Statistics."""
    with (
        ExpReader(_path("cog_ovr.tif")) as src,
        Reader(_path("cog_ovr.tif")) as sync_src,
    ):
        stats = src.statistics()
        assert len(stats) == 1
        assert isinstance(stats["b1"], BandStatistics)

        sync_stats = sync_src.statistics()
        assert sync_stats["b1"].percentile_2 == stats["b1"].percentile_2
        assert sync_stats["b1"].percentile_98 == stats["b1"].percentile_98

        stats = src.statistics(percentiles=[3])
        assert stats["b1"].percentile_3

        # make sure kwargs are passed to `preview`
        stats = src.statistics(width=100, height=100, max_size=None)
        assert stats["b1"].count == 10000.0

        stats = src.statistics(expression="b1;b1*2")
        assert stats["b1"].description == "b1"
        assert stats["b2"].description == "b1*2"
        assert stats["b1"].min == stats["b2"].min / 2

    with ExpReader(_path("cog_cmap.tif")) as src:
        stats = src.statistics(categorical=True, categories=[1, 3])
        assert stats["b1"].histogram[1] == [1.0, 3.0]


@pytest.mark.parametrize(
    "src_path",
    [
        "cog_uint8_rgb_mask.tif",
        "cog_uint8_rgb_nodata.tif",
        "cog_uint8_rgba.tif",
    ],
)
def test_mask(src_path):
    """Test masks for nodata/mask band/alpha band datasets."""
    with ExpReader(_path(src_path)) as src:
        im = src.preview(max_size=1024)
        assert im.array.shape[0] == 3

        assert im.array.data[0, 0, 0] == 0
        assert im.array.data[0, -1, -1]
        assert im.array.mask[0, 0, 0]
        assert not im.array.mask[0, -1, -1]

        # GDAL Like mask (0 = valid, 255 = invalid)
        assert im.mask[0, 0] == 0
        assert im.mask[-1, -1] == 255

        # Alpha mask (0 = invalid, 255 = valid)
        if im.alpha_mask is not None:
            assert im.alpha_mask[0, 0] == 0
            assert im.alpha_mask[-1, -1] == 255

    with Reader(_path(src_path)) as sync_src:
        sync_im = sync_src.preview(max_size=1024)
        numpy.testing.assert_array_equal(im.array.data, sync_im.array.data)
        numpy.testing.assert_array_equal(im.array.mask, sync_im.array.mask)


@pytest.mark.parametrize(
    "src_path",
    [
        "cog_dateline.tif",
        "cog_uint8_rgb_mask.tif",
        "cog_uint8_rgb_nodata.tif",
        "cog_uint8_rgba.tif",
    ],
)
def test_reader_tile(src_path):
    """tests tile() method against the rasterio Reader."""
    with ExpReader(_path(src_path)) as src, Reader(_path(src_path)) as sync_src:
        minzoom, maxzoom = src.minzoom, src.maxzoom
        w, s, e, n = src.get_geographic_bounds("epsg:4326")

        extrema = {}
        for zoom in range(minzoom, maxzoom + 1):
            ul_tile = src.tms.tile(w, n, zoom)
            lr_tile = src.tms.tile(e, s, zoom)
            extrema[zoom] = {
                "x": {"min": ul_tile.x, "max": lr_tile.x + 1},
                "y": {"min": ul_tile.y, "max": lr_tile.y + 1},
            }

        for zoom, ext in extrema.items():
            for x in range(ext["x"]["min"], ext["x"]["max"]):
                for y in range(ext["y"]["min"], ext["y"]["max"]):
                    try:
                        tile = src.tile(x, y, zoom)
                    except TileOutsideBounds:
                        continue

                    sync_tile = sync_src.tile(x, y, zoom)
                    assert tile.bounds == sync_tile.bounds
                    assert tile.array.shape == sync_tile.array.shape
                    assert tile.assets == sync_tile.assets
                    numpy.testing.assert_allclose(sync_tile.array, tile.array, rtol=1.5)
                    numpy.testing.assert_array_equal(
                        sync_tile.array.mask, tile.array.mask
                    )

        with pytest.raises(TileOutsideBounds):
            src.tile(extrema[minzoom]["x"]["max"], extrema[minzoom]["y"]["max"], minzoom)


def test_reader_tile_footprint():
    """Compare tiles for a dataset without nodata/mask (footprint mask from the warp).

    The rasterio Reader uses GDAL WarpedVRT (footprint mask + GDAL overview selection)
    while the experimental reader reads overview pixels then warps them onto the
    output grid in a single pass. Both pick the same overview and use the same
    overview geometry (the overview covers the full dataset extent), so the values
    are identical except for a few pixels (< 0.1%) at the lowest zoom. Footprint
    masks differ by at most one edge pixel per tile.
    """
    with ExpReader(_path("cog.tif")) as src, Reader(_path("cog.tif")) as sync_src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        for zoom in range(src.minzoom, src.maxzoom + 1):
            ul_tile = src.tms.tile(w, n, zoom)
            lr_tile = src.tms.tile(e, s, zoom)
            for x in range(ul_tile.x, lr_tile.x + 1):
                for y in range(ul_tile.y, lr_tile.y + 1):
                    try:
                        tile = src.tile(x, y, zoom)
                    except TileOutsideBounds:
                        continue

                    sync_tile = sync_src.tile(x, y, zoom)
                    assert tile.bounds == sync_tile.bounds
                    assert tile.array.shape == sync_tile.array.shape

                    # Footprint masks differ by at most one edge pixel
                    mask, sync_mask = tile.array.mask, sync_tile.array.mask
                    assert (mask != sync_mask).sum() <= 1

                    # Values are identical (all zooms but the lowest: < 0.1% differ)
                    valid = ~mask & ~sync_mask
                    data, sync_data = tile.array.data[valid], sync_tile.array.data[valid]
                    if zoom == src.minzoom:
                        assert (data != sync_data).mean() < 0.001
                    else:
                        numpy.testing.assert_array_equal(data, sync_data)


def test_reader_tile_buffer():
    """tile() with buffer."""
    with ExpReader(_path("cog.tif")) as src, Reader(_path("cog.tif")) as sync_src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        t = src.tms.tile((w + e) / 2, (s + n) / 2, src.minzoom + 2)

        img = src.tile(t.x, t.y, t.z, buffer=1)
        sync_img = sync_src.tile(t.x, t.y, t.z, buffer=1)
        assert img.array.shape == (1, 258, 258)
        assert img.array.shape == sync_img.array.shape
        numpy.testing.assert_allclose(img.bounds, sync_img.bounds)

        img = src.tile(t.x, t.y, t.z, buffer=0.5)
        assert img.array.shape == (1, 257, 257)

        with pytest.raises(InvalidBufferSize):
            src.tile(t.x, t.y, t.z, buffer=0.25)


def test_reader_part():
    """tests part() method."""
    bbox = (
        -56.624124590533825,
        73.50183615350426,
        -56.530950796449005,
        73.52687881825946,
    )

    with (
        ExpReader(_path("cog_nodata.tif")) as src,
        Reader(_path("cog_nodata.tif")) as sync_src,
    ):
        img = src.part(bbox)
        sync_img = sync_src.part(bbox)
        assert img.bounds == sync_img.bounds
        assert img.assets == sync_img.assets
        numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

        img = src.part(bbox, dst_crs=src.crs)
        sync_img = sync_src.part(bbox, dst_crs=sync_src.crs)
        assert img.bounds == sync_img.bounds
        numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

        img = src.part(bbox, dst_crs="EPSG:3857")
        sync_img = sync_src.part(bbox, dst_crs="EPSG:3857")
        assert img.bounds == sync_img.bounds
        numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

        img = src.part(bbox, max_size=20)
        sync_img = sync_src.part(bbox, max_size=20)
        assert img.bounds == sync_img.bounds
        numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

        img = src.part(bbox, width=20, height=10)
        sync_img = sync_src.part(bbox, width=20, height=10)
        assert img.bounds == sync_img.bounds
        numpy.testing.assert_allclose(sync_img.array, img.array, rtol=1.5)

        img = src.part(bbox, expression="b1*2;b1-100")
        assert img.band_descriptions == ["b1*2", "b1-100"]

        # bbox larger than the dataset
        gbbox = src.get_geographic_bounds("epsg:4326")
        gbbox = (gbbox[0] - 2.0, gbbox[1] - 2.0, gbbox[2] + 2.0, gbbox[3] + 2.0)
        img = src.part(gbbox, dst_crs=src.crs)
        sync_img = sync_src.part(gbbox, dst_crs=sync_src.crs)
        numpy.testing.assert_array_equal(sync_img.array, img.array)


def test_reader_part_outside():
    """part() should raise when bbox doesn't intersect with the dataset."""
    with ExpReader(_path("cog.tif")) as src:
        w, s, e, n = src.bounds
        dx, dy = e - w, n - s
        for bbox in [
            (w - 2 * dx, s, w - dx, n),  # left
            (e + dx, s, e + 2 * dx, n),  # right
            (w, n + dy, e, n + 2 * dy),  # above
            (w, s - 2 * dy, e, s - dy),  # below
        ]:
            with pytest.raises(ValueError, match="do not intersect"):
                src.part(bbox, bounds_crs=src.crs)


def test_reader_unsupported_options():
    """Unsupported options are ignored with a warning."""
    with ExpReader(_path("cog.tif")) as src:
        bbox = src.get_geographic_bounds("epsg:4326")

        with pytest.warns(UserWarning, match="Unsupported options will be ignored"):
            src.part(bbox, max_size=64, padding=2)

        with pytest.warns(UserWarning, match="Unsupported options will be ignored"):
            src.preview(max_size=64, vrt_options={"add_alpha": True})

        # `None` values are not reported
        with warnings.catch_warnings():
            warnings.simplefilter("error", UserWarning)
            src.part(bbox, max_size=64, padding=None)


def test_reader_feature():
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

    with (
        ExpReader(_path("cog_nodata.tif")) as src,
        Reader(_path("cog_nodata.tif")) as sync_src,
    ):
        # dst_crs should default to epsg:4326
        img = src.feature(feature, max_size=1024)
        sync_img = sync_src.feature(feature, max_size=1024)
        assert img.data.shape == (1, 334, 1024)
        assert img.band_names == ["b1"]
        # NOTE: Output shape is different from the rasterio Reader (348x1024)
        # because the output size is estimated from the bounds in the dataset CRS
        assert img.bounds == sync_img.bounds
        assert img.cutline_mask is not None
        assert img.cutline_mask.shape == (334, 1024)

        img = src.feature(feature, dst_crs=src.crs, max_size=1024)
        assert img.data.shape == (1, 1024, 869)

        img = src.feature(feature, max_size=30)
        assert img.data.shape == (1, 10, 30)

        img = src.feature(feature, expression="b1*2;b1-100", max_size=1024)
        assert img.data.shape == (2, 334, 1024)
        assert img.band_descriptions == ["b1*2", "b1-100"]

        with pytest.warns(ExpressionMixingWarning):
            img = src.feature(
                feature, indexes=(1, 2, 3), expression="b1*2", max_size=1024
            )
            assert img.band_descriptions == ["b1*2"]

        img = src.feature(feature, indexes=(1, 1), max_size=1024)
        assert img.data.shape == (2, 334, 1024)
        assert img.band_descriptions == ["b1", "b1"]
