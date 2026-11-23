"""Generate the SVG figures used in docs/src/blog/posts/cog-vs-geozarr.md.

    python3 docs/scripts/cog_vs_geozarr/make_figures.py

Each figure is written twice to docs/src/blog/posts/img/cog_vs_geozarr/:
<name>.svg (light palette) and <name>_dark.svg (dark palette), both with a
transparent background. The post shows one or the other with mkdocs-material's
`#only-light` / `#only-dark` image suffixes, following the site's palette toggle.
"""

import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "src", "blog", "posts", "img", "cog_vs_geozarr")

LIGHT_VARS = """:root { --bg:#ffffff; --panel:#f6f7f9; --fg:#1f2328; --muted:#59636e; --line:#d0d7de;
          --cog:#2563eb; --cog-soft:#dbe6fd; --zarr:#c2410c; --zarr-soft:#fde4d6;
          --cog-o:#a8c1f7; --zarr-o:#e7b3a0; }"""
DARK_VARS = """:root { --bg:#0d1117; --panel:#161b22; --fg:#e6edf3; --muted:#9198a1; --line:#3d444d;
          --cog:#4a8cf0; --cog-soft:#1c2c4d; --zarr:#e06a30; --zarr-soft:#4a2516;
          --cog-o:#27406a; --zarr-o:#633420; }"""

STYLE = """<style>
  __VARS__
  text { white-space:pre; }
  .bg { fill:none; } .panel { fill:var(--panel); stroke:var(--line); }
  .t { fill:var(--fg); font-size:13px; } .s { fill:var(--muted); font-size:11.5px; }
  .xs { fill:var(--muted); font-size:10.5px; }
  .h1 { fill:var(--fg); font-size:20px; font-weight:600; }
  .h2c { fill:var(--cog); font-size:16px; font-weight:600; }
  .h2z { fill:var(--zarr); font-size:16px; font-weight:600; }
  .b { fill:var(--fg); font-size:13px; font-weight:600; }
  .bc { fill:var(--cog); font-size:13px; font-weight:600; }
  .bz { fill:var(--zarr); font-size:13px; font-weight:600; }
  .mono { fill:var(--fg); font-size:11.5px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; }
  .monos { fill:var(--muted); font-size:10.5px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; }
  .onc { fill:#ffffff; font-size:12px; font-weight:600; }
  .ln { stroke:var(--line); stroke-width:1; fill:none; }
  .axis { stroke:var(--line); stroke-width:1; fill:none; }
  .dash { stroke:var(--muted); stroke-width:1; stroke-dasharray:3 3; fill:none; }
  .life { stroke:var(--line); stroke-width:2; fill:none; }
  .cogS { fill:var(--cog); } .cogF { fill:var(--cog-soft); stroke:var(--cog); stroke-width:1; }
  .cogG { stroke:var(--cog); stroke-width:0.6; opacity:.7; }
  .cogO { fill:var(--cog-o); }
  .zarS { fill:var(--zarr); } .zarF { fill:var(--zarr-soft); stroke:var(--zarr); stroke-width:1; }
  .zarG { stroke:var(--zarr); stroke-width:0.5; opacity:.6; }
  .zarO { fill:var(--zarr-o); }
  .fpc { fill:none; stroke:var(--fg); stroke-width:1.6; }
  .box { fill:var(--bg); stroke:var(--line); }
  .gray { fill:var(--muted); } .grayO { fill:var(--muted); opacity:.4; }
  .hc { paint-order:stroke; stroke:var(--cog-soft); stroke-width:5px; stroke-linejoin:round; }
  .hp { paint-order:stroke; stroke:var(--panel); stroke-width:5px; stroke-linejoin:round; }
  .arr { stroke:var(--muted); stroke-width:1.5; fill:none; marker-end:url(#am); }
  .arr-c { stroke:var(--cog); stroke-width:1.5; fill:none; marker-end:url(#ac); }
  .arr-z { stroke:var(--zarr); stroke-width:1.5; fill:none; marker-end:url(#az); }
  .arr-cd { stroke:var(--cog); stroke-width:1.5; fill:none; stroke-dasharray:5 3; marker-end:url(#ac); }
  .arr-zd { stroke:var(--zarr); stroke-width:1.5; fill:none; stroke-dasharray:5 3; marker-end:url(#az); }
</style>
<defs>
  <marker id="am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="var(--muted)"/></marker>
  <marker id="ac" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="var(--cog)"/></marker>
  <marker id="az" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="var(--zarr)"/></marker>
</defs>"""


