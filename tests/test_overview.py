"""Test overview fetching."""
# Create COG with each IFD level having its own value
# import os
# import numpy
# import rasterio
# from rasterio import transform
#
# with rasterio.open("cog.tif") as src:
#     profile = src.profile
#
#     profile["blockxsize"] = 256
#     profile["blockysize"] = 256
#     profile["compress"] = "DEFLATE"
#     profile["tiled"] = True
#     profile["nodata"] = 0
#     profile["dtype"] = "uint8"
#
#     # create tif without overview
#     v = 1
#     arr = numpy.zeros((src.height, src.width), dtype="uint8") + v
#     with rasterio.open(f"tmp.tif", "w", **profile) as dst:
#         dst.write(arr, indexes=1)
#
#     # create overviews
#     overview_factor = 1
#     while min(src.width // overview_factor, src.height // overview_factor) > 256:
#         v += 1
#         overview_factor *= 2
#         height = arr.shape[0] // 2
#         width = arr.shape[1] // 2
#         arr = numpy.zeros((height, width), dtype=arr.dtype) + v
#         profile["width"] = width
#         profile["height"] = height
#         profile["transform"] = transform.from_bounds(*src.bounds, height, width)
#         with rasterio.open(f"tmp.tif.ovr.{overview_factor}", "w", **profile) as dst:
#             dst.write(arr, indexes=1)
# # https://github.com/airbusgeo/cogger
# os.system("cogger -output cog_ovr.tif tmp.tif tmp.tif.ovr.2 tmp.tif.ovr.4 tmp.tif.ovr.8 tmp.tif.ovr.16")

import os

import numpy

from rio_tiler.io import Reader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

# cog_ovr:
# Id         Size           Value
# raw        2658x2667      1
# ovr0       1329x1333      2
# ovr1       664x666        3
# ovr2       332x333        4
# ovr3       166x166        5
COG = os.path.join(PREFIX, "cog_ovr.tif")

# cog_gcps_ovr:
# Id         Size           Value
# raw        1280x837       1
# ovr0       640x418        2
# ovr1       320x209        3
COG_GCPS = os.path.join(PREFIX, "cog_gcps_ovr.tif")


def test_simple_cog():
    """Test Overview fetching with simple cog."""
    # Simple read (no WarpedVRT)
    with Reader(COG) as src:
        im = src.preview(max_size=2048)  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.preview(max_size=1024)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.preview(max_size=512)  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

        im = src.preview(max_size=256)  # should fetch the thrid overview (value==4)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [4]

        im = src.preview(max_size=128)  # should fetch the last overview (value==5)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [5]

    # Using WarpedVRT
    with Reader(COG) as src:
        im = src.preview(
            max_size=4096, dst_crs="epsg:4326"
        )  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.preview(
            max_size=2048, dst_crs="epsg:4326"
        )  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.preview(
            max_size=1024, dst_crs="epsg:4326"
        )  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

        im = src.preview(
            max_size=512, dst_crs="epsg:4326"
        )  # should fetch the third overview (value==4)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [4]

        im = src.preview(
            max_size=256, dst_crs="epsg:4326"
        )  # should fetch the last overview (value==5)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [5]


def test_gcps_cog():
    """Test Overview fetching with gcps cog."""
    # Simple WarpedVRT (to apply the gcps)
    with Reader(COG_GCPS) as src:
        im = src.preview(max_size=1024)  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.preview(max_size=512)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.preview(max_size=256)  # should fetch the last overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

    # Using WarpedVRT of a WarpedVRT
    with Reader(COG_GCPS) as src:
        im = src.preview(
            max_size=1024, dst_crs="epsg:3857"
        )  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.preview(
            max_size=512, dst_crs="epsg:3857"
        )  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.preview(
            max_size=256, dst_crs="epsg:3857"
        )  # should fetch the last overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]


def test_simple_cog_tile_read():
    """Test Overview fetching with simple cog."""
    # Using WarpedVRT
    with Reader(COG) as src:
        # Full tile
        im = src.tile(173, 97, 9)  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.tile(87, 49, 8)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.tile(43, 24, 7)  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

        im = src.tile(21, 12, 6)  # should fetch the thrid overview (value==4)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [4]

        im = src.tile(10, 6, 5)  # should fetch the last overview (value==5)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [5]

        # Tile on border
        im = src.tile(169, 102, 9)  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.tile(84, 48, 8)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.tile(42, 24, 7)  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

    # Using WarpedVRT with buffer
    with Reader(COG) as src:
        # Full tile
        im = src.tile(173, 97, 9, buffer=4)  # should fetch the raw resolution (value==1)
        assert im.array.shape == (1, 264, 264)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.tile(87, 49, 8, buffer=4)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.tile(43, 24, 7, buffer=4)  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]

        im = src.tile(21, 12, 6, buffer=4)  # should fetch the thrid overview (value==4)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [4]

        im = src.tile(10, 6, 5, buffer=4)  # should fetch the last overview (value==5)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [5]

        # Tile on border
        im = src.tile(169, 102, 9, buffer=4)  # should fetch the raw resolution (value==1)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [1]

        im = src.tile(84, 48, 8, buffer=4)  # should fetch the first overview (value==2)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [2]

        im = src.tile(42, 24, 7, buffer=4)  # should fetch the second overview (value==3)
        assert numpy.unique(im.data[0, im.mask == 255]).tolist() == [3]
