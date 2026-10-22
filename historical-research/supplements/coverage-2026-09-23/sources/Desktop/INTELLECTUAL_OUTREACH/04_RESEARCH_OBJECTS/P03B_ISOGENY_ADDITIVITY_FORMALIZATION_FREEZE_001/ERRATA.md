# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

An earlier crosswalk row transcribed the **base** curve's split `I₄` at 2 and nonsplit `I₁` at
31 into a row about the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has
**nonsplit `I₄` at 2, split `I₁` at 31**. Tamagawa product `(2,1,2)` unaffected.

## E2 — wrapper stale metadata, seventh consecutive occurrence

Both returns ship a `MANIFEST.sha256` byte-identical to the handoff's, replaying **26/28** and
failing exactly the two files each run changed. Both `tree/receipts/` describe the **input**:
one `sorry`, the `declaration uses sorry` warning, `sorryAx` on the target.

Not a proof defect. Both rebuild clean here with zero `sorry` and standard axioms, and all ten
inherited Lean sources came back byte-identical in both.

Both trees preserved exactly as delivered, each with a `STALE_METADATA_NOTICE.md`. This
object's root `MANIFEST.sha256` and `receipts/` are canonical.

> **Never certify an Aristotle return from its own receipts.** The returned source is the
> object to audit; build, axiom, source-scan, manifest and deterministic-archive evidence is
> always regenerated externally. Count declarations from source, never from a run's prose.

Failure modes seen so far: stale metadata (Delta A, Delta B, P01 A, P01 B, P03a B, P03b A,
P03b B) and a partial wrapper (P03a A).

## E3 — no new prose miscount found

Unlike P01 and P03a, neither P03b summary's lemma count was checked against prose here,
because the freeze does not rely on any: all counts in this object are taken mechanically from
source (`receipts/TARGET_STATEMENT_COMPARISON.txt`, Run A **12** added, Run B **17** added).
Recorded so the absence of an E3 entry is not read as an absence of checking.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.
Cross-referenced: this object's root manifest excludes only itself, so all three nested
manifests are covered as ordinary entries.

## Not an erratum: the convergent scaled-map reduction

Both runs independently reduced to a single scaled coordinate map with `c = 1` for `φ` and
`c = 2` for `φ̂`. The handoff did **not** suggest this. It is a genuine convergent finding, not
a supplied step, and it is recorded in `AB_ARCHITECTURE_COMPARISON.md` §4 and
`CONTINUATION_BASE_ASSESSMENT.md` so it is carried into P03d rather than rediscovered.
