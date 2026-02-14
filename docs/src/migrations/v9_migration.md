
!!! note

    This migration guide was generated with the help of Claude AI and may require review.

`rio-tiler` version 9.0 introduced [many breaking changes](../release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 9.0.

Changelog: https://github.com/cogeotiff/rio-tiler/compare/8.0.5..9.0.0


## Tile Size Default

The default `tilesize` option (`256`) for `tile()` methods has been removed. The tile size now defaults to the TMS tilematrix `tileHeight` and `tileWidth`.

```python
from rio_tiler.io import Reader

# before (8.x)
with Reader("cog.tif") as src:
    # tiles were always 256x256 by default
    img = src.tile(0, 0, 0)
    assert img.width == 256
    assert img.height == 256

# now (9.x)
with Reader("cog.tif") as src:
    # tiles now use TMS tileMatrixSet dimensions (still 256x256 for WebMercatorQuad)
    img = src.tile(0, 0, 0)
    # but for custom TMS, it will use that TMS's tile dimensions

    # To explicitly set 256x256:
    img = src.tile(0, 0, 0, tilesize=256)
```


## Band Names in ImageData

The `band_names` attribute in `ImageData` now uses unique names when reading the same band multiple times:

```python
from rio_tiler.io import Reader

# before (8.x)
with Reader("cog.tif") as src:
    img = src.read(indexes=(1, 1,))
    print(img.band_names)
    >> ["b1", "b1"]

# now (9.x)
with Reader("cog.tif") as src:
    img = src.read(indexes=(1, 1,))
    print(img.band_names)
    >> ["b1", "b2"]
```


## MultiBandReader Deprecation

The `MultiBandReader` class is deprecated. Use `MultiBaseReader` instead.

```python
# before (8.x)
from rio_tiler.io.base import MultiBandReader

class MyReader(MultiBandReader):
    ...

# now (9.x)
from rio_tiler.io.base import MultiBaseReader

class MyReader(MultiBaseReader):
    # Adapt your implementation to use MultiBaseReader's interface
    ...
```


## MultiBaseReader Expression Changes

### Expression Syntax

In `MultiBaseReader`, expressions now use the format `b1/b2` where `b1`, `b2`, etc. refer to the band index within the merged ImageData object returned by the `read` method, not the original asset band indexes:

```python
from rio_tiler.io.stac import STACReader

# before (8.x) - expressions could reference asset-specific bands
with STACReader("item.json") as src:
    # Using asset-specific expressions was inconsistent
    src.preview(assets=["asset1", "asset2"], expression="asset1_b1+asset2_b1")

# now (9.x) - expressions use merged ImageData band indexes
with STACReader("item.json") as src:
    # asset1 and asset2 are both 1-band datasets
    # After merging, the ImageData has bands b1 (from asset1) and b2 (from asset2)
    src.preview(assets=["asset1", "asset2"], expression="b1+b2")

    # If asset1 has 1 band and asset3 has 2 bands:
    # After merging: b1 (from asset1), b2 (first band of asset3), b3 (second band of asset3)
    src.preview(assets=["asset1", "asset3"], expression="b1+b2/b3")
```

### Removed Methods and Parameters

- The `parse_expression` method has been **removed** from `MultiBaseReader`
- The `asset_indexes` option has been **removed** from `MultiBaseReader` methods

```python
# before (8.x)
with STACReader("item.json") as src:
    img = src.tile(0, 0, 0, assets=["visual"], asset_indexes={"visual": (1, 2, 3)})

# now (9.x) - use asset option syntax instead
with STACReader("item.json") as src:
    # Use the new asset option syntax: {"name": `asset_name`, "indexes": [1], ...}
    img = src.tile(
        0, 
        0, 
        0, 
        assets=[
            {"name": "visual", "indexes": [1, 2, 3]}
        ]
    )
```


## STACReader Asset Options Syntax

`STACReader` now accepts asset-specific options using dictionaries `{"name": "asset_name", "indexes": [1], ...}`:

```python
from rio_tiler.io.stac import STACReader

# before (8.x)
with STACReader("item.json") as src:
    img = src.tile(0, 0, 0, assets=["visual"], asset_indexes={"visual": (1, 2, 3)})

# now (9.x)
with STACReader("item.json") as src:
    # Specify indexes per asset using the pipe syntax
    img = src.tile(0, 0, 0, assets=[{"name": "visual", "indexes": [1, 2, 3]}])

    # Multiple options can be combined
    img = src.tile(0, 0, 0, assets=[{"name": "visual", "indexes": [1, 2, 3], "expression": "b1+b2-b3"}])
```

Asset's options are distributed between `reader-options` and `method-options` in `_get_asset_info` method, which can be overridden for custom behavior.

## Statistics Key Names

Statistics now use band names (indexes) as keys instead of band descriptions:

```python
from rio_tiler.io import Reader

# before (8.x)
with Reader("cog.tif") as src:
    img = src.read()
    print(img.band_names)
    >> ["b1", "b2", "b3"]
    # band_names could be descriptions like ["red", "green", "blue"]
    # or empty strings ["", "", ""] if no band description

    stats = src.statistics(expression="b1+2")
    print(list(stats))
    >> ["b1+2"]  # Expression used as key

# now (9.x)
with Reader("cog.tif") as src:
    img = src.read()
    print(img.band_names)
    >> ["b1", "b2", "b3"]
    # band_names always use "bN" format

    stats = src.statistics(expression="b1+2")
    print(list(stats))
    >> ["b1"]  # Band name used as key

    # The expression is now stored in the description field
    print(stats["b1"].description)
    >> "red+2"  # or "b1+2" if no band description
```


## MultiBaseReader._get_reader Method Signature

The `_get_reader` method signature has changed. It now only returns the reader class, not a tuple of `(reader, reader_options)`. Reader options should now be passed via the `AssetInfo["reader_options"]` field instead.

```python
from rio_tiler.io.base import MultiBaseReader
from rio_tiler.io import Reader
from rio_tiler.types import AssetInfo

# before (8.x)
class MyReader(MultiBaseReader):
    def _get_reader(self, asset_info: AssetInfo) -> tuple[type[Reader], dict]:
        """Get Asset Reader and options."""
        reader_options = {"nodata": 0}
        return Reader, reader_options

# now (9.x)
class MyReader(MultiBaseReader):
    def _get_reader(self, asset_info: AssetInfo) -> type[Reader]:
        """Get Asset Reader."""
        return Reader

    def _get_asset_info(self, asset: str) -> AssetInfo:
        """Return asset info with reader options."""
        ...
        # Reader options are now passed via AssetInfo
        info["reader_options"] = {"nodata": 0}
        return info
```


## AssetInfo Type Changes

The `AssetInfo` TypedDict has been updated with new fields:

```python
from typing import Any, NotRequired, Sequence, TypedDict

# now (9.x)
class AssetInfo(TypedDict):
    """Asset Reader Options."""

    url: Any
    name: str
    media_type: str | None
    reader_options: dict  # NEW: used to pass reader-specific options
    method_options: dict  # NEW: used to pass method-specific options
    env: NotRequired[dict]
    metadata: NotRequired[dict]
    dataset_statistics: NotRequired[Sequence[tuple[float, float]]]
```

The new `reader_options/method_options` attributes is used in `MultiBaseReader` to pass specific options (like `indexes` or `expression`) to the underlying reader.


## BandStatistics Model

A new `description` field has been added to the `BandStatistics` model:

```python
from rio_tiler.io import Reader

# now (9.x)
with Reader("cog.tif") as src:
    stats = src.statistics()

    # Access the description for each band's statistics
    print(stats["b1"].description)
    >> "red"  # The band's description (or "b1" if none)
```


## Expression Band Descriptions

The `ImageData.apply_expression()` method now infers band descriptions for expression results:

```python
from rio_tiler.io import Reader

# before (8.x)
with Reader("cog_with_tags.tif") as src:
    img = src.preview(expression="b1*2")
    print(img.band_descriptions)
    >> [""]  # Empty description

# now (9.x)
with Reader("cog_with_tags.tif") as src:
    img = src.preview(expression="b1*2")
    print(img.band_descriptions)
    >> ["Green*2"]  # Description inferred from band description and expression
```


## New Features

### method_options in AssetInfo

The `method_options` attribute in `AssetInfo` allows passing method-specific options when reading assets in `MultiBaseReader`:

```python
from rio_tiler.io.stac import STACReader

with STACReader("item.json") as src:
    # Using asset option syntax passes options via method_options
    img = src.tile(0, 0, 0, assets=[{"name": "visual", "indexes": [1, 2]}])
```

### reader_options in AssetInfo

The `reader_options` attribute in `AssetInfo` allows passing reader-specific options when reading assets in `MultiBaseReader`:

```python
from typing import Any
import attr
from rio_tiler.io.stac import STACReader


@attr.s
class CustomSTACReader(STACReader):

    def _get_asset_info(self, asset: str | dict) -> AssetInfo:

        asset_name: str
        reader_options: dict[str, Any] = {}
        method_options: dict[str, Any] = {}
        if isinstance(asset, dict):

            # NOTE: if asset is a dict, the `asset name` should be store in
            # the `name` key:val
            asset_name = asset["name"]
            
            if indexes := asset.get("indexes"):
                method_options["indexes"] = indexes
            if expr := asset.get("expression"):
                method_options["expression"] = expr
            if "nodata" in asset:
                # NOTE: `nodata` can be a `Reader` Option
                reader_options = float(asset["nodata"]) # cast nodata to float
        else:
            asset_name = asset

        info = super()._get_asset_info(asset_name)
        info["reader_options"] = reader_options
        info["method_options"] = method_options
        return info

with CustomSTACReader("item.json") as src:
    # indexes=1,2: method option
    # nodata=0: reader option
    img = src.tile(0, 0, 0, assets=[{"name": "visual", "indexes": [1, 2], "nodata": 0}])
```

### BandStatistics description

Statistics now include a `description` field that provides context about what the statistic represents:

```python
from rio_tiler.io import Reader

with Reader("cog.tif") as src:
    stats = src.statistics(expression="b1+b2")
    # The description shows the actual band descriptions used in the expression
    print(stats["b1"].description)
```

### Inferred Expression Descriptions

When using expressions, the resulting `ImageData` now has meaningful band descriptions derived from the source bands:

```python
from rio_tiler.io import Reader

with Reader("cog.tif") as src:
    img = src.preview(expression="b1/b2")
    # band_descriptions are inferred from the expression
    print(img.band_descriptions)
    >> ["red/green"]  # Based on source band descriptions
```


## Migration Checklist

1. **Update tile() calls** - If you relied on the default 256 tilesize, explicitly pass `tilesize=256`

2. **Update expressions in MultiBaseReader** - Change expressions from asset-specific syntax to merged band index syntax (`b1`, `b2`, etc.)

3. **Replace asset_indexes** - Use the new asset option syntax `{"name" : "asset", "indexes": [1, 2, 3]}` instead of the `asset_indexes` parameter

4. **Update MultiBandReader subclasses** - Migrate to `MultiBaseReader`

5. **Update statistics parsing** - If you accessed statistics by expression strings, update to use band name keys and check the `description` field

6. **Update AssetInfo handling** - If you create custom `AssetInfo` objects, add the new `reader_options` and `method_options` fields

7. **Update _get_reader overrides** - If you override `_get_reader`, update to return only the reader class and move reader options to `_get_asset_info`
