"""rio-tiler.io"""

from .base import BaseReader, MultiBandReader, MultiBaseReader  # noqa
from .cogeo import COGReader  # noqa
from .stac import STACReader  # noqa
from .xarray import XarrayReader  # noqa
