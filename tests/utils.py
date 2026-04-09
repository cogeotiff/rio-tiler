"""create Zarr fixtures."""

from datetime import datetime

import numpy
import xarray
from zarr.codecs import BloscCodec


def create_zarr(path: str) -> None:
    """Create a archive."""
    arr = numpy.arange(0.0, 3599 * 1799 * 2, dtype="float32").reshape(2, 1799, 3599)
    arr[:, 0:50, 0:50] = 0  # we set the top-left corner to 0

    data = xarray.DataArray(
        arr,
        dims=("time", "y", "x"),
        coords={
            "x": numpy.arange(-179.9, 180, 0.1),
            "y": numpy.arange(89.9, -90, -0.1),
            "time": [datetime(2022, 1, 1), datetime(2022, 1, 2)],
        },
    )
    data.attrs.update(
        {
            "valid_min": arr.min(),
            "valid_max": arr.max(),
        }
    )
    ds = data.to_dataset(name="dataset")

    compressor = BloscCodec(cname="zstd", clevel=3, shuffle="shuffle", blocksize=0)

    def create_encoding(ds, spatial_chunk=64):
        """Create encoding for dataset variables."""
        encoding = {}
        for var in ds.data_vars:
            data_shape = ds[var].shape
            if len(data_shape) >= 2:
                chunk_y = min(spatial_chunk, data_shape[-2])
                chunk_x = min(spatial_chunk, data_shape[-1])
                chunks = (chunk_y, chunk_x)
            else:
                chunks = (min(spatial_chunk, data_shape[-1]),)

            encoding[var] = {
                "compressors": [compressor],
                "chunks": chunks,
                "fill_value": 0,
            }

        # Add coordinate encoding
        for coord in ds.coords:
            encoding[coord] = {"compressors": None}

        return encoding

    encoding = create_encoding(ds)

    ds.to_zarr(
        path,
        mode="w",
        consolidated=True,
        zarr_format=3,
        encoding=encoding,
    )
