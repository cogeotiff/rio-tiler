`rio-tiler`'s Readers provide simple `.statistics` method to retrieve dataset statistics (min, max, histogram...). We can easily extend this to create a `.zonal_statistics` method which will accept input features to get statistics from.

```python

import attr
from typing import Any, Union, Optional, List, Dict

from rio_tiler import io
from rio_tiler.utils import get_array_statistics
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
            percentiles: List[int] = [2, 98],
            hist_options: Optional[Dict] = None,
            max_size: int = None,
            **kwargs: Any,
        ) -> FeatureCollection:
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
                FeatureCollection

            """
            kwargs = {**self._kwargs, **kwargs}

            hist_options = hist_options or {}

            # We transform the input Feature to a FeatureCollection
            if not isinstance(geojson, FeatureCollection):
                geojson = FeatureCollection(features=[geojson])

            for feature in geojson:
                # Get data overlapping with the feature (using Reader.feature method)
                data = self.feature(
                    feature.dict(exclude_none=True),
                    max_size=max_size,
                    **kwargs,
                )

                # Get band statistics for the data
                stats = get_array_statistics(
                    data.as_masked(),
                    categorical=categorical,
                    categories=categories,
                    percentiles=percentiles,
                    **hist_options,
                )

                # Update input feature properties and add the statistics
                feature.properties = feature.properties or {}
                feature.properties.update(
                    {
                        "statistics": {
                            f"{data.band_names[ix]}": BandStatistics(
                                **stats[ix]
                            )
                            for ix in range(len(stats))
                        }
                    }
                )

            return geojson
```
