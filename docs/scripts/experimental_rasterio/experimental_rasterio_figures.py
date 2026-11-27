"""Generate the figures used in docs/src/experimental/rasterio.md.

    uv run --with matplotlib python docs/scripts/experimental_rasterio/experimental_rasterio_figures.py

Figures are written to docs/src/img/experimental-rasterio/:

- pipelines.png: rio_tiler.io.Reader vs rio_tiler.experimental.rasterio.Reader pipelines
- read-then-warp.png: window read in the dataset CRS vs tile returned in the output CRS
- tiles-comparison.png: tiles from both readers and their differences
- agreement-per-zoom.png: per-zoom agreement for all the tiles covering tests/fixtures/cog.tif

The per-zoom numbers are also printed (zoom, tiles, median/worst different
values in pixels, median/worst mask mismatch in pixels), to update the table
in the docs.
"""

import os
import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy  # noqa: E402
from matplotlib.colors import ListedColormap  # noqa: E402
from matplotlib.patches import (  # noqa: E402
    FancyArrowPatch,
    FancyBboxPatch,
    Polygon,
    Rectangle,
)
from morecantile import Tile  # noqa: E402
from rasterio.warp import transform as transform_coords  # noqa: E402

warnings.simplefilter("ignore")

from rio_tiler.experimental.rasterio import Reader as ExpReader  # noqa: E402
from rio_tiler.io import Reader  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(ROOT, "docs", "src", "img", "experimental-rasterio")
FIX = os.path.join(ROOT, "tests", "fixtures")
os.makedirs(OUT, exist_ok=True)

# Reference palette (light mode)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#8a8985"
GRID = "#e4e3df"
BLUE = "#2a78d6"  # slot 1
ORANGE = "#eb6834"  # slot 2
AQUA = "#1baf7a"  # slot 3
MASKED = "#d9d8d3"

plt.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "text.color": INK,
        "axes.labelcolor": INK2,
        "axes.edgecolor": GRID,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
    }
)


def _save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=150, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", path)


# -----------------------------------------------------------------------------
# 1. Pipelines diagram
# -----------------------------------------------------------------------------
def pipelines():
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 52)
    ax.axis("off")

    def box(x, y, w, h, title, sub, color):
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.4,rounding_size=1.2",
                fc="white",
                ec=color,
                lw=2,
            )
        )
        ax.text(
            x + w / 2,
            y + h - 2.6,
            title,
            ha="center",
            va="top",
            weight="bold",
            fontsize=9.5,
        )
        ax.text(
            x + w / 2,
            y + h - 6.6,
            sub,
            ha="center",
            va="top",
            fontsize=8,
            color=INK2,
            linespacing=1.35,
        )

    def arrow(x0, x1, y):
        ax.add_patch(
            FancyArrowPatch(
                (x0, y), (x1, y), arrowstyle="-|>", mutation_scale=12, lw=1.4, color=MUTED
            )
        )

    # Lane 1: WarpedVRT
    ax.text(
        0,
        50.5,
        "rio_tiler.io.Reader  —  warp on read (GDAL WarpedVRT)",
        weight="bold",
        fontsize=11,
        color=BLUE,
    )
    y1, h = 30, 16
    box(0.5, y1, 22, h, "Output grid", "bbox + width/height\nin the output CRS", BLUE)
    box(
        29,
        y1,
        30,
        h,
        "WarpedVRT",
        "virtual dataset in the\noutput CRS, aligned with\nthe requested bounds",
        BLUE,
    )
    box(
        65.5,
        y1,
        22,
        h,
        "vrt.read()",
        "GDAL picks the overview\nand warps each output\npixel from the source",
        BLUE,
    )
    box(94, y1, 15.5, h, "ImageData", "output CRS\n+ footprint mask", BLUE)
    for a, b in [(23.5, 28.5), (59.8, 65), (88.4, 93.5)]:
        arrow(a, b, y1 + h / 2)

    # Lane 2: experimental
    ax.text(
        0,
        24.5,
        "rio_tiler.experimental.rasterio.Reader  —  read native, then warp",
        weight="bold",
        fontsize=11,
        color=ORANGE,
    )
    y2 = 4
    box(0.5, y2, 17, h, "Source window", "bbox → window in\nthe dataset CRS", ORANGE)
    box(
        22.5,
        y2,
        19,
        h,
        "Pick overview",
        "from the output\nresolution (same rule\nas async-geotiff)",
        ORANGE,
    )
    box(
        46.5,
        y2,
        21,
        h,
        "dataset.read()",
        "window + out_shape at\noverview resolution\n(native pixels, no warp)",
        ORANGE,
    )
    box(
        72.5,
        y2,
        17,
        h,
        "_warp.warp()",
        "warp onto the output\ngrid in one pass\n(rasterio.warp)",
        ORANGE,
    )
    box(94, y2, 15.5, h, "ImageData", "output CRS\n+ mask", ORANGE)
    for a, b in [(18.4, 22), (42.4, 46), (68.4, 72), (90.4, 93.5)]:
        arrow(a, b, y2 + h / 2)

    _save(fig, "pipelines.png")


