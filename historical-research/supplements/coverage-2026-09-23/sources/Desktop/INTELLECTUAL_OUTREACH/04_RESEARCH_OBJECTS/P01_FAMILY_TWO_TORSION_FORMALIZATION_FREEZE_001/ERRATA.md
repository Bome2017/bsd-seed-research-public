# Errata

Recorded, never silently repaired.

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁`
at 31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected; no downstream
conclusion changes. Carried unedited in every packet since.

## E2 — the Aristotle wrapper ships input metadata as output metadata (now systematic)

This is the **fourth and fifth** consecutive occurrence: Delta Run A, Delta Run B, P01 Run A,
P01 Run B.

Both P01 returns ship a `MANIFEST.sha256` byte-identical to the handoff's
(`379d32f559df363c61209819297f5e3db473268c3ca0f36f0f9dfe5428f91dd6`). Replayed against the
tree each accompanies, each fails on the two files its run changed:

    README.md:                            FAILED
    RequestProject/P01/TwoTorsion.lean:   FAILED
    21/23 OK

Both trees' `receipts/` are the handoff's: `build.txt` still carries the
`declaration uses sorry` warning, `nontautology_and_axioms.txt` still records `sorryAx` on
`p01_family_two_torsion`, `source_scan.txt` still reports one `sorry`, and `probe.lean` still
holds the handoff's deliberate `sorry`s.

**Assessment.** A custody/packaging defect in the wrapper, not a proof defect, and no longer
plausibly a one-off. Both runs' own `ARISTOTLE_SUMMARY.md` files are accurate and describe the
clean rebuild correctly; the wrapper simply does not regenerate `receipts/` or the manifest.

**Disposition.** Both trees preserved **exactly as delivered**, each with a
`STALE_METADATA_NOTICE.md`. This object's root `MANIFEST.sha256` and `receipts/` are
canonical, generated after independent rebuilds performed here.

**Standing rule, now confirmed five times:**

> **Never certify an Aristotle return from its own receipts.** Regenerate the source scan,
> axiom audit, build receipt, manifest and archive from the returned source before sealing.

## E3 — Run B's summary miscounts its own lemmas (upstream, cosmetic)

`02_run_B/tree/ARISTOTLE_SUMMARY.md` says it added "four proved auxiliary lemmas" and then
lists five: `Wab_negY_eq`, `Wab_two_torsion_iff`, `int_isSquare_of_rat_sq`,
`Ecurve_x_eq_zero`, `E'curve_x_cases`. The list has four bullets, but the last bullet names
two lemmas.

The mechanical count from the source is **5** added declarations, confirmed in
`receipts/RUN_B_INDEPENDENT_REBUILD.txt` (31 declarations, 26 shipped). No mathematical
significance, and no claim anywhere depends on the number. Uncorrected in the frozen summary.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.
Cross-referenced because the same filter question applies here: this object's root manifest
excludes only itself, so all three nested manifests (`00_v1_handoff/`, `01_run_A/tree/`,
`02_run_B/tree/`) are covered as ordinary entries. That is deliberate — the two stale return
manifests are the evidence for E2 and must be under integrity control.

## Not an erratum: the supplied route

The P01 handoff's `TASK.md` spelled out the intended route, including the full Legendre
obstruction chain. Both runs therefore converged on it. That is a property of the experiment
design, disclosed in `STATUS.md` and `AB_ARCHITECTURE_COMPARISON.md` §1, and recorded here
only so that nobody later reads it as something concealed.
