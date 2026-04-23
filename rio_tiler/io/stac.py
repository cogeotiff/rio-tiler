"""rio_tiler.io.stac: STAC reader."""

import json
import math
import os
import warnings
from collections.abc import Iterator, Sequence
from threading import Lock
from typing import Any, TypedDict
from urllib.parse import urlparse

import attr
import httpx
import pystac
import rasterio
from affine import Affine
from cachetools import LRUCache, cached
from cachetools.keys import hashkey
from morecantile import TileMatrixSet
from rasterio.crs import CRS
from rasterio.features import bounds as featureBounds
from rasterio.transform import array_bounds, from_bounds

from rio_tiler.constants import STAC_ALTERNATE_KEY, WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidAssetName, MissingAssets
from rio_tiler.io.base import BaseReader, MultiBaseReader
from rio_tiler.io.rasterio import Reader
from rio_tiler.types import AssetInfo, AssetType, AssetWithOptions

try:
    from boto3.session import Session as boto3_session

except ImportError:  # pragma: nocover
    boto3_session = None  # type: ignore


lru_cache = LRUCache(maxsize=512)  # type: ignore


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


def aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = False,
    client: "boto3_session.client" = None,
) -> bytes:
    """AWS s3 get object content."""
    assert boto3_session is not None, "'boto3' must be installed to use s3:// urls"

    if not client:
        if profile_name := os.environ.get("AWS_PROFILE", None):
            session = boto3_session(profile_name=profile_name)

        else:
            access_key = os.environ.get("AWS_ACCESS_KEY_ID", None)
            secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
            access_token = os.environ.get("AWS_SESSION_TOKEN", None)

            # AWS_REGION is GDAL specific. Later overloaded by standard AWS_DEFAULT_REGION
            region_name = os.environ.get(
                "AWS_DEFAULT_REGION", os.environ.get("AWS_REGION", None)
            )

            session = boto3_session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_access_key,
                aws_session_token=access_token,
                region_name=region_name or None,
            )

        # AWS_S3_ENDPOINT and AWS_HTTPS are GDAL config options of vsis3 driver
        # https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files
        endpoint_url = os.environ.get("AWS_S3_ENDPOINT", None)
        if endpoint_url:
            use_https = os.environ.get("AWS_HTTPS", "YES")
            if use_https.upper() in ["YES", "TRUE", "ON"]:
                endpoint_url = "https://" + endpoint_url

            else:
                endpoint_url = "http://" + endpoint_url

        client = session.client("s3", endpoint_url=endpoint_url)

    params = {"Bucket": bucket, "Key": key}
    if request_pays or os.environ.get("AWS_REQUEST_PAYER", "").lower() == "requester":
        params["RequestPayer"] = "requester"

    response = client.get_object(**params)
    return response["Body"].read()


@cached(  # type: ignore
    lru_cache,
    key=lambda filepath, **kargs: hashkey(filepath, json.dumps(kargs)),
    lock=Lock(),
)
def fetch(filepath: str, **kwargs: Any) -> dict:
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
    include: set[str] | None = None,
    exclude: set[str] | None = None,
    include_asset_types: set[str] | None = None,
    exclude_asset_types: set[str] | None = None,
) -> Iterator[str]:
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


def _to_pystac_item(item: dict | pystac.Item) -> pystac.Item:
    """Attr converter to convert to Dict to pystac.Item

    Args:
        item (Union[Dict, pystac.Item]): STAC Item.

    Returns
        pystac.Item: pystac STAC item object.

    """
    if isinstance(item, dict):
        return pystac.Item.from_dict(item)

    return item


class Projection(TypedDict):
    """Projection info extracted from STAC Item."""

    width: int
    height: int
    bounds: tuple[float, float, float, float]
    transform: Affine
    crs: CRS


