
Starting with rio-tiler 2.0, we replaced [`mercantile`][mercantile] with [_`morecantile`_][morecantile], enabling support for other [**TileMatrixSets**](http://docs.opengeospatial.org/is/17-083r2/17-083r2.html) than the default WebMercator grid.

[mercantile]: https://github.com/mapbox/mercantile
[morecantile]: https://github.com/developmentseed/morecantile

```python
import morecantile
from rio_tiler.io import COGReader
from rasterio.crs import CRS

# By default we use WebMercator TMS
with COGReader("my.tif") as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(3857)  # default is always WebMercator

# Print default grids
for name, tms in morecantile.tms.tms.items():
    print(name, "-", tms.crs)

>>> LINZAntarticaMapTilegrid - EPSG:5482
    EuropeanETRS89_LAEAQuad - EPSG:3035
    CanadianNAD83_LCC - EPSG:3978
    UPSArcticWGS84Quad - EPSG:5041
    NZTM2000 - EPSG:2193
    UTM31WGS84Quad - EPSG:32631
    UPSAntarcticWGS84Quad - EPSG:5042
    WorldMercatorWGS84Quad - EPSG:3395
    WorldCRS84Quad - EPSG:4326
    WebMercatorQuad - EPSG:3857


# Use EPSG:4326 (WGS84) grid
wgs84_grid = morecantile.tms.get("WorldCRS84Quad")
with COGReader("my.tif", tms=wgs84_grid) as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(4326)

# Create Custom grid
extent = [-948.75, -543592.47, 5817.41, -3333128.95]  # From https:///epsg.io/3031
epsg3031TMS = morecantile.TileMatrixSet.custom(
    extent, CRS.from_epsg(3031), identifier="MyCustomTmsEPSG3031"
)
with COGReader("my.tif", tms=epsg3031TMS) as cog:
    img = cog.tile(1, 1, 1)
    assert img.crs == CRS.from_epsg(3031)
```
