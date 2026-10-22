module

public import Mathlib

/-!
# Rank-two anchor: formal supports for the obstruction (delta 2026-10-06)

Abstract lemmas behind the `PRECISE_OBSTRUCTION` return in
`BSD_ARISTOTLE_DELTA_RANK2_ANCHOR_2026-10-06/RESULT_RANK2_ANCHOR.md`.

Nothing here is a statement about the seed's L-function or its Tate–Shafarevich
group. Every arithmetic input (orders of vanishing, the shape of a Gross–Zagier type
identity, the action of `Gal(K/ℚ)`) appears as an explicit hypothesis. The lemmas
isolate the mechanism at each first failure:

* `ProductOrder.*`: if `F = G·H` with `ord G ≥ 2` and `ord H ≥ 1`, then `F`, `F'` and `F''`
  vanish at the point and `F''' = 3·G''·H'`. Read with `F = L(E/K,s)`, `G = L(E,s)`,
  `H = L(E^K,s)`: every identity that is linear in `L^(k)(E/K,1)` with `k ≤ 2` is `0 = 0`,
  and the first nonvanishing term is `3·L''(E,1)·L'(E^K,1)`.
* `degenerate_identity_iff`: a family of identities `c·Z t = B t` with a fixed factor
  `c = 0` holds or fails independently of `Z`; it carries no information about `Z` at any
  order in `t`.
* `equivariant_minus_to_plus_eq_zero`: with `2` invertible, an involution-equivariant
  linear map sends the `(−1)`-eigenspace to `0` in any module on which the involution
  acts trivially. Read with the involution generating `Gal(K/ℚ)`: a rank-one anchor for the
  twist `E^K` lives in the `(−1)`-part and cannot equivariantly produce a quantity in the
  `(+1)`-part, where `E`'s own tame coefficient lies.
* `seed_calibration`: arithmetic consistency of the calibration
  `4·c∞·Tam·#Ш/tors² = 8q` with the record's numbers.
-/

@[expose] public section

namespace Rank2Anchor

section ProductOrder

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜] {G H : 𝕜 → 𝕜} {x : 𝕜}

/-- Leibniz at order `n` for smooth `G`, `H`, written out. -/
lemma leibniz (n : ℕ) (hG : ContDiff 𝕜 ⊤ G) (hH : ContDiff 𝕜 ⊤ H) :
    iteratedDeriv n (G * H) x = ∑ i ∈ Finset.range (n + 1),
      (n.choose i : 𝕜) * iteratedDeriv i G x * iteratedDeriv (n - i) H x :=
  iteratedDeriv_mul (hG.contDiffAt.of_le (by exact_mod_cast le_top))
    (hH.contDiffAt.of_le (by exact_mod_cast le_top))

/-- If `G` vanishes to order `≥ 2` and `H` to order `≥ 1` at `x`, then `G·H` and its first
two derivatives vanish at `x`. -/
theorem ProductOrder.low_derivs_vanish (hG : ContDiff 𝕜 ⊤ G) (hH : ContDiff 𝕜 ⊤ H)
    (hG0 : iteratedDeriv 0 G x = 0) (hG1 : iteratedDeriv 1 G x = 0)
    (hH0 : iteratedDeriv 0 H x = 0) :
    iteratedDeriv 0 (G * H) x = 0 ∧ iteratedDeriv 1 (G * H) x = 0 ∧
      iteratedDeriv 2 (G * H) x = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [leibniz 0 hG hH]; simp [hG0]
  · rw [leibniz 1 hG hH]; simp [Finset.sum_range_succ, hG0, hG1, hH0]
  · rw [leibniz 2 hG hH]; simp [Finset.sum_range_succ, hG0, hG1, hH0]

/-- If `G` vanishes to order `≥ 2` and `H` to order `≥ 1` at `x`, then
`(G·H)'''(x) = 3·G''(x)·H'(x)`. -/
theorem ProductOrder.third_deriv (hG : ContDiff 𝕜 ⊤ G) (hH : ContDiff 𝕜 ⊤ H)
    (hG0 : iteratedDeriv 0 G x = 0) (hG1 : iteratedDeriv 1 G x = 0)
    (hH0 : iteratedDeriv 0 H x = 0) :
    iteratedDeriv 3 (G * H) x = 3 * iteratedDeriv 2 G x * iteratedDeriv 1 H x := by
  rw [leibniz 3 hG hH]
  simp [Finset.sum_range_succ, hG0, hG1, hH0, Nat.choose]

