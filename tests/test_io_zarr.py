"""tests rio_tiler.io.xarray readers"""

import os

import pytest

from rio_tiler.experimental.zarr import ZarrReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
ZARR_3D = os.path.join(PREFIX, "dataset_3d.zarr")


@pytest.mark.parametrize(
    "filename",
    [
        ZARR_3D,
    ],
)
def test_dataset_reader(filename):
    """test reader."""
    with ZarrReader(filename) as ds:
        assert ds.variables
        assert ds.crs
        assert ds.transform
        assert ds.bounds


def test_dataset_reader_variable():
    """test reader."""
    with ZarrReader(ZARR_3D) as ds:
        info = ds.info(variable="dataset")
        assert info.band_descriptions == [
            ("b1", "2022-01-01T00:00:00.000000000"),
            ("b2", "2023-01-01T00:00:00.000000000"),
        ]

        info = ds.info(variable="dataset", sel=["time=2022-01-01T00:00:00.000000000"])
        assert info.band_descriptions == [
            ("b1", "2022-01-01T00:00:00.000000000"),
        ]

    with ZarrReader(ZARR_3D) as ds:
        stats = ds.statistics(variable="dataset")
        assert stats["2022-01-01T00:00:00.000000000"]

        img = ds.tile(0, 0, 0, variable="dataset")
        assert img.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        img = ds.tile(0, 0, 0, variable="dataset", indexes=1)
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        img = ds.tile(
            0, 0, 0, variable="dataset", sel=["time=2022-01-01T00:00:00.000000000"]
        )
        assert img.band_names == ["2022-01-01T00:00:00.000000000"]

        img = ds.part((-160, -80, 160, 80), variable="dataset")
        assert img.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        img = ds.preview(variable="dataset")
        assert img.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        pts = ds.point(0, 0, variable="dataset")
        assert pts.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        feat = {
            "type": "Polygon",
            "coordinates": [
                [
                    (-160.0, -80.0),
                    (160.0, -80.0),
                    (160.0, 80.0),
                    (-160.0, 80.0),
                    (-160.0, -80.0),
                ]
            ],
        }
        img = ds.feature(feat, variable="dataset")
        assert img.band_names == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]
