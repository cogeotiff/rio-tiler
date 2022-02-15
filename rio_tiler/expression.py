"""rio-tiler.expression: Parse and Apply expression."""

import re
import warnings
from typing import List, Sequence, Tuple, Union

import numexpr
import numpy


def parse_expression(expression: str, cast: bool = True) -> Tuple:
    """Parse rio-tiler band math expression.

    Args:
        expression (str): band math/combination expression.
        cast (bool): cast band names to integers (convert to index values). Defaults to True.

    Returns:
        tuple: band names/indexes.

    Examples:
        >>> parse_expression("b1,b2")
            (2, 1)

        >>> parse_expression("B1/B2", cast=False)
            ("2", "1")

    """
    bands = set(re.findall(r"\bb(?P<bands>[0-9A-Z]+)\b", expression, re.IGNORECASE))
    return tuple(map(int, bands)) if cast else tuple(bands)


def get_expression_blocks(expression: str) -> List[str]:
    """Split expression in blocks.

    Args:
        expression (str): band math/combination expression.

    Returns:
        list: expression blocks (str).

    Examples:
        >>> parse_expression("b1/b2,b2+b1")
            ("b1/b2", "b2+b1")

    """
    if ";" in expression:
        return [expr for expr in expression.split(";") if expr]

    expr = [expr for expr in expression.split(",") if expr]
    if len(expr) > 1:
        warnings.warn(
            "Using comma `,` for multiband expression will be deprecated in rio-tiler 4.0. Please use semicolon `;`.",
            DeprecationWarning,
        )

    return expr


def apply_expression(
    blocks: Sequence[str],
    bands: Sequence[Union[str, int]],
    data: numpy.ndarray,
) -> numpy.ndarray:
    """Apply rio-tiler expression.

    Args:

        blocks (sequence): expression for a specific layer.
        bands (sequence): bands names.
        data (numpy.array):  array of bands.

    Returns:
        numpy.array: output data.

    """
    return numpy.array(
        [
            numpy.nan_to_num(
                numexpr.evaluate(bloc.strip(), local_dict=dict(zip(bands, data)))
            )
            for bloc in blocks
            if bloc
        ]
    )
