import urllib
from enum import Enum
from typing import List, Optional, Tuple, Dict, Any

import uvicorn
from mangum import Mangum
import xarray
from fastapi import FastAPI, Query
from fastapi.responses import Response
from pydantic import BaseModel, Field, root_validator
from rio_tiler.io.xarray import XarrayReader
from starlette.requests import Request
from rio_tiler.colormap import cmap


class SchemeEnum(str, Enum):
    """TileJSON scheme choice."""

    xyz = "xyz"
    tms = "tms"


class TileJSON(BaseModel):
    """
    TileJSON model.

    Based on https://github.com/mapbox/tilejson-spec/tree/master/2.2.0

    """

    tilejson: str = "2.2.0"
    name: Optional[str]
    description: Optional[str]
    version: str = "1.0.0"
    attribution: Optional[str]
    template: Optional[str]
    legend: Optional[str]
    scheme: SchemeEnum = SchemeEnum.xyz
    tiles: List[str]
    grids: Optional[List[str]]
    data: Optional[List[str]]
    minzoom: int = Field(0, ge=0, le=30)
    maxzoom: int = Field(30, ge=0, le=30)
    bounds: List[float] = [-180, -90, 180, 90]
    center: Optional[Tuple[float, float, int]]

    @root_validator
    def compute_center(cls, values):
        """Compute center if it does not exist."""
        bounds = values["bounds"]
        if not values.get("center"):
            values["center"] = (
                (bounds[0] + bounds[2]) / 2,
                (bounds[1] + bounds[3]) / 2,
                values["minzoom"],
            )
        return values

    class Config:
        """TileJSON model configuration."""

        use_enum_values = True


app = FastAPI()
cm = cmap.get('rdpu')


@app.get("/tiles/{z}/{x}/{y}", response_class=Response)
def tile(
        z: int,
        x: int,
        y: int,
        url: str = Query(description="Zarr URL"),
        variable: str = Query(description="Zarr Variable"),
        idx: int = Query(description="Time index")
):
    with xarray.open_dataset(url, engine="zarr", decode_coords="all") as src:
        ds = src.isel(time=[idx])[variable][:1]
        # Make sure we are a CRS
        crs = ds.rio.crs or "epsg:4326"
        ds.rio.write_crs(crs, inplace=True)

        with XarrayReader(ds) as dst:
            img = dst.tile(x, y, z)
            img.rescale(
                in_range=((260, 320),),
                out_range=((-20, 255),)
            )
        content = img.render(colormap=cm)
        return Response(content, media_type="image/png")


@app.get(
    "/tilejson.json",
    response_model=TileJSON,
    responses={200: {"description": "Return a tilejson"}},
    response_model_exclude_none=True,
    tags=["API"],
)
def tilejson(
        request: Request,
        url: str = Query(description="Zarr URL"),
        variable: str = Query(description="Zarr Variable"),
        idx: int = Query(description="Time index")
):
    """Handle /tilejson.json requests."""
    kwargs: Dict[str, Any] = {"z": "{z}", "x": "{x}", "y": "{y}"}

    tile_url = request.url_for("tile", **kwargs)

    qs = [
        (key, value)
        for (key, value) in request.query_params._list
        if key not in ["tile_format"]
    ]
    if qs:
        tile_url += f"?{urllib.parse.urlencode(qs)}"

    with xarray.open_dataset(url, engine="zarr", decode_coords="all") as src:
        ds = src.isel(time=[idx])[variable][:1]
        # Make sure we are a CRS
        crs = ds.rio.crs or "epsg:4326"
        ds.rio.write_crs(crs, inplace=True)

        with XarrayReader(ds) as dst:
            return dict(
                bounds=dst.geographic_bounds,
                minzoom=dst.minzoom,
                maxzoom=dst.maxzoom,
                name="xarray",
                tilejson="2.1.0",
                tiles=[tile_url],
            )


###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################

handler = Mangum(app)

###############################################################################
#   Run the self contained application                                        #
###############################################################################

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
