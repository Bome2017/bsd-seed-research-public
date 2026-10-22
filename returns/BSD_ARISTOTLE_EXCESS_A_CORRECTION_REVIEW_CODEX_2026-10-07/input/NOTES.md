# NOTES (working log)
1. Ran prepare_reference.py: READING_SETS_VERIFIED, 6566 members hash-checked, 0 research files read by the script.
2. Read governing docs (SOURCES.md). Chose to test, in order: A1 (task-suggested higher Fitting),
   A2 (Kolyvagin nu), A3 (Kato + p-adic leading term).
3. Collision search (COLLISION_CHECK.md). A2 fully covered by HEEGNER_NU.md; A3 by d-infinity/HGZ2 and p-adic regulator rows.
4. Built A1 control map with H2 retained; found its T=0 generator is the classical one-prime class (PROOF.md); stopped A1.
5. No computation run; no Lean development (no new formal step; bookkeeping already kernel-checked in record).
6. (2026-10-07, second pass) The reviewer flagged two problems: (a) the Fitting-to-Heegner
   equivalence moves between Euler-system constructions without a comparison; (b) the "−23 never
   computed" statement contradicts the record. Both were confirmed. (a) Statement 4 of Prop. 1 is
   withdrawn, with comparisons C1–C4 recorded; A1 is no longer reduced to A2. (b) Searched the
   record. Found the 2026-09-21 Arb certificate and the 2026-10-06 float value. Ran the read-only
   checks/d23_trace_check.py: 17/1,070 certificate manifest entries are present and all match;
   tail bound and endpoints recheck exactly; root number −1; models isomorphic. The core sum
   cannot be replayed because its source, units and coefficients are absent.