class Fig:
    def __init__(self, w, h, label):
        self.w, self.h, self.out = w, h, []
        self.a(
            f'<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            "font-family=\"-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif\" "
            f'role="img" aria-label="{label}">'
        )
        self.a(STYLE)
        self.rect(0, 0, w, h, "bg", rx=0)

    def a(self, s):
        self.out.append(s)

    def text(self, x, y, s, cls="t", anchor="start"):
        s = html.escape(s, quote=False)
        self.a(
            f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'
        )

    def rect(self, x, y, w, h, cls, rx=4, title=None):
        t = f"<title>{title}</title>" if title else ""
        self.a(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" class="{cls}">{t}</rect>'
        )

    def line(self, x1, y1, x2, y2, cls="ln"):
        self.a(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}"/>'
        )

    def path(self, d, cls):
        self.a(f'<path d="{d}" class="{cls}"/>')

    def bar(self, x, y, w, h, cls, title=None, r=4):
        """Horizontal bar, square at the baseline (left), rounded data-end (right)."""
        r = min(r, w / 2, h / 2)
        t = f"<title>{title}</title>" if title else ""
        d = (
            f"M{x:.1f},{y:.1f} H{x + w - r:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} "
            f"V{y + h - r:.1f} Q{x + w:.1f},{y + h:.1f} {x + w - r:.1f},{y + h:.1f} H{x:.1f} Z"
        )
        self.a(f'<path d="{d}" class="{cls}">{t}</path>')

    def grid(self, x, y, size_px, image_px, block_px, cls_fill, cls_grid):
        """Square of `size_px` representing `image_px`, ruled every `block_px` (to scale)."""
        self.rect(x, y, size_px, size_px, cls_fill, rx=0)
        step = block_px * size_px / image_px
        n = int(image_px // block_px)
        if step >= 2:
            for i in range(1, n + 1):
                p = i * step
                if p < size_px - 0.5:
                    self.line(x + p, y, x + p, y + size_px, cls_grid)
                    self.line(x, y + p, x + size_px, y + p, cls_grid)

    def save(self, name):
        self.a("</svg>")
        svg = "\n".join(self.out)
        os.makedirs(OUT, exist_ok=True)
        base = os.path.splitext(name)[0]
        for suffix, vars_ in (("", LIGHT_VARS), ("_dark", DARK_VARS)):
            with open(os.path.join(OUT, f"{base}{suffix}.svg"), "w") as f:
                f.write(svg.replace("__VARS__", vars_))


# ───────────────────────────── structure ─────────────────────────────
def structure():
    f = Fig(1200, 830, "COG vs GeoZarr structure")
    T = f.text
    T(
        600,
        42,
        "Same Sentinel-2 band (B04, 10980×10980) — stored as a COG vs a GeoZarr",
        "h1",
        "middle",
    )
    f.rect(30, 70, 555, 740, "panel", rx=8)
    f.rect(615, 70, 555, 740, "panel", rx=8)

    # COG
    T(55, 104, "COG — one file per band", "h2c")
    T(55, 124, "S2C_33TVF_20260928_0_L2A_B04.tif · 212 MB · uint16 · DEFLATE", "s")
    bx0, bx1, by, bh, hx1, ox1 = 60, 555, 175, 46, 135, 235
    f.rect(bx0, by, hx1 - bx0, bh, "cogS", rx=0)
    f.rect(hx1, by, ox1 - hx1, bh, "cogF", rx=0)
    f.rect(ox1, by, bx1 - ox1, bh, "cogF", rx=0)
    for i in range(1, 11):
        x = ox1 + i * (bx1 - ox1) / 11
        f.line(x, by, x, by + bh, "cogG")
    for i in range(1, 4):
        x = hx1 + i * (ox1 - hx1) / 4
        f.line(x, by, x, by + bh, "cogG")
    T((bx0 + hx1) / 2, by + 28, "HEADER", "onc", "middle")
    T((hx1 + ox1) / 2, by + 20, "overviews", "t hc", "middle")
    T((hx1 + ox1) / 2, by + 35, "×16 … ×2", "xs hc", "middle")
    T((ox1 + bx1) / 2, by + 20, "full-resolution blocks", "t hc", "middle")
    T((ox1 + bx1) / 2, by + 35, "121 × (1024×1024)", "xs hc", "middle")
    for x, s in [(bx0, "0"), (hx1, "32 KB"), (ox1, "~54 MB"), (bx1, "212 MB")]:
        T(x, by + bh + 15, s, "monos", "middle")
    T(bx0, by + bh + 30, "byte layout of the file (not to scale)", "xs")
    hc = (bx0 + hx1) / 2
    f.path(f"M{hc},{by - 2} C{hc},{by - 30} 420,{by - 30} 420,{by - 3}", "arr-c")
    f.path(f"M{hc},{by - 2} C{hc},{by - 22} 185,{by - 22} 185,{by - 3}", "arr-c")
    T(300, by - 26, "header holds the byte offset of every block", "s", "middle")

    zy = 280
    f.rect(60, zy, 495, 182, "box", rx=6)
    T(75, zy + 22, "HEADER", "b")
    T(140, zy + 22, "first 32 KB — 1 GET gives the whole layout", "s")
    ifds = [
        ("IFD 0", "full res", "10980²", "11×11", "121"),
        ("IFD 1", "×2", "5490²", "6×6", "36"),
        ("IFD 2", "×4", "2745²", "3×3", "9"),
        ("IFD 3", "×8", "1373²", "2×2", "4"),
        ("IFD 4", "×16", "687²", "1×1", "1"),
    ]
    cols = [75, 135, 215, 300, 390]
    for c, s in zip(
        cols, ["", "level", "size", "blocks", "TileOffsets[] / TileByteCounts[]"]
    ):
        T(c, zy + 46, s, "xs")
    for i, row in enumerate(ifds):
        yy = zy + 68 + i * 22
        if i % 2 == 0:
            f.rect(68, yy - 15, 479, 21, "cogF", rx=2)
        T(cols[0], yy, row[0], "mono")
        T(cols[1], yy, row[1], "t")
        T(cols[2], yy, row[2], "mono")
        T(cols[3], yy, row[3], "mono")
        T(cols[4], yy, f"{row[4]} × (offset, nbytes)", "mono")

    # GeoZarr
    T(640, 104, "GeoZarr — one store, all bands × all resolutions", "h2z")
    T(
        640,
        124,
        ".zarr/measurements/reflectance · uint16 (scale/offset codec) · Blosc zstd · sharded",
        "s",
    )
    rx0, ry0, rw, rh = 740, 145, 305, 48
    f.rect(rx0, ry0, rw, rh, "zarF", rx=6)
    T(rx0 + 14, ry0 + 20, "reflectance/", "b")
    T(rx0 + 14, ry0 + 38, "zarr.json — consolidated: 81 arrays · 215 KB", "s")
    groups = [
        ("r10m", "10980²"),
        ("r20m", "5490²"),
        ("r60m", "1830²"),
        ("r120m", "915²"),
        ("r360m", "305²"),
        ("r720m", "152²"),
    ]
    gy, gw, gh, gap, gx0, bus = 228, 78, 40, 10, 633, 212
    f.line(rx0 + rw / 2, ry0 + rh, rx0 + rw / 2, bus)
    f.line(gx0 + gw / 2, bus, gx0 + 5 * (gw + gap) + gw / 2, bus)
    for i, (g, sz) in enumerate(groups):
        x = gx0 + i * (gw + gap)
        f.line(x + gw / 2, bus, x + gw / 2, gy)
        f.rect(x, gy, gw, gh, "box", rx=4)
        T(x + gw / 2, gy + 17, g + "/", "b", "middle")
        T(x + gw / 2, gy + 32, sz, "monos", "middle")
    ay, aw, ah, abus = 300, 46, 24, 286
    f.line(gx0 + gw / 2, gy + gh, gx0 + gw / 2, abus)
    f.line(gx0 + aw / 2, abus, gx0 + 3 * (aw + 6) + aw / 2, abus)
    for i, b in enumerate(["b02", "b03", "b04", "b08"]):
        x = gx0 + i * (aw + 6)
        f.line(x + aw / 2, abus, x + aw / 2, ay)
        f.rect(x, ay, aw, ah, "zarS" if b == "b04" else "box", rx=4)
        T(x + aw / 2, ay + 16, b, "onc" if b == "b04" else "mono", "middle")
    T(845, ay + 10, "one array per band in every group", "s")
    T(845, ay + 25, "(r20m / r60m … hold more bands)", "xs")

    b04x = gx0 + 2 * (aw + 6) + aw / 2
    sx0, sx1, sy, sh, ix0 = 650, 1150, 372, 46, 1062
    f.line(b04x, ay + ah, b04x, sy, "dash")
    T(b04x + 6, sy - 8, "c/0/0", "monos")
    f.rect(sx0, sy, ix0 - sx0, sh, "zarF", rx=0)
    f.rect(ix0, sy, sx1 - ix0, sh, "zarS", rx=0)
    x = sx0
    while x < ix0 - 6:
        x += 6
        f.line(x, sy, x, sy + sh, "zarG")
    T((ix0 + sx1) / 2, sy + 28, "INDEX", "onc", "middle")
    f.path(
        f"M{(ix0 + sx1) / 2},{sy - 2} C{(ix0 + sx1) / 2},{sy - 28} 930,{sy - 28} 930,{sy - 3}",
        "arr-z",
    )
    T(985, sy - 24, "offsets", "s", "middle")
    T(sx0, sy + sh + 15, "0", "monos", "middle")
    T(sx1, sy + sh + 15, "150 MB", "monos", "middle")
    T(sx0, sy + sh + 30, "r10m/b04/c/0/0 — ONE shard = the whole array", "t")
    T(sx0, sy + sh + 46, "2025 inner chunks (45×45 of 244×244), Morton order", "s")
    T(sx1, sy + sh + 30, "index at the end", "t", "end")
    T(sx1, sy + sh + 46, "2025 × (offset, nbytes) · 32 KB", "s", "end")

    base = 700
    for x0 in (55, 640):
        T(
            x0,
            512,
            "Pyramid, to scale — grid lines = smallest unit a reader can fetch",
            "s",
        )
    S = 170 / 10980
    for x, img, lab, sub in [
        (70, 10980, "full res", "1024² blocks"),
        (270, 5490, "×2", ""),
        (380, 2745, "×4", ""),
        (450, 1373, "×8", ""),
        (500, 687, "×16", ""),
    ]:
        size = img * S
        f.grid(x, base - size, size, img, 1024, "cogF", "cogG")
        T(x + size / 2, base + 18, lab, "t", "middle")
        if sub:
            T(x + size / 2, base + 34, sub, "xs", "middle")
    T(310, base + 34, "overviews: same file, same 1024² blocks", "xs")
    for x, img, chunk, lab, sub in [
        (655, 10980, 244, "r10m", "244² chunks"),
        (855, 5490, 183, "r20m", "183² chunks"),
        (965, 1830, 183, "r60m", ""),
        (1025, 915, 183, "r120m", ""),
        (1072, 305, 256, "r360m", ""),
        (1132, 152, 152, "r720m", ""),
    ]:
        size = max(img * S, 2)
        f.grid(x, base - size, size, img, chunk, "zarF", "zarG")
        T(x + size / 2, base + 18, lab, "t", "middle")
        if sub:
            T(x + size / 2, base + 34, sub, "xs", "middle")
    T(965, base + 34, "sibling groups, 1 shard each", "xs")

    T(55, 770, "Tile read = 2 dependent round trips", "b")
    T(55, 790, "① header (32 KB)  →  ② block ranges", "s")
    T(640, 770, "Tile read = 3 dependent round trips", "b")
    T(640, 790, "① zarr.json (215 KB)  →  ② shard index (32 KB)  →  ③ chunk ranges", "s")
    f.save("structure.svg")


# ───────────────────────────── tile request flow ─────────────────────────────
def tile_request_flow():
    f = Fig(1000, 280, "A tile request in two steps")
    T = f.text
    # request
    f.rect(20, 55, 180, 70, "box", rx=6)
    T(110, 85, "GET /tiles/14/6944/6268", "mono", "middle")
    T(110, 104, "one 256×256 web-map tile", "xs", "middle")
    f.path("M200,90 L246,90", "arr")
    # reader
    f.rect(250, 30, 290, 120, "panel", rx=6)
    T(268, 56, "Dataset Reader", "b")
    for i, s in enumerate(
        [
            "tile → bbox in the dataset CRS",
            "pick the level (overview / multiscale)",
            "find the overlapping blocks / chunks",
        ]
    ):
        T(268, 82 + i * 20, "· " + s, "s")
    # S3
    f.rect(800, 30, 180, 120, "panel", rx=6)
    T(890, 82, "Storage", "b", "middle")
    T(890, 101, "HTTP range requests", "s", "middle")
    # two calls
    for y, lab, sub in [
        (60, "① metadata", "“what is in there, and where are the bytes?”"),
        (126, "② data", "“give me exactly those bytes”"),
    ]:
        f.path(f"M542,{y} L796,{y}", "arr")
        f.path(f"M796,{y + 8} L544,{y + 8}", "arr")
        T(670, y - 8, lab, "b", "middle")
        T(670, y + 24, sub, "xs", "middle")
    # output
    f.path("M395,150 L395,186", "arr")
    f.rect(250, 190, 290, 50, "box", rx=6)
    T(395, 212, "decode → reproject", "t", "middle")
    T(395, 229, "to WebMercator → 256×256 array", "s", "middle")
    # callout
    T(600, 205, "Every request/response pair = 1 round trip", "b")
    T(600, 224, "(~100 ms+ to remote storage). On object storage the cost is", "s")
    T(600, 241, "round trips, not bytes: each one that waits for the", "s")
    T(600, 258, "previous adds a full latency.", "s")
    f.save("tile_request_flow.svg")


# ───────────────────────────── COG header ─────────────────────────────
def cog_header():
    f = Fig(1000, 250, "COG: read the header")
    T = f.text
    bx0, bx1, by, bh, hx1, ox1 = 40, 960, 80, 50, 170, 330
    f.rect(bx0, by, hx1 - bx0, bh, "cogS", rx=0)
    f.rect(hx1, by, ox1 - hx1, bh, "cogF", rx=0)
    f.rect(ox1, by, bx1 - ox1, bh, "cogF", rx=0)
    for i in range(1, 11):
        x = ox1 + i * (bx1 - ox1) / 11
        f.line(x, by, x, by + bh, "cogG")
    for i in range(1, 4):
        x = hx1 + i * (ox1 - hx1) / 4
        f.line(x, by, x, by + bh, "cogG")
    T((bx0 + hx1) / 2, by + 24, "HEADER", "onc", "middle")
    T((bx0 + hx1) / 2, by + 39, "IFDs + offsets", "onc", "middle")
    T((hx1 + ox1) / 2, by + 22, "overviews", "t hc", "middle")
    T((hx1 + ox1) / 2, by + 38, "×16 … ×2, small", "xs hc", "middle")
    T((ox1 + bx1) / 2, by + 22, "full-resolution blocks (11 × 11)", "t hc", "middle")
    T((ox1 + bx1) / 2, by + 38, "1024×1024 uint16, DEFLATE", "xs hc", "middle")
    for x, s in [(bx0, "0"), (hx1, "32 KB"), (ox1, "~54 MB"), (bx1, "212 MB")]:
        T(x, by + bh + 16, s, "monos", "middle")
    # GET
    T(40, 28, "① GET bytes=0-32767", "bc")
    T(40, 46, "1 request", "s")
    f.path(f"M60,52 L60,{by - 3}", "arr-c")
    # offsets arcs
    f.path(f"M140,{by - 2} C140,{by - 34} 640,{by - 34} 640,{by - 3}", "arr-c")
    f.path(f"M140,{by - 2} C140,{by - 22} 250,{by - 22} 250,{by - 3}", "arr-c")
    T(
        420,
        40,
        "the header holds the byte offset of every block, of every level",
        "s",
        "middle",
    )
    T(40, 182, "TileOffsets[]    = [ 3562, 378214, … , 142834054, … ]", "mono")
    T(40, 202, "TileByteCounts[] = [ 374652, … , 1567374, … ]", "mono")
    T(
        40,
        234,
        "After this single request the reader knows the exact byte range of any block — no more metadata requests.",
        "s",
    )
    T(960, 234, "byte layout, not to scale", "xs", "end")
    f.save("cog_header.svg")


# ───────────────────────────── COG blocks ─────────────────────────────
def cog_blocks():
    f = Fig(1000, 410, "COG: fetch the blocks")
    T = f.text
    gx, gy, c = 50, 50, 30
    size = 10980 / 1024 * c
    f.grid(gx, gy, size, 10980, 1024, "cogF", "cogG")
    for i in range(11):
        T(gx + i * c + c / 2, gy - 8, str(i), "xs", "middle")
        T(gx - 10, gy + i * c + c / 2 + 4, str(i), "xs", "middle")
    # fetched blocks
    for col, row in [(4, 4), (5, 4), (4, 5), (5, 5)]:
        f.rect(
            gx + col * c,
            gy + row * c,
            c,
            c,
            "cogO",
            rx=0,
            title=f"block ({row},{col}) fetched",
        )
    # z12 footprint ~743 px (cols 5080-5822, rows 4861-5601) → 2 × 2 blocks
    fp = 743 / 1024 * c
    f.rect(gx + 5080 / 1024 * c, gy + 4861 / 1024 * c, fp, fp, "fpc", rx=0)
    # z14 footprint ~186 px (cols 5264-5450, rows 5414-5599) inside block (5,5)
    fz = 186 / 1024 * c
    f.rect(gx + 5264 / 1024 * c, gy + 5414 / 1024 * c, fz, fz, "fpc", rx=0)
    T(
        gx + size / 2,
        gy + size + 22,
        "full resolution: 11 × 11 blocks of 1024×1024 (to scale)",
        "xs",
        "middle",
    )

    # z12 callout
    y12 = gy + 3 * c
    f.line(gx + 5822 / 1024 * c + 2, gy + 4861 / 1024 * c, 440, y12, "dash")
    T(450, y12 - 34, "z12 tile — footprint ~743 px", "b")
    T(
        450,
        y12 - 16,
        "→ 2 × 2 blocks: 4 ranges, all fetched in parallel (1 round trip)",
        "s",
    )
    T(450, y12 + 8, "GET bytes=31709542-32104336   394,795 B   block (4,4)", "mono")
    T(450, y12 + 26, "GET bytes=32104337-32505212   400,876 B   block (4,5)", "mono")
    T(450, y12 + 44, "…  2 more ranges for row 5", "monos")
    # z14 callout
    y14 = gy + 8 * c
    f.line(gx + 5450 / 1024 * c + 2, gy + 5507 / 1024 * c, 440, y14, "dash")
    T(450, y14 - 8, "z14 tile — footprint ~186 px", "b")
    T(450, y14 + 10, "→ 1 whole 1024² block = 1.57 MB", "s")
    T(450, y14 + 28, "the tile uses ~3% of the bytes it downloads", "s")
    # legend
    f.rect(450, 345, 16, 12, "cogO", rx=0)
    T(472, 355, "block fetched", "s")
    f.rect(570, 345, 16, 12, "fpc", rx=0)
    T(592, 355, "tile footprint", "s")
    T(
        450,
        385,
        "Trade-off: big blocks → few requests, but most of each block is unused at high zoom.",
        "s",
    )
    f.save("cog_blocks.svg")


# ───────────────────────────── Zarr tree ─────────────────────────────
def zarr_tree():
    f = Fig(1000, 330, "GeoZarr: read zarr.json")
    T = f.text
    rx0, ry0, rw, rh = 360, 30, 330, 50
    f.rect(rx0, ry0, rw, rh, "zarF", rx=6)
    T(rx0 + 14, ry0 + 21, "reflectance/", "b")
    T(rx0 + 14, ry0 + 39, "zarr.json — consolidated · 215 KB · 81 arrays", "s")
    T(40, 50, "① GET zarr.json", "bz")
    T(40, 68, "1 request, 215 KB", "s")
    f.path(f"M175,55 L{rx0 - 4},55", "arr-z")

    groups = [
        ("r10m", "10980²"),
        ("r20m", "5490²"),
        ("r60m", "1830²"),
        ("r120m", "915²"),
        ("r360m", "305²"),
        ("r720m", "152²"),
    ]
    gy, gw, gh, gap, gx0, bus = 120, 120, 42, 20, 90, 102
    f.line(rx0 + rw / 2, ry0 + rh, rx0 + rw / 2, bus)
    f.line(gx0 + gw / 2, bus, gx0 + 5 * (gw + gap) + gw / 2, bus)
    for i, (g, sz) in enumerate(groups):
        x = gx0 + i * (gw + gap)
        f.line(x + gw / 2, bus, x + gw / 2, gy)
        f.rect(x, gy, gw, gh, "box", rx=4)
        T(x + gw / 2, gy + 18, g + "/", "b", "middle")
        T(x + gw / 2, gy + 34, sz, "monos", "middle")
    T(40, gy + 26, "levels", "xs", "middle")
    ay, aw, ah, abus = 200, 54, 26, 184
    f.line(gx0 + gw / 2, gy + gh, gx0 + gw / 2, abus)
    f.line(gx0 + aw / 2, abus, gx0 + 3 * (aw + 8) + aw / 2, abus)
    for i, b in enumerate(["b02", "b03", "b04", "b08"]):
        x = gx0 + i * (aw + 8)
        f.line(x + aw / 2, abus, x + aw / 2, ay)
        f.rect(x, ay, aw, ah, "zarS" if b == "b04" else "box", rx=4)
        T(x + aw / 2, ay + 17, b, "onc" if b == "b04" else "mono", "middle")
    T(40, ay + 17, "bands", "xs", "middle")
    b04x = gx0 + 2 * (aw + 8) + aw / 2
    f.line(b04x, ay + ah, b04x, 262, "dash")
    f.rect(gx0, 266, 330, 42, "zarF", rx=4)
    T(gx0 + 12, 284, "c/0/0 — ONE shard = the whole array", "t")
    T(gx0 + 12, 300, "10980×10980 · 150 MB", "s")
    T(40, 290, "shard", "xs", "middle")

    nx = 520
    f.rect(nx, 200, 440, 108, "panel", rx=6)
    T(nx + 16, 224, "What zarr.json tells us", "b")
    T(nx + 16, 242, "shapes, transforms, chunk grid, codecs — for all 81 arrays", "s")
    T(nx + 16, 270, "What it does not tell us", "b")
    T(nx + 16, 288, "where each inner chunk sits inside the shard", "s")
    f.save("zarr_tree.svg")


# ───────────────────────────── Zarr shard ─────────────────────────────
def zarr_shard():
    f = Fig(1000, 430, "GeoZarr: shard index, then chunks")
    T = f.text
    sx0, sx1, sy, sh, ix0 = 40, 960, 90, 50, 800
    f.rect(sx0, sy, ix0 - sx0, sh, "zarF", rx=0)
    f.rect(ix0, sy, sx1 - ix0, sh, "zarS", rx=0)
    x = sx0
    while x < ix0 - 8:
        x += 8
        f.line(x, sy, x, sy + sh, "zarG")
    f.rect(352, sy, 16, sh, "zarO", rx=0, title="coalesced chunk range")
    T(580, sy + 31, "chunk(0,0) … chunk(i,j) … chunk(44,44)", "t hp", "middle")
    T((ix0 + sx1) / 2, sy + 31, "INDEX", "onc", "middle")
    # ②a
    T(880, 34, "②a GET bytes=-32404", "bz", "middle")
    T(880, 52, "2025 × 16 B + crc32c", "s", "middle")
    f.path(f"M880,58 L880,{sy - 3}", "arr-z")
    # ②b
    T(360, 34, "②b GET bytes=63161124-63740650", "bz", "middle")
    T(360, 52, "needs ②a to know the offsets", "s", "middle")
    f.path(f"M360,58 L360,{sy - 3}", "arr-z")
    # offsets arc under
    f.path(
        f"M880,{sy + sh + 2} C880,{sy + sh + 34} 360,{sy + sh + 34} 360,{sy + sh + 3}",
        "arr-zd",
    )
    T(620, sy + sh + 42, "offsets", "s", "middle")
    T(sx0, sy + sh + 16, "0", "monos", "middle")
    T(sx1, sy + sh + 16, "150 MB", "monos", "middle")
    T(
        40,
        212,
        "r10m/b04/c/0/0 · 45 × 45 = 2025 inner chunks of 244×244 uint16 · index at the end",
        "s",
    )
    f.line(40, 232, 960, 232)

    # coalescing
    T(40, 258, "②b is coalesced", "b")
    T(
        150,
        258,
        "the reader merges chunk ranges into one GET when the gap between them is small (< 1 MiB)",
        "s",
    )
    # chunk grid around the tile: rows 20-23, cols 21-23 (Morton order inside the shard)
    need = {(22, 21), (22, 22)}
    extra = {(23, 21), (20, 22), (21, 22), (20, 23), (21, 23)}
    cx, cy, cs = 80, 292, 26
    for r in range(20, 24):
        for cc in range(21, 24):
            cls = "zarS" if (r, cc) in need else "zarO" if (r, cc) in extra else "zarF"
            f.rect(cx + (cc - 21) * cs, cy + (r - 20) * cs, cs - 2, cs - 2, cls, rx=2)
        T(cx - 8, cy + (r - 20) * cs + cs / 2 + 3, str(r), "xs", "end")
    for cc in range(21, 24):
        T(cx + (cc - 21) * cs + cs / 2 - 1, cy - 6, str(cc), "xs", "middle")
    T(cx + 1.5 * cs, cy + 4 * cs + 16, "tile needs (22,21), (22,22)", "xs", "middle")

    rx, ry, rh, cw = 270, 312, 40, 88
    cells = [
        ("22,21", 1),
        ("23,21", 0),
        ("20,22", 0),
        ("21,22", 0),
        ("20,23", 0),
        ("21,23", 0),
        ("22,22", 1),
    ]
    f.rect(rx - 30, ry, 30, rh, "zarF", rx=0)
    T(rx - 15, ry + 25, "…", "t", "middle")
    x = span0 = rx
    for lab, needed in cells:
        f.rect(x, ry, cw - 2, rh, "zarS" if needed else "zarO", rx=0)
        T(x + cw / 2 - 1, ry + 25, lab, "onc" if needed else "mono", "middle")
        x += cw
    span1 = x - 2
    f.rect(x, ry, 40, rh, "zarF", rx=0)
    T(x + 20, ry + 25, "…", "t", "middle")
    f.path(
        f"M{span0},{ry - 6} L{span0},{ry - 14} L{span1},{ry - 14} L{span1},{ry - 6}", "ln"
    )
    T(
        (span0 + span1) / 2,
        ry - 20,
        "one coalesced GET · 580 KB (7 chunks) for the 2 chunks needed (163 KB)",
        "b",
        "middle",
    )
    T(
        rx - 30,
        ry + rh + 20,
        "chunks are stored in Morton (Z) order — everything in between is downloaded too",
        "s",
    )
    f.rect(rx - 30, ry + rh + 36, 14, 10, "zarS", rx=0)
    T(rx - 10, ry + rh + 45, "needed", "xs")
    f.rect(rx + 50, ry + rh + 36, 14, 10, "zarO", rx=0)
    T(rx + 70, ry + rh + 45, "downloaded, not needed", "xs")
    f.save("zarr_shard.svg")


# ───────────────────────────── round trips ─────────────────────────────
def round_trips():
    f = Fig(1000, 430, "Round trips: COG vs GeoZarr")
    T = f.text
    sides = [
        (
            0,
            "c",
            "COG — 2 round trips",
            [
                ("GET bytes=0-32767", "32 KB"),
                ("GET block ranges (parallel)", "0.4 – 1.6 MB"),
            ],
        ),
        (
            500,
            "z",
            "GeoZarr (sharded) — 3 round trips",
            [
                ("GET zarr.json", "215 KB"),
                ("GET bytes=-32404 (shard index)", "32 KB"),
                ("GET chunk range (coalesced)", "0.3 – 0.7 MB"),
            ],
        ),
    ]
    for ox, k, title, trips in sides:
        cl, s3 = ox + 70, ox + 400
        T(ox + 30, 30, title, "h2c" if k == "c" else "h2z")
        T(cl, 60, "reader", "b", "middle")
        T(s3, 60, "storage", "b", "middle")
        end = 85 + len(trips) * 100
        f.line(cl, 70, cl, end, "life")
        f.line(s3, 70, s3, 395, "life")
        for i, (req, resp) in enumerate(trips):
            y = 90 + i * 100
            f.path(f"M{cl},{y} L{s3 - 2},{y + 16}", f"arr-{k}")
            T((cl + s3) / 2, y - 2, req, "mono", "middle")
            f.path(f"M{s3},{y + 38} L{cl + 2},{y + 54}", f"arr-{k}d")
            T((cl + s3) / 2, y + 66, resp, "s", "middle")
            T(s3 + 12, y + 32, f"RTT {i + 1}", "b")
        T(cl, end + 18, "decode, reproject", "s", "middle")
        f.rect(cl - 5, end - 5, 10, 10, f"{'cogS' if k == 'c' else 'zarS'}", rx=2)
    f.line(500, 20, 500, 410)
    f.save("round_trips.svg")


# ───────────────────────────── bar charts ─────────────────────────────
TILES = [
    ("z14", "14/8849/6139", "full res / r10m"),
    ("z12", "12/2212/1534", "full res / r20m"),
    ("z10", "10/553/383", "overview / r120m"),
    ("z9", "9/276/191", "overview / r120m"),
]


def _legend(f, y, extra=None):
    f.rect(230, y - 10, 12, 12, "cogS", rx=2)
    f.text(248, y, "COG", "s")
    f.rect(300, y - 10, 12, 12, "zarS", rx=2)
    f.text(318, y, "GeoZarr", "s")
    if extra:
        extra(f, y)


def _axis(f, x0, x1, top, bottom, vmax, step, unit):
    v = 0
    while v <= vmax:
        x = x0 + (x1 - x0) * v / vmax
        f.line(x, top, x, bottom, "axis")
        f.text(x, top - 6, f"{v:,}" + (f" {unit}" if v == vmax else ""), "xs", "middle")
        v += step


def bytes_chart():
    data = [
        (1600.142, 827.412, "1 + 1", "1 + 1 + 1"),
        (1643.723, 853.837, "1 + 4", "1 + 1 + 1"),
        (817.099, 500.999, "1 + 2", "1 + 1 + 1"),
        (407.420, 891.666, "1 + 1", "1 + 1 + 1"),
    ]
    f = Fig(1000, 330, "Bytes downloaded per tile")
    x0, x1, vmax = 230, 880, 2000
    _legend(f, 26)
    top = 64
    _axis(f, x0, x1, top, 310, vmax, 500, "KB")
    for i, ((z, tile, lvl), (c, zz, gc, gz)) in enumerate(zip(TILES, data)):
        y = 78 + i * 58
        f.text(30, y + 14, f"{z} · {tile}", "t")
        f.text(30, y + 31, lvl, "xs")
        for j, (v, cls, k, g) in enumerate(
            [(c, "cogS", "COG", gc), (zz, "zarS", "GeoZarr", gz)]
        ):
            yy = y + j * 18
            w = (x1 - x0) * v / vmax
            f.bar(x0, yy, w, 16, cls, title=f"{z} {k}: {v:,.0f} KB in {g} GETs")
            f.text(x0 + w + 6, yy + 12, f"{v:,.0f} KB", "s")
    f.save("bytes_per_tile.svg")


def time_chart():
    data = [
        ((544, 738, 1281), (769, 533, 1290)),
        ((572, 874, 1465), (796, 509, 1291)),
        ((565, 657, 1205), (786, 391, 1175)),
        ((580, 485, 1066), (791, 498, 1283)),
    ]
    f = Fig(1000, 350, "Time per tile")

    def extra(f, y):
        f.rect(420, y - 10, 12, 12, "grayO", rx=0)
        f.text(438, y, "open", "s")
        f.rect(486, y - 10, 12, 12, "gray", rx=0)
        f.text(504, y, "tile", "s")

    _legend(f, 26, extra)
    x0, x1, vmax = 230, 880, 1600
    top = 64
    _axis(f, x0, x1, top, 310, vmax, 200, "ms")
    for i, ((z, tile, lvl), rows) in enumerate(zip(TILES, data)):
        y = 78 + i * 58
        f.text(30, y + 14, f"{z} · {tile}", "t")
        f.text(30, y + 31, lvl, "xs")
        for j, ((op, tl, tot), k) in enumerate(zip(rows, ["c", "z"])):
            yy = y + j * 18
            wo = (x1 - x0) * op / vmax
            wt = (x1 - x0) * tl / vmax
            name = "COG" if k == "c" else "GeoZarr"
            f.rect(
                x0,
                yy,
                wo - 1,
                16,
                "cogO" if k == "c" else "zarO",
                rx=0,
                title=f"{z} {name} open: {op} ms",
            )
            f.bar(
                x0 + wo + 1,
                yy,
                wt - 1,
                16,
                "cogS" if k == "c" else "zarS",
                title=f"{z} {name} tile: {tl} ms",
            )
            f.text(x0 + wo + wt + 6, yy + 12, f"{tot:,} ms", "s")
    f.text(
        30,
        336,
        "Median of 10 cold runs (fresh process each), laptop → us-east-1. Labels are the median total; open and tile medians are computed separately.",
        "xs",
    )
    f.save("time_per_tile.svg")


# ───────────────────────────── multi-band round trips ─────────────────────────────
def multiband_round_trips():
    f = Fig(1000, 300, "Round trips for a 3-band tile")
    T = f.text
    x0, cw, n = 230, 240, 3
    for i in range(n):
        T(x0 + i * cw + cw / 2, 30, f"RTT {i + 1}", "b", "middle")
        f.line(x0 + i * cw, 40, x0 + i * cw, 280, "ln")
    f.line(x0 + n * cw, 40, x0 + n * cw, 280, "ln")
    rows = [
        (
            "COG",
            "STAC Item, 3 files",
            "c",
            [
                ["STAC Item"],
                ["header B04", "header B03", "header B02"],
                ["blocks B04", "blocks B03", "blocks B02"],
            ],
            "Item + 3 header + 3 block reads",
        ),
        (
            "GeoZarr",
            "1 store, 3 arrays",
            "z",
            [
                ["zarr.json"],
                ["shard index b04", "shard index b03", "shard index b02"],
                ["chunks b04", "chunks b03", "chunks b02"],
            ],
            "7 GETs",
        ),
    ]
    for r, (name, sub, k, steps, foot) in enumerate(rows):
        y0 = 48 + r * 116
        T(20, y0 + 22, name, "h2c" if k == "c" else "h2z")
        T(20, y0 + 42, sub, "s")
        T(20, y0 + 60, foot, "xs")
        for i, reqs in enumerate(steps):
            for j, lab in enumerate(reqs):
                meta = lab.startswith(("header", "shard", "zarr", "STAC"))
                cls = (
                    ("cogF" if k == "c" else "zarF")
                    if meta
                    else ("cogS" if k == "c" else "zarS")
                )
                bx, by = x0 + i * cw + 10, y0 + 8 + j * 30
                f.rect(bx, by, cw - 20, 24, cls, rx=3)
                T(bx + (cw - 20) / 2, by + 16, lab, "s" if meta else "onc", "middle")
        if r == 0:
            f.line(10, y0 + 108, 990, y0 + 108, "ln")
    f.rect(230, 286, 14, 10, "grayO", rx=2)
    T(250, 295, "metadata", "xs")
    f.rect(320, 286, 14, 10, "gray", rx=2)
    T(340, 295, "pixel data", "xs")
    T(990, 295, "stacked boxes = requests in flight at the same time", "xs", "end")
    f.save("multiband_round_trips.svg")


# ───────────────────────────── multi-band charts ─────────────────────────────
MB_TILES = TILES[:3]


def multiband_bytes_chart():
    data = [
        (4716.679, 1991.013, "7 ranges", "7 GET"),
        (4838.992, 2062.192, "16 ranges", "7 GET"),
        (2393.540, 1032.839, "10 ranges", "7 GET"),
    ]
    f = Fig(1000, 280, "Bytes downloaded per 3-band tile")
    x0, x1, vmax = 300, 860, 5000
    for x, cls, lab in [
        (300, "cogS", "COG — 3 files"),
        (420, "zarS", "GeoZarr — 1 store"),
    ]:
        f.rect(x, 16, 12, 12, cls, rx=2)
        f.text(x + 18, 26, lab, "s")
    _axis(f, x0, x1, 64, 250, vmax, 1000, "KB")
    for i, ((z, tile, lvl), (c, zz, rc, rz)) in enumerate(zip(MB_TILES, data)):
        y = 78 + i * 58
        f.text(30, y + 14, f"{z} · {tile}", "t")
        f.text(30, y + 31, lvl, "xs")
        for j, (v, cls, name, req) in enumerate(
            [(c, "cogS", "COG", rc), (zz, "zarS", "GeoZarr", rz)]
        ):
            yy = y + j * 18
            w = (x1 - x0) * v / vmax
            f.text(x0 - 8, yy + 12, req, "xs", "end")
            f.bar(x0, yy, w, 16, cls, title=f"{z} {name}: {v:,.0f} KB, {req}")
            f.text(x0 + w + 6, yy + 12, f"{v:,.0f} KB", "s")
    f.text(
        30,
        270,
        "B04 + B03 + B02, cold, every range recorded. COG: 7 calls (STAC Item + 3 headers + 3 block reads). GeoZarr: 7 GETs.",
        "xs",
    )
    f.save("multiband_bytes.svg")


def multiband_time_chart():
    data = [
        [(503, 1339, 1854), (780, 973, 1764)],
        [(502, 1457, 1949), (786, 986, 1767)],
        [(490, 1182, 1684), (795, 767, 1566)],
    ]
    series = [("COG", "c"), ("GeoZarr", "z")]
    f = Fig(1000, 280, "Time per 3-band tile")
    for x, cls, lab in [
        (300, "cogS", "COG"),
        (360, "zarS", "GeoZarr"),
        (450, "grayO", "open"),
        (510, "gray", "tile"),
    ]:
        f.rect(x, 16, 12, 12, cls, rx=2 if cls in ("cogS", "zarS") else 0)
        f.text(x + 18, 26, lab, "s")
    x0, x1, vmax = 300, 880, 2000
    _axis(f, x0, x1, 64, 250, vmax, 400, "ms")
    for i, ((z, tile, lvl), rows) in enumerate(zip(MB_TILES, data)):
        y = 78 + i * 58
        f.text(30, y + 14, f"{z} · {tile}", "t")
        f.text(30, y + 31, lvl, "xs")
        for j, ((op, tl, tot), (name, k)) in enumerate(zip(rows, series)):
            yy = y + j * 18
            wo = (x1 - x0) * op / vmax
            wt = (x1 - x0) * tl / vmax
            f.text(x0 - 8, yy + 12, name, "xs", "end")
            f.rect(
                x0,
                yy,
                wo - 1,
                16,
                "cogO" if k == "c" else "zarO",
                rx=0,
                title=f"{z} {name} open: {op} ms",
            )
            f.bar(
                x0 + wo + 1,
                yy,
                wt - 1,
                16,
                "cogS" if k == "c" else "zarS",
                title=f"{z} {name} tile: {tl} ms",
            )
            f.text(x0 + wo + wt + 6, yy + 12, f"{tot:,} ms", "s")
    f.text(
        30,
        270,
        "Median of 10 cold runs (fresh process each), laptop → us-east-1. COG open = STAC Item fetch; GeoZarr open = zarr.json.",
        "xs",
    )
    f.save("multiband_time.svg")


if __name__ == "__main__":
    structure()
    tile_request_flow()
    cog_header()
    cog_blocks()
    zarr_tree()
    zarr_shard()
    round_trips()
    bytes_chart()
    time_chart()
    multiband_round_trips()
    multiband_bytes_chart()
    multiband_time_chart()
