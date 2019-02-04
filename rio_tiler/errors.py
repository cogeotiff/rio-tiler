"""Errors and warnings."""


class RioTilerError(Exception):
    """Base exception class."""


class InvalidFormat(RioTilerError):
    """Invalid image format."""


class TileOutsideBounds(RioTilerError):
    """Z-X-Y Tile is outside image bounds."""


class InvalidLandsatSceneId(RioTilerError):
    """Invalid Landsat-8 scene id."""


class InvalidSentinelSceneId(RioTilerError):
    """Invalid Sentinel-2 scene id."""


class InvalidCBERSSceneId(RioTilerError):
    """Invalid CBERS scene id."""


class InvalidBandName(RioTilerError):
    """Invalid band name."""


class DeprecationWarning(UserWarning):
    """Rio-tiler module deprecations warning."""


class NoOverviewWarning(UserWarning):
    """Dataset has no overviews."""
