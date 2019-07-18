"""tests rio_tiler.utils"""

from rio_tiler import cmap, utils


def test_get_cmaplist():
    """Should work as expected return cmap names."""
    assert len(cmap.cmap_list) == 167
    for name in cmap.cmap_list:
        cm = utils.get_colormap(name, format="gdal")
        assert cm.shape == (256, 3)
        assert cm.dtype == "uint8"
