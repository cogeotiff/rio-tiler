"""rio_tiler.utils: utility functions."""

import math
import warnings
from io import BytesIO
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import numpy
import rasterio
from affine import Affine
from numpy.typing import NDArray
from rasterio import windows
from rasterio.crs import CRS
from rasterio.dtypes import _gdal_typename
from rasterio.enums import ColorInterp, MaskFlags, Resampling
from rasterio.errors import NotGeoreferencedWarning
from rasterio.features import is_valid_geom
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.helpers import coords
from rasterio.transform import from_bounds, rowcol
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform, transform_geom

from rio_tiler.colormap import apply_cmap
from rio_tiler.constants import WEB_MERCATOR_CRS, WGS84_CRS
from rio_tiler.errors import InvalidFormat, RioTilerError
from rio_tiler.types import BBox, ColorMapType, IntervalTuple, RIOResampling


def _chunks(my_list: Sequence, chuck_size: int) -> Generator[Sequence, None, None]:
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(my_list), chuck_size):
        yield my_list[i : i + chuck_size]


# Ref: https://stackoverflow.com/posts/73905572
def _weighted_quantiles(
    values: NDArray[numpy.floating],
    weights: NDArray[numpy.floating],
    quantiles: float = 0.5,
) -> float:
    i = numpy.argsort(values)
    c = numpy.cumsum(weights[i])
    return float(values[i[numpy.searchsorted(c, numpy.array(quantiles) * c[-1])]])


# Ref: https://stackoverflow.com/questions/2413522
def _weighted_stdev(
    values: NDArray[numpy.floating],
    weights: NDArray[numpy.floating],
) -> float:
    average = numpy.average(values, weights=weights)
    variance = numpy.average((values - average) ** 2, weights=weights)
    return float(math.sqrt(variance))


