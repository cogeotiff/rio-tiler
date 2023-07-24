
`rio-tiler` provides multiple [abstract base
classes](https://docs.python.org/3.7/library/abc.html) from which it derives its
main readers: [`Reader`](../readers.md#reader) and
[`STACReader`](../readers.md#stacreader). You can also use these classes to build
custom readers.

## Abstract Base Classes

### **BaseReader**

Main `rio_tiler.io` Abstract Base Class.

##### Minimal Arguments

- **input**: Input
- **tms**: The TileMatrixSet define which default projection and map grid the reader uses. Defaults to WebMercatorQuad.

- **bounds**: Dataset's bounding box. Not in the `__init__` method.
- **crs**: dataset's crs. Not in the `__init__` method.
- **geographic_crs**: CRS to use as geographic coordinate system. Defaults to WGS84. Not in the `__init__` method.

!!! important
    BaseClass Arguments outside the `__init__` method and without default value **HAVE TO** be set in the `__attrs_post_init__` step.

#### Methods

- **tile_exists**: Check if a given tile (for the input TMS) intersect the dataset bounds.

##### Properties

- **geographic_bounds**: dataset's bounds in WGS84 crs (calculated from `self.bounds` and `self.crs`).

##### Abstract Methods

Abstract methods, are method that **HAVE TO** be implemented in the child class.

- **info**: returns dataset info (`rio_tiler.models.Info`)
- **statistics**: returns dataset band statistics (`Dict[str, rio_tiler.models.BandStatistics]`)
- **tile**: reads data for a specific XYZ slippy map indexes (`rio_tiler.models.ImageData`)
- **part**: reads specific part of a dataset (`rio_tiler.models.ImageData`)
- **preview**: creates an overview of a dataset (`rio_tiler.models.ImageData`)
- **point**: reads pixel value for a specific point (`List`)
- **feature**: reads data for a geojson feature (`rio_tiler.models.ImageData`)

Example: [`Reader`](../readers.md#reader)

### **MultiBaseReader**

The goal of the `MultiBaseReader` is to enable joining results from multiple files (e.g STAC).

The `MultiBaseReader` has the same attributes/properties/methods as the `BaseReader`.

Example: [`STACReader`](../readers.md#stacreader)

```python
import os
import pathlib
from typing import Dict, Type

import attr
from morecantile import TileMatrixSet
from rio_tiler.io.base import MultiBaseReader
from rio_tiler.io import Reader, BaseReader
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.models import Info

@attr.s
class AssetFileReader(MultiBaseReader):

    input: str = attr.ib()
    prefix: str = attr.ib() # we add a custom attribute

    # because we add another attribute (prefix) we need to
    # re-specify the other attribute for the class
    reader: Type[BaseReader] = attr.ib(default=Reader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # we place min/max zoom in __init__
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.assets = sorted(
            [p.stem.split("_")[1] for p in pathlib.Path(self.input).glob(f"*{self.prefix}*.tif")]
        )
        with self.reader(self._get_asset_url(self.assets[0])) as cog:
            self.bounds = cog.bounds
            self.crs = cog.crs

            if self.minzoom is None:
                self.minzoom = cog.minzoom

            if self.maxzoom is None:
                self.maxzoom = cog.maxzoom

    def _get_asset_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.input, f"{self.prefix}{band}.tif")

# we have a directoty with "scene_b1.tif", "scene_b2.tif"
with AssetFileReader(input="my_dir/", prefix="scene_") as cr:
    print(cr.assets)
    >>> ['band1', 'band2']

    info = cr.info(assets=("band1", "band2"))
    # MultiBaseReader returns a Dict
    assert isinstance(info, dict)
    print(list(info))
    >>> ['band1', 'band2']

    assert isinstance(info["band1"], Info)
    print(info["band1"].model_dump_json(exclude_none=True))
    >>> {
        'bounds': [-11.979244865430259, 24.296321392464325, -10.874546803397614, 25.304623891542263],
        'minzoom': 7,
        'maxzoom': 9,
        'band_metadata': [('b1', {})],
        'band_descriptions': [('b1', '')],
        'dtype': 'uint16',
        'nodata_type': 'Nodata',
        'colorinterp': ['gray']
    }
    img = cr.tile(238, 218, 9, assets=("band1", "band2"))

    print(img.assets)
    >>> ['my_dir/scene_band1.tif', 'my_dir/scene_band2.tif']

    # Each assets have 1 bands, so when combining each img we get a (2, 256, 256) array.
    print(img.data.shape)
    >>> (2, 256, 256)
```

### **MultiBandsReader**

Almost as the previous `MultiBaseReader`, the `MultiBandsReader` children will merge results extracted from different file but taking each file as individual bands.

The `MultiBaseReader` has the same attributes/properties/methods as the `BaseReader`.

Example

```python
import os
import pathlib
from typing import Dict, Type

import attr
from morecantile import TileMatrixSet
from rio_tiler.io.base import MultiBandReader
from rio_tiler.io import COGReader, BaseReader
from rio_tiler.constants import WEB_MERCATOR_TMS

@attr.s
class BandFileReader(MultiBandReader):

    input: str = attr.ib()
    prefix: str = attr.ib() # we add a custom attribute

    # because we add another attribute (prefix) we need to
    # re-specify the other attribute for the class
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # we place min/max zoom in __init__
    minzoom: int = attr.ib(default=None)
    maxzoom: int = attr.ib(default=None)

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.bands = sorted(
            [p.stem.split("_")[1] for p in pathlib.Path(self.input).glob(f"*{self.prefix}*.tif")]
        )
        with self.reader(self._get_band_url(self.bands[0])) as cog:
            self.bounds = cog.bounds
            self.crs = cog.crs

            if self.minzoom is None:
                self.minzoom = cog.minzoom

            if self.maxzoom is None:
                self.maxzoom = cog.maxzoom

    def _get_band_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.input, f"{self.prefix}{band}.tif")


# we have a directoty with "scene_b1.tif", "scene_b2.tif"
with BandFileReader(input="my_dir/", prefix="scene_") as cr:
    print(cr.bands)
    >>> ['band1', 'band2']

    print(cr.info(bands=("band1", "band2")).model_dump_json(exclude_none=True))
    >>> {
        'bounds': [-11.979244865430259, 24.296321392464325, -10.874546803397614, 25.304623891542263],
        'minzoom': 7,
        'maxzoom': 9,
        'band_metadata': [('band1', {}), ('band2', {})],
        'band_descriptions': [('band1', ''), ('band2', '')],
        'dtype': 'uint16',
        'nodata_type': 'Nodata',
        'colorinterp': ['gray', 'gray']
    }

    img = cr.tile(238, 218, 9, bands=("band1", "band2"))

    print(img.assets)
    >>> ['my_dir/scene_band1.tif', 'my_dir/scene_band2.tif']

    print(img.data.shape)
    >>> (2, 256, 256)
```

Note: [`rio-tiler-pds`][rio-tiler-pds] readers are built using the `MultiBandReader` base class.

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds


## Custom Reader subclass

The example :point_down: was created as a response to https://github.com/developmentseed/titiler/discussions/235. In short, the user needed a way to keep metadata information from an asset within a STAC item.

Sadly when we are using the STAC Reader we only keep the metadata about the item but not the assets metadata (because we built the STAC Reader with the idea that user might first want to merge assets together).

But rio-tiler has been designed to be easily customizable.

```python
import attr
from rasterio.io import DatasetReader
from rio_tiler.io.stac import fetch, _to_pystac_item
from rio_tiler.io import Reader
import pystac

@attr.s
class CustomSTACReader(Reader):
    """Custom Reader support."""

    # This will keep the STAC item info within the instance
    item: pystac.Item = attr.ib(default=None, init=False)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        # get STAC item URL and asset name
        asset = self.input.split(":")[-1]
        stac_url = self.input.replace(f":{asset}", "")

        # Fetch the STAC item
        self.item = pystac.Item.from_dict(fetch(stac_url), stac_url)

        # Get asset url from the STAC Item
        self.input = self.item.assets[asset].get_absolute_href()
        super().__attrs_post_init__()

with CustomSTACReader("https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json:pan") as cog:
    print(type(cog.dataset))
    print(cog.input)
    print(cog.nodata)
    print(cog.bounds)

>>> rasterio.io.DatasetReader
>>> "https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/s5_11055_6057_20070622_p10_1_lcc00_cog.tif"
>>> 0
>>> (-869900.0, 1370200.0, -786360.0, 1453180.0)
```

In this `CustomSTACReader`, we are using a custom path `schema` in form of `{item-url}:{asset-name}`. When creating an instance of `CustomSTACReader`, we will do the following:

1. Parse the input path to get the STAC url and asset name
2. Fetch and parse the STAC item
3. Construct a new `input` using the asset full url.
4. Fall back to the regular `Reader` initialization (using `super().__attrs_post_init__()`)


## Simple Reader


```python
from typing import Any, Dict

import attr
import rasterio
from rasterio.io import DatasetReader
from rio_tiler.io import BaseReader
from rio_tiler.models import BandStatistics, Info, ImageData
from morecantile import TileMatrixSet

from rio_tiler.constants import BBox, WEB_MERCATOR_TMS

@attr.s
class SimpleReader(BaseReader):

    input: DatasetReader = attr.ib()

    # We force tms to be outside the class __init__
    tms: TileMatrixSet = attr.ib(init=False, default=WEB_MERCATOR_TMS)

    # We overwrite the abstract base class attribute definition and set default
    minzoom: int = attr.ib(init=False, default=WEB_MERCATOR_TMS.minzoom)
    maxzoom: int = attr.ib(init=False, default=WEB_MERCATOR_TMS.maxzoom)

    def __attrs_post_init__(self):
        # Set bounds and crs variable
        self.bounds = self.input.bounds
        self.crs = self.input.crs

    # implement all mandatory methods
    def info(self) -> Info:
        raise NotImplemented

    def statistics(self, **kwargs: Any) -> Dict[str, BandStatistics]:
        raise NotImplemented

    def part(self, bbox: BBox, **kwargs: Any) -> ImageData:
        raise NotImplemented

    def preview(self, **kwargs: Any) -> ImageData:
        raise NotImplemented

    def point(self, lon: float, lat: float, **kwargs: Any) -> List:
        raise NotImplemented

    def feature(self, shape: Dict, **kwargs: Any) -> ImageData:
        raise NotImplemented

    def tile(self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any) -> ImageData:
        if not self.tile_exists(tile_x, tile_y, tile_z):
            raise TileOutsideBounds(
                f"Tile {tile_z}/{tile_x}/{tile_y} is outside bounds"
            )

        tile_bounds = self.tms.xy_bounds(Tile(x=tile_x, y=tile_y, z=tile_z))

        data, mask = reader.part(
            self.input,
            tile_bounds,
            width=256,
            height=256,
            bounds_crs=tms.rasterio_crs,
            dst_crs=tms.rasterio_crs,
            **kwargs,
        )
        return ImageData(
            data, mask, bounds=tile_bounds, crs=tms.rasterio_crs
        )

with rasterio.open("file.tif") as src:
    with SimpleReader(src) as cog:
        img = cog.tile(1, 1, 1)
```