# -----------------------------------------------------------------------------
# 2. What is read (dataset CRS) vs what is returned (output CRS)
# -----------------------------------------------------------------------------
def geometry():
    path = os.path.join(FIX, "cog.tif")
    with ExpReader(path) as src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        t = src.tms.tile((w + e) / 2, (s + n) / 2, src.minzoom + 1)
        bbox = src.tms.xy_bounds(Tile(t.x, t.y, t.z))

        # Replay `part` steps to get the source window that is read
        captured = {}
        orig_read = src._read

        def spy(**kwargs):
            img = orig_read(**kwargs)
            captured["img"] = img
            captured["window"] = kwargs.get("window")
            captured["out_shape"] = kwargs.get("out_shape")
            return img

        src._read = spy
        tile = src.tile(t.x, t.y, t.z)
        src._read = orig_read
        native = captured["img"]
        decim = round(captured["window"].width / captured["out_shape"][1])

        # Tile footprint (densified) in dataset CRS
        xs = numpy.concatenate(
            [
                numpy.linspace(bbox.left, bbox.right, 50),
                numpy.full(50, bbox.right),
                numpy.linspace(bbox.right, bbox.left, 50),
                numpy.full(50, bbox.left),
            ]
        )
        ys = numpy.concatenate(
            [
                numpy.full(50, bbox.top),
                numpy.linspace(bbox.top, bbox.bottom, 50),
                numpy.full(50, bbox.bottom),
                numpy.linspace(bbox.bottom, bbox.top, 50),
            ]
        )
        fx, fy = transform_coords(src.tms.rasterio_crs, src.crs, xs, ys)

        fig, (a1, a2) = plt.subplots(
            1, 2, figsize=(11, 5.4), gridspec_kw={"wspace": 0.25}
        )

        # Left: native read in dataset CRS
        nb = native.bounds
        data = native.array[0]
        a1.imshow(
            numpy.ma.masked_array(data.data, mask=data.mask),
            extent=(nb[0], nb[2], nb[1], nb[3]),
            cmap="Greys_r",
        )
        a1.add_patch(Polygon(numpy.c_[fx, fy], closed=True, fill=False, ec=ORANGE, lw=2))
        a1.add_patch(
            Rectangle(
                (nb[0], nb[1]),
                nb[2] - nb[0],
                nb[3] - nb[1],
                fill=False,
                ec=BLUE,
                lw=2,
                ls="--",
            )
        )
        a1.set_title(
            f"1. Read in the dataset CRS ({src.crs.to_string()})\n"
            f"window {data.shape[1]}×{data.shape[0]} px at overview 1/{decim}",
            loc="left",
        )
        a1.set_xlim(nb[0] - (nb[2] - nb[0]) * 0.08, nb[2] + (nb[2] - nb[0]) * 0.08)
        a1.set_ylim(nb[1] - (nb[3] - nb[1]) * 0.08, nb[3] + (nb[3] - nb[1]) * 0.08)
        a1.tick_params(labelsize=7)
        a1.ticklabel_format(style="plain", useOffset=False)
        a1.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
        from matplotlib.lines import Line2D

        a1.legend(
            handles=[
                Line2D(
                    [],
                    [],
                    color=BLUE,
                    lw=2,
                    ls="--",
                    label="read window (clamped to the dataset)",
                ),
                Line2D(
                    [], [], color=ORANGE, lw=2, label="tile footprint in the dataset CRS"
                ),
            ],
            loc="upper center",
            bbox_to_anchor=(0.5, -0.07),
            frameon=False,
            fontsize=8.5,
            ncol=1,
        )

        # Right: final tile in output CRS
        tb = tile.bounds
        td = tile.array[0]
        a2.imshow(
            numpy.ma.masked_array(td.data, mask=td.mask),
            extent=(tb[0], tb[2], tb[1], tb[3]),
            cmap="Greys_r",
        )
        a2.add_patch(
            Rectangle(
                (tb[0], tb[1]), tb[2] - tb[0], tb[3] - tb[1], fill=False, ec=ORANGE, lw=2
            )
        )
        a2.set_title(
            f"2. Warped to the output CRS (EPSG:3857)\ntile {t.z}/{t.x}/{t.y} — {td.shape[1]}×{td.shape[0]} px",
            loc="left",
        )
        a2.tick_params(labelsize=7)
        a2.ticklabel_format(style="plain", useOffset=False)
        for a in (a1, a2):
            a.set_facecolor(MASKED)

    _save(fig, "read-then-warp.png")


