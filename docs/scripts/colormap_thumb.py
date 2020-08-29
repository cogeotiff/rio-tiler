"""
colormap_thumb.py: Create colormap thumbnails for documentation

This file is derived from the matplotlib documentation.
https://matplotlib.org/tutorials/colors/colormaps.html
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from rio_tiler.colormap import cmap, make_lut

cmaps = [
    ("Custom", ["cfastie", "rplumbo", "schwarzwald"]),
    (
        "Perceptually Uniform Sequential",
        ["viridis", "plasma", "inferno", "magma", "cividis"],
    ),
    (
        "Sequential",
        [
            "Greys",
            "Purples",
            "Blues",
            "Greens",
            "Oranges",
            "Reds",
            "YlOrBr",
            "YlOrRd",
            "OrRd",
            "PuRd",
            "RdPu",
            "BuPu",
            "GnBu",
            "PuBu",
            "YlGnBu",
            "PuBuGn",
            "BuGn",
            "YlGn",
        ],
    ),
    (
        "Sequential (2)",
        [
            "binary",
            "gist_yarg",
            "gist_gray",
            "gray",
            "bone",
            "pink",
            "spring",
            "summer",
            "autumn",
            "winter",
            "cool",
            "Wistia",
            "hot",
            "afmhot",
            "gist_heat",
            "copper",
        ],
    ),
    (
        "Diverging",
        [
            "PiYG",
            "PRGn",
            "BrBG",
            "PuOr",
            "RdGy",
            "RdBu",
            "RdYlBu",
            "RdYlGn",
            "Spectral",
            "coolwarm",
            "bwr",
            "seismic",
        ],
    ),
    ("Cyclic", ["twilight", "twilight_shifted", "hsv"]),
    (
        "Qualitative",
        [
            "Pastel1",
            "Pastel2",
            "Paired",
            "Accent",
            "Dark2",
            "Set1",
            "Set2",
            "Set3",
            "tab10",
            "tab20",
            "tab20b",
            "tab20c",
        ],
    ),
    (
        "Miscellaneous",
        [
            "flag",
            "prism",
            "ocean",
            "gist_earth",
            "terrain",
            "gist_stern",
            "gnuplot",
            "gnuplot2",
            "CMRmap",
            "cubehelix",
            "brg",
            "gist_rainbow",
            "rainbow",
            "jet",
            "nipy_spectral",
            "gist_ncar",
        ],
    ),
]


gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def make_colormap(name):
    """Use rio-tiler colormap to create matplotlib colormap
    """
    colormap = make_lut(cmap.get(name))
    # rescale to 0-1
    return ListedColormap(colormap / 255, name=name)


def plot_color_gradients(cmap_category, cmap_list):
    """Make
    """
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axes = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    axes[0].set_title(cmap_category + " colormaps", fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect="auto", cmap=make_colormap(name))
        ax.text(
            -0.01,
            0.5,
            name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    return fig


def main():
    """Create thumbnails"""
    for cmap_category, cmap_list in cmaps:
        plot_color_gradients(cmap_category, cmap_list)

        # Export fig
        out_path = (
            Path(__file__).parents[0]
            / ".."
            / "img"
            / (cmap_category.replace(" ", "_").lower() + ".png")
        )
        out_path.parents[0].mkdir(exist_ok=True)
        plt.savefig(out_path, dpi=200)


if __name__ == "__main__":
    main()
