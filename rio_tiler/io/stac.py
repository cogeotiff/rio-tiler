"""rio_tiler.io.stac: STAC reader."""

import functools
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Sequence, Set, Tuple, Union
from urllib.parse import urlparse

import numpy
import requests

from ..errors import InvalidAssetName, MissingAssets
from ..expression import apply_expression
from ..utils import aws_get_object
from .base import BaseReader
from .cogeo import (
    multi_info,
    multi_metadata,
    multi_part,
    multi_point,
    multi_preview,
    multi_stats,
    multi_tile,
)

DEFAULT_VALID_TYPE = {
    "image/tiff; application=geotiff",
    "image/tiff; application=geotiff; profile=cloud-optimized",
    "image/vnd.stac.geotiff; cloud-optimized=true",
    "image/tiff",
    "image/x.geotiff",
    "image/jp2",
    "application/x-hdf5",
    "application/x-hdf",
}


@functools.lru_cache(maxsize=512)
def fetch(filepath: str) -> Dict:
    """Fetch items."""
    parsed = urlparse(filepath)
    if parsed.scheme == "s3":
        bucket = parsed.netloc
        key = parsed.path.strip("/")
        return json.loads(aws_get_object(bucket, key))

    elif parsed.scheme in ["https", "http", "ftp"]:
        return requests.get(filepath).json()

    else:
        with open(filepath, "r") as f:
            return json.load(f)


def _get_assets(
    item: Dict,
    include: Optional[Set[str]] = None,
    exclude: Optional[Set[str]] = None,
    include_asset_types: Optional[Set[str]] = None,
    exclude_asset_types: Optional[Set[str]] = None,
) -> Iterator:
    """Get Asset list."""
    for asset, asset_info in item["assets"].items():
        _type = asset_info.get("type")

        if exclude and asset in exclude:
            continue

        if (
            _type
            and (exclude_asset_types and _type in exclude_asset_types)
            or (include and asset not in include)
        ):
            continue

        if (
            _type
            and (include_asset_types and _type not in include_asset_types)
            or (include and asset not in include)
        ):
            continue

        yield asset


