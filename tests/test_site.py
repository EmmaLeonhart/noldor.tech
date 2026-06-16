"""Validate the committed site assets and landing page.

These tests guard the deliverables (SVGs, favicons, index.html, CNAME). They
parse the shipped files directly; they do not regenerate anything.
"""
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SVG_NS = "{http://www.w3.org/2000/svg}"

SVG_FILES = ["noldor-wordmark.svg", "noldor-mark.svg", "favicon.svg"]


@pytest.mark.parametrize("name", SVG_FILES)
def test_svg_is_well_formed_with_nonempty_paths(name):
    path = ASSETS / name
    assert path.exists(), f"missing {name}"
    tree = ET.parse(path)  # raises on malformed XML
    root = tree.getroot()
    assert root.tag == f"{SVG_NS}svg"
    assert root.get("viewBox"), f"{name} has no viewBox"
    paths = root.iter(f"{SVG_NS}path")
    ds = [p.get("d", "").strip() for p in paths]
    ds = [d for d in ds if d]
    assert ds, f"{name} has no non-empty <path>"
    # paths should contain actual move/curve commands, not be trivially short
    assert any(len(d) > 50 for d in ds), f"{name} paths look empty/trivial"


def test_wordmark_uses_currentcolor():
    svg = (ASSETS / "noldor-wordmark.svg").read_text(encoding="utf-8")
    assert 'fill="currentColor"' in svg


def test_favicon_pngs_exist_and_nonempty():
    for name in ["favicon-32.png", "apple-touch-icon.png", "icon-512.png"]:
        p = ASSETS / name
        assert p.exists(), f"missing {name}"
        assert p.stat().st_size > 200, f"{name} too small"
        assert p.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", f"{name} not a PNG"


def test_index_html_references_assets():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "<title>Noldor Technologies</title>" in html
    # inline wordmark present
    assert '<svg class="wordmark"' in html
    # favicons wired up
    assert "assets/favicon.svg" in html
    assert "assets/favicon-32.png" in html
    assert "assets/apple-touch-icon.png" in html
    # links its stylesheets, including the shared identity layers
    assert 'href="styles.css"' in html
    assert 'href="identity.css"' in html
    assert 'href="celestial.css"' in html


def test_shared_identity_files_present():
    """The vendored canonical identity + celestial layers must ship."""
    for name in ["identity.css", "celestial.css"]:
        p = ROOT / name
        assert p.exists(), f"missing {name}"
        assert p.stat().st_size > 1000, f"{name} too small"


def test_index_has_theme_toggle_dark_default():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert 'data-theme="dark"' in html  # dark default on <html>
    assert 'id="theme-toggle"' in html  # toggle control present


def test_favicon_svg_is_theme_aware():
    svg = (ASSETS / "favicon.svg").read_text(encoding="utf-8")
    assert "@media (prefers-color-scheme: dark)" in svg, "favicon.svg not theme-aware"


def test_app_icons_are_opaque():
    """Raster app icons must be fully opaque (read on any bg; iOS-safe)."""
    from PIL import Image
    for name in ["favicon-32.png", "apple-touch-icon.png", "icon-512.png"]:
        im = Image.open(ASSETS / name).convert("RGBA")
        alpha = im.getchannel("A").getextrema()
        assert alpha[0] == 255, f"{name} has transparency (min alpha {alpha[0]})"


def test_index_html_has_tagline():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "Vector symbolic architecture" in html


def test_cname_is_custom_domain():
    cname = (ROOT / "CNAME").read_text(encoding="utf-8").strip()
    assert cname == "noldor.tech"


def test_no_yantra_mention():
    """The old name must not appear in shipped site files."""
    for f in ["index.html", "styles.css"]:
        text = (ROOT / f).read_text(encoding="utf-8")
        assert not re.search(r"yantra", text, re.I), f"'Yantra' found in {f}"
