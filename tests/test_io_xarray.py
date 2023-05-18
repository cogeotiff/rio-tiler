"""tests rio_tiler.io.xarray.XarrayReader"""

import os
from datetime import datetime

import pytest
import rioxarray
import morecantile
import numpy
import xarray

from rio_tiler.io import XarrayReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")

planet = os.path.join(PREFIX, "PLANET_SCOPE_3D.nc")


def test_xarray_reader():
    """test XarrayReader."""
    arr = numpy.arange(0.0, 33 * 35).reshape(1, 33, 35)
    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": list(range(-170, 180, 10)),
            "y": list(range(-80, 85, 5)),
            "time": [datetime(2022, 1, 1)],
        },
    )
    data.attrs.update({"valid_min": arr.min(), "valid_max": arr.max()})

    data.rio.write_crs("epsg:4326", inplace=True)
    with XarrayReader(data) as dst:
        info = dst.info()
        assert info.minzoom == 0
        assert info.maxzoom == 0
        assert info.band_metadata == [("b1", {})]
        assert info.band_descriptions == [("b1", "2022-01-01T00:00:00.000000000")]
        assert info.height == 33
        assert info.width == 35
        assert info.count == 1
        assert info.attrs

    with XarrayReader(data) as dst:
        img = dst.tile(0, 0, 0)
        assert img.count == 1
        assert img.width == 256
        assert img.height == 256
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]
        assert img.dataset_statistics == ((arr.min(), arr.max()),)

        # Tests for auto_expand
        ## Test that a high-zoom tile will error with auto_expand=False
        tms = morecantile.tms.get("WebMercatorQuad")
        zoom = 10
        x, y = tms.xy(-170, -80)
        tile = tms._tile(x, y, zoom)
        bounds = tms.xy_bounds(tile)
        with pytest.raises(rioxarray.exceptions.OneDimensionalRaster) as error:
            error = dst.tile(tile.x, tile.y, zoom)
        assert str(error.value) == "At least one of the clipped raster x,y coordinates has only one point."
        ##
        ## Test that a high-zoom tile will succeed with auto_expand=True
        img = dst.tile(tile.x, tile.y, zoom, auto_expand=True)
        assert img.count == 1
        assert img.width == 256
        assert img.height == 256
        assert img.bounds == bounds
        assert img.dataset_statistics == ((arr.min(), arr.max()),)

        img = dst.part((-160, -80, 160, 80))
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        pt = dst.point(0, 0)
        assert pt.count == 1
        assert pt.band_names == ["2022-01-01T00:00:00.000000000"]
        assert pt.coordinates
        xys = [[0, 2.499], [0, 2.501], [-4.999, 0], [-5.001, 0], [-170, 80]]
        for xy in xys:
            x = xy[0]
            y = xy[1]
            pt = dst.point(x, y)
            assert pt.data[0] == data.sel(x=x, y=y, method="nearest")

        feat = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-92.46093749999999, 72.91963546581484],
                        [-148.0078125, 33.137551192346145],
                        [-143.08593749999997, -28.613459424004414],
                        [43.9453125, -47.04018214480665],
                        [142.734375, -12.897489183755892],
                        [157.5, 68.13885164925573],
                        [58.71093750000001, 74.95939165894974],
                        [-40.42968749999999, 75.14077784070429],
                        [-92.46093749999999, 72.91963546581484],
                    ]
                ],
            },
        }
        img = dst.feature(feat)
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        img = dst.feature(feat, dst_crs="epsg:3857")
        assert img.count == 1
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]
        assert img.crs.to_epsg() == 3857
