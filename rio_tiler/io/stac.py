"""rio_tiler.io.stac: STAC reader."""

import json
from typing import Any, Dict, Iterator, Optional, Set, Type, Union
from urllib.parse import urlparse

import attr
import httpx
import pystac
import rasterio
from cachetools import LRUCache, cached
from cachetools.keys import hashkey
from morecantile import TileMatrixSet
from rasterio.crs import CRS

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidAssetName, MissingAssets
from rio_tiler.io.base import BaseReader, MultiBaseReader
from rio_tiler.io.rasterio import Reader
from rio_tiler.types import AssetInfo
from rio_tiler.utils import aws_get_object

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


@cached(
    LRUCache(maxsize=512),
    key=lambda filepath, **kargs: hashkey(filepath, json.dumps(kargs)),
)
def fetch(filepath: str, **kwargs: Any) -> Dict:
    """Fetch STAC items.

    A LRU cache is set on top of this function.

    Args:
        filepath (str): STAC item URL.
        kwargs (any): additional options to pass to client.

    Returns:
        dict: STAC Item content.

    """
    parsed = urlparse(filepath)
    if parsed.scheme == "s3":
        bucket = parsed.netloc
        key = parsed.path.strip("/")
        return json.loads(aws_get_object(bucket, key, **kwargs))

    elif parsed.scheme in ["https", "http", "ftp"]:
        resp = httpx.get(filepath, **kwargs)
        resp.raise_for_status()
        return resp.json()
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
        input (str): STAC Item path, URL or S3 URL.
        item (dict or pystac.Item, STAC): Stac Item.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set minzoom for the tiles.
        maxzoom (int, optional): Set maxzoom for the tiles.
        geographic_crs (rasterio.crs.CRS, optional): CRS to use as geographic coordinate system. Defaults to WGS84.
        include_assets (set of string, optional): Only Include specific assets.
        exclude_assets (set of string, optional): Exclude specific assets.
        include_asset_types (set of string, optional): Only include some assets base on their type.
        exclude_asset_types (set of string, optional): Exclude some assets base on their type.
        reader (rio_tiler.io.BaseReader, optional): rio-tiler Reader. Defaults to `rio_tiler.io.Reader`.
        reader_options (dict, optional): Additional option to forward to the Reader. Defaults to `{}`.
        fetch_options (dict, optional): Options to pass to `rio_tiler.io.stac.fetch` function fetching the STAC Items. Defaults to `{}`.

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

    input: str = attr.ib()
    item: pystac.Item = attr.ib(default=None, converter=_to_pystac_item)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib()
    maxzoom: int = attr.ib()

    geographic_crs: CRS = attr.ib(default=WGS84_CRS)

    include_assets: Optional[Set[str]] = attr.ib(default=None)
    exclude_assets: Optional[Set[str]] = attr.ib(default=None)

    include_asset_types: Set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: Optional[Set[str]] = attr.ib(default=None)

    reader: Type[BaseReader] = attr.ib(default=Reader)
    reader_options: Dict = attr.ib(factory=dict)

    fetch_options: Dict = attr.ib(factory=dict)

    ctx: Any = attr.ib(default=rasterio.Env)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.item = self.item or pystac.Item.from_dict(
            fetch(self.input, **self.fetch_options), self.input
        )

        # TODO: get bounds/crs using PROJ extension if available
        self.bounds = self.item.bbox
        self.crs = WGS84_CRS

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

    @minzoom.default
    def _minzoom(self):
        return self.tms.minzoom

    @maxzoom.default
    def _maxzoom(self):
        return self.tms.maxzoom

    def _get_asset_info(self, asset: str) -> AssetInfo:
        """Validate asset names and return asset's url.

        Args:
            asset (str): STAC asset name.

        Returns:
            str: STAC asset href.

        """
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        asset_info = self.item.assets[asset]
        info = AssetInfo(url=asset_info.get_absolute_href())

        if "file:header_size" in asset_info.extra_fields:
            h = asset_info.extra_fields["file:header_size"]
            info["env"] = {"GDAL_INGESTED_BYTES_AT_OPEN": h}

        return info
