module

public import Mathlib
public import RequestProject.Continuation.Frontier

/-!
# The auxiliary-prime lemma is where the weight sits

Lean source for `research_return/REVISION_7.md`.

`Frontier.TameCarrier` bundles two different statements:

* **(Law)** the cross-`p` law: at *every* admissible auxiliary `ℓ`,
  `Wd · C(p,ℓ) ≡ Wn · A(p,ℓ) · R(p,ℓ) · u (mod p)` for a `p`-unit `u`. Here `A = a_ℓ − 2`,
  `R` is the tame regulator, and `W = Wn / Wd` is one fixed rational number;
* **(Aux)** existence of a *nondegenerate* auxiliary: some admissible `ℓ` with
  `p ∤ A(p,ℓ)·R(p,ℓ)`.

This file separates them and proves the following.

* `tameCarrier_of_law_of_aux`: (Law) + (Aux) give `TameCarrier`, so with the one-way detector
  the support lies in `S₀ ∪ primeFactors(Wn)` (`support_subset_of_law_of_aux`).
* `degenerate_of_shaNonzero`: (Law) + the one-way detector + `Ш[p] ≠ 0` + `p ∤ Wn` force
  **every** admissible auxiliary to be degenerate. So (Aux) is false at every such `p`: no
  proof of (Aux) at `p` can avoid proving `Ш[p] = 0` (given (Law) and the detector).
* `support_subset_degenerate`: the support lies in `S₀ ∪ primeFactors(Wn) ∪ Deg`, where
  `Deg = {p | every admissible ℓ is degenerate}` depends only on `A` and `R`.
* `degenerate_subset_support`: with the two-way detector (`Ш[p] = 0 ⇒ some admissible ℓ has
  p ∤ C(p,ℓ)`), `Deg ⊆ S₀ ∪ primeFactors(Wd) ∪ support`.
* `support_finite_iff_degenerate_finite`: under (Law) and the two-way detector, FIN is
  *equivalent* to finiteness of `Deg`. The cofinite form of (Aux) is FIN, restated as a statement
  about the Mordell–Weil tame regulators and point counts only.
* `support_subset_of_law_288`: route B (`W = 8q`, denominator `≤ 21`, hence `W = 288`) still
  leaves `Deg`: the support is only confined to `S₀ ∪ {2, 3} ∪ Deg`.
* `exists_sl2_trace_ne_two`, `card_trace_two_sl2`: the group-theoretic input for the
  `a_ℓ − 2` factor. For an odd prime `p`, `SL₂(𝔽_p)` contains elements of trace `≠ 2`. Exactly
  `p²` of its `p(p² − 1)` elements have trace `2`. With an open-image theorem and Chebotarev
  (both imported, not formalized), the primes `ℓ ≡ 1 (mod p)` with `a_ℓ ≢ 2` therefore have
  relative density `1 − p/(p² − 1) > 0`. This factor of (Aux) is free of `Ш`; the regulator
  factor is not.

As elsewhere, `Ш[p] ≠ 0` is an abstract predicate and every arithmetic input is a hypothesis.
-/

@[expose] public section

namespace AuxiliaryPrime

open Frontier

