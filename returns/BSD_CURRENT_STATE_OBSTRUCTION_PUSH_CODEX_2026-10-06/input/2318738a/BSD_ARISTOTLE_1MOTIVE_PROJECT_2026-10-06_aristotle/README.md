This project was edited by [Aristotle](https://aristotle.harmonic.fun).

To cite Aristotle:
- Tag @Aristotle-Harmonic on GitHub PRs/issues
- Add as co-author to commits:
```
Co-authored-by: Aristotle (Harmonic) <[email-redacted]>
```

# Aristotle project: a fixed 1-motive receiver for the BSD seed (2026-10-06)

**Read order**
1. `CURRENT_FRONTIER.md`
2. `DELTA_TASK_1MOTIVE.md`, which governs this run
3. `TASK.md`, for the do-not list, the admission test and the return format

**Contents**
- The canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2). In `2_CLOSED_LANES/` it adds:
  - `RANK2_ANCHOR_RESULT.md`;
  - `DERIVED_GROSS_RESULT.md`;
  - `RECEIVER_FIXED_LOCAL_CARRIER.md`;
  - the matching closed-lanes rows.
- The delta task, `DELTA_TASK_1MOTIVE.md` (revised per Pro, 10-06). Its object is M_E = [ℤ² → E] with u(e_i) = P_i. The run asks for:
  - the fixed receiver Sel(ℚ, M_E)(p) ≅ Ш(E/ℚ)[p];
  - a record that BSS and Sakamoto do not apply to T_pM_E (proved in the pre-check);
  - a test of the Macias Castillo–Sano Selmer-complex determinant / Stark-system construction, and of its canonical element and globalization.
- The Lean templates, placed at buildable module paths (`Coinvariant/`, `RequestProject/Continuation/`):
  - Lean v4.28.0 with Mathlib v4.28.0 (8f9d9cff);
  - `lakefile.toml` declares both libraries.

**Submission:** see `SUBMIT_COMMAND.txt`. The prompt text is in `SUBMISSION_PROMPT.txt`.
