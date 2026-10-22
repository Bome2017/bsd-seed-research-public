import PrimarySupport.Primary

/-!
# A2 — stretch target S3: the torsion example `⨁_{p ≠ 2,5} (ZMod p)²`

It is torsion, has zero 2- and 5-parts, 3-part of order 9, every primary part finite of square
order, infinitely many nonzero primary parts, and it is infinite.
-/

namespace PrimarySupport

/-- Index set of the example: the primes other than `2` and `5`. -/
abbrev CIdx : Type := {p : ℕ | p.Prime ∧ p ≠ 2 ∧ p ≠ 5}

/-- Codex's torsion example `⨁_{p ≠ 2,5} (ZMod p)²`. -/
abbrev CG : Type := Π₀ p : CIdx, ZMod (p : ℕ) × ZMod (p : ℕ)

lemma zmod_sq_nsmul {m n : ℕ} (h : m ∣ n) (a : ZMod m × ZMod m) : n • a = 0 := by
  obtain ⟨c, rfl⟩ := h
  have hz : ∀ b : ZMod m, (m * c) • b = 0 := by
    intro b
    rw [nsmul_eq_mul]
    push_cast
    rw [ZMod.natCast_self, zero_mul, zero_mul]
  exact Prod.ext (by simp) (by simp)

lemma cg_isTorsion : AddMonoid.IsTorsion CG := by
  intro x
  rw [isOfFinAddOrder_iff_nsmul_eq_zero]
  refine ⟨∏ q ∈ x.support, (q : ℕ), Finset.prod_pos fun q _ => (q : CIdx).2.1.pos, ?_⟩
  refine DFinsupp.ext fun q => ?_
  rw [DFinsupp.smul_apply, DFinsupp.zero_apply]
  by_cases hq : q ∈ x.support
  · exact zmod_sq_nsmul (Finset.dvd_prod_of_mem (fun r : CIdx => (r : ℕ)) hq) (x q)
  · rw [DFinsupp.notMem_support_iff.mp hq, smul_zero]

/-- Off the prime `p`, an element of the `p`-primary part vanishes. -/
lemma cg_apply_eq_zero_of_mem_primary {p : ℕ} (hp : p.Prime) {x : CG}
    (hx : x ∈ primaryPart CG p) (q : CIdx) (hq : (q : ℕ) ≠ p) : x q = 0 := by
  obtain ⟨k, hk⟩ := hx
  have hkq : (p ^ k) • (x q) = 0 := by
    have h := congrArg (fun y : CG => y q) hk
    simpa using h
  haveI : Fact ((q : ℕ)).Prime := ⟨(q : CIdx).2.1⟩
  have hne : ((p ^ k : ℕ) : ZMod (q : ℕ)) ≠ 0 := by
    rw [Ne, ZMod.natCast_eq_zero_iff]
    intro hdvd
    exact hq ((Nat.prime_dvd_prime_iff_eq (q : CIdx).2.1 hp).mp
      (Nat.Prime.dvd_of_dvd_pow (q : CIdx).2.1 hdvd))
  have hfst : ((p ^ k : ℕ) : ZMod (q : ℕ)) * (x q).1 = 0 := by
    rw [← nsmul_eq_mul]
    exact congrArg Prod.fst hkq
  have hsnd : ((p ^ k : ℕ) : ZMod (q : ℕ)) * (x q).2 = 0 := by
    rw [← nsmul_eq_mul]
    exact congrArg Prod.snd hkq
  refine Prod.ext ?_ ?_
  · rcases mul_eq_zero.mp hfst with h | h
    · exact absurd h hne
    · exact h
  · rcases mul_eq_zero.mp hsnd with h | h
    · exact absurd h hne
    · exact h

/-- Primes outside the index set have trivial primary part. -/
lemma cg_primary_eq_bot {p : ℕ} (hp : p.Prime) (hidx : p = 2 ∨ p = 5) :
    primaryPart CG p = ⊥ := by
  rw [AddSubgroup.eq_bot_iff_forall]
  intro x hx
  refine DFinsupp.ext fun q => ?_
  have hq : (q : ℕ) ≠ p := by
    rcases hidx with rfl | rfl
    · exact (q : CIdx).2.2.1
    · exact (q : CIdx).2.2.2
  rw [cg_apply_eq_zero_of_mem_primary hp hx q hq, DFinsupp.zero_apply]

/-- A single supported at an index prime lies in the corresponding primary part. -/
lemma cg_single_mem_primary (q : CIdx) (a : ZMod (q : ℕ) × ZMod (q : ℕ)) :
    (DFinsupp.single q a : CG) ∈ primaryPart CG (q : ℕ) := by
  refine ⟨1, DFinsupp.ext fun r => ?_⟩
  rw [DFinsupp.smul_apply, DFinsupp.zero_apply, pow_one]
  by_cases hr : r = q
  · subst hr
    rw [DFinsupp.single_eq_same]
    exact zmod_sq_nsmul dvd_rfl a
  · rw [DFinsupp.single_eq_of_ne hr, smul_zero]

