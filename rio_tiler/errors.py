"""Errors and warnings."""


class RioTilerError(Exception):
    """Base exception class."""


class InvalidFormat(RioTilerError):
    """Invalid image format."""


class TileOutsideBounds(RioTilerError):
    """Z-X-Y Tile is outside image bounds."""


class PointOutsideBounds(RioTilerError):
    """Point is outside image bounds."""


class InvalidBandName(RioTilerError):
    """Invalid band name."""


class InvalidColorMapName(Exception):
    """Invalid colormap name."""


class AlphaBandWarning(UserWarning):
    """Automaticaly removed Alpha band from output array."""


class NoOverviewWarning(UserWarning):
    """Dataset has no overviews."""


class InvalidAssetName(RioTilerError):
    """Invalid Asset name."""


class MissingAssets(RioTilerError):
    """Missing Assets."""


class MissingBands(RioTilerError):
    """Missing bands."""


class ExpressionMixingWarning(UserWarning):
    """Expression and assets/indexes mixing."""


class InvalidMosaicMethod(RioTilerError):
    """Invalid Pixel Selection method for mosaic."""


class ColorMapAlreadyRegistered(Exception):
    """ColorMap is already registered."""


class EmptyMosaicError(RioTilerError):
    """Mosaic method returned empty array."""
