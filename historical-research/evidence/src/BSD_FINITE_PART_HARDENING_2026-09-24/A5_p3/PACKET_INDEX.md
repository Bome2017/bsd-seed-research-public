# Aristotle A5 packet: Sha[3^∞] ≅ (ℤ/3)², 2026-09-24

| | |
|---|---|
| archive | `package/ARISTOTLE_A5_SHA3_v2_2026-09-24.tar.gz` (**v2; the only version to submit**) |
| sha256 | `cb374846b3e7aee1b1405757d41aa26c8797e6ece88f41d5185add25c11f379d` |
| bytes | 34364 |
| files | 33 plus `MANIFEST.sha256`; manifest 33/33 and frozen 6/6 on a fresh unpack |
| environment | Lean `v4.28.0`, Mathlib `v4.28.0` (`8f9d9cff…`), the same pins as A4 and the 09-19/09-22 Aristotle returns |
| working copy | `package/ARISTOTLE_A5_SHA3/` (the same bytes) |
| erratum | `ERRATUM_v2_2026-09-25.md`: one stale authority heading in `MATHEMATICAL_SPEC.md` (audit T1-F1). The archive is unchanged |

## What it asks

Replace 23 `sorry`s:
- **15 CORE:**
  - the `p = 3` criterion M1–M5;
  - the Cassels–Tate order-9 lemma M6;
  - eight finite certificate targets: point count, `a₃ = −1`, non-split, multiplicative `I₂`, `a_{4,·} = (0, −54, 15480)`,
    `v₃ = 2`, the recorded weights, and the folded sum;
  - the headline `ShaThreePrimary`: finite, order 9, `≅ (ℤ/3)²`, conditional on the inputs.
- **7 FULL:** non-vacuity, Teichmüller lift, reindexing, plus-symmetry, the `U₃` relation between the two independent
  certified tables, depth three, and the normalisation control.
- **1 STRETCH:** the general Cassels–Tate square-order lemma.

Every imported theorem is a field of `ThreeInputs`, in the paper's governing order of inference (v0.2.2, Theorem
`thm:sha3`; claim S.3):
- Skinner 2016 Thm A (the SU Euler-removal provenance limit is recorded);
- `ord_T f ≥ 2` and control finiteness, **first**;
- the independent height certificate (nondegeneracy; `Reg_γ` a unit);
- Jones 1989 Thm 3.1, forward direction only;
- SW Prop. 3.5, mod 27;
- the Cassels–Tate pairing.

No equality clause at a multiplicative prime is assumed.

The certified symbol tables (`m = 81`, `m = 27`) and the recorded weight table are sha-bound data.

## Already checked by the custodian (see `PREPACKAGE_AUDIT.md`)

- Every statement is true on the data (Python, exact), and all sources verify against `P3_MANIFEST.sha256`.
- The package compiles against the pinned Mathlib, from a fresh unpack, with zero diagnostics besides the 23 `sorry`
  warnings.
- 14 decidable targets close by `decide +kernel` (9.6 s) using only the standard axioms.
- The reductions `M1–M4 ⇒ M5` and `M5 + M6 ⇒ headline` compile using only the standard axioms (`provenance/Wiring_*.lean`).

Genuinely open for the prover: M1–M4, M6, F1 and S1.

## Scope

This is proof-engineering hardening of the `p = 3` step (paper Theorem `thm:sha3`; claim S.3), the same pipeline as A4.
It proves nothing about FIN, the global `#Sha(E/ℚ)`, or any other prime. The imported theorems keep their recorded
provenance limit (the SU Euler-removal interface), and no novelty is claimed.

Not submitted by the custodian. The user submits.

## Revision history

- **v1** (`ec25947f…`, 32,208 bytes). Withdrawn before any submission. It is kept, for the record only, in
  `superseded/SUPERSEDED_v1_ARISTOTLE_A5_SHA3_2026-09-24.tar.gz`.
  - Its `equalityClause` field followed the older `SHA3_THEOREM.md` wording (the SW Thm 6.1 equality clause at a
    multiplicative prime), which the paper states the governing argument does not use.
- **v2** (`cb374846…`). Replaces that field by `controlFiniteness` and `heightCert`, updates the citations, and passed
  every check again from a fresh unpack. See `PREPACKAGE_AUDIT.md` §5.
