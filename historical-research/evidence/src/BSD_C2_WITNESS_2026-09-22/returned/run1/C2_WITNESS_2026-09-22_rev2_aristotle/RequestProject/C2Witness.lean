import Mathlib

/-!
# The witness `c₂(p)` for the BLV square-root anticyclotomic `p`-adic `L`-function

This file formalises the *algebraic* content of the witness described in the task packet
(`INPUTS.md` §4, as corrected by the definition note): BLV's construction is taken with
`g = f_E`, `L = 1`, `R = ℤ_p`, a topological generator `γ_∞` of `Gal(K_∞/K) ≅ ℤ_p` is fixed,
`Λ = ℤ_p[[T]]` with `T = γ_∞ - 1`, and

    c₂(p) = [T²] 𝓛_{f_E} ∈ ℤ_p .

At the first finite layer the image of `𝓛_{f_E,1}` in `𝔽_p[G₁]/I³ ≃ 𝔽_p[t]/(t³)` determines only
the reduction `c₂(p) mod p`, and

    c₂(p) mod p  =  - ∑_{j=0}^{p-1} C(j,2) · ψ̄_{f_E}(γ^j P₁),        P₁ = traced conductor-`p²`
                                                                       Gross point.

Nothing about elliptic curves, Gross points or `p`-adic `L`-functions is *assumed* here: the
arithmetic inputs are abstracted into the data of the mod-`p` values
`v j = ψ̄_{f_E}(γ^j P₁) ∈ 𝔽_p`, and what is proved is the exact algebra that surrounds the
witness.  The four blocks are:

1.  **First-layer algebra.**  The coefficient extraction that produces the displayed formula
    (`coeff_sum_one_add_X_pow`), the hockey-stick evaluation of the cyclic norm element
    (`coeff_sum_one_add_X_pow_const`), the fact that for `p ≥ 5` the norm element — hence the
    ordinary stabilisation term `α^{-1} ψ(P₀)·N` — dies in `𝔽_p[t]/(t³)`
    (`norm_element_coeff_eq_zero`), and the identification `𝔽_p[G₁]/I³ ≃ 𝔽_p[t]/(t³)`
    (`one_add_X_pow_char`, `X_pow_mem_span_X_pow_three`).

2.  **The layer-one element and reduction to a second moment.**  `layerOne` is the image of
    BLV's `𝓛_{f_E,1} = α^{-1}∑_σ ψ(σP₀)σ − ∑_σ ψ(σP₁)σ` in `𝔽_p[t]/(t³)`, and `coeff_layerOne`
    proves the reduction formula of the task statement from BLV's definition.  The layer-one
    image of `𝓛_{f_E}` lies in `I²` (unconditional lower order: BD Annals 2005, Cor. 3, with
    `(r⁺,r⁻) = (2,0)`), which in the present notation says `moment 1 v = 0`
    (`moment_one_eq_zero_of_layerOne_mem`).  Granting only that, the witness becomes a pure
    second-moment condition (`c2bar_eq_neg_inv_two_mul_moment_two`,
    `c2bar_ne_zero_iff_moment_two_ne_zero`, `layerOne_coeff_two_ne_zero_iff`):

        c₂(p) mod p = -2⁻¹ ∑_{j=0}^{p-1} j² · v j ,   so   c₂(p) ∈ ℤ_p^×  ⟺  ∑_j j² v j ≠ 0 in 𝔽_p.

3.  **Well-posedness and an obstruction.**  Changing the topological generator `γ_∞ ↦ γ_∞^a`
    rescales the second moment by the unit `a^{-2}`, so the witness is independent of that choice
    (`momentZ_generator_change`, `momentZ_two_ne_zero_generator_independent`); and the second
    moment vanishes identically whenever `j ↦ v j` is given by a polynomial of low degree
    (`momentZ_eq_zero_of_low_degree`, `momentZ_two_eq_zero_of_affine`).  Sharply
    (`momentZ_two_eq_neg_coeff`, `momentZ_two_ne_zero_iff_coeff_ne_zero`): writing the packet as
    the polynomial function `v x = ∑_{i<p} c i · x^i`, one has `∑_x x² v x = -c (p-3)`, so the
    witness is *exactly* the degree-`(p−3)` coefficient of the interpolating polynomial of the
    Gross-point packet — a single high-degree mod-`p` Fourier-type coefficient.

