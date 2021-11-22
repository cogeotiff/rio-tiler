"""rio_tiler.utils: utility functions."""

import os
from io import BytesIO
from typing import Any, Dict, Generator, List, Optional, Sequence, Tuple, Union

import numpy
import rasterio
from affine import Affine
from boto3.session import Session as boto3_session
from rasterio import windows
from rasterio.crs import CRS
from rasterio.dtypes import _gdal_typename
from rasterio.enums import ColorInterp, MaskFlags, Resampling
from rasterio.features import is_valid_geom
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.rio.helpers import coords
from rasterio.transform import from_bounds, rowcol
from rasterio.vrt import WarpedVRT
from rasterio.warp import calculate_default_transform, transform_geom

from .colormap import apply_cmap
from .constants import WEB_MERCATOR_CRS
from .errors import RioTilerError
from .types import BBox, ColorMapType, IntervalTuple


def _chunks(my_list: Sequence, chuck_size: int) -> Generator[Sequence, None, None]:
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(my_list), chuck_size):
        yield my_list[i : i + chuck_size]


def aws_get_object(
    bucket: str,
    key: str,
    request_pays: bool = False,
    client: boto3_session.client = None,
) -> bytes:
    """AWS s3 get object content."""
    if not client:
        session = boto3_session()
        endpoint_url = os.environ.get("AWS_S3_ENDPOINT", None)
        client = session.client("s3", endpoint_url=endpoint_url)

    params = {"Bucket": bucket, "Key": key}
    if request_pays or os.environ.get("AWS_REQUEST_PAYER", "").lower() == "requester":
        params["RequestPayer"] = "requester"

    response = client.get_object(**params)
    return response["Body"].read()


def get_bands_names(
    indexes: Optional[Sequence[int]] = None,
    expression: Optional[str] = None,
    count: Optional[int] = None,
) -> List[str]:
    """Define bands names based on expression, indexes or band count."""
    if expression:
        return expression.split(",")

    elif indexes:
        return [str(idx) for idx in indexes]

    elif count:
        return [str(idx + 1) for idx in range(count)]

    else:
        raise ValueError(
            "one of expression or indexes or count must be passed to define band names."
        )


