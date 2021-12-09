"""Tiff Reader."""


import contextlib
import math
import warnings
from typing import Any, Dict, List, Union

import attr
import rasterio
from morecantile import TileMatrixSet
from morecantile.models import TileMatrix
from rasterio.crs import CRS
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.overview import get_maximum_overview_level

from ..errors import NoOverviewWarning
from ..models import BandStatistics, ImageData, Info
from ..types import BBox
from .base import BaseReader


@attr.s
class Reader(BaseReader):
    """Simple Image Reader.

    Attributes:
        input (str): Image path.
        dataset (rasterio.io.DatasetReader or rasterio.io.DatasetWriter, optional): Rasterio dataset.
        colormap (dict, optional): Overwrite internal colormap.

    Examples:
        >>> with Reader(src_path) as img:
            cog.tile(...)
            assert cog.dataset

        >>> with rasterio.open(src_path) as src_dst:
                with Reader(None, src_dataset=src_dst) as img:
                    cog.tile(...)

    """

    input: str = attr.ib()
    dataset: Union[DatasetReader, DatasetWriter, MemoryFile] = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(init=False)
    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    bounds: BBox = attr.ib(init=False)

    # not applicable
    crs: CRS = attr.ib(init=False, default=None)
    geographic_crs: CRS = attr.ib(init=False, default=None)

    colormap: Dict = attr.ib(default=None)

    # Context Manager to handle rasterio open/close
    _ctx_stack = attr.ib(init=False, factory=contextlib.ExitStack)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        self.dataset = self.dataset or rasterio.open(self.filepath)

        self.nodata = self.dataset.nodata

        self.bounds = (0, 0, self.dataset.width, self.dataset.height)

        self.minzoom = 0

        # Calculate the maximum overview level of a dataset at which
        # the smallest overview is smaller than `minsize`.
        # https://github.com/rasterio/rasterio/blob/master/rasterio/rio/overview.py#L33-L59
        self.maxzoom = get_maximum_overview_level(
            self.dataset.width,
            self.dataset.height,
            minsize=256,
        )

        # Fake TMS
        tms: Dict[str, Any] = {
            "title": "tms",
            "identifier": "cog",
            "supportedCRS": "+proj=set +units=m",
            "tileMatrix": [],
        }

        for zoom in range(self.minzoom, self.maxzoom + 1):
            res = max(
                self.dataset.width / 256 / 2.0 ** zoom,
                self.dataset.height / 256 / 2.0 ** zoom,
            )

            width = self.dataset.width / 256 * (2 ** zoom)
            height = self.dataset.height / 256 * (2 ** zoom)

            tms["tileMatrix"].append(
                TileMatrix(
                    **dict(
                        identifier=str(zoom),
                        scaleDenominator=res * 1 / 0.00028,
                        topLeftCorner=[0, self.dataset.height],
                        tileWidth=256,
                        tileHeight=256,
                        matrixWidth=math.ceil(width / 256),
                        matrixHeight=math.ceil(height / 256),
                    )
                )
            )

        self.tms = TileMatrixSet(**tms)

        if self.colormap is None:
            self._get_colormap()

        if min(
            self.dataset.width, self.dataset.height
        ) > 512 and not self.dataset.overviews(1):
            warnings.warn(
                "The dataset has no Overviews. rio-tiler performances might be impacted.",
                NoOverviewWarning,
            )

    def info(self) -> Info:
        """Return Dataset's info.

        Returns:
            rio_tile.models.Info: Dataset info.

        """
        raise NotImplementedError

    def statistics(self, **kwargs: Any) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        raise NotImplementedError

    def tile(self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any) -> ImageData:
        """Read a Map tile from the Dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        raise NotImplementedError

    def part(self, bbox: BBox, **kwargs: Any) -> ImageData:
        """Read a Part of a Dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    def preview(self, **kwargs: Any) -> ImageData:
        """Read a preview of a Dataset.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError

    def point(self, lon: float, lat: float, **kwargs: Any) -> List:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.

        Returns:
            list: Pixel value per bands/assets.

        """
        raise NotImplementedError

    def feature(self, shape: Dict, **kwargs: Any) -> ImageData:
        """Read a Dataset for a GeoJSON feature.

        Args:
            shape (dict): Valid GeoJSON feature.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        raise NotImplementedError
