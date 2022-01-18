"""Setup for rio-tiler."""

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = [
    "attrs",
    "boto3",
    "numexpr",
    "numpy",
    "morecantile>=3.0,<3.1",
    "pydantic",
    "pystac>=0.5.4",
    "rasterio>=1.1.7",
    "httpx",
    "rio-color",
    "cachetools",
    "importlib_resources>=1.1.0;python_version<'3.9'",
]

extra_reqs = {
    "test": [
        "pytest",
        "pytest-asyncio",
        "pytest-benchmark",
        "pytest-cov",
        "rio-cogeo>=3.0.0",
    ],
    "dev": [
        "pytest",
        "pytest-benchmark",
        "pytest-cov",
        "pytest-asyncio",
        "rio-cogeo>=3.0.0",
        "pre-commit",
        "tox",
    ],
    "docs": ["nbconvert", "mkdocs", "mkdocs-material", "pygments", "mkdocs-jupyter"],
}

setup(
    name="rio-tiler",
    version="3.0.3",
    python_requires=">=3.7",
    description="User friendly Rasterio plugin to read raster datasets.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="cog cogeotiff raster map tiles gdal rasterio raster-processing slippy-map",
    author="Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/cogeotiff/rio-tiler",
    license="BSD",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={"rio_tiler": ["py.typed", "cmap_data/*.npy"]},
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
