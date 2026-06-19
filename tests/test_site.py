"""Validate noldor.tech as a path-preserving redirect to topazcomputing.com.

noldor.tech is no longer a standalone site; it redirects (preserving path, query,
and hash) to https://topazcomputing.com. These tests guard that redirect.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = "https://topazcomputing.com"


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_cname_unchanged():
    assert read("CNAME").strip() == "noldor.tech"


def test_index_redirects_to_topaz_preserving_path():
    html = read("index.html")
    assert DEST in html
    assert "window.location.replace" in html
    assert "window.location.pathname" in html
    assert "window.location.search" in html
    assert "window.location.hash" in html


def test_404_redirects_to_topaz_preserving_path():
    html = read("404.html")
    assert DEST in html
    assert "window.location.replace" in html
    assert "window.location.pathname" in html


def test_redirect_is_noindex():
    assert 'name="robots" content="noindex"' in read("index.html")


def test_deploy_ships_redirect_files():
    deploy = read(".github/workflows/deploy.yml")
    assert "index.html 404.html CNAME" in deploy
