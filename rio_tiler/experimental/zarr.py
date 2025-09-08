"""rio_tiler.io.experimental.xarray Readers."""

from __future__ import annotations

import contextlib
from functools import cache
from pathlib import Path
from typing import Any, Callable, Dict, List, Literal, Optional, Union
from urllib.parse import urlparse

import attr
from morecantile import TileMatrixSet
from rasterio.crs import CRS

from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
from rio_tiler.errors import InvalidGeographicBounds
from rio_tiler.io.base import BaseReader
from rio_tiler.io.xarray import XarrayReader
from rio_tiler.models import BandStatistics, ImageData, Info, PointData
from rio_tiler.types import BBox

try:
    import obstore
    from zarr.storage import ObjectStore
except ImportError:  # pragma: nocover
    ObjectStore = None  # type: ignore
    obstore = None  # type: ignore

try:
    import rioxarray
    import xarray
except ImportError:  # pragma: nocover
    xarray = None  # type: ignore
    rioxarray = None  # type: ignore

sel_methods = Literal["nearest", "pad", "ffill", "backfill", "bfill"]


@cache
def open_dataset(src_path: str, **kwargs: Any) -> xarray.Dataset:
    """Open Xarray dataset

    Args:
        src_path (str): dataset path.

    Returns:
        xarray.DataTree

    """
    parsed = urlparse(src_path)
    if not parsed.scheme:
        src_path = str(Path(src_path).resolve())
        src_path = "file://" + src_path
    store = obstore.store.from_url(src_path, **kwargs)
    zarr_store = ObjectStore(store=store, read_only=True)
    ds = xarray.open_dataset(
        zarr_store,
        decode_times=True,
        decode_coords="all",
        consolidated=True,
        engine="zarr",
    )
    return ds


