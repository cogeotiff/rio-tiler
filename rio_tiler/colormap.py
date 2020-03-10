"""rio-tiler colormap functions."""

from typing import Dict, Tuple

import os

import numpy


def _empty_cmap() -> Dict:
    return {i: [0, 0, 0, 0] for i in range(256)}


def _update_alpha(cmap: Dict, idx: Tuple[int], alpha: int = 0) -> None:
    if not isinstance(idx, tuple):
        idx = tuple((idx,))

    for i in idx:
        cmap[i] = cmap[i][0:3] + (alpha,)


def _remove_value(cmap: Dict, idx: Tuple[int]) -> None:
    if not isinstance(idx, tuple):
        idx = tuple((idx,))

    for i in idx:
        cmap.pop(i, None)


def _update_cmap(cmap: Dict, values: Dict) -> None:
    for i, color in values.items():
        if len(color) == 3:
            color += [255]
        cmap[i] = color


def get_colormap(name: str) -> Dict:
    """
    Return colormap dict.

    Attributes
    ----------
        name : str, optional
            Colormap name (default: cfastie)

    Returns
    -------
        colormap : dict
            GDAL RGBA Color Table dictionary.

    """
    cmap_file = os.path.join(os.path.dirname(__file__), "cmap", f"{name}.npy")
    cmap = numpy.load(cmap_file)
    return {idx: value.tolist() for idx, value in enumerate(cmap)}


# From https://github.com/mojodna/marblecutter/blob/5b9040ba6c83562a465eabdbb6e8959e6a8bf041/marblecutter/utils.py#L35
def make_lut(colormap: Dict) -> numpy.ma.array:
    """
    Create a lookup table numpy.ma.array from a GDAL RGBA Color Table dictionary.

    Attributes
    ----------
        colormap : dict
            GDAL RGBA Color Table dictionary.

    Returns
    -------
        lut : numpy.ndarray
            returns a JSON like object with the metadata.

    """
    lut = numpy.zeros(shape=(256, 4), dtype=numpy.uint8)
    for i, color in colormap.items():
        lut[int(i)] = color
    return lut


def apply_cmap(data: numpy.ndarray, cmap: Dict) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Apply colormap on tile data.

    Attributes
    ----------
        colormap : dict
            GDAL RGBA Color Table dictionary.

    Returns
    -------
        lut : numpy.array
            returns a JSON like object with the metadata.

    """
    if data.shape[0] > 1:
        raise Exception("Source data must be 1 band")

    lookup_table = make_lut(cmap)

    # apply the color map
    data = lookup_table[data[0], :]
    data = numpy.transpose(data, [2, 0, 1])
    return data[:-1], data[-1]
