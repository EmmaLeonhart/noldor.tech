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
