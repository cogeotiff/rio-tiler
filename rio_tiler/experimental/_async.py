"""rio_tiler.experimental.async_geotiff: rio-tiler Async reader built on top of async-geotiff."""

from __future__ import annotations

import abc
import math
import warnings
from typing import TYPE_CHECKING, Any, Literal, cast

import attr
from async_geotiff import Window
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.transform import from_bounds
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import (
    ExpressionMixingWarning,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.expression import parse_expression
from rio_tiler.io.base import SpatialMixin
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes, RIOResampling, WarpResampling
from rio_tiler.utils import _get_width_height, _missing_size, cast_to_sequence

if TYPE_CHECKING:
    from async_geotiff import GeoTIFF, Overview


@attr.s
class AsyncBaseReader(SpatialMixin, metaclass=abc.ABCMeta):
    """Rio-tiler.io AsyncBaseReader."""

    input: Any = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    @abc.abstractmethod
    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        ...

    @abc.abstractmethod
    async def statistics(self) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        ...

    @abc.abstractmethod
    async def tile(self, tile_x: int, tile_y: int, tile_z: int) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        ...

    @abc.abstractmethod
    async def part(self, bbox: BBox, **kwargs: Any) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def preview(self) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...

    @abc.abstractmethod
    async def point(self, lon: float, lat: float) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            list: Pixel value per bands/assets.

        """
        ...

    @abc.abstractmethod
    async def feature(self, shape: dict) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        ...


@attr.s
class Reader(AsyncBaseReader):
    """Rio-tiler.io AsyncBaseReader."""

    input: GeoTIFF = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    colormap: dict | None = attr.ib(default=None)

    async def __aenter__(self):
        """Support using with Context Managers."""
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        pass

    def __attrs_post_init__(self):
        """Post init."""
        self.bounds = self.input.bounds
        self.crs = CRS.from_user_input(self.input.crs)

        self.transform = self.input.transform
        self.height = self.input.height
        self.width = self.input.width

        if self.colormap is None and self.input.colormap is not None:
            self.colormap = self.input.colormap.as_rasterio()

    def _get_overview_level(
        self,
        target_res: float,
        zoom_level_strategy: Literal["AUTO", "LOWER", "UPPER"] = "AUTO",
    ) -> int:
        """Return the overview level corresponding to the resolution."""
        src_res = max(abs(self.input.transform.a), abs(self.input.transform.e))

        available_resolutions = [src_res] + [
            min(abs(ovr.transform.a), abs(ovr.transform.e))
            for ovr in self.input.overviews
        ]

        # Based on aiocogeo:
        # https://github.com/geospatial-jeff/aiocogeo/blob/5a1d32c3f22c883354804168a87abb0a2ea1c328/aiocogeo/partial_reads.py#L113-L147
        percentage = {"AUTO": 50, "LOWER": 100, "UPPER": 0}.get(zoom_level_strategy, 50)

        assert 0 <= percentage <= 100
        # Iterate over zoom levels from lowest/coarsest to highest/finest. If the `target_res` is more than `percentage`
        # percent of the way from the zoom level below to the zoom level above, then upsample the zoom level below, else
        # downsample the zoom level above.
        for i in reversed(range(1, len(available_resolutions))):
            res_current = available_resolutions[i]
            res_higher = available_resolutions[i - 1]
            threshold = res_current - (res_current - res_higher) * (percentage / 100.0)
            if target_res > threshold or target_res == res_current:
                return i

        return 0

    async def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tiler.models.Info: Dataset info.

        """
        raise NotImplementedError

    async def statistics(self) -> dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Returns:
            dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        raise NotImplementedError

    async def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int | None = None,
        indexes: Indexes | None = None,
        expression: str | None = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile(x={tile_x}, y={tile_y}, z={tile_z}) is outside bounds"
            )

        matrix = self.tms.matrix(tile_z)
        bbox = cast(
            BBox,
            self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z)),
        )

        return await self.part(
            bbox,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            max_size=None,
            indexes=indexes,
            expression=expression,
            **kwargs,
        )

    async def part(  # noqa: C901
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    async def preview(
        self,
        indexes: Indexes | None = None,
        expression: str | None = None,
        dst_crs: CRS | None = None,
        max_size: int = 1024,
        height: int | None = None,
        width: int | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width = self.input.width
        dst_height = self.input.height
        if dst_crs and dst_crs != self.crs:
            # Get shape of the dataset in the output CRS
            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, self.width, self.height, *self.bounds
            )

        if max_size:
            height, width = _get_width_height(max_size, dst_height, dst_width)

        elif _missing_size(width, height):
            ratio = dst_height / dst_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        # Shape in the output CRS
        height = height or dst_height
        width = width or dst_width

        # 2. determine overview level to read
        # Output dataset `transform` in the output CRS
        if dst_crs and dst_crs != self.crs:
            proj_bbox = transform_bounds(
                self.crs, dst_crs, *self.input.bounds, densify_pts=21
            )
            transform, _, _ = calculate_default_transform(
                dst_crs,
                self.crs,
                width,
                height,
                *proj_bbox,
            )
        else:
            transform = from_bounds(*self.input.bounds, width, height)

        # 3. Select Overview level
        target_res = min(abs(transform.a), abs(transform.e))
        dataset: GeoTIFF | Overview = self.input
        if level := self._get_overview_level(target_res):
            dataset = self.input.overviews[level - 1]

        # 4. Read data
        array = await dataset.read()

        indexes = indexes or list(range(1, self.input.count + 1))
        img = ImageData(
            array.as_masked()[[ix - 1 for ix in indexes]],
            crs=CRS.from_user_input(self.input.crs),
            bounds=self.input.bounds,
            band_descriptions=[f"b{ix}" for ix in indexes],
        )

        if expression:
            img = img.apply_expression(expression)

        # 5. Reproject if needed
        if dst_crs and dst_crs != self.crs:
            img = img.reproject(
                dst_crs=dst_crs,
                reproject_method=reproject_method,
            )

        # 6. Resize
        if width != img.width or height != img.height:
            img = img.resize(
                width=width,
                height=height,
                resampling_method=resampling_method,
            )

        return img

    async def point(
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        expression: str | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            expression: (str, optional): Expression to apply on the pixel values. Defaults to `None`.

        Returns:
            list: Pixel value per bands/assets.

        """
        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        indexes = cast_to_sequence(indexes)

        if coord_crs != self.crs:
            xs, ys = transform_coords(coord_crs, self.crs, [lon], [lat])
            lon, lat = xs[0], ys[0]

        dataset_min_lon, dataset_min_lat, dataset_max_lon, dataset_max_lat = self.bounds
        # check if latitude is inverted
        if dataset_min_lat > dataset_max_lat:
            warnings.warn(
                "BoundingBox of the dataset is inverted (minLat > maxLat).",
                UserWarning,
            )

        dataset_min_lat, dataset_max_lat = (
            min(dataset_min_lat, dataset_max_lat),
            max(dataset_min_lat, dataset_max_lat),
        )
        if not (
            (dataset_min_lon < lon < dataset_max_lon)
            and (dataset_min_lat < lat < dataset_max_lat)
        ):
            raise PointOutsideBounds("Point is outside dataset bounds")

        # TODO: handle interpolation
        row, col = self.input.index(lon, lat)
        row_off, col_off = row, col

        window = Window(row_off=row_off, col_off=col_off, width=1, height=1)

        array = await self.input.read(window=window)
        indexes = indexes or list(range(1, self.input.count + 1))

        pt = PointData(
            array.as_masked()[[ix - 1 for ix in indexes], 0, 0],
            coordinates=(lon, lat),
            crs=coord_crs,
            pixel_location=(row, col),
            band_descriptions=[f"b{ix}" for ix in indexes],
        )

        if expression:
            pt = pt.apply_expression(expression)

        return pt

    async def feature(self, shape: dict) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError
