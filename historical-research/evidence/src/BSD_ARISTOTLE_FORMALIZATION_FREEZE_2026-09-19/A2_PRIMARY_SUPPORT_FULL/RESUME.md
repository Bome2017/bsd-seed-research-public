# RESUME — A2_PRIMARY_SUPPORT_FULL (successor freeze)

## Status
DONE.
- Primary support, content and assembly are LEAN MACHINE-CHECKED, at level A2_FULL, with 3/3 stretch targets.
- FIN and FORMULA are UNCHANGED.
- #Sha = 9t² is checked only as the abstract `order_nine_t_sq` under its exact hypotheses.

## Verify
```bash
cd ~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A2_PRIMARY_SUPPORT_FULL && shasum -a 256 -c MANIFEST.sha256
```

## Rebuild offline
Do this in a scratch copy, because building writes `.lake/`, `build.log` and `axioms.log`.
```bash
cd source/ARISTOTLE_A2_PRIMARY_SUPPORT_2026-09-19_aristotle/pkg/A2_PRIMARY_SUPPORT
mkdir -p .lake && cp -cR ~/run013-family-minimisation-successor-2026-09-10/.lake/packages .lake/packages
bash scripts/acceptance.sh          # expected: LEVEL: A2_FULL, FIRST_NOT_CLEAN_TARGET: None, 3 stretch clean
lake env lean ../../../../audit/TypeIntegrity.lean
```

## Do not
- Do not re-prove the primary-support assembly unless a defect in the frozen Lean proof is found (handoff DO_NOT_RESURRECT).
- Do not read H2 as #Sha = 9, and do not read J2/L7 as J_E ≠ 0.
- Do not rely on the stale `source/.../MANIFEST.sha256`.
