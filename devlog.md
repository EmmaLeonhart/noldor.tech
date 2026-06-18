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
- **Vendored the shared visual identity:** copied Yantra's `site/identity.css`
  (the canonical shared file across emmaleonhart.com + sister sites) and
  `site/celestial.css` (the periwinkle→cyan→violet starfield/glow layer used by
  Yantra + Sutra) into the repo root, byte-for-byte. This is the basis for the
  "common visual identity with Sutra" the user asked for; the landing restyle
  links them next.

## 2026-06-16 — Landing rebuilt on the shared identity (dark, celestial, sections)

Restyled `index.html` onto the shared identity and expanded it from a single
hero into a practical one-pager — Noldor now visually matches the Sutra/Yantra
family.

- **Identity wiring:** links `identity.css` + `celestial.css` (+ page-only
  `styles.css`), Google Fonts (Inter / Instrument Serif / JetBrains Mono),
  `data-theme="dark"` default with a pre-paint script, and the shared
  weather-sunny/night **theme toggle** (persists to `localStorage`). The tengwar
  wordmark is the hero, `currentColor`-driven with a periwinkle drop-shadow glow
  in dark; verified both themes + the toggle via Playwright.
- **`styles.css` reduced to page layout only** — no local palette/`.btn`
  redeclaration (the thing that makes sister sites diverge).
- **Practical sections** (not lore): *What we build* (VSA for analog hardware +
  edge AI), *Built on Sutra* (links live `sutra.noldor.tech`), *Get in touch*
  (GitHub + Sutra links). Dropped an invented `hello@` email rather than ship an
  unverified inbox — contact is via GitHub for now (a real address can be wired
  up later).
- **Tests:** added checks for identity/celestial linkage + presence and the
  dark-default toggle; `test_no_yantra_mention` caught a "Yantra" leak in an HTML
  comment (the site must not surface the old name) — scrubbed. **11 passing.**
- Deploy workflow now ships `identity.css` + `celestial.css`.

## 2026-06-16 — Brand mark switched to "Ñol" (Option B, user's firm choice)

User firmly chose the two-tengwa mark over the single-tengwa monogram.

- Produced it as a **crisp vector** (not the low-res `data_lake/Noldor logo.png`):
  `tools/build_logos.py` now cuts the first *two* tengwar — *Ñol* (ñoldo + lambe)
  — straight from the traced wordmark → `assets/noldor-mark.svg`. Removed the
  superseded `noldor-letter.svg`.
- **Favicons** regenerated from the mark; since it's wider than tall, they're
  letterboxed onto a square transparent canvas (no squash) at 2× then fit for
  crispness. `favicon.svg` / `favicon-32.png` / `apple-touch-icon.png` /
  `icon-512.png` updated.
- Updated README + tests (`noldor-mark.svg`). **11 passing.**
- Noted polish for later (`todo.md`): the mark is dark `#2b2b2b`, so it's
  low-contrast on dark browser chrome — a dual-tone / theme-aware favicon would
  fix it.

## 2026-06-16 — Theme-aware favicon + opaque app icons

Work-loop item pulled from `todo.md`.

- **`favicon.svg` is now theme-aware:** an embedded `<style>` with
  `@media (prefers-color-scheme: dark)` flips the `currentColor` glyph — dark on
  light chrome, light on dark chrome. Verified both schemes render correctly in
  Chromium.
- **App icons are opaque:** `favicon-32.png` / `apple-touch-icon.png` /
  `icon-512.png` now render the light mark on an opaque deep-navy square
  (`#0c0c14`, `--bg-soft`) with an inset margin — readable on any background and
  iOS-safe (no black-filled transparency).
- **Tests:** added `test_favicon_svg_is_theme_aware` + `test_app_icons_are_opaque`.
  **13 passing.**

## 2026-06-16 — Open Graph / social-card image (1200×630)

Work-loop item pulled from `todo.md`.

