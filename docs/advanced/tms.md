
Starting with rio-tiler 2.0, we replaced [mercantile](https://github.com/mapbox/mercantile) dependencie with [**morecantile**](https://github.com/developmentseed/morecantile). Mercantile was used to work with the Web Mercator [**TileMatrixSet**](http://docs.opengeospatial.org/is/17-083r2/17-083r2.html) and helps to define the bounding box (in web mercator projection) for each Tile.

In version 2.0 we are expanding the capabilities of rio-tiler to work with different TileMatrixSet by using **Morecantile** which was specifically designed to work with pre-defined and user-defined **TMS**.

```python
import morecantile
from morecantile import tms
from rio_tiler.io import COGReader

# By default we use WebMercator TMS
with COGReader("my.tif") as cog:
    data, mask = cog.tile(1, 1, 1)

# Print default grids
print(tms.list())
>>> [
    'LINZAntarticaMapTilegrid',
    'EuropeanETRS89_LAEAQuad',
    'CanadianNAD83_LCC',
    'UPSArcticWGS84Quad',
    'NZTM2000',
    'UTM31WGS84Quad',
    'UPSAntarcticWGS84Quad',
    'WorldMercatorWGS84Quad',
    'WorldCRS84Quad',
    'WebMercatorQuad'
]

# Use EPSG:4326 (WGS84) grid
epsg43326TMS = tms.get("WorldCRS84Quad")
with COGReader("my.tif", tms=epsg43326TMS) as cog:
    data, mask = cog.tile(1, 1, 1)

# Create Custom grid
crs = CRS.from_epsg(3031)
extent = [-948.75, -543592.47, 5817.41, -3333128.95]  # From https:///epsg.io/3031
epsg3031TMS = morecantile.TileMatrixSet.custom(extent, crs, identifier="MyCustomTmsEPSG3031")

with COGReader("my.tif", tms=epsg3031TMS) as cog:
    data, mask = cog.tile(1, 1, 1)
```
