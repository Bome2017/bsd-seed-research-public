import Mathlib
import Coinvariant.TameCarrier

/-!
# The circularity wall for `W`, and the nondegenerate-`ℓ` lemma

Abstract logic for the tame route after the K288 batch. Nothing here is a statement about the
curve unless explicitly said; the arithmetic inputs appear as hypotheses.

## Part A: the circularity wall
If the global scalar is *defined* as `W = K · #Ш` (the refined Mazur–Tate/BKS-type constant,
`K = 32` for this seed), then `Ш[p] ≠ 0 ⇒ p ∣ W` holds for **every** prime `p` by Cauchy's
theorem alone, with no tame input at all (`circular_W_detects`, `circular_template_tautology`).
So such a `W` cannot be the source of FIN; and `W = 288` is then literally `#Ш = 9`
(`circular_W_eq_288_iff`).

## Part B: the nondegenerate auxiliary prime
* `det_one_sub_fin_two`, `trace_eq_two_iff_det_one_sub_eq_zero`: for `g ∈ GL₂` with `det g = 1`
  (Frobenius at `ℓ ≡ 1 mod p`), `a_ℓ ≡ 2` iff `det(1 - g) = 0` iff `g` has a fixed vector
  (`trace_eq_two_iff_fixed_vector`), i.e. `p ∣ #E(𝔽_ℓ)`-type degeneracy.
* `traceTwoCount_eq`: in `SL₂(𝔽_p)` exactly `p²` elements have trace `2`, for every prime `p`
  (general proof, `traceTwo_card` over any finite field); `slTwoCount_eq` checks
  `|SL₂(𝔽_p)| = p(p² - 1)` for `p = 5, 7, …, 47` by computation. So under full image and Chebotarev, the
  `a_ℓ ≡ 2` locus among `ℓ ≡ 1 (mod p)` has relative density `p/(p² - 1)`.
* `exists_nondegenerate_of_card`: the counting form of target 2: if, among a finite set of
  admissible `ℓ`, fewer than `|Λ| - |{a_ℓ ≡ 2}|` have `R_{p,ℓ} ≡ 0`, a nondegenerate `ℓ` exists.
* `nondegenerate_forces_good` / `degenerate_everywhere_of_bad`: if the identity holds at *every*
  admissible `ℓ` (`ℓ`-independence) and `p ∤ W`, then at a bad prime **every** admissible `ℓ` is
  degenerate. So target 2 at a prime `p ∤ W` is, given the identity and the Ota bridge, as strong
  as `Ш[p] = 0`: it must be proved from the definition of `R_{p,ℓ}`, not from `Ш`.
-/

namespace TameCircularity

open Matrix

/-! ## Part A: the circularity wall -/

/-- **Cauchy step.** If a finite abelian group has a nonzero element killed by the prime `p`,
then `p` divides its order. -/
theorem prime_dvd_card_of_torsion {G : Type*} [AddCommGroup G] [Finite G] (p : ℕ)
    (hp : p.Prime) (h : ∃ x : G, x ≠ 0 ∧ p • x = 0) : p ∣ Nat.card G := by
  obtain ⟨x, hx0, hpx⟩ := h
  have hord : addOrderOf x = p := by
    haveI := Fact.mk hp
    exact addOrderOf_eq_prime hpx hx0
  rw [← hord]
  exact addOrderOf_dvd_natCard x

/-- **The circularity wall.** If `W := K · #Ш` (any integer `K`), then `Ш[p] ≠ 0 ⇒ p ∣ W` holds
for every prime `p`, for purely group-theoretic reasons. No tame quantity, no auxiliary `ℓ`, no
identity `C_2 = (a_ℓ - 2) R W u` is used. -/
theorem circular_W_detects {Sha : Type*} [AddCommGroup Sha] [Finite Sha] (K : ℤ) (p : ℕ)
    (hp : p.Prime) (h : ∃ x : Sha, x ≠ 0 ∧ p • x = 0) :
    (p : ℤ) ∣ K * (Nat.card Sha : ℤ) :=
  Dvd.dvd.mul_left (Int.natCast_dvd_natCast.mpr (prime_dvd_card_of_torsion p hp h)) K

