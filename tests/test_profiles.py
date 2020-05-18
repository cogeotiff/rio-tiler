"""tests rio_tiler.profiles."""

import pytest

from rio_tiler.profiles import img_profiles


def test_gdal_profiles():
    """Return GDAL compatible profiles."""
    assert img_profiles["jpeg"]
    assert img_profiles["png"]
    assert img_profiles["pngraw"]
    assert img_profiles["webp"]
    with pytest.raises(KeyError):
        img_profiles["wepc"]

    prof = img_profiles.get("jpeg")
    prof["test"] = True
    new_prof = img_profiles.get("jpeg")
    assert not new_prof.get("test")

    prof = img_profiles["jpeg"]
    prof["test"] = True
    new_prof = img_profiles["jpeg"]
    assert not new_prof.get("test")

    prof = img_profiles.get("jpe", {"a": "b"})
    assert prof == {"a": "b"}
