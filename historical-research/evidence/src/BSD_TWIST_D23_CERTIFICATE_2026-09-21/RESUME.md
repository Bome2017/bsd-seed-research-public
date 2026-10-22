# RESUME — certify L'(E^{-23},1) != 0

Deliverable: a ball enclosure of the truncated sum (1) plus tail bound (2) with |sum| > B_D(T), or a costed report of
why that is not reached. Formulas and corpus pointers in STATE.json. Certificate logic: |truncated| > B(T) => nonzero.
Do not launch the full sum before the cutoff-adequacy and cost steps are recorded here.

## 2026-09-21 — feasibility answered
`FEASIBILITY_REPORT.md`. (1) T = 3.45e9 is NOT an adequate certificate cutoff: B = 0.343. Use T = 7e9 (B = 1.08e-6),
418 of 2333 segments, 17.9% of corpus. (2) Cost: stage W (2h33m, prime coefficients) is ALREADY PAID and is the corpus
we reuse; stage A streams at 2.0-2.2e7 terms/sec, so T = 7e9 is ~5.7 min. UNMEASURED: the E_1-in-balls kernel, which
does not exist yet. Format verified: int32 per prime, cross-checked a_5..a_37 and a_2243 against direct point counts.
Nothing computed, nothing launched.

## 2026-09-21 — corrections accepted (FEASIBILITY_CORRECTIONS_ACCEPTED.md governs)
- "Both questions answered" and "3.45e9 inadequate" WITHDRAWN: adequacy is UNDETERMINED until the truncated interval
  exists. 7e9 is a candidate only. Choose the cutoff FROM the interval and tail.
- The E_1/Arb/Taylor/remainder machinery ALREADY EXISTS (arbcore.c lines 18, 77-90, 112; unit test mode g2t line 305).
  Missing piece is a twist MODE, not the apparatus. Modes dispatch at line 327: l2, ms, msl, tmin, g2t.
- ~6 min is an anchor from a different workload, not a twist benchmark. Dense path (line 159, calloc(top+1,4)) needs
  26.1 GiB at 7e9 on a 16 GiB host -> MUST use the per-block traversal at line 240.
- 1e9 scout: rigorous tail 5548.43, heuristic only.
NEXT: implement + benchmark an isolated twist mode; validate blocks against direct Arb in the g2t pattern. Not launched.