def get_array_statistics(
    data: numpy.ma.MaskedArray,
    categorical: bool = False,
    categories: Optional[List[float]] = None,
    percentiles: List[int] = [2, 98],
    **kwargs: Any,
) -> List[Dict[Any, Any]]:
    """Calculate per band array statistics.

    Args:
        data (numpy.ma.MaskedArray): input masked array data to get the statistics from.
        categorical (bool): treat input data as categorical data. Defaults to False.
        categories (list of numbers, optional): list of categories to return value for.
        percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
        kwargs (optional): options to forward to `numpy.histogram` function (only applies for non-categorical data).

    Returns:
        list of dict

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
    if len(data.shape) < 3:
        data = numpy.expand_dims(data, axis=0)

    output: List[Dict[Any, Any]] = []
    percentiles_names = [f"percentile_{int(p)}" for p in percentiles]

    for b in range(data.shape[0]):
        keys, counts = numpy.unique(data[b].compressed(), return_counts=True)

        valid_pixels = float(numpy.ma.count(data[b]))
        masked_pixels = float(numpy.ma.count_masked(data[b]))
        valid_percent = round((valid_pixels / data[b].size) * 100, 2)
        info_px = {
            "valid_pixels": valid_pixels,
            "masked_pixels": masked_pixels,
            "valid_percent": valid_percent,
        }

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
            h_counts, h_keys = numpy.histogram(data[b][~data[b].mask], **kwargs)
            histogram = [h_counts.tolist(), h_keys.tolist()]

        percentiles_values = numpy.percentile(
            data[b].compressed(), percentiles
        ).tolist()

        output.append(
            {
                "min": float(data[b].min()),
                "max": float(data[b].max()),
                "mean": float(data[b].mean()),
                "count": float(data[b].count()),
                "sum": float(data[b].sum()),
                "std": float(data[b].std()),
                "median": float(numpy.ma.median(data[b])),
                "majority": float(keys[counts.tolist().index(counts.max())].tolist()),
                "minority": float(keys[counts.tolist().index(counts.min())].tolist()),
                "unique": float(counts.size),
                **dict(zip(percentiles_names, percentiles_values)),
                "histogram": histogram,
                **info_px,
            }
        )

    return output


# https://github.com/OSGeo/gdal/blob/b1c9c12ad373e40b955162b45d704070d4ebf7b0/gdal/frmts/ingr/IngrTypes.cpp#L191
def _div_round_up(a: int, b: int) -> int:
    return (a // b) if (a % b) == 0 else (a // b) + 1


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

        for ovr_idx in range(ovr_idx, len(res) - 1):
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
) -> Tuple[Affine, int, int]:
    """Calculate VRT transform.

    Args:
        src_dst (rasterio.io.DatasetReader or rasterio.io.DatasetWriter or rasterio.vrt.WarpedVRT): Rasterio dataset.
        bounds (tuple): Bounding box coordinates in target crs (**dst_crs**).
        height (int, optional): Desired output height of the array for the input bounds.
        width (int, optional): Desired output width of the array for the input bounds.
        dst_crs (rasterio.crs.CRS, optional): Target Coordinate Reference System. Defaults to `epsg:3857`.

    Returns:
        tuple: VRT transform (affine.Affine), width (int) and height (int)

    """
    dst_transform, _, _ = calculate_default_transform(
        src_dst.crs, dst_crs, src_dst.width, src_dst.height, *src_dst.bounds
    )

    # If bounds window is aligned with the dataset internal tile we align the bounds with the pixels.
    # This is to limit the number of internal block fetched.
    if _requested_tile_aligned_with_internal_tile(
        src_dst, bounds, height, width, dst_crs
    ):
        col_off, row_off, w, h = windows.from_bounds(
            *bounds,
            transform=src_dst.transform,
            width=width,
            height=height,
        ).flatten()

        w = windows.Window(
            round(col_off, window_precision),
            round(row_off, window_precision),
            round(w, window_precision),
            round(h, window_precision),
        )
        bounds = src_dst.window_bounds(w)

    w, s, e, n = bounds

    # TODO: Explain
    if not height or not width:
        vrt_width = max(1, round((e - w) / dst_transform.a))
        vrt_height = max(1, round((s - n) / dst_transform.e))
        vrt_transform = from_bounds(w, s, e, n, vrt_width, vrt_height)
        return vrt_transform, vrt_width, vrt_height

    # TODO: Explain
    tile_transform = from_bounds(w, s, e, n, width, height)
    w_res = (
        tile_transform.a
        if abs(tile_transform.a) < abs(dst_transform.a)
        else dst_transform.a
    )
    h_res = (
        tile_transform.e
        if abs(tile_transform.e) < abs(dst_transform.e)
        else dst_transform.e
    )

    # TODO: Explain
    vrt_width = max(1, round((e - w) / w_res))
    vrt_height = max(1, round((s - n) / h_res))
    vrt_transform = from_bounds(w, s, e, n, vrt_width, vrt_height)

    return vrt_transform, vrt_width, vrt_height


def has_alpha_band(src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT]) -> bool:
    """Check for alpha band or mask in source."""
    if (
        any([MaskFlags.alpha in flags for flags in src_dst.mask_flag_enums])
        or ColorInterp.alpha in src_dst.colorinterp
    ):
        return True
    return False


def has_mask_band(src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT]) -> bool:
    """Check for mask band in source."""
    if any(
        [
            (MaskFlags.per_dataset in flags and MaskFlags.alpha not in flags)
            for flags in src_dst.mask_flag_enums
        ]
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
    image = numpy.clip(image, imin, imax) - imin
    image = image / numpy.float64(imax - imin)
    return image * (omax - omin) + omin


def _requested_tile_aligned_with_internal_tile(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    bounds: BBox,
    height: Optional[int] = None,
    width: Optional[int] = None,
    bounds_crs: CRS = WEB_MERCATOR_CRS,
) -> bool:
    """Check if tile is aligned with internal tiles."""
    if not src_dst.is_tiled:
        return False

    if src_dst.crs != bounds_crs:
        return False

    col_off, row_off, w, h = windows.from_bounds(
        *bounds, transform=src_dst.transform, height=height, width=width
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
        >>> with COGReader("my_tif.tif") as cog:
            img = cog.preview()
            with open('test.jpg', 'wb') as f:
                f.write(render(img.data, img.mask, img_format="jpeg"))


    """
    img_format = img_format.upper()

    if len(data.shape) < 3:
        data = numpy.expand_dims(data, axis=0)

    if colormap:
        data, alpha = apply_cmap(data, colormap)
        if mask is not None:
            mask = (
                mask * alpha * 255
            )  # This is a special case when we want to mask some valid data

    # WEBP doesn't support 1band dataset so we must hack to create a RGB dataset
    if img_format == "WEBP" and data.shape[0] == 1:
        data = numpy.repeat(data, 3, axis=0)

    if img_format == "PNG" and data.dtype == "uint16" and mask is not None:
        mask = linear_rescale(mask, (0, 255), (0, 65535)).astype("uint16")

    elif img_format == "JPEG":
        mask = None

    elif img_format == "NPY":
        # If mask is not None we add it as the last band
        if mask is not None:
            mask = numpy.expand_dims(mask, axis=0)
            data = numpy.concatenate((data, mask))

        bio = BytesIO()
        numpy.save(bio, data)
        bio.seek(0)
        return bio.getvalue()

    elif img_format == "NPZ":
        bio = BytesIO()
        if mask is not None:
            numpy.savez_compressed(bio, data=data, mask=mask)
        else:
            numpy.savez_compressed(bio, data=data)
        bio.seek(0)
        return bio.getvalue()

    count, height, width = data.shape

    output_profile = dict(
        driver=img_format,
        dtype=data.dtype,
        count=count + 1 if mask is not None else count,
        height=height,
        width=width,
    )
    output_profile.update(creation_options)

    with MemoryFile() as memfile:
        with memfile.open(**output_profile) as dst:
            dst.write(data, indexes=list(range(1, count + 1)))
            # Use Mask as an alpha band
            if mask is not None:
                dst.write(mask.astype(data.dtype), indexes=count + 1)

        return memfile.read()


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


