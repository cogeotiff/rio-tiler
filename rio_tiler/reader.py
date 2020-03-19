"""rio-tiler.reader: image utility functions."""

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

import math
import warnings
from concurrent import futures

import numpy

from affine import Affine

import mercantile

import rasterio
from rasterio.io import DatasetReader, DatasetWriter
from rasterio.crs import CRS
from rasterio.vrt import WarpedVRT
from rasterio.warp import transform_bounds, transform
from rasterio.enums import Resampling, ColorInterp
from rasterio.windows import Window

from rio_tiler import constants
from rio_tiler.utils import (
    get_vrt_transform,
    has_alpha_band,
    has_mask_band,
    non_alpha_indexes,
    _stats as raster_stats,
    _requested_tile_aligned_with_internal_tile as is_aligned,
    tile_exists,
)
from rio_tiler.errors import TileOutsideBounds, AlphaBandWarning


def _read(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    height: int,
    width: int,
    indexes: Optional[Union[Sequence[int], int]] = None,
    out_window: Optional[Window] = None,
    nodata: Optional[Union[float, int, str]] = None,
    resampling_method: Resampling = "bilinear",
    force_binary_mask: bool = True,
    unscale: bool = False,
    vrt_options: Dict = {},
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Create WarpedVRT and read data and mask.

    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        height : int
            Output height of the array.
        width : int
            Output width of the array.
        indexes : list of ints or a single int, optional
            Band indexes
        out_window: rasterio.windows.Window, optional
            Output window to read.
        nodata: int or float, optional
        resampling_method : str, optional
            Resampling algorithm. Default is "bilinear".
        force_binary_mask, bool, optional
            If True, rio-tiler makes sure mask has only 0 or 255 values.
            Default is set to True.
        unscale, bool, optional
            If True, apply scale and offset to the data array.
            Default is set to False.
        vrt_options: dict, optional
            These will be passed to the rasterio.warp.WarpedVRT class.

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    vrt_params = dict(add_alpha=True, resampling=Resampling[resampling_method])
    nodata = nodata if nodata is not None else src_dst.nodata
    if nodata is not None:
        vrt_params.update(dict(nodata=nodata, add_alpha=False, src_nodata=nodata))

    if has_alpha_band(src_dst):
        vrt_params.update(dict(add_alpha=False))

    if indexes is None:
        indexes = non_alpha_indexes(src_dst)
        if indexes != src_dst.indexes:
            warnings.warn(
                "Alpha band was removed from the output data array", AlphaBandWarning
            )

    vrt_params.update(vrt_options)
    with WarpedVRT(src_dst, **vrt_params) as vrt:
        data = vrt.read(
            out_shape=(len(indexes), height, width),
            indexes=indexes,
            window=out_window,
            resampling=Resampling[resampling_method],
        )
        if ColorInterp.alpha in vrt.colorinterp:
            idx = vrt.colorinterp.index(ColorInterp.alpha) + 1
            mask = vrt.read(
                indexes=idx,
                out_shape=(height, width),
                window=out_window,
                resampling=Resampling[resampling_method],
                out_dtype="uint8",
            )
        else:
            mask = vrt.dataset_mask(
                out_shape=(height, width),
                window=out_window,
                resampling=Resampling[resampling_method],
            )

        if force_binary_mask:
            mask = numpy.where(mask != 0, numpy.uint8(255), numpy.uint8(0))

        if unscale:
            data = data.astype("float32", casting="unsafe")
            numpy.multiply(data, vrt.scales[0], out=data, casting="unsafe")
            numpy.add(data, vrt.offsets[0], out=data, casting="unsafe")

    return data, mask


def part(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: Tuple[float, float, float, float],
    height: int,
    width: int,
    padding: int = 0,
    dst_crs: CRS = constants.WEB_MERCATOR_CRS,
    bounds_crs: Optional[CRS] = None,
    minimum_overlap: Optional[float] = None,
    warp_vrt_option: Dict = {},
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Read part of an image.

    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        bounds : tuple
            Output bounds (left, bottom, right, top) in target crs ("dst_crs").
        height : int
            Output height of the array.
        width : int
            Output width of the array.
        padding : int, optional
            Padding to apply to each edge of the tile when retrieving data
            to assist in reducing resampling artefacts along edges.
        dst_crs: CRS or str, optional
            Target coordinate reference system, default is "epsg:3857".
        bounds_crs: CRS or str, optional
            Overwrite bounds coordinate reference system, default is equal
            to the output CRS (dst_crs).
        minimum_tile_cover: float, optional
            Minimum % overlap for which to raise an error with dataset not
            covering enought of the tile.
        warp_vrt_option: dict, optional
            These will be passed to the rasterio.warp.WarpedVRT class.
        kwargs : Any, optional
            Additional options to forward to reader._read()

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    if not bounds_crs:
        bounds_crs = dst_crs

    bounds = transform_bounds(bounds_crs, dst_crs, *bounds, densify_pts=21)

    src_bounds = transform_bounds(src_dst.crs, dst_crs, *src_dst.bounds, densify_pts=21)
    x_overlap = max(0, min(src_bounds[2], bounds[2]) - max(src_bounds[0], bounds[0]))
    y_overlap = max(0, min(src_bounds[3], bounds[3]) - max(src_bounds[1], bounds[1]))
    cover_ratio = (x_overlap * y_overlap) / (
        (bounds[2] - bounds[0]) * (bounds[3] - bounds[1])
    )
    if minimum_overlap and cover_ratio < minimum_overlap:
        raise TileOutsideBounds(
            "Dataset covers less than {:.0f}% of tile".format(cover_ratio * 100)
        )

    vrt_transform, vrt_width, vrt_height = get_vrt_transform(
        src_dst, bounds, dst_crs=dst_crs
    )

    out_window = Window(col_off=0, row_off=0, width=vrt_width, height=vrt_height)

    if padding > 0 and not is_aligned(src_dst, bounds, height, width):
        vrt_transform = vrt_transform * Affine.translation(-padding, -padding)
        orig_vrt_height = vrt_height
        orig_vrt_width = vrt_width
        vrt_height = vrt_height + 2 * padding
        vrt_width = vrt_width + 2 * padding
        out_window = Window(
            col_off=padding,
            row_off=padding,
            width=orig_vrt_width,
            height=orig_vrt_height,
        )

    return _read(
        src_dst,
        height,
        width,
        out_window=out_window,
        vrt_options=dict(
            crs=dst_crs,
            transform=vrt_transform,
            width=vrt_width,
            height=vrt_height,
            **warp_vrt_option,
        ),
        **kwargs,
    )


def preview(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    max_size: int = 1024,
    height: int = None,
    width: int = None,
    **kwargs: Any,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Read image and resample to low resolution.


    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        max_size : int
            `max_size` of the longest dimension, respecting
            bounds X/Y aspect ratio.
        height: int, optional
            output height of the data
        width: int, optional
            output width of the data
        kwargs : Any, optional
            Additional options to forward to reader._read()

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    if not height and not width:
        if max(src_dst.height, src_dst.width) < max_size:
            height, width = src_dst.height, src_dst.width
        else:
            ratio = src_dst.height / src_dst.width
            if ratio > 1:
                height = max_size
                width = math.ceil(height / ratio)
            else:
                width = max_size
                height = math.ceil(width * ratio)

    return _read(src_dst, height, width, **kwargs)


def point(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    coordinates: Tuple[float, float],
    indexes: Optional[Union[Sequence[int], int]] = None,
    coord_crs: CRS = constants.WGS84_CRS,
    unscale: bool = False,
) -> List:
    """
    Read point value

    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        coordinates : tuple
            (X, Y) coordinates.
        indexes : list of ints or a single int, optional
            Band indexes
        coord_crs : rasterio.crs.CRS, optional
            (X, Y) coordinate system. Default is WGS84/EPSG:4326.
        unscale, bool, optional
            If True, apply scale and offset to the data.
            Default is set to False.
        kwargs : Any, optional
            Additional options to forward to src_dst.sample()

    Returns
    -------
        point : list
            List of pixel values per bands indexes.

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    lon, lat = transform(coord_crs, src_dst.crs, [coordinates[0]], [coordinates[1]])
    if not (
        (src_dst.bounds[0] < lon[0] < src_dst.bounds[2])
        and (src_dst.bounds[1] < lat[0] < src_dst.bounds[3])
    ):
        raise Exception("Point is outside dataset bounds")

    indexes = indexes if indexes is not None else src_dst.indexes

    point_values = list(src_dst.sample([(lon[0], lat[0])], indexes=indexes))[0]

    if unscale:
        point_values = point_values.astype("float32", casting="unsafe")
        numpy.multiply(
            point_values, src_dst.scales[0], out=point_values, casting="unsafe"
        )
        numpy.add(point_values, src_dst.offsets[0], out=point_values, casting="unsafe")

    return point_values.tolist()


def metadata(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: Optional[Tuple[float, float, float, float]] = None,
    indexes: Optional[Union[Sequence[int], int]] = None,
    max_size: int = 1024,
    bounds_crs: CRS = constants.WGS84_CRS,
    percentiles: Tuple[float, float] = (2.0, 98.0),
    hist_options: Dict = {},
    **kwargs: Any,
) -> Dict:
    """
    Retrieve statistics from multiple sentinel bands.

    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        bounds : tuple, optional
            Bounding box coordinates from which to calculate image statistics.
        max_size : int
            `max_size` of the longest dimension, respecting
            bounds X/Y aspect ratio.
        indexes : list of ints or a single int, optional
            Band indexes.
        bounds_crs: CRS or str, optional
            Specify bounds coordinate reference system, default WGS84/EPSG4326.
        percentiles: tuple, optional
            Tuple of Min/Max percentiles to compute. Default is (2, 98).
        hist_options : dict, optional
            Options to forward to numpy.histogram function.
        kwargs : Any, optional
            Additional options to forward to part or preview

    Returns
    -------
        dict

    """
    if isinstance(indexes, int):
        indexes = (indexes,)

    if indexes is None:
        indexes = non_alpha_indexes(src_dst)
        if indexes != src_dst.indexes:
            warnings.warn(
                "Alpha band was removed from the output data array", AlphaBandWarning
            )

    if bounds:
        asp_ratio = abs((bounds[2] - bounds[0]) / (bounds[1] - bounds[3]))
        if asp_ratio > 1:
            width = max_size
            height = math.ceil(max_size / asp_ratio)
        else:
            width = math.ceil(max_size * asp_ratio)
            height = max_size

        data, mask = part(
            src_dst,
            bounds,
            height,
            width,
            indexes=indexes,
            dst_crs=src_dst.crs,
            bounds_crs=bounds_crs,
            **kwargs,
        )
        bounds = transform_bounds(
            bounds_crs, constants.WGS84_CRS, *bounds, densify_pts=21
        )

    else:
        data, mask = preview(src_dst, max_size=max_size, indexes=indexes, **kwargs)
        bounds = transform_bounds(
            src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
        )

    data = numpy.ma.array(data)
    data.mask = mask == 0

    def _get_descr(ix):
        """Return band description."""
        name = src_dst.descriptions[ix - 1]
        if not name:
            name = "band{}".format(ix)
        return name

    band_descriptions = [(ix, _get_descr(ix)) for ix in indexes]

    statistics = {
        indexes[b]: raster_stats(data[b], percentiles=percentiles, **hist_options)
        for b in range(data.shape[0])
    }

    other_meta = dict()
    if src_dst.scales[0] and src_dst.offsets[0]:
        other_meta.update(dict(scale=src_dst.scales[0]))
        other_meta.update(dict(offset=src_dst.offsets[0]))

    if has_alpha_band(src_dst):
        nodata_type = "Alpha"
    elif has_mask_band(src_dst):
        nodata_type = "Mask"
    elif src_dst.nodata is not None:
        nodata_type = "Nodata"
    else:
        nodata_type = "None"

    try:
        cmap = src_dst.colormap(1)
        other_meta.update(dict(colormap=cmap))
    except ValueError:
        pass

    return dict(
        bounds=bounds,
        statistics=statistics,
        band_descriptions=band_descriptions,
        dtype=src_dst.meta["dtype"],
        colorinterp=[src_dst.colorinterp[ix - 1].name for ix in indexes],
        nodata_type=nodata_type,
        **other_meta,
    )


def tile(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    x: int,
    y: int,
    z: int,
    tilesize: int = 256,
    **kwargs,
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Read mercator tile from an image.

    Attributes
    ----------
        src_dst : rasterio.io.DatasetReader
            rasterio.io.DatasetReader object
        x : int
            Mercator tile X index.
        y : int
            Mercator tile Y index.
        z : int
            Mercator tile ZOOM level.
        tilesize : int, optional
            Output tile size. Default is 256.
        kwargs : Any, optional
            Additional options to forward to part()

    Returns
    -------
        data : numpy ndarray
        mask: numpy array

    """
    bounds = transform_bounds(
        src_dst.crs, constants.WGS84_CRS, *src_dst.bounds, densify_pts=21
    )
    if not tile_exists(bounds, z, x, y):
        raise TileOutsideBounds(f"Tile {z}/{x}/{y} is outside image bounds")

    tile_bounds = mercantile.xy_bounds(mercantile.Tile(x=x, y=y, z=z))
    return part(src_dst, tile_bounds, tilesize, tilesize, **kwargs)


def multi_tile(
    assets: Sequence[str], *args: Any, **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Assemble multiple rio_tiler.reader.tile."""

    def worker(asset: str):
        with rasterio.open(asset) as src_dst:
            return tile(src_dst, *args, **kwargs)

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(worker, assets)))
        data = numpy.concatenate(data)
        mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255
        return data, mask


def multi_preview(
    assets: Sequence[str], *args: Any, **kwargs: Any
) -> Tuple[numpy.ndarray, numpy.ndarray]:
    """Assemble multiple rio_tiler.reader.preview."""

    def worker(asset: str):
        with rasterio.open(asset) as src_dst:
            return preview(src_dst, *args, **kwargs)

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        data, masks = zip(*list(executor.map(worker, assets)))
        data = numpy.concatenate(data)
        mask = numpy.all(masks, axis=0).astype(numpy.uint8) * 255
        return data, mask


def multi_point(assets: Sequence[str], *args: Any, **kwargs: Any) -> Sequence:
    """Assemble multiple rio_tiler.reader.point."""

    def worker(asset: str):
        with rasterio.open(asset) as src_dst:
            return point(src_dst, *args, **kwargs)

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        return list(executor.map(worker, assets))


def multi_metadata(assets: Sequence[str], *args: Any, **kwargs: Any) -> Sequence:
    """Assemble multiple rio_tiler.reader.metadata."""

    def worker(asset: str):
        with rasterio.open(asset) as src_dst:
            return metadata(src_dst, *args, **kwargs)

    with futures.ThreadPoolExecutor(max_workers=constants.MAX_THREADS) as executor:
        return list(executor.map(worker, assets))
