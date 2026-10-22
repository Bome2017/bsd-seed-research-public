/-
Run013 — `DualPhiSelmer.lean`

**LEVEL A, second half.**

    Sel^{hat phi_q}(E'_q / Q) = {1}    for every q in F_62.

Orientation (`TARGET.md` §3): the dual coverings are

    C^{(hat phi)}_{q,d} : n^2 = d u^4 - 15 q u^2 v^2 + (64 q^2 / d) v^4,

i.e. they are built from the coefficients `(a, b) = (-15 q, 64 q^2)` of the *target*
curve `E_q : y^2 = x^3 - 15 q x^2 + 64 q^2 x`.

The inclusion `⊆` is proved by
* the support reduction (`Support.lean`): the primes dividing a squarefree
  representative divide `b = 64 q^2`, hence lie in `{2, q}`;
* the archimedean condition (`LocalInfinity.lean`): the class is positive;
* the three exclusions at the moving prime `q` (`LocalQ.lean`), which use
  `(2/q) = -1` and `(-31/q) = -1`.
-/
import RequestProject.Run013.Selmer
import RequestProject.Run013.Support
import RequestProject.Run013.Squareclasses
import RequestProject.Run013.LocalInfinity
import RequestProject.Run013.LocalQ
import RequestProject.Run013.Family

namespace Run013

variable {q : ℕ}

/-- First coefficient of `E_q`, i.e. of the `hat phi_q`-descent. -/
def dualA (q : ℕ) : ℚ := -15 * q

/-- Second coefficient of `E_q`, i.e. of the `hat phi_q`-descent. -/
def dualB (q : ℕ) : ℚ := 64 * (q : ℚ) ^ 2

lemma dualB_ne_zero (hq : 0 < q) : dualB q ≠ 0 := by
  have : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  simp only [dualB]
  positivity

lemma dual_cov_one : Cov ℚ (dualA q) (dualB q) 1 := by
  refine ⟨1, 0, 1, by simp, ?_⟩
  norm_num

/-- **Exact dual `hat phi_q`-Selmer group.**

For every `q` in the frozen family `F_62`,

    Sel^{hat phi_q}(E'_q / Q) = {1}

as a subset of `Q*/Q*^2`. -/
theorem dual_phi_selmer_eq_min (hq : F62min q) :
    SelmerSet (dualA q) (dualB q) = {cls 1} := by
  haveI := hq.fact_prime
  have hqpos : 0 < q := hq.pos
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hqpos.ne'
  have hbne : dualB q ≠ 0 := dualB_ne_zero hqpos
  apply Set.eq_of_subset_of_subset
  · rintro c ⟨d, rfl, hL⟩
    obtain ⟨D, hDsf, hsq⟩ := exists_squarefree_rep (d : ℚ) d.ne_zero
    have hDne0 : D ≠ 0 := hDsf.ne_zero
    have hDne : (D : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hDne0
    have hLD : LocalKummerAll (dualA q) (dualB q) (D : ℚ) :=
      localKummerAll_sqEq hbne d.ne_zero (SqEq.symm hDne hsq) hL
    obtain ⟨hinf, hcov⟩ := (localKummerAll_iff_cov hbne hDne).mp hLD
    have hcovZ : ∀ (r : ℕ) [Fact r.Prime],
        Cov ℚ_[r] (((-15 * (q : ℤ) : ℤ)) : ℚ_[r]) (((64 * (q : ℤ) ^ 2 : ℤ)) : ℚ_[r])
          ((D : ℤ) : ℚ_[r]) := by
      intro r _
      have hr := hcov r
      rw [dualA, dualB] at hr
      convert hr using 2 <;> push_cast <;> ring
    -- support reduction: the primes dividing `D` lie in `{2, q}`
    have hsupp := support_reduction (-15 * (q : ℤ)) (64 * (q : ℤ) ^ 2) D hDsf hcovZ
    have hprimes : ∀ r : ℕ, r.Prime → (r : ℤ) ∣ D → r = 2 ∨ r = q := by
      intro r hr hrD
      have hdvd := hsupp r hr hrD
      have hrp : Prime (r : ℤ) := Nat.prime_iff_prime_int.mp hr
      have hdvd' : (r : ℤ) ∣ (2 : ℤ) ^ 6 * ((q : ℤ) * (q : ℤ)) := by
        refine Dvd.dvd.trans hdvd (dvd_of_eq ?_); ring
      rcases hrp.dvd_mul.mp hdvd' with h1 | h1
      · left
        have h2 : (r : ℤ) ∣ 2 := hrp.dvd_of_dvd_pow h1
        have : r ∣ 2 := by exact_mod_cast h2
        exact (Nat.prime_dvd_prime_iff_eq hr Nat.prime_two).mp this
      · right
        rcases hrp.dvd_mul.mp h1 with h2 | h2 <;>
          · have : r ∣ q := by exact_mod_cast h2
            exact (Nat.prime_dvd_prime_iff_eq hr hq.prime).mp this
    have hclass := squarefree_int_classify hDsf Nat.prime_two hq.prime hprimes
    -- archimedean condition: `D > 0`
    have hpos : 0 < D := by
      rcases lt_trichotomy D 0 with h | h | h
      · exfalso
        refine localinf_dual (q : ℝ) (by exact_mod_cast hqpos) (D : ℝ) (by exact_mod_cast h) ?_
        rw [dualA, dualB] at hinf
        convert hinf using 2 <;> push_cast <;> ring
      · exact absurd h hDne0
      · exact h
    -- exclusions at the moving prime `q`
    have hq2 := hq.not_isSquare_two
    have hq31 := hq.not_isSquare_neg_thirtyone
    have hne2 : D ≠ 2 := by
      rintro rfl
      exact localq_dual_two hq.ne_two hq2 (by simpa using hcovZ q)
    have hneq : D ≠ (q : ℤ) := by
      rintro rfl
      exact localq_dual_q hq31 (by simpa using hcovZ q)
    have hne2q : D ≠ 2 * (q : ℤ) := by
      rintro rfl
      exact localq_dual_twoq hq.ne_two hq31 (by simpa using hcovZ q)
    -- only `D = 1` survives
    have hD1 : D = 1 := by
      rcases hclass with h | h | h | h | h | h | h | h <;> subst h
      · rfl
      · omega
      · exact absurd rfl hne2
      · omega
      · exact absurd rfl hneq
      · exact absurd (by omega) hqpos.ne'
      · exact absurd (by push_cast; ring) hne2q
      · exfalso; have := hqpos; push_cast at hpos; omega
    have hclsD : qcl d = cls (D : ℚ) := by
      rw [cls_of_ne hDne]
      exact qcl_eq_of_sqEq (by simpa using hsq)
    rw [hclsD, hD1]
    simp
  · intro c hc
    rw [Set.mem_singleton_iff] at hc
    subst hc
    exact mem_selmerSet_cls_of_global hbne one_ne_zero dual_cov_one

/-- The audited statement of `TARGET.md` §4, preserved verbatim on the six-field family. -/
theorem dual_phi_selmer_eq (hq : F62 q) :
    SelmerSet (dualA q) (dualB q) = {cls 1} :=
  dual_phi_selmer_eq_min hq.toMin

end Run013
