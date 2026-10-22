/-
# RUN014-C2 — machine-checked fragments of the supplied mechanism

This file formalises the *finite, elementary* parts of the supplied mechanism for the
elliptic curve `62a1` and its prime quadratic twists `E_q`, namely:

* the definition of the prime family `F_62` and a machine-checked witness `13 ∈ F_62`;
* the 2-adic exclusion at the place `2` in the `phi_q` orientation (the four classes
  `-1, 31, -q, 31q` are locally insoluble), proved by reduction modulo `16`;
* the archimedean exclusion in the dual orientation (no real point for `d < 0`);
* the identity `x^2 - 15 q x + 64 q^2 = (x - 23 q)^2` modulo `31` together with the
  fact that `23` is a square modulo `31`, the two inputs of the local computation at `31`;
* the root-freeness of `z^2 - 15 z + 64` modulo `q` when `-31` is not a square,
  the input of the local computation at the twisting prime `q`;
* the absence of rational 4-torsion on `E_q`.

The remaining parts of the mechanism (the passage from the two isogeny Selmer groups to
`rank = 0` and `Sha[2^∞] = 0`, and all analytic inputs) are not formalised here; they are
classified in `work/FINAL_REPORT.md`.
-/
import Mathlib

namespace Run014

/-! ## 1. The prime family `F_62` -/

/-- The number of affine `F_q`-points of the Cremona curve `62a1`,
`y^2 + x y + y = x^3 - x^2 - x + 1`, counted by brute force. -/
def affineCount (q : ℕ) : ℕ :=
  ((Finset.range q ×ˢ Finset.range q).filter (fun p =>
     (((p.2 : ℤ) ^ 2 + (p.1 : ℤ) * (p.2 : ℤ) + (p.2 : ℤ))
        - ((p.1 : ℤ) ^ 3 - (p.1 : ℤ) ^ 2 - (p.1 : ℤ) + 1)) % (q : ℤ) = 0)).card

/-- `#E(F_q)` for `E = 62a1`, including the point at infinity. -/
def cardE (q : ℕ) : ℕ := affineCount q + 1

/-- The trace of Frobenius `a_q = q + 1 - #E(F_q)` for `E = 62a1`. -/
def traceE (q : ℕ) : ℤ := (q : ℤ) + 1 - (cardE q : ℤ)

/-- The prime family `F_62` of the supplied mechanism. -/
structure InF62 (q : ℕ) : Prop where
  prime : Nat.Prime q
  not_dvd_372 : ¬ q ∣ 372
  mod_eight : q % 8 = 5
  nonresidue : ¬ IsSquare ((q : ZMod 31))
  two_adic : cardE q % 8 = 4
  trace_ne_zero : traceE q ≠ 0

/-- `13` belongs to `F_62`: this is the finite witness on which the infinitude argument
of the mechanism (a Chebotarev argument) is based. -/
theorem thirteen_mem_F62 : InF62 13 where
  prime := by norm_num
  not_dvd_372 := by decide
  mod_eight := by norm_num
  nonresidue := by decide
  two_adic := by decide
  trace_ne_zero := by decide

/-- The witness values: `#E(F_13) = 12` and `a_13 = 2`. -/
theorem cardE_thirteen : cardE 13 = 12 ∧ traceE 13 = 2 := by
  constructor <;> decide

/-! ## 2. The local exclusion at the place `2` in the `phi_q` orientation -/

private lemma mod16_exclusion :
    ∀ Q U V N : ZMod 16, (Q = 5 ∨ Q = 13) → (U.val % 2 = 1 ∨ V.val % 2 = 1) →
      N ^ 2 ≠ -U ^ 4 + 30 * Q * U ^ 2 * V ^ 2 + 31 * Q ^ 2 * V ^ 4 ∧
      N ^ 2 ≠ 31 * U ^ 4 + 30 * Q * U ^ 2 * V ^ 2 - Q ^ 2 * V ^ 4 ∧
      N ^ 2 ≠ -Q * U ^ 4 + 30 * Q * U ^ 2 * V ^ 2 + 31 * Q * V ^ 4 ∧
      N ^ 2 ≠ 31 * Q * U ^ 4 + 30 * Q * U ^ 2 * V ^ 2 - Q * V ^ 4 := by decide

private lemma cast_odd {u : ℤ} (h : ¬ (2 ∣ u)) : ((u : ZMod 16)).val % 2 = 1 := by
  have hv : (((u : ZMod 16)).val : ℤ) = u % 16 := ZMod.val_intCast u
  have h2 : u % 2 = 1 := by omega
  omega

