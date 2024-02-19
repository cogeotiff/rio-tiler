"""rio_tiler.mosaic.methods.defaults: default mosaic filling methods."""

from dataclasses import dataclass, field
from typing import List, Optional

import numpy

from rio_tiler.mosaic.methods.base import MosaicMethodBase


@dataclass
class FirstMethod(MosaicMethodBase):
    """Feed the mosaic array with the first pixel available."""

    exit_when_filled: bool = field(default=True, init=False)

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add data to the mosaic array."""
        if self.mosaic is None:
            self.mosaic = array

        else:
            pidex = self.mosaic.mask & ~array.mask

            mask = numpy.where(pidex, array.mask, self.mosaic.mask)
            self.mosaic = numpy.ma.where(pidex, array, self.mosaic)
            self.mosaic.mask = mask


@dataclass
class HighestMethod(MosaicMethodBase):
    """Feed the mosaic array with the highest pixel values."""

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add data to the mosaic array."""
        if self.mosaic is None:
            self.mosaic = array

        else:
            pidex = (
                numpy.bitwise_and(array.data > self.mosaic.data, ~array.mask)
                | self.mosaic.mask
            )

            mask = numpy.where(pidex, array.mask, self.mosaic.mask)
            self.mosaic = numpy.ma.where(pidex, array, self.mosaic)
            self.mosaic.mask = mask


@dataclass
class LowestMethod(MosaicMethodBase):
    """Feed the mosaic array with the lowest pixel values."""

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add data to the mosaic array."""
        if self.mosaic is None:
            self.mosaic = array

        else:
            pidex = (
                numpy.bitwise_and(array.data < self.mosaic.data, ~array.mask)
                | self.mosaic.mask
            )

            mask = numpy.where(pidex, array.mask, self.mosaic.mask)
            self.mosaic = numpy.ma.where(pidex, array, self.mosaic)
            self.mosaic.mask = mask


@dataclass
class MeanMethod(MosaicMethodBase):
    """Stack the arrays and return the Mean pixel value."""

    enforce_data_type: bool = True
    stack: List[numpy.ma.MaskedArray] = field(default_factory=list, init=False)

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return Mean of the data stack."""
        if self.stack:
            array = numpy.ma.mean(numpy.ma.stack(self.stack, axis=0), axis=0)
            if self.enforce_data_type:
                array = array.astype(self.stack[0].dtype)

            return array

        return None

    def feed(self, array: numpy.ma.MaskedArray):
        """Add array to the stack."""
        self.stack.append(array)


@dataclass
class MedianMethod(MosaicMethodBase):
    """Stack the arrays and return the Median pixel value."""

    enforce_data_type: bool = True
    stack: List[numpy.ma.MaskedArray] = field(default_factory=list, init=False)

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return Median of the data stack."""
        if self.stack:
            array = numpy.ma.median(numpy.ma.stack(self.stack, axis=0), axis=0)
            if self.enforce_data_type:
                array = array.astype(self.stack[0].dtype)

            return array

        return None

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add array to the stack."""
        self.stack.append(array)


@dataclass
class StdevMethod(MosaicMethodBase):
    """Stack the arrays and return the Standard Deviation value."""

    stack: List[numpy.ma.MaskedArray] = field(default_factory=list, init=False)

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return STDDEV of the data stack."""
        if self.stack:
            return numpy.ma.std(numpy.ma.stack(self.stack, axis=0), axis=0)

        return None

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add array to the stack."""
        self.stack.append(array)


@dataclass
class LastBandHighMethod(MosaicMethodBase):
    """Feed the mosaic array using the last band as decision factor (highest value)."""

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return data."""
        if self.mosaic is not None:
            return self.mosaic[:-1].copy()

        return None

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add data to the mosaic array."""
        if self.mosaic is None:
            self.mosaic = array

        else:
            pidex = (
                numpy.bitwise_and(array.data[-1] > self.mosaic.data[-1], ~array.mask)
                | self.mosaic.mask
            )

            mask = numpy.where(pidex, array.mask, self.mosaic.mask)
            self.mosaic = numpy.ma.where(pidex, array, self.mosaic)
            self.mosaic.mask = mask


@dataclass
class LastBandLowMethod(MosaicMethodBase):
    """Feed the mosaic array using the last band as decision factor (lowest value)."""

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return data."""
        if self.mosaic is not None:
            return self.mosaic[:-1].copy()

        return None

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add data to the mosaic array."""
        if self.mosaic is None:
            self.mosaic = array

        else:
            pidex = (
                numpy.bitwise_and(array.data[-1] < self.mosaic.data[-1], ~array.mask)
                | self.mosaic.mask
            )

            mask = numpy.where(pidex, array.mask, self.mosaic.mask)
            self.mosaic = numpy.ma.where(pidex, array, self.mosaic)
            self.mosaic.mask = mask


@dataclass
class CountMethod(MosaicMethodBase):
    """Stack the arrays and return the valid pixel count."""

    stack: List[numpy.ma.MaskedArray] = field(default_factory=list, init=False)

    @property
    def data(self) -> Optional[numpy.ma.MaskedArray]:
        """Return valid data count of the data stack."""
        if self.stack:
            data = numpy.ma.count(numpy.ma.stack(self.stack, axis=0), axis=0)

            # only need unint8 for small mosaic stacks
            if len(self.stack) < 256:
                data = data.astype(numpy.uint8)

            # only need the counts from one band
            if len(data.shape) > 2:
                data = data[0]

            # mask is always empty
            mask = numpy.zeros(data.shape, dtype=bool)
            array = numpy.ma.MaskedArray(data, mask)

            return array

        return None

    def feed(self, array: Optional[numpy.ma.MaskedArray]):
        """Add array to the stack."""
        self.stack.append(array)
