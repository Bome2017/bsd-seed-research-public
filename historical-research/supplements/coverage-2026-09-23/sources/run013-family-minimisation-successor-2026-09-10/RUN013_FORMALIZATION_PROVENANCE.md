# Run013 formalization provenance ledger

## Original Aristotle artifact

```text
ORIGINAL_ARISTOTLE_ARCHIVE =
/Users/bsm/Downloads/32315cd1-6782-4568-84f0-08b5f6bd1071-aristotle.tar.gz

ORIGINAL_ARISTOTLE_ARCHIVE_SHA256 =
5b50f776c6c0bfbd2088fbfaa40bf69f537bcdfcf13da54269d33909f5b8d419

ORIGINAL_STALE_MANIFEST_SHA256 =
60c6e5ddef0902b715ed2a361818e18b53879a733c2a35af90b27de3bbb08f51

ORIGINAL_MANIFEST_REPLAY =
24/26 FAIL

ORIGINAL_MANIFEST_DEFECTS =
.gitignore absent;
lake-manifest.json actual bytes do not match stale listed digest

ORIGINAL_LAKE_MANIFEST_EXPECTED_BY_STALE_MANIFEST =
84965c68cec2c5a17f6b17216a7018b1ff71ead889c9dcf0883668f5dcd1bb31

ORIGINAL_LAKE_MANIFEST_ACTUAL_SHA256 =
116c6ef00aa899fb38c08c5e4c92c0e434d0e7f9d574fcb5d4d42cc90ffb07cb
```

The original archive also contained `ARISTOTLE_SUMMARY.md` and `README.md`,
which were not listed by its stale manifest. They are preserved and enumerated
by the successor's active manifest. The original manifest itself is excluded
from the successor and replaced by `MANIFEST.sha256` under the convention in
`MANIFEST_POLICY.md`.

**THE DEFECT IS IN THE ORIGINAL ARCHIVE'S SELF-DESCRIPTION, NOT IN THE
FORMALIZED MATHEMATICS.**

```text
HISTORICAL_GIT_IDENTITY =
NOT_SUPPLIED

GIT_IDENTITY_REQUIRED =
NO

CONTENT_ADDRESSED_ORIGINAL_ARTIFACT =
PRESERVED

SUCCESSOR_PURPOSE =
PACKAGING / MANIFEST CORRECTION ONLY

THEOREM-BEARING SOURCE CHANGES =
NONE
```

## Handoff binding

```text
HANDOFF_ARCHIVE_SHA256 =
652944cf19010247368525f3a68c310c9abc7d3eb20df2a2509c291c5c5d410e

HANDOFF_MANIFEST_SHA256 =
39816c9244f00bdb124aeaf693e5e4772eab21018b5f4fe0af844eb47130c3e7

FROZEN_SOURCE_PROJECT_MANIFEST_SHA256 =
921fce81c78a3164431da6cf6eb618d37bb3d376108f733c534111726ee55d40

HANDOFF_BINDING =
PASS
```

## Independent formal-audit and clean-build binding

```text
AUDITED_IMMUTABLE_EXTRACTION =
/private/tmp/run013-hostile-audit.L0o1WE/immutable/run013-aristotle-handoff-2026-08-22_aristotle

INDEPENDENT_CLEAN_BUILD_TREE =
/private/tmp/run013-hostile-audit.L0o1WE/build/run013-aristotle-handoff-2026-08-22_aristotle

INDEPENDENT_FORMAL_AUDIT_REPORT =
RUN013_INDEPENDENT_FORMAL_AUDIT.md

INDEPENDENT_FORMAL_AUDIT_REPORT_SHA256 =
8ca73949f35e327bd0d1e98f449056a9392541a8d6131561cd477bcde8b45c29

ORIGINAL_ARISTOTLE_FORMALIZATION_REPORT_SHA256 =
b7519917de47babeabac6a429b278e390a9401466c212d5567bd826cf36d84d3

Lean =
v4.28.0

mathlib =
8f9d9cff6bd728b17a24e163c9402775d9e6a365

INDEPENDENT_CLEAN_BUILD =
8052/8052 jobs; exit 0

FRESH_AXIOM_HARNESS =
35 declarations; exit 0

FRESH_LOCALTWO_REELABORATION =
PASS; exit 0

BUILD_RELEVANT_BYTES =
UNCHANGED (0 differences among 22 files)

CLEAN_BUILD_EVIDENCE =
PRESERVED_FROM_INDEPENDENT_AUDIT
```

The 22-file build-relevant set comprises all 19 `.lean` files plus
`lakefile.toml`, `lean-toolchain`, and `lake-manifest.json`. The hashes are bound
in `RUN013_SOURCE_PRESERVATION_BASELINE.md`. Because all 22 files are identical
to the independently successful clean-build tree, the 8052-job build was not
rerun for this packaging-only successor.

## Canonical formal status

```text
SELMER_OBJECT_CLASSIFICATION =
STANDARD_EXPLICIT_SELMER_REALIZATION_FORMALIZED

LEVEL_A =
PASS

LEVEL_B_CANONICAL_STATUS =
CONDITIONAL_FORMAL_PASS

LEVEL_C =
PARTIAL

LEVEL_D =
EXTERNAL_DEPENDENCIES_RECORDED

FORMALIZATION_FATAL_ERROR =
NO
```
