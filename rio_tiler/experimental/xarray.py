"""Xarray experimental reader."""

from __future__ import annotations

import math
import warnings
from typing import Any, cast

import attr
import numpy
from affine import Affine
from morecantile import Tile, TileMatrixSet
from rasterio.crs import CRS
from rasterio.transform import array_bounds, rowcol
from rasterio.warp import calculate_default_transform
from rasterio.warp import transform as transform_coords
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds as window_from_bounds

from rio_tiler._warp import warp
from rio_tiler.constants import (
    MAX_ARRAY_SIZE,
    WEB_MERCATOR_CRS,
    WEB_MERCATOR_TMS,
    WGS84_CRS,
)
from rio_tiler.errors import (
    InvalidGeographicBounds,
    MaxArraySizeError,
    PointOutsideBounds,
    TileOutsideBounds,
)
from rio_tiler.io.xarray import Options, XarrayReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox, Indexes, NoData, RIOResampling, WarpResampling
from rio_tiler.utils import (
    CRS_to_uri,
    _get_width_height,
    _missing_size,
    cast_to_sequence,
)

try:
    import xarray
except ImportError:  # pragma: nocover
    xarray = None  # type: ignore


MULTISCALE_CONVENTION_UUID = "d35379db-88df-4056-af3a-620245f8e347"
SPATIAL_CONVENTION_UUID = "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4"
PROJ_CONVENTION_UUID = "f17cb550-5864-4468-aeb7-f3180cfb622f"


def _has_multiscales(conventions: list[dict]) -> bool:
    return next(
        (True for c in conventions if c["uuid"] == MULTISCALE_CONVENTION_UUID),
        False,
    )


def _has_spatial(conventions: list[dict]) -> bool:
    return next(
        (True for c in conventions if c["uuid"] == SPATIAL_CONVENTION_UUID),
        False,
    )


def _has_proj(conventions: list[dict]) -> bool:
    return next(
        (True for c in conventions if c["uuid"] == PROJ_CONVENTION_UUID),
        False,
    )


def _get_proj_crs(attributes: dict) -> CRS:
    """Get CRS defined by PROJ conventions."""
    proj_string = next(
        (  # type: ignore
            attributes.get(key)
            for key in ["proj:code", "proj:wkt2", "proj:projjson"]
            if key in attributes
        )
    )
    return CRS.from_user_input(proj_string)