/-- **The tail template is a tautology for the circular `W`.** The conclusion of
`TameCarrier.tame_bad_primes_dvd_W` for `W = K · #Ш` (every bad prime divides `W`) holds outright;
all tame hypotheses of that template are idle for this `W`. -/
theorem circular_template_tautology {Sha : Type*} [AddCommGroup Sha] [Finite Sha] (K : ℤ) :
    ∀ p : ℕ, p.Prime → (∃ x : Sha, x ≠ 0 ∧ p • x = 0) → (p : ℤ) ∣ K * (Nat.card Sha : ℤ) :=
  fun p hp h => circular_W_detects K p hp h

/-- **With `K = 32`, `W = 288` is exactly `#Ш = 9`.** So proving `W = 288` for the circular `W`
is the statement `#Ш = 9` itself. -/
theorem circular_W_eq_288_iff (n : ℕ) : (32 : ℤ) * n = 288 ↔ n = 9 := by
  constructor
  · intro h; omega
  · rintro rfl; norm_num

/-- **What the nine residues say under the circular explanation (consistency only).** If
`W = 32 n` with `n = #Ш` is `≡ 288` modulo each of the nine primes `17, …, 47` and
`32 n < M - 288`, then `n = 9`. This is a consistency check of the data with `#Ш = 9`; it cannot
be used to prove `#Ш = 9`, since the identity with this `W` already presupposes `#Ш`. -/
theorem circular_nine_residues (n : ℕ) (hsize : (32 : ℤ) * n < 20475850236047 - 288)
    (h : ∀ p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℤ),
      (32 : ℤ) * n ≡ 288 [ZMOD p]) : n = 9 := by
  have habs : |(32 : ℤ) * n| < 20475850236047 - 288 := by
    rw [abs_of_nonneg (by positivity)]; exact hsize
  have := TameCarrier.integer_pinned_by_nine_residues _ habs h
  exact (circular_W_eq_288_iff n).mp this

/-! ## Part B: the nondegenerate auxiliary prime -/

/-- For a `2 × 2` matrix over a commutative ring, `det(1 - g) = 1 - tr g + det g`. -/
theorem det_one_sub_fin_two {R : Type*} [CommRing R] (g : Matrix (Fin 2) (Fin 2) R) :
    (1 - g).det = 1 - g.trace + g.det := by
  rw [Matrix.det_fin_two, Matrix.det_fin_two, Matrix.trace_fin_two]
  simp
  ring

/-- **`a_ℓ ≡ 2` is the fixed-vector degeneracy.** If `det g = 1` (Frobenius at `ℓ ≡ 1 mod p`),
then `tr g = 2 ↔ det(1 - g) = 0`. -/
theorem trace_eq_two_iff_det_one_sub_eq_zero {R : Type*} [CommRing R]
    (g : Matrix (Fin 2) (Fin 2) R) (hdet : g.det = 1) :
    g.trace = 2 ↔ (1 - g).det = 0 := by
  rw [det_one_sub_fin_two, hdet]
  constructor
  · intro h; rw [h]; ring
  · intro h; linear_combination -h

/-- Over a field, for `det g = 1`: `tr g = 2` iff `g` fixes a nonzero vector. For
`g = ρ̄_{E,p}(Frob_ℓ)` with `ℓ ≡ 1 (mod p)` this says `a_ℓ ≡ 2 (mod p)` iff `E(𝔽_ℓ)[p] ≠ 0`. -/
theorem trace_eq_two_iff_fixed_vector {K : Type*} [Field K]
    (g : Matrix (Fin 2) (Fin 2) K) (hdet : g.det = 1) :
    g.trace = 2 ↔ ∃ v : Fin 2 → K, v ≠ 0 ∧ g.mulVec v = v := by
  rw [trace_eq_two_iff_det_one_sub_eq_zero g hdet, ← Matrix.exists_mulVec_eq_zero_iff]
  constructor
  · rintro ⟨v, hv, h⟩
    refine ⟨v, hv, ?_⟩
    rw [Matrix.sub_mulVec, Matrix.one_mulVec, sub_eq_zero] at h
    exact h.symm
  · rintro ⟨v, hv, h⟩
    refine ⟨v, hv, ?_⟩
    rw [Matrix.sub_mulVec, Matrix.one_mulVec, h, sub_self]

