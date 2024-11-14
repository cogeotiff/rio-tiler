"""rio-tiler colormap functions and classes."""

import json
import os
import pathlib
import re
import warnings
from typing import Dict, List, Sequence, Tuple, Union

import attr
import numpy

from rio_tiler.errors import (
    ColorMapAlreadyRegistered,
    InvalidColorFormat,
    InvalidColorMapName,
    InvalidFormat,
)
from rio_tiler.types import (
    ColorMapType,
    DataMaskType,
    DiscreteColorMapType,
    GDALColorMapType,
    IntervalColorMapType,
)

try:
    from importlib.resources import as_file
    from importlib.resources import files as resources_files
except ImportError:
    # Try backported to PY<39 `importlib_resources`.
    from importlib_resources import as_file  # type: ignore
    from importlib_resources import files as resources_files  # type: ignore


EMPTY_COLORMAP: GDALColorMapType = {i: (0, 0, 0, 0) for i in range(256)}

_RIO_CMAP_DIR = resources_files(__package__) / "cmap_data"
with as_file(_RIO_CMAP_DIR) as p:
    DEFAULT_CMAPS_FILES = {
        f.stem: f for f in p.glob("**/*") if f.suffix in {".npy", ".json"}
    }

USER_CMAPS_DIR = os.environ.get("COLORMAP_DIRECTORY", None)
if USER_CMAPS_DIR:
    DEFAULT_CMAPS_FILES.update(
        {
            f.stem: f
            for f in pathlib.Path(USER_CMAPS_DIR).glob("**/*")
            if f.suffix in {".npy", ".json"}
        }
    )


def _update_alpha(cmap: GDALColorMapType, idx: Sequence[int], alpha: int = 0) -> None:
    """Update the alpha value of a colormap index."""
    if isinstance(idx, int):
        idx = (idx,)

    for i in idx:
        cmap[i] = cmap[i][0:3] + (alpha,)


def _remove_value(cmap: GDALColorMapType, idx: Sequence[int]) -> None:
    """Remove value from a colormap dict."""
    if isinstance(idx, int):
        idx = (idx,)

    for i in idx:
        cmap.pop(i, None)


def _update_cmap(cmap: GDALColorMapType, values: GDALColorMapType) -> None:
    """Update a colormap dict."""
    for i, color in values.items():
        cmap[i] = color


# From https://github.com/mojodna/marblecutter/blob/5b9040ba6c83562a465eabdbb6e8959e6a8bf041/marblecutter/utils.py#L35
def make_lut(colormap: GDALColorMapType) -> numpy.ndarray:
    """Create a lookup table numpy.ndarray from a GDAL RGBA Color Table dictionary.

    Args:
        colormap (dict): GDAL RGBA Color Table dictionary.

    Returns:
        numpy.ndarray: colormap lookup table.

    """
    lut = numpy.zeros(shape=(256, 4), dtype=numpy.uint8)
    for i, color in colormap.items():
        lut[int(i)] = numpy.array(color)

    return lut


def apply_cmap(data: numpy.ndarray, colormap: ColorMapType) -> DataMaskType:
    """Apply colormap on data.

    Args:
        data (numpy.ndarray): 1D image array to translate to RGB.
        colormap (dict or sequence): GDAL RGBA Color Table dictionary or sequence (for intervals).

    Returns:
        tuple: Data (numpy.ndarray) and Mask (numpy.ndarray) values.

    Raises:
        InvalidFormat: If data is not a 1 band dataset (1, col, row).

    """
    if data.shape[0] > 1:
        raise InvalidFormat("Source data must be 1 band")

    if isinstance(colormap, Sequence):
        return apply_intervals_cmap(data, colormap)

    # if colormap has less or more than 256 values OR its `max` key >= 256 we can't use
    # rio_tiler.colormap.make_lut, because we don't want to create a `lookup table`
    # with more than 256 entries (256 x 4) array. In this case we use `apply_discrete_cmap`
    # which can work with arbitrary colormap dict.
    if (
        len(colormap) != 256
        or max(colormap) >= 256
        or min(colormap) < 0
        or any(isinstance(k, float) for k in colormap)
    ):
        return apply_discrete_cmap(data, colormap)

    # For now we assume ColorMap are in uint8
    if data.dtype != numpy.uint8:
        warnings.warn(
            f"Input array is of type {data.dtype} and `will be converted to Int in order to apply the ColorMap.",
            UserWarning,
        )
        data = data.astype(numpy.uint8)

    lookup_table = make_lut(colormap)  # type: ignore
    data = lookup_table[data[0], :]

    data = numpy.transpose(data, [2, 0, 1])

    return data[:-1], data[-1]


