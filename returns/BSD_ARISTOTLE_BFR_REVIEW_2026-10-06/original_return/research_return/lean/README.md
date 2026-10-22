# Lean formalization

* Toolchain: `leanprover/lean4:v4.28.0` (`lean-toolchain`). Mathlib is pinned by
  `lake-manifest.json` (rev `v4.28.0` in `lakefile.toml`).
* Sources: `RequestProject/Seed/Curve.lean`, `AuxPoint.lean`, `Local4547.lean`,
  `BadPrimes.lean`. They are part of the default `RequestProject` target (glob
  `RequestProject.+`).
* Build: `lake build` (see `BUILD_TRANSCRIPT.txt`).
* Axioms: see `AXIOM_AUDIT.txt`. The only axioms are `propext`, `Classical.choice` and
  `Quot.sound`. There is no `sorry`, `admit`, new `axiom`, `@[implemented_by]` or
  `native_decide`. The 4547 certificate uses `decide +kernel`, which is plain kernel
  reduction and adds no trusted compiler.

## Principal declarations

| declaration | statement (informal) |
|---|---|
| `Seed.translate_curve_eq_orig` | the `u = 1` model change from the minimal model to the original model |
| `Seed.curve_Δ`, `Seed.curve_c₄`, `Seed.disc_factorization` | `Δ = 2⁸3²·2243·4547³·5843²`, `c₄ = 3169004368` |
| `Seed.P1_nonsingular`, `P2_nonsingular`, `T_addOrderOf` | the basis points are on the curve; `T` has order 2 |
| `Seed.Rp_nonsingular` | `R_p ∈ E(K)` whenever `s² = d_p` in a char-0 field `K` |
| `Seed.dp_neg`, `dp_not_sq`, `dp_modEq_one`, `dp_mul_p_not_sq` | `d_p < 0`; `d_p ≡ 1 (p²)`; `d_p·(±p)` is not a square |
| `Seed.exists_sqrt_dp_padic`, `Seed.Rp_padic` | for odd `p`: a unit square root exists, and `R_p ∈ E₁(ℚ_p) \ E₂(ℚ_p)` |
| `Seed.Rp_padic_2243/4547/5843` | specialisations at the bad primes |
| `Seed.Local.index_coprime`, `reduction_quotient_factorizations` | bad-prime index divisibilities |
| `Seed.Local.chainCert_true` | the 4547 certificate for `P2` |
| `Seed.card_affine_F5`, `five_not_dvd_disc` | `#E(𝔽₅) = 8`; good reduction at 5 |

## What these statements do and do not establish

The statements are concrete arithmetic facts about the actual curve. They are **not** a
formalization of Theorem BFR, Selmer groups, Sha, or BSD. The bridges to those objects
(Imp-1 to Imp-10 in `../ASSUMPTIONS.json`) are not formalized. In particular, no structure
with an abstract `Sha` field is introduced.
