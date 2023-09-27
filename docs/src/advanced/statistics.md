
### Statistics

`rio-tiler`'s Readers provide simple `.statistics` method to retrieve dataset global statistics

```python
with Reader("my.tif") as src:
    stats = src.statistics()

# Statistics result is in form of Dict[str, rio_tiler.models.BandStatistics]
print(stats.keys())
>>> ["b1", "b2", "b3"]

# rio_tiler.models.BandStatistics is a pydantic model
print(stats["1"].model_dump().keys())
[
    "min",
    "max",
    "mean",
    "count",
    "sum",
    "std",
    "median",
    "majority",
    "minority",
    "unique",
    "histogram",
    "valid_percent",
    "masked_pixels",
    "valid_pixels",
    # Percentile entries depend on user inputs
    "percentile_2",
    "percentile_98",
]
```

### Zonal Statistics

You can easily extend the `statistics()` method to create a `.zonal_statistics` one which will accept input features to get statistics from.

```python

import attr
from typing import Any, Union, Optional, List, Dict

from rio_tiler import io
from rio_tiler.models import BandStatistics

from geojson_pydantic.features import Feature, FeatureCollection
from geojson_pydantic.geometries import Polygon

class Reader(io.Reader):
    """Custom Reader with zonal_statistics method."""

    def zonal_statistics(
            self,
            geojson: Union[FeatureCollection, Feature],
            categorical: bool = False,
            categories: Optional[List[float]] = None,
            percentiles: Optional[List[int]] = None,
            hist_options: Optional[Dict] = None,
            max_size: int = None,
            **kwargs: Any,
        ) -> Union[FeatureCollection, Feature]:
            """Return statistics from GeoJSON features.

            Args:
                geojson (Feature or FeatureCollection): a GeoJSON Feature or FeatureCollection.
                categorical (bool): treat input data as categorical data. Defaults to False.
                categories (list of numbers, optional): list of categories to return value for.
                percentiles (list of numbers, optional): list of percentile values to calculate. Defaults to `[2, 98]`.
                hist_options (dict, optional): Options to forward to numpy.histogram function.
                max_size (int, optional): Limit the size of the longest dimension of the dataset read, respecting bounds X/Y aspect ratio. Defaults to None.
                kwargs (optional): Options to forward to `self.preview`.

            Returns:
                Feature or FeatureCollection

            """
            kwargs = {**self.options, **kwargs}

            hist_options = hist_options or {}

            fc = geojson
            # We transform the input Feature to a FeatureCollection
            if isinstance(fc, Feature):
                fc = FeatureCollection(type="FeatureCollection", features=[geojson])

            for feature in fc:
                # Get data overlapping with the feature (using Reader.feature method)
                data = self.feature(
                    feature.model_dump(exclude_none=True),
                    max_size=max_size,
                    **kwargs,
                )
                stats = data.statistics(
                    categorical=categorical,
                    categories=categories,
                    percentiles=percentiles,
                    hist_options=hist_options,
                )

                # Update input feature properties and add the statistics
                feature.properties = feature.properties or {}
                feature.properties.update({"statistics": stats})

            return fc.features[0] if isinstance(geojson, Feature) else fc
```


### Area Weighted Statistics

When getting statistics from `feature`, you may want to calculate values from the pixels which intersect with the geometry but also take the pixel intersection percentage into account. Starting with rio-tiler `6.2.0`, we've added a `coverage` option to the `statistics` utility which enable the user to pass an array representing the coverage percentage such as:

```python
import numpy
from rio_tiler.utils import get_array_statistics
# Data Array
# 1, 2
# 3, 4
data = numpy.ma.array((1, 2, 3, 4)).reshape((1, 2, 2))

# Coverage Array
# 0.5, 0
# 1, 0.25
coverage = numpy.array((0.5, 0, 1, 0.25)).reshape((2, 2))

stats = get_array_statistics(data, coverage=coverage)
assert len(stats) == 1
assert stats[0]["min"] == 1
assert stats[0]["max"] == 4
assert stats[0]["mean"] == 1.125  # (1 * 0.5 + 2 * 0.0 + 3 * 1.0 + 4 * 0.25) / 4
assert stats[0]["count"] == 1.75  # (0.5 + 0 + 1 + 0.25) sum of the coverage array
```

When using with a `feature`, your code might look something like:

```python
from rio_tiler.io import Reader
from rio_tiler.constants import WGS84_CRS

with Reader(path) as src:
    # First get the array for the feature
    data = src_dst.feature(
        shape,
        shape_crs=WGS84_CRS,
    )

    # Get the coverage % array, using ImageData.get_coverage_array method
    coverage_array = data.get_coverage_array(
        shape, shape_crs=WGS84_CRS
    )

    # Get statistics (ImageData.statistics is calling `rio_tiler.utils.get_array_statistics`)
    stats = data.statistics(coverage=coverage_array)
```

!!! warnings
    The coverage weights will only have influence on specific statistics:

    - `mean`
    - `count`
    - `sum`
    - `std`
    - `median`

