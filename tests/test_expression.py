"""test rio_tiler.expression functions."""

import warnings

import numpy
import pytest

from rio_tiler.errors import InvalidExpression
from rio_tiler.expression import (
    apply_expression,
    get_expression_blocks,
    parse_expression,
)


@pytest.mark.parametrize(
    "expr",
    [
        # old denylist cases
        "eval(x) for x in ('b1', 'b2')",
        # exec/compile bypass attempts
        'exec(\'__import__("os").system("id")\') + b1',
        "compile('pass', '', 'exec') + b1",
        # indirect eval via builtins
        "__import__('os').system('id') + b1",
        "getattr(__builtins__, 'eval')('1') + b1",
        # attribute access
        "b1.__class__ + b2",
        "b1.__class__.__bases__[0] + b2",
        # lambda
        "(lambda: b1)()",
        # list/dict/set comprehensions
        "[x for x in (b1,)]",
        "{x for x in (b1,)}",
        "{x: x for x in (b1,)}",
        # arbitrary function call
        "open('/etc/passwd') + b1",
        "print(b1)",
        # subscript
        "b1[0] + b2",
    ],
)
def test_parse_eval_invalid(expr):
    """test parse_expression error."""
    with pytest.raises(InvalidExpression):
        parse_expression(expr)


@pytest.mark.parametrize(
    "expr",
    [
        # arithmetic
        "b1*2;b2",
        "b1+b2",
        "b1-b2",
        "b1/b2",
        "b1**2",
        "b1%b2",
        "b1//b2",
        "-b1",
        # comparison / logical
        "b1>0",
        "b1>=b2",
        "(b1>0) & (b2<1)",
        "(b1>0) | (b2<1)",
        "~b1",
        # ternary
        "where(b1>0,b1,0)",
        "where((b1==1) | (b1 > 0.5), 1, 0);b2",
        # math functions
        "sin(b1)",
        "cos(b1)",
        "tan(b1)",
        "arcsin(b1)",
        "arccos(b1)",
        "arctan(b1)",
        "arctan2(b1,b2)",
        "sinh(b1)",
        "cosh(b1)",
        "tanh(b1)",
        "log(b1)",
        "log10(b1)",
        "log1p(b1)",
        "log2(b1)",
        "exp(b1)",
        "expm1(b1)",
        "sqrt(b1)",
        "abs(b1)",
        "sum(b1)*(-1)",
        "prod(b1)",
        "min(b1,b2)",
        "max(b1,b2)",
        "round(b1)",
        "sign(b1)",
        # multi-block
        "b1/b2;b2+b1",
    ],
)
def test_parse_eval_valid(expr):
    """test parse_expression valid."""
    parse_expression(expr)


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
    with warnings.catch_warnings():
        warnings.simplefilter("error")
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