def get_array_statistics(
    data: numpy.ma.MaskedArray,
    categorical: bool = False,
    categories: Optional[List[float]] = None,
    percentiles: Optional[List[int]] = None,
    coverage: Optional[NDArray[numpy.floating]] = None,
    **kwargs: Any,
) -> List[Dict[Any, Any]]:
    """Calculate per band array statistics.

    Args:
        data (numpy.ma.MaskedArray): input masked array data to get the statistics from.
        categorical (bool): treat input data as categorical data. Defaults to `False`.
        categories (list of numbers, optional): list of categories to return value for.
        percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
        coverage (numpy.array, optional): Data coverage fraction.
        kwargs (optional): options to forward to `numpy.histogram` function (only applies for non-categorical data).

    Returns:
        list: list of array statistics (dict)

    Examples:
        >>> data = numpy.ma.zeros((1, 256, 256))
        >>> get_array_statistics(data)
        [
            {
                'min': 0.0,
                'max': 0.0,
                'mean': 0.0,
                'count': 65536.0,
                'sum': 0.0,
                'std': 0.0,
                'median': 0.0,
                'majority': 0.0,
                'minority': 0.0,
                'unique': 1.0,
                'percentile_2': 0.0,
                'percentile_98': 0.0,
                'histogram': [
                    [0, 0, 0, 0, 0, 65536, 0, 0, 0, 0],
                    [-0.5, -0.4, -0.3, -0.19999999999999996, -0.09999999999999998, 0.0, 0.10000000000000009, 0.20000000000000007, 0.30000000000000004, 0.4, 0.5]
                ],
                'valid_pixels': 65536.0,
                'masked_pixels': 0.0,
                'valid_percent': 100.0
            }
        ]

    """
    percentiles = percentiles or [2, 98]

    if len(data.shape) < 3:
        data = numpy.ma.expand_dims(data, axis=0)

    output: List[Dict[Any, Any]] = []
    percentiles_names = [f"percentile_{int(p)}" for p in percentiles]

    if coverage is not None:
        assert (
            coverage.shape
            == (
                data.shape[1],
                data.shape[2],
            )
        ), f"Invalid shape ({coverage.shape}) for Coverage, expected {(data.shape[1], data.shape[2])}"

    else:
        coverage = numpy.ones((data.shape[1], data.shape[2]))

    # Avoid non masked nan/inf values
    numpy.ma.fix_invalid(data, copy=False)

    for b in range(data.shape[0]):
        data_comp = data[b].compressed()

        keys, counts = numpy.unique(data_comp, return_counts=True)

        valid_pixels = float(numpy.ma.count(data[b]))
        masked_pixels = float(numpy.ma.count_masked(data[b]))
        valid_percent = round((valid_pixels / data[b].size) * 100, 2)

        if categorical:
            out_dict = dict(zip(keys.tolist(), counts.tolist()))
            h_keys = (
                numpy.array(categories).astype(keys.dtype) if categories else keys
            ).tolist()
            histogram = [
                [out_dict.get(x, 0) for x in h_keys],
                h_keys,
            ]
        else:
            h_counts, h_keys = numpy.histogram(data_comp, **kwargs)
            histogram = [h_counts.tolist(), h_keys.tolist()]

        # Data coverage fractions
        data_cov = data[b] * coverage
        # Coverage Array + data mask
        masked_coverage = numpy.ma.MaskedArray(coverage, mask=data_cov.mask)

        if valid_pixels:
            # TODO: when switching to numpy~=2.0
            # percentiles_values = numpy.percentile(
            #     data_comp, percentiles, weights=coverage.flatten()
            # ).tolist()
            percentiles_values = [
                _weighted_quantiles(data_comp, masked_coverage.compressed(), pp / 100.0)
                for pp in percentiles
            ]
        else:
            percentiles_values = [numpy.nan] * len(percentiles_names)

        if valid_pixels:
            majority = float(keys[counts.tolist().index(counts.max())].tolist())
            minority = float(keys[counts.tolist().index(counts.min())].tolist())
        else:
            majority = numpy.nan
            minority = numpy.nan

        _count = masked_coverage.sum()
        _sum = data_cov.sum()

        output.append(
            {
                # Minimum value, not taking coverage fractions into account.
                "min": float(data[b].min()),
                # Maximum value, not taking coverage fractions into account.
                "max": float(data[b].max()),
                # Mean value, weighted by the percent of each cell that is covered.
                "mean": float(_sum / _count),
                # Sum of all non-masked cell coverage fractions.
                "count": float(_count),
                # Sum of values, weighted by their coverage fractions.
                "sum": float(_sum),
                # Population standard deviation of cell values, taking into account coverage fraction.
                "std": _weighted_stdev(data_comp, masked_coverage.compressed()),
                # Median value of cells, weighted by the percent of each cell that is covered.
                "median": _weighted_quantiles(data_comp, masked_coverage.compressed()),
                # The value occupying the greatest number of cells.
                "majority": majority,
                # The value occupying the least number of cells.
                "minority": minority,
                # Unique values.
                "unique": float(counts.size),
                # quantiles
                **dict(zip(percentiles_names, percentiles_values)),
                "histogram": histogram,
                # Number of non-masked cells, not taking coverage fractions into account.
                "valid_pixels": valid_pixels,
                # Number of masked cells, not taking coverage fractions into account.
                "masked_pixels": masked_pixels,
                # Percent of valid cells
                "valid_percent": valid_percent,
            }
        )

    return output


