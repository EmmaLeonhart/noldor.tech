# Noldor Technologies — logo + landing site (first pass)

**Date:** 2026-06-16
**Status:** Approved (brainstorming complete, user said "let's go")

## Context

Noldor Technologies (`noldor.tech`) does **vector symbolic architecture for
analogue / edge-AI hardware**. The company name is written **Ñoldor** — the
archaic Quenya spelling with the velar nasal `ñ`. The logo is the name rendered
in tengwar (Quenya mode), per the tecendil transcription:
<https://www.tecendil.com/?q=%C3%91oldor&mode=quenya>.

A raster of that render exists at `data_lake/Noldor.png` (dark `#333` glyphs).
This first pass turns it into clean vector logos and a minimal landing page
deployed to GitHub Pages at `https://noldor.tech`.

The earlier name "Yantra" is **not** mentioned anywhere in deliverables.

## Deliverables

- `assets/noldor-wordmark.svg` — full **Ñoldor** wordmark, clean vector paths,
  single fill via `currentColor` (recolors with CSS), no font dependency.
- `assets/noldor-letter.svg` — the leftmost tengwa (the archaic `ñ` / *ñoldo*)
  isolated, used as monogram + favicon source.
- `index.html` + small CSS — one-page landing: centered wordmark, one-line
  tagline, letter favicon. Dark logo on light background, responsive/centered,
  no framework.
- `CNAME` = `noldor.tech`.
- Tests (`pytest`) + GitHub Actions CI + GitHub Actions Pages deploy workflow.

## Logo production approach

Chosen: **rebuild from a Tengwar font** (not raster-trace), so the paths are
clean and editable.

1. **Source a font.** The PNG reads as **Tengwar Annatar Italic** (slanted
   calligraphic curls). Obtain a matching Tengwar font into a *gitignored*
   working dir — preferring tecendil's own open-source font if reachable, since
   that guarantees a glyph-for-glyph match. Determine the correct Quenya-mode
   glyph + tehta sequence for `Ñoldor`.
2. **Outline glyphs → SVG.** Use `fontTools` (`svgPathPen` over the `glyf`
   table) to extract each glyph's outline as an SVG path. Assemble into one
   `<svg>` with a single `currentColor` fill. **Ship outlines only — never the
   font file** — so font redistribution licensing is a non-issue and the SVG is
   self-contained.
3. **Verify the match.** Rasterize the generated SVG and overlay it against
   `Noldor.png` with Pillow; confirm the shapes line up before committing.
4. **Isolate the first glyph** into `noldor-letter.svg`.

**Fallback:** if no font render matches the PNG closely, raster-trace
`Noldor.png` (install `potrace`/a python tracer) to produce a clean vector that
looks right. A mismatched logo is never shipped silently.

## Site

- Static `index.html` + one CSS file. Centered wordmark (inline or `<img>` SVG),
  one-line tagline: *vector symbolic architecture for analogue / edge-AI
  hardware* (final wording TBD-light, user can tweak). Letter SVG as favicon.
- Near-black logo (`#333`) on a light background; responsive and centered.
- No JS framework; minimal/no JS.

## Repo, CI, deploy

- Public GitHub repo named **noldor.tech**; local folder stays `noldor`.
- **GitHub Pages via GitHub Actions** (`actions/upload-pages-artifact` +
  `actions/deploy-pages`), not legacy branch Pages.
- `CNAME` file = `noldor.tech` for the custom domain.
- CI workflow runs the test suite on push/PR.

## Testing

- `pytest`: each SVG parses as well-formed XML and has ≥1 non-empty `<path>`;
  `index.html` references both the wordmark and the favicon; `CNAME` content is
  exactly `noldor.tech`.

## Out of scope (this pass)

- Multi-section site, contact forms, analytics, the old "Yantra" name.
