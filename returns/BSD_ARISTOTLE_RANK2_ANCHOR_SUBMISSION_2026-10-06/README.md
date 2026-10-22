# Aristotle project: the rank-two global anchor (BSD seed, 2026-10-06)

**Read order**
1. `CURRENT_FRONTIER.md`
2. `DELTA_TASK_RANK2_ANCHOR.md`, which governs this run
3. `TASK.md`, for the do-not list, the admission test and the return format

**Contents**
- The canonical packet `BSD_SEED_FRONTIER_2026-10-06` (lab commit 6b32e5a): `CURRENT_FRONTIER.md`, `TASK.md`, `1_PROVED_STATE/`, `2_CLOSED_LANES/` and `3_LIVE_QUESTION/`.
- The delta task for this run, `DELTA_TASK_RANK2_ANCHOR.md`.
- The Lean templates, placed at buildable module paths (`Coinvariant/`, `RequestProject/Continuation/`):
  - Lean v4.28.0 with Mathlib v4.28.0 (8f9d9cff); `lakefile.toml` declares both libraries.
  - Every file was compiled locally beforehand. All theorems use only the standard axioms, except `TameCircularity.slTwoCount_eq` (`native_decide`). See `3_LIVE_QUESTION/lean/LEAN_RECOMPILE.txt`.

**Submission:** see `SUBMIT_COMMAND.txt`. The prompt text is in `SUBMISSION_PROMPT.txt`.
