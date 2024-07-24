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

colormap_number = 211


def test_get_cmaplist(monkeypatch):
    """Should work as expected return all rio-tiler colormaps."""
    monkeypatch.delenv("COLORMAP_DIRECTORY", raising=False)
    assert len(DEFAULT_CMAPS_FILES) == colormap_number


def test_cmapObject(monkeypatch):
    """Test Colormap object handler."""
    monkeypatch.delenv("COLORMAP_DIRECTORY", raising=False)

    cmap = colormap.cmap
    assert len(cmap.list()) == colormap_number

    with pytest.raises(InvalidColorMapName):
        cmap.get("something")

    # `register()` returns a new ColorMaps Objects without modifying the original
    cmap.register({"empty": colormap.EMPTY_COLORMAP})
    assert len(cmap.list()) == colormap_number
    assert len(DEFAULT_CMAPS_FILES) == colormap_number

    # check new cmap is registered and it didn't affect the original Dict
    new_cmap = cmap.register({"empty": colormap.EMPTY_COLORMAP})
    assert len(DEFAULT_CMAPS_FILES) == colormap_number
    assert len(cmap.list()) == colormap_number
    assert len(new_cmap.list()) == colormap_number + 1

    # register multiple cmap
    new_cmap = cmap.register({"empty": colormap.EMPTY_COLORMAP, "empty2": "fake.npy"})
    assert len(new_cmap.list()) == colormap_number + 2

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
    val = {1: (0, 0, 0, 0), 2: (255, 255, 255, 255)}
    colormap._update_cmap(cm, val)
    assert cm[1] == (0, 0, 0, 0)
    assert cm[2] == (255, 255, 255, 255)


def test_make_lut():
    """Should create valid lookup table."""
    cm = {1: (100, 100, 100, 255), 2: (255, 255, 255, 255)}
    lut = colormap.make_lut(cm)
    assert len(lut) == 256
    assert lut[0].tolist() == [0, 0, 0, 0]
    assert lut[1].tolist() == [100, 100, 100, 255]
    assert lut[4].tolist() == [0, 0, 0, 0]


def test_apply_cmap():
    """Should return valid data and mask."""
    cm = {1: (0, 0, 0, 255), 2: (255, 255, 255, 255)}
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

    data = data.astype("uint16")
    d, m = colormap.apply_cmap(data, cm)
    assert d.dtype == numpy.uint8
    assert m.dtype == numpy.uint8

    with pytest.raises(InvalidFormat):
        data = numpy.repeat(data, 3, axis=0)
        colormap.apply_cmap(data, cm)


def test_apply_discrete_cmap():
    """Should return valid data and mask."""
    cm = {1: (0, 0, 0, 255), 2: (255, 255, 255, 255)}
    data = numpy.zeros(shape=(1, 10, 10), dtype=numpy.uint16)
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
    dd, mm = colormap.apply_cmap(data, cm)
    numpy.testing.assert_array_equal(dd, d)
    numpy.testing.assert_array_equal(mm, m)

    data = data.astype("uint16")
    d, m = colormap.apply_discrete_cmap(data, cm)
    assert d.dtype == numpy.uint8
    assert m.dtype == numpy.uint8

    cm = {1: (0, 0, 0, 255), 1000: (255, 255, 255, 255)}
    d, m = colormap.apply_cmap(data, cm)
    dd, mm = colormap.apply_discrete_cmap(data, cm)
    numpy.testing.assert_array_equal(dd, d)
    numpy.testing.assert_array_equal(mm, m)

    cm = deepcopy(colormap.EMPTY_COLORMAP)
    cm.pop(255)
    cm[1000] = (255, 255, 255, 255)
    d, m = colormap.apply_cmap(data, cm)
    dd, mm = colormap.apply_discrete_cmap(data, cm)
    numpy.testing.assert_array_equal(dd, d)
    numpy.testing.assert_array_equal(mm, m)

    cm = {1: (0, 0, 0, 255), 256: (255, 255, 255, 255)}
    assert colormap.apply_cmap(data, cm)

    # Test with negative value
    data = data.astype("int16")
    cm = {-100: (255, 255, 255, 255), 1: (0, 0, 0, 255), 256: (255, 255, 255, 255)}
    data[0, 5:, 5:] = -100
    d, m = colormap.apply_cmap(data, cm)
    dd, mm = colormap.apply_discrete_cmap(data, cm)
    numpy.testing.assert_array_equal(dd, d)
    numpy.testing.assert_array_equal(mm, m)


def test_apply_intervals_cmap():
    """Should return valid data and mask."""
    cm = [
        # ([min, max], [r, g, b, a])
        ((1, 2), (255, 0, 0, 255)),
        ((2, 3), (255, 240, 255, 255)),
    ]
    data = numpy.zeros(shape=(1, 10, 10), dtype=numpy.uint16)
    data[0, 0:2, 0:2] = 1000
    data[0, 2:5, 2:5] = 1
    data[0, 5:, 5:] = 2
    d, m = colormap.apply_intervals_cmap(data, cm)
    assert d.shape == (3, 10, 10)
    assert m.shape == (10, 10)
    assert d[0, 3, 4] == 255
    assert d[1, 5, 5] == 240

    mask = numpy.zeros(shape=(10, 10), dtype=numpy.uint8)
    mask[2:5, 2:5] = 255
    mask[5:, 5:] = 255
    numpy.testing.assert_array_equal(m, mask)

    data = data.astype("uint16")
    d, m = colormap.apply_intervals_cmap(data, cm)
    assert d.dtype == numpy.uint8
    assert m.dtype == numpy.uint8

    cm = [
        # ((min, max), (r, g, b, a))
        ((0, 2), (0, 255, 0, 255)),
        ((2, 3), (255, 255, 255, 255)),
        ((3, 1001), (255, 0, 0, 255)),
    ]
    d, m = colormap.apply_intervals_cmap(data, cm)
    assert d.shape == (3, 10, 10)
    assert m.shape == (10, 10)
    assert d[0, 0, 0] == 255


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


def test_discrete_float():
    """test for titiler issue 738."""
    cm = {
        0: (0, 255, 255, 255),
        1: (83, 151, 145, 255),
        2: (87, 194, 23, 255),
        3: (93, 69, 255, 255),
        4: (98, 217, 137, 255),
        5: (140, 255, 41, 255),
        6: (150, 110, 255, 255),
        7: (179, 207, 100, 255),
        8: (214, 130, 156, 255),
        9: (232, 170, 108, 255),
        10: (255, 225, 128, 255),
        11: (255, 184, 180, 255),
        12: (255, 255, 140, 255),
        13: (255, 180, 196, 255),
        14: (255, 0, 0, 255),
        15: (255, 218, 218, 255),
    }

    data = numpy.round(numpy.random.random_sample((1, 256, 256)) * 15)
    d, m = colormap.apply_cmap(data.copy(), cm)
    dd, mm = colormap.apply_discrete_cmap(data.copy(), cm)
    assert d.dtype == numpy.uint8
    assert m.dtype == numpy.uint8