- `og:image` previously pointed at the 512² square icon; social platforms want a
  1200×630 landscape card. `tools/build_logos.py` now renders
  `assets/og-image.png` — the light wordmark on the brand navy gradient with a
  periwinkle glow, "NOLDOR TECHNOLOGIES" (letter-spaced) + the tagline.
- Wired `og:image` (+ width/height) and a full `twitter:card`
  (`summary_large_image`, title, description, image) into `index.html`.
- Test `test_og_image_is_landscape_card` (exists, 1200×630, opaque, referenced).
  **14 passing.** Removed the now-done theme-aware-favicon / OG-bg note from
  `todo.md`.

## 2026-06-16 — Branded 404 page

Work-loop item (the Yantra→Noldor redirect preserves paths, so inbound links
land on noldor.tech paths that don't exist here; `notes.md` asked for at least
"something… just to be safe").

- Added `404.html` on the shared identity (links `identity.css` + `celestial.css`,
  dark default + theme toggle + aurora), with the inlined wordmark, a
  "404 — page not found" line, and a `.btn-primary` link home. GitHub Pages
  serves it automatically for unknown paths. Verified rendering via Playwright.
- Added `404.html` to the deploy artifact (`deploy.yml`).
- Tests: `test_404_page_on_shared_identity` + `test_404_in_deploy_artifact`.
  **16 passing.**

## 2026-06-17 — SEO: robots.txt + sitemap.xml

Work-loop item. Also verified the vendored `identity.css` / `celestial.css` are
still byte-identical to upstream Yantra (no drift).

- Added `robots.txt` (allow all, points to the sitemap) and `sitemap.xml`
  (lists `https://noldor.tech/`); both added to the deploy artifact.
- Tests: robots→sitemap reference, sitemap well-formedness + homepage `loc`,
  deploy inclusion. **19 passing.**

## 2026-06-17 — Reverted the celestial/identity theme (too garish)

User feedback: the shared dark/celestial identity theming was too garish; go
back to the earlier clean look. Full revert (their choice):

- Restored `index.html` + `styles.css` to the earlier minimal landing
  (commit `ae7e73c`): warm off-white, dark wordmark, "NOLDOR TECHNOLOGIES",
  one-line tagline, single deep-violet hairline, footer; light/dark via
  `prefers-color-scheme`. Dropped the dark-default, theme toggle, celestial
  starfield/glow, and the added content sections.
- Removed `identity.css`, `celestial.css`, and `assets/og-image.png` (the dark
  social card). Re-skinned `404.html` to the clean minimal style (links
  `styles.css`, no identity/celestial).
- `tools/build_logos.py`: dropped OG-image generation; keeps wordmark, the
  "Ñol" mark, and favicons. `deploy.yml`: stopped shipping identity/celestial.
- Kept (separate from the page theme, not part of the complaint): the Option-B
  "Ñol" brand mark + theme-aware favicon + SEO files (`robots.txt`,
  `sitemap.xml`).
- Tests updated: added `test_no_celestial_identity_theme` (regression guard that
  the theme can't silently return); removed identity/toggle/og-image tests;
  re-pointed the 404 test. **17 passing.** Verified the reverted page renders the
  clean look (Playwright).

## 2026-06-17 — Site explainer content ("what we do") — deployed for review

User asked for info on the site explaining what Noldor does. Drafted three
short sections in the clean minimal style (no celestial), grounded in the user's
own Sutra docs (`what-is-sutra.md`, `vision.md`) — no invented specifics:

- **What we do** — computation is geometric; VSA puts symbolic/structured
  computation in vector space where bind/bundle/similarity are matmul/add/dot.
- **Why analog & edge** — it all reduces to matrix multiplication, which analog
  in-memory + edge accelerators run cheaply → computation near the data.
- **Sutra** — the geometrically compiled language; links `sutra.noldor.tech`.

Process note: first parked the draft on a `content-draft` branch (not deployed)
pending sign-off; the user reviews on the live site, so merged to `main` to
deploy for review. Iterate/revert on their feedback (the revert path is proven).
Open question flagged to the user: Sutra-as-"software-layer" framing.
