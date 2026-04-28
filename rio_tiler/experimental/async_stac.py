"""rio_tiler.experimental.async_stac: STAC reader with async support."""

import warnings
from collections.abc import Sequence
from typing import Any

import attr
import pystac
from morecantile import TileMatrixSet
from rasterio.features import bounds as featureBounds

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidAssetName, MissingAssets
from rio_tiler.io.base import AsyncBaseReader, AsyncMultiBaseReader
from rio_tiler.io.stac import (
    DEFAULT_VALID_TYPE,
    STAC_ALTERNATE_KEY,
    _extract_proj_info,
    _get_assets,
    _to_pystac_item,
)
from rio_tiler.types import AssetInfo, AssetType, AssetWithOptions


@attr.s
class AsyncSTACReader(AsyncMultiBaseReader):
    """Async STAC Reader.

    Attributes:
        input (dict or pystac.Item, STAC): Stac Item.
        reader (rio_tiler.io.BaseReader): rio-tiler Reader.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        minzoom (int, optional): Set minzoom for the tiles.
        maxzoom (int, optional): Set maxzoom for the tiles.
        include_assets (set of string, optional): Only Include specific assets.
        exclude_assets (set of string, optional): Exclude specific assets.
        include_asset_types (set of string, optional): Only include some assets base on their type.
        exclude_asset_types (set of string, optional): Exclude some assets base on their type.
        default_assets (list of string or dict, optional): Default assets to use if none are defined.
        reader_options (dict, optional): Additional option to forward to the Reader. Defaults to `{}`.

    Examples:
        >>> from obstore.store import from_url

            # Custom Async Reader using obstore+async-geotiff
            @asynccontextmanager
            async def reader(url: str, *args:  **kwargs: Any):
                parsed = urlparse(url)

                directory = posixpath.dirname(parsed.path)
                store_url = f"{parsed.scheme}://{parsed.netloc}{directory}"
                store = from_url(store_url)

                filename = posixpath.basename(parsed.path)
                geotiff = await GeoTIFF.open(filename, store=store, prefetch=prefetch)
                async with GeoTIFFReader(geotiff, *args, **kwargs) as src:
                    yield src

            async with AsyncSTACReader(input=item, reader=reader) as stac:
                await stac.tile(...)

    """

    input: pystac.Item = attr.ib(converter=_to_pystac_item)
    reader: type[AsyncBaseReader] = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int | None = attr.ib(default=None)
    maxzoom: int | None = attr.ib(default=None)

    include_assets: set[str] | None = attr.ib(default=None)
    exclude_assets: set[str] | None = attr.ib(default=None)

    include_asset_types: set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types: set[str] | None = attr.ib(default=None)

    default_assets: Sequence[AssetType] | None = attr.ib(default=None)

    reader_options: dict = attr.ib(factory=dict)

    item: Any = attr.ib(init=False)
    assets: Sequence[str] = attr.ib(init=False)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.item = self.input
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
        # Variables
        if vars := asset.get("variables"):
            method_options["variables"] = vars
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

            # For Zarr bands = variable
            media_type = (
                metadata.media_type.split(";")[0].strip() if metadata.media_type else ""
            )
            zarr_media_types = [
                "application/x-zarr",
                "application/vnd.zarr",
                "application/vnd+zarr",
            ]
            if media_type in zarr_media_types:
                common_to_variable = {
                    b.get("eo:common_name") or b.get("common_name") or b["name"]: b[
                        "name"
                    ]
                    for b in stac_bands
                }
                method_options["variables"] = [
                    common_to_variable.get(v, v) for v in bands
                ]

            # For COG bands = indexes
            else:
                # There is no standard for precedence between 'eo:common_name' and 'name'
                # in STAC specification, so we will use 'eo:common_name' if it exists,
                # otherwise fallback to 'name', and if not exist use the band index as last resource.
                common_to_variable = {
                    b.get("eo:common_name")
                    or b.get("common_name")
                    or b.get("name")
                    or str(ix): ix
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
