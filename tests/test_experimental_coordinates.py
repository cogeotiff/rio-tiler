"""Coordinates convention decoding when the optional isochron dependency is missing."""

import importlib

import pytest


@pytest.mark.parametrize(
    "module", ["rio_tiler.experimental.xarray", "rio_tiler.experimental.zarr"]
)
def test_coordinates_without_isochron(module, monkeypatch):
    """Only ISO 8601 interval coordinates need isochron."""
    mod = importlib.import_module(module)
    monkeypatch.setattr(mod, "isochron", None)

    assert mod._get_bnames_from_coordinates(
        {"type": "interval", "start": 1000, "stop": 3000, "step": 1000}
    ) == ["1000", "2000", "3000"]
    assert mod._get_bnames_from_coordinates(
        {"type": "inline", "values": ["t1", "t2"]}
    ) == ["t1", "t2"]

    with pytest.raises(ImportError, match="isochron must be installed"):
        mod._get_bnames_from_coordinates(
            {
                "type": "interval",
                "start": "2024-01-01T00:00:00Z",
                "stop": "2024-01-03T00:00:00Z",
                "step": "P1D",
            }
        )
