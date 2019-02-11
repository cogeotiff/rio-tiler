"""tests rio_tiler.profiles."""

import pytest

from rio_tiler import profiles


def test_gdal_profiles():
    """Return GDAL compatible profiles."""
    assert profiles.img_profiles["jpeg"]
    assert profiles.img_profiles["png"]
    assert profiles.img_profiles["pngraw"]
    assert profiles.img_profiles["webp"]
    with pytest.raises(KeyError):
        profiles.img_profiles["wepc"]
