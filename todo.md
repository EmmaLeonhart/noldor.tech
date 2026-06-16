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

- **Monogram / alt-mark decision.** Current `noldor-letter.svg` is the first
  tengwa with its o-curl; `data_lake/Noldor logo.png` is a two-tengwa ("Ñol")
  alternative; a bare-*ñoldo* is a third option. Pick one with the user.
- **Possible exact-Telcontar wordmark.** Current wordmark is a faithful trace of
  the tecendil PNG (IoU 0.987). A glyph-perfect Telcontar build would need a
  shaping engine (HarfBuzz/Graphite) the current tooling lacks.
