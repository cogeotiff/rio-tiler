"""rio_tiler.io.base: ABC class for rio-tiler readers."""

import abc
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy


# ref: https://github.com/python/mypy/issues/5374
@dataclass  # type: ignore
class BaseReader(metaclass=abc.ABCMeta):
    """Rio-tiler.io BaseReader."""

    bounds: Sequence[float] = field(init=False)

    @abc.abstractmethod
    def __enter__(self):
        """Support using with Context Managers."""
        ...

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """Support using with Context Managers."""
        ...

    @property
    def minzoom(self) -> int:
        """Dataset Min zoom."""
        ...

    @property
    def maxzoom(self) -> int:
        """Dataset Max zoom."""
        ...

    @property
    def center(self) -> Tuple[float, float, int]:
        """Dataset center + minzoom."""
        return (
            (self.bounds[0] + self.bounds[2]) / 2,
            (self.bounds[1] + self.bounds[3]) / 2,
            self.minzoom,
        )

    @abc.abstractmethod
    def info(self) -> Dict:
        """Return Dataset's info."""
        ...

    @property
    def spatial_info(self) -> Dict:
        """Return Dataset's spatial info."""
        return {
            "bounds": self.bounds,
            "center": self.center,
            "minzoom": self.minzoom,
            "maxzoom": self.maxzoom,
        }

    @abc.abstractmethod
    def stats(
        self,
        pmin: float = 2.0,
        pmax: float = 98.0,
        hist_options: Optional[Dict] = None,
        **kwargs: Any,
    ) -> Dict:
        """Return Dataset's statistics."""
        ...

    @abc.abstractmethod
    def metadata(self, pmin: float = 2.0, pmax: float = 98.0, **kwargs: Any,) -> Dict:
        """Return Dataset's statistics and info."""
        info = self.info()
        info["statistics"] = self.stats(pmin, pmax, **kwargs)
        return info

    @abc.abstractmethod
    def tile(
        self, tile_x: int, tile_y: int, tile_z: int, **kwargs: Any
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Map tile from the Dataset."""
        ...

    @abc.abstractmethod
    def part(
        self, bbox: Tuple[float, float, float, float], **kwargs: Any
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Read a Part of a Dataset."""
        ...

    @abc.abstractmethod
    def preview(self, **kwargs: Any) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Return a preview of a Dataset."""
        ...

    @abc.abstractmethod
    def point(self, lon: float, lat: float, **kwargs: Any) -> List:
        """Read a value from a Dataset."""
        ...
