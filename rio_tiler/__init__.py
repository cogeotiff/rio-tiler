"""rio-tiler."""

import pkg_resources

from . import (  # noqa
    colormap,
    constants,
    errors,
    expression,
    io,
    mercator,
    mosaic,
    profiles,
    reader,
    tasks,
    utils,
)

version = pkg_resources.get_distribution(__package__).version
