"""create Zarr fixtures."""

from typing import Any

import numpy
import zarr
from affine import Affine
from zarr.codecs import BloscCodec


def create_zarr(path: str, geozarr: bool = False) -> None:
    """Create a zarr archive."""
    arr = numpy.arange(0.0, 3600 * 1800 * 2, dtype="float32").reshape(2, 1800, 3600)
    arr[:, 0:50, 0:50] = 0  # we set the top-left corner to 0

    compressor = BloscCodec(cname="zstd", clevel=3, shuffle="shuffle", blocksize=0)

    # Create zarr group
    root = zarr.open_group(path, mode="w", zarr_format=3)

    attributes: dict[str, Any] = {
        "valid_min": float(arr.min()),
        "valid_max": float(arr.max()),
    }
    if geozarr:
        attributes["zarr_conventions"] = [
            {
                "schema_url": "https://raw.githubusercontent.com/zarr-conventions/spatial/refs/tags/v1/schema.json",
                "spec_url": "https://github.com/zarr-conventions/spatial/blob/v1/README.md",
                "uuid": "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4",
                "name": "spatial:",
                "description": "Spatial coordinate information",
            },
            {
                "schema_url": "https://raw.githubusercontent.com/zarr-experimental/geo-proj/refs/tags/v1/schema.json",
                "spec_url": "https://github.com/zarr-experimental/geo-proj/blob/v1/README.md",
                "uuid": "f17cb550-5864-4468-aeb7-f3180cfb622f",
                "name": "proj:",
                "description": "Coordinate reference system information for geospatial data",
            },
        ]
        attributes.update(
            {
                "spatial:dimensions": ["y", "x"],
                "spatial:transform": list(
                    Affine.translation(-180, 90) * Affine.scale(0.1, -0.1)
                ),
                "proj:code": "EPSG:4326",
            }
        )

    # Create the main dataset array
    dataset = root.create_array(
        "dataset",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        compressors=[compressor],
        dimension_names=["time", "y", "x"],
        attributes=attributes,
    )
    dataset[:] = arr

    # Create coordinate arrays
    # NOTE: in Xarray/rioxarray world they consider the node coordinate (center of pixel)
    x_coords = numpy.arange(-179.9, 180.1, 0.1)
    root.create_array(
        "x",
        data=x_coords,
        dimension_names=["x"],
    )

    # NOTE: in Xarray/rioxarray world they consider the node coordinate (center of pixel)
    y_coords = numpy.arange(89.9, -90.1, -0.1)
    root.create_array(
        "y",
        data=y_coords,
        dimension_names=["y"],
    )

    time_coords = numpy.array(["2022-01-01", "2022-01-02"], dtype="datetime64[D]")
    root.create_array(
        "time",
        data=time_coords,
        dimension_names=["time"],
    )

    # Write consolidated metadata
    zarr.consolidate_metadata(root.store)
