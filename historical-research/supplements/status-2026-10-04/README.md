# Research status supplement — October 4, 2026

This documentation supplement is based on the frozen v0.2.6 tree. The 89 release claims, their grades, evidence and paper are unchanged. The original release README is preserved in base/README.md; its old “unreleased” wording describes its banking stage.

Read [CURRENT.md](CURRENT.md) for endpoint accounting and correction precedence. These records are separately graded; none is silently promoted into the release claim ledger.

| Record | Grade/scope | Source documents |
|---|---|---|
| two-prime-scalar | Reviewed at retained/imported-theorem grade; scalar not independently controlled | [REPORT.md](records/two-prime-scalar/REPORT.md), [AUDIT.md](records/two-prime-scalar/AUDIT.md), [NORMALIZATION_CHECK.md](records/two-prime-scalar/NORMALIZATION_CHECK.md) |
| weight-three-index | Reviewed at retained/imported-theorem grade; ordinary domain only; bound on b open | [REPORT.md](records/weight-three-index/REPORT.md), [VERIFIED_DERIVATION.md](records/weight-three-index/VERIFIED_DERIVATION.md) |
| weight-three-pairing | Confirmed with corrections; mixed-height interpretation not established | [REPORT.md](records/weight-three-pairing/REPORT.md), [CORRECTIONS.md](records/weight-three-pairing/CORRECTIONS.md), [DERIVATION.md](records/weight-three-pairing/DERIVATION.md) |
| receiver-exactness | Local exactness confirmed at retained-input grade; no upper bound | [REPORT.md](records/receiver-exactness/REPORT.md), [REVIEW.md](records/receiver-exactness/REVIEW.md), [LOCAL_EXACTNESS.md](records/receiver-exactness/input/BSD_SECOND_TORSION_LOCAL_EXACTNESS_PUSH_2026-10-03/LOCAL_EXACTNESS.md) |
| receiver-pairings | Pairing audit confirmed at retained-input grade; no new bound | [REPORT.md](records/receiver-pairings/REPORT.md), [REVIEW.md](records/receiver-pairings/REVIEW.md), [AMBIENT_LIFT_SCREEN.md](records/receiver-pairings/AMBIENT_LIFT_SCREEN.md), [BOUND_ATTEMPT.md](records/receiver-pairings/BOUND_ATTEMPT.md) |
| receiver-relations | Arithmetic generation/relations review; no sufficient relation-rank estimate | [REPORT.md](records/receiver-relations/REPORT.md) |
| product-relations | Scoped review; tested failures are not a universal exclusion | [REPORT.md](records/product-relations/REPORT.md) |
| additive-support | Support and actual-coefficient distinctions retained | [REPORT.md](records/additive-support/REPORT.md) |
| uniform-findings-repair | Specific corrections supersede blanket architectural closures | [REPORT.md](records/uniform-findings-repair/REPORT.md), [AUDIT.md](records/uniform-findings-repair/AUDIT.md) |
| rs2-and-compendium | Analytic derivation and scoped reconciliation; arithmetic height comparison open | [REPORT.md](records/rs2-and-compendium/REPORT.md), [COMBINATION_CHECK.md](records/rs2-and-compendium/COMBINATION_CHECK.md), [READ_LOG.md](records/rs2-and-compendium/coverage/READ_LOG.md), [RS2_INDEPENDENT_REVIEW.md](records/rs2-and-compendium/sources/RS2_INDEPENDENT_REVIEW.md) |
| packet-transfer | Written derivations awaiting independent review; no admissible witness realization | [REPORT.md](records/packet-transfer/REPORT.md), [CONSTRUCTION.md](records/packet-transfer/CONSTRUCTION.md), [SOURCES.md](records/packet-transfer/SOURCES.md) |
| closed-lift | Written derivation awaiting independent review; no Sha consequence established | [REPORT.md](records/closed-lift/REPORT.md), [PROOF.md](records/closed-lift/PROOF.md), [SOURCES.md](records/closed-lift/SOURCES.md) |
| uniform-refocus | Historical strategic review; fixed-prime work is not a uniform theorem | [REPORT.md](records/uniform-refocus/REPORT.md) |
| p53-preflight | Frozen preflight; not a new primary certificate | [PREFLIGHT_RETURN.md](records/p53-preflight/PREFLIGHT_RETURN.md), [STATE.json](records/p53-preflight/STATE.json) |

## Full record and integrity

The complete captured experimental delta is in [the lab checkpoint](https://github.com/Bome2017/bsd-seed-lab/tree/3606917c4fad2c6cc277325cabe51d0b9183e0ab/work/state-sync-2026-10-04), pinned at `3606917c4fad2c6cc277325cabe51d0b9183e0ab`. It includes the compendium, controls, original returns and context omitted from this shorter research supplement.

Source documents here are byte-for-byte copies. Historical absolute paths and links retain their original form; SOURCE_BINDINGS.json supplies each file's immutable lab path. Some individual source documents refer to other files in their full lab dossier. They are not represented here as independently replayable miniature bundles.

Use Python 3.10 or newer:

```bash
python3 supplements/status-2026-10-04/verify_update.py --with-release-checks
```

The verifier checks every frozen base file (restoring the original README only in a temporary tree), the supplement manifest, source copies and allowed file set. With the option above it runs the existing release and transition checkers on that exact frozen tree. This avoids rewriting historical manifests to make a documentation update resemble a new mathematical release.

The historical verifier commands in the preserved README target the frozen release. Use this wrapper on the supplemented branch. No fresh large arithmetic or Lean replay, human review, or novelty certification is claimed.

[Verification receipt](VERIFICATION.json): the exact reconstructed release passes its transition check and all 18 release checks. No new theorem certification is implied.
