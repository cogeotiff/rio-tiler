"""tests rio_tiler.utils"""

import pytest

from rio_tiler import profiles
from rio_tiler.errors import DeprecationWarning, InvalidFormat


# TODO: Remove on 1.0.0
def test_pil_profile():
    """Raises a warning when fetching PIL profiles."""
    with pytest.warns(DeprecationWarning):
        profiles.get("jpeg")
        profiles.get("png")
        profiles.get("webp")
        with pytest.raises(InvalidFormat):
            profiles.get("wepc")


def test_gdal_profiles():
    """Return GDAL compatible profiles."""
    assert profiles.img_profiles["jpeg"]
    assert profiles.img_profiles["png"]
    assert profiles.img_profiles["pngraw"]
    assert profiles.img_profiles["webp"]
    with pytest.raises(KeyError):
        profiles.img_profiles["wepc"]