# -----------------------------------------------------------------------------
# 3. Visual comparison of tiles
# -----------------------------------------------------------------------------
def _diff_rgb(a, b):
    """Return RGB image: gray = same, orange = value differs, blue = mask differs."""
    am, bm = numpy.ma.getmaskarray(a.array)[0], numpy.ma.getmaskarray(b.array)[0]
    both = ~am & ~bm
    vdiff = numpy.zeros(am.shape, bool)
    vdiff[both] = (a.array.data[:, both] != b.array.data[:, both]).any(axis=0)
    mdiff = am != bm

    def hex2rgb(h):
        return numpy.array([int(h[i : i + 2], 16) / 255 for i in (1, 3, 5)])

    out = numpy.ones(am.shape + (3,)) * hex2rgb(SURFACE)
    out[both] = hex2rgb("#c9c8c3")
    out[vdiff] = hex2rgb(ORANGE)
    out[mdiff] = hex2rgb(BLUE)
    return out, vdiff.sum() / max(both.sum(), 1), mdiff.mean()


def _show(ax, img):
    if img.array.shape[0] >= 3:
        rgb = img.array.data[:3].transpose(1, 2, 0).astype("float32")
        rgb = rgb / max(rgb.max(), 1)
        m = numpy.ma.getmaskarray(img.array)[0]
        rgba = numpy.dstack([rgb, (~m).astype("float32")])
        ax.imshow(numpy.ones(m.shape + (3,)) * 0.85)
        ax.imshow(rgba)
    else:
        cmap = plt.get_cmap("Greys_r").copy()
        cmap.set_bad(MASKED)
        ax.imshow(img.array[0], cmap=cmap)


def tiles():
    cases = []
    with ExpReader(os.path.join(FIX, "cog.tif")) as src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        cx, cy = (w + e) / 2, (s + n) / 2
        for z in (src.minzoom + 1, src.maxzoom):
            t = src.tms.tile(cx, cy, z)
            cases.append(("cog.tif", t, f"cog.tif — z{z} (no nodata, footprint mask)"))
    with ExpReader(os.path.join(FIX, "cog_uint8_rgba.tif")) as src:
        w2, s2, e2, n2 = src.get_geographic_bounds("epsg:4326")
        t = src.tms.tile((w2 + e2) / 2, (s2 + n2) / 2, src.minzoom + 1)
        cases.append(
            ("cog_uint8_rgba.tif", t, f"cog_uint8_rgba.tif — z{t.z} (alpha band)")
        )

    fig, axes = plt.subplots(
        len(cases),
        3,
        figsize=(10.5, 3.9 * len(cases)),
        gridspec_kw={"wspace": 0.05, "hspace": 0.45},
    )
    for row, (name, t, label) in zip(axes, cases):
        p = os.path.join(FIX, name)
        with Reader(p) as sync_src, ExpReader(p) as exp_src:
            a = sync_src.tile(t.x, t.y, t.z)
            b = exp_src.tile(t.x, t.y, t.z)
        _show(row[0], a)
        _show(row[1], b)
        rgb, vfrac, mfrac = _diff_rgb(a, b)
        row[2].imshow(rgb)
        row[0].set_title("rio_tiler.io.Reader", loc="left", fontsize=10)
        row[1].set_title("experimental.rasterio.Reader", loc="left", fontsize=10)
        row[2].set_title(
            f"Difference — values {vfrac:.1%} · mask {mfrac:.2%}",
            loc="left",
            fontsize=10,
        )
        row[0].text(
            0,
            1.17,
            label,
            transform=row[0].transAxes,
            fontsize=11.5,
            weight="bold",
            color=INK,
        )
        for ax in row:
            ax.set_xticks([])
            ax.set_yticks([])
            for sp in ax.spines.values():
                sp.set_color(GRID)

    # legend
    fig.legend(
        handles=[
            Rectangle((0, 0), 1, 1, color="#c9c8c3", label="same value"),
            Rectangle(
                (0, 0), 1, 1, color=ORANGE, label="different value (valid in both)"
            ),
            Rectangle(
                (0, 0),
                1,
                1,
                color=BLUE,
                label="different mask (valid in one reader only)",
            ),
        ],
        loc="lower center",
        bbox_to_anchor=(0.5, 0.06),
        ncol=3,
        frameon=False,
        fontsize=9.5,
        handlelength=1.2,
        handleheight=1.2,
    )
    _save(fig, "tiles-comparison.png")


