"""test rio_tiler.expression functions."""

import numpy
import pytest

from rio_tiler.expression import (
    apply_expression,
    get_expression_blocks,
    parse_expression,
)


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("b1;b2", [1, 2]),
        ("B1;b2", [1, 2]),
        ("B1;B2", [1, 2]),
        ("where((b1==1) | (b1 > 0.5),1,0);", [1]),
    ],
)
def test_parse(expr, expected):
    """test parse_expression."""
    assert sorted(parse_expression(expr)) == expected


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("b1;b2", ["1", "2"]),
        ("B1;b2", ["1", "2"]),
        ("B1;B2", ["1", "2"]),
    ],
)
def test_parse_cast(expr, expected):
    """test parse_expression without casting."""
    assert sorted(parse_expression(expr, cast=False)) == expected


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("b1", ["b1"]),
        ("b1;", ["b1"]),
        ("b1;b2", ["b1", "b2"]),
        ("where((b1==1) | (b1 > 0.5),1,0);", ["where((b1==1) | (b1 > 0.5),1,0)"]),
    ],
)
def test_get_blocks(expr, expected):
    """test get_expression_blocks."""
    with pytest.warns(None):
        assert get_expression_blocks(expr) == expected


def test_apply_expression():
    """test apply_expression."""
    # divide b1 by b2
    data = numpy.zeros(shape=(2, 10, 10), dtype=numpy.uint8)
    data[0] += 1
    data[1] += 2
    d = apply_expression(["b1/b2"], ["b1", "b2"], data)
    assert numpy.unique(d) == 0.5

    # complex expression
    data = numpy.zeros(shape=(2, 10, 10), dtype=numpy.uint8)
    data[0, 0:5, 0:5] += 1
    d = apply_expression(["where((b1==1) | (b1 > 0.5),1,0)"], ["b1", "b2"], data)
    # data has 2 bands but expression just use one
    assert d.shape == (1, 10, 10)
    assert len(numpy.unique(d)) == 2
    assert numpy.unique(d[0, 0:5, 0:5]) == [1]

    data = numpy.zeros(shape=(2, 10, 10), dtype=numpy.uint8)
    data[0, 0:5, 0:5] += 1
    data[1, 0:5, 0:5] += 5
    d = apply_expression(
        ["where((b1==1) | (b1 > 0.5),1,0)", "where(b2 > 5,1,0)"], ["b1", "b2"], data
    )
    assert d.shape == (2, 10, 10)
