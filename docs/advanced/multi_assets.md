
`rio_tiler.io.cogeo` submodule has `multi_*` functions (tile, part, preview, point, metadata, info, stats) allowing to fetch and merge info/data
from multiple dataset (think about multiple bands stored in separated files).

```python
from typing import Dict
from rio_tiler.io.cogeo import multi_tile

assets = ["b1.tif", "b2.tif", "b3.tif"]
tile, mask = multi_tile(assets, x, y, z, tilesize=256)

print(tile.shape)
> (3, 256, 256)

# Others
metadata = multi_info(assets)
stats = multi_stats(assets, pmin=2, pmax=98, ...)
metadata = multi_metadata(assets, pmin=2, pmax=98, ...)
values = multi_points(assets, lon, lat, ...)
data, mask = multi_part(assets, bbox, ...)
data, mask = multi_preview(assets, ...)
```

You can also use `rio_tiler.io.base.MultiBaseReader` to build a custom asset reader:

```python
import attr
from rio_tiler.io.base import MultiBaseReader
from rio_tiler.io import COGReader, BaseReader


# CustomReader is a subclass of MultiBaseReader.
# To ease the creation of the class and because MultiBaseReader is built with `attr`
# we also need to add the `@attr.s` wrapper on top of our custom class.
@attr.s
class CustomReader(MultiBaseReader):

    directory: str = attr.ib() # required arg
    reader: Type[BaseReader] = attr.ib(default=COGReader) # the default reader is COGReader

    def __enter__(self):
        # List files in directory
        dirs = os.listdir(self.directory)

        # get list of tifs
        tiff = [f for f in dirs if f.endswith(".tif")]

        # create list of assets names - REQUIRED
        self.assets = [os.path.basename(f).split(".")[0] for f in tiff]

        # `self.bounds` needs to be set! - REQUIRED
        with self.reader(tiff[0]) as cog:
            self.bounds = cog.bounds

        return self

    def _get_asset_url(self, asset: str) -> str:
        """Validate asset names and return asset's url."""
        if asset not in self.assets:
            raise InvalidAssetName(f"{asset} is not valid")

        return os.path.join(self.directory, f"{asset}.tif")

# we have a directoty with "b1.tif", "b2.tif", "b3.tif"
with CustomReader("my_dir/") as cr:
    print(cr.assets)
    tile, mask = cr.tile(x, y, z, assets="b1")

> ["b1", "b2", "b3"]

print(tile.shape)
> (3, 256, 256)
```
