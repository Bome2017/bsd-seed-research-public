# ADDENDUM_002: scope correction to ADDENDUM_001 (2026-09-18)

This is an addendum. The frozen files and ADDENDUM_001 are unchanged. Its sha256 is PENDING, because the shell is blocked in the coordinator conversation; see ~/SEED_2243_12_MECHANISM_LANES_2026-09-18/HANDOFF_LANE1_NEXT.md, Step 1.

## Correction

ADDENDUM_001's sentence "only Reg₅ mod 5³ is model-independent" is proved and tested **only for model changes with u = 1**. That covers the translations x → x + r (together with s, t shifts), and those are the only changes its scripts tried. The seed model and its minimal model differ by exactly such a change: u = 1, r = 7578.

For changes with u ≠ 1, the Lane-2 session reports the following, which it verified and refereed. It is recorded here as reported and was not replayed locally.
- PARI 2.17.3 and 2.17.4 have an **additional scaling defect**. On a u = 7 model of the seed, PARI's leading term of Reg₅ is 4·5², not 5². The correct back-map is a = a′ − r·b′/u², b = b′/u².
- So PARI's p-adic height and regulator output on a u ≠ 1 model is unreliable even in its leading digit.
- The valuation is still 2 in that example.

## Why N5 is unaffected

- The certificate's N5 value was computed on the seed model, which is related to the minimal model by a u = 1 change.
- N5 uses only ord₅ Reg₅ = 2.
- For canonical heights, rescaling by u ∈ Z₅^× multiplies the pairing by a 5-adic unit. It cannot change the valuation.

## Canonical value (Lane 4 verification, pointer only)

The Lane-4 session's `~/BSD_SEED_2243_12_LANE4_AUDIT_FORMAL_2026-09-18/numerics/L4_reg5_NOTE.md` reports:
- Sage `padic_height` reproduces SW's 446d1 value, and gives the same Reg₅ on the original and minimal models: 5² + 3·5³ + 3·5⁴ + ….
- PARI agrees with that when run on `ellminimalmodel`.
- Canonical Reg_γ ≡ 21 (mod 25). The SW gate's raw-model digit, 6 (mod 25), is not canonical.

## Safe practice

- Run PARI p-adic heights only on `ellminimalmodel` output, mapping points with `ellchangepoint`, or cross-check with Sage.
- Never rescale (u ≠ 1) before calling PARI.
- Quote valuations, or digits verified canonical.
