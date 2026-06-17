# Yantra site (yantraos.org) — sitemap / page inventory

Captured 2026-06-16 from the `EmmaLeonhart/Yantra` repo. `yantraos.org` is
served only from that repo's `site/` directory (via `.github/workflows/pages.yml`).
It is a **single-page landing site** — there are no separate sub-pages, only
in-page section anchors.

## Pages that actually exist

| URL | Source | Title | Keep? |
|-----|--------|-------|-------|
| `https://yantraos.org/` | `site/index.html` | Yantra — self-optimizing landing pages | TBD |

In-page anchors on `/`: `#how`, `#different`, `#sutra`, `#waitlist`.

Assets: `/identity.css`, `/celestial.css`.

## Rebrand cutover

- **To:** https://noldor.tech
- **How:** path-preserving JS redirect — `redirect/index.html` + `redirect/404.html`
  forward `yantraos.org/<path>` → `noldor.tech/<path>`, so nothing 404s even
  for paths that never existed.
- **Cutover date:** 2026-06-18.
- **Mechanism (time-based):** `.github/workflows/pages.yml` runs on a daily
  schedule and checks the date — it deploys `site/` (normal page) before the
  cutover and `redirect/` on or after it. No PR merge, no session cron. (The
  earlier PR #1 + 3pm local cron were superseded 2026-06-16.)

## Decision notes

The site is one page, so "preserving pages" is trivial — the single landing
page redirects to the noldor.tech home. No content needs porting beyond
whatever of the messaging/style you want to fold into noldor.tech itself.
