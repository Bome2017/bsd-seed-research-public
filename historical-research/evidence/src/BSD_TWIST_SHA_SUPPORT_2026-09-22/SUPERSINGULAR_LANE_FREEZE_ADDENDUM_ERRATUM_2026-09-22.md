# Erratum to SUPERSINGULAR_LANE_FREEZE_ADDENDUM_2026-09-22.md (two wording corrections)

Filed 2026-09-22 as a separate file. The addendum itself is left byte-identical (sha `13736ff7…`, pinned in
`~/BSD_A3_LEAN_CORE_2026-09-22/MANIFEST.sha256`). Neither correction changes the promoted statement.

1. **`M_2(p) ≠ 0` is a sufficient route, not an obligation.** Where the addendum lists "the uniform nonvanishing
   `M_2(p) ≠ 0`" among the remaining gaps, read it this way: the obligation is `Sha(E/Q)[p^∞] = 0` at the good primes.
   `M_2(p) ≠ 0` is one sufficient witness for it. If `M_2(p) = 0` at some prime, that refutes nothing, and the primary
   vanishing may still be proved another way.

2. **"UNCOVERED" at 2243, 4547, 5843 means "not covered by the good-prime forward bridge."** It does not mean that no
   route exists. The retained prime ledger (`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md` l.167–168,
   `FIN_FRONTIER.md` §4) records:
   * 2243 (split) and 5843 (non-split): a semistable fixed-prime route, with no completed certificates. The split
     case also needs its stated nonzero L-invariant input.
   * 4547 (additive, type III): a witness semi-decision whose additive-prime control theorem is missing.

   The feasibility of the multiplicative routes is being checked in `~/BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/`.
