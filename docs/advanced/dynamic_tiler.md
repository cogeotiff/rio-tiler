
`rio-tiler` aims to be a lightweight plugin for `rasterio` to read [slippy map
tiles](https://en.wikipedia.org/wiki/Tiled_web_map) from a raster sources.

Given that `rio-tiler` allows for simple, efficient reading of tiles, you can
then leverage `rio-tiler` to create a **dynamic tile server** to display raster
tiles on a web map.

There are couple tile servers built on top of rio-tiler:

- [`titiler`](https://github.com/developmentseed/titiler)
- [`rio-viz`](https://github.com/developmentseed/rio-viz)

## Example Application

To build a simple dynamic tiling application, we can use
[FastAPI](https://github.com/tiangolo/fastapi). Note that `titiler` uses
`FastAPI` internally, so you might consider using `titiler` instead of making
your own API.

### Requirements

- `rio-tiler ~= 2.0`
- `fastapi`
- `uvicorn`

Install with

```bash
pip install fastapi uvicorn rio-tiler
```

### `app.py`

```python
"""rio-tiler tile server."""

import os
from enum import Enum
from typing import Any, Dict, List, Optional
from types import DynamicClassAttribute

from urllib.parse import urlencode

import uvicorn
from fastapi import FastAPI, Path, Query
from rasterio.crs import CRS
from starlette.requests import Request
from starlette.responses import Response

from rio_tiler.profiles import img_profiles
from rio_tiler.io import COGReader


app = FastAPI(
    title="rio-tiler",
    description="A lightweight Cloud Optimized GeoTIFF tile server",
)


@app.get(
    r"/{z}/{x}/{y}.png",
    responses={
        200: {
            "content": {"image/png": {}}, "description": "Return an image.",
        }
    },
    response_class=ImageResponse,
    description="Read COG and return a tile",
)
def tile(
    z: int,
    x: int,
    y: int,
    url: str = Query(..., description="Cloud Optimized GeoTIFF URL."),
):
    """Handle tile requests."""
    with COGReader(url) as cog:
        img = cog.tile(x, y, z, tilesize=256)
    content = img.render(img_format="PNG", **img_profiles.get("png"))
    return Response(content, media_type="image/png")


@app.get("/tilejson.json", responses={200: {"description": "Return a tilejson"}})
def tilejson(
    request: Request,
    url: str = Query(..., description="Cloud Optimized GeoTIFF URL."),
):
    """Return TileJSON document for a COG."""
    tile_url = request.url_for("tile", {"z": "{z}", "x": "{x}", "y": "{y}"})
    tile_url = f"{tile_url}?url={url}"

    with COGReader(url) as cog:
        return {
            "bounds": cog.bounds,
            "center": cog.center,
            "minzoom": cog.minzoom,
            "maxzoom": cog.maxzoom,
            "name": os.path.basename(url),
            "tiles": [tile_url],
        }
```

## Launch Example

Use `uvicorn` to launch the application. Note that `app:app` tells `uvicorn` to
call the `app` function within `app.py`, so you must be in the same directory as
`app.py`.

```
uvicorn app:app --reload
```
