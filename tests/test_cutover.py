"""Guard the date-gated cutover: noldor.tech -> topazcomputing.com on 2026-06-20.

Until the cutover date the deploy serves the Noldor landing; on/after it the
deploy serves the path-preserving redirect in redirect/. These tests check the
redirect files and that deploy.yml wires the date gate + schedule.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = "https://topazcomputing.com"
CUTOVER = "2026-06-20"


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_redirect_files_exist_and_target_topaz():
    for name in ("redirect/index.html", "redirect/404.html"):
        html = read(name)
        assert DEST in html, f"{name} does not target {DEST}"
        assert "window.location.replace" in html
        assert "window.location.pathname" in html  # path-preserving
        assert "window.location.search" in html
        assert "window.location.hash" in html
        assert 'name="robots" content="noindex"' in html


def test_deploy_has_cutover_gate_and_schedule():
    wf = read(".github/workflows/deploy.yml")
    assert f'CUTOVER="{CUTOVER}"' in wf, "cutover date missing/incorrect"
    assert "redirect/index.html" in wf, "deploy doesn't serve the redirect after cutover"
    assert "schedule:" in wf and "cron:" in wf, "no scheduled trigger to flip the cutover"


def test_landing_still_present_until_cutover():
    # The landing must still exist so pre-cutover deploys keep serving it.
    assert "<title>Noldor Technologies</title>" in read("index.html")
    assert read("CNAME").strip() == "noldor.tech"
