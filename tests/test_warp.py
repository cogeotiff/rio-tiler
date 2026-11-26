"""Tests for rio_tiler._warp."""

import numpy
import rasterio
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.io import MemoryFile
from rasterio.transform import from_bounds as rasterio_from_bounds
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds

from rio_tiler._warp import get_downsampling_factor, get_overview_level, warp
from rio_tiler.models import ImageData

WGS84 = CRS.from_epsg(4326)
WEB_MERCATOR = CRS.from_epsg(3857)
UTM21N = CRS.from_epsg(32621)

# Bounds in WGS84 that project cleanly into WebMercator
WGS84_BOUNDS = (-10.0, 40.0, 10.0, 60.0)

# Synthetic source bounds in UTM21N (well within valid projection range)
_SRC_BOUNDS_UTM = (400000.0, 8100000.0, 450000.0, 8150000.0)
_SRC_WIDTH, _SRC_HEIGHT = 64, 64
_DST_WIDTH, _DST_HEIGHT = 32, 32


def _make_gradient_image(width: int, height: int, crs: CRS, bounds: tuple) -> ImageData:
    """Create a 2D gradient ImageData useful for detecting resampling differences."""
    x = numpy.linspace(0, 255, width, dtype=numpy.float32)
    y = numpy.linspace(0, 255, height, dtype=numpy.float32)
    xx, yy = numpy.meshgrid(x, y)
    data = ((xx + yy) / 2).astype(numpy.uint8)[numpy.newaxis, ...]
    array = numpy.ma.MaskedArray(data, mask=False)
    return ImageData(array, bounds=bounds, crs=crs)


def _make_utm_memfile() -> MemoryFile:
    """Create an in-memory gradient raster in UTM21N for WarpedVRT comparison tests."""
    transform = rasterio_from_bounds(*_SRC_BOUNDS_UTM, _SRC_WIDTH, _SRC_HEIGHT)
    xx, yy = numpy.meshgrid(numpy.arange(_SRC_WIDTH), numpy.arange(_SRC_HEIGHT))
    data = ((xx + yy) * 4).astype(numpy.int16)[numpy.newaxis, :]
    memfile = MemoryFile()
    with memfile.open(
        driver="GTiff",
        dtype="int16",
        width=_SRC_WIDTH,
        height=_SRC_HEIGHT,
        count=1,
        crs=UTM21N,
        transform=transform,
    ) as ds:
        ds.write(data)
    return memfile


def test_warp_reproject_method_has_effect():
    """reproject_method is the warp kernel when the CRS changes."""
    dst_bounds = transform_bounds(WGS84, WEB_MERCATOR, *WGS84_BOUNDS)

    # upsampling and downsampling
    for src_size, dst_size in [(64, 256), (256, 64)]:
        img = _make_gradient_image(src_size, src_size, WGS84, WGS84_BOUNDS)
        out_nearest = warp(
            img,
            dst_crs=WEB_MERCATOR,
            dst_bounds=dst_bounds,
            dst_width=dst_size,
            dst_height=dst_size,
            reproject_method="nearest",
        )
        out_bilinear = warp(
            img,
            dst_crs=WEB_MERCATOR,
            dst_bounds=dst_bounds,
            dst_width=dst_size,
            dst_height=dst_size,
            reproject_method="bilinear",
        )
        assert out_nearest.array.shape == (1, dst_size, dst_size)
        assert out_bilinear.array.shape == (1, dst_size, dst_size)
        assert not numpy.array_equal(out_nearest.array, out_bilinear.array)


def test_warp_resampling_method_no_effect_when_reprojecting():
    """resampling_method has no effect when the CRS changes (single warp pass).

    Like rio_tiler.io.Reader (WarpedVRT), only reproject_method is used.
    """
    img = _make_gradient_image(64, 64, WGS84, WGS84_BOUNDS)
    dst_bounds = transform_bounds(WGS84, WEB_MERCATOR, *WGS84_BOUNDS)

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=256,
        dst_height=256,
        resampling_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=256,
        dst_height=256,
        resampling_method="bilinear",
    )
    numpy.testing.assert_array_equal(out_nearest.array, out_bilinear.array)