def create_cutline(
    src_dst: Union[DatasetReader, DatasetWriter, WarpedVRT],
    geometry: Dict,
    geometry_crs: CRS = None,
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
    if "geometry" in geometry:
        geometry = geometry["geometry"]

    if not is_valid_geom(geometry):
        raise RioTilerError("Invalid geometry")

    geom_type = geometry["type"]
    if geom_type not in ["Polygon", "MultiPolygon"]:
        raise RioTilerError(
            "Invalid geometry type: {geom_type}. Should be Polygon or MultiPolygon"
        )

    if geometry_crs:
        geometry = transform_geom(geometry_crs, src_dst.crs, geometry)

    polys = []
    geom = (
        [geometry["coordinates"]] if geom_type == "Polygon" else geometry["coordinates"]
    )
    for p in geom:
        xs, ys = zip(*coords(p))
        src_y, src_x = rowcol(src_dst.transform, xs, ys)
        src_x = [max(0, min(src_dst.width, x)) for x in src_x]
        src_y = [max(0, min(src_dst.height, y)) for y in src_y]
        poly = ", ".join([f"{x} {y}" for x, y in list(zip(src_x, src_y))])
        polys.append(f"(({poly}))")

    str_poly = ",".join(polys)

    return (
        f"POLYGON {str_poly}"
        if geom_type == "Polygon"
        else f"MULTIPOLYGON ({str_poly})"
    )


def resize_array(
    data: numpy.ndarray,
    height: int,
    width: int,
    resampling_method: Resampling = "nearest",
) -> numpy.ndarray:
    """resize array to a given height and width."""
    out_shape: Union[Tuple[int, int], Tuple[int, int, int]]
    if len(data.shape) == 2:
        count = 1
        h = data.shape[0]
        w = data.shape[1]
        out_shape = (height, width)
    else:
        count = data.shape[0]
        h = data.shape[1]
        w = data.shape[2]
        out_shape = (count, height, width)

    # We are using GDAL MEM driver to create a new dataset from the numpy array
    # ref: https://github.com/rasterio/rasterio/blob/master/rasterio/_io.pyx#L1946-L1955
    info = {
        "DATAPOINTER": data.__array_interface__["data"][0],
        "PIXELS": w,
        "LINES": h,
        "BANDS": count,
        "DATATYPE": _gdal_typename(data.dtype.name),
    }
    dataset_options = ",".join(f"{name}={val}" for name, val in info.items())
    datasetname = f"MEM:::{dataset_options}"
    with rasterio.open(datasetname, "r+") as src:
        # if a 2D array is passed, using indexes=1 makes sure we return an 2D array
        indexes = 1 if len(data.shape) == 2 else None
        return src.read(
            out_shape=out_shape,
            indexes=indexes,
            resampling=Resampling[resampling_method],
        )