def _extract_proj_info(
    item: pystac.Item, assets: list[str] | None = None
) -> Projection | None:
    """Extract projection info from STAC Item.

    Args:
        item (pystac.Item): STAC Item.
        assets (list[str]): An optional list of assets to use instead of the item's proj value.

    Returns:
        Projection: projection info extracted from the STAC Item.

    """
    if not item.ext.has("proj"):
        return None

    crs = item.ext.proj.crs_string

    # Asset level projection extension
    assets = assets or list(item.assets)
    asset_proj: dict[str, Any] = {}

    for asset in assets:
        asset_info = item.assets[asset]
        if asset_info.ext.has("proj"):
            if all(
                [
                    asset_info.ext.proj.transform,
                    asset_info.ext.proj.shape,
                ]
            ):
                tr = Affine(*asset_info.ext.proj.transform)
                asset_proj[asset] = {
                    "shape": asset_info.ext.proj.shape,
                    "transform": tr,
                    "bounds": array_bounds(
                        asset_info.ext.proj.shape[0],
                        asset_info.ext.proj.shape[1],
                        tr,
                    ),
                    "crs_string": asset_info.ext.proj.crs_string or crs,
                }

    if asset_proj:
        # 1. check that all assets have the same projection info
        # if multiple CRS if will be too expensive to handle
        crss = [p["crs_string"] for p in asset_proj.values()]
        if crs:
            crss.append(crs)

        if len(set(crss)) == 1:
            crs = next(iter(crss))
            if not crs:
                return None

            # 2. create unified bounds, transform and shape for the item based on the assets info
            bounds = (
                min(p["bounds"][0] for p in asset_proj.values()),
                min(p["bounds"][1] for p in asset_proj.values()),
                max(p["bounds"][2] for p in asset_proj.values()),
                max(p["bounds"][3] for p in asset_proj.values()),
            )

            # 3. Get the highest resolution asset and use its transform to calculate
            # the theoritical shape of the item
            highest_res_asset = min(
                asset_proj.items(),
                key=lambda p: (
                    abs(p[1]["transform"][0]),  # pixel width
                    abs(p[1]["transform"][4]),  # pixel height
                ),
            )
            xres = highest_res_asset[1]["transform"][0]
            yres = highest_res_asset[1]["transform"][4]

            # 4. Get dataset shape from bounds and resolution
            height = abs(math.floor((bounds[3] - bounds[1]) / yres))
            width = abs(math.floor((bounds[2] - bounds[0]) / xres))

            transform = from_bounds(*bounds, width, height)

            return Projection(
                width=width,
                height=height,
                bounds=bounds,
                transform=transform,
                crs=CRS.from_string(crs),
            )

    # Item Level projection extension
    if all(
        [
            item.ext.proj.transform,
            item.ext.proj.shape,
            crs,
        ]
    ):
        height, width = item.ext.proj.shape
        transform = Affine(*item.ext.proj.transform)
        bounds = array_bounds(height, width, transform)

        return Projection(
            width=width,
            height=height,
            bounds=bounds,
            transform=transform,
            crs=CRS.from_string(crs),
        )

    return None