@attr.s
class ZarrReader(BaseReader):
    """Zarr dataset Reader.

    Attributes:
        input (str): dataset path.
        dataset (xarray.Dataset): Xarray dataset.
        tms (morecantile.TileMatrixSet, optional): TileMatrixSet grid definition. Defaults to `WebMercatorQuad`.
        opener (Callable): Xarray dataset opener. Defaults to `open_dataset`.
        opener_options (dict): Options to forward to the opener callable.

    Examples:
        >>> with ZarrReader(
                "s3://mur-sst/zarr-v1",
                opener_options={
                    "skip_signature": True,
                    "region": "us-west-2",
                }
            ) as src:
                print(src)
                print(src.variables)
                img = src.tile(x, y, z, tmax)

    """

    input: str = attr.ib()
    dataset: xarray.Dataset = attr.ib(default=None)

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    opener: Callable[..., xarray.Dataset] = attr.ib(default=open_dataset)
    opener_options: Dict = attr.ib(factory=dict)
    _ctx_stack: contextlib.ExitStack = attr.ib(init=False, factory=contextlib.ExitStack)

    def __attrs_post_init__(self):
        """Set bounds and CRS."""
        assert xarray is not None, "xarray must be installed to use XarrayReader"
        assert rioxarray is not None, "rioxarray must be installed to use XarrayReader"

        if not self.dataset:
            self.dataset = self._ctx_stack.enter_context(
                self.opener(self.input, **self.opener_options)
            )

        # NOTE: rioxarray returns **ordered** bounds in form of (minx, miny, maxx, maxx)
        self.bounds = tuple(self.dataset.rio.bounds())
        # Make sure we have a valid CRS
        self.dataset = self.dataset.rio.write_crs(
            self.dataset.rio.crs or "epsg:4326",
        )

        self.crs = self.dataset.rio.crs

        # adds half x/y resolution on each values
        # https://github.com/corteva/rioxarray/issues/645#issuecomment-1461070634
        xres, yres = map(abs, self.dataset.rio.resolution())
        if self.crs == WGS84_CRS and (
            self.bounds[0] + xres / 2 < -180
            or self.bounds[1] + yres / 2 < -90
            or self.bounds[2] - xres / 2 > 180
            or self.bounds[3] - yres / 2 > 90
        ):
            raise InvalidGeographicBounds(
                f"Invalid geographic bounds: {self.bounds}. Must be within (-180, -90, 180, 90)."
            )

        self.transform = self.dataset.rio.transform()
        self.height = self.dataset.rio.height
        self.width = self.dataset.rio.width

    def close(self):
        """Close xarray dataset."""
        self._ctx_stack.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        self.close()

    @property
    def variables(self) -> List[str]:
        """Return dataset variable names"""
        return list(self.dataset.data_vars)

    def _arrange_dims(self, da: xarray.DataArray) -> xarray.DataArray:
        """Arrange coordinates and time dimensions.

        An rioxarray.exceptions.InvalidDimensionOrder error is raised if the coordinates are not in the correct order time, y, and x.
        See: https://github.com/corteva/rioxarray/discussions/674

        We conform to using x and y as the spatial dimension names..

        """
        if "x" not in da.dims and "y" not in da.dims:
            try:
                latitude_var_name = next(
                    name
                    for name in ["lat", "latitude", "LAT", "LATITUDE", "Lat"]
                    if name in da.dims
                )
                longitude_var_name = next(
                    name
                    for name in ["lon", "longitude", "LON", "LONGITUDE", "Lon"]
                    if name in da.dims
                )
            except StopIteration as e:
                raise ValueError(f"Couldn't find X/Y dimensions in {da.dims}") from e

            da = da.rename({latitude_var_name: "y", longitude_var_name: "x"})

        if "TIME" in da.dims:
            da = da.rename({"TIME": "time"})

        if extra_dims := [d for d in da.dims if d not in ["x", "y"]]:
            da = da.transpose(*extra_dims, "y", "x")
        else:
            da = da.transpose("y", "x")

        # If min/max values are stored in `valid_range` we add them in `valid_min/valid_max`
        vmin, vmax = da.attrs.get("valid_min"), da.attrs.get("valid_max")
        if "valid_range" in da.attrs and not (vmin is not None and vmax is not None):
            valid_range = da.attrs.get("valid_range")
            da.attrs.update({"valid_min": valid_range[0], "valid_max": valid_range[1]})

        return da

    def _get_variable(
        self,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
    ) -> xarray.DataArray:
        """Get DataArray from xarray Dataset."""
        da = self.dataset[variable]

        if sel:
            _idx: Dict[str, List] = {}
            for s in sel:
                val: Union[str, slice]
                dim, val = s.split("=")

                # cast string to dtype of the dimension
                if da[dim].dtype != "O":
                    val = da[dim].dtype.type(val)

                if dim in _idx:
                    _idx[dim].append(val)
                else:
                    _idx[dim] = [val]

            sel_idx = {k: v[0] if len(v) < 2 else v for k, v in _idx.items()}
            da = da.sel(sel_idx, method=method)

        da = self._arrange_dims(da)

        # Make sure we have a valid CRS
        crs = da.rio.crs or "epsg:4326"
        da = da.rio.write_crs(crs)

        if crs == "epsg:4326" and (da.x > 180).any():
            # Adjust the longitude coordinates to the -180 to 180 range
            da = da.assign_coords(x=(da.x + 180) % 360 - 180)

            # Sort the dataset by the updated longitude coordinates
            da = da.sortby(da.x)

        assert len(da.dims) in [
            2,
            3,
        ], "rio_tiler.io.xarray.DatasetReader can only work with 2D or 3D DataArray"

        return da

    def spatial_info(  # type: ignore
        self,
        *,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
    ):
        """Return xarray.DataArray info."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return {
                "crs": da.crs,
                "bounds": da.bounds,
                "minzoom": da.minzoom,
                "maxzoom": da.maxzoom,
            }

    def get_geographic_bounds(  # type: ignore
        self,
        crs: CRS,
        *,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
    ) -> BBox:
        """Return Geographic Bounds for a Geographic CRS."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.get_geographic_bounds(crs)

    def info(  # type: ignore
        self,
        *,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
    ) -> Info:
        """Return xarray.DataArray info."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.info()

    def statistics(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> Dict[str, BandStatistics]:
        """Return statistics from a dataset."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.statistics(*args, **kwargs)

    def tile(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read a Web Map tile from a dataset."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
            tms=self.tms,
        ) as da:
            return da.tile(*args, **kwargs)

    def part(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a dataset."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.part(*args, **kwargs)

    def preview(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Return a preview of a dataset."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.preview(*args, **kwargs)

    def point(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> PointData:
        """Read a pixel value from a dataset."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.point(*args, **kwargs)

    def feature(  # type: ignore
        self,
        *args: Any,
        variable: str,
        sel: Optional[List[str]] = None,
        method: Optional[sel_methods] = None,
        **kwargs: Any,
    ) -> ImageData:
        """Read part of a dataset defined by a geojson feature."""
        with XarrayReader(
            self._get_variable(variable, sel=sel, method=method),
        ) as da:
            return da.feature(*args, **kwargs)
