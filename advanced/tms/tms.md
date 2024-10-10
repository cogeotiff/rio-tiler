
Starting with rio-tiler 2.0, we replaced [`mercantile`][mercantile] with [_`morecantile`_][morecantile], enabling support for other [**TileMatrixSets**](http://docs.opengeospatial.org/is/17-083r2/17-083r2.html) than the default WebMercator grid.

[mercantile]: https://github.com/mapbox/mercantile
[morecantile]: https://github.com/developmentseed/morecantile

```python
import morecantile
from rio_tiler.io import Reader
from rasterio.crs import CRS
from pyproj import CRS as projCRS

# By default we use WebMercator TMS
with Reader("my.tif") as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(3857)  # default image output is the TMS crs (WebMercator)

# Print default grids
for name in morecantile.tms.list():
    print(name, "-", morecantile.tms.get(name).rasterio_crs)

>>> CanadianNAD83_LCC - EPSG:3978
    EuropeanETRS89_LAEAQuad - EPSG:3035
    LINZAntarticaMapTilegrid - EPSG:5482
    NZTM2000Quad - EPSG:2193
    UPSAntarcticWGS84Quad - EPSG:5042
    UPSArcticWGS84Quad - EPSG:5041
    UTM31WGS84Quad - EPSG:32631
    WGS1984Quad - EPSG:4326
    WebMercatorQuad - EPSG:3857
    WorldCRS84Quad - OGC:CRS84
    WorldMercatorWGS84Quad - EPSG:3395


# Use EPSG:4326 (WGS84) grid
wgs84_grid = morecantile.tms.get("WorldCRS84Quad")
with Reader("my.tif", tms=wgs84_grid) as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(4326)

# Create Custom grid
extent = [-948.75, -543592.47, 5817.41, -3333128.95]  # From https:///epsg.io/3031
epsg3031TMS = morecantile.TileMatrixSet.custom(
    extent, projCRS.from_epsg(3031), identifier="MyCustomTmsEPSG3031"
)
with Reader("my.tif", tms=epsg3031TMS) as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(3031)
```
