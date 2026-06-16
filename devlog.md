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
