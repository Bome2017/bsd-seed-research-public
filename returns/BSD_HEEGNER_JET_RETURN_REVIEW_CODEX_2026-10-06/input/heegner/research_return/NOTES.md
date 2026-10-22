# Research notes (continuation run, 2026-10-06)

## Startup

`NOTES.md`, `RESUME.md` and `STATE.json` were created first. Then `prepare_reference.py` ran
(5,180 members verified), followed by `prepare_latest_review.py` (64 members verified). The
extracted trees are git-ignored (`reading_set/`, `accepted/`).

## Read, in order

1. `WHAT_WE_LEARNED.md`, `CONSTRUCTION_WORK.md`, `TASK.md`.
2. Accepted review:
   * `REPORT.md`, `CORRECTIONS.md`, `MATHEMATICAL_RECONSTRUCTION.md`, `HANDOFF.md`;
   * the original return's `RESULT.md`, `HANDOFF.md`, `ASSUMPTIONS.json`;
   * `checks/genus2_quotients.py`.
3. Reading set:
   * `ARISTOTLE_PROMPT.md` (via the research map);
   * `guide/01`, `guide/04`, `guide/05`;
   * `guide/03` cards W01–W07 in full, and all card headings.
4. Compendium, by targeted search:
   * p-adic regulator entries;
   * generalized Kato / diagonal-cycle entries (H5–H9, K9);
   * the `D=-23` twist certificate units;
   * the Heegner/Kolyvagin entries (E12a-158, E6-022/024, Kim arXiv:2609.15328 applicability);
   * the A3 rank-two Heegner analogue block.

Not everything extracted was read. The compendium (≈9 MB) and the historical stops file were
searched, not read in full.

## Mechanism choice

Mechanisms considered and their first failed implications (none new):

* receiver relation kernels (W16–W21);
* `p`-adic BSD / Kato–Perrin-Riou leading terms (unit-ness of `L_p^*/Reg_p` is equivalent to
  the target);
* generalized Kato classes (record K9 CLOSED_NEGATIVE);
* genus-two family of twisted points (points give lower bounds only);
* Heegner over `ℚ(√−23)` (blocker: "no cross-prime index").

Selected: the last, with the new operation of supersingular inert auxiliary primes.

## Side attempt

A small-height search for a rational point on `E^{−23}` (`|x|` small, denominators `w < 60`)
found nothing within the time limit. It was abandoned as peripheral, since the record already
certifies rank 1 analytically.

## Cleanup

After reading, the generated extractions `reading_set/` and `accepted/` were deleted from the
project directory. Both are reproducible with `prepare_reference.py` and
`prepare_latest_review.py`, and the original ZIPs in `payload/` are unchanged. The reading set
contains historical scanner-control Lean files that deliberately declare axioms. Leaving them
expanded inside the project tree would make it look as though axioms had been introduced.
