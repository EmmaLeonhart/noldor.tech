# noldor — Long-horizon backlog

**Abstract destinations**, not steps. Items here get decomposed into concrete
steps in `queue.md` one at a time, as they become unblocked. See `CLAUDE.md`
§ "Queue and longer-horizon work".

---

## Site content & style

- **Mine the old Yantra site for style.** The user wants the general visual
  style they've been developing on the Yantra site carried over here. *Blocked
  on:* the Yantra repo location / live URL (need it from the user). Site should
  stay **practical** — explain what Noldor does — not lore-heavy
  (`data_lake/notes.md`).
- **Grow past the single landing page.** Sections explaining the product
  (vector symbolic architecture, analogue hardware, edge AI), who it's for, and
  contact — once direction firms up.

## Yantra migration / redirects

- **Preserve Yantra inbound links.** Yantra pages will redirect here and link in;
  avoid bare 404s. The user will drop a **sitemap / list of Yantra pages** into
  `data_lake/`. Decide which to keep, and provide at least a catch-all / landing
  for the rest. *Blocked on:* that page list arriving in the data lake.
- **Cron to watch the data lake (3pm Pacific).** The user asked for a scheduled
  job that checks `data_lake/` at 3pm Pacific for the Yantra sitemap/page list.
  *Note:* `CronCreate` is session-local (dies with the session); a job that must
  fire "tomorrow at 3pm" needs the session running then, or a durable mechanism.
  Confirm approach with the user.

## Logo / brand polish

- **Monogram variant decision.** Current `noldor-letter.svg` is the first tengwa
  *with* its o-vowel curl. A bare-*ñoldo* (letter only, no vowel) variant is a
  quick alternative if preferred.
- **Possible exact-Telcontar wordmark.** The current wordmark is a faithful
  trace of the tecendil PNG (IoU 0.987). If a glyph-perfect Telcontar font build
  is ever wanted, it needs a shaping engine (HarfBuzz/Graphite) the current
  tooling lacks.
