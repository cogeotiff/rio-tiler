"""tests rio_tiler colormaps"""

from copy import deepcopy

import numpy
import pytest

from rio_tiler import colormap
from rio_tiler.colormap import DEFAULT_CMAPS_FILES
from rio_tiler.errors import (
    ColorMapAlreadyRegistered,
    InvalidColorFormat,
    InvalidColorMapName,
    InvalidFormat,
)


def test_get_cmaplist(monkeypatch):
    """Should work as expected return all rio-tiler colormaps."""
    monkeypatch.delenv("COLORMAP_DIRECTORY", raising=False)
    assert len(DEFAULT_CMAPS_FILES) == 167


def test_cmapObject(monkeypatch):
    """Test Colormap object handler."""
    monkeypatch.delenv("COLORMAP_DIRECTORY", raising=False)

    cmap = colormap.cmap
    assert len(cmap.list()) == 167

    with pytest.raises(InvalidColorMapName):
        cmap.get("something")

    # `register()` returns a new ColorMaps Objects without modifying the original
    cmap.register({"empty": colormap.EMPTY_COLORMAP})
    assert len(cmap.list()) == 167
    assert len(DEFAULT_CMAPS_FILES) == 167

    # check new cmap is registered and it didn't affect the original Dict
    new_cmap = cmap.register({"empty": colormap.EMPTY_COLORMAP})
    assert len(DEFAULT_CMAPS_FILES) == 167
    assert len(cmap.list()) == 167
    assert len(new_cmap.list()) == 168

    # register multiple cmap
    new_cmap = cmap.register({"empty": colormap.EMPTY_COLORMAP, "empty2": "fake.npy"})
    assert len(new_cmap.list()) == 169

    with pytest.raises(ColorMapAlreadyRegistered):
        new_cmap.register({"empty": colormap.EMPTY_COLORMAP})

    assert new_cmap.get("empty")


def test_valid_cmaps():
    """Make sure all colormaps have 4 values and 256 items."""
    for c in colormap.cmap.list():
        cm = colormap.cmap.get(c)
        assert len(cm[0]) == 4
        assert len(cm.items()) == 256


def test_update_alpha():
    """Should update the alpha channel."""
    cm = colormap.cmap.get("viridis")
    idx = 1
    assert cm[idx][-1] == 255
    colormap._update_alpha(cm, idx)
    assert cm[idx][-1] == 0

    idx = [2, 3]
    colormap._update_alpha(cm, idx)
    assert cm[idx[0]][-1] == 0
    assert cm[idx[1]][-1] == 0

    idx = 1
    assert cm[idx][-1] == 0
    colormap._update_alpha(cm, idx, alpha=255)
    assert cm[idx][-1] == 255


def test_remove_value():
    """Should remove cmap value."""
    cm = colormap.cmap.get("viridis")
    idx = 1
    colormap._remove_value(cm, idx)
    assert not cm.get(1)

    idx = [2, 3]
    colormap._remove_value(cm, idx)
    assert not cm.get(2)
    assert not cm.get(3)


def test_update_cmap():
    """Should update the colormap."""
    cm = colormap.cmap.get("viridis")
    val = {1: [0, 0, 0], 2: [255, 255, 255, 255]}
    colormap._update_cmap(cm, val)
    assert cm[1] == [0, 0, 0, 255]
    assert cm[2] == [255, 255, 255, 255]


def test_make_lut():
    """Should create valid lookup table."""
    cm = {1: [100, 100, 100, 255], 2: [255, 255, 255, 255]}
    lut = colormap.make_lut(cm)
    assert len(lut) == 256
    assert lut[0].tolist() == [0, 0, 0, 0]
    assert lut[1].tolist() == [100, 100, 100, 255]
    assert lut[4].tolist() == [0, 0, 0, 0]


def test_apply_cmap():
    """Should return valid data and mask."""
    cm = {1: [0, 0, 0, 255], 2: [255, 255, 255, 255]}
    data = numpy.zeros(shape=(1, 10, 10), dtype=numpy.uint8)
    data[0, 2:5, 2:5] = 1
    data[0, 5:, 5:] = 2
    d, m = colormap.apply_cmap(data, cm)
    assert d.shape == (3, 10, 10)
    assert m.shape == (10, 10)
    mask = numpy.zeros(shape=(10, 10), dtype=numpy.uint8)
    mask[2:5, 2:5] = 255
    mask[5:, 5:] = 255
    numpy.testing.assert_array_equal(m, mask)

    with pytest.raises(InvalidFormat):
        data = numpy.repeat(data, 3, axis=0)
        colormap.apply_cmap(data, cm)


def test_apply_discrete_cmap():
    """Should return valid data and mask."""
    cm = {1: [0, 0, 0, 255], 2: [255, 255, 255, 255]}
    data = numpy.zeros(shape=(1, 10, 10), dtype=numpy.uint8)
    data[0, 0:2, 0:2] = 1000
    data[0, 2:5, 2:5] = 1
    data[0, 5:, 5:] = 2
    d, m = colormap.apply_discrete_cmap(data, cm)
    assert d.shape == (3, 10, 10)
    assert m.shape == (10, 10)
    mask = numpy.zeros(shape=(10, 10), dtype=numpy.uint8)
    mask[2:5, 2:5] = 255
    mask[5:, 5:] = 255
    numpy.testing.assert_array_equal(m, mask)

    cm = {1: [0, 0, 0, 255], 1000: [255, 255, 255, 255]}
    d, m = colormap.apply_cmap(data, cm)
    dd, mm = colormap.apply_discrete_cmap(data, cm)
    numpy.testing.assert_array_equal(dd, d)
    numpy.testing.assert_array_equal(mm, m)

    cm = deepcopy(colormap.EMPTY_COLORMAP)
    cm.pop(255)
    cm[1000] = [255, 255, 255, 255]

    d, m = colormap.apply_cmap(data, cm)
    dd, mm = colormap.apply_discrete_cmap(data, cm)

    cm = {1: [0, 0, 0, 255], 256: [255, 255, 255, 255]}
    assert colormap.apply_cmap(data, cm)


@pytest.mark.parametrize(
    "value,result",
    [
        ["#FFF", (255, 255, 255, 255)],
        ["#FFF0", (255, 255, 255, 0)],
        ["#FF0000", (255, 0, 0, 255)],
        ["#FF000000", (255, 0, 0, 0)],
        [[255, 255, 255], (255, 255, 255, 255)],
        [[255, 255, 255, 0], (255, 255, 255, 0)],
    ],
)
def test_parse_color(value, result):
    """should parse HEX color and/or return a rio-tiler compatible colormap value."""
    assert colormap.parse_color(value) == result


def test_parse_color_bad():
    """Should raise InvalidColorFormat."""
    with pytest.raises(InvalidColorFormat):
        colormap.parse_color("#00000")

    with pytest.raises(InvalidColorFormat):
        colormap.parse_color("00000")

    with pytest.raises(InvalidColorFormat):
        colormap.parse_color([0, 0])

    with pytest.raises(InvalidColorFormat):
        colormap.parse_color([0, 0, 0, 0, 0])
