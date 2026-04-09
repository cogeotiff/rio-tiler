"""create Zarr fixtures."""

import numpy
import zarr
from zarr.codecs import BloscCodec


def create_zarr(path: str) -> None:
    """Create a zarr archive."""
    arr = numpy.arange(0.0, 3599 * 1799 * 2, dtype="float32").reshape(2, 1799, 3599)
    arr[:, 0:50, 0:50] = 0  # we set the top-left corner to 0

    compressor = BloscCodec(cname="zstd", clevel=3, shuffle="shuffle", blocksize=0)

    # Create zarr group
    root = zarr.open_group(path, mode="w", zarr_format=3)

    # Create the main dataset array
    dataset = root.create_array(
        "dataset",
        shape=arr.shape,
        chunks=(1, 64, 64),
        dtype="float32",
        fill_value=0,
        compressors=[compressor],
        dimension_names=["time", "y", "x"],
        attributes={
            "valid_min": float(arr.min()),
            "valid_max": float(arr.max()),
        },
    )
    dataset[:] = arr

    # Create coordinate arrays
    x_coords = numpy.arange(-179.9, 180, 0.1)
    root.create_array(
        "x",
        data=x_coords,
        dimension_names=["x"],
    )

    y_coords = numpy.arange(89.9, -90, -0.1)
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