# -----------------------------------------------------------------------------
# 4. Agreement per zoom level (cog.tif)
# -----------------------------------------------------------------------------
def per_zoom():
    path = os.path.join(FIX, "cog.tif")
    zooms, same_med, same_min, mask_med, mask_max = [], [], [], [], []
    with Reader(path) as sync_src, ExpReader(path) as src:
        w, s, e, n = src.get_geographic_bounds("epsg:4326")
        for z in range(src.minzoom, src.maxzoom + 1):
            ul, lr = src.tms.tile(w, n, z), src.tms.tile(e, s, z)
            same, mism = [], []
            for x in range(ul.x, lr.x + 1):
                for y in range(ul.y, lr.y + 1):
                    try:
                        b = src.tile(x, y, z)
                    except Exception:
                        continue
                    a = sync_src.tile(x, y, z)
                    am, bm = a.array.mask[0], b.array.mask[0]
                    both = ~am & ~bm
                    same.append(
                        int((a.array.data[0][both] != b.array.data[0][both]).sum())
                    )
                    mism.append(int((am != bm).sum()))
            zooms.append(z)
            same_med.append(numpy.median(same))
            same_min.append(numpy.max(same))
            mask_med.append(numpy.median(mism))
            mask_max.append(numpy.max(mism))
            print(
                z,
                len(mism),
                round(same_med[-1], 2),
                round(same_min[-1], 2),
                round(mask_med[-1], 3),
                round(mask_max[-1], 3),
            )

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 3.6), gridspec_kw={"wspace": 0.28})
    for ax in (a1, a2):
        ax.grid(axis="y", color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.set_xticks(zooms)
        ax.set_xlabel("zoom level")

    a1.plot(zooms, same_med, color=BLUE, lw=2, marker="o", ms=6, mec=SURFACE, mew=1.5)
    a1.plot(
        zooms,
        same_min,
        color=BLUE,
        lw=2,
        ls="--",
        marker="o",
        ms=6,
        mec=SURFACE,
        mew=1.5,
        alpha=0.55,
    )
    a1.set_ylim(-0.1, 5)
    a1.set_yticks(range(0, 6))
    a1.set_title("Different values (pixels per 256×256 tile)", loc="left")
    a1.annotate(
        "median tile",
        (zooms[2], same_med[2]),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        color=INK2,
        fontsize=9,
    )
    a1.annotate(
        "worst tile",
        (zooms[0], same_min[0]),
        xytext=(8, 4),
        textcoords="offset points",
        ha="center",
        color=INK2,
        fontsize=9,
    )

    a2.plot(zooms, mask_med, color=ORANGE, lw=2, marker="o", ms=6, mec=SURFACE, mew=1.5)
    a2.plot(
        zooms,
        mask_max,
        color=ORANGE,
        lw=2,
        ls="--",
        marker="o",
        ms=6,
        mec=SURFACE,
        mew=1.5,
        alpha=0.55,
    )
    a2.set_ylim(-0.1, 5)
    a2.set_yticks(range(0, 6))
    a2.set_title("Mask mismatch (pixels per 256×256 tile)", loc="left")
    a2.annotate(
        "median tile",
        (zooms[2], mask_med[2]),
        xytext=(0, 8),
        ha="center",
        textcoords="offset points",
        color=INK2,
        fontsize=9,
    )
    a2.annotate(
        "worst tile",
        (zooms[2], mask_max[2]),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        color=INK2,
        fontsize=9,
    )
    _save(fig, "agreement-per-zoom.png")


if __name__ == "__main__":
    pipelines()
    geometry()
    tiles()
    per_zoom()
