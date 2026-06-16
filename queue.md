# noldor — Work Queue

**This file is a queue of *concrete, executable steps*, not a state snapshot.**
Finished work is deleted from here and recorded in `devlog.md` (dated entry) +
`git log`, in the same commit. Do not leave checkmarks or "done" markers — if an
item is still here, it is not done. See `CLAUDE.md` § "Workflow Rules".

**Three-cron playbook is RUNNING this session** (work-loop `3 * * * *`,
auto-flush `15 * * * *`, status-report `42 * * * *`). The pinned tail keeps them
alive and signs off. Work items run top to bottom.

---

## Active — Visual identity + content (decomposed from `data_lake/notes.md`)

3. **Restyle `index.html` to the shared identity.** Link `identity.css`; rebuild
   the landing on its palette/type/tokens (dark default). Keep the tengwar
   wordmark (it uses `currentColor`, so it adapts to theme). Remove now-duplicated
   declarations from `styles.css` (page-specific layout only — do NOT re-declare
   `.btn` or palette locally; that's what made the sister sites diverge).

4. **Add the dark/light theme toggle + web fonts.** Wire the toggle (persist to
   `localStorage`, default dark) using the MkDocs-Material weather-sunny /
   weather-night icons that match the Sutra docs + Yantra site. Ensure Instrument
   Serif / Inter / JetBrains Mono actually load.

5. **Expand the landing into practical product sections.** Tight, practical
   sections (not lore): what Noldor does (vector symbolic architecture for
   analog hardware + edge AI), the Sutra connection (link to sutra.noldor.tech),
   and a contact line. Pull factual cues from Sutra docs
   (`what-is-sutra.md`, `vision.md`). Keep it on-brand and short.

6. **[needs-user] Alt logo mark `data_lake/Noldor logo.png`.** Shows the first
   two tengwar ("Ñol"). Decide with the user whether it replaces/augments the
   current single-tengwa monogram + favicon. Do NOT swap silently — flagged for
   the user; skip autonomously until they choose.

---

## Always last — keep the crons alive and sign off

A. **Ensure the three crons are running** — work-loop (`3 * * * *`), auto-flush
   (`15 * * * *`), status-report (`42 * * * *`). Start/restart if a planning
   burst or queue re-fill killed them.
B. **Run the status-report action once more, independently** — an end-of-session
   summary of everything that happened this session.

---

## Pointers

- Long-horizon backlog: `todo.md`. Completed work: `devlog.md`. History: `git log`.
- Done (parallel session): Yantra→Noldor redirect (PR #1), `data_lake/yantra-sitemap.*`,
  3pm-Pacific cutover cron. Don't redo these.
