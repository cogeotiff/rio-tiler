
# Breaking changes

`rio-tiler` version 4.0 introduced [many breaking changes](release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 4.0.

## Python >=3.8

As for rasterio, we removed python 3.7 support (https://github.com/rasterio/rasterio/issues/2445)

## *COG*Reader -> **Reader**

Because the main reader will not only work with COG but most of GDAL supported raster, we choose to rename it to `Reader`.

```python
# before
from rio_tiler.io import COGReader
from rio_tiler.io.cogeo import COGReader

# now
from rio_tiler.io import Reader
from rio_tiler.io.rasterio import Reader
```

Note: We created `rio_tiler.io.COGReader` alias to `Reader` for compatibility.

## rio_tiler.io.cogeo -> rio_tiler.io.**rasterio**

Reader's submodule now reflect the backend they use (rasterio, xarray, stac, ...)

```python
# before
from rio_tiler.io.cogeo import COGReader

# now
from rio_tiler.io.rasterio import Reader
```

## **Band names**

Band names are now prefixed with `b` (e.g `b1`, `b2`)

```python
# before
with COGReader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as src:
    stats = src.statistics()
   print(list(stats))
   >>> ["1", "2", "3"]

    info = src.info()
    print(info.band_metadata)
    >>> [("1", {}), ("2", {}), ("3", {})]

    print(info.band_descriptions)
    >>> [("1", ""), ("2", ""), ("3", "")]

# now
with Reader(
  "http://oin-hotosm.s3.amazonaws.com/5a95f32c2553e6000ce5ad2e/0/10edab38-1bdd-4c06-b83d-6e10ac532b7d.tif"
) as src:
    stats = src.statistics()
    print(list(stats))
    >>> ["b1", "b2", "b3"]

    info = src.info()
    print(info.band_metadata)
    >>> [("b1", {}), ("b2", {}), ("b3", {})]

    print(info.band_descriptions)
    >>> [("b1", ""), ("b2", ""), ("b3", "")]
```

## MultiBaseReader **Expressions**

We updated the `expression` format for `MultiBaseReader` (e.g STAC) to include **band names** and not only the asset name

```python
# before
with STACReader("stac.json") as stac:
    stac.tile(701, 102, 8, expression="green/red")

# now
with STACReader("stac.json") as stac:
    stac.tile(701, 102, 8, expression="green_b1/red_b1")
```

In addition we also removed `asset_expression` option in `MultiBaseReader`. This can be achieved directly using expression.

```python
# before
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        assets=["B01", "B02"],
        asset_expression={
            "B01": "b1+500",  # add 500 to the first band
            "B02": "b1-100",  # substract 100 to the first band
        }
    )

# now
with STACReader(stac_url, exclude_assets={"thumbnail"},) as stac:
    img = stac.tile(
        145,
        103,
        8,
        tilesize=256,
        expression="B01_b1+500;B02_b1-100",
    )
```

## No more GCPCOGReader

`rio_tiler.io.Reader` will now recognize if the files has internal GCPS.

```python
# before
from rio_tiler.io import GCPCOGReader

with GCPCOGReader("my_tif_with_gcps.tif") as src:
    pass

# now
from rio_tiler.io import Reader

with Reader("my_tif_with_gcps.tif") as src:
    pass
```

## **PointData** object

As for method returning `images`, methods returning point values (`Reader.point()`) now return a `PointData` object.

```python
# before
with COGReader("cog.tif") as cog:
    print(cog.point(10.20, -42.0))
    >>> [0, 0, 0]

# now
with Reader("cog.tif") as cog:
    print(cog.point(10.20, -42.0))
    >>> PointData(
        data=array([3744], dtype=uint16),
        mask=array([255], dtype=uint8),
        band_names=['b1'],
        coordinates=(10.20, -42),
        crs=CRS.from_epsg(4326),
        assets=['cog.tif'],
        metadata={}
    )
```

## Low-level reader methods return ImageData and PointData objects

`rio_tiler.reader.read` and `rio_tiler.readers.part` now return `ImageData` object instead of `Tuple[ndarray, ndarray]`.

```python
from rio_tiler.reader import read, part, point
from rio_tiler.models import ImageData, PointData

# before
with rasterio.open("image.tif") as src:
    data, mask = read(src)
    pts = point(10.20, -42.0)
    print(pts)
    >>> [0, 0, 0]

# now
with rasterio.open("image.tif") as src:
    img = read(src)
    assert isinstance(img, ImageData)

    pts = point(src, (10.20, -42.0))
    assert isinstance(pts, PointData)
    print(pts)
    >>> PointData(
        data=array([3744], dtype=uint16),
        mask=array([255], dtype=uint8),
        band_names=['b1'],
        coordinates=(10.20, -42),
        crs=CRS.from_epsg(4326),
        assets=['cog.tif'],
        metadata={}
    )
```

## **Reader** options

We removed `nodata`, `unscale`, `resampling_method`, `vrt_options` and `post_process` options to `rio_tiler.io.Reader` init method and replaced with a global `options`:
```python
# before
with COGReader("cog.tif", nodata=1, resampling_method="bilinear") as cog:
    data = cog.preview()

# now
with Reader(COGEO, options={"nodata": 1, "resampling_method": "bilinear"}) as cog:
    data = cog.preview()
```

## Base classes **minzoom** and **maxzoom**

We moved min/max zoom attribute from the `SpatialMixin` to the base classes definition directly. This means that each class should now take care of the definition of those two variables.

```python
# before
@attr.s
class BandFileReader(MultiBandReader):
    """Test MultiBand"""

    input: str = attr.ib()
    tms: morecantile.TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: Type[BaseReader] = attr.ib(init=False, default=Reader)
    reader_options: Dict = attr.ib(factory=dict)

    def __attrs_post_init__(self):
        ...

# now
@attr.s
class BandFileReader(MultiBandReader):
    """Test MultiBand"""

    input: str = attr.ib()
    tms: morecantile.TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    reader: Type[BaseReader] = attr.ib(init=False, default=Reader)
    reader_options: Dict = attr.ib(factory=dict)

    minzoom: int = attr.ib()
    maxzoom: int = attr.ib()

    @minzoom.default
    def _minzoom(self):
        return self.tms.minzoom

    @maxzoom.default
    def _maxzoom(self):
        return self.tms.maxzoom

    def __attrs_post_init__(self):
        ...
```

# New Features

## Non-Geo reader

Because not all raster are geo-referenced, we added `rio_tiler.io.ImageReader` to allow opening and reading non-geo images. All methods are returning data in the pixel coordinate system.

```python
with ImageReader("image.jpg") as src:
    info = src.info()

    stats = src.statistics()

    # Part of the image (Origin is top-lef, coordinates should be in form of (left, bottom, right, top))
    im = src.part((0, 100, 100, 0))

    # 256x256 Tile (Origin of the TMS is top-lef)
    im = src.tile(0, 0, src.maxzoom)

    # read pixel x=10, y=5 (Origin is top-left)
    pt = src.point(10, 5)
```

## Xarray reader

We added an *optional* xarray compatible reader in rio-tiler v4.0. The reader takes a xarray.DataArray as input which should have a CRS and geo-spatial variables (x,y or longitude,latitude).

```python
import rioxarray
import xarray
from rio_tiler.io import XarrayReader

with xarray.open_dataset(
    "https://ncsa.osn.xsede.org/Pangeo/pangeo-forge/noaa-coastwatch-geopolar-sst-feedstock/noaa-coastwatch-geopolar-sst.zarr",
    engine="zarr",
    decode_coords="all"
) as src:
    ds = src["analysed_sst"][:1]
    # the SST dataset do not have a CRS info
    # so we need to add it to `virtualy` within the Xarray DataArray
    ds.rio.write_crs("epsg:4326", inplace=True)

    with XarrayReader(ds) as dst:
        print(dst.info())
        img = dst.tile(1, 1, 2)
```

Note: Users might experience some really bad performance depending on the chunking of the original zarr.

## Dataset Statistics

Starting with rio-tiler 4.0, if the input dataset has [`statistics`](https://gdal.org/user/raster_data_model.html#raster-band) (e.g `STATISTICS_MINIMUM`, `STATISTICS_MAXIMUM`) within its metadata, rio-tiler will try to use it to rescale automatically the output image.

```python
from rio_tiler.io import Reader

with Reader("https://data.geo.admin.ch/ch.swisstopo.swissalti3d/swissalti3d_2019_2573-1085/swissalti3d_2019_2573-1085_0.5_2056_5728.tif") as src:
    info = src.info()
    print(info.band_metadata)
    >>> [('b1',
    {'STATISTICS_COVARIANCES': '10685.98787505646',
    'STATISTICS_EXCLUDEDVALUES': '-9999',
    'STATISTICS_MAXIMUM': '2015.0944824219',
    'STATISTICS_MEAN': '1754.471184271',
    'STATISTICS_MINIMUM': '1615.8128662109',
    'STATISTICS_SKIPFACTORX': '1',
    'STATISTICS_SKIPFACTORY': '1',
    'STATISTICS_STDDEV': '103.37305197708'})]

    img = src.preview()
    # The min/max statistics are saved within every output image object
    print(img.dataset_statistics)
    >>> [(1615.8128662109, 2015.0944824219)]

    buffer = img.render()
    >>> rio-tiler/rio_tiler/models.py:516: InvalidDatatypeWarning: Invalid type: `float32` for the `PNG` driver. Data will be rescaled using min/max type bounds  or dataset_statistics.
```
