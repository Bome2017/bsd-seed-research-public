/-
Run013 — `PhiSelmer.lean`

**LEVEL A, first half.**

    Sel^{phi_q}(E_q / Q) = {1, -31, q, -31 q}    for every q in F_62.

Orientation (`TARGET.md` §3): the `phi_q`-coverings are

    C^{(phi)}_{q,d} : n^2 = d u^4 + 30 q u^2 v^2 - (31 q^2 / d) v^4,

i.e. they are built from the coefficients `(a, b) = (30 q, -31 q^2)` of the *target*
curve `E'_q : y^2 = x^3 + 30 q x^2 - 31 q^2 x`.

The inclusion `⊆` is proved by
* the support reduction (`Support.lean`): every prime dividing a squarefree
  representative divides `b = -31 q^2`, hence lies in `{31, q}`;
* the `2`-adic condition (`LocalTwo.lean`): the class is `≡ 1 (mod 4)`.

The inclusion `⊇` is proved by exhibiting honest **rational** points on the four
coverings; these give local points at every place by base change.
-/
import RequestProject.Run013.Selmer
import RequestProject.Run013.Support
import RequestProject.Run013.Squareclasses
import RequestProject.Run013.LocalTwo
import RequestProject.Run013.Family

namespace Run013

variable {q : ℕ}

/-- The coefficient pair of `E'_q`, i.e. of the `phi_q`-descent. -/
def phiA (q : ℕ) : ℚ := 30 * q

/-- The coefficient pair of `E'_q`, i.e. of the `phi_q`-descent. -/
def phiB (q : ℕ) : ℚ := -31 * (q : ℚ) ^ 2

lemma phiB_ne_zero (hq : 0 < q) : phiB q ≠ 0 := by
  have : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  simp only [phiB]
  positivity

lemma phiA_intCast (q : ℕ) : phiA q = ((30 * (q : ℤ) : ℤ) : ℚ) := by
  simp [phiA]

lemma phiB_intCast (q : ℕ) : phiB q = ((-31 * (q : ℤ) ^ 2 : ℤ) : ℚ) := by
  simp [phiB]

/-! ## The four global points -/

lemma phi_cov_one : Cov ℚ (phiA q) (phiB q) 1 := by
  refine ⟨1, 0, 1, by simp, ?_⟩
  norm_num

lemma phi_cov_negthirtyone : Cov ℚ (phiA q) (phiB q) (-31) := by
  refine ⟨0, 1, (q : ℚ), by simp, ?_⟩
  simp only [phiA, phiB]
  norm_num

lemma phi_cov_q (hq : 0 < q) : Cov ℚ (phiA q) (phiB q) (q : ℚ) := by
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  refine ⟨1, 1, 0, by simp, ?_⟩
  simp only [phiA, phiB]
  field_simp
  ring

lemma phi_cov_negthirtyoneq (hq : 0 < q) : Cov ℚ (phiA q) (phiB q) (-(31 * (q : ℚ))) := by
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  refine ⟨1, 1, 0, by simp, ?_⟩
  simp only [phiA, phiB]
  field_simp
  ring

/-! ## The main theorem -/

/-- **Exact `phi_q`-Selmer group.**

For every `q` in the frozen family `F_62`,

    Sel^{phi_q}(E_q / Q) = {1, -31, q, -31 q}

