
Starting with rio-tiler **8.0**, we've added a `Mosaic Backend` (originally hosted in defined in [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic)). The backend is an Abstract Base Class built on top of the `BaseReader` abstrac base class.

To construct your own mosaic backend, you'll need to write three methods: `assets_for_tile`, `assets_for_point` and `assets_for_bbox`.

### **rio_tiler.mosaic.backend.BaseBackend**

##### Arguments

- **input** (Any): Input.
- **tms** (morecantile.TileMatrixSet): The TileMatrixSet define which default projection and map grid the reader uses. Defaults to WebMercatorQuad
- **reader** (BaseReader, optional): Reader to use to read assets (defaults to rio_tiler.io.rasterio.Reader)
- **reader_options** (dict, optional): Options to forward to the reader init
- **bounds: BBox**: Mosaic's bounding box. Not in the `__init__` method
- **crs: CRS**: Mosaic's crs. Not in the `__init__` method
- **minzoom** (int, optional): dataset's minimum zoom level (for input tms). Not in the `__init__` method
- **maxzoom** (int, optional): dataset's maximum zoom level (for input tms). Not in the `__init__` method

!!! important
    BaseClass Arguments outside the `__init__` method and without default value **HAVE TO** be set in the `__attrs_post_init__` step.

##### Abstract Methods

Abstract methods, are method that **HAVE TO** be implemented in the child class.

- **assets_for_tile(x, z, z, \*\*kwargs)**: returns list of assets for a specifi tiles
- **assets_for_point(lng, lat, coord_crs, \*\*kwargs)**: returns list of assets for a specifi lon/lat coordinates
- **assets_for_bbox(xmin, ymin, xmax, ymax, coord_crs, \*\*kwargs)**:: returns list of assets for a specifi bounding box

##### Methods 

- **asset_name(asset: Any) -> str**: returns asset name (usefull if assets are not of type string, e.g Dict)
- **info() -> MosaicInfo**: returns Mosaic Info
- **point(lon: float, lat: float, coord_crs: CRS, search_options: dict | None, \*\*kwargs) -> list[PointData]**: returns list of PointData for all assets
- **tile(x: int, y: int, z: int, search_options: dict | None, \*\*kwargs) -> ImageData**: creates ImageData from multiple assets for a specific TMS tile
- **part(bbox: BBox, bounds_crs: CRS, search_options: dict | None, \*\*kwargs) -> ImageData**: creates ImageData from multiple assets for a specific Bounding Box
- **feature(shape: dict, shape_crs: CRS, search_options: dict | None, \*\*kwargs) -> ImageData**: creates ImageData from multiple assets for a specific GeoJSON shape
- **statistics()**: NotImplemented
- **preview()**: NotImplemented


### Example: STAC API Backend

**requirements**: rio-tiler>=8.0, geojson_pydantic, pystac-client