@attr.s
class STACReader(MultiBaseReader):
    """STAC Reader.

    Attributes:
        input (str): STAC Item path, URL or S3 URL.
        item (dict or pystac.Item, STAC): Stac Item.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set minzoom for the tiles.
        maxzoom (int, optional): Set maxzoom for the tiles.
        include_assets (set of string, optional): Only Include specific assets.
        exclude_assets (set of string, optional): Exclude specific assets.
        include_asset_types (set of string, optional): Only include some assets base on their type.
        exclude_asset_types (set of string, optional): Exclude some assets base on their type.
        default_assets (list of string or dict, optional): Default assets to use if none are defined.
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

    input: str | None = attr.ib()
    item: pystac.Item | None = attr.ib(default=None, converter=_to_pystac_item)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int | None = attr.ib(default=None)
    maxzoom: int | None = attr.ib(default=None)

    include_assets: set[str] | None = attr.ib(default=None)
    exclude_assets: set[str] | None = attr.ib(default=None)

    include_asset_types: set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: set[str] | None = attr.ib(default=None)

    assets: Sequence[str] = attr.ib(init=False)
    default_assets: Sequence[AssetType] | None = attr.ib(default=None)

    reader: type[BaseReader] = attr.ib(default=Reader)
    reader_options: dict = attr.ib(factory=dict)

    fetch_options: dict = attr.ib(factory=dict)

    ctx: type[rasterio.Env] = attr.ib(default=rasterio.Env)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.item = self.item or pystac.Item.from_dict(
            fetch(self.input, **self.fetch_options), self.input
        )
        self.assets = self.get_asset_list()
        if not self.assets:
            raise MissingAssets("No valid asset found. Asset's media types not supported")

        if proj := _extract_proj_info(self.item, assets=self.assets):
            self.height = proj["height"]
            self.width = proj["width"]
            self.bounds = proj["bounds"]
            self.transform = proj["transform"]
            self.crs = proj["crs"]
        else:
            self.bounds = (
                tuple(self.item.bbox)
                if self.item.bbox
                else featureBounds(self.item.geometry)
            )
            self.crs = WGS84_CRS

        self.minzoom = self.minzoom if self.minzoom is not None else self._minzoom
        self.maxzoom = self.maxzoom if self.maxzoom is not None else self._maxzoom

    def get_asset_list(self) -> list[str]:
        """Get valid asset list"""
        return list(
            _get_assets(
                self.item,
                include=self.include_assets,
                exclude=self.exclude_assets,
                include_asset_types=self.include_asset_types,
                exclude_asset_types=self.exclude_asset_types,
            )
        )

    def _get_options(
        self,
        asset: AssetWithOptions,
        metadata: pystac.Asset,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        method_options: dict[str, Any] = {}
        reader_options: dict[str, Any] = {}

        # Indexes
        if indexes := asset.get("indexes"):
            method_options["indexes"] = indexes
        # Expression
        if expr := asset.get("expression"):
            method_options["expression"] = expr
        # Bands
        if bands := asset.get("bands"):
            stac_bands = (
                metadata.extra_fields.get("bands")
                or metadata.extra_fields.get("eo:bands")  # V1.0
            )
            if not stac_bands:
                raise ValueError(
                    "Asset does not have 'bands' metadata, unable to use 'bands' option"
                )

            # There is no standard for precedence between 'eo:common_name' and 'name'
            # in STAC specification, so we will use 'eo:common_name' if it exists,
            # otherwise fallback to 'name', and if not exist use the band index as last resource.
            common_to_variable = {
                b.get("eo:common_name") or b.get("common_name") or b.get("name") or ix: ix
                for ix, b in enumerate(stac_bands, 1)
            }
            band_indexes: list[int] = []
            for b in bands:
                if idx := common_to_variable.get(b):
                    band_indexes.append(idx)
                else:
                    raise ValueError(
                        f"Band '{b}' not found in asset metadata, unable to use 'bands' option"
                    )

                method_options["indexes"] = band_indexes

        return reader_options, method_options

    def _get_asset_info(self, asset: AssetType) -> AssetInfo:  # noqa: C901
        """Validate asset names and return asset's info.

        Args:
            asset (AssetType): STAC asset name.

        Returns:
            AssetInfo: STAC asset info.

        """
        if isinstance(asset, str):
            asset = {"name": asset}

        if not asset.get("name"):
            raise ValueError("asset dictionary does not have `name` key")

        asset_name = asset["name"]
        if asset_name not in self.assets:
            raise InvalidAssetName(
                f"'{asset_name}' is not valid, should be one of {self.assets}"
            )

        asset_info = self.item.assets[asset_name]

        reader_options, method_options = self._get_options(asset, asset_info)

        info = AssetInfo(
            url=asset_info.get_absolute_href() or asset_info.href,
            name=asset_name,
            media_type=asset_info.media_type,
            reader_options=reader_options,
            method_options=method_options,
        )

        info["metadata"] = asset_info.extra_fields

        if STAC_ALTERNATE_KEY and asset_info.extra_fields.get("alternate"):
            if alternate := asset_info.extra_fields["alternate"].get(STAC_ALTERNATE_KEY):
                info["url"] = alternate["href"]

        # https://github.com/stac-extensions/file
        if head := asset_info.extra_fields.get("file:header_size"):
            info["env"] = {"GDAL_INGESTED_BYTES_AT_OPEN": head}

        # https://github.com/stac-extensions/raster
        if (
            stac_bands := (
                asset_info.extra_fields.get("bands")
                or asset_info.extra_fields.get("raster:bands")  # V1.0
            )
        ) and "expression" not in method_options:
            stats = [
                (float(b["statistics"]["minimum"]), float(b["statistics"]["maximum"]))
                for b in stac_bands
                if {"minimum", "maximum"}.issubset(b.get("statistics", {}))
            ]
            # check that stats data are all double and raise warning if not
            if (
                stats
                and all(isinstance(v, (int, float)) for stat in stats for v in stat)
                and len(stats) == len(stac_bands)
            ):
                info["dataset_statistics"] = stats
            else:
                warnings.warn(
                    "Some statistics data in STAC are invalid, they will be ignored.",
                    UserWarning,
                )

        return info
