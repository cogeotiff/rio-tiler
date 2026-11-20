"""Export the SVG figures to transparent PNGs (light + dark palette), macOS only.

    python3 docs/scripts/cog_vs_geozarr/export_png.py

Reads the light SVGs written by make_figures.py and writes, into ./png,
<name>.png (light palette, for white slides/docs) and <name>_dark.png
(dark palette, for black slides), both at 2x and with a transparent background.

Uses Quick Look (qlmanage), which only renders onto an opaque background and
into a ~800px-wide viewport. So each figure is rendered at a reduced display
width, once on white and once on black, and alpha is recovered from the
difference between the two renders.
"""

import glob
import os
import re
import subprocess
import tempfile

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "src", "blog", "posts", "img", "cog_vs_geozarr")
PNG = os.path.join(HERE, "png")
SCALE = 2
VIEW_W = 600  # display width handed to Quick Look; must fit its viewport

# Slide palette: a brighter take on the SVG's dark theme, for black backgrounds.
DARK_VARS = """:root { --bg:#12171e; --panel:#1d232c; --fg:#f5f8fa; --muted:#bcc4cd; --line:#5f6873;
          --cog:#6ea8ff; --cog-soft:#26427d; --zarr:#ff8550; --zarr-soft:#6e3421;
          --cog-o:#3d61a3; --zarr-o:#934f30; }"""


def render(
    svg: str, w: float, h: float, extra_css: str, tmp: str, name: str
) -> np.ndarray:
    svg = re.sub(
        rf' width="{w:g}" height="{h:g}"',
        f' width="{VIEW_W}" height="{h * VIEW_W / w:.3f}"',
        svg,
        count=1,
    )
    svg = svg.replace("</svg>", f"<style>{extra_css}</style></svg>")
    path = os.path.join(tmp, name + ".svg")
    with open(path, "w") as f:
        f.write(svg)
    subprocess.run(
        ["qlmanage", "-t", "-s", str(int(w * SCALE)), "-o", tmp, path],
        check=True,
        capture_output=True,
    )
    im = Image.open(path + ".png").convert("RGB")
    im = im.crop((0, 0, int(w * SCALE), int(h * SCALE)))
    return np.asarray(im).astype(np.float64) / 255.0


def main():
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(PNG, exist_ok=True)
        for f in sorted(glob.glob(os.path.join(SRC, "*.svg"))):
            if f.endswith("_dark.svg"):
                continue
            base = os.path.splitext(os.path.basename(f))[0]
            svg = open(f).read()
            w, h = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
            for suffix, theme_css in (("", ""), ("_dark", DARK_VARS)):
                on_white = render(
                    svg, w, h, theme_css + " .bg{fill:#fff}", tmp, base + suffix + "_w"
                )
                on_black = render(
                    svg, w, h, theme_css + " .bg{fill:#000}", tmp, base + suffix + "_b"
                )
                # composite = alpha * color + (1 - alpha) * background
                alpha = 1.0 - (on_white - on_black).mean(axis=2)
                alpha = np.clip(alpha, 0.0, 1.0)
                safe = np.where(alpha > 1e-4, alpha, 1.0)[..., None]
                rgb = np.clip(on_black / safe, 0.0, 1.0)
                rgba = np.dstack([rgb, alpha])
                out = os.path.join(PNG, f"{base}{suffix}.png")
                Image.fromarray((rgba * 255).round().astype(np.uint8), "RGBA").save(
                    out, optimize=True
                )
                print("wrote", os.path.relpath(out))


if __name__ == "__main__":
    main()
