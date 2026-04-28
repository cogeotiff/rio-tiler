"""rio_tiler.mosaic.backend: base Backend class."""

import abc
import logging
import warnings
from typing import Any

import attr
import numpy
from morecantile import TileMatrixSet
from pydantic import BaseModel, ConfigDict, Field
from rasterio.crs import CRS
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import bounds as featureBounds
from rasterio.features import rasterize
from rasterio.warp import transform_geom

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import NoAssetFoundError, PointOutsideBounds
from rio_tiler.io import (
    AsyncBaseReader,
    AsyncMultiBaseReader,
    BaseReader,
    MultiBaseReader,
    Reader,
)
from rio_tiler.models import BandStatistics, ImageData, PointData
from rio_tiler.mosaic.reader import async_mosaic_reader, mosaic_reader
from rio_tiler.tasks import async_multi_values_list, multi_values_list
from rio_tiler.types import BBox
from rio_tiler.utils import (
    CRS_to_uri,
    Timer,
    _validate_shape_input,
    inherit_rasterio_env,
)

logger = logging.getLogger(__name__)


class MosaicInfo(BaseModel):
    """Mosaic info responses."""

    bounds: BBox = Field(default=(-180, -90, 180, 90))
    crs: str

    model_config = ConfigDict(extra="allow")


