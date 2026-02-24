"""test tasks."""

import os
from typing import Any

import rasterio
from rasterio._env import get_gdal_config

from rio_tiler import tasks
from rio_tiler.io import Reader
from rio_tiler.models import ImageData, PointData
from rio_tiler.utils import inherit_rasterio_env

COG = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")


def test_multi_arrays(monkeypatch):
    """Test Multi Arrays method."""

    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):

        @inherit_rasterio_env
        def reader(asset: str) -> ImageData:
            with Reader(asset) as src:
                im = src.read()
                value = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
                # For this test we forward the GDAL env information
                # to the ImageData band_descriptions.
                im.band_descriptions = [value]

            return im

    img = tasks.multi_arrays([COG, COG], reader, threads=2)
    assert img.count == 2
    assert img.band_descriptions == ["FALSE", "FALSE"]


def test_multi_point(monkeypatch):
    """Test Multi Points method."""

    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):

        @inherit_rasterio_env
        def reader(asset: str, *args: Any) -> PointData:
            with Reader(asset) as src:
                pt = src.point(*args)
                value = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
                # For this test we forward the GDAL env information
                # to the PointData band_descriptions.
                pt.band_descriptions = [value]

            return pt

    lon = -56.624124590533825
    lat = 73.52687881825946
    pt = tasks.multi_points([COG, COG], reader, lon, lat, threads=2)
    assert pt.count == 2
    assert pt.band_descriptions == ["FALSE", "FALSE"]


def test_multi_values(monkeypatch):
    """Test Multi Values method."""

    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    assets = {
        "1": COG,
        "2": COG,
    }

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):

        @inherit_rasterio_env
        def reader(asset: str, *args: Any) -> PointData:
            with Reader(assets[asset]) as src:
                pt = src.point(*args)
                value = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
                # For this test we forward the GDAL env information
                # to the PointData band_descriptions.
                pt.band_descriptions = [value]

            return pt

    lon = -56.624124590533825
    lat = 73.52687881825946
    pt = tasks.multi_values(["1", "2"], reader, lon, lat, threads=2)
    assert len(pt) == 2
    assert pt["1"].band_descriptions == ["FALSE"]
    assert pt["2"].band_descriptions == ["FALSE"]


def test_multi_values_list(monkeypatch):
    """Test Multi Values List method."""

    monkeypatch.setenv("GDAL_DISABLE_READDIR_ON_OPEN", "something")

    assets = {
        "1": COG,
        "2": COG,
    }

    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="FALSE"):

        @inherit_rasterio_env
        def reader(asset: str, *args: Any) -> PointData:
            with Reader(assets[asset]) as src:
                pt = src.point(*args)
                value = get_gdal_config("GDAL_DISABLE_READDIR_ON_OPEN")
                # For this test we forward the GDAL env information
                # to the PointData band_descriptions.
                pt.band_descriptions = [value]

            return pt

    lon = -56.624124590533825
    lat = 73.52687881825946
    pt = tasks.multi_values_list(["1", "2"], reader, lon, lat, threads=2)
    assert len(pt) == 2
    assert pt[0][1].band_descriptions == ["FALSE"]
    assert pt[1][1].band_descriptions == ["FALSE"]
