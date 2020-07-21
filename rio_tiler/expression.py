"""rio-tiler.expression: Parse and Apply expression."""

import re
from typing import Sequence, Tuple, Union

import numexpr
import numpy


def parse_expression(expression: str, cast: bool = True) -> Tuple:
    """
    Parse rio-tiler band math expression.

    Attributes
    ----------
    expression: str
        band math/combination expression (e.g b3/b2).

    Returns
    -------
    bands: Tuple

    """
    bands = set(re.findall(r"b(?P<bands>[0-9A-Z]+)", expression, re.IGNORECASE))
    return tuple(map(int, bands)) if cast else tuple(bands)


def apply_expression(
    blocks: Sequence[str], bands: Sequence[Union[str, int]], data: numpy.ndarray,
) -> numpy.ndarray:
    """
    Apply rio-tiler expression.

    Attributes
    ----------
    blocks: Tuple or List
        expression for a specific layer.
    bands: Tuple or List
        bands names.
    data: numpy.array
        array of bands.

    Returns
    -------
    data: numpy.array

    """
    data = dict(zip(bands, data))
    return numpy.array(
        [
            numpy.nan_to_num(numexpr.evaluate(bloc.strip(), local_dict=data))
            for bloc in blocks
        ]
    )
