"""rio-tiler.tests.benchmarks."""

import mercantile
from rasterio.coords import BoundingBox
from rasterio.crs import CRS

benchmark_tiles = {
    "north": {
        "full": mercantile.Tile(x=70, y=17, z=7),
        "masked": mercantile.Tile(x=69, y=16, z=7),
        "boundless": mercantile.Tile(x=68, y=17, z=7),
    },
    "south": {
        "full": mercantile.Tile(x=124, y=108, z=7),
        "masked": mercantile.Tile(x=125, y=109, z=7),
        "boundless": mercantile.Tile(x=122, y=107, z=7),
    },
    "equator": {
        "full": mercantile.Tile(x=537, y=499, z=10),
        "masked": mercantile.Tile(x=535, y=498, z=10),
        "boundless": mercantile.Tile(x=540, y=497, z=10),
    },
    "dateline": {
        "full": mercantile.Tile(x=510, y=169, z=10),
        "masked": mercantile.Tile(x=510, y=168, z=10),
        "boundless": mercantile.Tile(x=509, y=171, z=10),
    },
}

# LC08_L1TP_212004_20190816_20190902_01_T1
north = {
    "bounds": BoundingBox(
        left=433192.5, bottom=8534992.5, right=707407.5, top=8809207.5
    ),
    "crs": CRS.from_epsg(32633),
}

# LC08_L1GT_054115_20200120_20200120_01_RT
south = {
    "bounds": BoundingBox(
        left=123892.5, bottom=-1521007.5, right=387607.5, top=-1258492.5
    ),
    "crs": CRS.from_epsg(3031),
}

# LC08_L1TP_085024_20170816_20170825_01_T1
dateline = {
    "bounds": BoundingBox(
        left=570292.5, bottom=5612092.5, right=803107.5, top=5847607.5
    ),
    "crs": CRS.from_epsg(32660),
}

# LC08_L1TP_187057_20151212_20170401_01_T1
equator = {
    "name": "equator",
    "bounds": BoundingBox(left=382792.5, bottom=362992.5, right=610507.5, top=595207.5),
    "crs": CRS.from_epsg(32632),
}

benchmark_dataset = [
    dict(equator, dtype="uint8", nodata_type="alpha"),
    dict(equator, dtype="uint8", nodata_type="nodata"),
    dict(equator, dtype="uint8", nodata_type="mask"),
    dict(equator, dtype="uint8", nodata_type="none"),
    dict(equator, dtype="int8", nodata_type="alpha"),
    dict(equator, dtype="int8", nodata_type="nodata"),
    dict(equator, dtype="int8", nodata_type="mask"),
    dict(equator, dtype="int8", nodata_type="none"),
    dict(equator, dtype="uint16", nodata_type="alpha"),
    dict(equator, dtype="uint16", nodata_type="nodata"),
    dict(equator, dtype="uint16", nodata_type="mask"),
    dict(equator, dtype="uint16", nodata_type="none"),
    dict(equator, dtype="int16", nodata_type="alpha"),
    dict(equator, dtype="int16", nodata_type="nodata"),
    dict(equator, dtype="int16", nodata_type="mask"),
    dict(equator, dtype="int16", nodata_type="none"),
    dict(equator, dtype="uint32", nodata_type="alpha"),
    dict(equator, dtype="uint32", nodata_type="nodata"),
    dict(equator, dtype="uint32", nodata_type="mask"),
    dict(equator, dtype="uint32", nodata_type="none"),
    dict(equator, dtype="int32", nodata_type="alpha"),
    dict(equator, dtype="int32", nodata_type="nodata"),
    dict(equator, dtype="int32", nodata_type="mask"),
    dict(equator, dtype="int32", nodata_type="none"),
    dict(equator, dtype="float32", nodata_type="alpha"),
    dict(equator, dtype="float32", nodata_type="nodata"),
    dict(equator, dtype="float32", nodata_type="mask"),
    dict(equator, dtype="float32", nodata_type="none"),
    dict(equator, dtype="float64", nodata_type="alpha"),
    dict(equator, dtype="float64", nodata_type="nodata"),
    dict(equator, dtype="float64", nodata_type="mask"),
    dict(equator, dtype="float64", nodata_type="none"),
]