def apply_discrete_cmap(
    data: numpy.ndarray, colormap: Union[GDALColorMapType, DiscreteColorMapType]
) -> DataMaskType:
    """Apply discrete colormap.

    Args:
        data (numpy.ndarray): 1D image array to translate to RGB.
        colormap (GDALColorMapType or DiscreteColorMapType): Discrete ColorMap dictionary.

    Returns:
        tuple: Data (numpy.ndarray) and Alpha band (numpy.ndarray).

    Examples:
        >>> data = numpy.random.randint(0, 3, size=(1, 256, 256))
            cmap = {
                0: (0, 0, 0, 0),
                1: (255, 255, 255, 255),
                2: (255, 0, 0, 255),
                3: (255, 255, 0, 255),
            }
            data, mask = apply_discrete_cmap(data, cmap)
            assert data.shape == (3, 256, 256)

    """
    res = numpy.zeros((data.shape[1], data.shape[2], 4), dtype=numpy.uint8)

    for k, v in colormap.items():
        res[data[0] == k] = numpy.array(v)

    data = numpy.transpose(res, [2, 0, 1])

    # If the output data has values between 0-255
    # we cast the output array to Uint8
    if data.min() >= 0 and data.max() <= 255:
        data = data.astype("uint8")

    return data[:-1], data[-1]


def apply_intervals_cmap(
    data: numpy.ndarray, colormap: IntervalColorMapType
) -> DataMaskType:
    """Apply intervals colormap.

    Args:
        data (numpy.ndarray): 1D image array to translate to RGB.
        colormap (IntervalColorMapType): Sequence of intervals and color in form of [([min, max], [r, g, b, a]), ...].

    Returns:
        tuple: Data (numpy.ndarray) and Alpha band (numpy.ndarray).

    Examples:
        >>> data = numpy.random.randint(0, 3, size=(1, 256, 256))
            cmap = [
                ((0, 1), (0, 0, 0, 0)),
                ((1, 2), (255, 255, 255, 255)),
                ((2, 3), (255, 0, 0, 255)),
                ((3, 4), (255, 255, 0, 255)),
            ]

            data, mask = apply_intervals_cmap(data, cmap)
            assert data.shape == (3, 256, 256)

    """
    res = numpy.zeros((data.shape[1], data.shape[2], 4), dtype=numpy.uint8)

    for k, v in colormap:
        res[(data[0] >= k[0]) & (data[0] < k[1])] = numpy.array(v)

    data = numpy.transpose(res, [2, 0, 1])

    # If the output data has values between 0-255
    # we cast the output array to Uint8
    if data.min() >= 0 and data.max() <= 255:
        data = data.astype("uint8")

    return data[:-1], data[-1]


