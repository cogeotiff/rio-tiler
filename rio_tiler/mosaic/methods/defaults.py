"""rio_tiler.mosaic.methods.defaults: default mosaic filling methods."""

import numpy

from .base import MosaicMethodBase
import hdmedians as hd


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
            tile = tile.astype(self.tile[0].dtype) if self.enforce_data_type else tile
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Create a stack of tile."""
        self.tile.append(tile)


class StdevMethod(MosaicMethodBase):
    """Stack the tiles and return the Standard Deviation value."""

    def __init__(self, enforce_data_type=True):
        """Overwrite base and init Stdev method."""
        super(StdevMethod, self).__init__()
        self.enforce_data_type = enforce_data_type
        self.tile = []

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            tile = numpy.ma.std(numpy.ma.stack(self.tile, axis=0), axis=0)
            tile = tile.astype(self.tile[0].dtype) if self.enforce_data_type else tile
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Add data to tile."""
        self.tile.append(tile)

class GeoMedianMethod(MosaicMethodBase):

    def __init__(self, enforce_data_type=True):
        super(GeoMedianMethod, self).__init__()
        self.enforce_data_type = enforce_data_type
        self.tile = []

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            # Convert with rescaling factor to float32 for input to Dale's hdmedians
            stacked_tile = (numpy.ma.stack(self.tile, axis=1) / 10000).astype(numpy.float32)
            b, t, y, x = stacked_tile.shape
            tile = numpy.ma.zeros((b, y, x)).astype(numpy.float32)

            # TODO: How to implement geomedian without introducing too many new dependencies?
            for xid in range(x):     # for each x-axis
                for yid in range(y): # for each y-axis
                    tile[:, yid, xid] = hd.geomedian(stacked_tile[:, :, yid, xid])

            # Convert back to uint16
            tile = (tile * 10000).astype(self.tile[0].dtype) if self.enforce_data_type else (tile * 10000)
            return tile.data, (tile[0] != 0) * 255
        else:
            return None, None

    def feed(self, tile):
        """Add data to tile."""
        self.tile.append(tile)

class MaxIndexMethod(MosaicMethodBase):

    def __init__(self, enforce_data_type=True, formula='(b2-b1)/(b2+b1)'):
        super(MaxIndexMethod, self).__init__()
        self.tile = []
        self.enforce_data_type = enforce_data_type
        self.formula = formula

    @property
    def data(self):
        """Return data and mask."""
        if self.tile:
            tile = numpy.ma.stack(self.tile, axis=0)
            t, b, y, x = tile.shape

            for n in range(b):
               self.formula = self.formula.replace(f'b{n+1}', f'tile[:, {n}, ...]')
            try:
                index = eval(self.formula)
            except NameError:
                raise NameError("the provided formula is invalid. "
                                 " bands must be specified with the letter 'b' followed with the band number, eg. 'b1'")

            argmax_index = numpy.ma.argmax(index, axis=0)
            ixgrid = numpy.ix_(numpy.arange(t), numpy.arange(y), numpy.arange(x))
            tile = tile[argmax_index, :, ixgrid[1], ixgrid[2]].squeeze(axis=0)
            tile = numpy.moveaxis(tile, -1, 0).astype(self.tile[0].dtype) if self.enforce_data_type \
                else numpy.moveaxis(tile, -1, 0)
            return tile.data, ~tile.mask[0] * 255
        else:
            return None, None

    def feed(self, tile):
        """Add data to tile."""
        self.tile.append(tile)