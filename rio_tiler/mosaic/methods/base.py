"""rio-tiler.mosaic.methods abc class."""

import abc

import numpy


class MosaicMethodBase(abc.ABC):
    """Abstract base class for rio-tiler-mosaic methods objects."""

    def __init__(self):
        """Init backend."""
        self.tile = None
        self.exit_when_filled = False

    @property
    def is_done(self):
        """
        Check if the tile filling is done.

        Returns
        -------
        bool

        """
        if self.tile is None:
            return False

        if self.exit_when_filled and not numpy.ma.is_masked(self.tile):
            return True

        return False

    @property
    def data(self):
        """
        Return data and mask.

        Returns
        -------
        tile: numpy.ndarray
        mask: numpy.ndarray

        """
        if self.tile is not None:
            return self.tile.data, ~self.tile.mask[0] * 255
        else:
            return None, None

    @abc.abstractmethod
    def feed(self, tile):
        """
        Fill mosaic tile.

        Parameters
        ----------
        tile: numpy.ma.ndarray

        """