def test_warp_resampling_method_has_effect_same_crs():
    """resampling_method is the warp kernel when the CRS doesn't change."""
    bounds = (-1e6, 4e6, 1e6, 6e6)
    rng = numpy.random.default_rng(42)

    # upsampling and downsampling
    for src_size, dst_size in [(64, 256), (256, 64)]:
        # NOTE: random data, because bilinear on a linear gradient can match nearest
        data = rng.integers(0, 255, (1, src_size, src_size), dtype=numpy.uint8)
        img = ImageData(numpy.ma.MaskedArray(data), bounds=bounds, crs=WEB_MERCATOR)
        out = {
            method: warp(
                img,
                dst_crs=WEB_MERCATOR,
                dst_bounds=bounds,
                dst_width=dst_size,
                dst_height=dst_size,
                resampling_method=method,
            )
            for method in ["nearest", "bilinear", "gauss"]
        }
        for img_out in out.values():
            assert img_out.array.shape == (1, dst_size, dst_size)

        assert not numpy.array_equal(out["nearest"].array, out["bilinear"].array)
        # `gauss` isn't supported by the warper: two steps (warp + resize).
        # NOTE: when downsampling, the intermediate grid is capped to the output
        # size (memory bound), so the resize is a no-op and `gauss` has no effect.
        if dst_size > src_size:
            assert not numpy.array_equal(out["nearest"].array, out["gauss"].array)


def test_warp_reproject_method_no_effect_same_crs():
    """reproject_method has no effect when the CRS doesn't change.

    Like rio_tiler.io.Reader (no WarpedVRT), only resampling_method is used.
    """
    bounds = (-1e6, 4e6, 1e6, 6e6)
    img = _make_gradient_image(64, 64, WEB_MERCATOR, bounds)

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=bounds,
        dst_width=256,
        dst_height=256,
        reproject_method="nearest",
        resampling_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=bounds,
        dst_width=256,
        dst_height=256,
        reproject_method="bilinear",
        resampling_method="nearest",
    )
    numpy.testing.assert_array_equal(out_nearest.array, out_bilinear.array)


def test_warp_masked_pixels_propagate():
    """Masked pixels in the source remain masked in the output."""
    data = numpy.ma.MaskedArray(
        numpy.ones((1, 64, 64), dtype=numpy.uint8),
        mask=numpy.zeros((1, 64, 64), dtype=bool),
    )
    # mask the top-left quadrant
    data.mask[:, :32, :32] = True

    img = ImageData(data, bounds=WGS84_BOUNDS, crs=WGS84)
    dst_bounds = transform_bounds(WGS84, WEB_MERCATOR, *WGS84_BOUNDS)

    out = warp(
        img, dst_crs=WEB_MERCATOR, dst_bounds=dst_bounds, dst_width=64, dst_height=64
    )

    # Some pixels in the top-left area should still be masked
    assert out.array.mask.any()
    # The bottom-right area should be largely unmasked
    assert not out.array.mask[:, 32:, 32:].all()


# ---------------------------------------------------------------------------
# Comparison tests: warp() vs WarpedVRT
#
# Both paths start from the same in-memory raster so source-pixel selection
# is identical. The only difference is the transformation mechanism:
#   warp()    — rasterio.warp.reproject directly onto the output grid
#   WarpedVRT — GDAL warp kernel + dataset.read(out_shape)
# ---------------------------------------------------------------------------
def test_warp_vs_warped_vrt_nearest():
    """warp() with nearest should match WarpedVRT for the same in-memory source."""
    with _make_utm_memfile() as memfile:
        with memfile.open() as ds:
            src_data = ds.read(masked=True)
            img = ImageData(src_data, bounds=_SRC_BOUNDS_UTM, crs=UTM21N)

            with WarpedVRT(ds, crs=WGS84, resampling=Resampling.nearest) as vrt:
                b = vrt.bounds
                wgs84_bounds = (b.left, b.bottom, b.right, b.top)
                vrt_data = vrt.read(
                    out_shape=(1, _DST_HEIGHT, _DST_WIDTH),
                    resampling=Resampling.nearest,
                    masked=True,
                )

    warp_img = warp(
        img,
        dst_crs=WGS84,
        dst_bounds=wgs84_bounds,
        dst_width=_DST_WIDTH,
        dst_height=_DST_HEIGHT,
        reproject_method="nearest",
        resampling_method="nearest",
    )

    assert warp_img.array.shape == vrt_data.shape
    assert warp_img.crs == WGS84

    # Interior pixels (skip 2-pixel border) must agree exactly for nearest.
    interior = numpy.zeros(warp_img.array.shape, dtype=bool)
    interior[:, 2:-2, 2:-2] = True
    valid = interior & ~warp_img.array.mask & ~vrt_data.mask
    assert valid.any()
    # Nearest can still differ by 1-2 source pixels at sub-pixel grid seams.
    numpy.testing.assert_allclose(
        warp_img.array.data[valid].astype(float),
        vrt_data.data[valid].astype(float),
        atol=16,
    )