```python
from typing import Set, Sequence,Type

import attr
import pystac
from pystac_client import ItemSearch
from rio_tiler.io import BaseReader, Reader, STACReader
from rio_tiler.io.stac import DEFAULT_VALID_TYPE
from rio_tiler.mosaic.backend import BaseBackend
from rio_tiler.types import BBox
from rio_tiler.constants import WEB_MERCATOR_TMS, WGS84_CRS
import rasterio
from rasterio.transform import array_bounds
from rasterio.warp import transform, transform_bounds
from morecantile import TileMatrixSet
from rio_tiler.errors import MissingAssets
from geojson_pydantic import Point, Polygon
from geojson_pydantic.geometries import Geometry


# Custom STACReader which accept pystac.Item as input
@attr.s
class PySTACReader(STACReader):
    input: pystac.Item  = attr.ib()

    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    include_assets: Set[str] | None = attr.ib(default=None)
    exclude_assets: Set[str] | None = attr.ib(default=None)

    include_asset_types: Set[str] = attr.ib(default=DEFAULT_VALID_TYPE)
    exclude_asset_types:  Set[str] | None = attr.ib(default=None)

    assets: Sequence[str] = attr.ib(init=False)
    default_assets: Sequence[str] | None = attr.ib(default=None)

    reader: Type[BaseReader] = attr.ib(default=Reader)
    reader_options: dict = attr.ib(factory=dict)

    fetch_options: dict = attr.ib(factory=dict)

    ctx: rasterio.Env = attr.ib(default=rasterio.Env)

    item: pystac.Item = attr.ib(init=False)

    def __attrs_post_init__(self):
        """Fetch STAC Item and get list of valid assets."""
        self.item = self.input

        self.bounds = tuple(self.item.bbox)
        self.crs = WGS84_CRS

        if hasattr(self.item, "ext") and self.item.ext.has("proj"):
            if all(
                [
                    self.item.ext.proj.transform,
                    self.item.ext.proj.shape,
                    self.item.ext.proj.crs_string,
                ]
            ):
                self.height, self.width = self.item.ext.proj.shape
                self.transform = Affine(*self.item.ext.proj.transform)
                self.bounds = array_bounds(self.height, self.width, self.transform)
                self.crs = rasterio.crs.CRS.from_string(self.item.ext.proj.crs_string)

        self.minzoom = self.minzoom if self.minzoom is not None else self._minzoom
        self.maxzoom = self.maxzoom if self.maxzoom is not None else self._maxzoom

        self.assets = self.get_asset_list()
        if not self.assets:
            raise MissingAssets("No valid asset found. Asset's media types not supported")


# Custom STACAPI Backend
@attr.s
class Backend(BaseBackend):
    """Test Backend implementation."""

    # STAC API URL
    input: list[str] = attr.ib()
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: Type[PySTACReader] = attr.ib(default=PySTACReader)
    reader_options: dict = attr.ib(factory=dict)

    bounds: BBox = attr.ib(init=False)
    crs: rasterio.crs.CRS = attr.ib(init=False)

    minzoom: int = attr.ib(init=False)
    maxzoom: int = attr.ib(init=False)

    def __attrs_post_init__(self):
        """Post Init."""
        self.bounds = (-180., -90., 180., 90.)
        self.crs = rasterio.crs.CRS.from_epsg(4326)
        self.minzoom = self.tms.minzoom
        self.maxzoom = self.tms.maxzoom

    def asset_name(self, asset: pystac.Item) -> str:
        """Get asset name."""
        return f"{asset.collection_id}_{asset.id}"

    def get_assets(
        self,
        geom: Geometry,
        search_query: Optional[Dict] = None,
        fields: Optional[List[str]] = None,
    ) -> List[pystac.Item]:
        """Find assets."""
        search_query = search_query or {}
        params = {
            **search_query,
            "intersects": geom.model_dump_json(exclude_none=True),
        }
        params.pop("bbox", None)

        results = ItemSearch(f"{self.input}/search", **params)
        return list(results.items())    
    
    def assets_for_tile(self, x: int, y: int, z: int, **kwargs: Any) -> List[Dict]:
        """Retrieve assets for tile."""
        bbox = self.tms.bounds(x, y, z)
        return self.get_assets(Polygon.from_bounds(*bbox), **kwargs)

    def assets_for_point(
        self,
        lng: float,
        lat: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> List[Dict]:
        """Retrieve assets for point."""
        if coord_crs != WGS84_CRS:
            xs, ys = transform(coord_crs, WGS84_CRS, [lng], [lat])
            lng, lat = xs[0], ys[0]

        return self.get_assets(Point(type="Point", coordinates=(lng, lat)), **kwargs)

    def assets_for_bbox(
        self,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        coord_crs: CRS = WGS84_CRS,
        **kwargs: Any,
    ) -> List[Dict]:
        """Retrieve assets for bbox."""
        if coord_crs != WGS84_CRS:
            xmin, ymin, xmax, ymax = transform_bounds(
                coord_crs,
                WGS84_CRS,
                xmin,
                ymin,
                xmax,
                ymax,
            )

        return self.get_assets(Polygon.from_bounds(xmin, ymin, xmax, ymax), **kwargs)
```

###### Usage

```python
# Find asset for a specific Point
with Backend("https://stac.eoapi.dev") as mosaic:
    assets = mosaic.assets_for_point(
        -113.914, 
        50.886, 
        search_query={"collections": "sentinel2-temporal-mosaics"},
    )
    print(assets)
    >> [<Item id=11UQS_2023-01-01_2024-01-01>, <Item id=11UQS_2022-01-01_2023-01-01>]

# Create Tile Image for `sentinel2-temporal-mosaics` collection
with Backend("https://stac.eoapi.dev") as mosaic:
    img, asset_used = mosaic.tile(
        187,
        343,
        10,
        # Options forwarded to the STACReader (MultiBaseReader)
        assets=["B01"],
        asset_as_band=True,
        # Option forwared to the `assets_for_tile` method
        search_options={
            "search_query": {"collections": "sentinel2-temporal-mosaics"},
        }
    )
    print(img.assets)
    >>[<Item id=11UQS_2023-01-01_2024-01-01>, <Item id=11UPS_2023-01-01_2024-01-01>]

    print(asset_used)
    >> [
        'sentinel2-temporal-mosaics_11UQS_2023-01-01_2024-01-01',
        'sentinel2-temporal-mosaics_11UPS_2023-01-01_2024-01-01',
    ]

    print(img.band_descriptions)
    >> ['B01'] 

    print(img.band_names)
    >> ['B01']
```