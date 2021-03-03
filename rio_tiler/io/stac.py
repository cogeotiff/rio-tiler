"""rio_tiler.io.stac: STAC reader."""

import functools
import json
from typing import Dict, Iterator, Optional, Set, Type, Union
from urllib.parse import urlparse

import attr
import pystac
import requests
from morecantile import TileMatrixSet

from ..constants import WEB_MERCATOR_TMS
from ..errors import InvalidAssetName, MissingAssets
from ..utils import aws_get_object
from .base import BaseReader, MultiBaseReader
from .cogeo import COGReader

DEFAULT_VALID_TYPE = {
    "image/tiff; application=geotiff",
    "image/tiff; application=geotiff; profile=cloud-optimized",
    "image/tiff; profile=cloud-optimized; application=geotiff",
    pystac.MediaType.COG,
    "image/vnd.stac.geotiff; cloud-optimized=true",
    "image/tiff",
    "image/x.geotiff",
    "image/jp2",
    "application/x-hdf5",
    "application/x-hdf",
}


@functools.lru_cache(maxsize=512)
def fetch(filepath: str) -> Dict:
    """Fetch STAC items.

    A LRU cache is set on top of this function.

    Args:
        filepath (str): STAC item URL.

    Returns:
        dict: STAC Item content.

    """
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
    stac_item: pystac.Item,
    include: Optional[Set[str]] = None,
    exclude: Optional[Set[str]] = None,
    include_asset_types: Optional[Set[str]] = None,
    exclude_asset_types: Optional[Set[str]] = None,
) -> Iterator:
    """Get valid asset list.

    Args:
        stac_item (pystac.Item): STAC Item.
        include (Optional[Set[str]]): Only Include specific assets.
        exclude (Optional[Set[str]]): Exclude specific assets.
        include_asset_types (Optional[Set[str]]): Only include some assets base on their type.
        exclude_asset_types (Optional[Set[str]]): Exclude some assets base on their type.

    Yields
        str: valid STAC asset name.

    """
    for asset, asset_info in stac_item.get_assets().items():
        _type = asset_info.media_type

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


def _to_pystac_item(item: Union[None, Dict, pystac.Item]) -> Union[None, pystac.Item]:
    """Attr converter to convert to Dict to pystac.Item

    Args:
        stac_item (Union[Dict, pystac.Item]): STAC Item.

    Returns
        pystac.Item: pystac STAC item object.

    """
    if isinstance(item, Dict):
        return pystac.Item.from_dict(item)

    return item


@attr.s
class STACReader(MultiBaseReader):
    """STAC Reader.

    Attributes:
        filepath (str): STAC Item path, URL or S3 URL.
        item (dict or pystac.Item, STAC): Stac Item.
        minzoom (int, optional): Set minzoom for the tiles.
        minzoom (int, optional): Set maxzoom for the tiles.
        include (set of string, optional): Only Include specific assets.
        exclude (set of string, optional): Exclude specific assets.
        include_asset_types (set of string, optional): Only include some assets base on their type.
        exclude_asset_types (set of string, optional): Exclude some assets base on their type.
        reader (rio_tiler.io.BaseReader, optional): rio-tiler Reader. Defaults to `rio_tiler.io.COGReader`.
        reader_options (dict, optional): additional option to forward to the Reader. Defaults to `{}`.

    Examples:
        >>> with STACReader(stac_path) as stac:
            stac.tile(...)

        >>> with STACReader(stac_path, reader=MyCustomReader, reader_options={...}) as stac:
            stac.tile(...)

        >>> my_stac = {
                "type": "Feature",
                "stac_version": "1.0.0",
                ...
            }
            with STACReader(None, item=my_stac) as stac:
                # the dict will be translated to a pystac item
                assert isinstance(stac.item, pystac.Item)
                stac.tile(...)

    """

    filepath: str = attr.ib()
    item: pystac.Item = attr.ib(default=None, converter=_to_pystac_item)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)
    include_assets: Optional[Set[str]] = attr.ib(default=None)
    exclude_assets: Optional[Set[str]] = attr.ib(default=None)
    include_asset_types: Set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: Optional[Set[str]] = attr.ib(default=None)
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.item = self.item or pystac.Item.from_dict(
            fetch(self.filepath), self.filepath
        )
        self.bounds = self.item.bbox
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
            raise MissingAssets("No valid asset found")

        if self.minzoom is None:
            self.minzoom = self.tms.minzoom

        if self.maxzoom is None:
            self.maxzoom = self.tms.maxzoom

    def _get_asset_url(self, asset: str) -> str:
        """Validate asset names and return asset's url.

        Args:
            asset (str): STAC asset name.

        Returns:
            str: STAC asset href.

        """
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        return self.item.assets[asset].get_absolute_href()
