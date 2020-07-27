"""rio_tiler.mosaic.methods.defaults: default mosaic filling methods."""

import numpy

from .base import MosaicMethodBase


class FirstMethod(MosaicMethodBase):
    """Feed the mosaic tile with the first pixel available."""

    def __init__(self):
        """Overwrite base and init First method."""
        super(FirstMethod, self).__init__()
        self.exit_when_filled = True

    def feed(self, tile):
        """Add data to tile."""
        if self.tile is None:
            self.tile = tile
        pidex = self.tile.mask & ~tile.mask

        mask = numpy.where(pidex, tile.mask, self.tile.mask)
        self.tile = numpy.ma.where(pidex, tile, self.tile)
        self.tile.mask = mask


class HighestMethod(MosaicMethodBase):
    """Feed the mosaic tile with the highest pixel values."""

    def feed(self, tile):
        """Add data to tile."""
        if self.tile is None:
            self.tile = tile

        pidex = (
            numpy.bitwise_and(tile.data > self.tile.data, ~tile.mask) | self.tile.mask
        )

        mask = numpy.where(pidex, tile.mask, self.tile.mask)
        self.tile = numpy.ma.where(pidex, tile, self.tile)
        self.tile.mask = mask


class LowestMethod(MosaicMethodBase):
    """Feed the mosaic tile with the lowest pixel values."""

    def feed(self, tile):
        """Add data to tile."""
        if self.tile is None:
            self.tile = tile

        pidex = (
            numpy.bitwise_and(tile.data < self.tile.data, ~tile.mask) | self.tile.mask
        )

        mask = numpy.where(pidex, tile.mask, self.tile.mask)
        self.tile = numpy.ma.where(pidex, tile, self.tile)
        self.tile.mask = mask


class MeanMethod(MosaicMethodBase):
    """Stack the tiles and return the Mean pixel value."""

    def __init__(self, enforce_data_type=True):
        """Overwrite base and init Mean method."""
        super(MeanMethod, self).__init__()
        self.enforce_data_type = enforce_data_type
        self.tile = []

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            tile = numpy.ma.mean(numpy.ma.stack(self.tile, axis=0), axis=0)
            if self.enforce_data_type:
                tile = tile.astype(self.tile[0].dtype)
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Add data to tile."""
        self.tile.append(tile)


class MedianMethod(MosaicMethodBase):
    """Stack the tiles and return the Median pixel value."""

    def __init__(self, enforce_data_type=True):
        """Overwrite base and init Median method."""
        super(MedianMethod, self).__init__()
        self.enforce_data_type = enforce_data_type
        self.tile = []

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            tile = numpy.ma.median(numpy.ma.stack(self.tile, axis=0), axis=0)
            if self.enforce_data_type:
                tile = tile.astype(self.tile[0].dtype)
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Create a stack of tile."""
        self.tile.append(tile)


class StdevMethod(MosaicMethodBase):
    """Stack the tiles and return the Standart Deviation value."""

    def __init__(self, enforce_data_type=True):
        """Overwrite base and init Stdev method."""
        super(StdevMethod, self).__init__()
        self.tile = []

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            tile = numpy.ma.std(numpy.ma.stack(self.tile, axis=0), axis=0)
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Add data to tile."""
        self.tile.append(tile)
