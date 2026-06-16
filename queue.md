# noldor — Work Queue

**This file is a queue of *concrete, executable steps*, not a state snapshot.**
Finished work is deleted from here and recorded in `devlog.md` (dated entry) +
`git log`, in the same commit. Do not leave checkmarks or "done" markers — if an
item is still here, it is not done. See `CLAUDE.md` § "Workflow Rules".

Spec for the current work: `docs/superpowers/specs/2026-06-16-noldor-logo-site-design.md`.

> Running interactively with the user present on a bounded task, so the
> three-cron autonomous playbook is **not** started this session.

---

## Active — Noldor logo + landing site (first pass)

1. **Source a Tengwar font + transcription.** Get a Tengwar font matching the
   PNG (Annatar Italic style; prefer tecendil's own open-source font for an
   exact match) into a *gitignored* working dir (`.fonts/` or `data_lake/`).
   Work out the correct Quenya-mode glyph + tehta sequence for `Ñoldor`.

2. **Generate `assets/noldor-wordmark.svg`.** Extract glyph outlines with
   `fontTools` (`svgPathPen`), assemble one `<svg>` with a single `currentColor`
   fill, ship outlines only (no font file). Overlay-compare against
   `data_lake/Noldor.png` with Pillow to confirm the match. Trace-fallback
   (`potrace`/python tracer) only if the font render can't match.

3. **Generate `assets/noldor-letter.svg` + favicon.** Isolate the leftmost
   tengwa (archaic `ñ`/*ñoldo*) into its own SVG monogram; produce favicon
   asset(s) from it.

4. **Build `index.html` + CSS.** Centered wordmark, one-line tagline (*vector
   symbolic architecture for analogue / edge-AI hardware*), letter favicon,
   near-black logo on light bg, responsive. No framework.

5. **Tests + CI.** `pytest`: SVGs are well-formed XML with >=1 non-empty path;
   `index.html` references wordmark + favicon; `CNAME` == `noldor.tech`. Add
   `.github/workflows/ci.yml` running the suite on push/PR.

6. **GitHub Pages via Actions + custom domain.** Add `CNAME` file, add a Pages
   deploy workflow (`actions/upload-pages-artifact` + `actions/deploy-pages`),
   create the public repo **noldor.tech**, push, confirm CI + deploy are green.

---

## Always last

A. **Run an end-of-session summary** of everything that happened this session.

---

## Pointers

- Long-horizon backlog: `todo.md` (create when the first pass is done).
- Completed work: `devlog.md`. Narrative history: `git log`.
