# SEED SPECIALIZATION — every hypothesis of Theorem BFR on the actual curve

**Curve and model.** The minimal model is `y² = x³ − x² − 66020924x − 65074271436`, obtained
from the original model by the `u = 1` translation `x = X + 7578` [Lean:
`Seed.translate_curve_eq_orig`]. All local statements use this minimal model; the formal group
facts (Imp-5) require minimality at `p`. `Δ = 2⁸·3²·2243·4547³·5843²` [Lean], so the model is
minimal at 2243, 4547 and 5843 (`v_p(Δ) < 12`).

**Basis and lattice.** `P1 = (−3031, 327384)`, `P2 = (−2394, 281520)` and `T = (−7578, 0)` are
on the curve [Lean]. Saturation and index one come from release R.1 (imported). No rescaling
of points (such as `16P_i`) is used, so the determinant-scaling caveat of W05 does not arise.

| hypothesis | p = 2243 | p = 4547 | p = 5843 |
|---|---|---|---|
| p prime, p ≥ 5 | yes [Lean] | yes [Lean] | yes [Lean] |
| residual image `GL₂(𝔽_p)` | A.3 (imported, all odd p) | A.3 | A.3 |
| reduction type at p | `I₁` split [Chk-2; A.1] | `III`, cusp [Chk-2; A.1] | `I₂` non-split [Chk-2; A.1] |
| `c_p` | 1 (A.1) | 2 (A.1) | 2 (A.1) |
| `#Ẽ_ns(𝔽_p)` | 2242 [Chk-2] | 4547 [Chk-2] | 5844 [Chk-2] |
| `p ∤ [E(ℚ_p):E₁]` | yes [Lean `index_coprime`] | **no** (index `2·4547`) | yes [Lean] |
| `d_p ≡ 1 mod p²`, `√d_p ∈ ℤ_p^×` | [Lean] | [Lean] | [Lean] |
| `R_p ∈ E₁ \ E₂` | [Lean `Rp_padic_2243`] | [Lean `Rp_padic_4547`] | [Lean `Rp_padic_5843`] |
| local Kummer generator | `R_p` | `P2` [Lean `chainCert_true` + Imp-7] | `R_p` |
| `R_p` locally p-divisible? | no | **yes** (L(iii)) | no |
| `p ∤ c_q` for all `q ≠ p` | yes (all `c_q ∈ {1,2}`) | yes | yes |
| `F_p ∩ ℚ(E[p]) = ℚ` | [Lean `dp_mul_p_not_sq`] + A.3 | same | same |
| parity (for (b)) | retained (Imp-4) | retained | retained |

**Finite exceptions created.** None among `p ∈ {2243, 4547, 5843}`. The theorem is stated
only for these three primes. For good `p ≥ 5` the record's own forward proposition applies.

**Periods, Manin constant, L-values.** These are not used.

**Conditionality.** The theorem is unconditional relative to the imports Imp-1 to Imp-10.
Only part (b) uses parity (Imp-4). No FIN, BSD, ETNC or witness hypothesis is used. The
grades of A.1, A.3 and R.1 are the record's retained grades. They were not re-certified here,
except for the reduction-type re-checks in `checks/`.