/-- Number of `(a, b, c, d) ∈ 𝔽_p⁴` with `ad - bc = 1` and `a + d = 2`, i.e. trace-`2`
elements of `SL₂(𝔽_p)` (parametrized by `(a, b, c)` with `d = 2 - a`). -/
def traceTwoCount (p : ℕ) [NeZero p] : ℕ :=
  ((Finset.univ : Finset (ZMod p × ZMod p × ZMod p)).filter
    (fun x => x.1 * (2 - x.1) - x.2.1 * x.2.2 = 1)).card

/-- Number of elements of `SL₂(𝔽_p)` as `(a, b, c, d)` with `ad - bc = 1`. -/
def slTwoCount (p : ℕ) [NeZero p] : ℕ :=
  ((Finset.univ : Finset (ZMod p × ZMod p × ZMod p × ZMod p)).filter
    (fun x => x.1 * x.2.2.2 - x.2.1 * x.2.2.1 = 1)).card

lemma card_mul_eq_ne {F : Type*} [Field F] [Fintype F] [DecidableEq F] (t : F) (ht : t ≠ 0) :
    ((Finset.univ : Finset (F × F)).filter (fun x => x.1 * x.2 = t)).card =
      Fintype.card F - 1 := by
  open Finset in
  have : (univ : Finset (F × F)).filter (fun x => x.1 * x.2 = t) =
      (univ.erase (0:F)).image (fun b => (b, t / b)) := by
    ext ⟨b, c⟩
    simp only [mem_filter, mem_univ, true_and, mem_image, mem_erase, ne_eq, Prod.mk.injEq]
    constructor
    · intro h
      have hb : b ≠ 0 := by rintro rfl; simp at h; exact ht h.symm
      exact ⟨b, ⟨hb, trivial⟩, rfl, by field_simp; rw [← h]⟩
    · rintro ⟨b', hb', rfl, rfl⟩
      have := hb'.1
      field_simp
  rw [this, Finset.card_image_of_injective _ (fun x y h => by simpa using congrArg Prod.fst h),
    Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ]

lemma card_mul_eq_zero {F : Type*} [Field F] [Fintype F] [DecidableEq F] :
    ((Finset.univ : Finset (F × F)).filter (fun x => x.1 * x.2 = 0)).card =
      2 * Fintype.card F - 1 := by
  open Finset in
  have : (univ : Finset (F × F)).filter (fun x => x.1 * x.2 = 0) =
      (univ.filter (fun x : F × F => x.1 = 0)) ∪ (univ.filter (fun x : F × F => x.2 = 0)) := by
    ext ⟨b, c⟩; simp [mul_eq_zero]
  rw [this]
  have h1 : (Finset.univ.filter (fun x : F × F => x.1 = 0)) =
      ({0} : Finset F) ×ˢ Finset.univ := by
    ext ⟨b, c⟩; simp [eq_comm]
  have h2 : (Finset.univ.filter (fun x : F × F => x.2 = 0)) =
      Finset.univ ×ˢ ({0} : Finset F) := by
    ext ⟨b, c⟩; simp [eq_comm]
  have h3 : (Finset.univ.filter (fun x : F × F => x.1 = 0)) ∩
      (Finset.univ.filter (fun x : F × F => x.2 = 0)) = {(0, 0)} := by
    ext ⟨b, c⟩; simp
  have := Finset.card_union_add_card_inter (Finset.univ.filter (fun x : F × F => x.1 = 0))
    (Finset.univ.filter (fun x : F × F => x.2 = 0))
  rw [h3, h1, h2] at this
  rw [h1, h2]
  simp only [Finset.card_product, Finset.card_singleton, Finset.card_univ, one_mul,
    mul_one] at this
  have hpos : 0 < Fintype.card F := Fintype.card_pos
  omega

