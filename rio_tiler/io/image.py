"""Image Reader."""

import contextlib
import math
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

import attr
import morecantile
import numpy
import rasterio
from morecantile.utils import _parse_tile_arg
from rasterio import windows
from rasterio.crs import CRS
from rasterio.enums import ColorInterp, Resampling
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.overview import get_maximum_overview_level

from ..errors import (
    AlphaBandWarning,
    ExpressionMixingWarning,
    IncorrectTileBuffer,
    NoOverviewWarning,
)
from ..expression import apply_expression, parse_expression
from ..models import BandStatistics, ImageData, Info
from ..types import BBox, DataMaskType, Indexes, NumType
from ..utils import (
    get_array_statistics,
    get_bands_names,
    has_alpha_band,
    has_mask_band,
    non_alpha_indexes,
)
from .base import BaseReader


def imread(
    src_dst: Union[DatasetReader, DatasetWriter],
    height: Optional[int] = None,
    width: Optional[int] = None,
    indexes: Optional[Indexes] = None,
    window: Optional[windows.Window] = None,
    force_binary_mask: bool = True,
    unscale: bool = False,
    resampling_method: Resampling = "nearest",
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
    ] = None,
    nodata=None,
) -> DataMaskType:
    """Low level read function.

    Like rio_tiler.reader.read but without WarpedVRT

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    if indexes is None:
        indexes = non_alpha_indexes(src_dst)
        if indexes != src_dst.indexes:
            warnings.warn(
                "Alpha band was removed from the output data array", AlphaBandWarning
            )

    out_shape = (len(indexes), height, width) if height and width else None
    mask_out_shape = (height, width) if height and width else None
    resampling = Resampling[resampling_method]

    if ColorInterp.alpha in src_dst.colorinterp:
        idx = src_dst.colorinterp.index(ColorInterp.alpha) + 1
        indexes = tuple(indexes) + (idx,)
        if out_shape:
            out_shape = (len(indexes), height, width)

        data = src_dst.read(
            indexes=indexes,
            window=window,
            out_shape=out_shape,
            resampling=resampling,
            boundless=True,
        )
        data, mask = data[0:-1], data[-1].astype("uint8")
    else:
        data = src_dst.read(
            indexes=indexes,
            window=window,
            out_shape=out_shape,
            resampling=resampling,
            boundless=True,
        )
        mask = src_dst.dataset_mask(
            window=window,
            out_shape=mask_out_shape,
            resampling=resampling,
            boundless=True,
        )

    if force_binary_mask:
        mask = numpy.where(mask != 0, numpy.uint8(255), numpy.uint8(0))

    if unscale:
        data = data.astype("float32", casting="unsafe")
        numpy.multiply(data, src_dst.scales[0], out=data, casting="unsafe")
        numpy.add(data, src_dst.offsets[0], out=data, casting="unsafe")

    if post_process:
        data, mask = post_process(data, mask)

    return data, mask


@attr.s
class TileMatrixSet:
    """TMS For local image."""

    width: int = attr.ib()
    height: int = attr.ib()
    tile_size: int = attr.ib(default=256)

    def _ul(self, *tile: morecantile.Tile) -> morecantile.Coords:
        """Return the upper left coordinate of the (x, y, z) tile."""
        t = _parse_tile_arg(*tile)

        res = max(
            self.width / self.tile_size / 2.0 ** t.z,
            self.height / self.tile_size / 2.0 ** t.z,
        )

        xcoord = self.tile_size * t.x * res
        ycoord = self.tile_size * t.y * res

        return morecantile.Coords(xcoord, ycoord)

    def xy_bounds(self, *tile: morecantile.Tile) -> morecantile.BoundingBox:
        """Return the bounding box of the (x, y, z) tile"""
        t = _parse_tile_arg(*tile)
        left, bottom = self._ul(t)
        right, top = self._ul(morecantile.Tile(t.x + 1, t.y + 1, t.z))
        return morecantile.BoundingBox(left, bottom, right, top)


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

    # Define global options to be forwarded to functions reading the data (e.g `rio_tiler.reader.read`)
    unscale: Optional[bool] = attr.ib(default=None)
    resampling_method: Optional[Resampling] = attr.ib(default=None)
    post_process: Optional[
        Callable[[numpy.ndarray, numpy.ndarray], DataMaskType]
    ] = attr.ib(default=None)

    # We use _kwargs to store values of nodata, unscale, vrt_options and resampling_method.
    # _kwargs is used avoid having to set those values on each method call.
    _kwargs: Dict[str, Any] = attr.ib(init=False, factory=dict)

    # Context Manager to handle rasterio open/close
    _ctx_stack = attr.ib(init=False, factory=contextlib.ExitStack)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        if self.unscale is not None:
            self._kwargs["unscale"] = self.unscale

        if self.resampling_method is not None:
            self._kwargs["resampling_method"] = self.resampling_method

        if self.post_process is not None:
            self._kwargs["post_process"] = self.post_process

        self.dataset = self.dataset or self._ctx_stack.enter_context(
            rasterio.open(self.input)
        )

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

        self.tms = TileMatrixSet(width=self.dataset.width, height=self.dataset.height)

        if self.colormap is None:
            try:
                self.colormap = self.dataset.colormap(1)
            except ValueError:
                self.colormap = {}
                pass

        if min(
            self.dataset.width, self.dataset.height
        ) > 512 and not self.dataset.overviews(1):
            warnings.warn(
                "The dataset has no Overviews. rio-tiler performances might be impacted.",
                NoOverviewWarning,
            )

    def close(self):
        """Close rasterio dataset."""
        self._ctx_stack.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    def info(self) -> Info:
        """Return COG info."""

        def _get_descr(ix):
            """Return band description."""
            return self.dataset.descriptions[ix - 1] or ""

        if has_alpha_band(self.dataset):
            nodata_type = "Alpha"
        elif has_mask_band(self.dataset):
            nodata_type = "Mask"
        elif self.nodata is not None:
            nodata_type = "Nodata"
        else:
            nodata_type = "None"

        meta = {
            "bounds": self.bounds,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
            "band_metadata": [
                (f"{ix}", self.dataset.tags(ix)) for ix in self.dataset.indexes
            ],
            "band_descriptions": [
                (f"{ix}", _get_descr(ix)) for ix in self.dataset.indexes
            ],
            "dtype": self.dataset.meta["dtype"],
            "colorinterp": [
                self.dataset.colorinterp[ix - 1].name for ix in self.dataset.indexes
            ],
            "nodata_type": nodata_type,
            # additional info (not in default model)
            "driver": self.dataset.driver,
            "count": self.dataset.count,
            "width": self.dataset.width,
            "height": self.dataset.height,
            "overviews": self.dataset.overviews(1),
        }
        if self.dataset.scales[0] and self.dataset.offsets[0]:
            meta.update(
                {"scale": self.dataset.scales[0], "offset": self.dataset.offsets[0]}
            )

        if self.colormap:
            meta.update({"colormap": self.colormap})

        if nodata_type == "Nodata":
            meta.update({"nodata_value": self.nodata})

        return Info(**meta)

    def statistics(
        self,
        categorical: bool = False,
        categories: Optional[List[float]] = None,
        percentiles: List[int] = [2, 98],
        hist_options: Optional[Dict] = None,
        max_size: int = 1024,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return bands statistics from a dataset.

        Args:
            categorical (bool): treat input data as categorical data. Defaults to False.
            categories (list of numbers, optional): list of categories to return value for.
            percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
            hist_options (dict, optional): Options to forward to numpy.histogram function.
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            kwargs (optional): Options to forward to `self.preview`.

        Returns:
            Dict[str, rio_tiler.models.BandStatistics]: bands statistics.

        """
        kwargs = {**self._kwargs, **kwargs}

        data = self.preview(max_size=max_size, **kwargs)

        hist_options = hist_options or {}

        stats = get_array_statistics(
            data.as_masked(),
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            **hist_options,
        )

        return {
            f"{data.band_names[ix]}": BandStatistics(**stats[ix])
            for ix in range(len(stats))
        }

    def tile(
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int = 256,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        tile_buffer: Optional[NumType] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read a tile from an Image.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output image size. Defaults to `256`.
            indexes (int or sequence of int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            tile_buffer (int or float, optional): Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * tile_buffer` (e.g 0.5 = 257x257, 1.0 = 258x258).
            kwargs (optional): Options to forward to the `COGReader.part` method.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and tile spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        tile_bounds = self.tms.xy_bounds(morecantile.Tile(x=tile_x, y=tile_y, z=tile_z))
        if tile_buffer is not None:
            if tile_buffer % 0.5:
                raise IncorrectTileBuffer(
                    "`tile_buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."
                )

            x_res = (tile_bounds.right - tile_bounds.left) / tilesize
            y_res = (tile_bounds.top - tile_bounds.bottom) / tilesize

            # Buffered Tile Bounds
            tile_bounds = morecantile.BoundingBox(
                tile_bounds.left - x_res * tile_buffer,
                tile_bounds.bottom - y_res * tile_buffer,
                tile_bounds.right + x_res * tile_buffer,
                tile_bounds.top + y_res * tile_buffer,
            )

            # Buffered Tile Size
            tilesize += int(tile_buffer * 2)

        return self.part(
            tile_bounds,
            height=tilesize,
            width=tilesize,
            max_size=None,
            indexes=indexes,
            expression=expression,
            **kwargs,
        )

    def part(
        self,
        bbox: BBox,
        indexes: Optional[Union[int, Sequence]] = None,
        expression: Optional[str] = None,
        max_size: int = None,
        height: int = None,
        width: int = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part."""
        kwargs = {**self._kwargs, **kwargs}

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        window = windows.Window(
            col_off=bbox[0],
            row_off=bbox[1],
            width=bbox[2] - bbox[0],
            height=bbox[3] - bbox[1],
        )

        if max_size and not (width and height):
            if max(window.height, window.width) > max_size:
                ratio = window.height / window.width
                if ratio > 1:
                    height = max_size
                    width = math.ceil(height / ratio)
                else:
                    width = max_size
                    height = math.ceil(width * ratio)

        data, mask = imread(
            self.dataset,
            window=window,
            height=height,
            width=width,
            indexes=indexes,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        return ImageData(
            data,
            mask,
            bounds=bbox,
            assets=[self.input],
            band_names=get_bands_names(
                indexes=indexes, expression=expression, count=data.shape[0]
            ),
        )

    def preview(
        self,
        indexes: Optional[Indexes] = None,
        expression: Optional[str] = None,
        max_size: int = 1024,
        height: Optional[int] = None,
        width: Optional[int] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Return a preview of an Image

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            expression (str, optional): rio-tiler expression (e.g. b1/b2+b3).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            kwargs (optional): Options to forward to the `rio_tiler.reader.preview` function.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        kwargs = {**self._kwargs, **kwargs}

        if isinstance(indexes, int):
            indexes = (indexes,)

        if indexes and expression:
            warnings.warn(
                "Both expression and indexes passed; expression will overwrite indexes parameter.",
                ExpressionMixingWarning,
            )

        if expression:
            indexes = parse_expression(expression)

        max_size = max_size or max(self.dataset.height, self.dataset.width)
        if max(self.dataset.height, self.dataset.width) < max_size:
            height, width = self.dataset.height, self.dataset.width
        else:
            ratio = self.dataset.height / self.dataset.width
            if ratio > 1:
                height = max_size
                width = math.ceil(height / ratio)
            else:
                width = max_size
                height = math.ceil(width * ratio)

        data, mask = imread(
            self.dataset,
            height=height,
            width=width,
            indexes=indexes,
            **kwargs,
        )

        if expression:
            blocks = expression.lower().split(",")
            bands = [f"b{bidx}" for bidx in indexes]
            data = apply_expression(blocks, bands, data)

        return ImageData(
            data,
            mask,
            bounds=self.bounds,
            assets=[self.input],
            band_names=get_bands_names(
                indexes=indexes, expression=expression, count=data.shape[0]
            ),
        )

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
