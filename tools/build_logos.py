#!/usr/bin/env python
"""Generate the Noldor logo SVGs (and favicons) from data_lake/Noldor.png.

The source PNG is the tecendil Quenya-mode rendering of "Ñoldor" (Tengwar
Telcontar). We vectorize it with potrace into clean single-fill SVG paths and
ship outlines only — no font dependency.

This is a one-time, reproducible asset generator. It depends on:
  - potrace (Windows binary expected at .fonts/potrace_bin/.../potrace.exe,
    overridable via the POTRACE env var)
  - Pillow, cairosvg

The committed deliverables are the files under assets/. CI validates those;
it does not re-run this script (potrace is not installed in CI).

Run:  python tools/build_logos.py
"""
from __future__ import annotations

import io
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data_lake" / "Noldor.png"
ASSETS = ROOT / "assets"
WORK = ROOT / ".fonts"  # gitignored scratch space

POTRACE = os.environ.get(
    "POTRACE", str(WORK / "potrace_bin" / "potrace-1.16.win64" / "potrace.exe")
)

UPSCALE = 4
THRESHOLD = 128
PAD = 12  # padding (in source px) around a cropped region before upscaling


def ink_mask(gray: np.ndarray) -> np.ndarray:
    return gray < THRESHOLD


def load_gray() -> np.ndarray:
    return np.array(Image.open(SRC).convert("L"))


def ink_bbox(mask: np.ndarray) -> tuple[int, int, int, int]:
    ys, xs = np.where(mask)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def mark_xrange(mask: np.ndarray, gap: int = 6) -> tuple[int, int]:
    """X-range of the brand mark — the first two tengwar, "Ñol" (ñoldo + lambe).

    The leftmost column-run holds two touching tengwar (ñoldo + its o-tehta, and
    lambe) with no blank column between them; the next blank gap ends the run.
    The whole run is the chosen mark.
    """
    cols = np.where(mask.any(axis=0))[0]
    start = prev = cols[0]
    run_end = cols[-1] + 1
    for c in cols[1:]:
        if c - prev > gap:
            run_end = prev + 1
            break
        prev = c
    return int(start), int(run_end)


def crop_to_pbm(gray: np.ndarray, box: tuple[int, int, int, int], out_pbm: Path):
    x0, y0, x1, y1 = box
    x0 = max(0, x0 - PAD); y0 = max(0, y0 - PAD)
    x1 = min(gray.shape[1], x1 + PAD); y1 = min(gray.shape[0], y1 + PAD)
    crop = Image.fromarray(gray[y0:y1, x0:x1])
    big = crop.resize((crop.width * UPSCALE, crop.height * UPSCALE), Image.LANCZOS)
    arr = np.array(big)
    pbm = Image.fromarray(np.where(arr < THRESHOLD, 0, 255).astype("uint8")).convert("1")
    pbm.save(out_pbm)


def run_potrace(pbm: Path, svg: Path):
    if not Path(POTRACE).exists():
        sys.exit(f"potrace not found at {POTRACE} (set POTRACE env var)")
    subprocess.run(
        [POTRACE, "--svg", "--turdsize", "2", "--alphamax", "1.0",
         "--opttolerance", "0.2", "-o", str(svg), str(pbm)],
        check=True,
    )


def clean_svg(raw_svg: Path, title: str) -> str:
    """Turn potrace output into a minimal, themeable SVG (fill=currentColor)."""
    text = raw_svg.read_text()
    w = float(re.search(r'width="([\d.]+)', text).group(1))
    h = float(re.search(r'height="([\d.]+)', text).group(1))
    transform = re.search(r"<g transform=\"([^\"]+)\"", text).group(1)
    paths = re.findall(r"<path d=\"([^\"]+)\"", text)
    path_els = "\n  ".join(f'<path d="{d}"/>' for d in paths)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" '
        f'fill="currentColor" role="img" aria-label="{title}">\n'
        f'  <title>{title}</title>\n'
        f'  <g transform="{transform}">\n  {path_els}\n  </g>\n'
        f"</svg>\n"
    )


def _font(names, size):
    """First available TrueType font from `names`, falling back to default."""
    from PIL import ImageFont
    for n in names:
        for path in (n, f"C:/Windows/Fonts/{n}"):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def _draw_tracked(draw, xy_center_y, text, font, fill, tracking, width):
    """Draw horizontally-centered text with letter-spacing (tracking, px)."""
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = (width - total) / 2
    for ch, w in zip(text, widths):
        draw.text((x, xy_center_y), ch, font=font, fill=fill)
        x += w + tracking