# https://github.com/OSGeo/gdal/blob/b1c9c12ad373e40b955162b45d704070d4ebf7b0/gdal/frmts/ingr/IngrTypes.cpp#L191
def _div_round_up(a: int, b: int) -> int:
    return (a // b) if (a % b) == 0 else (a // b) + 1


def _round_window(window: windows.Window) -> windows.Window:
    (row_start, row_stop), (col_start, col_stop) = window.toranges()
    row_start, row_stop = int(math.floor(row_start)), int(math.ceil(row_stop))
    col_start, col_stop = int(math.floor(col_start)), int(math.ceil(col_stop))
    return windows.Window(
        col_off=col_start,
        row_off=row_start,
        width=max(col_stop - col_start, 0.0),
        height=max(row_stop - row_start, 0.0),
    )


def get_overview_level(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: BBox,
    height: int,
    width: int,
    dst_crs: CRS = WEB_MERCATOR_CRS,
) -> int:
    """Return the overview level corresponding to the tile resolution.

    Freely adapted from https://github.com/OSGeo/gdal/blob/41993f127e6e1669fbd9e944744b7c9b2bd6c400/gdal/apps/gdalwarp_lib.cpp#L2293-L2362

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        bounds (tuple): Bounding box coordinates in target crs (**dst_crs**).
        height (int): Desired output height of the array for the input bounds.
        width (int): Desired output width of the array for the input bounds.
        dst_crs (rasterio.crs.CRS, optional): Target Coordinate Reference System. Defaults to `epsg:3857`.

    Returns:
        int: Overview level.

    """
    dst_transform, _, _ = calculate_default_transform(
        src_dst.crs, dst_crs, src_dst.width, src_dst.height, *src_dst.bounds
    )
    src_res = dst_transform.a

    # Compute what the "natural" output resolution
    # (in pixels) would be for this input dataset
    vrt_transform = from_bounds(*bounds, width, height)
    target_res = vrt_transform.a

    ovr_idx = -1
    if target_res > src_res:
        res = [src_res * decim for decim in src_dst.overviews(1)]

        for idx in range(ovr_idx, len(res) - 1):
            ovr_idx = idx
            ovrRes = src_res if ovr_idx < 0 else res[ovr_idx]
            nextRes = res[ovr_idx + 1]

            if (ovrRes < target_res) and (nextRes > target_res):
                break

            if abs(ovrRes - target_res) < 1e-1:
                break

        else:
            ovr_idx = len(res) - 1

    return ovr_idx


def get_vrt_transform(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: BBox,
    height: Optional[int] = None,
    width: Optional[int] = None,
    dst_crs: CRS = WEB_MERCATOR_CRS,
    window_precision: int = 6,
    align_bounds_with_dataset: bool = False,
) -> Tuple[Affine, int, int]:
    """Calculate VRT transform.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        bounds (tuple): Bounding box coordinates in target crs (**dst_crs**).
        height (int, optional): Output height of the array for the input bounds.
        width (int, optional): Output width of the array for the input bounds.
        dst_crs (rasterio.crs.CRS, optional): Target Coordinate Reference System. Defaults to `epsg:3857`.
        align_bounds_with_dataset (bool): Align input bounds with dataset transform. Defaults to `False`.

    Returns:
        tuple: VRT transform (affine.Affine), width (int) and height (int)

    """
    # 1. Get the Dataset Resolution in the output crs
    if src_dst.crs != dst_crs:
        src_width = src_dst.width
        src_height = src_dst.height
        src_bounds = list(src_dst.bounds)

        # Fix for https://github.com/cogeotiff/rio-tiler/issues/654
        #
        # When using `calculate_default_transform` with dataset
        # which span at high/low latitude outside the area_of_use
        # of the WebMercator projection, we `crop` the dataset
        # to get the transform (resolution).
        #
        # Note: Should be handled in gdal 3.8 directly
        # https://github.com/OSGeo/gdal/pull/8775
        if (
            src_dst.crs == WGS84_CRS
            and dst_crs == WEB_MERCATOR_CRS
            and (src_bounds[1] < -85.06 or src_bounds[3] > 85.06)
        ):
            warnings.warn(
                "Adjusting dataset latitudes to avoid re-projection overflow",
                UserWarning,
            )
            src_bounds[1] = max(src_bounds[1], -85.06)
            src_bounds[3] = min(src_bounds[3], 85.06)
            w = windows.from_bounds(*src_bounds, transform=src_dst.transform)
            src_height = round(w.height)
            src_width = round(w.width)

        # Specific FIX when bounds and transform are inverted
        # See: https://github.com/US-GHG-Center/veda-config-ghg/pull/333
        elif (
            src_dst.crs == WGS84_CRS
            and dst_crs == WEB_MERCATOR_CRS
            and (src_bounds[1] > 85.06 or src_bounds[3] < -85.06)
        ):
            warnings.warn(
                "Adjusting dataset latitudes to avoid re-projection overflow",
                UserWarning,
            )
            src_bounds[1] = min(src_bounds[1], 85.06)
            src_bounds[3] = max(src_bounds[3], -85.06)
            w = windows.from_bounds(*src_bounds, transform=src_dst.transform)
            src_height = round(w.height)
            src_width = round(w.width)

        dst_transform, _, _ = calculate_default_transform(
            src_dst.crs, dst_crs, src_width, src_height, *src_bounds
        )

    else:
        dst_transform = src_dst.transform

    # 2. adjust output bounds if needed
    # If bounds window is aligned with the dataset internal tile we align the bounds with the pixels.
    # This is to limit the number of internal block fetched.
    if _requested_tile_aligned_with_internal_tile(src_dst, bounds, bounds_crs=dst_crs):
        # Get Window for the input bounds
        # e.g Window(col_off=17920.0, row_off=11007.999999999998, width=255.99999999999636, height=256.0000000000018)
        col_off, row_off, w, h = windows.from_bounds(
            *bounds, transform=dst_transform
        ).flatten()

        # Round Window
        w = windows.Window(
            round(col_off, window_precision),
            round(row_off, window_precision),
            round(w, window_precision),
            round(h, window_precision),
        )

        # Get Bounds for the rounded window
        bounds = src_dst.window_bounds(w)

    elif align_bounds_with_dataset:
        window = _round_window(windows.from_bounds(*bounds, transform=dst_transform))
        bounds = windows.bounds(window, dst_transform)

    w, s, e, n = bounds

    # 3. Calculate the VRT Height/Width
    # When no output size (resolution) - Use Dataset Resolution
    # NOTE: When we don't `fix` the output width/height, we're using the reprojected dataset resolution
    # to calculate what is the size/transform of the VRT
    w_res = dst_transform.a
    h_res = dst_transform.e

    # NOTE: When we have desired output height/width, we can use them to
    # calculate the output size/transform. The VRT resolution will be aligned with the desired
    # output resolution (if not bigger)
    if height and width:
        output_transform = from_bounds(w, s, e, n, width, height)

        # NOTE: Here we check if the Output Resolution is higher thant the dataset resolution (OverZoom)
        # When not over-zooming we don't want to use the output Width/Height to calculate the transform
        # See issues https://github.com/cogeotiff/rio-tiler/pull/648
        if abs(dst_transform.a) > abs(output_transform.a):
            w_res = output_transform.a

        if abs(dst_transform.e) > abs(output_transform.e):
            h_res = output_transform.e

    vrt_width = max(1, round((e - w) / w_res))
    vrt_height = max(1, round((s - n) / h_res))
    vrt_transform = from_bounds(w, s, e, n, vrt_width, vrt_height)
    return vrt_transform, vrt_width, vrt_height


def has_alpha_band(src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT]) -> bool:
    """Check for alpha band or mask in source."""
    if (
        any(MaskFlags.alpha in flags for flags in src_dst.mask_flag_enums)
        or ColorInterp.alpha in src_dst.colorinterp
    ):
        return True
    return False


