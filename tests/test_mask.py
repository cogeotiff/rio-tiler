"""test masks."""

import os

import morecantile
import numpy
import pytest
from rasterio.coords import BoundingBox
from rasterio.crs import CRS

from rio_tiler.io import COGReader

tiles = {
    "masked": morecantile.Tile(x=535, y=498, z=10),
    "boundless": morecantile.Tile(x=540, y=497, z=10),
}
equator = {
    "name": "equator",
    "bounds": BoundingBox(left=382792.5, bottom=362992.5, right=610507.5, top=595207.5),
    "crs": CRS.from_epsg(32632),
}

dataset = [
    dict(equator, dtype="uint8", nodata_type="alpha"),
    dict(equator, dtype="uint8", nodata_type="nodata"),
    dict(equator, dtype="uint8", nodata_type="mask"),
    dict(equator, dtype="int8", nodata_type="alpha"),
    dict(equator, dtype="int8", nodata_type="nodata"),
    dict(equator, dtype="int8", nodata_type="mask"),
    # dict(equator, dtype="uint16", nodata_type="alpha"), #fail
    dict(equator, dtype="uint16", nodata_type="nodata"),
    dict(equator, dtype="uint16", nodata_type="mask"),
    # dict(equator, dtype="int16", nodata_type="alpha"), # Fail
    dict(equator, dtype="int16", nodata_type="nodata"),
    # dict(equator, dtype="int16", nodata_type="mask"), # Fail
]

cog_path = os.path.join(os.path.dirname(__file__), "fixtures", "mask")


def test_mask_bilinear(cloudoptimized_geotiff):
    """Test mask read with bilinear resampling"""
    src_path = cloudoptimized_geotiff(
        cog_path, **equator, dtype="uint8", nodata_type="mask"
    )
    with COGReader(src_path) as cog:
        data, mask = cog.tile(
            535,
            498,
            10,
            tilesize=256,
            resampling_method="bilinear",
            force_binary_mask=True,
        )
        masknodata = (data[0] != 0).astype(numpy.uint8) * 255
        numpy.testing.assert_array_equal(mask, masknodata)

        data, mask = cog.tile(
            535,
            498,
            10,
            tilesize=256,
            resampling_method="bilinear",
            force_binary_mask=False,
        )
        masknodata = (data[0] != 0).astype(numpy.uint8) * 255
        assert not numpy.array_equal(mask, masknodata)


@pytest.mark.parametrize("resampling", ["bilinear", "nearest"])
@pytest.mark.parametrize("tile_name", ["masked"])
@pytest.mark.parametrize("dataset_info", dataset)
def test_mask(dataset_info, tile_name, resampling, cloudoptimized_geotiff):
    """Test tile read for multiple combination of datatype/mask/tile extent."""
    src_path = cloudoptimized_geotiff(cog_path, **dataset_info)

    tile = tiles[tile_name]
    with COGReader(src_path) as cog:
        data, mask = cog.tile(
            tile.x,
            tile.y,
            tile.z,
            tilesize=256,
            resampling_method=resampling,
            force_binary_mask=True,
        )
        masknodata = (data[0] != 0).astype(numpy.uint8) * 255
        numpy.testing.assert_array_equal(mask, masknodata)
