
`rio-tiler` provides multiple [abstract base
classes](https://docs.python.org/3.7/library/abc.html) from which it derives its
main readers: [`COGReader`](../readers.md#cogreader) and
[`STACReader`](../readers.md#stacreader). You can also use these classes to build
custom readers.

## Abstract Base Classes

### **BaseReader**

Main `rio_tiler.io` Abstract Base Class.

##### Minimal Arguments

- **tms**: morecantile.TileMatrixSet (default is set to WebMercatorQuad). The TileMatrixSet define which default projection and map grid the reader uses.

- **bounds**: bounding box of the dataset. Not in the `init` method.
- **minzoom**: dataset minzoom. Not in the `init` method.
- **maxzoom**: dataset maxzoom. Not in the `init` method.

Class arguments set to be define outside the `init` method can be set in the `__attrs_post_init__` step.

Example:
```python

@attr.s
class Reader(BaseReader):

    filepath: str = attr.ib() # Required argument
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    # We can overwrite the baseclass attribute definition
    minzoom: int = attr.ib(default=WEB_MERCATOR_TMS.minzoom)
    maxzoom: int = attr.ib(default=WEB_MERCATOR_TMS.maxzoom)

    bounds: Tuple[float, float, float, float] = attr.ib(init=False)
    dataset: rasterio.io.DatasetReader = attr.ib(init=False)

    def __attrs_post_init__(self):
        # Set the dataset variable
        self.dataset = rasterio.open(self.filepath)

        # Set bounds variable
        self.bounds = transform_bounds(
            self.dataset.crs, constants.WGS84_CRS, *self.dataset.bounds, densify_pts=21
        )
    ...
```

##### Properties

- **center**: dataset center (calculated from bounds and minzoom).
- **spatial_info**: bounds + zoom info.

Those properties will be added by default in every readers (because bounds and zooms info are part of the BaseReader definition).

##### Abstract Methods

Abstract methods, are mehtod that **HAVE TO** be implemented in the subclass.

- **info**: returns dataset info (`rio_tiler.models.Info`)
- **stats**: returns dataset array statistric (`Dict[str, rio_tiler.models.ImageStatistics]`)
- **metadata**: returns info + stats (`rio_tiler.models.Metadata`)
- **tile**: reads data for a specific XYZ slippy map indexes (`rio_tiler.models.ImageData`)
- **part**: reads specific part of a dataset (`rio_tiler.models.ImageData`)
- **preview**: creates an overview of a dataset (`rio_tiler.models.ImageData`)
- **point**: reads pixel value for a specific point (`List`)
- **feature**: reads data for a geojson feature (`rio_tiler.models.ImageData`)

Example: [`COGReader`](../readers.md#cogreader)

### **AsyncBaseReader**

Equivalent of `BaseReader` for async-ready readers (e.g [aiocogeo](https://github.com/geospatial-jeff/aiocogeo)). The `AsyncBaseReader` has the same properties/methods as the `BaseReader`.

see example of reader built using `AsyncBaseReader`: https://github.com/cogeotiff/rio-tiler/blob/832ecbd97f560c2764818bca30ca95ef25408527/tests/test_io_async.py#L49

### **MultiBaseReader**

This abstract class inherit from `BaseReader`. The goal of the `MultiBaseReader` is to enable readers that need to join results from multiple files (e.g STAC).

Example: [`STACReader`](../readers.md#stacreader)

```python
import os
import pathlib
from typing import Dict, Type

import attr
from morecantile import TileMatrixSet
from rio_tiler.io.base import MultiBaseReader
from rio_tiler.io import COGReader, BaseReader
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.models import Info

@attr.s
class AssetFileReader(MultiBaseReader):

    path: str = attr.ib()
    prefix: str = attr.ib()
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.assets = sorted(
            [p.stem.split("_")[1] for p in pathlib.Path(self.path).glob(f"*{self.prefix}*.tif")]
        )
        with self.reader(self._get_asset_url(self.assets[0])) as cog:
            self.bounds = cog.bounds
            self.minzoom = cog.minzoom
            self.maxzoom = cog.maxzoom

    def _get_asset_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.path, f"{self.prefix}{band}.tif")

# we have a directoty with "scene_b1.tif", "scene_b2.tif"
with AssetFileReader("my_dir/", "scene_") as cr:
    print(cr.assets)
    >>> ['b1', 'b2']

    info = cr.info(assets=("b1", "b2"))
    # MultiBaseReader returns a Dict
    assert isinstance(info, dict)
    print(list(info))
    >>> ['b1', 'b2']

    assert isinstance(info["b1"], Info)
    print(info["b1"].dict(exclude_none=True))
    >>> {
        'bounds': (-11.979244865430259, 24.296321392464325, -10.874546803397614, 25.304623891542263),
        'center': (-11.426895834413937, 24.800472642003292, 7),
        'minzoom': 7,
        'maxzoom': 9,
        'band_metadata': [('1', {})],
        'band_descriptions': [('1', '')],
        'dtype': 'uint16',
        'nodata_type': 'Nodata',
        'colorinterp': ['gray']
    }
    img = cr.tile(238, 218, 9, assets=("b1", "b2"))

    print(img.assets)
    >>> ['my_dir/scene_b1.tif', 'my_dir/scene_b2.tif']

    # Each assets have 1 bands, so when combining each img we get a (2, 256, 256) array.
    print(img.data.shape)
    >>> (2, 256, 256)
```

### **MultiBandsReader**

Almost as the previous `MultiBaseReader`, the `MultiBandsReader` subclasses will merge results extracted from differents assets but taking each assets as individual bands.

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

    path: str = attr.ib()
    prefix: str = attr.ib()
    reader: Type[BaseReader] = attr.ib(default=COGReader)
    reader_options: Dict = attr.ib(factory=dict)
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    def __attrs_post_init__(self):
        """Parse Sceneid and get grid bounds."""
        self.bands = sorted(
            [p.stem.split("_")[1] for p in pathlib.Path(self.path).glob(f"*{self.prefix}*.tif")]
        )
        with self.reader(self._get_band_url(self.bands[0])) as cog:
            self.bounds = cog.bounds
            self.minzoom = cog.minzoom
            self.maxzoom = cog.maxzoom

    def _get_band_url(self, band: str) -> str:
        """Validate band's name and return band's url."""
        return os.path.join(self.path, f"{self.prefix}{band}.tif")


# we have a directoty with "scene_b1.tif", "scene_b2.tif"
with BandFileReader("my_dir/", "scene_") as cr:
    print(cr.bands)
    >>> ['b1', 'b2']

    print(cr.info(bands=("b1", "b2")).dict(exclude_none=True))
    >>> {
        'bounds': (-11.979244865430259, 24.296321392464325, -10.874546803397614, 25.304623891542263),
        'center': (-11.426895834413937, 24.800472642003292, 7),
        'minzoom': 7,
        'maxzoom': 9,
        'band_metadata': [('b1', {}), ('b2', {})],
        'band_descriptions': [('b1', ''), ('b2', '')],
        'dtype': 'uint16',
        'nodata_type': 'Nodata',
        'colorinterp': ['gray', 'gray']
    }

    img = cr.tile(238, 218, 9, bands=("b1", "b2"))

    print(img.assets)
    >>> ['my_dir/scene_b1.tif', 'my_dir/scene_b2.tif']

    print(img.data.shape)
    >>> (2, 256, 256)
```

Note: [`rio-tiler-pds`][rio-tiler-pds] readers are built using the `MultiBandReader` base class.

[rio-tiler-pds]: https://github.com/cogeotiff/rio-tiler-pds


## Custom COGReader subclass

The example :point_down: was created as a response to https://github.com/developmentseed/titiler/discussions/235. In short, the user needed a way to keep metadata information from an asset within a STAC item.

Sadly when we are using the STAC Reader we only keep the metadata about the item but not the assets metadata (because we built the STAC Reader with the idea that user might first want to merge assets together).

But rio-tiler has been designed to be easily customizable.

```python
import attr
from rasterio.io import DatasetReader
from rio_tiler.io.stac import fetch, _to_pystac_item
from rio_tiler.io import COGReader
import pystac

@attr.s
class CustomSTACReader(COGReader):
    """Custom COG Reader with GCPS support."""

    # This will keep the STAC item info within the instance
    item: pystac.Item = attr.ib(default=None, init=False)

    def __attrs_post_init__(self):
        """Define _kwargs, open dataset and get info."""
        # get STAC item URL and asset name
        asset = self.filepath.split(":")[-1]
        stac_url = self.filepath.replace(f":{asset}", "")

        # Fetch the STAC item
        self.item = pystac.Item.from_dict(fetch(stac_url), stac_url)

        # Get asset url from the STAC Item
        self.filepath = self.item.assets[asset].get_absolute_href()
        super().__attrs_post_init__()

with CustomSTACReader("https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json:pan") as cog:
    print(type(cog.dataset))
    print(cog.filepath)
    print(cog.nodata)
    print(cog.bounds)

>>> rasterio.io.DatasetReader
>>> "https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/s5_11055_6057_20070622_p10_1_lcc00_cog.tif"
>>> 0
>>> (-111.87793996076493, 60.48627186654449, -109.94924666908423, 61.42036313093244)
```

In this `CustomSTACReader`, we are using a custom path `schema` in form of `{item-url}:{asset-name}`. When creating an instance of `CustomSTACReader`, we will do the following:

1. Parse the input path to get the STAC url and asset name
2. Fetch and parse the STAC item
3. Construct a new `filename` using the asset full url.
4. Fall back to the regular `COGReader` initialization (using `super().__attrs_post_init__()`)
