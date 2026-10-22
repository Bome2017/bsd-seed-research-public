/-
`S_dyadic` saturation — THE TARGET.

One theorem, now proved.  It asserts that on the certified `(4,1)` stratum `H₄₁`, every square
class that is *everywhere locally soluble* is in fact *rationally soluble* — a genuine
local-to-global statement for these covering families — and records the explicit descent quotient.

Both sides come from the vendored, certified infrastructure:
  * `Run013.LocalKummerAll` — solubility at ℝ and at **every** ℚ_p;
  * `Run013.Cov ℚ` — rational solubility of the quartic covering.
Neither is defined in terms of the other, and neither mentions the answer.

`GlobalSet` below is defined by **actual rational solubility**, not by membership in an asserted
set.  See `FORMALIZATION_BOUNDARY.md`.
-/
import RequestProject.SDyadic.DualSide
import RequestProject.SDyadic.Witness

namespace SDyadic

open Run013
open scoped Classical

/-! ## The certified `(4,1)` stratum -/

/-- `H₄₁`: either `D < 0` with exactly one distinct prime divisor of `|D|`, or `D > 0` with exactly
two, both `≡ 3 (mod 4)`.  This is exactly the stratum on which certified `S_dyadic` gives
`(|Sel^φ|, |Sel^φ̂|) = (4,1)`. -/
def H41 (ε : ℤ) (m : ℕ) : Prop :=
  (DD ε m < 0 ∧ sCount ε m = 1) ∨
  (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3)

/-! ## The global set, defined by actual rational solubility -/

/-- The square classes that are **rationally** soluble for the covering attached to `(a,b)`.

Defined by `Cov ℚ`, i.e. by the existence of an honest rational point on the quartic — **not** by
membership in any asserted answer set. -/
noncomputable def GlobalSet (a b : ℚ) : Set Qsq :=
  {c | ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b (d : ℚ)}

/-! ## The explicit descent quotient

`⟨[D],[q]⟩ / ⟨[D]⟩`.  This is an **explicit descent quotient** of square classes.  It is *not* a
formal `Sel₂`, and must not be described as one: no `H¹`, no cocycles, no comparison map is
constructed anywhere in this project. -/

/-- `⟨[D], [q]⟩ ≤ ℚ*/ℚ*²`. -/
noncomputable def GphiExp (ε : ℤ) (m : ℕ) (q : ℕ) : Subgroup Qsq :=
  Subgroup.closure {cls ((DD ε m : ℤ) : ℚ), cls ((q : ℚ))}

/-- `⟨[D]⟩ ≤ ℚ*/ℚ*²`, the image of the comparison kernel. -/
noncomputable def KExp (ε : ℤ) (m : ℕ) : Subgroup Qsq :=
  Subgroup.closure {cls ((DD ε m : ℤ) : ℚ)}

/-! ## The target -/

/-- **THE PRINCIPAL TARGET — explicit descent saturation on `H₄₁`.**

For the dyadic family on the certified `(4,1)` stratum:

1. every everywhere-locally-soluble class for the φ coefficient pair is rationally soluble, and
   conversely;
2. the same for the dual pair;
3. hence `GlobalSet = SelmerSet` for both pairs;
4. and the explicit descent quotient `⟨[D],[q]⟩/⟨[D]⟩` has order 2, written as the index
   of `⟨[D]⟩` inside `⟨[D],[q]⟩`.

Rational witnesses for the four φ classes, from the reviewed target document:

    d = 1   : (u,v,n) = (1,0,1)
    d = D   : (u,v,n) = (0,1,q)
    d = q   : (u,v,n) = (1,1,0)
    d = Dq  : (u,v,n) = (1,1,0)