def has_mask_band(src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT]) -> bool:
    """Check for mask band in source."""
    if any(
        (MaskFlags.per_dataset in flags and MaskFlags.alpha not in flags)
        for flags in src_dst.mask_flag_enums
    ):
        return True
    return False


def non_alpha_indexes(src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT]) -> Tuple:
    """Return indexes of non-alpha bands."""
    return tuple(
        b
        for ix, b in enumerate(src_dst.indexes)
        if (
            src_dst.mask_flag_enums[ix] is not MaskFlags.alpha
            and src_dst.colorinterp[ix] is not ColorInterp.alpha
        )
    )


def linear_rescale(
    image: numpy.ndarray,
    in_range: IntervalTuple,
    out_range: IntervalTuple = (0, 255),
) -> numpy.ndarray:
    """Apply linear rescaling to a numpy array.

    Args:
        image (numpy.ndarray): array to rescale.
        in_range (tuple): array min/max value to rescale from.
        out_range (tuple, optional): output min/max bounds to rescale to. Defaults to `(0, 255)`.

    Returns:
        numpy.ndarray: linear rescaled array.

    """
    imin, imax = in_range
    omin, omax = out_range
    im = numpy.clip(image, imin, imax) - imin
    im = im / numpy.float64(imax - imin)
    return im * (omax - omin) + omin


