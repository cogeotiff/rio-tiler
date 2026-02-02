"""rio-tiler.expression: Parse and Apply expression."""

import re
from collections.abc import Sequence

import numexpr
import numpy

from rio_tiler.errors import InvalidExpression


def parse_expression(expression: str, cast: bool = True) -> tuple:
    """Parse rio-tiler band math expression and extract bands.

    Args:
        expression (str): band math/combination expression.
        cast (bool): cast band names to integers (convert to index values). Defaults to True.

    Returns:
        tuple: band names/indexes.

    Examples:
        >>> parse_expression("b1+b2")
            (1, 2)

        >>> parse_expression("B1/B2", cast=False)
            ('1', '2')

    """
    bands = set(re.findall(r"\bb(?P<bands>[0-9A-Z]+)\b", expression, re.IGNORECASE))
    output_bands = tuple(map(int, bands)) if cast else tuple(bands)
    if not output_bands:
        raise InvalidExpression(
            f"Could not find any valid bands in '{expression}' expression."
        )

    return output_bands


def get_expression_blocks(expression: str) -> list[str]:
    """Split expression in blocks.

    Args:
        expression (str): band math/combination expression.

    Returns:
        list: expression blocks (str).

    Examples:
        >>> get_expression_blocks("b1/b2;b2+b1")
            ['b1/b2', 'b2+b1']

    """
    return [expr.lower() for expr in expression.split(";") if expr]


def apply_expression(
    blocks: Sequence[str],
    bands: Sequence[str],
    data: numpy.ndarray,
) -> numpy.ma.MaskedArray:
    """Apply rio-tiler expression.

    Args:

        blocks (sequence): expression for a specific layer.
        bands (sequence): bands names.
        data (numpy.array):  array of bands.

    Returns:
        numpy.array: output data.

    """
    if len(bands) != data.shape[0]:
        raise ValueError(
            f"Incompatible number of bands ({bands}) and data shape {data.shape}"
        )

    try:
        return numpy.ma.MaskedArray(
            [
                numpy.nan_to_num(
                    numexpr.evaluate(bloc.strip(), local_dict=dict(zip(bands, data)))
                )
                for bloc in blocks
                if bloc
            ]
        )
    except KeyError as e:
        raise InvalidExpression(f"Invalid band/asset name {str(e)}") from e