/-- **Trace-`2` count over any finite field.** Exactly `q²` elements of `SL₂(𝔽_q)` have trace
`2` (written as triples `(a, b, c)` with `d = 2 - a`). -/
theorem traceTwo_card {F : Type*} [Field F] [Fintype F] [DecidableEq F] :
    ((Finset.univ : Finset (F × F × F)).filter
      (fun x => x.1 * (2 - x.1) - x.2.1 * x.2.2 = 1)).card = Fintype.card F ^ 2 := by
  open Finset in
  rw [card_filter, Fintype.sum_prod_type]
  simp only [← Finset.card_filter]
  have key : ∀ a : F, ((Finset.univ : Finset (F × F)).filter
      (fun x => a * (2 - a) - x.1 * x.2 = 1)).card =
      if a = 1 then 2 * Fintype.card F - 1 else Fintype.card F - 1 := by
    intro a
    have e : ((Finset.univ : Finset (F × F)).filter (fun x => a * (2 - a) - x.1 * x.2 = 1)) =
        (Finset.univ : Finset (F × F)).filter (fun x => x.1 * x.2 = -(a - 1) ^ 2) := by
      ext x; simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      constructor <;> intro h <;> linear_combination -h
    rw [e]
    split_ifs with ha
    · subst ha; simpa using card_mul_eq_zero (F := F)
    · apply card_mul_eq_ne
      have : a - 1 ≠ 0 := sub_ne_zero.mpr ha
      simpa using this
  simp only [key]
  rw [Finset.sum_ite, Finset.sum_const, Finset.sum_const, Finset.filter_eq', Finset.filter_ne',
    Finset.card_erase_of_mem (Finset.mem_univ _)]
  simp only [Finset.mem_univ, if_true, Finset.card_singleton, Finset.card_univ, smul_eq_mul,
    one_mul]
  obtain ⟨k, hk⟩ : ∃ k, Fintype.card F = k + 1 :=
    ⟨_, (Nat.succ_pred_eq_of_pos Fintype.card_pos).symm⟩
  rw [hk]
  simp only [Nat.add_sub_cancel]
  ring_nf
  omega

/-- **Trace-`2` count**: exactly `p²` elements of `SL₂(𝔽_p)` have trace `2`, for every prime `p`. -/
theorem traceTwoCount_eq (p : ℕ) [Fact p.Prime] : traceTwoCount p = p ^ 2 := by
  unfold traceTwoCount
  rw [traceTwo_card, ZMod.card]

/-- `|SL₂(𝔽_p)| = p (p² - 1)` for the tested primes `p = 5, …, 47`. -/
theorem slTwoCount_eq :
    slTwoCount 5 = 5 * (5 ^ 2 - 1) ∧ slTwoCount 7 = 7 * (7 ^ 2 - 1) ∧
    slTwoCount 11 = 11 * (11 ^ 2 - 1) ∧ slTwoCount 13 = 13 * (13 ^ 2 - 1) ∧
    slTwoCount 17 = 17 * (17 ^ 2 - 1) ∧ slTwoCount 19 = 19 * (19 ^ 2 - 1) ∧
    slTwoCount 23 = 23 * (23 ^ 2 - 1) ∧ slTwoCount 29 = 29 * (29 ^ 2 - 1) ∧
    slTwoCount 31 = 31 * (31 ^ 2 - 1) ∧ slTwoCount 37 = 37 * (37 ^ 2 - 1) ∧
    slTwoCount 41 = 41 * (41 ^ 2 - 1) ∧ slTwoCount 43 = 43 * (43 ^ 2 - 1) ∧
    slTwoCount 47 = 47 * (47 ^ 2 - 1) := by
  native_decide