def _requested_tile_aligned_with_internal_tile(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: BBox,
    bounds_crs: CRS = WEB_MERCATOR_CRS,
) -> bool:
    """Check if tile is aligned with internal tiles."""
    if src_dst.block_shapes and src_dst.block_shapes[0][1] == src_dst.width:
        return False

    if src_dst.crs != bounds_crs:
        return False

    col_off, row_off, w, h = windows.from_bounds(
        *bounds, transform=src_dst.transform
    ).flatten()

    if round(w) % 64 and round(h) % 64:
        return False

    if (src_dst.width - round(col_off)) % 64:
        return False

    if (src_dst.height - round(row_off)) % 64:
        return False

    return True


def render(
    data: numpy.ndarray,
    mask: Optional[numpy.ndarray] = None,
    img_format: str = "PNG",
    colormap: Optional[ColorMapType] = None,
    **creation_options: Any,
) -> bytes:
    """Translate numpy.ndarray to image bytes.

    Args:
        data (numpy.ndarray): Image array to encode.
        mask (numpy.ndarray, optional): Mask array.
        img_format (str, optional): Image format. See: for the list of supported format by GDAL: https://www.gdal.org/formats_list.html. Defaults to `PNG`.
        colormap (dict or sequence, optional): RGBA Color Table dictionary or sequence.
        creation_options (optional): Image driver creation options to forward to GDAL.

    Returns
        bytes: image body.

    Examples:
        >>> with Reader("my_tif.tif") as src:
            img = src.preview()
            with open('test.jpg', 'wb') as f:
                f.write(render(img.data, img.mask, img_format="jpeg"))


    """
    img_format = img_format.upper()

    if len(data.shape) < 3:
        data = numpy.expand_dims(data, axis=0)

    if colormap:
        data, alpha = apply_cmap(data, colormap)
        # We take both the input mask and the alpha from the colormap
        # if input mask is not provided then we assume output is wanted without alpha band
        # this can be seen as a bug but at the time of writing we assume it's a feature.
        if mask is not None:
            mask = numpy.bitwise_and(alpha, mask)

    # WEBP doesn't support 1band dataset so we must hack to create a RGB dataset
    if img_format == "WEBP" and data.shape[0] == 1:
        data = numpy.repeat(data, 3, axis=0)

    if img_format == "PNG" and data.dtype == "uint16" and mask is not None:
        # By rio-tiler design, mask should always be between 0 and 255
        mask = linear_rescale(mask, (0, 255), (0, 65535)).astype("uint16")

    elif img_format == "JPEG":
        mask = None

    elif img_format == "NPY":
        # If mask is not None we add it as the last band
        if mask is not None:
            m = numpy.expand_dims(mask, axis=0)
            data = numpy.concatenate((data, m))

        with BytesIO() as bio:
            numpy.save(bio, data)
            return bio.getvalue()

    elif img_format == "NPZ":
        with BytesIO() as bio:
            if mask is not None:
                numpy.savez_compressed(bio, data=data, mask=mask)
            else:
                numpy.savez_compressed(bio, data=data)

            return bio.getvalue()

    count, height, width = data.shape

    output_profile = {
        "driver": img_format,
        "dtype": data.dtype,
        "count": count + 1 if mask is not None else count,
        "height": height,
        "width": width,
    }
    output_profile.update(creation_options)

    try:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=NotGeoreferencedWarning,
                module="rasterio",
            )
            with MemoryFile() as memfile:
                with memfile.open(**output_profile) as dst:
                    dst.write(data, indexes=list(range(1, count + 1)))

                    # Use Mask as an alpha band
                    if mask is not None:
                        if ColorInterp.alpha not in dst.colorinterp:
                            dst.colorinterp = *dst.colorinterp[:-1], ColorInterp.alpha

                        dst.write(mask.astype(data.dtype), indexes=count + 1)

                return memfile.read()

    except Exception as e:
        raise InvalidFormat(
            f"Could not encode array of shape ({count},{height},{width}) and of datatype `{data.dtype}` using {img_format} driver"
        ) from e


