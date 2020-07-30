"""Errors and warnings."""


class RioTilerError(Exception):
    """Base exception class."""


class InvalidFormat(RioTilerError):
    """Invalid image format."""


class TileOutsideBounds(RioTilerError):
    """Z-X-Y Tile is outside image bounds."""


class InvalidBandName(RioTilerError):
    """Invalid band name."""


class InvalidColorMapName(Exception):
    """Invalid colormap name."""


class DeprecationWarning(UserWarning):
    """Rio-tiler module deprecations warning."""


class AlphaBandWarning(UserWarning):
    """Automaticaly removed Alpha band from output array."""


class NoOverviewWarning(UserWarning):
    """Dataset has no overviews."""


class InvalidAssetName(RioTilerError):
    """Invalid Asset name."""


class MissingAssets(RioTilerError):
    """Missing Assets."""
