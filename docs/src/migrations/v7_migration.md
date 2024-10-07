
`rio-tiler` version 7.0 introduced [many breaking changes](../release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 7.0.

## `SpatialMixin` class and `TMS`

The `SpatialMixin` class, used in `BaseReader` class had numerous breaking changes:

- removed `tms` and `geographic_crs` attributes

- changed `geographic_bounds(self)` from `property` to `method` -> `geographic_bounds(self, geographic_crs: CRS = WGS84_CRS)`

- removed `_dst_geom_in_tms_crs` method

- removed `_minzoom` and `_maxzoom` property

The main change is the removal of the `tms` attribute, which means the `BaseReader` do not have `tms` information, thus the `.tile()` now needs a tms argument:

```python
# before
import morecantile
from rio_tiler.io import Reader

with Reader("cog.tif", tms=morecantile.tms.get("WebMercatorQuad")) as src:
    _ = src.tile(0, 0, 0)

# now
with Reader("cog.tif") as src:
    _ = src.tile(0, 0, 0, tms=morecantile.tms.get("WebMercatorQuad"))
```

same for the `tile_exists` method

```python
# before
import morecantile
from rio_tiler.io import Reader

with Reader("cog.tif", tms=morecantile.tms.get("WebMercatorQuad")) as src:
    _ = src.tile_exists(0, 0, 0)

# now
with Reader("cog.tif") as src:
    _ = src.tile_exists(0, 0, 0, tms=morecantile.tms.get("WebMercatorQuad"))
```

By removing the `tms` attribute, we also removed the `min/max zoom` properties. We've added `.get_zooms(tms: TileMatrixSet)` method to the `SpatialMixin` class to allow users to retrieve the zoom information:

```python
# before
import morecantile
from rio_tiler.io import Reader

with Reader("cog.tif", tms=morecantile.tms.get("WebMercatorQuad")) as src:
    minzoom, maxzoom = src.minzoom, src.maxzoom

# now
with Reader("cog.tif") as src:
    minzoom, maxzoom = src.get_zooms(morecantile.tms.get("WebMercatorQuad"))
```

Same for the `geographic_bounds`, which now needs to be retrieved using the `geographic_bounds(tms: TileMatrixSet)` method (instead of the `.geographic_bounds` property), because we've removed the `geographic_crs` attribute.

```python
# before
from rasterio.crs import CRS
from rio_tiler.io import Reader

with Reader("cog.tif", geographic_crs=CRS.from_epsg(4326)) as src:
    _ = src.geographic_bounds

# now
with Reader("cog.tif") as src:
    _ = src.geographic_bounds(CRS.from_epsg(4326))
```


## `Info()` and Models

- `rio_tiler.models.SpatialInfo` was removed