as a subset of `Q*/Q*^2`. -/
theorem phi_selmer_eq_min (hq : F62min q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls (q : ℚ), cls (-(31 * (q : ℚ)))} := by
  haveI := hq.fact_prime
  have hqpos : 0 < q := hq.pos
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hqpos.ne'
  have hbne : phiB q ≠ 0 := phiB_ne_zero hqpos
  apply Set.eq_of_subset_of_subset
  · -- the hard inclusion
    rintro c ⟨d, rfl, hL⟩
    obtain ⟨D, hDsf, hsq⟩ := exists_squarefree_rep (d : ℚ) d.ne_zero
    have hDne0 : D ≠ 0 := hDsf.ne_zero
    have hDne : (D : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hDne0
    have hLD : LocalKummerAll (phiA q) (phiB q) (D : ℚ) :=
      localKummerAll_sqEq hbne d.ne_zero (SqEq.symm hDne hsq) hL
    obtain ⟨-, hcov⟩ := (localKummerAll_iff_cov hbne hDne).mp hLD
    -- rewrite the local conditions with integral coefficients
    have hcovZ : ∀ (r : ℕ) [Fact r.Prime],
        Cov ℚ_[r] (((30 * (q : ℤ) : ℤ)) : ℚ_[r]) (((-31 * (q : ℤ) ^ 2 : ℤ)) : ℚ_[r])
          ((D : ℤ) : ℚ_[r]) := by
      intro r _
      have := hcov r
      rw [phiA, phiB] at this
      convert this using 2 <;> push_cast <;> ring
    -- support reduction
    have hsupp := support_reduction (30 * (q : ℤ)) (-31 * (q : ℤ) ^ 2) D hDsf hcovZ
    have hprimes : ∀ r : ℕ, r.Prime → (r : ℤ) ∣ D → r = 31 ∨ r = q := by
      intro r hr hrD
      have hdvd := hsupp r hr hrD
      have hdvd' : (r : ℤ) ∣ (31 : ℤ) * (q : ℤ) * (q : ℤ) := by
        refine (dvd_neg).mp ?_
        refine Dvd.dvd.trans hdvd (dvd_of_eq ?_)
        ring
      have hrp : Prime (r : ℤ) := Nat.prime_iff_prime_int.mp hr
      rcases hrp.dvd_mul.mp hdvd' with h1 | h1
      · rcases hrp.dvd_mul.mp h1 with h2 | h2
        · left
          have : r ∣ 31 := by exact_mod_cast h2
          exact ((Nat.prime_dvd_prime_iff_eq hr (by norm_num)).mp this)
        · right
          have : r ∣ q := by exact_mod_cast h2
          exact ((Nat.prime_dvd_prime_iff_eq hr hq.prime).mp this)
      · right
        have : r ∣ q := by exact_mod_cast h1
        exact ((Nat.prime_dvd_prime_iff_eq hr hq.prime).mp this)
    have hclass := squarefree_int_classify hDsf (by norm_num : Nat.Prime 31) hq.prime hprimes
    -- `D` is odd
    have hDodd : ¬ (2 : ℤ) ∣ D := by
      intro h2
      have : (2 : ℕ) = 31 ∨ (2 : ℕ) = q := hprimes 2 Nat.prime_two (by exact_mod_cast h2)
      rcases this with h | h
      · exact absurd h (by norm_num)
      · exact hq.ne_two h.symm
    -- the `2`-adic condition
    have hD4 : D % 4 = 1 := by
      haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
      refine local2_phi q hq.mod_eight D hDodd ?_
      exact hcovZ 2
    have hq4 : (q : ℤ) % 4 = 1 := by
      have := hq.mod_four
      omega
    -- assemble
    have hclsD : qcl d = cls (D : ℚ) := by
      rw [cls_of_ne hDne]
      exact qcl_eq_of_sqEq (by simpa using hsq)
    rw [hclsD]
    rcases hclass with h | h | h | h | h | h | h | h <;> rw [h] at hD4 ⊢ <;>
      first
        | (exfalso; omega)
        | (push_cast; simp)
  · -- the four classes really are Selmer
    have h1 : cls (1 : ℚ) ∈ SelmerSet (phiA q) (phiB q) :=
      mem_selmerSet_cls_of_global hbne one_ne_zero (phi_cov_one)
    have h2 : cls (-31 : ℚ) ∈ SelmerSet (phiA q) (phiB q) :=
      mem_selmerSet_cls_of_global hbne (by norm_num) (phi_cov_negthirtyone)
    have h3 : cls (q : ℚ) ∈ SelmerSet (phiA q) (phiB q) :=
      mem_selmerSet_cls_of_global hbne hq0 (phi_cov_q hqpos)
    have h4 : cls (-(31 * (q : ℚ))) ∈ SelmerSet (phiA q) (phiB q) :=
      mem_selmerSet_cls_of_global hbne (by simpa using hq0) (phi_cov_negthirtyoneq hqpos)
    intro c hc
    rcases hc with rfl | rfl | rfl | rfl
    · exact h1
    · exact h2
    · exact h3
    · exact h4

/-- The audited statement of `TARGET.md` §4, preserved verbatim on the six-field family. -/
theorem phi_selmer_eq (hq : F62 q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls (q : ℚ), cls (-(31 * (q : ℚ)))} :=
  phi_selmer_eq_min hq.toMin

end Run013
