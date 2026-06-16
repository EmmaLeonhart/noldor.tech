# noldor — Work Queue

**This file is a queue of *concrete, executable steps*, not a state snapshot.**
Finished work is deleted from here and recorded in `devlog.md` (dated entry) +
`git log`, in the same commit. Do not leave checkmarks or "done" markers — if an
item is still here, it is not done. See `CLAUDE.md` § "Workflow Rules".

Spec for the current work: `docs/superpowers/specs/2026-06-16-noldor-logo-site-design.md`.

> Running interactively with the user present on a bounded task, so the
> three-cron autonomous playbook is **not** started this session.

---

## Active — Noldor logo + landing site (first pass)

6. **GitHub Pages via Actions + custom domain.** Create the public repo
   **noldor.tech**, push `main`, confirm CI + the Pages deploy workflow are
   green, and that the custom domain serves. (Site files, `CNAME`, and both
   workflows are already committed.)

---

## Always last

A. **Run an end-of-session summary** of everything that happened this session.

---

## Pointers

- Long-horizon backlog: `todo.md` (create when the first pass is done).
- Completed work: `devlog.md`. Narrative history: `git log`.
