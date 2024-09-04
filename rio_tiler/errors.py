"""Errors and warnings."""


class RioTilerError(Exception):
    """Base exception class."""


class InvalidFormat(RioTilerError):
    """Invalid image format."""


class TileOutsideBounds(RioTilerError):
    """Z-X-Y Tile is outside image bounds."""


class InvalidBufferSize(RioTilerError):
    "`buffer` must be a multiple of `0.5` (e.g: 0.5, 1, 1.5, ...)."


class PointOutsideBounds(RioTilerError):
    """Point is outside image bounds."""


class InvalidBandName(RioTilerError):
    """Invalid band name."""


class InvalidColorMapName(RioTilerError):
    """Invalid colormap name."""


class AlphaBandWarning(UserWarning):
    """Automatically removed Alpha band from output array."""


class NoOverviewWarning(UserWarning):
    """Dataset has no overviews."""


class InvalidAssetName(RioTilerError):
    """Invalid Asset name."""


class InvalidExpression(RioTilerError):
    """Invalid Expression."""


class MissingAssets(RioTilerError):
    """Missing Assets."""


class MissingBands(RioTilerError):
    """Missing bands."""


class ExpressionMixingWarning(UserWarning):
    """Expression and assets/indexes mixing."""


class InvalidMosaicMethod(RioTilerError):
    """Invalid Pixel Selection method for mosaic."""


class ColorMapAlreadyRegistered(RioTilerError):
    """ColorMap is already registered."""


class EmptyMosaicError(RioTilerError):
    """Mosaic method returned empty array."""


class InvalidColorFormat(RioTilerError):
    """Invalid color format."""


class InvalidDatatypeWarning(UserWarning):
    """Invalid Output Datatype."""


class AssetAsBandError(RioTilerError):
    """Can't use asset_as_band with multiple bands."""


class InvalidPointDataError(RioTilerError):
    """Invalid PointData."""


class MissingCRS(RioTilerError):
    """Dataset doesn't have CRS information."""


class InvalidGeographicBounds(RioTilerError):
    """Invalid Geographic bounds."""
