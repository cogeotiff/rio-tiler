"""rio_tiler.io.stac: STAC reader."""

import functools
import json
from dataclasses import dataclass
from typing import Any, Dict, Iterator, Optional, Set, Tuple, Type
from urllib.parse import urlparse

import requests

from ..errors import InvalidAssetName
from ..utils import aws_get_object
from .base import BaseReader, MultiAssetsReader
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


@dataclass(init=False)
class STACReader(MultiAssetsReader):
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

    def __init__(
        self,
        filepath: str,
        item: Optional[Dict] = None,
        minzoom: int = 0,
        maxzoom: int = 30,
        include_assets: Optional[Set[str]] = None,
        exclude_assets: Optional[Set[str]] = None,
        include_asset_types: Set[str] = None,
        exclude_asset_types: Optional[Set[str]] = None,
        reader: Type[BaseReader] = COGReader,
        **kwargs: Any,
    ):
        """Create STACReader instance."""
        self.filepath = filepath
        self.item = item
        self.minzoom = minzoom
        self.maxzoom = maxzoom
        self.include_assets = include_assets
        self.exclude_assets = exclude_assets
        self.include_asset_types = include_asset_types or DEFAULT_VALID_TYPE
        self.exclude_asset_types = exclude_asset_types
        self.reader = reader
        self.reader_options = kwargs

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

    def _get_asset_url(self, asset: str) -> str:
        """Validate asset names and return asset's url."""
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        return self.item["assets"][asset]["href"]

    @property
    def center(self) -> Tuple[float, float, int]:
        """Dataset center + minzoom."""
        return (
            (self.bounds[0] + self.bounds[2]) / 2,
            (self.bounds[1] + self.bounds[3]) / 2,
            self.minzoom,
        )

    @property
    def spatial_info(self) -> Dict:
        """Return Dataset's spatial info."""
        return {
            "bounds": self.bounds,
            "center": self.center,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
        }
