# noldor — Devlog

**This file is where "done" lives.** `queue.md` is delete-only: when a queue
item is finished, the item is **deleted from `queue.md`** and a dated entry
is **appended here**, in the same commit as the work, then pushed. Never
tick a box in place — a checked box left in `queue.md` is the failure mode
this file exists to prevent.

Also record releases (tag + a one-line note), notable milestones, and
anything else worth a chronological trail. Newest entries at the bottom.

This is the **same convention as the cleanvibe repo's own `devlog.md`** —
every cleanvibe-scaffolded project gets one for the same reason.

See `CLAUDE.md` § "Workflow Rules" and `queue.md`'s preamble.

---

## 2026-06-16 — Project scaffolded

Scaffolded with `cleanvibe new` (cleanvibe v1.13.1). Future entries
land here as queue items get deleted.

## 2026-06-16 — Logo SVGs generated (wordmark + letter mark + favicons)

Produced the Ñoldor logo assets from `data_lake/Noldor.png` (the tecendil
Quenya-mode render).

- **Font investigation → trace.** Identified `arnog/tecendil-js` as the engine
  and pulled the Tengwar Annatar family for comparison. Annatar didn't match the
  PNG (the big flowing *ando* is characteristic of tecendil's default **Tengwar
  Telcontar**, not Annatar). Telcontar relies on OpenType/Graphite shaping that
  Pillow can't drive reliably, so I took the design's pre-approved **trace
  fallback** — potrace on an upscaled bilevel of the PNG. Result matches the
  source at IoU 0.987 with clean smooth Béziers.
- **Deliverables** in `assets/`: `noldor-wordmark.svg` (full name, `currentColor`
  fill, outlines only — no font shipped), `noldor-letter.svg` (the leftmost
  tengwa = archaic ñ / *ñoldo* + its o-curl, split from lambe at the run's thin
  interior connection), plus `favicon.svg`, `favicon-32.png`,
  `apple-touch-icon.png`, `icon-512.png`.
- **Reproducible generator:** `tools/build_logos.py` (depends on potrace +
  Pillow + cairosvg; the committed `assets/` are the source of truth, CI does not
  re-run it).
- Open question for the user: monogram currently includes the o-vowel curl; a
  bare-*ñoldo* variant is a quick swap if preferred.

## 2026-06-16 — Landing page + tests + CI

- **`index.html` + `styles.css`:** minimal one-screen landing — inlined tengwar
  wordmark (so `currentColor` follows the theme), "NOLDOR TECHNOLOGIES"
  letter-spaced, tagline *"Vector symbolic architecture for analogue hardware
  and edge AI."*, accent hairline, footer. Light + dark via
  `prefers-color-scheme`; responsive via `clamp()`; reduced-motion honored.
  Verified rendering in both themes (Playwright screenshots). Tone kept
  practical per `data_lake/notes.md` (no lore).
- **Favicons + OG tags** wired up; `CNAME` = `noldor.tech`.
- **Tests:** `tests/test_site.py` — SVGs well-formed with non-empty paths,
  wordmark uses `currentColor`, favicons are real PNGs, `index.html` references
  all assets + tagline, `CNAME` correct, no "Yantra" in shipped files. 9 passing.
- **CI:** `.github/workflows/ci.yml` (pytest on push/PR). **Deploy:**
  `.github/workflows/deploy.yml` (assembles a clean `_site/`, `upload-pages-artifact`
  + `deploy-pages` on `main`).
- README rewritten to describe the project.

## 2026-06-16 — Deployed: public repo + GitHub Pages + custom domain

- Created public repo **EmmaLeonhart/noldor.tech** and pushed `main`.
- Enabled Pages (build_type=workflow); made the deploy workflow self-enabling
  (`configure-pages` `enablement: true`).
- **CI green; Pages deploy green.** Site live at
  `https://emmaleonhart.github.io/noldor.tech/` (HTTP 200, correct content).
- Custom domain: the apex DNS for `noldor.tech` already points at GitHub Pages
  (185.199.108–111.153, set up by the user). Registered the domain on the repo
  Pages config (`cname=noldor.tech`); **`http://noldor.tech/` serves HTTP 200**.
  HTTPS cert is provisioning (automatic); enable "Enforce HTTPS" once ready.
- Created `todo.md` with the long-horizon items from `data_lake/notes.md`
  (Yantra style mining, Yantra→noldor redirects / page-list handling, the
  3pm-Pacific data-lake cron, monogram variant). Most are blocked on user input.

**First-pass milestone:** Noldor Technologies logo + landing site is live.

## 2026-06-16 — Yantra → Noldor redirect cutover prepared

- **Yantra side (PR, not yet live):** `EmmaLeonhart/Yantra#1` replaces the
  `yantraos.org` landing page with a path-preserving JS redirect
  (`site/index.html` + `site/404.html`) → `noldor.tech/<path>`. CNAME stays on
  the Yantra repo; merging the PR makes the redirect live (pages.yml deploys).
- **Data lake:** `data_lake/yantra-sitemap.{json,md}` — inventory of the one
  live yantraos.org page (single-page site) + the cutover target/PR.
- **Cutover automation:** local cron at 3pm Pacific (session job 240b264c)
  reads the sitemap and, on/after 2026-06-18, merges Yantra PR #1.

## 2026-06-16 — Work loop started; "analog" wording fix

- Started the three-cron playbook for this session (work-loop `3 * * * *`,
  auto-flush `15 * * * *`, status-report `42 * * * *`) and decomposed the
  expanded `data_lake/notes.md` into the visual-identity queue.
- **Fix:** "analogue" → "**analog**" (user correction) in `index.html`
  (meta description, OG description, tagline) and `README.md`. Shipped files now
  contain no "analogue"; 9 tests still pass.
