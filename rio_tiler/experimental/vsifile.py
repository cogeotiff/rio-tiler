"""rio_tiler.io.Reader with VSIFILE/Obstore Opener."""

from typing import Union

import attr
import rasterio
from rasterio.io import DatasetReader, DatasetWriter, MemoryFile
from rasterio.vrt import WarpedVRT

from rio_tiler.io import Reader

try:
    import vsifile
    from vsifile.rasterio import opener
except ImportError:  # pragma: nocover
    vsifile = None  # type: ignore
    opener = None  # type: ignore


@attr.s
class VSIReader(Reader):
    """Rasterio Reader with VSIFILE opener."""

    dataset: Union[DatasetReader, DatasetWriter, MemoryFile, WarpedVRT] = attr.ib(
        default=None, init=False
    )

    def __attrs_post_init__(self):
        """Use vsifile.rasterio.opener as Python file opener."""
        assert vsifile is not None, "VSIFILE must be installed to use VSIReader"

        self.dataset = self._ctx_stack.enter_context(
            rasterio.open(self.input, opener=opener)
        )

        super().__attrs_post_init__()
