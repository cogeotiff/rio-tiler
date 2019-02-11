"""Image file profiles."""

from rasterio.profiles import Profile


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
