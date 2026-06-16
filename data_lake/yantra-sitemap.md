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
- **How:** path-preserving JS redirect — `site/index.html` + `site/404.html`
  forward `yantraos.org/<path>` → `noldor.tech/<path>`, so nothing 404s even
  for paths that never existed.
- **Target:** 2026-06-18, 3pm Pacific.
- **Yantra PR (prepared, not yet merged):** https://github.com/EmmaLeonhart/Yantra/pull/1
- A local cron checks this data lake at 3pm Pacific; once this sitemap is
  present and the date has arrived, it merges the PR to make the redirect live.

## Decision notes

The site is one page, so "preserving pages" is trivial — the single landing
page redirects to the noldor.tech home. No content needs porting beyond
whatever of the messaging/style you want to fold into noldor.tech itself.
