# noldor — Long-horizon backlog

**Abstract destinations**, not steps. Items get decomposed into `queue.md` one at
a time as they become unblocked. See `CLAUDE.md` § "Queue and longer-horizon work".

---

## Brand / cross-site identity

- **Keep Noldor on the canonical shared identity.** Yantra's `site/identity.css`
  is the one shared visual-identity file across emmaleonhart.com + sister sites
  (Yantra, Sutra, Loka). As it evolves upstream, keep Noldor's vendored copy in
  sync rather than diverging. (Active decomposition in `queue.md`.)
- **`sutra.noldor.tech`.** A `sutra.yantraos.org-redirect` already points at
  `sutra.noldor.tech`; serving that subdomain is a Sutra-repo concern, noted here
  for coordination.

## Site content

- **Grow the site as direction firms up.** Beyond the practical landing:
  deeper product explanation, who it's for, links across the Yantra/Sutra/Loka
  family. Stay practical, not lore-heavy (`data_lake/notes.md`).

## Logo polish

- **Theme-aware favicon.** The brand mark `noldor-mark.svg` is dark `#2b2b2b`,
  so it's low-contrast on dark browser chrome / dark social cards. Add a
  dual-tone or `prefers-color-scheme` favicon (and consider a branded background
  for the OG `icon-512`).
- **Maybe use the mark in the topbar.** Currently the topbar brand is the text
  "Noldor"; the *Ñol* mark could replace/accompany it.
- **Possible exact-Telcontar wordmark.** Current wordmark is a faithful trace of
  the tecendil PNG (IoU 0.987). A glyph-perfect Telcontar build would need a
  shaping engine (HarfBuzz/Graphite) the current tooling lacks.
