
`rio-tiler` aims to be a lightweight plugin for `rasterio` whose sole goal is to
read a Mercator Tile from a raster dataset.

Given that `rio-tiler` allows for simple, efficient reading of tiles, you can
then leverage `rio-tiler` to create a **dynamic tile server** to display raster
tiles on a web map.

There are couple tile servers built on top of rio-tiler:

- [`titiler`](https://github.com/developmentseed/titiler)
- [`cogeo-tiler`](https://github.com/developmentseed/cogeo-tiler)
- [`cogeo-mosaic-tiler`](https://github.com/developmentseed/cogeo-mosaic-tiler)
- [`rio-viz`](https://github.com/developmentseed/rio-viz)

## Example Application

To build a simple dynamic tiling application, we can use
[FastAPI](https://github.com/tiangolo/fastapi). Note that `titiler` uses
`FastAPI` internally, so you might consider using `titiler` instead of making
your own API.

### Requirements

- `rio-tiler ~= 2.0b`
- `fastapi`
- `uvicorn`

Install with

```bash
pip install fastapi uvicorn 'rio-tiler~=2.0b'
```

### `app.py`

```python
"""rio-tiler tile server."""

import os
from enum import Enum
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

import uvicorn
from fastapi import FastAPI, Path, Query
from rasterio.crs import CRS
from starlette.background import BackgroundTask
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import Response

from rio_tiler.profiles import img_profiles
from rio_tiler.utils import render
from rio_tiler.io import COGReader

# From developmentseed/titiler
drivers = dict(jpg="JPEG", png="PNG")
mimetype = dict(png="image/png", jpg="image/jpg",)

class ImageType(str, Enum):
    """Image Type Enums."""

    png = "png"
    jpg = "jpg"



class TileResponse(Response):
    """Tiler's response."""

    def __init__(
        self,
        content: bytes,
        media_type: str,
        status_code: int = 200,
        headers: dict = {},
        background: BackgroundTask = None,
        ttl: int = 3600,
    ) -> None:
        """Init tiler response."""
        headers.update({"Content-Type": media_type})
        if ttl:
            headers.update({"Cache-Control": "max-age=3600"})
        self.body = self.render(content)
        self.status_code = 200
        self.media_type = media_type
        self.background = background
        self.init_headers(headers)


app = FastAPI(
    title="rio-tiler",
    description="A lightweight Cloud Optimized GeoTIFF tile server",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=0)

responses = {
    200: {
        "content": {"image/png": {}, "image/jpg": {}},
        "description": "Return an image.",
    }
}
tile_routes_params: Dict[str, Any] = dict(
    responses=responses, tags=["tiles"], response_class=TileResponse
)


@app.get("/{z}/{x}/{y}", **tile_routes_params)
def tile(
    z: int,
    x: int,
    y: int,
    url: str = Query(..., description="Cloud Optimized GeoTIFF URL."),
):
    """Handle tiles requests."""
    with COGReader(url) as cog:
        tile, mask = cog.tile(x, y, z, tilesize=256)

    format = ImageType.jpg if mask.all() else ImageType.png

    driver = drivers[format.value]
    options = img_profiles.get(driver.lower(), {})
    img = render(tile, mask, img_format=driver, **options)

    return TileResponse(img, media_type=mimetype[format.value])


@app.get("/tilejson.json", responses={200: {"description": "Return a tilejson"}})
def tilejson(
    request: Request,
    url: str = Query(..., description="Cloud Optimized GeoTIFF URL."),
    minzoom: Optional[int] = Query(None, description="Overwrite default minzoom."),
    maxzoom: Optional[int] = Query(None, description="Overwrite default maxzoom."),
):
    """Return TileJSON document for a COG."""
    tile_url = request.url_for("tile", {"z": "{z}", "x": "{x}", "y": "{y}"}).replace("\\", "")

    kwargs = dict(request.query_params)
    kwargs.pop("tile_format", None)
    kwargs.pop("tile_scale", None)
    kwargs.pop("minzoom", None)
    kwargs.pop("maxzoom", None)

    qs = urlencode(list(kwargs.items()))
    tile_url = f"{tile_url}?{qs}"

    with COGReader(url) as cog:
        center = list(cog.center)
        if minzoom:
            center[-1] = minzoom
        tjson = {
            "bounds": cog.bounds,
            "center": tuple(center),
            "minzoom": minzoom or cog.minzoom,
            "maxzoom": maxzoom or cog.maxzoom,
            "name": os.path.basename(url),
            "tiles": [tile_url],
        }

    return tjson
```

## Launch Example

Use `uvicorn` to launch the application. Note that `app:app` tells `uvicorn` to
call the `app` function within `app.py`, so you must be in the same directory as
`app.py`.

```
uvicorn app:app --reload
```

## Create an AWS Lambda package

The easiest way to make sure the package will work on AWS is to use docker

```dockerfile
FROM lambci/lambda:build-python3.7

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 CFLAGS="--std=c99"

RUN pip3 install rio-tiler --no-binary numpy -t /tmp/python -U

RUN cd /tmp/python && zip -r9q /tmp/package.zip *
```

Ref: https://github.com/vincentsarago/simple-rio-lambda

