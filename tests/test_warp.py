"""Tests for rio_tiler._warp.warp() two-step pipeline."""

import numpy
from rasterio.crs import CRS
from rasterio.enums import Resampling
from rasterio.io import MemoryFile
from rasterio.transform import from_bounds as rasterio_from_bounds
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds

from rio_tiler._warp import warp
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
    """Check reproject_method has effect."""
    img = _make_gradient_image(256, 256, WGS84, WGS84_BOUNDS)
    dst_bounds = transform_bounds(WGS84, WEB_MERCATOR, *WGS84_BOUNDS)

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=256,
        dst_height=256,
        reproject_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=256,
        dst_height=256,
        reproject_method="bilinear",
    )
    assert out_nearest.array.shape == (1, 256, 256)
    assert out_bilinear.array.shape == (1, 256, 256)
    assert not numpy.array_equal(out_nearest.array, out_bilinear.array)

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=64,
        dst_height=64,
        reproject_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=64,
        dst_height=64,
        reproject_method="bilinear",
    )
    assert out_nearest.array.shape == (1, 64, 64)
    assert out_bilinear.array.shape == (1, 64, 64)
    assert not numpy.array_equal(out_nearest.array, out_bilinear.array)


def test_warp_resampling_methods_has_effect():
    """Check resampling_method has effect."""
    img = _make_gradient_image(256, 256, WGS84, WGS84_BOUNDS)
    dst_bounds = transform_bounds(WGS84, WEB_MERCATOR, *WGS84_BOUNDS)

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=512,
        dst_height=512,
        resampling_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=dst_bounds,
        dst_width=512,
        dst_height=512,
        resampling_method="bilinear",
    )
    assert out_nearest.array.shape == (1, 512, 512)
    assert out_bilinear.array.shape == (1, 512, 512)
    assert not numpy.array_equal(out_nearest.array, out_bilinear.array)


def test_warp_resampling_method_no_effect_when_downsampling():
    """resampling_method has no effect when downsampling.

    The intermediate chunk is capped to the output tile size to bound peak
    memory, so step 2 (resize) is always a no-op in the downsampling case.
    reproject_method is the only kernel that matters.
    """
    img = _make_gradient_image(256, 256, WEB_MERCATOR, (-1e6, 4e6, 1e6, 6e6))

    out_nearest = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=(-1e6, 4e6, 1e6, 6e6),
        dst_width=32,
        dst_height=32,
        reproject_method="bilinear",
        resampling_method="nearest",
    )
    out_bilinear = warp(
        img,
        dst_crs=WEB_MERCATOR,
        dst_bounds=(-1e6, 4e6, 1e6, 6e6),
        dst_width=32,
        dst_height=32,
        reproject_method="bilinear",
        resampling_method="bilinear",
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
#   warp()    — rasterio.warp.reproject (step 1) + resize_array (step 2)
#   WarpedVRT — GDAL warp kernel (step 1) + dataset.read(out_shape) (step 2)
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