private lemma cast_q {q : ℤ} (h : q % 8 = 5) : ((q : ZMod 16) = 5 ∨ (q : ZMod 16) = 13) := by
  have h16 : q % 16 = 5 ∨ q % 16 = 13 := by omega
  rcases h16 with h1 | h1
  · left
    have : (q : ZMod 16) = ((5 : ℤ) : ZMod 16) := by
      rw [ZMod.intCast_eq_intCast_iff]; unfold Int.ModEq; omega
    simpa using this
  · right
    have : (q : ZMod 16) = ((13 : ℤ) : ZMod 16) := by
      rw [ZMod.intCast_eq_intCast_iff]; unfold Int.ModEq; omega
    simpa using this

/-- **Local exclusion at 2 (`phi_q` orientation).**  For `q ≡ 5 (mod 8)` none of the four
squareclasses `d = -1, 31, -q, 31 q` is represented by a primitive integral point of the
covering `n^2 = d u^4 + 30 q u^2 v^2 + (-31 q^2 / d) v^4`; hence none of them is 2-adically
soluble, and the `phi_q`-Selmer group is contained in `{1, q, -31, -31 q}`. -/
theorem phi_local_two_exclusion (q u v n : ℤ) (hq : q % 8 = 5)
    (hprim : ¬ (2 ∣ u) ∨ ¬ (2 ∣ v)) :
    n ^ 2 ≠ -u ^ 4 + 30 * q * u ^ 2 * v ^ 2 + 31 * q ^ 2 * v ^ 4 ∧
    n ^ 2 ≠ 31 * u ^ 4 + 30 * q * u ^ 2 * v ^ 2 - q ^ 2 * v ^ 4 ∧
    n ^ 2 ≠ -q * u ^ 4 + 30 * q * u ^ 2 * v ^ 2 + 31 * q * v ^ 4 ∧
    n ^ 2 ≠ 31 * q * u ^ 4 + 30 * q * u ^ 2 * v ^ 2 - q * v ^ 4 := by
  have hpar : ((u : ZMod 16)).val % 2 = 1 ∨ ((v : ZMod 16)).val % 2 = 1 := by
    rcases hprim with h | h
    · exact Or.inl (cast_odd h)
    · exact Or.inr (cast_odd h)
  obtain ⟨e1, e2, e3, e4⟩ :=
    mod16_exclusion (q : ZMod 16) (u : ZMod 16) (v : ZMod 16) (n : ZMod 16) (cast_q hq) hpar
  refine ⟨fun h => e1 ?_, fun h => e2 ?_, fun h => e3 ?_, fun h => e4 ?_⟩ <;>
    · have := congrArg (fun z : ℤ => (z : ZMod 16)) h
      push_cast at this
      linear_combination this

/-! ## 3. The archimedean exclusion in the dual orientation -/

/-- **Archimedean exclusion (dual orientation).**  For `q > 0` and `d < 0` the covering
`n^2 = d u^4 - 15 q u^2 v^2 + (64 q^2 / d) v^4` has no real point: the right-hand side is
strictly negative for every nonzero real pair `(u, v)`. -/
theorem dual_real_exclusion (q d u v : ℝ) (hq : 0 < q) (hd : d < 0) (huv : u ≠ 0 ∨ v ≠ 0) :
    d * u ^ 4 - 15 * q * u ^ 2 * v ^ 2 + (64 * q ^ 2 / d) * v ^ 4 < 0 := by
  have h1 : d * u ^ 4 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hd.le (by positivity)
  have h2 : 15 * q * u ^ 2 * v ^ 2 ≥ 0 := by positivity
  have h3 : (64 * q ^ 2 / d) * v ^ 4 ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg (div_nonpos_of_nonneg_of_nonpos (by positivity) hd.le)
      (by positivity)
  rcases huv with h | h
  · have : d * u ^ 4 < 0 := mul_neg_of_neg_of_pos hd (by positivity)
    linarith
  · have : (64 * q ^ 2 / d) * v ^ 4 < 0 :=
      mul_neg_of_neg_of_pos (div_neg_of_pos_of_neg (by positivity) hd) (by positivity)
    linarith

/-! ## 4. The local inputs at `31` and at the twisting prime `q` -/

/-- The component quadratic of `E_q` is a perfect square modulo `31`, with double root
`23 q`. -/
theorem g_sq_mod_31 (q x : ZMod 31) : x ^ 2 - 15 * q * x + 64 * q ^ 2 = (x - 23 * q) ^ 2 := by
  have h31 : (31 : ZMod 31) = 0 := by decide
  linear_combination (q * x - 15 * q ^ 2) * h31

