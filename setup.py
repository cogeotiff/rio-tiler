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
    "mercantile",
    "morecantile>=2.0,<2.1",
    "rasterio>=1.1.7",
    "requests",
    "rio-color",
]

extra_reqs = {
    "test": ["pytest", "pytest-benchmark", "pytest-cov", "rio-cogeo"],
    "dev": [
        "pytest",
        "pytest-benchmark",
        "pytest-cov",
        "pytest-asyncio",
        "rio-cogeo",
        "pre-commit",
    ],
    "docs": ["nbconvert", "mkdocs", "mkdocs-material", "pygments", "mkdocs-jupyter"],
}

setup(
    name="rio-tiler",
    version="2.0.0rc2",
    python_requires=">=3.5",
    description="Rasterio plugin to read mercator tiles from Cloud Optimized GeoTIFF.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="COG cogeo raster aws map tiles gdal rasterio",
    author="Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/cogeotiff/rio-tiler",
    license="BSD",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={"rio_tiler": ["cmap_data/*.npy"]},
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
