"""Create synthetic polar stereographic COGs with real land footprints.

north: EPSG:3413, south: EPSG:3031. Valid data = land (Natural Earth low-res
countries) within the grid; ocean = nodata.

Pixel value encodes the geographic position:
  value = round(|lat|) * 1000 + round(lon + 180)   (int32, nodata -9999)

Usage: python tests/fixtures/scripts/create_cog_poles.py <naturalearth_lowres.shp> tests/fixtures

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

SIZE = 2048
# Symmetric extent: the pole sits exactly at the image center; covers the whole
# hemisphere down to the equator (~12,370 km from the pole). 12.5 km resolution.
HALF_EXTENT = 12_800_000
RES = 2 * HALF_EXTENT / SIZE
NODATA = -9999

for name, epsg in [("north", 3413), ("south", 3031)]:
    with tempfile.TemporaryDirectory() as tmpdir:
        # Clip to the hemisphere first so the polar reprojection stays clean
        clip = "-180 0 180 90" if name == "north" else "-180 -90 180 0"
        clipped = os.path.join(tmpdir, "land.gpkg")
        subprocess.run(
            [
                "ogr2ogr",
                "-f",
                "GPKG",
                "-clipsrc",
                *clip.split(),
                "-t_srs",
                f"EPSG:{epsg}",
                "-wrapdateline",
                clipped,
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
                "-te",
                str(-HALF_EXTENT),
                str(-HALF_EXTENT),
                str(HALF_EXTENT),
                str(HALF_EXTENT),
                "-ts",
                str(SIZE),
                str(SIZE),
                "-a_srs",
                f"EPSG:{epsg}",
                "-q",
                clipped,
                mask_path,
            ],
            check=True,
        )
        with rasterio.open(mask_path) as src:
            land = src.read(1).astype(bool)

    cols, rows = numpy.meshgrid(numpy.arange(SIZE) + 0.5, numpy.arange(SIZE) + 0.5)
    xs = -HALF_EXTENT + cols * RES
    ys = HALF_EXTENT - rows * RES
    lon, lat = Transformer.from_crs(
        f"EPSG:{epsg}", "EPSG:4326", always_xy=True
    ).transform(xs, ys)

    data = (numpy.round(numpy.abs(lat)) * 1000 + numpy.round(lon + 180)).astype("int32")
    data[~land] = NODATA

    profile = {
        "driver": "GTiff",
        "dtype": "int32",
        "count": 1,
        "width": SIZE,
        "height": SIZE,
        "crs": f"EPSG:{epsg}",
        "transform": from_origin(-HALF_EXTENT, HALF_EXTENT, RES, RES),
        "nodata": NODATA,
    }
    with MemoryFile() as mem:
        with mem.open(**profile) as tmp:
            tmp.write(data, 1)
            tmp.set_band_description(1, "lat_lon_code")
            tmp.update_tags(
                description=f"Synthetic {name} pole COG over land; "
                "value = round(|lat|)*1000 + round(lon+180)"
            )
            copy(
                tmp,
                f"{OUT}/cog_{name}_pole.tif",
                driver="COG",
                compress="DEFLATE",
                blocksize=512,
                overview_resampling="nearest",
            )
    print(f"wrote {OUT}/cog_{name}_pole.tif")
