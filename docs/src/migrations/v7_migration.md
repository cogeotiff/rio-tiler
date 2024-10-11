
`rio-tiler` version 7.0 introduced [many breaking changes](../release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 7.0.

Changelog: https://github.com/cogeotiff/rio-tiler/compare/6.7.0..7.0.0


## Info Model

#### Bounds

The `bounds` property was replaced from the `geographic bounds` to the dataset `bounds`, and the associated CRS was also added as a new property.

```python
# before
with Reader("cog.tif") as src:
    info = src.info()
    assert src.geographic_bounds == info.bounds

# now
with Reader("cog.tif") as src:
    info = src.info()
    assert src.bounds == info.bounds
    assert info.crs
```

#### Min/Max zooms

We removed the `minzoom` and `maxzoom` properties from the `rio_tiler.models.Info` (and removed the `SpatialInfo` model). We chose to removed any `external` geographic metadata to ease the use of the `info()` method.

```python
# before
with Reader("cog.tif") as src:
    info = src.info()
    assert info.minzoom
    assert info.maxzoom

# now
# The min/max zooms are still Reader's properties
with Reader("cog.tif") as src:
    assert src.minzoom
    assert src.maxzoom
```

## Geographic CRS and Bounds

we removed the `geographic_crs` attribute in the BaseReader class and replaced the `geographic_bounds` property with a `get_geographic_bounds(crs: rasterio.crs.CRS)` method.

```python
from rasterio.crs import CRS
from rio_tiler.io import Reader

# before
with Reader("cog.tif", geographic_crs=CRS.from_epsg(4326)) as src:
    bounds = src.geographic_bounds

# now
with Reader("cog.tif") as src:
    bounds = src.get_geographic_bounds(CRS.from_epsg(4326))
```

## ColorMaps

In previous version, the `ColorMaps.get(name: str)` method did not care about the *Case* of the name. This has been disabled and now the name should reflect the `basename` of the colormap file (`.npy`) or the name used while registering the colormap to the ColorMaps object.

```python
from rio_tiler.colormap import cmap

# before
assert cmap.get("Viridis")

# now
assert cmap.get("Viridis")
>> InvalidColorMapName: Invalid colormap name: Viridis
```

## New Features

* add support for `.json` colormap files (in addition to `.npy` files)

* Enable dynamic definition of Asset **reader** in `MultiBaseReader`

    ```python
    @attr.s
    class STACReader(OfficialSTACReader):

        include_asset_types: Set[str] = attr.ib(default=valid_types)

        def _get_reader(self, asset_info: AssetInfo) -> Type[BaseReader]:
            """Get Asset Reader."""
            asset_type = asset_info.get("type", None)

            if asset_type and asset_type in [
                "application/x-hdf5",
                "application/x-hdf",
                "application/vnd.zarr",
                "application/x-netcdf",

            ]:
                return XarrayReader

            return Reader
    ```

* add `default_assets` for MultiBaseReader

* add `default_bands` for MultiBandReader

* add `transform`, `height` and `width` attributes in `SpatialMixin` class

* add support for STAC's Projection extension to derive bounds, crs, minzoom and maxzoom properties

* enable **Alternate** asset's HREF for STAC by using `RIO_TILER_STAC_ALTERNATE_KEY` environment variable

* add support for GDAL VRT Connection string for STAC Assets

    ```python
    with STACReader("file.grib") as stac:
        info = stac.info(assets="vrt://asset?bands=1")
    ```

* make `ImageData.rescale` and `ImageData.apply_color_formula` to return `self`