def parse_color(rgba: Union[Sequence[int], str]) -> Tuple[int, int, int, int]:
    """Parse RGB/RGBA color and return valid rio-tiler compatible RGBA colormap entry.

    Args:
        rgba (str or list of int): HEX encoded or list RGB or RGBA colors.

    Returns:
        tuple: RGBA values.

    Examples:
        >>> parse_color("#FFF")
        (255, 255, 255, 255)

        >>> parse_color("#FF0000FF")
        (255, 0, 0, 255)

        >>> parse_color("#FF0000")
        (255, 0, 0, 255)

        >>> parse_color([255, 255, 255])
        (255, 255, 255, 255)

    """
    if isinstance(rgba, str):
        if re.match("^#[a-fA-F0-9]{3,4}$", rgba):
            factor = 2
            hex_pattern = (
                r"^#"
                r"(?P<red>[a-fA-F0-9])"
                r"(?P<green>[a-fA-F0-9])"
                r"(?P<blue>[a-fA-F0-9])"
                r"(?P<alpha>[a-fA-F0-9])?"
                r"$"
            )
        elif re.match("^#([a-fA-F0-9][a-fA-F0-9]){3,4}$", rgba):
            factor = 1
            hex_pattern = (
                r"^#"
                r"(?P<red>[a-fA-F0-9][a-fA-F0-9])"
                r"(?P<green>[a-fA-F0-9][a-fA-F0-9])"
                r"(?P<blue>[a-fA-F0-9][a-fA-F0-9])"
                r"(?P<alpha>[a-fA-F0-9][a-fA-F0-9])?"
                r"$"
            )
        else:
            raise InvalidColorFormat(f"Invalid color format: {rgba}")

        match = re.match(hex_pattern, rgba)
        rgba = [
            int(n * factor, 16)
            for n in match.groupdict().values()
            if n is not None  # type: ignore
        ]

    if len(rgba) > 4 or len(rgba) < 3:
        raise InvalidColorFormat(f"Invalid color format: {rgba}")

    rgba = tuple(rgba)
    if len(rgba) == 3:
        rgba += (255,)

    return rgba  # type: ignore


@attr.s(frozen=True)
class ColorMaps:
    """Default Colormaps holder.

    Attributes:
        data (dict): colormaps. Defaults to `rio_tiler.colormap.DEFAULTS_CMAPS`.

    """

    data: Dict[str, Union[str, pathlib.Path, ColorMapType]] = attr.ib(
        default=attr.Factory(lambda: DEFAULT_CMAPS_FILES)
    )

    def get(self, name: str) -> ColorMapType:
        """Fetch a colormap.

        Args:
            name (str): colormap name.

        Returns
            dict: colormap dictionary.

        """
        cmap = self.data.get(name, None)
        if cmap is None:
            raise InvalidColorMapName(f"Invalid colormap name: {name}")

        if isinstance(cmap, (pathlib.Path, str)):
            if isinstance(cmap, str):
                cmap = pathlib.Path(cmap)

            if cmap.suffix == ".npy":
                colormap = numpy.load(cmap)
                assert colormap.shape == (256, 4)
                assert colormap.dtype == numpy.uint8
                cmap_data = {idx: tuple(value) for idx, value in enumerate(colormap)}

            elif cmap.suffix == ".json":
                with cmap.open() as f:
                    cmap_data = json.load(
                        f,
                        object_hook=lambda x: {
                            int(k): parse_color(v) for k, v in x.items()
                        },
                    )

                # Make sure to match colormap type
                if isinstance(cmap_data, Sequence):
                    cmap_data = [
                        (tuple(inter), parse_color(v))  # type: ignore
                        for (inter, v) in cmap_data
                    ]

            else:
                raise ValueError(f"Not supported {cmap.suffix} extension for ColorMap")

            # save the numpy array / dict / sequence in the data dict
            # avoiding the need to re-load the data
            self.data[name] = cmap_data
            return cmap_data

        return cmap

    def list(self) -> List[str]:
        """List registered Colormaps.

        Returns
            list: list of colormap names.

        """
        return list(self.data)

    def register(
        self,
        custom_cmap: Dict[str, Union[str, pathlib.Path, ColorMapType]],
        overwrite: bool = False,
    ) -> "ColorMaps":
        """Register a custom colormap.

        Args:
            custom_cmap (dict): custom colormap(s) to register.
            overwrite (bool): Overwrite existing colormap with same key. Defaults to False.

        Examples:
            >>> cmap = cmap.register({"acmap": {0: (0, 0, 0, 0), ...}})

            >>> cmap = cmap.register({"acmap": "acmap.npy"})

        """
        for name, _ in custom_cmap.items():
            if not overwrite and name in self.data:
                raise ColorMapAlreadyRegistered(
                    f"{name} is already registered. Use force=True to overwrite."
                )

        return ColorMaps({**self.data, **custom_cmap})


cmap = ColorMaps()  # noqa
