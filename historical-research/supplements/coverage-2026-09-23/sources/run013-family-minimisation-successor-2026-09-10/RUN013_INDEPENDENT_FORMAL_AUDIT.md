# Run013 independent formal-audit result

Date: 2026-08-23

This is the durable report of the completed independent hostile audit. It does
not reinterpret the original artifact's manifest failure as a pass.

## Artifact and audit roots

```text
ORIGINAL_ARISTOTLE_ARCHIVE =
/Users/bsm/Downloads/32315cd1-6782-4568-84f0-08b5f6bd1071-aristotle.tar.gz

ORIGINAL_ARISTOTLE_ARCHIVE_SHA256 =
5b50f776c6c0bfbd2088fbfaa40bf69f537bcdfcf13da54269d33909f5b8d419

AUDITED_IMMUTABLE_EXTRACTION =
/private/tmp/run013-hostile-audit.L0o1WE/immutable/run013-aristotle-handoff-2026-08-22_aristotle

INDEPENDENT_CLEAN_BUILD_TREE =
/private/tmp/run013-hostile-audit.L0o1WE/build/run013-aristotle-handoff-2026-08-22_aristotle
```

## Provenance result

The original archive identity passed. Its embedded
`PROJECT_MANIFEST.sha256` had SHA-256
`60c6e5ddef0902b715ed2a361818e18b53879a733c2a35af90b27de3bbb08f51`,
but strict replay was 24/26 and failed: the listed `.gitignore` was absent and
the untouched `lake-manifest.json` had SHA-256
`116c6ef00aa899fb38c08c5e4c92c0e434d0e7f9d574fcb5d4d42cc90ffb07cb`
rather than the stale listed digest
`84965c68cec2c5a17f6b17216a7018b1ff71ead889c9dcf0883668f5dcd1bb31`.

Accordingly, the completed audit verdict was:

```text
ORIGINAL_ARTIFACT_IDENTITY = PASS
CONTENT_ADDRESSED_PROJECT_IDENTITY = FAIL
RUN013_FORMAL_GATE = FAIL_PACKAGING_ONLY
FORMALIZATION_FATAL_ERROR = NO
```

## Independent rebuild and trust result

The audit used a clean writable extraction with no reused `.lake`, `.olean`, or
other build products.

```text
Lean = v4.28.0
mathlib = 8f9d9cff6bd728b17a24e163c9402775d9e6a365
lake build = 8052/8052 jobs, exit 0
fresh Audit.lean axiom harness = exit 0, 35 declarations
fresh LocalTwo.lean re-elaboration = exit 0
kernel decide = PASS
SORRY_COUNT = 0
ADMIT_COUNT = 0
CUSTOM_AXIOMS = none
ALLOWED_STANDARD_AXIOMS = propext; Classical.choice; Quot.sound
```

No theorem source invoked `unsafe`, `native_decide`, `Lean.ofReduceBool`,
`implemented_by`, an external process, an assumed certificate, or an untrusted
checker result.

## Substantive result

```text
SELMER_OBJECT_CLASSIFICATION =
STANDARD_EXPLICIT_SELMER_REALIZATION_FORMALIZED

F62_FIDELITY = PASS
CURVE_MODEL_FIDELITY = PASS
ISOGENY_ORIENTATION = PASS
SELMER_SEMANTIC_FIDELITY = PASS
COVERING_KUMMER_BRIDGE = PASS
PADIC_NORMALIZATION = PASS
SUPPORT_REDUCTION = PASS
PHI_LOCAL_TWO = PASS
PHI_REVERSE_INCLUSION = PASS
DUAL_INFINITY = PASS
DUAL_LOCAL_Q = PASS
LOCAL_31 = PASS
PRIMARY_PHI_SELMER = PASS
PRIMARY_DUAL_PHI_SELMER = PASS
NO_HIDDEN_Q_BOUND = PASS
FOUR_CLASS_DISTINCTNESS = PASS

LEVEL_A = PASS
LEVEL_B_CANONICAL_STATUS = CONDITIONAL_FORMAL_PASS
LEVEL_C = PARTIAL
LEVEL_D = EXTERNAL_DEPENDENCIES_RECORDED
```

The isogeny composition theorem proves generic affine x-coordinate
compatibility only, not a full isogeny-morphism equality. No H1 Selmer object,
actual `Sel_2(E)`, or actual Sha object is formalized. The Level C component,
torsion, differential, Tamagawa, and analytic statements retain their documented
partial or conditional scope.

The sole blocking result was the original archive's outer packaging manifest.