def build_og_image(light_svg: str, cairosvg):
    """Render assets/og-image.png — a 1200x630 social card: light wordmark on the
    brand navy with a periwinkle glow, company name, and tagline."""
    from PIL import ImageDraw, ImageFilter
    W, H = 1200, 630
    top, bot = (7, 7, 12), (12, 12, 22)
    img = Image.new("RGB", (W, H), top)
    # vertical gradient
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        px_row = tuple(round(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = px_row
    # periwinkle glow, top-centre
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W / 2 - 430, -260, W / 2 + 430, 360], fill=(139, 155, 255, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img.convert("RGBA"), glow)

    # wordmark (light), centred upper
    wm_svg = ASSETS_wordmark_light()
    png = cairosvg.svg2png(bytestring=wm_svg.encode(), output_width=1280)
    wm = Image.open(io.BytesIO(png)).convert("RGBA")
    target_w = 580
    scale = target_w / wm.width
    wm = wm.resize((target_w, max(1, round(wm.height * scale))), Image.LANCZOS)
    wm_y = 108
    img.alpha_composite(wm, ((W - wm.width) // 2, wm_y))

    d = ImageDraw.Draw(img)
    name_f = _font(["arialbd.ttf", "Arial.ttf"], 30)
    tag_f = _font(["arial.ttf", "Arial.ttf"], 30)
    _draw_tracked(d, wm_y + wm.height + 36, "NOLDOR TECHNOLOGIES",
                  name_f, (176, 188, 255, 255), 8, W)
    tagline = "Vector symbolic architecture for analog hardware and edge AI"
    tw = d.textlength(tagline, font=tag_f)
    d.text(((W - tw) / 2, wm_y + wm.height + 96), tagline, font=tag_f,
           fill=(140, 140, 170, 255))

    img.convert("RGB").save(ASSETS / "og-image.png")


def ASSETS_wordmark_light():
    svg = (ASSETS / "noldor-wordmark.svg").read_text(encoding="utf-8")
    return svg.replace('fill="currentColor"', 'fill="#ece8e1"')


def main():
    ASSETS.mkdir(exist_ok=True)
    WORK.mkdir(exist_ok=True)
    gray = load_gray()
    mask = ink_mask(gray)

    # Full wordmark
    word_pbm = WORK / "_word.pbm"; word_raw = WORK / "_word_raw.svg"
    crop_to_pbm(gray, ink_bbox(mask), word_pbm)
    run_potrace(word_pbm, word_raw)
    (ASSETS / "noldor-wordmark.svg").write_text(
        clean_svg(word_raw, "Ñoldor"), encoding="utf-8"
    )

    # Brand mark — the first two tengwar, "Ñol" (ñoldo + lambe)
    mx0, mx1 = mark_xrange(mask)
    sub = mask[:, mx0:mx1]
    ys = np.where(sub.any(axis=1))[0]
    mark_box = (mx0, ys.min(), mx1, ys.max() + 1)
    mark_pbm = WORK / "_mark.pbm"; mark_raw = WORK / "_mark_raw.svg"
    crop_to_pbm(gray, mark_box, mark_pbm)
    run_potrace(mark_pbm, mark_raw)
    (ASSETS / "noldor-mark.svg").write_text(
        clean_svg(mark_raw, "Ñol"), encoding="utf-8"
    )

    # Drop the older single-tengwa monogram if present (superseded by the mark).
    (ASSETS / "noldor-letter.svg").unlink(missing_ok=True)

    # ---- Favicons -----------------------------------------------------
    # Identity colours: dark glyph on light chrome, light glyph on dark.
    INK_DARK = "#2b2b2b"      # glyph on a light background
    INK_LIGHT = "#ece8e1"     # glyph on a dark background
    BG_NAVY = (12, 12, 20)    # --bg-soft #0c0c14, opaque app-icon background
    import cairosvg
    mark_svg = (ASSETS / "noldor-mark.svg").read_text(encoding="utf-8")

    # SVG favicon — theme-aware. currentColor follows the `color` property, which
    # a prefers-color-scheme media query flips, so the glyph stays legible on
    # both light and dark browser chrome.
    style = ("<style>svg{color:%s}"
             "@media (prefers-color-scheme: dark){svg{color:%s}}</style>"
             % (INK_DARK, INK_LIGHT))
    favicon_svg = re.sub(r"(<svg\b[^>]*>)", r"\1" + style, mark_svg, count=1)
    (ASSETS / "favicon.svg").write_text(favicon_svg, encoding="utf-8")

    # Raster app icons — light mark on an OPAQUE deep-navy square, letterboxed
    # with an inset margin (the mark is wider than tall; no squash). Opaque so
    # they read on any background, and so iOS doesn't fill transparency black.
    light_svg = mark_svg.replace('fill="currentColor"', f'fill="{INK_LIGHT}"')
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"),
                       (512, "icon-512.png")]:
        png = cairosvg.svg2png(bytestring=light_svg.encode(),
                               output_width=size * 2)  # 2x then fit, for crispness
        glyph = Image.open(io.BytesIO(png)).convert("RGBA")
        inner = size * 0.78  # inset margin
        scale = min(inner / glyph.width, inner / glyph.height)
        glyph = glyph.resize((max(1, round(glyph.width * scale)),
                              max(1, round(glyph.height * scale))), Image.LANCZOS)
        canvas = Image.new("RGBA", (size, size), (*BG_NAVY, 255))
        canvas.alpha_composite(glyph, ((size - glyph.width) // 2,
                                       (size - glyph.height) // 2))
        canvas.save(ASSETS / name)

    # ---- Open Graph / social card (1200x630) --------------------------
    build_og_image(light_svg, cairosvg)

    print("Wrote:")
    for p in sorted(ASSETS.iterdir()):
        print("  ", p.relative_to(ROOT), p.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