def mapzen_elevation_rgb(data: numpy.ndarray) -> numpy.ndarray:
    """Encode elevation value to RGB values compatible with Mapzen tangram.

    Args:
        data (numpy.ndarray): Image array to encode.

    Returns
        numpy.ndarray: Elevation encoded in a RGB array.

    """
    data = numpy.clip(data + 32768.0, 0.0, 65535.0)
    r = data / 256
    g = data % 256
    b = (data * 256) % 256
    return numpy.stack([r, g, b]).astype(numpy.uint8)


def pansharpening_brovey(
    rgb: numpy.ndarray, pan: numpy.ndarray, weight: float, pan_dtype: str
) -> numpy.ndarray:
    """Apply Brovey pansharpening method.

    Brovey Method: Each resampled, multispectral pixel is
    multiplied by the ratio of the corresponding
    panchromatic pixel intensity to the sum of all the
    multispectral intensities.

    Original code from https://github.com/mapbox/rio-pansharpen

    """

    def _calculateRatio(
        rgb: numpy.ndarray, pan: numpy.ndarray, weight: float
    ) -> numpy.ndarray:
        return pan / ((rgb[0] + rgb[1] + rgb[2] * weight) / (2 + weight))

    with numpy.errstate(invalid="ignore", divide="ignore"):
        ratio = _calculateRatio(rgb, pan, weight)
        return numpy.clip(ratio * rgb, 0, numpy.iinfo(pan_dtype).max).astype(pan_dtype)


def _convert_to_raster_space(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    poly_coordinates: List,
    op: Optional[Callable[[float], Any]] = None,
) -> List[str]:
    # NOTE: we could remove this once we have rasterio >= 1.4.2
    op = op or numpy.floor
    polygons = []
    for point in poly_coordinates:
        xs, ys = zip(*coords(point))
        src_y, src_x = rowcol(src_dst.transform, xs, ys, op=op)
        polygon = ", ".join([f"{int(x)} {int(y)}" for x, y in list(zip(src_x, src_y))])
        polygons.append(f"({polygon})")

    return polygons


def create_cutline(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    geometry: Dict,
    geometry_crs: CRS = None,
    op: Optional[Callable[[float], Any]] = None,
) -> str:
    """
    Create WKT Polygon Cutline for GDALWarpOptions.

    Ref: https://gdal.org/api/gdalwarp_cpp.html?highlight=vrt#_CPPv415GDALWarpOptions

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        geometry (dict): GeoJSON feature or GeoJSON geometry. By default the coordinates are considered to be in the dataset CRS. Use `geometry_crs` to set a specific CRS.
        geometry_crs (rasterio.crs.CRS, optional): Input geometry Coordinate Reference System
    Returns:
        str: WKT geometry in form of `POLYGON ((x y, x y, ...)))

    """
    geometry = _validate_shape_input(geometry)
    geom_type = geometry["type"]

    if geometry_crs:
        geometry = transform_geom(geometry_crs, src_dst.crs, geometry)

    if geom_type == "Polygon":
        polys = ",".join(_convert_to_raster_space(src_dst, geometry["coordinates"], op))
        wkt = f"POLYGON ({polys})"

    elif geom_type == "MultiPolygon":
        multi_polys = []
        for poly in geometry["coordinates"]:
            polys = ",".join(_convert_to_raster_space(src_dst, poly, op))
            multi_polys.append(f"({polys})")
        str_multipoly = ",".join(multi_polys)
        wkt = f"MULTIPOLYGON ({str_multipoly})"

    else:
        raise RioTilerError(
            "Invalid geometry type: {geom_type}. Should be Polygon or MultiPolygon"
        )

    return wkt


