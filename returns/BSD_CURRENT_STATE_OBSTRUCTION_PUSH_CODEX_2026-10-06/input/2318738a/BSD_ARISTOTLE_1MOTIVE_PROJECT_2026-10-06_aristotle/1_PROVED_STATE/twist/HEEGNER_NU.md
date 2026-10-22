# Heegner lane: what `ν_p ≤ 2` means, and the `p = 53, ℓ = 3391` arithmetic

Verdict: **NU_LE_TWO_RESTATES_SELMER.** If you take Zhang's Lemma 8.4 as an input (root number
`ε(E/ℚ) = +1`, `K = ℚ(√-23)`), the condition `ν_p ≤ 2` is *exactly* a Selmer bound on both
eigenspaces. Under one more condition on the twist, which can be checked for a single fixed curve,
it is equivalent for all but finitely many `p` to `Ш(E/ℚ)[p] = 0`. So a uniform `ν_p ≤ 2` theorem
is the ordinary half of FIN, stated in different words. It is not a new bound. This verdict covers
only the target `ν_p ≤ 2`. Nothing is claimed about methods that would bound `ν_p` by some route
other than Selmer dimensions.

## 1. Bookkeeping, checked in Lean (`Coinvariant/KolyvaginOrder.lean`)

Notation: `s⁺ = dim Sel_p(E/K)⁺ = dim Sel_p(E/ℚ) = 2 + dim Ш(E/ℚ)[p]` and
`s⁻ = dim Sel_p(E/K)⁻ = dim Sel_p(E^K/ℚ)`, where `E^K` is the twist by `-23`.
Lemma 8.4 (hypothesis `ZhangLemma84`) says: for odd `ν`, `s⁺ = ν+1` and `s⁻ ≤ ν`; for even `ν`,
`s⁻ = ν+1` and `s⁺ ≤ ν`.

| Lean theorem | Statement |
|---|---|
| `nu_eq_max_sub_one` | `ν = max(s⁺, s⁻) − 1`, so the Selmer dimensions determine `ν` |
| `one_le_nu` | `ν = 0` cannot happen, because the two rational points give `s⁺ ≥ 2` |
| `sha_eq_zero_of_nu_le_two` | your criterion: `ν ≤ 2 ⇒ Ш(E/ℚ)[p] = 0` (confirmed; it uses the sign in Lemma 8.4, not Selmer parity) |
| `nu_le_two_iff` | **`ν ≤ 2 ⇔ Ш(E/ℚ)[p] = 0 ∧ dim Sel_p(E^K/ℚ) ≤ 3`** |
| `sm_eq_three_of_nu_eq_two` | `ν = 2` can only happen when `dim Sel_p(E^K/ℚ) = 3` |
| `nu_le_two_iff_sha_of_twist` | if `dim Sel_p(E^K/ℚ) ≤ 1`: `ν ≤ 2 ⇔ ν = 1 ⇔ Ш(E/ℚ)[p] = 0` |
| `cofinite_nu_iff_cofinite_sha` | on any set of primes where the twist side is minimal, `{p : ν_p > 2} = {p : Ш(E/ℚ)[p] ≠ 0}` |

All of these build with no `sorry` and use only the standard axioms.

**Effect on point 3 of your note (the `ν = 2` relaxation).** The relaxation is logically correct.
But `ν = 2` forces `dim Sel_p(E^K/ℚ) = 3`. Suppose `E^K(ℚ)` has rank 1 and `Ш(E^K/ℚ)` is finite.
Gross–Zagier–Kolyvagin gives both when `ord_{s=1} L(E^K,s) = 1`; this is a single computation for
one fixed curve, and it was **not** done here. Then `s⁻ = 1` for all but finitely many `p`. On that
cofinite set `ν_p = 2` never happens, the first nonzero class must have one prime factor, and a
two-prime derived-class determinant has nothing to detect. So on the tail you care about,
`ν_p ≤ 2` is the same as `ν_p = 1`, which is the same as `Ш(E/ℚ)[p] = 0`. So a cofinite
`ν_p ≤ 2` theorem *is* cofinite `Ш[p] = 0`. (This is a statement about the target `ν_p ≤ 2` only.
It does not say that no easier intermediate object exists; see `FRONTIER.md`.)

The Lemma 8.4 bookkeeping cannot produce a cofinite estimate. The places such an estimate could
come from are the ones your note lists: a fixed-content special-value or Jochnowitz formula
whose `p`-adic valuation is controlled uniformly. None was found or tested here.

## 2. `p = 53`, `ℓ = 3391`, checked in Lean (`Coinvariant/KolyvaginPrime3391.lean`)

These are computed on the project's own minimal model `Seed.curve`. `seed_equation_iff` shows the
point count is the count for that equation.

* `affine_count_3391`: there are exactly 3391 affine points over `𝔽_3391`. So
  `#E(𝔽_3391) = 3392` and **`a_3391 = 0`** (`a_3391_eq_zero`). So 3391 is in fact a
  supersingular prime.
* `three_three_nine_one_inert`: `(−23 / 3391) = −1`, so 3391 is inert in `K`.
* `fifty_three_dvd`: `53 ∣ 3392`.
* `ap_53`: `a_53 = −6`, so 53 is ordinary.

So 3391 is a Kolyvagin prime for `p = 53`. If Lemma 8.4 applies (that is, Zhang's Hypothesis ♥ at
53, with your observation that `N⁻ = 1` and that `H¹(ℚ_ℓ, E[53]) = 0` at 2 and 4547 by Lemma 5.1(2)),
then `c(3391) ≠ 0` gives `ν_53 ≤ 1`, which gives `Ш(E/ℚ)[53] = 0` by `sha_eq_zero_of_nu_le_two`.
**Whether `c(3391) ≠ 0 mod 53` is still unknown.** Nothing here computes a derived Heegner class.
The Hypothesis ♥ inputs (full image, ramification at 3, 2243 and 5843) are your retained inputs and
were not re-derived. The Lean statement does not use Selmer parity, but it does need Zhang's sign
convention `ε_ν = ε(E/ℚ)(−1)^{ν+1}` to be applied with `ε(E/ℚ) = +1`, the global root number of the
seed.

## 3. W3 / `arbcore msl` at `m = 289`

This project does not contain the `arbcore msl` evaluator or the `corpus-ext-6445` coefficient
corpus, so the seed calibration `[a/289]⁺ → ℓ₂ mod 17` **was not run**. Nothing here bears on it.
It still has to be run on the infrastructure where `msl` lives.
