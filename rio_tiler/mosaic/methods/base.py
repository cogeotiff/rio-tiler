"""rio-tiler.mosaic.methods abc class."""

import abc
from dataclasses import dataclass, field
from typing import Optional

import numpy


@dataclass
class MosaicMethodBase(abc.ABC):
    """Abstract base class for rio-tiler-mosaic methods objects."""

    mosaic: Optional[numpy.ma.MaskedArray] = field(default=None, init=False)
    exit_when_filled: bool = field(default=False, init=False)
    cutline_mask: Optional[numpy.ndarray] = field(default=None, init=False)
    width: int = field(init=False)
    height: int = field(init=False)
    count: int = field(init=False)

    @property
    def is_done(self) -> bool:
        """Check if the mosaic filling is done.

        Returns:
            bool

        """
        if self.mosaic is None:
            return False

        if self.exit_when_filled:
            if (
                self.cutline_mask is not None
                and numpy.sum(numpy.where(~self.cutline_mask, self.mosaic.mask, False))
                == 0
            ):
                return True
            elif not numpy.ma.is_masked(self.mosaic):
                return True

        return False

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return data."""
        return self.mosaic

    @abc.abstractmethod
    def feed(self, array: numpy.ma.MaskedArray):
        """Fill mosaic array.

        Args:
            array (numpy.ma.ndarray): data

        """