4.  **Integral statement.**  `c₂(p) ∈ ℤ_p^×` is equivalent to the reduction of `𝓛` having order
    exactly `2`, i.e. to `μ(𝓛) = 0` together with `λ(𝓛) = 2`
    (`isUnit_c2_iff_order_eq_two`).  This is the Iwasawa-theoretic form of the target and is what
    the accompanying report identifies as the first missing theorem.
-/

namespace C2Witness

open Finset Polynomial

/-! ## 1. First-layer algebra -/

section Layer

variable {R : Type*} [CommRing R]

/-- Coefficient extraction at the first layer: writing `γ^j = (1+t)^j`, the `t^k`-coefficient of
`∑_j a j · γ^j` is `∑_j C(j,k) · a j`.  For `k = 2` this is precisely the computational formula
for the witness. -/
theorem coeff_sum_one_add_X_pow (n k : ℕ) (a : ℕ → R) :
    (∑ j ∈ range n, C (a j) * (1 + X) ^ j).coeff k = ∑ j ∈ range n, (j.choose k : R) * a j := by
  simp [Polynomial.finset_sum_coeff, coeff_one_add_X_pow, mul_comm]

/-- Hockey stick: `∑_{j<n} C(j,k) = C(n,k+1)`. -/
theorem sum_range_choose_eq_choose (n k : ℕ) :
    ∑ j ∈ range n, j.choose k = n.choose (k + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.sum_range_succ, ih, Nat.choose_succ_succ' n k]
      omega

/-- The coefficients of the cyclic norm element `N = ∑_{j<n} (1+t)^j` are binomial coefficients. -/
theorem coeff_sum_one_add_X_pow_const (n k : ℕ) :
    (∑ j ∈ range n, ((1 + X : R[X])) ^ j).coeff k = (n.choose (k + 1) : R) := by
  have h : ∑ j ∈ range n, ((1 + X : R[X])) ^ j
      = ∑ j ∈ range n, C (1 : R) * (1 + X) ^ j := by simp
  rw [h, coeff_sum_one_add_X_pow]
  simp [← Nat.cast_sum, sum_range_choose_eq_choose]

end Layer

/-- For `p ≥ 5` prime the cyclic norm element `N = ∑_{j<p}(1+t)^j` lies in `(t³)` modulo `p`:
its coefficients in degrees `0, 1, 2` are `p`, `C(p,2)`, `C(p,3)`, all divisible by `p`.
This is why the ordinary stabilisation term `α^{-1}ψ(P₀)·N` is invisible in the quotient
`𝔽_p[t]/(t³)` that computes the witness. -/
theorem norm_element_coeff_eq_zero {p : ℕ} (hp : p.Prime) (hp5 : 5 ≤ p) {k : ℕ} (hk : k ≤ 2) :
    (∑ j ∈ range p, ((1 + X : (ZMod p)[X])) ^ j).coeff k = 0 := by
  rw [coeff_sum_one_add_X_pow_const]
  have : (p : ℕ) ∣ p.choose (k + 1) := hp.dvd_choose_self (Nat.succ_ne_zero k) (by omega)
  obtain ⟨m, hm⟩ := this
  rw [hm]
  simp

/-- In characteristic `p`, `(1+t)^p - 1 = t^p`; so `𝔽_p[G₁] ≃ 𝔽_p[t]/(t^p)`. -/
theorem one_add_X_pow_char (p : ℕ) [Fact p.Prime] :
    ((1 + X : (ZMod p)[X])) ^ p - 1 = X ^ p := by
  rw [add_pow_char]
  simp

/-- For `p ≥ 3` the relation `t^p` is already contained in `I³ = (t³)`; combined with
`one_add_X_pow_char` this is the isomorphism `𝔽_p[G₁]/I³ ≃ 𝔽_p[t]/(t³)`. -/
theorem X_pow_mem_span_X_pow_three {p : ℕ} (hp : 3 ≤ p) :
    (X : (ZMod p)[X]) ^ p ∈ Ideal.span {(X : (ZMod p)[X]) ^ 3} := by
  rw [Ideal.mem_span_singleton]
  exact pow_dvd_pow _ hp

/-! ## 2. The witness functional and its reduction to a second moment -/

section Witness

variable (p : ℕ)

/-- The mod-`p` witness, as a functional of the packet of Gross-point values
`v j = ψ̄_{f_E}(γ^j P₁) ∈ 𝔽_p`:

    c₂(p) mod p = - ∑_{j=0}^{p-1} C(j,2) · v j. -/
def c2bar (v : ℕ → ZMod p) : ZMod p := -∑ j ∈ range p, (j.choose 2 : ZMod p) * v j

/-- The `k`-th moment `∑_{j=0}^{p-1} j^k · v j` of the packet. -/
def moment (k : ℕ) (v : ℕ → ZMod p) : ZMod p := ∑ j ∈ range p, (j : ZMod p) ^ k * v j

/-- An element of `(tⁿ)` has vanishing coefficients in degrees `< n`. -/
theorem coeff_eq_zero_of_mem_span_X_pow {R : Type*} [CommRing R] {f : R[X]} {n : ℕ}
    (hf : f ∈ Ideal.span {(X : R[X]) ^ n}) {k : ℕ} (hk : k < n) : f.coeff k = 0 := by
  obtain ⟨g, rfl⟩ := Ideal.mem_span_singleton.1 hf
  rw [mul_comm, Polynomial.coeff_mul_X_pow']
  simp [Nat.not_le.2 hk]

/-- **The witness is a function of the image in `𝔽_p[G₁]/I³ ≃ 𝔽_p[t]/(t³)` only.**  Two packets
whose layer-one elements `∑_j v j · γ^j` agree modulo `(t³)` have the same witness.  Together with
`one_add_X_pow_char` and `X_pow_mem_span_X_pow_three` this is the statement that
`c₂(p) mod p`, and not the integral coefficient, is what the first finite layer determines. -/
theorem c2bar_eq_of_sub_mem_span (v w : ℕ → ZMod p)
    (h : (∑ j ∈ range p, C (v j) * (1 + X) ^ j) - (∑ j ∈ range p, C (w j) * (1 + X) ^ j)
      ∈ Ideal.span {(X : (ZMod p)[X]) ^ 3}) :
    c2bar p v = c2bar p w := by
  have h2 := coeff_eq_zero_of_mem_span_X_pow h (k := 2) (by norm_num)
  rw [Polynomial.coeff_sub, coeff_sum_one_add_X_pow, coeff_sum_one_add_X_pow, sub_eq_zero] at h2
  unfold c2bar
  rw [h2]

theorem two_mul_choose_two_add (j : ℕ) : 2 * j.choose 2 + j = j ^ 2 := by
  induction j with
  | zero => simp
  | succ n ih =>
      rw [Nat.choose_succ_succ' n 1, Nat.choose_one_right]
      ring_nf
      ring_nf at ih
      omega

/-- The universal relation between the witness and the first two moments:
`2 · c₂ = M₁ - M₂`. -/
theorem two_mul_c2bar (v : ℕ → ZMod p) :
    2 * c2bar p v = moment p 1 v - moment p 2 v := by
  unfold c2bar moment
  rw [mul_neg, Finset.mul_sum, ← Finset.sum_sub_distrib]
  rw [neg_eq_iff_eq_neg, ← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  have h : ((2 * j.choose 2 + j : ℕ) : ZMod p) = ((j ^ 2 : ℕ) : ZMod p) := by
    rw [two_mul_choose_two_add]
  push_cast at h
  have : (2 : ZMod p) * (j.choose 2 : ZMod p) = (j : ZMod p) ^ 2 - (j : ZMod p) := by
    linear_combination h
  rw [← mul_assoc, this]
  ring

variable [Fact p.Prime]

/-- `2` is invertible mod an odd prime. -/
theorem two_ne_zero_of_ne_two (hp2 : p ≠ 2) : (2 : ZMod p) ≠ 0 := by
  have h2 : ((2 : ℕ) : ZMod p) ≠ 0 := by
    rw [Ne, CharP.cast_eq_zero_iff (ZMod p) p]
    intro hd
    exact hp2 ((Nat.prime_dvd_prime_iff_eq (Fact.out : p.Prime) Nat.prime_two).1 hd)
  simpa using h2

/-- **Reduction of the witness to a second moment.**  The unconditional lower order
`𝓛_{f_E} ∈ I²` (BD Annals 2005, Cor. 3, with `(r⁺,r⁻) = (2,0)`) says exactly that the first
moment of the packet vanishes mod `p`.  Granting that, the witness is `-2⁻¹` times the second
moment. -/
theorem c2bar_eq_neg_inv_two_mul_moment_two (hp2 : p ≠ 2) (v : ℕ → ZMod p)
    (h1 : moment p 1 v = 0) :
    c2bar p v = -(2 : ZMod p)⁻¹ * moment p 2 v := by
  have h2 := two_ne_zero_of_ne_two p hp2
  have h := two_mul_c2bar p v
  rw [h1, zero_sub] at h
  field_simp
  linear_combination h

/-- **The witness in second-moment form.**  For `p` odd, and granting the unconditional
vanishing of the first moment, `c₂(p) ∈ ℤ_p^×` is equivalent to the nonvanishing mod `p` of the
second moment `∑_{j=0}^{p-1} j² ψ̄_{f_E}(γ^j P₁)`. -/
theorem c2bar_ne_zero_iff_moment_two_ne_zero (hp2 : p ≠ 2) (v : ℕ → ZMod p)
    (h1 : moment p 1 v = 0) :
    c2bar p v ≠ 0 ↔ moment p 2 v ≠ 0 := by
  have h2 := two_ne_zero_of_ne_two p hp2
  rw [c2bar_eq_neg_inv_two_mul_moment_two p hp2 v h1]
  simp [inv_ne_zero h2]


/-! ### The layer-one element

Write `E₁` for the image, in `𝔽_p[t]/(t³) = 𝔽_p[G₁]/I³`, of BLV's

    𝓛_{f_E,1} = α^{-1} ∑_{σ∈G₁} ψ(σ P₀)·σ  −  ∑_{σ∈G₁} ψ(σ P₁)·σ ,

i.e. of `u · N − ∑_j v j · γ^j` with `u = α^{-1} ψ̄(P₀)`, `N = ∑_{j<p} γ^j` the cyclic norm element,
and `v j = ψ̄(γ^j P₁)`.
-/

/-- The layer-one element of BLV's construction, written in `𝔽_p[t]`. -/
noncomputable def layerOne (u : ZMod p) (v : ℕ → ZMod p) : (ZMod p)[X] :=
  C u * (∑ j ∈ range p, (1 + X) ^ j) - ∑ j ∈ range p, C (v j) * (1 + X) ^ j

/-- **The reduction formula of `INPUTS.md` §4, proved.**  For `p ≥ 5` the stabilisation term
`α^{-1}ψ(P₀)·N` is invisible in degrees `≤ 2`, so for `k ≤ 2` the `t^k`-coefficient of the
layer-one element is `-∑_{j<p} C(j,k) ψ̄(γ^j P₁)`.  For `k = 2` this is exactly

    c₂(p) mod p  =  - ∑_{j=0}^{p-1} C(j,2) · ψ̄_{f_E}(γ^j P₁). -/
theorem coeff_layerOne (hp5 : 5 ≤ p) (u : ZMod p) (v : ℕ → ZMod p)
    {k : ℕ} (hk : k ≤ 2) :
    (layerOne p u v).coeff k = -∑ j ∈ range p, (j.choose k : ZMod p) * v j := by
  unfold layerOne
  rw [Polynomial.coeff_sub, coeff_sum_one_add_X_pow, Polynomial.coeff_C_mul,
    norm_element_coeff_eq_zero (Fact.out) hp5 hk, mul_zero, zero_sub]

theorem coeff_two_layerOne (hp5 : 5 ≤ p) (u : ZMod p) (v : ℕ → ZMod p) :
    (layerOne p u v).coeff 2 = c2bar p v :=
  coeff_layerOne p hp5 u v (le_refl 2)

theorem coeff_one_layerOne (hp5 : 5 ≤ p) (u : ZMod p) (v : ℕ → ZMod p) :
    (layerOne p u v).coeff 1 = -moment p 1 v := by
  rw [coeff_layerOne p hp5 u v (by norm_num)]
  simp [moment]

/-- The unconditional lower order `𝓛_{f_E} ∈ I²` (BD Annals 2005, Cor. 3, with `(r⁺,r⁻)=(2,0)`)
forces the first moment of the Gross-point packet to vanish mod `p`. -/
theorem moment_one_eq_zero_of_layerOne_mem (hp5 : 5 ≤ p) (u : ZMod p)
    (v : ℕ → ZMod p) (h : layerOne p u v ∈ Ideal.span {(X : (ZMod p)[X]) ^ 2}) :
    moment p 1 v = 0 := by
  have := coeff_eq_zero_of_mem_span_X_pow h (k := 1) (by norm_num)
  rw [coeff_one_layerOne p hp5 u v, neg_eq_zero] at this
  exact this

/-- **Capstone.**  For `p ≥ 5`, granting only the unconditional lower order (`layerOne ∈ I²`),
the witness `c₂(p) ∈ ℤ_p^×` is equivalent to the nonvanishing mod `p` of the second moment
`∑_{j=0}^{p-1} j² · ψ̄_{f_E}(γ^j P₁)` of the traced conductor-`p²` Gross-point packet. -/
theorem layerOne_coeff_two_ne_zero_iff (hp5 : 5 ≤ p) (u : ZMod p)
    (v : ℕ → ZMod p) (h : layerOne p u v ∈ Ideal.span {(X : (ZMod p)[X]) ^ 2}) :
    (layerOne p u v).coeff 2 ≠ 0 ↔ moment p 2 v ≠ 0 := by
  rw [coeff_two_layerOne p hp5 u v]
  exact c2bar_ne_zero_iff_moment_two_ne_zero p (by omega) v
    (moment_one_eq_zero_of_layerOne_mem p hp5 u v h)

end Witness

/-! ## 3. Moments as functions on `G₁`, generator change, and the low-degree obstruction -/

section Moments

variable (p : ℕ) [NeZero p]

/-- The `k`-th moment of a packet regarded as a function on `G₁ ≅ ℤ/p`. -/
def momentZ (k : ℕ) (v : ZMod p → ZMod p) : ZMod p := ∑ x : ZMod p, x ^ k * v x

theorem sum_range_eq_sum_univ (f : ZMod p → ZMod p) :
    ∑ j ∈ range p, f j = ∑ x : ZMod p, f x := by
  refine Finset.sum_nbij' (i := fun (j : ℕ) => (j : ZMod p)) (j := fun (x : ZMod p) => x.val)
    ?_ ?_ ?_ ?_ ?_ <;>
  intros <;> simp_all [ZMod.val_lt, ZMod.natCast_val, Nat.mod_eq_of_lt]

theorem moment_eq_momentZ (k : ℕ) (v : ZMod p → ZMod p) :
    moment p k (fun j => v (j : ZMod p)) = momentZ p k v :=
  sum_range_eq_sum_univ p (fun x => x ^ k * v x)

variable [Fact p.Prime]

/-- **Independence of the topological generator.**  Replacing `γ_∞` by `γ_∞^a` (`a` prime to `p`)
replaces the packet `v` by `x ↦ v (a x)` and multiplies the `k`-th moment by `a^{-k}`.  For
`k = 2` this is the finite-layer shadow of the transformation `c₂ ↦ a^{-2} c₂` of the
`T²`-coefficient, and shows that unit status of the witness does not depend on the choice of
topological generator. -/
theorem momentZ_generator_change {a : ZMod p} (ha : a ≠ 0) (k : ℕ) (v : ZMod p → ZMod p) :
    momentZ p k (fun x => v (a * x)) = a⁻¹ ^ k * momentZ p k v := by
  unfold momentZ
  rw [Finset.mul_sum,
    ← Equiv.sum_comp (Equiv.mulLeft₀ a⁻¹ (inv_ne_zero ha)) (fun x => x ^ k * v (a * x))]
  refine Finset.sum_congr rfl (fun y _ => ?_)
  have he : (Equiv.mulLeft₀ a⁻¹ (inv_ne_zero ha)) y = a⁻¹ * y := rfl
  have hay : a * (a⁻¹ * y) = y := by field_simp
  simp only [he, hay, mul_pow]
  ring

theorem momentZ_two_ne_zero_generator_independent {a : ZMod p} (ha : a ≠ 0)
    (v : ZMod p → ZMod p) :
    momentZ p 2 (fun x => v (a * x)) ≠ 0 ↔ momentZ p 2 v ≠ 0 := by
  rw [momentZ_generator_change p ha]
  have ha' : (a⁻¹ : ZMod p) ^ 2 ≠ 0 := pow_ne_zero _ (inv_ne_zero ha)
  exact ⟨fun h hz => h (by rw [hz, mul_zero]), fun h hz => h ((mul_eq_zero.1 hz).resolve_left ha')⟩

/-- **The low-degree obstruction.**  If the packet `v` is given on `G₁` by a polynomial function
of degree `≤ d` with `k + d < p - 1`, its `k`-th moment vanishes.  So no packet whose mod-`p`
values are a low-degree polynomial function of the Galois index can witness `c₂(p) ∈ ℤ_p^×`:
the witness is a statement of equidistribution type. -/
theorem momentZ_eq_zero_of_low_degree {k d : ℕ} (c : ℕ → ZMod p) (h : k + d < p - 1) :
    momentZ p k (fun x => ∑ i ∈ range (d + 1), c i * x ^ i) = 0 := by
  have hcard : Fintype.card (ZMod p) = p := ZMod.card p
  unfold momentZ
  have hstep : ∀ x : ZMod p, x ^ k * (∑ i ∈ range (d + 1), c i * x ^ i)
      = ∑ i ∈ range (d + 1), c i * x ^ (k + i) := by
    intro x
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl (fun i _ => by rw [pow_add]; ring)
  rw [Finset.sum_congr rfl (fun x _ => hstep x), Finset.sum_comm]
  refine Finset.sum_eq_zero (fun i hi => ?_)
  have hi' : i ≤ d := by simpa [Nat.lt_succ_iff] using hi
  have : ∑ x : ZMod p, c i * x ^ (k + i) = c i * ∑ x : ZMod p, x ^ (k + i) := by
    rw [Finset.mul_sum]
  rw [this, FiniteField.sum_pow_lt_card_sub_one (ZMod p) (k + i) (by omega), mul_zero]

/-- An affine packet has vanishing second moment (`p ≥ 5`); in particular constant packets
cannot witness `c₂(p) ∈ ℤ_p^×`. -/
theorem momentZ_two_eq_zero_of_affine (hp5 : 5 ≤ p) (A B : ZMod p) :
    momentZ p 2 (fun x => A + B * x) = 0 := by
  have h := momentZ_eq_zero_of_low_degree p (k := 2) (d := 1)
    (fun i => if i = 0 then A else B) (by omega)
  simpa [Finset.sum_range_succ] using h


/-- Sum of `k`-th powers over `𝔽_p`, `k > 0`: it is `-1` when `(p-1) ∣ k` and `0` otherwise. -/
theorem sum_pow_eq_ite (k : ℕ) (hk : 0 < k) :
    ∑ x : ZMod p, x ^ k = if (p - 1) ∣ k then -1 else 0 := by
  have h := FiniteField.sum_pow_units (ZMod p) k
  rw [ZMod.card] at h
  rw [← h]
  have key : ∑ x : ZMod p, x ^ k = ∑ x ∈ univ.erase (0 : ZMod p), x ^ k := by
    rw [Finset.sum_erase _ (by simp [hk.ne'])]
  rw [key]
  refine (Finset.sum_bij (i := fun (u : (ZMod p)ˣ) _ => (u : ZMod p)) ?_ ?_ ?_ ?_).symm
  · intro u _
    simp [Units.ne_zero]
  · intro u _ w _ huw
    exact Units.ext huw
  · intro x hx
    simp only [Finset.mem_erase, Finset.mem_univ, and_true] at hx
    exact ⟨Units.mk0 x hx, Finset.mem_univ _, rfl⟩
  · intro u _
    rfl

/-- **The witness reads off one coefficient of the interpolating polynomial.**  If the packet is
written as the polynomial function `v x = ∑_{i<p} c i · x^i` (which every function on `𝔽_p` is,
uniquely — see `exists_poly_repr`), then for `p ≥ 5`

    ∑_{x} x² · v x  =  - c (p-3).

So the witness sees exactly the degree-`(p−3)` coefficient of the packet, and nothing else. -/
theorem momentZ_two_eq_neg_coeff (hp5 : 5 ≤ p) (c : ℕ → ZMod p) :
    momentZ p 2 (fun x => ∑ i ∈ range p, c i * x ^ i) = -c (p - 3) := by
  unfold momentZ
  have hstep : ∀ x : ZMod p, x ^ 2 * (∑ i ∈ range p, c i * x ^ i)
      = ∑ i ∈ range p, c i * x ^ (2 + i) := by
    intro x
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl (fun i _ => by rw [pow_add]; ring)
  rw [Finset.sum_congr rfl (fun x _ => hstep x), Finset.sum_comm]
  have hsum : ∀ i ∈ range p, ∑ x : ZMod p, c i * x ^ (2 + i)
      = c i * (if (p - 1) ∣ (2 + i) then -1 else 0) := by
    intro i _
    rw [← Finset.mul_sum, sum_pow_eq_ite p (2 + i) (by omega)]
  rw [Finset.sum_congr rfl hsum, Finset.sum_eq_single (p - 3)]
  · have hEq : 2 + (p - 3) = p - 1 := by omega
    rw [hEq, if_pos dvd_rfl]
    ring
  · intro i hi hne
    have hnd : ¬ (p - 1) ∣ (2 + i) := by
      rintro ⟨t, ht⟩
      simp only [Finset.mem_range] at hi
      match t with
      | 0 => omega
      | 1 => omega
      | (t + 2) =>
        have : (p - 1) * 2 ≤ (p - 1) * (t + 2) := Nat.mul_le_mul_left _ (by omega)
        omega
    rw [if_neg hnd, mul_zero]
  · intro h
    simp only [Finset.mem_range] at h
    omega

/-- Every function on `𝔽_p` is a polynomial function of degree `< p` (Lagrange interpolation). -/
theorem exists_poly_repr (v : ZMod p → ZMod p) :
    ∃ c : ℕ → ZMod p, ∀ x, v x = ∑ i ∈ range p, c i * x ^ i := by
  classical
  set f := Lagrange.interpolate (univ : Finset (ZMod p)) id v
  have hcard : (univ : Finset (ZMod p)).card = p := by
    rw [Finset.card_univ, ZMod.card]
  have hdeg : f.degree < (p : WithBot ℕ) := by
    have := Lagrange.degree_interpolate_lt (s := (univ : Finset (ZMod p))) (v := id) v
      Function.injective_id.injOn
    rwa [hcard] at this
  have hnat : f.natDegree < p := by
    rcases eq_or_ne f 0 with h | h
    · simp [h, (Fact.out : p.Prime).pos]
    · exact (Polynomial.natDegree_lt_iff_degree_lt h).2 hdeg
  refine ⟨fun i => f.coeff i, fun x => ?_⟩
  rw [← Polynomial.eval_eq_sum_range' hnat]
  exact (Lagrange.eval_interpolate_at_node v Function.injective_id.injOn (mem_univ x)).symm

/-- **Sharp form of the obstruction.**  For `p ≥ 5` the witness is nonzero exactly when the
interpolating polynomial of the Gross-point packet `j ↦ ψ̄_{f_E}(γ^j P₁)` has nonzero coefficient
in degree `p − 3`.  Low-degree behaviour of the packet is therefore not merely insufficient
(`momentZ_eq_zero_of_low_degree`): the witness is blind to every degree other than `p − 3`. -/
theorem momentZ_two_ne_zero_iff_coeff_ne_zero (hp5 : 5 ≤ p) (v : ZMod p → ZMod p)
    (c : ℕ → ZMod p) (hc : ∀ x, v x = ∑ i ∈ range p, c i * x ^ i) :
    momentZ p 2 v ≠ 0 ↔ c (p - 3) ≠ 0 := by
  have hv : v = fun x => ∑ i ∈ range p, c i * x ^ i := funext hc
  rw [hv, momentZ_two_eq_neg_coeff p hp5 c, neg_ne_zero]

end Moments

/-! ## 4. The integral witness: `c₂(p)` a unit ⟺ `μ = 0` and `λ = 2` -/

section Integral

variable {p : ℕ} [Fact p.Prime]

/-- `c₂(p) = [T²] 𝓛 ∈ ℤ_p`, for `Λ = ℤ_p[[T]]`, `T = γ_∞ - 1`. -/
noncomputable def c2 (L : PowerSeries ℤ_[p]) : ℤ_[p] := PowerSeries.coeff 2 L

theorem isUnit_iff_toZMod_ne_zero (x : ℤ_[p]) : IsUnit x ↔ PadicInt.toZMod x ≠ 0 := by
  rw [Ne, ← RingHom.mem_ker, PadicInt.ker_toZMod, IsLocalRing.mem_maximalIdeal, mem_nonunits_iff,
    not_not]

/-- **Iwasawa form of the target.**  For `𝓛 ∈ I² ⊆ Λ = ℤ_p[[T]]` (the unconditional lower order),
`c₂(p) ∈ ℤ_p^×` holds if and only if the mod-`p` reduction of `𝓛` has order exactly `2`, i.e.
`μ(𝓛) = 0` and `λ(𝓛) = 2`.  Equivalently `λ(L_p) = 4 = 2·rank`, since `L_p = 𝓛 · 𝓛^ι`. -/
theorem isUnit_c2_iff_order_eq_two (L : PowerSeries ℤ_[p])
    (h0 : PowerSeries.coeff 0 L = 0) (h1 : PowerSeries.coeff 1 L = 0) :
    IsUnit (c2 L) ↔ (PowerSeries.map (PadicInt.toZMod) L).order = 2 := by
  rw [show ((2 : ℕ∞)) = ((2 : ℕ) : ℕ∞) from rfl, PowerSeries.order_eq_nat]
  rw [c2, isUnit_iff_toZMod_ne_zero]
  constructor
  · intro h
    refine ⟨by simpa [PowerSeries.coeff_map] using h, ?_⟩
    intro i hi
    interval_cases i <;> simp [PowerSeries.coeff_map, h0, h1]
  · rintro ⟨h, -⟩
    simpa [PowerSeries.coeff_map] using h

/-- The converse direction genuinely fails: a square-root `L`-function of the shape `T⁴` has a
unit leading coefficient and nonzero reduction, yet `c₂ = 0`.  (This is the gap recorded in the
packet: a converse to the bridge needs `ρ_p = 4`.) -/
example : c2 (PowerSeries.X ^ 4 : PowerSeries ℤ_[p]) = 0 := by
  simp [c2, PowerSeries.coeff_X_pow]

end Integral

end C2Witness