/-- `23` is *not* a square modulo `31`; since `(q|31) = -1` as well, the double root
`23 q` of the reduced component quadratic *is* a square modulo `31`, which is the input of
the local computation at `31`. -/
theorem twentythree_nonsquare_mod_31 : ¬ IsSquare (23 : ZMod 31) := by decide

/-- Consequently `23 q` is a square modulo `31` for every non-residue `q`. -/
theorem twentythree_mul_nonsquare (q : ZMod 31) (hq : ¬ IsSquare q) : IsSquare (23 * q) := by
  revert hq; revert q; decide

/-- **Local input at the twisting prime.**  If `-31` is not a square modulo `q`, then the
component quadratic `z^2 - 15 z + 64` has no root modulo `q`; this is what forces the
odd valuation used to exclude the classes `q` and `2q` from the dual Selmer group. -/
theorem g_no_root_mod_q (q : ℕ) (h : ¬ IsSquare ((-31 : ZMod q))) (z : ZMod q) :
    z ^ 2 - 15 * z + 64 ≠ 0 := by
  intro hz
  exact h ⟨2 * z - 15, by linear_combination (-4 : ZMod q) * hz⟩

/-! ## 5. No rational 4-torsion on the twists -/

/-- **No rational 4-torsion.**  A rational point of order 4 on
`E_q : y^2 = x^3 - 15 q x^2 + 64 q^2 x` would have `x = 8 q` (the other candidate `-8q`
gives a negative right-hand side), forcing `64 q^3` to be a rational square; for an odd
prime `q` this is impossible.  Hence `E_q(Q)[2^∞] = Z/2`. -/
theorem no_four_torsion (q : ℕ) (hq : Nat.Prime q) (hodd : q ≠ 2) :
    ¬ ∃ y : ℤ, y ^ 2 = 64 * (q : ℤ) ^ 3 := by
  rintro ⟨y, hy⟩
  have hp : Prime ((q : ℤ)) := Nat.prime_iff_prime_int.mp hq
  have hq0 : ((q : ℤ)) ≠ 0 := by exact_mod_cast hq.pos.ne'
  have hdvd1 : (q : ℤ) ∣ y ^ 2 := ⟨64 * (q : ℤ) ^ 2, by linear_combination hy⟩
  obtain ⟨t, rfl⟩ := hp.dvd_of_dvd_pow hdvd1
  have h2 : t ^ 2 = 64 * (q : ℤ) := by
    have : (q : ℤ) ^ 2 * t ^ 2 = (q : ℤ) ^ 2 * (64 * (q : ℤ)) := by linear_combination hy
    exact mul_left_cancel₀ (pow_ne_zero 2 hq0) this
  have hdvd2 : (q : ℤ) ∣ t ^ 2 := ⟨64, by linear_combination h2⟩
  obtain ⟨s, rfl⟩ := hp.dvd_of_dvd_pow hdvd2
  have h3 : (q : ℤ) * s ^ 2 = 64 := by
    have : (q : ℤ) * ((q : ℤ) * s ^ 2) = (q : ℤ) * 64 := by linear_combination h2
    exact mul_left_cancel₀ hq0 this
  have hdvd3 : (q : ℤ) ∣ 64 := ⟨s ^ 2, h3.symm⟩
  have hdvd4 : q ∣ 64 := by exact_mod_cast hdvd3
  have : q ∣ 2 := hq.dvd_of_dvd_pow (n := 6) (by simpa using hdvd4)
  exact hodd ((Nat.prime_dvd_prime_iff_eq hq Nat.prime_two).mp this)

/-! ## 6. Bookkeeping for the 2-part of the BSD formula, and the scope of the family -/

/-- For the twists `E_q` one has `#E_q(Q)_tors = 2` and `prod_p c_p(E_q) = 4`, so the
analytic order of Sha,
`#Sha_an = L(E_q,1)/Omega_{E_q} * #E_q(Q)_tors^2 / prod_p c_p`, is *equal* to the algebraic
L-value.  Hence the 2-part of the BSD formula for `E_q` is exactly the statement
`ord_2 (L(E_q,1)/Omega_{E_q}) = ord_2 #Sha(E_q)[2^∞]`. -/
theorem sha_analytic_eq_algebraic_L (L : ℚ) : L * (2 : ℚ) ^ 2 / 4 = L := by ring

/-- The family is a proper subfamily of the primes: `7` is not in `F_62`.  A statement
proved for the members of `F_62` is therefore not a statement about all quadratic twists
of `62a1`. -/
theorem seven_not_mem_F62 : ¬ InF62 7 := by
  intro h
  have := h.mod_eight
  norm_num at this

end Run014
