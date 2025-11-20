"""rio_tiler.mosaic.backend: base Backend class."""

import abc
import logging
from typing import Any, Type

import attr
from morecantile import TileMatrixSet
from pydantic import BaseModel, Field
from rasterio.crs import CRS
from rasterio.features import bounds as featureBounds
from rasterio.features import geometry_mask

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import NoAssetFoundError, PointOutsideBounds
from rio_tiler.io import BaseReader, MultiBandReader, MultiBaseReader, Reader
from rio_tiler.models import ImageData, PointData
from rio_tiler.mosaic import mosaic_reader
from rio_tiler.tasks import multi_values
from rio_tiler.types import BBox
from rio_tiler.utils import CRS_to_uri, Timer, _validate_shape_input

logger = logging.getLogger(__name__)


class MosaicInfo(BaseModel):
    """Mosaic info responses."""

    bounds: BBox = Field(default=(-180, -90, 180, 90))
    crs: str


@attr.s
class BaseBackend(BaseReader):
    """Base Class for mosaic backend.

    Attributes:
        input (str): mosaic path.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        reader (rio_tiler.io.BaseReader): Dataset reader. Defaults to `rio_tiler.io.Reader`.
        reader_options (dict): Options to forward to the reader config.
        bounds (tuple): mosaic bounds (left, bottom, right, top). **READ ONLY attribute**.
        crs (rasterio.crs.CRS): mosaic crs in which its bounds is defined. **READ ONLY attribute**.
        minzoom (int): mosaic minimum zoom level. **READ ONLY attribute**.
        maxzoom (int): mosaic maximum zoom level. **READ ONLY attribute**.

    """

    input: str = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: Type[BaseReader] | Type[MultiBaseReader] | Type[MultiBandReader] = attr.ib(
        default=Reader
    )
    reader_options: dict = attr.ib(factory=dict)

    bounds: BBox = attr.ib(init=False)
    crs: CRS = attr.ib(init=False)

    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    @abc.abstractmethod
    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> list[str]:
        """Retrieve assets for tile."""

    @abc.abstractmethod
    def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS | None = None,
        **kwargs: Any,
    ) -> list[str]:
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
    ) -> list[str]:
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
    ) -> list[PointData]:
        """Get Point value from multiple assets."""
        search_options = search_options or {}
        mosaic_assets = self.assets_for_point(
            lon, lat, coord_crs=coord_crs, **search_options
        )
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for point ({lon},{lat})")

        def _reader(
            asset: str, lon: float, lat: float, coord_crs: CRS, **kwargs
        ) -> PointData:
            with self.reader(asset, **self.reader_options) as src_dst:
                return src_dst.point(lon, lat, coord_crs=coord_crs, **kwargs)

        if "allowed_exceptions" not in kwargs:
            kwargs.update({"allowed_exceptions": (PointOutsideBounds,)})

        logger.info(
            f"reading Point for {len(mosaic_assets)} assets with reader: {self.reader}"
        )
        return list(
            multi_values(mosaic_assets, _reader, lon, lat, coord_crs, **kwargs).values()
        )

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

        def _reader(asset: str, x: int, y: int, z: int, **kwargs: Any) -> ImageData:
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

        def _reader(asset: str, bbox: BBox, bounds_crs: CRS, **kwargs: Any) -> ImageData:
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
        search_options: dict | None = None,
        **kwargs: Any,
    ) -> tuple[ImageData, list[str]]:
        """Create an Image from multiple assets for a GeoJSON feature."""
        shape = _validate_shape_input(shape)
        bbox = featureBounds(shape)

        img, asset_used = self.part(
            bbox,
            bounds_crs=shape_crs,
            search_options=search_options,
            **kwargs,
        )
        img.array.mask = geometry_mask([shape], (img.height, img.width), img.transform)
        return img, asset_used

    ############################################################################
    # Not Implemented methods
    # BaseReader required those method to be implemented
    def statistics(self):
        """PlaceHolder for statistics."""
        raise NotImplementedError

    def preview(self):
        """PlaceHolder for preview."""
        raise NotImplementedError
