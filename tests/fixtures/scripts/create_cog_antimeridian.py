"""Create a synthetic COG crossing the antimeridian, with a real land footprint.

Area: Chukotka / Bering Strait (~172°E -> ~168°W, ~62°N -> ~70°N), in
UTM zone 60N (EPSG:32660), like a real scene straddling 180°.
Valid data = land (Natural Earth low-res); ocean = nodata.

Pixel value encodes the geographic position (same scheme as the polar COGs):
  value = round(|lat|) * 1000 + round(lon + 180)   (int32, nodata -9999)
so the longitude part jumps from ~359 to ~0 at the antimeridian.

Usage: python tests/fixtures/scripts/create_cog_antimeridian.py <naturalearth_lowres.shp> tests/fixtures

naturalearth_lowres.shp: Natural Earth 1:110m countries (e.g. the copy shipped in
pyogrio's test fixtures: pyogrio/tests/fixtures/naturalearth_lowres/).
Requires GDAL command line tools (ogr2ogr, gdal_rasterize) and pyproj.
"""

import os
import subprocess
import sys
import tempfile

import numpy
import rasterio
from pyproj import Transformer
from rasterio.io import MemoryFile
from rasterio.shutil import copy
from rasterio.transform import from_origin

SHP, OUT = sys.argv[1], sys.argv[2]

EPSG = 32660
RES = 450
WIDTH, HEIGHT = 2000, 2000
# Center the scene on 180°E, 66°N
cx, cy = Transformer.from_crs("EPSG:4326", f"EPSG:{EPSG}", always_xy=True).transform(
    180, 66
)
LEFT = round((cx - WIDTH * RES / 2) / RES) * RES
TOP = round((cy + HEIGHT * RES / 2) / RES) * RES
RIGHT, BOTTOM = LEFT + WIDTH * RES, TOP - HEIGHT * RES
NODATA = -9999

with tempfile.TemporaryDirectory() as tmpdir:
    projected = os.path.join(tmpdir, "land.gpkg")
    # Natural Earth splits Russia at 180°; reprojecting both halves to UTM 60N
    # puts them back side by side.
    subprocess.run(
        [
            "ogr2ogr",
            "-f",
            "GPKG",
            "-nlt",
            "MULTIPOLYGON",
            "-t_srs",
            f"EPSG:{EPSG}",
            "-spat",
            "160",
            "55",
            "180",
            "75",
            projected,
            SHP,
        ],
        check=True,
    )
    subprocess.run(
        [
            "ogr2ogr",
            "-append",
            "-nlt",
            "MULTIPOLYGON",
            "-t_srs",
            f"EPSG:{EPSG}",
            "-spat",
            "-180",
            "55",
            "-160",
            "75",
            projected,
            SHP,
        ],
        check=True,
    )
    mask_path = os.path.join(tmpdir, "mask.tif")
    subprocess.run(
        [
            "gdal_rasterize",
            "-burn",
            "1",
            "-ot",
            "Byte",
            "-init",
            "0",
            "-q",
            "-te",
            str(LEFT),
            str(BOTTOM),
            str(RIGHT),
            str(TOP),
            "-ts",
            str(WIDTH),
            str(HEIGHT),
            "-a_srs",
            f"EPSG:{EPSG}",
            projected,
            mask_path,
        ],
        check=True,
    )
    with rasterio.open(mask_path) as src:
        land = src.read(1).astype(bool)


def fbm(shape, beta, seed):
    """Fractal (power-law spectrum) noise normalized to [-1, 1]."""
    rng = numpy.random.default_rng(seed)
    kx = numpy.fft.fftfreq(shape[0])[:, None]
    ky = numpy.fft.fftfreq(shape[1])[None, :]
    k = numpy.hypot(kx, ky)
    k[0, 0] = 1
    amp = k ** (-beta / 2)
    amp[0, 0] = 0
    field = numpy.real(
        numpy.fft.ifft2(amp * numpy.exp(1j * rng.uniform(0, 2 * numpy.pi, shape)))
    )
    field -= field.mean()
    return field / numpy.abs(field).max()


def gaussian_blur(arr, sigma):
    """Gaussian blur (FFT)."""
    kx = numpy.fft.fftfreq(arr.shape[0])[:, None]
    ky = numpy.fft.fftfreq(arr.shape[1])[None, :]
    g = numpy.exp(-2 * (numpy.pi * sigma) ** 2 * (kx**2 + ky**2))
    return numpy.real(numpy.fft.ifft2(numpy.fft.fft2(arr) * g))


# Roughen the low-res Natural Earth coastline: blur the mask (smooth "distance to
# coast" proxy, sigma ~18 km), perturb it with fractal noise, re-threshold.
# This yields ragged coasts, bays, headlands and small offshore islands.
soft = gaussian_blur(land.astype("float64"), sigma=40)
noise = fbm(land.shape, beta=2.7, seed=42)
noise /= noise.std()
land = (soft + 0.22 * noise) > 0.5

cols, rows = numpy.meshgrid(numpy.arange(WIDTH) + 0.5, numpy.arange(HEIGHT) + 0.5)
xs = LEFT + cols * RES
ys = TOP - rows * RES
lon, lat = Transformer.from_crs(f"EPSG:{EPSG}", "EPSG:4326", always_xy=True).transform(
    xs, ys
)

data = (numpy.round(numpy.abs(lat)) * 1000 + numpy.round(lon + 180) % 360).astype("int32")
data[~land] = NODATA

profile = {
    "driver": "GTiff",
    "dtype": "int32",
    "count": 1,
    "width": WIDTH,
    "height": HEIGHT,
    "crs": f"EPSG:{EPSG}",
    "transform": from_origin(LEFT, TOP, RES, RES),
    "nodata": NODATA,
}
path = f"{OUT}/cog_antimeridian.tif"
with MemoryFile() as mem:
    with mem.open(**profile) as tmp:
        tmp.write(data, 1)
        tmp.set_band_description(1, "lat_lon_code")
        tmp.update_tags(
            description="Synthetic antimeridian-crossing COG over land (Chukotka); "
            "value = round(|lat|)*1000 + round(lon+180) % 360"
        )
        copy(
            tmp,
            path,
            driver="COG",
            compress="DEFLATE",
            blocksize=512,
            overview_resampling="nearest",
        )
print(f"wrote {path}")
