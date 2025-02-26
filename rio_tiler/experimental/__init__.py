"""The "experimental" module of rio-tiler contains potential new features that are subject to change."""

import warnings

from rio_tiler.errors import RioTilerExperimentalWarning

warnings.warn(
    "This module is experimental, its contents are subject to change and deprecation.",
    category=RioTilerExperimentalWarning,
)
