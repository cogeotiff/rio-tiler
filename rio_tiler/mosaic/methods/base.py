"""rio-tiler.mosaic.methods abc class."""

import abc
from typing import Optional, Tuple

import numpy


class MosaicMethodBase(abc.ABC):
    """Abstract base class for rio-tiler-mosaic methods objects."""

    def __init__(
        self, cutline_mask: numpy.ndarray = None, exit_when_filled: bool = False
    ) -> None:
        """Init backend."""
        self.cutline_mask = cutline_mask
        self.tile: Optional[numpy.ma.MaskedArray] = None
        self.exit_when_filled: bool = exit_when_filled

    @property
    def is_done(self) -> bool:
        """Check if the tile filling is done.

        Returns:
            bool

        """
        if self.tile is None:
            return False

        if self.exit_when_filled:
            if self.cutline_mask is not None and not numpy.sum(
                numpy.where(self.cutline_mask == 0, self.tile.mask, 0)
            ):
                return True
            elif not numpy.ma.is_masked(self.tile):
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