/-- A rank-one Gross–Zagier type identity `c · ĥ = F'(x)` (with `c ≠ 0`) applied to
`F = G·H` as above forces the height `ĥ` to vanish. -/
theorem ProductOrder.first_order_anchor_height_zero (hG : ContDiff 𝕜 ⊤ G)
    (hH : ContDiff 𝕜 ⊤ H) (hG0 : iteratedDeriv 0 G x = 0) (hG1 : iteratedDeriv 1 G x = 0)
    (hH0 : iteratedDeriv 0 H x = 0) {c ht : 𝕜} (hc : c ≠ 0)
    (hGZ : c * ht = iteratedDeriv 1 (G * H) x) : ht = 0 := by
  have := (ProductOrder.low_derivs_vanish hG hH hG0 hG1 hH0).2.1
  rw [this] at hGZ
  exact (mul_eq_zero.mp hGZ).resolve_left hc

end ProductOrder

section Degenerate

variable {T R : Type*} [MulZeroClass R]

/-- A family of identities `c · Z t = B t` with constant factor `c = 0` is equivalent to
`B = 0`, whatever `Z` is: it determines nothing about `Z`, at any order in `t`. -/
theorem degenerate_identity_iff {c : R} (hc : c = 0) (Z B : T → R) :
    (∀ t, c * Z t = B t) ↔ ∀ t, B t = 0 := by
  subst hc
  simp only [zero_mul]
  exact ⟨fun h t => (h t).symm, fun h t => (h t).symm⟩

/-- Consequently any two candidate values `Z`, `Z'` satisfy the degenerate identity
simultaneously. -/
theorem degenerate_identity_blind {c : R} (hc : c = 0) (Z Z' B : T → R) :
    (∀ t, c * Z t = B t) ↔ (∀ t, c * Z' t = B t) := by
  rw [degenerate_identity_iff hc, degenerate_identity_iff hc]

end Degenerate

section Eigen

variable {R M N : Type*} [CommRing R] [Invertible (2 : R)]
  [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]

/-- Equivariance kills the `(−1)`-eigenspace in a target with trivial action
(`2` invertible). -/
theorem equivariant_minus_to_plus_eq_zero (τM : M →ₗ[R] M) (τN : N →ₗ[R] N)
    (f : M →ₗ[R] N) (hf : ∀ m, f (τM m) = τN (f m)) {m : M} (hm : τM m = -m)
    (hfix : τN (f m) = f m) : f m = 0 := by
  have h1 : f m = -f m := by
    calc f m = τN (f m) := hfix.symm
      _ = f (τM m) := (hf m).symm
      _ = -f m := by rw [hm, map_neg]
  have h2 : (2 : R) • f m = 0 := by
    rw [two_smul]; nth_rewrite 1 [h1]; exact neg_add_cancel _
  calc f m = (⅟(2 : R) * 2) • f m := by rw [invOf_mul_self, one_smul]
    _ = 0 := by rw [mul_smul, h2, smul_zero]

/-- Version for a target on which the involution is the identity. -/
theorem equivariant_minus_to_trivial_eq_zero (τM : M →ₗ[R] M) (f : M →ₗ[R] N)
    (hf : ∀ m, f (τM m) = f m) {m : M} (hm : τM m = -m) : f m = 0 :=
  equivariant_minus_to_plus_eq_zero τM LinearMap.id f (by simpa using hf) hm rfl

end Eigen

/-- Calibration arithmetic on the seed's recorded numbers: with `c∞ = 2`, `Tam = 16`,
`tors = 2` and the conjectural `#Ш = 9`, `4·c∞·Tam·#Ш/tors² = 288 = 8·36`, and in general
`4·c∞·Tam·S/tors² = 4·c∞·(S·Tam/tors²)`, i.e. `K_E = 4·c∞·q` whenever
`q = #Ш·Tam/tors²`. -/
theorem seed_calibration :
    (4 * 2 * 16 * 9 / 2 ^ 2 : ℚ) = 288 ∧ (288 : ℚ) = 8 * 36 ∧
      ∀ cinf tam S tors : ℚ, 4 * cinf * tam * S / tors ^ 2 = 4 * cinf * (S * tam / tors ^ 2) := by
  refine ⟨by norm_num, by norm_num, fun cinf tam S tors => by ring⟩

end Rank2Anchor

end