def _array_gdal_name(data: numpy.ndarray) -> str:
    """Return GDAL MEM dataset name."""
    if len(data.shape) == 2:
        count = 1
        height = data.shape[0]
        width = data.shape[1]
    else:
        count = data.shape[0]
        height = data.shape[1]
        width = data.shape[2]

    info = {
        "DATAPOINTER": data.__array_interface__["data"][0],
        "PIXELS": width,
        "LINES": height,
        "BANDS": count,
        "DATATYPE": _gdal_typename(data.dtype.name),
    }
    # ref: https://github.com/rasterio/rasterio/pull/2512
    strides = data.__array_interface__.get("strides", None)
    if strides is not None:
        if len(strides) == 2:
            lineoffset, pixeloffset = strides
            info.update(LINEOFFSET=lineoffset, PIXELOFFSET=pixeloffset)
        else:
            bandoffset, lineoffset, pixeloffset = strides
            info.update(
                BANDOFFSET=bandoffset, LINEOFFSET=lineoffset, PIXELOFFSET=pixeloffset
            )

    dataset_options = ",".join(f"{name}={val}" for name, val in info.items())
    return f"MEM:::{dataset_options}"


def resize_array(
    data: numpy.ndarray,
    height: int,
    width: int,
    resampling_method: RIOResampling = "nearest",
) -> numpy.ndarray:
    """resize array to a given height and width."""
    out_shape: Union[Tuple[int, int], Tuple[int, int, int]]
    if len(data.shape) == 2:
        out_shape = (height, width)
    else:
        out_shape = (data.shape[0], height, width)

    datasetname = _array_gdal_name(data)
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=NotGeoreferencedWarning,
            module="rasterio",
        )
        with rasterio.open(datasetname, "r+") as src:
            # if a 2D array is passed, using indexes=1 makes sure we return an 2D array
            indexes = 1 if len(data.shape) == 2 else None
            return src.read(
                out_shape=out_shape,
                indexes=indexes,
                resampling=Resampling[resampling_method],
            )


def normalize_bounds(bounds: BBox) -> BBox:
    """Return BBox in correct minx, miny, maxx, maxy order."""
    return (
        min(bounds[0], bounds[2]),
        min(bounds[1], bounds[3]),
        max(bounds[0], bounds[2]),
        max(bounds[1], bounds[3]),
    )


def _validate_shape_input(shape: Dict) -> Dict:
    """Ensure input shape is valid and reduce features to geometry"""

    if "geometry" in shape:
        shape = shape["geometry"]

    if not is_valid_geom(shape):
        raise RioTilerError("Invalid geometry")

    return shape


def cast_to_sequence(val: Optional[Any] = None) -> Sequence:
    """Cast input to sequence if not Tuple of List."""
    if val is not None and not isinstance(val, (list, tuple)):
        val = (val,)

    return val


def _CRS_authority_info(crs: CRS) -> Optional[Tuple[str, str, str]]:
    """Convert CRS to URI.

    Code adapted from https://github.com/developmentseed/morecantile/blob/1829fe12408e4a1feee7493308f3f02257ef4caf/morecantile/models.py#L148-L161
    """
    # attempt to grab the authority, version, and code from the CRS
    if authority_code := crs.to_authority(confidence_threshold=70):
        version = "0"
        authority, code = authority_code
        # if we have a version number in the authority, split it out
        if "_" in authority:
            authority, version = authority.split("_")

        return authority, version, code

    return None


def CRS_to_uri(crs: CRS) -> Optional[str]:
    """Convert CRS to URI."""
    if info := _CRS_authority_info(crs):
        authority, version, code = info

        return f"http://www.opengis.net/def/crs/{authority}/{version}/{code}"

    return None


def CRS_to_urn(crs: CRS) -> Optional[str]:
    """Convert CRS to URN."""
    if info := _CRS_authority_info(crs):
        authority, version, code = info
        if version == "0":
            version = ""

        return f"urn:ogc:def:crs:{authority}:{version}:{code}"

    return None
