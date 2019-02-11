"""Image file profiles."""

import warnings

from rasterio.profiles import Profile
from rio_tiler.errors import InvalidFormat, DeprecationWarning


class JPEGProfile(Profile):
    """JPEG creation options ref: https://www.gdal.org/frmt_jpeg.html."""

    defaults = {"quality": 85}


class PNGProfile(Profile):
    """PNG creation options ref: https://www.gdal.org/frmt_png.html."""

    defaults = {"zlevel": 6}


class PNGRAWProfile(Profile):
    """PNG creation options ref: https://www.gdal.org/frmt_png.html."""

    defaults = {"zlevel": 1}


class WEBPProfile(Profile):
    """WEBP creation options ref: https://www.gdal.org/frmt_webp.html."""

    defaults = {"quality": 75, "lossless": False}


class ImagesProfiles(dict):
    """
    GDAL Image creation options.

    ref: https://github.com/mapnik/mapnik/wiki/Image-IO#default-output-details.

    """

    def __init__(self):
        """Initialize COGProfiles dict."""
        self.update(
            {
                "jpeg": JPEGProfile(),
                "png": PNGProfile(),
                "pngraw": PNGRAWProfile(),
                "webp": WEBPProfile(),
            }
        )


img_profiles = ImagesProfiles()


def get(name):
    """https://github.com/mapnik/mapnik/wiki/Image-IO#default-output-details."""
    warnings.warn(
        "Pillow compatible profile will be removed in 1.0.0", DeprecationWarning
    )
    if name == "jpeg":
        """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg"""
        return {"quality": 95}

    elif name == "png":
        """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png"""
        return {"compress_level": 0}

    elif name == "webp":
        """https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp"""
        return {"quality": 80}
    else:
        raise InvalidFormat("{} format is not supported".format(name))