def test_warp_vs_warped_vrt_bilinear():
    """warp() with bilinear should be close to WarpedVRT for the same in-memory source."""
    with _make_utm_memfile() as memfile:
        with memfile.open() as ds:
            src_data = ds.read(masked=True)
            img = ImageData(src_data, bounds=_SRC_BOUNDS_UTM, crs=UTM21N)

            with WarpedVRT(ds, crs=WGS84, resampling=Resampling.bilinear) as vrt:
                b = vrt.bounds
                wgs84_bounds = (b.left, b.bottom, b.right, b.top)
                vrt_data = vrt.read(
                    out_shape=(1, _DST_HEIGHT, _DST_WIDTH),
                    resampling=Resampling.bilinear,
                    masked=True,
                )

    warp_img = warp(
        img,
        dst_crs=WGS84,
        dst_bounds=wgs84_bounds,
        dst_width=_DST_WIDTH,
        dst_height=_DST_HEIGHT,
        reproject_method="bilinear",
        resampling_method="bilinear",
    )

    assert warp_img.array.shape == vrt_data.shape
    assert warp_img.crs == WGS84

    interior = numpy.zeros(warp_img.array.shape, dtype=bool)
    interior[:, 2:-2, 2:-2] = True
    valid = interior & ~warp_img.array.mask & ~vrt_data.mask
    assert valid.any()
    # Bilinear introduces minor floating-point differences at pixel-grid edges.
    numpy.testing.assert_allclose(
        warp_img.array.data[valid].astype(float),
        vrt_data.data[valid].astype(float),
        atol=5,
    )


def test_get_overview_level(monkeypatch):
    """Overview selection with GDAL's rule.

    Select the most downsampled overview whose factor is < desired * threshold + 0.1,
    with threshold = 1.2 for `nearest` and 1.0 for other resampling methods.
    """
    factors = [2, 4, 8, 16]

    # upsampling or full resolution
    assert get_overview_level(factors, 0.5) == 0
    assert get_overview_level(factors, 1) == 0
    assert get_overview_level(factors, 2) == 1
    assert get_overview_level(factors, 1000) == 4

    # no overviews
    assert get_overview_level([], 1000) == 0

    # nearest: an overview up to ~1.2x coarser than the output can be used
    assert get_overview_level(factors, 1.4) == 0  # 2 >= 1.4 * 1.2 + 0.1
    assert get_overview_level(factors, 1.6) == 1  # 2 < 1.6 * 1.2 + 0.1
    assert get_overview_level(factors, 3.5) == 2  # 4 < 3.5 * 1.2 + 0.1

    # other methods: never use an overview coarser than the output
    assert get_overview_level(factors, 1.6, "bilinear") == 0
    assert get_overview_level(factors, 1.95, "bilinear") == 1  # 2 < 1.95 + 0.1
    assert get_overview_level(factors, 3.5, "cubic") == 1

    # real (non integer) overview factors, e.g 2658 / 167 = 15.92
    assert get_overview_level([2.0, 3.99, 7.98, 15.92], 15.0, "bilinear") == 3
    assert get_overview_level([2.0, 3.99, 7.98, 15.92], 15.9, "bilinear") == 4

    # GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD overrides the default threshold
    with rasterio.Env(GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD="2"):
        assert get_overview_level(factors, 3.5, "cubic") == 2

    # RIO_TILER_OVERVIEW_OVERSAMPLING_THRESHOLD (read at import) takes precedence
    monkeypatch.setattr("rio_tiler._warp.OVERVIEW_OVERSAMPLING_THRESHOLD", 1.0)
    assert get_overview_level(factors, 1.6) == 0  # 2 >= 1.6 * 1.0 + 0.1
    with rasterio.Env(GDAL_OVERVIEW_OVERSAMPLING_THRESHOLD="2"):
        assert get_overview_level(factors, 3.5, "cubic") == 1


def test_get_downsampling_factor():
    """Downsampling factor, like rio_tiler.io.Reader computes it."""
    transform = rasterio_from_bounds(*_SRC_BOUNDS_UTM, 1000, 1000)  # 50m pixels
    kwargs = {
        "dataset_crs": UTM21N,
        "dataset_transform": transform,
        "dataset_width": 1000,
        "dataset_height": 1000,
        "dataset_bounds": _SRC_BOUNDS_UTM,
    }

    # same CRS: window size (in dataset pixels) / output size
    factor = get_downsampling_factor(
        output_bounds=(400000.0, 8100000.0, 410000.0, 8110000.0),  # 200x200 pixels
        output_crs=UTM21N,
        output_width=100,
        output_height=50,
        **kwargs,
    )
    assert factor == 2  # least reduced axis (200 / 100 vs 200 / 50)

    # different CRS: WarpedVRT size (dataset resolution in the output CRS) / output size
    dst_bounds = transform_bounds(UTM21N, WEB_MERCATOR, *_SRC_BOUNDS_UTM)
    full = get_downsampling_factor(
        output_bounds=dst_bounds,
        output_crs=WEB_MERCATOR,
        output_width=1000,
        output_height=1000,
        **kwargs,
    )
    half = get_downsampling_factor(
        output_bounds=dst_bounds,
        output_crs=WEB_MERCATOR,
        output_width=500,
        output_height=500,
        **kwargs,
    )
    assert 0.9 < full < 1.1
    assert half == 2 * full
