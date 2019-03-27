"""Setup for rio-tiler."""

from setuptools import setup, find_packages

with open("rio_tiler/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


with open("README.rst") as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["numpy", "numexpr", "mercantile", "boto3", "rasterio[s3]~=1.0", "rio-toa"]

extra_reqs = {
    "test": ["mock", "pytest", "pytest-cov"],
    "dev": ["mock", "pytest", "pytest-cov", "pre-commit"],
}

setup(
    name="rio_tiler",
    version=version,
    description=u"""Get mercator tile from landsat,
          sentinel or other AWS hosted raster""",
    long_description=readme,
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="raster aws tiler gdal rasterio",
    author=u"Vincent Sarago",
    author_email="vincent.sarago@mapbox.com",
    url="https://github.com/mapbox/rio-tiler",
    license="BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    package_data={"cmap": ["*.txt"]},
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
)
