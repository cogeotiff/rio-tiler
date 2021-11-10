
`rio-tiler` version 3.0 introduced [many breaking changes](release-notes.md). This
document aims to help with migrating your code to use `rio-tiler` 3.0.

## Morecantile 2.0 -> 3.0

Morecantile 3.0 switched from rasterio to pyproj for the coordinates transformation processes (https://github.com/developmentseed/morecantile/blob/master/CHANGES.md#300a0-2021-09-09).
Morecantile and Pyproj require python >= 3.7 which means rio-tiler had to remove python 3.6 supports.

## Bounds and CRS properties

Previously the `BaseReader.bounds` property was set to the `wgs84` representation of the dataset bounds but to accommodate to non-earth dataset we changed this and decided to store the native dataset `bounds`. We've also added `BaseReader.crs` to make sure user can work with the `bounds` property.

We've added a `BaseReader.geographic_bounds`, which will return the `bounds` in WGS84.

```python
# v2
from rio_tiler.io import COGReader
with COGReader("my_tif.tif") as cog:
    print(cog.bounds)       # bounds in WGS84

# v3
with COGReader("my_tif.tif") as cog:
    print(cog.bounds)       # dataset bounds
    assert cog.bounds == cog.dataset.bounds  # bounds should be equal to the dataset bounds
    print(cog.crs)
    assert cog.crs == cog.dataset.crs

    print(cog.geographic_bounds)  # bounds in WGS84 projection
```

## No more `max_size`

We've removed the default option `max_size=1024` in `BaseReader.part` and `BaseReader.feature` to return the highest resolution dataset by default.

```python
# v2
from rio_tiler.io import COGReader
with COGReader("my_tif.tif") as cog:
    data = cog.part(bbox)
    assert data.width =< 1024
    assert data.height =< 1024

# v3
with COGReader("my_tif.tif") as cog:
    data = cog.part(bbox) # Can return data > 1024x1024
    data = cog.part(bbox, max_size=1024)  # will return the same result as in rio-tiler v2
```

## Metadata and Statistics

The `BaseReader.metadata` method has been deprecated in rio-tiler v3. The method was previously returning a combination of the `info()` and `stats()` methods responses.

The reader's `.stats()` methods were also deprecated in favor of the newly `.statistics()` method which will return more verbose statistics.

```python
# v2
from rio_tiler.io import COGReader
with COGReader("my_tif.tif") as cog:
    data = cog.stats(bbox)

>>> {'1': ImageStatistics(percentiles=[1.0, 6896.0], min=1.0, max=7872.0, std=2271.0065537857326, histogram=[[503460.0, 0.0, 0.0, 161792.0, 283094.0, 0.0, 0.0, 0.0, 87727.0, 9431.0], [1.0, 788.1, 1575.2, 2362.3, 3149.4, 3936.5, 4723.6, 5510.7, 6297.8, 7084.900000000001, 7872.0]], valid_percent=100.0)}

# v3
with COGReader("my_tif.tif") as cog:
    data = cog.cog.statistics(bbox)

>>> {'1': BandStatistics(min=1.0, max=7872.0, mean=2107.524612053134, count=1045504.0, sum=2203425412.0, std=2271.0065537857326, median=2800.0, majority=1.0, minority=7072.0, unique=15.0, histogram=[[503460.0, 0.0, 0.0, 161792.0, 283094.0, 0.0, 0.0, 0.0, 87727.0, 9431.0], [1.0, 788.1, 1575.2, 2362.3, 3149.4, 3936.5, 4723.6, 5510.7, 6297.8, 7084.900000000001, 7872.0]], valid_percent=100.0, masked_pixels=0.0, valid_pixels=1045504.0, percentile_2=1.0, percentile_98=6896.0)}
```

## `asset_expression` and `asset_indexes`

In 3.0, we changed how `asset_expression` was defined in `rio_tiler.io.MultiBaseReader` (the base class of STAC like datasets). In 2.0, it was defined as a `string` (e.g `b1+100`) and would be applied to all `assets` and in 3.0 it's now a `dict` in form of `{"asset 1": "expression for asset 1", ...}`.

```python
# v2
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_expression="b1*2",  # expression was applied to each asset
    )

# v3
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_expression={"data1": "b1*2", "data2": "b2*100"},  # we can now pass per asset expression
    )
```

We also added `asset_indexes` to return specific indexes per asset.


```python
# v2
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        indexes=1,  # first band of each asset would be returned
    )

# v3
with STACReader("mystac.json") as stac:
    img = stac.preview(
        assets=("data1", "data2"),
        asset_indexes={"data1": (1, 2), "data2": (3,)},  # we can now pass per asset Indexes
    )
```

## Deprecation

- `rio_tiler.io.base.BaseReader.metadata()` method
- `rio_tiler.io.base.BaseReader.stats()` method
- `rio_tiler.io.base.BaseReader.spatial_info()` method
- `rio_tiler.io.base.BaseReader.center` property
- `rio_tiler.models.Metadata` model
- `rio_tiler.models.ImageStatistics` model
* `rio_tiler.reader.stats` function
* `rio_tiler.reader.metadata` function
* `rio_tiler.utils._stats` function