/-- At an index prime, the primary part is a copy of `(ZMod p)²`. -/
def cgPrimaryEquiv (q : CIdx) :
    (primaryPart CG (q : ℕ)) ≃ (ZMod (q : ℕ) × ZMod (q : ℕ)) where
  toFun x := (x : CG) q
  invFun a := ⟨DFinsupp.single q a, cg_single_mem_primary q a⟩
  left_inv := by
    rintro ⟨x, hx⟩
    refine Subtype.ext (DFinsupp.ext fun r => ?_)
    by_cases hr : r = q
    · subst hr
      exact DFinsupp.single_eq_same
    · have hrq : (r : ℕ) ≠ (q : ℕ) := fun h => hr (Subtype.ext h)
      rw [DFinsupp.single_eq_of_ne hr, cg_apply_eq_zero_of_mem_primary (q : CIdx).2.1 hx r hrq]
  right_inv a := DFinsupp.single_eq_same

lemma cg_card_primary (q : CIdx) :
    Nat.card (primaryPart CG (q : ℕ)) = (q : ℕ) * (q : ℕ) := by
  haveI : NeZero ((q : ℕ)) := ⟨(q : CIdx).2.1.pos.ne'⟩
  rw [Nat.card_congr (cgPrimaryEquiv q)]
  simp

lemma cg_primary_finite {p : ℕ} (hp : p.Prime) : (primaryPart CG p : Set CG).Finite := by
  by_cases hidx : p = 2 ∨ p = 5
  · rw [cg_primary_eq_bot hp hidx, AddSubgroup.coe_bot]
    exact Set.finite_singleton 0
  · push_neg at hidx
    let q : CIdx := ⟨p, hp, hidx.1, hidx.2⟩
    haveI : NeZero p := ⟨hp.pos.ne'⟩
    haveI : Finite (primaryPart CG p) := Finite.of_equiv _ (cgPrimaryEquiv q).symm
    exact Set.toFinite _

lemma cg_primary_isSquare {p : ℕ} (hp : p.Prime) : IsSquare (Nat.card (primaryPart CG p)) := by
  by_cases hidx : p = 2 ∨ p = 5
  · rw [cg_primary_eq_bot hp hidx, AddSubgroup.card_bot]
    exact ⟨1, by norm_num⟩
  · push_neg at hidx
    exact ⟨p, cg_card_primary ⟨p, hp, hidx.1, hidx.2⟩⟩

lemma cg_card_primary_three : Nat.card (primaryPart CG 3) = 9 := by
  have h := cg_card_primary ⟨3, by norm_num, by norm_num, by norm_num⟩
  norm_num at h
  exact h

lemma cg_primary_ne_bot {p : ℕ} (hp : p.Prime) (h2 : p ≠ 2) (h5 : p ≠ 5) :
    primaryPart CG p ≠ ⊥ := by
  haveI : NeZero p := ⟨hp.pos.ne'⟩
  haveI : Fact p.Prime := ⟨hp⟩
  intro hbot
  have hmem := cg_single_mem_primary ⟨p, hp, h2, h5⟩ ((1 : ZMod p), (0 : ZMod p))
  rw [hbot] at hmem
  have h0 : (DFinsupp.single (⟨p, hp, h2, h5⟩ : CIdx) ((1 : ZMod p), (0 : ZMod p)) : CG) = 0 := hmem
  have h1 := congrArg (fun y : CG => y ⟨p, hp, h2, h5⟩) h0
  simp only [DFinsupp.zero_apply] at h1
  rw [DFinsupp.single_eq_same] at h1
  exact one_ne_zero (congrArg Prod.fst h1)

lemma cg_support_infinite : {p : ℕ | p.Prime ∧ primaryPart CG p ≠ ⊥}.Infinite := by
  have hsub : {p : ℕ | p.Prime} \ {2, 5} ⊆ {p : ℕ | p.Prime ∧ primaryPart CG p ≠ ⊥} := by
    rintro p ⟨hp, hns⟩
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hns
    exact ⟨hp, cg_primary_ne_bot hp hns.1 hns.2⟩
  exact Set.Infinite.mono hsub (Set.Infinite.diff Nat.infinite_setOf_prime (Set.toFinite _))

lemma cg_not_finite : ¬ Finite CG := by
  have hidx : ({p : ℕ | p.Prime ∧ p ≠ 2 ∧ p ≠ 5}).Infinite := by
    refine Set.Infinite.mono ?_ (Set.Infinite.diff Nat.infinite_setOf_prime
      (Set.toFinite ({2, 5} : Set ℕ)))
    rintro p ⟨hp, hns⟩
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hns
    exact ⟨hp, hns.1, hns.2⟩
  haveI : Infinite CIdx := Set.infinite_coe_iff.mpr hidx
  have hinj : Function.Injective
      (fun q : CIdx => (DFinsupp.single q ((1 : ZMod (q : ℕ)), (0 : ZMod (q : ℕ))) : CG)) := by
    intro q r hqr
    by_contra hne
    haveI : Fact ((q : ℕ)).Prime := ⟨(q : CIdx).2.1⟩
    have h : (DFinsupp.single q ((1 : ZMod (q : ℕ)), (0 : ZMod (q : ℕ))) : CG) q
        = (DFinsupp.single r ((1 : ZMod (r : ℕ)), (0 : ZMod (r : ℕ))) : CG) q :=
      congrArg (fun y : CG => y q) hqr
    rw [DFinsupp.single_eq_same, DFinsupp.single_eq_of_ne hne] at h
    exact one_ne_zero (congrArg Prod.fst h)
  intro hfin
  exact (Infinite.of_injective _ hinj).not_finite hfin

end PrimarySupport