the last two using `1 − 2A + D = 0`.  The dual class `1` uses `(1,0,1)`.  A witness transports along
`d' = d z²` by `(u,v,n) ↦ (u/z, v, n/z)`, which supplies arbitrary squareclass representatives.  The
reverse implication is base change from `ℚ` to `ℝ` and to every `ℚ_p`. -/
theorem sdyadic_saturation
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m) :
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (phiA ε m q) (phiB ε m q) d ↔ Cov ℚ (phiA ε m q) (phiB ε m q) d)) ∧
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (dualA ε m q) (dualB ε m q) d ↔ Cov ℚ (dualA ε m q) (dualB ε m q) d)) ∧
    GlobalSet (phiA ε m q) (phiB ε m q) = SelmerSet (phiA ε m q) (phiB ε m q) ∧
    GlobalSet (dualA ε m q) (dualB ε m q) = SelmerSet (dualA ε m q) (dualB ε m q) ∧
    ((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2 := by
  classical
  have hqp : Nat.Prime q := hP.q_prime
  have hq0 : (q : ℤ) ≠ 0 := by exact_mod_cast hqp.ne_zero
  have hD0 : DD ε m ≠ 0 := D_ne_zero ε m
  have hH' : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3) := hH
  have hbphi : phiB ε m q ≠ 0 := by
    simp only [phiB]
    exact Int.cast_ne_zero.mpr (mul_ne_zero hD0 (pow_ne_zero 2 hq0))
  have hbdual : dualB ε m q ≠ 0 := by
    have hr0 : rr ε m ≠ 0 := by
      simp only [rr]
      rcases hP.eps_unit with rfl | rfl <;> positivity
    simp only [dualB, BB]
    exact Int.cast_ne_zero.mpr (mul_ne_zero (pow_ne_zero 2 hr0) (pow_ne_zero 2 hq0))
  -- the φ side
  have hphi : ∀ d : ℚ, d ≠ 0 →
      (LocalKummerAll (phiA ε m q) (phiB ε m q) d ↔ Cov ℚ (phiA ε m q) (phiB ε m q) d) := by
    intro d hd
    constructor
    · intro hL
      obtain ⟨e, he, hsf, hsq⟩ := exists_squarefree_rep d hd
      have heQ : ((e : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr he
      have hLe : LocalKummerAll (phiA ε m q) (phiB ε m q) ((e : ℤ) : ℚ) :=
        localKummerAll_sqEq hbphi hd (hsq.symm heQ) hL
      have hcov_e : Cov ℚ (phiA ε m q) (phiB ε m q) ((e : ℤ) : ℚ) := by
        rcases phi_exhaustion hP hH' he hsf hLe with h | h | h | h
        · exact cov_sqEq one_ne_zero h (cov_phi_one ε m q)
        · exact cov_sqEq (Int.cast_ne_zero.mpr hD0) h (cov_phi_D ε m q)
        · exact cov_sqEq (Int.cast_ne_zero.mpr hq0) h (cov_phi_q ε m q)
        · exact cov_sqEq (Int.cast_ne_zero.mpr (mul_ne_zero hD0 hq0)) h (cov_phi_Dq ε m q)
      exact cov_sqEq heQ hsq hcov_e
    · intro hcov
      rw [localKummerAll_iff_cov hbphi hd]
      exact ⟨cov_base_change hcov, fun p _ => cov_base_change hcov⟩
  -- the dual side
  have hdual : ∀ d : ℚ, d ≠ 0 →
      (LocalKummerAll (dualA ε m q) (dualB ε m q) d ↔ Cov ℚ (dualA ε m q) (dualB ε m q) d) := by
    intro d hd
    constructor
    · intro hL
      obtain ⟨e, he, hsf, hsq⟩ := exists_squarefree_rep d hd
      have heQ : ((e : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr he
      have hLe : LocalKummerAll (dualA ε m q) (dualB ε m q) ((e : ℤ) : ℚ) :=
        localKummerAll_sqEq hbdual hd (hsq.symm heQ) hL
      have hcov_e : Cov ℚ (dualA ε m q) (dualB ε m q) ((e : ℤ) : ℚ) :=
        cov_sqEq one_ne_zero (dual_exhaustion hP hH' he hsf hLe) (cov_dual_one ε m q)
      exact cov_sqEq heQ hsq hcov_e
    · intro hcov
      rw [localKummerAll_iff_cov hbdual hd]
      exact ⟨cov_base_change hcov, fun p _ => cov_base_change hcov⟩
  -- the two set identities
  have hglob : ∀ a b : ℚ, (∀ d : ℚ, d ≠ 0 → (LocalKummerAll a b d ↔ Cov ℚ a b d)) →
      GlobalSet a b = SelmerSet a b := by
    intro a b hiff
    ext c
    constructor
    · rintro ⟨d, rfl, hcov⟩
      exact ⟨d, rfl, (hiff (d : ℚ) d.ne_zero).mpr hcov⟩
    · rintro ⟨d, rfl, hL⟩
      exact ⟨d, rfl, (hiff (d : ℚ) d.ne_zero).mp hL⟩
  refine ⟨hphi, hdual, hglob _ _ hphi, hglob _ _ hdual, ?_⟩
  -- the explicit descent quotient
  have hqcast : ((q : ℤ) : ℚ) = ((q : ℕ) : ℚ) := by push_cast; ring
  have hqprime : Prime ((q : ℤ)) := Nat.prime_iff_prime_int.mp hqp
  have hnsq_q : ¬ IsSquare ((q : ℤ)) := by
    refine not_isSquare_of_prime_dvd_once hqprime dvd_rfl ?_
    intro hc
    have h2 : ((q : ℤ)) ^ 2 ≤ (q : ℤ) := Int.le_of_dvd (by positivity) hc
    have hq2 : (2 : ℤ) ≤ (q : ℤ) := by exact_mod_cast hqp.two_le
    nlinarith
  have hnsq_Dq : ¬ IsSquare (DD ε m * (q : ℤ)) := by
    refine not_isSquare_of_prime_dvd_once hqprime ⟨DD ε m, by ring⟩ ?_
    rintro ⟨c, hc⟩
    refine q_not_dvd_D hP ⟨c, ?_⟩
    have : DD ε m * (q : ℤ) = ((q : ℤ) * c) * (q : ℤ) := by rw [hc]; ring
    exact mul_right_cancel₀ hq0 this
  have hnot : cls ((q : ℚ)) ∉ Subgroup.closure ({cls ((DD ε m : ℤ) : ℚ)} : Set Qsq) := by
    intro hmem
    rcases mem_closure_singleton_of_sq_eq_one (qsq_sq_eq_one _) hmem with h1 | h1
    · exact cls_ne_one_of_not_isSquare hq0 hnsq_q (by rw [hqcast]; exact h1)
    · refine cls_ne_cls_of_not_isSquare_mul hq0 hD0 ?_ (by rw [hqcast]; exact h1)
      rw [mul_comm]
      exact hnsq_Dq
  simpa only [KExp, GphiExp] using
    index_two_of_closure_pair (a := cls ((DD ε m : ℤ) : ℚ)) (b := cls ((q : ℚ)))
      (qsq_sq_eq_one _) hnot

end SDyadic
