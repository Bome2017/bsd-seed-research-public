# Aristotle A4 packet: FIN finite-part verification, 2026-09-24

| | |
|---|---|
| archive | `ARISTOTLE_A4_FINITE_PART_2026-09-24.tar.gz` |
| sha256 | `3f809e8478059d5a89f8e69a3354d4dadf4ca815ad47640d19557abbf0c7fbd3` |
| bytes | 37336 |
| files | 30 plus `MANIFEST.sha256`; manifest 30/30, frozen 6/6, and the file set is exact on a fresh unpack |
| environment | Lean `v4.28.0`, Mathlib `v4.28.0` (`8f9d9cff…`), the same pins as the 09-19/09-22 Aristotle returns |
| working copy | `package/ARISTOTLE_A4_FINITE_PART/` (the same bytes) |

## What it asks

Replace 39 `sorry`s:
- **30 CORE:** the fixed-prime criterion M1–M6, plus six per-prime families at p = 5, 7, 11, 13;
- **7 FULL:** the polynomial link, non-vacuity, the ε-unit lemma, square valuation, squareclass, Néron multipliers,
  and the α⁻² regression;
- **2 STRETCH:** the general folding theorem and the local Gauss sum (Eichler case).

Every imported theorem is a field of `FixedPrimeInputs`: Kato divisibility, SW Thm 6.1, SW Prop. 3.5 and σ-height
integrality. The certified symbol tables are sha-bound data.

## Already checked by the custodian (see `PREPACKAGE_AUDIT.md`)

- Every statement is true on the data (Python, exact).
- The package compiles against the pinned Mathlib, from a fresh unpack.
- 22 decidable finite targets close by `decide +kernel` using only the standard axioms. So the certificate
  arithmetic for p = 5, 7, 11, 13 is already kernel-checked.

## Scope

This is proof-engineering hardening of FIN's finite part (p ≤ 13), in the same spirit as A1/A2. It proves nothing about
FIN, `#Sha = 9`, the primes ≥ 17 or the bad primes, and it makes no novelty claim.

Not submitted by the custodian. The user submits.
