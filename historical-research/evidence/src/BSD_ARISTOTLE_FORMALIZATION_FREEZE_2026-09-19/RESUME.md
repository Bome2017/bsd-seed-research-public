# RESUME — BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19 (canonical freeze root)

## Status
DONE — `A1_A2_FREEZE_PASS_WITH_CUSTODY_REPAIR`.
- A1: CONDITIONAL WC FINITE ALGEBRA = LEAN MACHINE-CHECKED, at A1_FULL.
- A2: PRIMARY SUPPORT / CONTENT / ASSEMBLY = LEAN MACHINE-CHECKED, at A2_FULL.
- FIN and FORMULA are UNCHANGED. What is NOT proved is listed in `FORMALIZATION_BOUNDARY.md`.

## Verify
```bash
cd ~/BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19 && shasum -a 256 -c MANIFEST.sha256
shasum -a 256 A1_WITNESS_CONTENT_FULL_FREEZE_2026-09-19.tar.gz A2_PRIMARY_SUPPORT_FULL_FREEZE_2026-09-19.tar.gz
```
Expected hashes:
- A1: `baa0435220954626b3f14a82fb874062d44267447ff1400748175ea55b276de0`
- A2: `fd55eab35ef1e51e5caaadc729f2f99d986e6158b2f4ca54d0b31d224f5d541c`

Rebuild recipes are in each freeze's `RESUME.md`.

## Rules
- Do not re-prove the conditional WC algebra or the primary-support assembly unless a defect in the frozen Lean proof is found
  (handoff DO_NOT_RESURRECT row 42).
- Any FIN-compression proposal must pass the Albertson coverage gate (DO_NOT_RESURRECT row 43).
- Never read these freezes as FIN, #Sha = 9, J_E ≠ 0, FORMULA or BSD.
