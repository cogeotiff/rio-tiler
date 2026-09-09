"""tests rio_tiler.io.xarray readers"""

import os

import numpy
import pytest
import rioxarray  # noqa
import xarray

from rio_tiler.experimental._zarr import ZarrReader

PREFIX = os.path.join(os.path.dirname(__file__), "fixtures")
ZARR_3D = os.path.join(PREFIX, "dataset_3d.zarr")


@pytest.mark.parametrize(
    "filename,options",
    [
        (ZARR_3D, {}),
        ("s3://mur-sst/zarr-v1", {"skip_signature": True, "region": "us-west-2"}),
    ],
)
def test_dataset_reader(filename, options):
    """test reader."""
    with ZarrReader(filename, opener_options=options) as ds:
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
        assert info.minmax == [(0.0, 1000.0), (0.0, 1000.0)]

        info = ds.info(variable="dataset", sel=["time=2022-01-01T00:00:00.000000000"])
        assert info.band_descriptions == [
            ("b1", "2022-01-01T00:00:00.000000000"),
        ]
        assert info.minmax == [(0.0, 1000.0)]

    with ZarrReader(ZARR_3D) as ds:
        stats = ds.statistics(variable="dataset")
        assert stats["b1"]

        img = ds.tile(0, 0, 0, variable="dataset")
        assert img.band_names == [
            "b1",
            "b2",
        ]
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        img = ds.tile(0, 0, 0, variable="dataset", indexes=1)
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000000"]

        img = ds.tile(
            0, 0, 0, variable="dataset", sel=["time=2022-01-01T00:00:00.000000000"]
        )
        assert img.band_descriptions == ["2022-01-01T00:00:00.000000000"]

        img = ds.part((-160, -80, 160, 80), variable="dataset")
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        img = ds.preview(variable="dataset")
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]

        pts = ds.point(0, 0, variable="dataset")
        assert pts.band_descriptions == [
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
        assert img.band_descriptions == [
            "2022-01-01T00:00:00.000000000",
            "2023-01-01T00:00:00.000000000",
        ]


def test_dataset_reader_global_bounds_float_precision(tmp_path):
    """Should not raise InvalidGeographicBounds when the half-cell allowance misses by a float residue."""
    # See `test_xarray_reader_global_bounds_float_precision`: a 0.4 degree
    # global grid, with coordinates built the way data providers write them.
    y = numpy.arange(90, -90.4, -0.4)
    x = numpy.arange(-180, 180, 0.4)
    ds = xarray.DataArray(
        numpy.zeros((len(y), len(x)), dtype="float32"),
        dims=("y", "x"),
        coords={"y": y, "x": x},
        name="dataset",
    ).to_dataset()
    ds.rio.write_crs("epsg:4326", inplace=True)

    src_path = str(tmp_path / "global.zarr")
    ds.to_zarr(src_path)

    with ZarrReader(src_path) as dst:
        assert dst.bounds[1] == pytest.approx(-90.2)
        assert dst.bounds[3] == pytest.approx(90.2)
