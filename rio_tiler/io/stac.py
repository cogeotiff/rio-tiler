"""rio_tiler.io.stac: STAC reader."""

from typing import Any, Dict, Sequence, Tuple

import numpy

from rio_tiler import reader
from rio_tiler.utils import tile_exists
from rio_tiler.errors import InvalidBandName, TileOutsideBounds


def _get_href(stac: Dict, assets: Sequence[str]) -> Sequence[str]:
    """Validate asset names and return asset's url."""
    _assets = list(stac["assets"].keys())
    for asset in assets:
        if asset not in _assets:
            raise InvalidBandName(f"{asset} is not a valid asset name.")

    return [stac["assets"][asset]["href"] for asset in assets]


def spatial_info(stac: Dict) -> Dict:
    """
    Return STAC spatial info.

    Attributes
    ----------
        stac : dict
            STAC item.

    Returns
    -------
        out : dict.

    """
    raise Exception("Not implemented")


def bounds(stac: Dict) -> Dict:
    """
    Return STAC bounds.

    Attributes
    ----------
        stac : dict
            STAC item.

    Returns
    -------
        out : dict
            dictionary with image bounds.

    """
    return dict(id=stac["id"], bounds=stac["bbox"])


def metadata(
    stac: Dict,
    assets: Sequence[str],
    pmin: float = 2.0,
    pmax: float = 98.0,
    hist_options: Dict = {},
    **kwargs: Any,
) -> Dict:
    """
    Return STAC assets statistics.

    Attributes
    ----------
        stac : dict
            STAC item.
        assets : list
            Asset names.
        pmin : int, optional, (default: 2)
            Histogram minimum cut.
        pmax : int, optional, (default: 98)
            Histogram maximum cut.
        hist_options : dict, optional
            Options to forward to numpy.histogram function.
            e.g: {bins=20, range=(0, 1000)}
        kwargs : optional
            These are passed to 'rio_tiler.reader.preview'

    Returns
    -------
        out : dict
            Dictionary with image bounds and bands statistics.

    """
    if isinstance(assets, str):
        assets = (assets,)

    assets_url = _get_href(stac, assets)
    responses = reader.multi_metadata(
        assets_url, percentiles=(pmin, pmax), hist_options=hist_options, **kwargs
    )

    info: Dict[str, Any] = dict(id=stac["id"])
    info["band_descriptions"] = [(ix + 1, b) for ix, b in enumerate(assets)]
    info["bounds"] = stac["bbox"]
    info["statistics"] = {b: d["statistics"][1] for b, d in zip(assets, responses)}
    info["dtypes"] = {b: d["dtype"] for b, d in zip(assets, responses)}
    info["nodata_types"] = {b: d["nodata_type"] for b, d in zip(assets, responses)}
    return info


def tile(
    stac: Dict,
    assets: Sequence[str],
    tile_x: int,
    tile_y: int,
    tile_z: int,
    tilesize: int = 256,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Create mercator tile from any images.

    Attributes
    ----------
        stac : dict
            STAC item.
        assets : list
            Asset names.
        tile_x : int
            Mercator tile X index.
        tile_y : int
            Mercator tile Y index.
        tile_z : int
            Mercator tile ZOOM level.
        tilesize : int, optional (default: 256)
            Output image size.
        kwargs: dict, optional
            These will be passed to the 'rio_tiler.reader.tile' function.

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    if isinstance(assets, str):
        assets = (assets,)

    if not tile_exists(stac["bbox"], tile_z, tile_x, tile_y):
        raise TileOutsideBounds(
            f"Tile {tile_z}/{tile_x}/{tile_y} is outside item bounds"
        )

    assets_url = _get_href(stac, assets)
    return reader.multi_tile(assets_url, tile_x, tile_y, tile_z, **kwargs)
