"""rio-tiler.mosaic.methods abc class."""

import abc
from typing import Optional, Tuple

import numpy


class MosaicMethodBase(abc.ABC):
    """Abstract base class for rio-tiler-mosaic methods objects."""

    def __init__(self) -> None:
        """Init backend."""
        self.tile: Optional[numpy.ma.MaskedArray] = None
        self.exit_when_filled: bool = False

    @property
    def is_done(self) -> bool:
        """Check if the tile filling is done.

        Returns:
            bool

        """
        if self.tile is None:
            return False

        if self.exit_when_filled and not numpy.ma.is_masked(self.tile):
            return True

        return False

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return data."""
        return self.tile

    @abc.abstractmethod
    def feed(self, tile: numpy.ma.MaskedArray):
        """Fill mosaic tile.

        Args:
            tile (numpy.ma.ndarray): data

        """