@dataclass
class STACReader(BaseReader):
    """
    STAC + Cloud Optimized GeoTIFF Reader.

    Examples
    --------
    with STACReader(stac_path) as stac:
        stac.tile(...)

    my_stac = {
        "type": "Feature",
        "stac_version": "1.0.0",
        ...
    }
    with STACReader(None, item=my_stac) as stac:
        stac.tile(...)

    Attributes
    ----------
    filepath: str
        STAC Item path, URL or S3 URL.
    item: Dict, optional
        STAC Item dict.
    minzoom: int, optional
        Set minzoom for the tiles.
    minzoom: int, optional
        Set maxzoom for the tiles.
    include_assets: Set, optional
        Only accept some assets.
    exclude_assets: Set, optional
        Exclude some assets.
    include_asset_types: Set, optional
        Only include some assets base on their type
    include_asset_types: Set, optional
        Exclude some assets base on their type

    Properties
    ----------
    bounds: tuple[float]
        STAC bounds in WGS84 crs.
    center: tuple[float, float, int]
        STAC item center + minzoom

    Methods
    -------
    tile(0, 0, 0, assets="B01", expression="B01/B02")
        Read a map tile from the COG.
    part((0,10,0,10), assets="B01", expression="B1/B20", max_size=1024)
        Read part of the COG.
    preview(assets="B01", max_size=1024)
        Read preview of the COG.
    point((10, 10), assets="B01")
        Read a point value from the COG.
    stats(assets="B01", pmin=5, pmax=95)
        Get Raster statistics.
    info(assets="B01")
        Get Assets raster info.
    metadata(assets="B01", pmin=5, pmax=95)
        info + stats

    """

    filepath: str
    item: Optional[Dict] = None
    minzoom: int = 0
    maxzoom: int = 30
    include_assets: Optional[Set[str]] = None
    exclude_assets: Optional[Set[str]] = None
    include_asset_types: Set[str] = field(default_factory=lambda: DEFAULT_VALID_TYPE)
    exclude_asset_types: Optional[Set[str]] = None

    def __enter__(self):
        """Support using with Context Managers."""
        self.item = self.item or fetch(self.filepath)

        # Get Zooms from proj: ?
        self.bounds: Tuple[float, float, float, float] = self.item["bbox"]

        self.assets = list(
            _get_assets(
                self.item,
                include=self.include_assets,
                exclude=self.exclude_assets,
                include_asset_types=self.include_asset_types,
                exclude_asset_types=self.exclude_asset_types,
            )
        )
        if not self.assets:
            raise Exception("No valid asset found")

        return self

    def __exit__(self, *args):
        """Support using with Context Managers."""
        pass

    def _get_href(self, assets: Sequence[str]) -> Sequence[str]:
        """Validate asset names and return asset's url."""
        invalid_assets = set(assets) - set(self.assets)
        if invalid_assets:
            raise InvalidAssetName(f"{invalid_assets} is/are not valid")

        return [self.item["assets"][asset]["href"] for asset in assets]

    def _parse_expression(self, expression: str) -> Sequence[str]:
        """Parse rio-tiler band math expression."""
        _re = re.compile("|".join(sorted(self.assets, reverse=True)))
        assets = list(set(re.findall(_re, expression)))
        return assets

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",  # Expression based on asset names
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Mercator Map tile from a COGs."""
        if isinstance(assets, str):
            assets = (assets,)

        if expression:
            assets = self._parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_urls = self._get_href(assets)
        data, mask = multi_tile(
            asset_urls, tile_x, tile_y, tile_z, expression=asset_expression, **kwargs,
        )

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def part(
        self,
        bbox: Tuple[float, float, float, float],
        max_size: int = 1024,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",  # Expression based on asset names
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read part of COGs."""
        if isinstance(assets, str):
            assets = (assets,)

        if expression:
            assets = self._parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_urls = self._get_href(assets)
        data, mask = multi_part(
            asset_urls, bbox, max_size=max_size, expression=asset_expression, **kwargs
        )

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def preview(
        self,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",  # Expression based on asset names
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Return a preview of COGs."""
        if isinstance(assets, str):
            assets = (assets,)

        if expression:
            assets = self._parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_urls = self._get_href(assets)
        data, mask = multi_preview(asset_urls, expression=asset_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            data = apply_expression(blocks, assets, data)

        return data, mask

    def point(
        self,
        lon: float,
        lat: float,
        assets: Union[Sequence[str], str] = None,
        expression: Optional[str] = "",  # Expression based on asset names
        asset_expression: Optional[
            str
        ] = "",  # Expression for each asset based on index names
        **kwargs: Any,
    ) -> List:
        """Read a value from COGs."""
        if isinstance(assets, str):
            assets = (assets,)

        if expression:
            assets = self._parse_expression(expression)

        if not assets:
            raise MissingAssets(
                "assets must be passed either via expression or assets options."
            )

        asset_urls = self._get_href(assets)
        point = multi_point(asset_urls, lon, lat, expression=asset_expression, **kwargs)

        if expression:
            blocks = expression.split(",")
            point = apply_expression(blocks, assets, point).tolist()

        return point

    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        hist_options: Optional[Dict] = None,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict:
        """Return array statistics from COGs."""
        if not assets:
            raise MissingAssets("Missing 'assets'")

        if isinstance(assets, str):
            assets = (assets,)

        asset_urls = self._get_href(assets)

        stats = multi_stats(asset_urls, pmin, pmax, hist_options=hist_options, **kwargs)
        return {asset: stats[ix] for ix, asset in enumerate(assets)}

    def info(self, assets: Union[Sequence[str], str] = None) -> Dict:
        """Return info from COGs."""
        if not assets:
            raise MissingAssets("Missing 'assets'")

        if isinstance(assets, str):
            assets = (assets,)

        asset_urls = self._get_href(assets)

        infos = multi_info(asset_urls)
        return {asset: infos[ix] for ix, asset in enumerate(assets)}

    def metadata(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        assets: Union[Sequence[str], str] = None,
        **kwargs: Any,
    ) -> Dict:
        """Return array statistics from COGs."""
        if not assets:
            raise MissingAssets("Missing 'assets'")

        if isinstance(assets, str):
            assets = (assets,)

        asset_urls = self._get_href(assets)

        stats = multi_metadata(asset_urls, pmin, pmax, **kwargs)
        return {asset: stats[ix] for ix, asset in enumerate(assets)}
