"""Setup for rio-tiler."""

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["numpy", "numexpr", "mercantile", "boto3", "rasterio[s3]~=1.0", "rio-toa"]

extra_reqs = {
    "test": ["mock", "pytest", "pytest-cov"],
    "dev": ["mock", "pytest", "pytest-cov", "pre-commit"],
}

setup(
    name="rio-tiler",
    version="1.2.11",
    description=u"""Get mercator tile from CloudOptimized GeoTIFF and other cloud hosted raster such as CBERS-4, Sentinel-2 and Landsat-8 AWS PDS""",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="COG cogeo raster aws map tiler gdal rasterio",
    author=u"Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/cogeotiff/rio-tiler",
    license="BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    package_data={"rio_tiler": ["cmap/*.npy"]},
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
