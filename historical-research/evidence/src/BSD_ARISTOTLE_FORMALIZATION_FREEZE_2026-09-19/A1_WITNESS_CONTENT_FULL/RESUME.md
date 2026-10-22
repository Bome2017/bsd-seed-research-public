# RESUME — A1_WITNESS_CONTENT_FULL (successor freeze)

## Status
DONE — `A1_FREEZE_PASS_WITH_CUSTODY_REPAIR`.
- The WC finite algebra is MACHINE-CHECKED.
- STATUS = CONDITIONAL, LEVEL = A1_FULL.
- The antecedent `A ≠ 0 ∧ A ∈ J_E` is NOT PROVED, and FIN is UNCHANGED.

## Verify
```bash
cd ~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A1_WITNESS_CONTENT_FULL && shasum -a 256 -c MANIFEST.sha256
```

## Rebuild offline
```bash
cd source/ARISTOTLE_A1_WITNESS_CONTENT_2026-09-19_aristotle/A1_WITNESS_CONTENT
mkdir -p .lake && cp -cR ~/run013-family-minimisation-successor-2026-09-10/.lake/packages .lake/packages
bash scripts/acceptance.sh          # expected: LEVEL: A1_FULL, FIRST_NOT_CLEAN_TARGET: None
lake env lean ../../../audit/TypeIntegrity.lean
```
Run the rebuild in a scratch copy: building writes `.lake/`, `build.log` and `axioms.log` into the tree.

## Do not
- Do not reprove the finite algebra (handoff DO_NOT_RESURRECT row 41).
- Do not read this as FIN, J_E ≠ 0, or uniform prime support.
- Do not rely on the stale `source/.../MANIFEST.sha256`; this directory's MANIFEST is authoritative.
