"""Setup for rio-tiler."""

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["numpy", "numexpr", "mercantile", "rasterio[s3]>=1.1.3", "rio-toa"]

extra_reqs = {
    "test": ["mock", "pytest", "pytest-benchmark", "pytest-cov", "rio-cogeo"],
    "dev": [
        "mock",
        "pytest",
        "pytest-benchmark",
        "pytest-cov",
        "rio-cogeo",
        "pre-commit",
    ],
}

setup(
    name="rio-tiler",
    version="2.0a2",
    python_requires=">=3",
    description=u"""Get mercator tile from CloudOptimized GeoTIFF and other cloud hosted raster such as CBERS-4, Sentinel-2, Sentinel-1 and Landsat-8 AWS PDS""",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
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
