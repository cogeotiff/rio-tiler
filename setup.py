"""Fake rio-tiler setup.py for github."""
import sys

from setuptools import setup

sys.stderr.write(
    """
===============================
Unsupported installation method
===============================
rio-tiler no longer supports installation with `python setup.py install`.
Please use `python -m pip install .` instead.
"""
)
sys.exit(1)


# The below code will never execute, however GitHub is particularly
# picky about where it finds Python packaging metadata.
# See: https://github.com/github/feedback/discussions/6456
#
# To be removed once GitHub catches up.

setup(
    name="rio-tiler",
    install_requires=[
        "attrs",
        "boto3",
        "cachetools",
        "httpx",
        "numexpr",
        "numpy",
        "morecantile>=3.1,<4.0",
        "pydantic",
        "pystac>=0.5.4",
        "rasterio>=1.3.0",
        "color-operations",
        "importlib_resources>=1.1.0; python_version < '3.9'",
    ],
)