@attr.s
class BaseBackend(BaseReader):
    """Base Class for mosaic backend.

    Attributes:
        input (Any): mosaic.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        reader (rio_tiler.io.BaseReader): Dataset reader. Defaults to `rio_tiler.io.Reader`.
        reader_options (dict): Options to forward to the reader config.
        bounds (tuple): mosaic bounds (left, bottom, right, top). **READ ONLY attribute**.
        crs (rasterio.crs.CRS): mosaic crs in which its bounds is defined. **READ ONLY attribute**.
        minzoom (int): mosaic minimum zoom level. **READ ONLY attribute**.
        maxzoom (int): mosaic maximum zoom level. **READ ONLY attribute**.

    """

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: type[BaseReader] | type[MultiBaseReader] = attr.ib(default=Reader)
    reader_options: dict = attr.ib(factory=dict)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    @abc.abstractmethod
    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> list[Any]:
        """Retrieve assets for tile."""

    @abc.abstractmethod
    def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS | None = None,
        **kwargs: Any,
    ) -> list[Any]:
        """Retrieve assets for point."""

    @abc.abstractmethod
    def assets_for_bbox(
        self,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        coord_crs: CRS | None = None,
        **kwargs,
    ) -> list[Any]:
        """Retrieve assets for bbox."""

    def asset_name(self, asset: Any) -> str:
        """Get asset name."""
        return str(asset)

    def info(self) -> MosaicInfo:  # type: ignore
        """Mosaic info."""
        return MosaicInfo(
            bounds=self.bounds,
            crs=CRS_to_uri(self.crs) or self.crs.to_wkt(),
        )

    def point(  # type: ignore
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> list[tuple[str, PointData]]:
        """Get Point value from multiple assets."""
        search_options = search_options or {}
        mosaic_assets = self.assets_for_point(
            lon, lat, coord_crs=coord_crs, **search_options
        )
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        @inherit_rasterio_env
        def _reader(
            asset: Any, lon: float, lat: float, coord_crs: CRS, **kwargs
        ) -> PointData:
            with self.reader(asset, **self.reader_options) as src_dst:
                return src_dst.point(lon, lat, coord_crs=coord_crs, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        logger.info(
            f"reading Point for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        return [
            (self.asset_name(asset), pt)
            for asset, pt in multi_values_list(
                mosaic_assets, _reader, lon, lat, coord_crs, **kwargs
            )
        ]

    def tile(  # type: ignore
        self,
        x: int,
        y: int,
        z: int,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Get Tile from multiple assets."""
        timings = []
        with Timer() as t:
            search_options = search_options or {}
            mosaic_assets = self.assets_for_tile(x, y, z, **search_options)
        timings.append(("search", round(t.elapsed * 1000, 2)))

        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for tile {z}-{x}-{y}")

        @inherit_rasterio_env
        def _reader(asset: Any, x: int, y: int, z: int, **kwargs: Any) -> ImageData:
            with self.reader(asset, tms=self.tms, **self.reader_options) as src_dst:
                return src_dst.tile(x, y, z, **kwargs)

        logger.info(
            f"reading Tile for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        with Timer() as t:
            img, asset_used = mosaic_reader(mosaic_assets, _reader, x, y, z, **kwargs)
        timings.append(("mosaicking", round(t.elapsed * 1000, 2)))
        img.metadata = {**img.metadata, "timings": timings}

        asset_used = [self.asset_name(asset) for asset in asset_used]
        return img, asset_used

    def part(  # type: ignore
        self,
        bbox: BBox,
        bounds_crs: CRS = WGS84_CRS,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Create an Image from multiple assets for a bbox."""
        xmin, ymin, xmax, ymax = bbox
        timings = []

        with Timer() as t:
            search_options = search_options or {}
            mosaic_assets = self.assets_for_bbox(
                xmin,
                ymin,
                xmax,
                ymax,
                coord_crs=bounds_crs,
                **search_options,
            )
        timings.append(("search", round(t.elapsed * 1000, 2)))

        if not mosaic_assets:
            raise NoAssetFoundError("No assets found for bbox input")

        @inherit_rasterio_env
        def _reader(asset: Any, bbox: BBox, bounds_crs: CRS, **kwargs: Any) -> ImageData:
            with self.reader(asset, **self.reader_options) as src_dst:
                return src_dst.part(bbox, bounds_crs=bounds_crs, **kwargs)

        logger.info(
            f"reading Part for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        with Timer() as t:
            img, asset_used = mosaic_reader(
                mosaic_assets, _reader, bbox, bounds_crs, **kwargs
            )
        timings.append(("mosaicking", round(t.elapsed * 1000, 2)))
        img.metadata = {**img.metadata, "timings": timings}

        asset_used = [self.asset_name(asset) for asset in asset_used]
        return img, asset_used

    def feature(  # type: ignore
        self,
        shape: dict,
        shape_crs: CRS = WGS84_CRS,
        dst_crs: CRS | None = None,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Create an Image from multiple assets for a GeoJSON feature."""
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        bbox = featureBounds(shape)

        img, asset_used = self.part(
            bbox,
            bounds_crs=shape_crs,
            dst_crs=dst_crs,
            search_options=search_options,
            **kwargs,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            cutline_mask = rasterize(
                [shape],
                out_shape=(img.height, img.width),
                transform=img.transform,
                all_touched=True,  # Mandatory for matching masks at different resolutions
                default_value=0,
                fill=1,
                dtype="uint8",
            ).astype("bool")

        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img, asset_used

    ############################################################################
    # Not Implemented methods
    # BaseReader required those method to be implemented
    def statistics(
        self,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """PlaceHolder for statistics."""
        raise NotImplementedError

    def preview(  # type: ignore
        self,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """PlaceHolder for preview."""
        raise NotImplementedError


@attr.s
class AsyncBaseBackend(AsyncBaseReader):
    """Base Class for mosaic backend.

    Attributes:
        input (Any): mosaic path.
        reader (rio_tiler.io.AsyncBaseReader or rio_tiler.io.AsyncMultiBaseReader): Dataset reader.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        reader_options (dict): Options to forward to the reader config.
        bounds (tuple): mosaic bounds (left, bottom, right, top). **READ ONLY attribute**.
        crs (rasterio.crs.CRS): mosaic crs in which its bounds is defined. **READ ONLY attribute**.
        minzoom (int): mosaic minimum zoom level. **READ ONLY attribute**.
        maxzoom (int): mosaic maximum zoom level. **READ ONLY attribute**.

    """

    input: Any = attr.ib()
    reader: type[AsyncBaseReader] | type[AsyncMultiBaseReader] = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader_options: dict = attr.ib(factory=dict)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    @abc.abstractmethod
    async def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> list[Any]:
        """Retrieve assets for tile."""

    @abc.abstractmethod
    async def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS | None = None,
        **kwargs: Any,
    ) -> list[Any]:
        """Retrieve assets for point."""

    @abc.abstractmethod
    async def assets_for_bbox(
        self,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        coord_crs: CRS | None = None,
        **kwargs,
    ) -> list[Any]:
        """Retrieve assets for bbox."""

    def asset_name(self, asset: Any) -> str:
        """Get asset name."""
        return str(asset)

    async def info(self) -> MosaicInfo:  # type: ignore
        """Mosaic info."""
        return MosaicInfo(
            bounds=self.bounds,
            crs=CRS_to_uri(self.crs) or self.crs.to_wkt(),
        )

    async def point(  # type: ignore
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> list[tuple[str, PointData]]:
        """Get Point value from multiple assets."""
        search_options = search_options or {}
        mosaic_assets = await self.assets_for_point(
            lon, lat, coord_crs=coord_crs, **search_options
        )
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        async def _reader(
            asset: Any, lon: float, lat: float, coord_crs: CRS, **kwargs
        ) -> PointData:
            async with self.reader(asset, **self.reader_options) as src_dst:
                return await src_dst.point(lon, lat, coord_crs=coord_crs, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        logger.info(
            f"reading Point for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        return [
            (self.asset_name(asset), pt)
            for asset, pt in await async_multi_values_list(
                mosaic_assets, _reader, lon, lat, coord_crs, **kwargs
            )
        ]

    async def tile(  # type: ignore
        self,
        x: int,
        y: int,
        z: int,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Get Tile from multiple assets."""
        timings = []
        with Timer() as t:
            search_options = search_options or {}
            mosaic_assets = await self.assets_for_tile(x, y, z, **search_options)
        timings.append(("search", round(t.elapsed * 1000, 2)))

        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for tile {z}-{x}-{y}")

        async def _reader(asset: Any, x: int, y: int, z: int, **kwargs: Any) -> ImageData:
            async with self.reader(asset, tms=self.tms, **self.reader_options) as src_dst:
                return await src_dst.tile(x, y, z, **kwargs)

        logger.info(
            f"reading Tile for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        with Timer() as t:
            img, asset_used = await async_mosaic_reader(
                mosaic_assets, _reader, x, y, z, **kwargs
            )
        timings.append(("mosaicking", round(t.elapsed * 1000, 2)))
        img.metadata = {**img.metadata, "timings": timings}

        asset_used = [self.asset_name(asset) for asset in asset_used]
        return img, asset_used

    async def part(  # type: ignore
        self,
        bbox: BBox,
        bounds_crs: CRS = WGS84_CRS,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Create an Image from multiple assets for a bbox."""
        xmin, ymin, xmax, ymax = bbox
        timings = []

        with Timer() as t:
            search_options = search_options or {}
            mosaic_assets = await self.assets_for_bbox(
                xmin,
                ymin,
                xmax,
                ymax,
                coord_crs=bounds_crs,
                **search_options,
            )
        timings.append(("search", round(t.elapsed * 1000, 2)))

        if not mosaic_assets:
            raise NoAssetFoundError("No assets found for bbox input")

        async def _reader(
            asset: Any, bbox: BBox, bounds_crs: CRS, **kwargs: Any
        ) -> ImageData:
            async with self.reader(asset, **self.reader_options) as src_dst:
                return await src_dst.part(bbox, bounds_crs=bounds_crs, **kwargs)

        logger.info(
            f"reading Part for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        with Timer() as t:
            img, asset_used = await async_mosaic_reader(
                mosaic_assets, _reader, bbox, bounds_crs, **kwargs
            )
        timings.append(("mosaicking", round(t.elapsed * 1000, 2)))
        img.metadata = {**img.metadata, "timings": timings}

        asset_used = [self.asset_name(asset) for asset in asset_used]
        return img, asset_used

    async def feature(  # type: ignore
        self,
        shape: dict,
        shape_crs: CRS = WGS84_CRS,
        dst_crs: CRS | None = None,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Create an Image from multiple assets for a GeoJSON feature."""
        shape = _validate_shape_input(shape)

        if not dst_crs:
            dst_crs = shape_crs

        bbox = featureBounds(shape)

        img, asset_used = await self.part(
            bbox,
            bounds_crs=shape_crs,
            dst_crs=dst_crs,
            search_options=search_options,
            **kwargs,
        )

        if dst_crs != shape_crs:
            shape = transform_geom(shape_crs, dst_crs, shape)

        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            cutline_mask = rasterize(
                [shape],
                out_shape=(img.height, img.width),
                transform=img.transform,
                all_touched=True,  # Mandatory for matching masks at different resolutions
                default_value=0,
                fill=1,
                dtype="uint8",
            ).astype("bool")

        img.array.mask = numpy.where(~cutline_mask, img.array.mask, True)

        return img, asset_used

    ############################################################################
    # Not Implemented methods
    # BaseReader required those method to be implemented
    async def statistics(
        self,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """PlaceHolder for statistics."""
        raise NotImplementedError

    async def preview(  # type: ignore
        self,
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """PlaceHolder for preview."""
        raise NotImplementedError