@attr.s
class GeoArrayReader(XarrayReader):
    """GeoZarr Array Reader.
    A Xarray based reader for geospatial arrays following Zarr Conventions.

    Attributes:
        input (xarray.DataArray): Xarray DataArray.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.

    Examples:
        >>> import xarray
            from obstore.store import HTTPStore
            from zarr.storage import ObjectStore
            from affine import Affine
            from rasterio.crs import CRS
            from matplotlib.pyplot import imshow

            # Create Obstore Store
            store = HTTPStore("https://s3.explorer.eopf.copernicus.eu/esa-zarr-sentinel-explorer-fra/tests-output/sentinel-2-l2a/S2B_MSIL2A_20260216T142149_N0512_R096_T25WFV_20260216T165051.zarr")
            zarr_store = ObjectStore(store=store, read_only=True)
            dt = xarray.open_datatree(
                zarr_store,
                engine="zarr",
                create_default_indexes=False,
                consolidated=True,
            )

            ds = dt["/measurements/reflectance/r720m"]

            attributes = ds.attrs

            tr = attributes["spatial:transform"]
            transform = Affine(*tr)
            crs = CRS.from_user_input(attributes["proj:code"])

            with GeoArrayReader(ds["b02"], transform=transform, crs=crs) as dst:
                img = dst.preview()

    """

    input: xarray.DataArray = attr.ib()

    crs: CRS | None = attr.ib(default=None)
    transform: Affine | None = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    options: Options = attr.ib()

    nbands: int = attr.ib(init=False)

    # List of names for the first dimension (e.g time, bands, etc)
    band_names: list[str] | None = attr.ib(default=None)

    _dims: list = attr.ib(init=False, factory=list)

    @options.default
    def _options_default(self):
        return {}

    def __attrs_post_init__(self) -> None:
        """Set bounds and CRS."""
        assert xarray is not None, "xarray must be installed to use XarrayReader"

        attributes = self.input.attrs

        # Zarr Conventions
        conventions: list[dict] = attributes.get("zarr_conventions", [])

        # Transform
        if not self.transform and _has_spatial(conventions):
            transform_type = attributes.get("spatial:transform_type") or "affine"
            tr = attributes.get("spatial:transform")
            if transform_type == "affine" and tr is not None:
                if attributes.get("spatial:registration", "pixel") == "node":
                    # NOTE: If the registration is "node", we need to adjust the transform to
                    # account for the fact that the coordinates refer to the center of the pixel rather than the edge.
                    tr[2] -= tr[0] / 2
                    tr[5] -= tr[4] / 2

                self.transform = Affine(*tr)

        assert self.transform, (
            "Affine transform is required, either as an argument or in `spatial` zarr_conventions"
        )

        # CRS
        if not self.crs and _has_proj(conventions):
            self.crs = _get_proj_crs(attributes)

        assert self.crs, (
            "CRS is required, either as an argument or in `geo-proj` zarr_conventions"
        )

        if len(self.input.shape) > 2:
            self._dims = [
                d
                for d in self.input.dims
                if d not in ["x", "y", "spatial_ref", "crs_wkt", "grid_mapping"]
            ]

        # NOTE: Assume shape of array is (bands, height, width) or (height, width)
        # and get height/width from the last 2 dimensions of the shape.
        shape = attributes.get("spatial:shape", self.input.shape)
        self.height, self.width = shape[-2], shape[-1]

        assert len(self.input.shape) in [2, 3], "Can't handle 1D or >=4D DataArray"
        if len(self.input.shape) == 3:
            self.nbands = self.input.shape[0]
        else:
            self.nbands = 1

        self.bounds = attributes.get("spatial:bounds")
        if not self.bounds:
            self.bounds = array_bounds(self.height, self.width, self.transform)

        if self.crs == WGS84_CRS and (
            self.bounds[0] < -180
            or self.bounds[1] < -90
            or self.bounds[2] > 180
            or self.bounds[3] > 90
        ):
            raise InvalidGeographicBounds(
                f"Invalid geographic bounds: {self.bounds}. Must be within (-180, -90, 180, 90)."
            )

        if self.band_names:
            assert len(self.band_names) == self.nbands, (
                "Length of band_names must match number of bands in the array"
            )

    @property
    def band_descriptions(self) -> list[str]:
        """
        Return list of `band descriptions` in DataArray.

        `Bands` are all dimensions not defined as spatial dims by rioxarray.
        """
        if self.band_names:
            return self.band_names

        if not self._dims:
            coords_name = [
                d
                for d in self.input.coords
                if d
                not in [
                    self.input.rio.x_dim,
                    self.input.rio.y_dim,
                    "spatial_ref",
                    "crs_wkt",
                    "grid_mapping",
                ]
            ]
            if coords_name:
                return [str(self.input.coords[coords_name[0]].data)]

            return [self.input.name or "b1"]  # type: ignore

        return [str(band) for d in self._dims for band in self.input[d].values]

    @property
    def minzoom(self):
        """Return dataset minzoom.

        A dataarray doesn't have overviews so minzoom==maxzoom
        """
        return self.maxzoom

    @property
    def maxzoom(self):
        """Return dataset maxzoom."""
        return self._maxzoom

    @property
    def _nodata_value(self) -> NoData | None:
        return self.input.attrs.get(
            "_FillValue",
            self.input.attrs.get(
                "missing_value",
                self.input.attrs.get("fill_value", self.input.attrs.get("nodata")),
            ),
        )

    def info(self) -> Info:
        """Return xarray.DataArray info."""
        metadata = [band.attrs for d in self._dims for band in self.input[d]] or [{}]

        nodata_type = "None"
        if self.options.get("nodata", self._nodata_value) is not None:
            nodata_type = "Nodata"

        meta = {
            "bounds": self.bounds,
            "crs": CRS_to_uri(self.crs) or self.crs.to_wkt(),
            "band_metadata": [(f"b{ix}", v) for ix, v in enumerate(metadata, 1)],
            "band_descriptions": [
                (f"b{ix}", v or f"b{ix}")
                for ix, v in enumerate(self.band_descriptions, 1)
            ],
            "dtype": str(self.input.dtype),
            "nodata_type": nodata_type,
            # additional info (not in default model)
            "name": self.input.name,
            "count": self.nbands,
            "width": self.width,
            "height": self.height,
            "dimensions": self.input.dims,
            "attrs": {
                k: (v.tolist() if isinstance(v, (numpy.ndarray, numpy.generic)) else v)
                for k, v in self.input.attrs.items()
            },
        }
        minv, maxv = self.input.attrs.get("valid_min"), self.input.attrs.get("valid_max")
        if minv is not None and maxv is not None:
            meta["minmax"] = list(((minv, maxv),) * self.nbands)

        return Info.model_validate(meta)

    def statistics(  # type: ignore[override]
        self,
        categorical: bool = False,
        categories: list[float] | None = None,
        percentiles: list[int] | None = None,
        hist_options: dict | None = None,
        indexes: Indexes | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> dict[str, BandStatistics]:
        """Return statistics from a dataset."""
        img = self._read(indexes=indexes, nodata=nodata)

        return img.statistics(
            categorical=categorical,
            categories=categories,
            percentiles=percentiles,
            hist_options=hist_options,
        )

    def tile(  # type: ignore[override]
        self,
        tile_x: int,
        tile_y: int,
        tile_z: int,
        tilesize: int | None = None,
        indexes: Indexes | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a Web Map tile from a dataset.

        Args:
            tile_x (int): Tile's horizontal index.
            tile_y (int): Tile's vertical index.
            tile_z (int): Tile's zoom level index.
            tilesize (int, optional): Output tile size. Defaults to TMS tilesize.
            indexes (sequence of int or int, optional): Band indexes.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            resampling_method (RIOResampling, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
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

        return self.part(
            bbox,
            dst_crs=self.tms.rasterio_crs,
            bounds_crs=self.tms.rasterio_crs,
            indexes=indexes,
            max_size=None,
            height=tilesize or matrix.tileHeight,
            width=tilesize or matrix.tileWidth,
            nodata=nodata,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
            **kwargs,
        )

    def part(  # type: ignore[override]
        self,
        bbox: BBox,
        dst_crs: CRS | None = None,
        bounds_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        max_size: int | None = None,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        reproject_method: WarpResampling = "nearest",
        resampling_method: RIOResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a dataset.

        Args:
            bbox (tuple): Output bounds (left, bottom, right, top) in target crs.
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to bounds_crs.
            bounds_crs (rasterio.crs.CRS, optional): CRS of the input bounds. Defaults to WGS84.
            indexes (sequence of int or int, optional): Band indexes.
            max_size (int, optional): Limit the size of the longest dimension.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.
            resampling_method (RIOResampling, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        dst_crs = dst_crs or bounds_crs

        # Transform bbox from bounds_crs → dst_crs
        if bounds_crs != dst_crs:
            bbox = transform_bounds(bounds_crs, dst_crs, *bbox, densify_pts=21)

        # 1. Estimate output dimensions
        if dst_crs != self.crs:
            # Case 1: Reprojection needed
            # - reproject bbox to dataset CRS
            # - compute native output shape in dataset resolution/CRS
            # - compute output shape in output CRS
            dst_bounds = transform_bounds(dst_crs, self.crs, *bbox, densify_pts=21)
            native_src_w = max(
                1, round((dst_bounds[2] - dst_bounds[0]) / abs(self.transform.a))
            )
            native_src_h = max(
                1, round((dst_bounds[3] - dst_bounds[1]) / abs(self.transform.e))
            )
            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, native_src_w, native_src_h, *dst_bounds
            )
        else:
            # Case 2: No reprojection needed
            # - keep output dataset bbox as input bbox
            # - compute output shape in dataset resolution/CRS
            dst_bounds = bbox
            dst_width = max(1, round((bbox[2] - bbox[0]) / abs(self.transform.a)))
            dst_height = max(1, round((bbox[3] - bbox[1]) / abs(self.transform.e)))

        # Case 1: `max_size` is set,
        # compute output shape based on it,
        # respecting aspect ratio of the output bbox (dst_width/dst_height)
        if max_size:
            height, width = _get_width_height(max_size, dst_height, dst_width)

        # Case 2: One of width/height is missing,
        # compute it but keep the aspect ratio from the max output bbox (dst_width/dst_height)
        elif _missing_size(width, height):
            ratio = dst_height / dst_width
            if width:
                height = math.ceil(width * ratio)
            else:
                width = math.ceil(height / ratio)

        # 2. Output shape (in the output CRS)
        height = cast(int, height or dst_height)
        width = cast(int, width or dst_width)

        # 3. Build pixel window from bounds in dataset CRS
        rasterio_win = window_from_bounds(*dst_bounds, transform=self.transform)
        row_off = math.floor(rasterio_win.row_off)
        col_off = math.floor(rasterio_win.col_off)
        win_width = math.ceil(rasterio_win.width) + 1
        win_height = math.ceil(rasterio_win.height) + 1

        # Validate intersection
        col_end = min(self.width, math.ceil(rasterio_win.col_off + rasterio_win.width))
        row_end = min(self.height, math.ceil(rasterio_win.row_off + rasterio_win.height))
        if col_off >= col_end or row_off >= row_end:
            raise ValueError("Input BBOX and dataset bounds do not intersect")

        # Clamp window to array bounds
        clipped_col_off = max(0, col_off)
        clipped_row_off = max(0, row_off)
        clipped_col_stop = min(self.width, col_off + win_width)
        clipped_row_stop = min(self.height, row_off + win_height)

        # 3. Read data from zarr array
        img = self._read(
            indexes=indexes,
            row_slice=slice(clipped_row_off, clipped_row_stop),
            col_slice=slice(clipped_col_off, clipped_col_stop),
            nodata=nodata,
        )

        # 4. Reproject/resample to output CRS and dimensions
        img = warp(
            img,
            dst_crs=dst_crs,
            dst_bounds=bbox,
            dst_width=width,
            dst_height=height,
            reproject_method=reproject_method,
            resampling_method=resampling_method,
        )
        return img

    def preview(  # type: ignore[override]
        self,
        indexes: Indexes | None = None,
        dst_crs: CRS | None = None,
        max_size: int | None = 1024,
        height: int | None = None,
        width: int | None = None,
        nodata: NoData | None = None,
        resampling_method: RIOResampling = "nearest",
        reproject_method: WarpResampling = "nearest",
        **kwargs: Any,
    ) -> ImageData:
        """Read a preview of a Dataset.

        Args:
            indexes (sequence of int or int, optional): Band indexes.
            dst_crs (rasterio.crs.CRS, optional): Target coordinate reference system. Defaults to None (same as input).
            max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to 1024.
            height (int, optional): Output height of the array.
            width (int, optional): Output width of the array.
            nodata (int or float, optional): Overwrite dataset internal nodata value.
            resampling_method (RIOResampling, optional): GDAL Resampling method to use when resizing. Defaults to "nearest".
            reproject_method (WarpResampling, optional): WarpKernel resampling algorithm. Defaults to `nearest`.

        Returns:
            rio_tiler.models.ImageData: ImageData instance with data, mask and input spatial info.

        """
        if max_size and (width or height):
            warnings.warn(
                "'max_size' will be ignored with with 'height' or 'width' set.",
                UserWarning,
            )
            max_size = None

        # 1. Determine output shape
        # get height/width of the dataset in the output CRS
        dst_width = self.width
        dst_height = self.height
        row_slice = None
        if dst_crs and dst_crs != self.crs:
            # Get shape of the dataset in the output CRS
            src_width = self.width
            src_height = self.height
            src_bounds = list(self.bounds)
            if (
                self.crs == WGS84_CRS
                and dst_crs == WEB_MERCATOR_CRS
                and (self.bounds[1] < -85.06 or self.bounds[3] > 85.06)
            ):
                warnings.warn(
                    "Adjusting dataset latitudes to avoid re-projection overflow (EPSG:4326 -> EPSG:3857) for latitudes outside of Web Mercator limits (-85.06, 85.06).",
                    UserWarning,
                )
                src_bounds[1] = max(src_bounds[1], -85.06)
                src_bounds[3] = min(src_bounds[3], 85.06)

                rasterio_win = window_from_bounds(*src_bounds, transform=self.transform)
                src_height = round(rasterio_win.height)
                row_off = math.floor(rasterio_win.row_off)
                win_height = math.ceil(rasterio_win.height) + 1
                row_slice = slice(row_off, row_off + win_height)

            _, dst_width, dst_height = calculate_default_transform(
                self.crs, dst_crs, src_width, src_height, *src_bounds
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

        # 2. Read data
        img = self._read(indexes=indexes, row_slice=row_slice, nodata=nodata)

        # 3. Reproject if needed
        if dst_crs and dst_crs != self.crs:
            img = img.reproject(
                dst_crs=dst_crs,
                reproject_method=reproject_method,
            )

        # 4. Resize
        if width != img.width or height != img.height:
            img = img.resize(
                width=width,
                height=height,
                resampling_method=resampling_method,
            )

        return img

    def point(  # type: ignore[override]
        self,
        lon: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        indexes: Indexes | None = None,
        nodata: NoData | None = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a value from a Dataset.

        Args:
            lon (float): Longitude.
            lat (float): Latitude.
            coord_crs (rasterio.crs.CRS, optional): Coordinate Reference System of the input coords. Defaults to `epsg:4326`.
            indexes (sequence of int or int, optional): Band indexes.
            nodata: (int or float, optional): Overwrite dataset internal nodata value. Defaults to `None`.

        Returns:
            PointData: Pixel value per bands/assets.

        """
        coordinates = (lon, lat)
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

        y, x = rowcol(self.transform, [lon], [lat])

        da, band_descriptions = self._sel_indexes(indexes)
        arr: numpy.ma.MaskedArray
        if da.ndim == 2:
            arr = da[int(y[0]), int(x[0])].to_masked_array()
            arr = numpy.expand_dims(arr, axis=0)  # type: ignore[assignment]
        else:
            arr = da[:, int(y[0]), int(x[0])].to_masked_array()

        nodata = (
            nodata
            if nodata is not None
            else self.options.get("nodata", self._nodata_value)
        )
        if nodata is not None:
            arr.mask |= arr.data == nodata

        indexes = cast_to_sequence(indexes)
        if not indexes:
            indexes = list(range(1, arr.shape[0] + 1))

        return PointData(
            arr,
            coordinates=coordinates,
            crs=coord_crs,
            band_names=[f"b{idx}" for idx in indexes],
            band_descriptions=band_descriptions,
            pixel_location=(x.tolist()[0], y.tolist()[0]),
            nodata=nodata,
        )

    def _read(
        self,
        row_slice: slice | None = None,
        col_slice: slice | None = None,
        indexes: Indexes | None = None,
        nodata: NoData | None = None,
    ) -> ImageData:
        """Read data from zarr AsyncArray.

        Args:
            indexes: Band indexes (1-based). If None, reads all bands.
            row_slice: Row slice for windowed read.
            col_slice: Column slice for windowed read.
            nodata (int or float, optional): Overwrite dataset internal nodata value.

        Returns:
            ImageData: Image data with mask and spatial info.

        """
        da, band_descriptions = self._sel_indexes(indexes)

        row_slice = row_slice or slice(0, self.height)
        col_slice = col_slice or slice(0, self.width)
        read_height = row_slice.stop - row_slice.start
        read_width = col_slice.stop - col_slice.start

        arr: numpy.ma.MaskedArray
        if len(da.shape) == 2:
            # 2D array: (height, width)
            nbytes = read_height * read_width * self.input.dtype.itemsize
            if nbytes > MAX_ARRAY_SIZE:
                raise MaxArraySizeError(
                    f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {(1, read_height, read_width)} in memory."
                )

            arr = da[row_slice, col_slice].to_masked_array()
            arr = numpy.expand_dims(arr, axis=0)  # type: ignore[assignment]

        else:
            # 3D array: (bands, height, width)
            nbytes = da.shape[0] * read_height * read_width * self.input.dtype.itemsize
            if nbytes > MAX_ARRAY_SIZE:
                raise MaxArraySizeError(
                    f"Maximum array limit {MAX_ARRAY_SIZE} reached, trying to put Array of {(da.shape[0], read_height, read_width)} in memory."
                )

            arr = da[:, row_slice, col_slice].to_masked_array()

        # if data has Nodata then we simply make sure the mask == the nodata
        nodata = (
            nodata
            if nodata is not None
            else self.options.get("nodata", self._nodata_value)
        )
        if nodata is not None:
            arr.mask |= arr.data == nodata

        # Calculate bounds for the read window
        read_transform = self.transform * Affine.translation(
            col_slice.start, row_slice.start
        )
        read_bounds = array_bounds(read_height, read_width, read_transform)

        indexes = cast_to_sequence(indexes)
        if not indexes:
            indexes = list(range(1, arr.shape[0] + 1))

        # Forward valid_min/valid_max to the ImageData object
        minv, maxv = da.attrs.get("valid_min"), da.attrs.get("valid_max")
        stats = None
        if minv is not None and maxv is not None:
            stats = ((minv, maxv),) * arr.shape[0]

        return ImageData(
            arr,
            bounds=read_bounds,
            band_names=[f"b{idx}" for idx in indexes],
            band_descriptions=band_descriptions,
            crs=self.crs,
            dataset_statistics=stats,
            nodata=nodata,
        )