/-- **(Law)** The cross-`p` law at every admissible auxiliary, outside `S₀`. -/
def TameLaw (C A R : ℕ → ℕ → ℤ) (adm : ℕ → ℕ → Prop) (Wn Wd : ℤ) (S₀ : Set ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∉ S₀ → ∀ ℓ : ℕ, adm p ℓ →
    ∃ u : ℤ, ¬ (p : ℤ) ∣ u ∧ (p : ℤ) ∣ Wd * C p ℓ - Wn * A p ℓ * R p ℓ * u

/-- An admissible auxiliary `ℓ` is *nondegenerate* at `p` if `p ∤ (a_ℓ − 2)·R(p,ℓ)`. -/
def Nondegenerate (A R : ℕ → ℕ → ℤ) (p ℓ : ℕ) : Prop := ¬ (p : ℤ) ∣ A p ℓ * R p ℓ

/-- **(Aux)** Outside `S₀`, every prime has a nondegenerate admissible auxiliary. -/
def AuxExists (A R : ℕ → ℕ → ℤ) (adm : ℕ → ℕ → Prop) (S₀ : Set ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∉ S₀ → ∃ ℓ : ℕ, adm p ℓ ∧ Nondegenerate A R p ℓ

/-- The totally degenerate primes: every admissible auxiliary is degenerate. This set is
defined from `a_ℓ − 2` and the tame regulators only. -/
def Deg (A R : ℕ → ℕ → ℤ) (adm : ℕ → ℕ → Prop) : Set ℕ :=
  {p : ℕ | p.Prime ∧ ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ A p ℓ * R p ℓ}

/-- The bad-prime support. -/
def Supp (shaNonzero : ℕ → Prop) : Set ℕ := {p : ℕ | p.Prime ∧ shaNonzero p}

lemma not_dvd_mul_iff {p : ℕ} (hp : p.Prime) {x y : ℤ} :
    ¬ (p : ℤ) ∣ x * y ↔ ¬ (p : ℤ) ∣ x ∧ ¬ (p : ℤ) ∣ y := by
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  constructor
  · intro h
    exact ⟨fun hx => h (dvd_mul_of_dvd_left hx y), fun hy => h (dvd_mul_of_dvd_right hy x)⟩
  · rintro ⟨hx, hy⟩ h
    rcases hpZ.dvd_or_dvd h with h' | h'
    · exact hx h'
    · exact hy h'

/-- (Law) + (Aux) give the bundled carrier of `Frontier`. -/
theorem tameCarrier_of_law_of_aux {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (hlaw : TameLaw C A R adm Wn Wd S₀) (haux : AuxExists A R adm S₀) :
    TameCarrier C A R adm Wn Wd S₀ := by
  intro p hp hpS
  obtain ⟨ℓ, hadm, hnd⟩ := haux p hp hpS
  obtain ⟨hA, hR⟩ := (not_dvd_mul_iff hp).mp hnd
  exact ⟨ℓ, hadm, hA, hR, hlaw p hp hpS ℓ hadm⟩

/-- (Law) + (Aux) + one-way detector: the support lies in `S₀ ∪ primeFactors(Wn)`. -/
theorem support_subset_of_law_of_aux {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hWn : Wn ≠ 0) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (haux : AuxExists A R adm S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    Supp shaNonzero ⊆ S₀ ∪ (Wn.natAbs.primeFactors : Set ℕ) :=
  support_subset_of_tameCarrier shaNonzero hWn (tameCarrier_of_law_of_aux hlaw haux) hdet

/-- **(Aux) fails at every bad prime not dividing `Wn`.** Under (Law) and the one-way detector,
`Ш[p] ≠ 0` and `p ∤ Wn` force `p ∣ (a_ℓ − 2)·R(p,ℓ)` at every admissible `ℓ`. -/
theorem degenerate_of_shaNonzero {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ)
    {p : ℕ} (hp : p.Prime) (hpS : p ∉ S₀) (hs : shaNonzero p) (hWn : ¬ (p : ℤ) ∣ Wn) :
    ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ A p ℓ * R p ℓ := by
  intro ℓ hadm
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  obtain ⟨u, hu, hdiv⟩ := hlaw p hp hpS ℓ hadm
  have h1 : (p : ℤ) ∣ Wd * C p ℓ := dvd_mul_of_dvd_right (hdet p hp hpS hs ℓ hadm) Wd
  have h2 : (p : ℤ) ∣ Wn * (A p ℓ * R p ℓ) * u := by
    have := dvd_sub h1 hdiv
    simp only [sub_sub_cancel] at this
    simpa [mul_assoc] using this
  rcases hpZ.dvd_or_dvd h2 with h3 | h3
  · rcases hpZ.dvd_or_dvd h3 with h4 | h4
    · exact absurd h4 hWn
    · exact h4
  · exact absurd h3 hu

/-- So a nondegenerate auxiliary at a prime `p ∤ Wn` (outside `S₀`) proves `Ш[p] = 0`. -/
theorem sha_zero_of_nondegenerate {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ)
    {p ℓ : ℕ} (hp : p.Prime) (hpS : p ∉ S₀) (hWn : ¬ (p : ℤ) ∣ Wn) (hadm : adm p ℓ)
    (hnd : Nondegenerate A R p ℓ) : ¬ shaNonzero p := fun hs =>
  hnd (degenerate_of_shaNonzero shaNonzero hlaw hdet hp hpS hs hWn ℓ hadm)

/-- **Support ⊆ `S₀ ∪ primeFactors(Wn) ∪ Deg`** (one-way detector). -/
theorem support_subset_degenerate {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    Supp shaNonzero ⊆ S₀ ∪ {p : ℕ | (p : ℤ) ∣ Wn} ∪ Deg A R adm := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl (Or.inl hpS)
  by_cases hW : (p : ℤ) ∣ Wn
  · exact Or.inl (Or.inr hW)
  exact Or.inr ⟨hp, degenerate_of_shaNonzero shaNonzero hlaw hdet hp hpS hs hW⟩

/-- **`Deg ⊆ S₀ ∪ primeFactors(Wd) ∪ support`** under (Law) and the *two-way* detector
"`Ш[p] = 0 ⇒` some admissible `ℓ` has `p ∤ C(p,ℓ)`". -/
theorem degenerate_subset_support {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (hconv : ∀ p : ℕ, p.Prime → p ∉ S₀ → ¬ shaNonzero p →
      ∃ ℓ : ℕ, adm p ℓ ∧ ¬ (p : ℤ) ∣ C p ℓ) :
    Deg A R adm ⊆ S₀ ∪ {p : ℕ | (p : ℤ) ∣ Wd} ∪ Supp shaNonzero := by
  rintro p ⟨hp, hdeg⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl (Or.inl hpS)
  by_cases hW : (p : ℤ) ∣ Wd
  · exact Or.inl (Or.inr hW)
  by_cases hs : shaNonzero p
  · exact Or.inr ⟨hp, hs⟩
  exfalso
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  obtain ⟨ℓ, hadm, hC⟩ := hconv p hp hpS hs
  obtain ⟨u, -, hdiv⟩ := hlaw p hp hpS ℓ hadm
  have h1 : (p : ℤ) ∣ Wn * A p ℓ * R p ℓ * u := by
    have := hdeg ℓ hadm
    exact Dvd.dvd.mul_right (by simpa [mul_assoc] using dvd_mul_of_dvd_right this Wn) u
  have h2 : (p : ℤ) ∣ Wd * C p ℓ := by simpa using dvd_add hdiv h1
  rcases hpZ.dvd_or_dvd h2 with h3 | h3
  · exact hW h3
  · exact hC h3

lemma finite_primes_dvd {W : ℤ} (hW : W ≠ 0) : {p : ℕ | (p : ℤ) ∣ W ∧ p.Prime}.Finite := by
  refine (Finset.finite_toSet W.natAbs.primeFactors).subset ?_
  rintro p ⟨hd, hp⟩
  simp only [Finset.mem_coe, Nat.mem_primeFactors]
  exact ⟨hp, Int.natCast_dvd.mp hd, by simpa using hW⟩

/-- **FIN ⇔ finiteness of the totally degenerate set.** Under (Law) with `Wn, Wd ≠ 0` and the
two-way detector, the bad-prime support is finite iff `Deg` is finite. -/
theorem support_finite_iff_degenerate_finite {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop}
    {Wn Wd : ℤ} {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hS₀ : S₀.Finite) (hWn : Wn ≠ 0)
    (hWd : Wd ≠ 0) (hlaw : TameLaw C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ)
    (hconv : ∀ p : ℕ, p.Prime → p ∉ S₀ → ¬ shaNonzero p →
      ∃ ℓ : ℕ, adm p ℓ ∧ ¬ (p : ℤ) ∣ C p ℓ) :
    (Supp shaNonzero).Finite ↔ (Deg A R adm).Finite := by
  constructor
  · intro hS
    refine ((hS₀.union (finite_primes_dvd hWd)).union hS).subset ?_
    intro p hp
    have hpp : p.Prime := hp.1
    rcases degenerate_subset_support shaNonzero hlaw hconv hp with (h | h) | h
    · exact Or.inl (Or.inl h)
    · exact Or.inl (Or.inr ⟨h, hpp⟩)
    · exact Or.inr h
  · intro hD
    refine ((hS₀.union (finite_primes_dvd hWn)).union hD).subset ?_
    intro p hp
    have hpp : p.Prime := hp.1
    rcases support_subset_degenerate shaNonzero hlaw hdet hp with (h | h) | h
    · exact Or.inl (Or.inl h)
    · exact Or.inl (Or.inr ⟨h, hpp⟩)
    · exact Or.inr h

/-- **Route B still needs (Aux).** With `W = 288` (as forced by `W = 8q` plus denominator `≤ 21`,
`TameScalar.eq_288_of_mem_lattice`), (Law) and the one-way detector confine the support to
`S₀ ∪ {2, 3} ∪ Deg`, and no further: the totally degenerate set is not removed by knowing `W`. -/
theorem support_subset_of_law_288 {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {S₀ : Set ℕ}
    (shaNonzero : ℕ → Prop) (hlaw : TameLaw C A R adm 288 1 S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    Supp shaNonzero ⊆ S₀ ∪ {2, 3} ∪ Deg A R adm := by
  intro p hp
  have hpp : p.Prime := hp.1
  rcases support_subset_degenerate shaNonzero hlaw hdet hp with (h | h) | h
  · exact Or.inl (Or.inl h)
  · left; right
    have h' : p ∣ 288 := Int.natCast_dvd_natCast.mp (by simpa using h)
    have : p ∈ (288 : ℕ).primeFactors := Nat.mem_primeFactors.mpr ⟨hpp, h', by norm_num⟩
    rw [primeFactors_288] at this
    simpa using this
  · exact Or.inr h

/-! ## The `a_ℓ − 2` factor: group theory for Chebotarev -/

/-- For an odd prime `p`, the rotation `!![0, -1; 1, 0] ∈ SL₂(𝔽_p)` has trace `0 ≠ 2`. -/
theorem exists_sl2_trace_ne_two {p : ℕ} [Fact p.Prime] (hp : p ≠ 2) :
    ∃ g : Matrix.SpecialLinearGroup (Fin 2) (ZMod p), (g : Matrix (Fin 2) (Fin 2) (ZMod p)).trace ≠ 2 := by
  refine ⟨⟨!![0, -1; 1, 0], by simp [Matrix.det_fin_two]⟩, ?_⟩
  simp only [Matrix.trace_fin_two_of]
  intro h
  have h2 : ((2 : ℕ) : ZMod p) = 0 := by push_cast; simpa using h.symm
  rw [ZMod.natCast_eq_zero_iff] at h2
  exact hp ((Nat.prime_dvd_prime_iff_eq (Fact.out) Nat.prime_two).mp h2)

section Count

variable {F : Type*} [Field F] [Fintype F] [DecidableEq F]

lemma card_mul_eq_ne_zero {k : F} (hk : k ≠ 0) :
    (Finset.univ.filter (fun x : F × F => x.1 * x.2 = k)).card = Fintype.card F - 1 := by
  have : (Finset.univ.filter (fun x : F × F => x.1 * x.2 = k)) =
      (Finset.univ.filter (fun b : F => b ≠ 0)).image (fun b => (b, k / b)) := by
    ext ⟨b, c⟩
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image, Prod.mk.injEq]
    constructor
    · intro h
      have hb : b ≠ 0 := by rintro rfl; simp at h; exact hk h.symm
      exact ⟨b, hb, rfl, by field_simp; rw [← h]⟩
    · rintro ⟨b', hb', rfl, rfl⟩
      field_simp
  rw [this, Finset.card_image_of_injective _ (fun a b h => by simpa using congrArg Prod.fst h),
    Finset.filter_ne', Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ]

lemma card_mul_eq_zero :
    (Finset.univ.filter (fun x : F × F => x.1 * x.2 = 0)).card = 2 * Fintype.card F - 1 := by
  have : (Finset.univ.filter (fun x : F × F => x.1 * x.2 = 0)) =
      (Finset.univ.filter (fun x : F × F => x.1 = 0)) ∪
        (Finset.univ.filter (fun x : F × F => x.2 = 0)) := by
    ext x; simp [mul_eq_zero]
  rw [this, Finset.card_union]
  have h1 : (Finset.univ.filter (fun x : F × F => x.1 = 0)).card = Fintype.card F := by
    rw [show (Finset.univ.filter (fun x : F × F => x.1 = 0)) = ({0} : Finset F) ×ˢ Finset.univ by
      ext ⟨a, b⟩; simp [eq_comm]]
    simp
  have h2 : (Finset.univ.filter (fun x : F × F => x.2 = 0)).card = Fintype.card F := by
    rw [show (Finset.univ.filter (fun x : F × F => x.2 = 0)) = Finset.univ ×ˢ ({0} : Finset F) by
      ext ⟨a, b⟩; simp [eq_comm]]
    simp
  have h3 : (Finset.univ.filter (fun x : F × F => x.1 = 0)) ∩
      (Finset.univ.filter (fun x : F × F => x.2 = 0)) = {(0, 0)} := by
    ext ⟨a, b⟩; simp
  rw [h1, h2, h3]; simp; omega

lemma card_triple :
    (Finset.univ.filter (fun x : F × F × F => x.2.1 * x.2.2 = -(x.1 - 1) ^ 2)).card =
      Fintype.card F ^ 2 := by
  rw [Finset.card_filter, Fintype.sum_prod_type]
  simp_rw [← Finset.card_filter]
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ (1 : F))]
  simp only [sub_self, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, neg_zero]
  rw [card_mul_eq_zero, Finset.sum_congr rfl (g := fun _ => Fintype.card F - 1)]
  · rw [Finset.sum_const, Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ,
      smul_eq_mul]
    have h1 : 1 ≤ Fintype.card F := Fintype.card_pos
    zify [h1, show 1 ≤ 2 * Fintype.card F by omega]
    ring
  · intro a ha
    apply card_mul_eq_ne_zero
    have : a - 1 ≠ 0 := sub_ne_zero.mpr (Finset.ne_of_mem_erase ha)
    simpa using this

lemma card_trace_two_eq_card_triple :
    (Finset.univ.filter (fun M : Matrix (Fin 2) (Fin 2) F => M.det = 1 ∧ M.trace = 2)).card =
      (Finset.univ.filter (fun x : F × F × F => x.2.1 * x.2.2 = -(x.1 - 1) ^ 2)).card := by
  refine Finset.card_bij (fun M _ => (M 0 0, M 0 1, M 1 0)) ?_ ?_ ?_
  · intro M hM
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Matrix.det_fin_two,
      Matrix.trace_fin_two] at hM ⊢
    have : M 1 1 = 2 - M 0 0 := by linear_combination hM.2
    rw [this] at hM; linear_combination -hM.1
  · intro M hM N hN h
    simp only [Prod.mk.injEq] at h
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Matrix.trace_fin_two] at hM hN
    ext i j; fin_cases i <;> fin_cases j
    · exact h.1
    · exact h.2.1
    · exact h.2.2
    · simp; linear_combination hM.2 - hN.2 - h.1
  · intro x hx
    refine ⟨!![x.1, x.2.1; x.2.2, 2 - x.1], ?_, rfl⟩
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Matrix.det_fin_two_of,
      Matrix.trace_fin_two_of] at hx ⊢
    constructor
    · linear_combination -hx
    · ring

/-- **Trace-two elements of `SL₂(𝔽_q)`.** Exactly `q²` matrices over a finite field `𝔽_q` have
determinant `1` and trace `2` (the identity and the `q² − 1` nontrivial unipotents). Since
`#SL₂(𝔽_q) = q(q² − 1)`, a Chebotarev-random Frobenius in `SL₂` has `a_ℓ ≡ 2` with probability
`q/(q² − 1)`. -/
theorem card_trace_two_sl2 :
    (Finset.univ.filter (fun M : Matrix (Fin 2) (Fin 2) F => M.det = 1 ∧ M.trace = 2)).card =
      Fintype.card F ^ 2 := by
  rw [card_trace_two_eq_card_triple, card_triple]

end Count

end AuxiliaryPrime

end