/-- **Counting form of target 2.** Let `Λ` be a finite set of admissible auxiliary primes for `p`,
`A ⊆ Λ` those with `a_ℓ ≡ 2`, and `Z ⊆ Λ` those with `R_{p,ℓ} ≡ 0`. If `|A| + |Z| < |Λ|`, some
admissible `ℓ` has both `a_ℓ ≢ 2` and `R_{p,ℓ} ≢ 0`. With full image, `|A|/|Λ| → p/(p² - 1)`, so
it suffices that `R_{p,ℓ} ≢ 0` on a set of relative density `> p/(p² - 1)`. -/
theorem exists_nondegenerate_of_card {ι : Type*} [DecidableEq ι] (Λ : Finset ι)
    (a2 R0 : ι → Prop) [DecidablePred a2] [DecidablePred R0]
    (hcard : (Λ.filter a2).card + (Λ.filter R0).card < Λ.card) :
    ∃ ℓ ∈ Λ, ¬ a2 ℓ ∧ ¬ R0 ℓ := by
  by_contra hno
  push_neg at hno
  have hsub : Λ ⊆ Λ.filter a2 ∪ Λ.filter R0 := by
    intro ℓ hℓ
    by_cases h : a2 ℓ
    · exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hℓ, h⟩)
    · exact Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hℓ, hno ℓ hℓ h⟩)
  have := (Finset.card_le_card hsub).trans (Finset.card_union_le _ _)
  omega

/-- **Target 2 is FIN-strength at primes `p ∤ W`, given the identity.** Suppose the identity
`C_2 = (a_ℓ - 2) R W u` holds at every admissible `ℓ` with `u_{p,ℓ} ≠ 0`, and the Ota bridge holds.
If `W ≢ 0 (mod p)` and some admissible `ℓ` is nondegenerate (`a_ℓ ≢ 2`, `R_{p,ℓ} ≢ 0`), then
`Ш[p] = 0`. -/
theorem nondegenerate_forces_good (Sha0 : Prop) (p : ℕ) [Fact p.Prime] (Adm : ℕ → Prop)
    (C2 R u a : ℕ → ZMod p) (W : ZMod p)
    (hid : ∀ ℓ, Adm ℓ → C2 ℓ = (a ℓ - 2) * R ℓ * W * u ℓ) (hu : ∀ ℓ, Adm ℓ → u ℓ ≠ 0)
    (hota : ∀ ℓ, Adm ℓ → ¬ Sha0 → C2 ℓ = 0) (hW : W ≠ 0)
    (hnd : ∃ ℓ, Adm ℓ ∧ a ℓ - 2 ≠ 0 ∧ R ℓ ≠ 0) : Sha0 := by
  by_contra hbad
  obtain ⟨ℓ, hadm, ha, hR⟩ := hnd
  exact hW (TameCarrier.tame_bad_prime_dvd_W Sha0 p (C2 ℓ) (R ℓ) (u ℓ) (a ℓ) W
    (hid ℓ hadm) ha hR (hu ℓ hadm) (hota ℓ hadm) hbad)

/-- **Contrapositive form.** Under the same hypotheses, at a bad prime with `p ∤ W` every
admissible `ℓ` is degenerate: `a_ℓ ≡ 2` or `R_{p,ℓ} ≡ 0`. So a proof that some admissible `ℓ` is
nondegenerate must come from the definition of `R_{p,ℓ}` (a function of `E(ℚ)` and `ℓ` only),
never from information about `Ш[p]`. -/
theorem degenerate_everywhere_of_bad (Sha0 : Prop) (p : ℕ) [Fact p.Prime] (Adm : ℕ → Prop)
    (C2 R u a : ℕ → ZMod p) (W : ZMod p)
    (hid : ∀ ℓ, Adm ℓ → C2 ℓ = (a ℓ - 2) * R ℓ * W * u ℓ) (hu : ∀ ℓ, Adm ℓ → u ℓ ≠ 0)
    (hota : ∀ ℓ, Adm ℓ → ¬ Sha0 → C2 ℓ = 0) (hW : W ≠ 0) (hbad : ¬ Sha0) :
    ∀ ℓ, Adm ℓ → a ℓ - 2 = 0 ∨ R ℓ = 0 := by
  intro ℓ hadm
  by_contra h
  push_neg at h
  exact hbad (nondegenerate_forces_good Sha0 p Adm C2 R u a W hid hu hota hW
    ⟨ℓ, hadm, h.1, h.2⟩)

end TameCircularity
