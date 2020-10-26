"""rio_tiler.io.stac: STAC reader."""

import functools
import json
from typing import Dict, Iterator, Optional, Set, Type
from urllib.parse import urlparse

import attr
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


@attr.s
class STACReader(MultiBaseReader):
    """
    STAC + Cloud Optimized GeoTIFF Reader.

    Examples
    --------
    with STACReader(stac_path) as stac:
        stac.tile(...)

    with STACReader(stac_path, reader=MyCustomReader, reader_options={...}) as stac:
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
    reader: BaseReader, optional
        rio-tiler Reader (default is set to rio_tiler.io.COGReader)
    reader_options: dict, optional
        additional option to forward to the Reader (default is {}).

    Properties
    ----------
    bounds: tuple[float]
        STAC bounds in WGS84 crs.
    center: tuple[float, float, int]
        STAC item center + minzoom
    spatial_info: dict
        STAC spatial info (zoom, bounds and center)

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

    filepath: str = attr.ib()
    item: Dict = attr.ib(default=None)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=0)
    maxzoom: int = attr.ib(default=30)
    include_assets: Optional[Set[str]] = attr.ib(default=None)
    exclude_assets: Optional[Set[str]] = attr.ib(default=None)
    include_asset_types: Set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: Optional[Set[str]] = attr.ib(default=None)
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        self.item = self.item or fetch(self.filepath)
        self.bounds = self.item["bbox"]
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

    def _get_asset_url(self, asset: str) -> str:
        """Validate asset names and return asset's url."""
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        return self.item["assets"][asset]["href"]
