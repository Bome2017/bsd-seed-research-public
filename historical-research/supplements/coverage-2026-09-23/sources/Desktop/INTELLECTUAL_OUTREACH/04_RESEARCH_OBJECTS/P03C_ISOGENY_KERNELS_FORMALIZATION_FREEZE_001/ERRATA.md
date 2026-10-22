# Errata

## E1 — CASE_CROSSWALK row 45 (carried forward, Claude's error, 2026-09)

The **base** curve's split `I₄` at 2 and nonsplit `I₁` at 31 were transcribed into a row about
the **twist**. `BSD_CHAIN.md` §4 is authoritative: the twist has nonsplit `I₄` at 2, split
`I₁` at 31. Tamagawa product `(2,1,2)` unaffected.

## E2 — wrapper stale metadata, ninth consecutive occurrence

Both returns ship the handoff's `MANIFEST.sha256`, replaying **27/29** and failing exactly the
two files each changed; both `tree/receipts/` describe the input. Not a proof defect — both
rebuild clean here with zero `sorry` and standard axioms, and all eleven inherited Lean
sources came back byte-identical in both.

Failure modes seen: stale metadata (Delta A/B, P01 A/B, P03a B, P03b A/B, P03c A/B) and a
partial wrapper (P03a A).

> **Never certify an Aristotle return from its own receipts.** Regenerate build, axiom,
> source-scan, manifest and archive evidence externally; count declarations from source.

## E3 — a process finding, not a defect: P03c's replication is confirmation-grade

Recorded here so it is impossible to overlook. The two returns added **zero** auxiliary
lemmas and their proofs differ in **two substantive lines**. Measurement:
`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt`. Discussion: `STATUS.md`.

The cause is the handoff's own `TASK.md`, which supplied the complete three-case route. That
was the right call for getting P03c closed quickly, and it is the intended payoff of the
earlier staging — but it means the second run contributes much less independent evidence than
at saturation or P03b.

**Standing consequence for later stages.** Before sending a short, tightly-specified target
to two accounts, decide which is wanted:

- *confirmation* — supply the route, expect near-identical returns, and label the result
  confirmation-grade, as here; or
- *independent cross-check* — state the target and the boundary but withhold the route, as
  the saturation and P03b handoffs effectively did.

Both are legitimate. What is not legitimate is supplying the route and then describing the
result as if it were an architectural cross-check.

## E4 — saturation Freeze 001's root manifest omits its nested manifests (Claude's error)

Recorded in full in `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md` E3.
This object's root manifest excludes only itself, so all three nested manifests are covered.
