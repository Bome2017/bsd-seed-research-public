import Mathlib
import RequestProject.ThresholdGap

/-!
# The new threshold `1521` is sharp, and the old sharpness witness is dead

`RequestProject/ThresholdGap.lean` proves that, with the retained primary inputs at `2, 5, 7` and
the imported `11`-primary vanishing, a finite `Ш` has order `9` or at least `1521 = 9 · 13²`.

This file machine-checks the two complementary facts.

1. **The record's own sharpness witness for the old threshold is excluded by the new input.**
   `(ℤ/3)² ⊕ (ℤ/11)²`, the group the record used to argue that `1089` could not be improved
   abstractly, has nonzero `11`-torsion, hence violates the imported input `Ш[11^∞] = 0`.  This is
   the exact sense in which the `C₁₁` computation unblocks the threshold argument.

2. **`1521` cannot be improved abstractly.**  `(ℤ/3)² ⊕ (ℤ/13)²` satisfies every hypothesis of the
   gap theorem — vanishing `p`-torsion for `p ∈ {2, 5, 7, 11}`, `#A[3^∞] = 9`, square primary
   orders away from `3`, and a nondegenerate alternating pairing on each primary part — and has
   order exactly `1521`.

Consequently the threshold in the record's endgame target moves from `1089` to `1521` and no
further: the sufficient hypothesis for order nine is now `#Ш < 1521`, and this is the last
improvement obtainable from the `11`-primary input alone.  This also supersedes the countermodel
in `RequestProject/TargetBCountermodel.lean`: the minimal countermodel to the record's target (B)
is no longer of order `1089` with `C_E = 33`, but of order `1521` with `C_E = 39`.
-/

namespace SeedBSD

namespace ThresholdSharpness

/-! ### 1. The old sharpness witness is excluded by the imported `11`-primary input -/

/-- The old witness `(ℤ/3)² ⊕ (ℤ/11)²`. -/
abbrev Gold : Type := (ZMod 3 × ZMod 3) × (ZMod 11 × ZMod 11)

/-- **The old witness has nonzero `11`-torsion**, so it is not a model of the retained inputs once
`Ш[11^∞] = 0` is imported. -/
theorem old_witness_has_eleven_torsion : ∃ g : Gold, g ≠ 0 ∧ (11 : ℕ) • g = 0 := by
  refine ⟨((0, 0), (1, 0)), ?_, ?_⟩
  · decide
  · decide

/-! ### 2. The new witness of order `1521` -/

/-- The new sharpness witness `G = (ℤ/3)² ⊕ (ℤ/13)²`. -/
abbrev G : Type := (ZMod 3 × ZMod 3) × (ZMod 13 × ZMod 13)

theorem card_G : Nat.card G = 1521 := by simp [Nat.card_eq_fintype_card]

theorem card_G_ne_nine : Nat.card G ≠ 9 := by rw [card_G]; norm_num

theorem smul39_zmod3 : ∀ x : ZMod 3, (39 : ℕ) • x = 0 := by decide
theorem smul39_zmod13 : ∀ x : ZMod 13, (39 : ℕ) • x = 0 := by decide
theorem smul13_zmod13 : ∀ x : ZMod 13, (13 : ℕ) • x = 0 := by decide
theorem smul3_zmod3 : ∀ x : ZMod 3, ((3 : ℕ) ^ 1) • x = 0 := by decide

/-- The exponent of `G` divides `39`. -/
theorem exponent_dvd (g : G) : (39 : ℕ) • g = 0 := by
  obtain ⟨⟨a, b⟩, ⟨c, d⟩⟩ := g
  exact Prod.ext (Prod.ext (by simpa using smul39_zmod3 a) (by simpa using smul39_zmod3 b))
    (Prod.ext (by simpa using smul39_zmod13 c) (by simpa using smul39_zmod13 d))

/-- The second factor is killed by `13`. -/
theorem snd_exponent (g : G) : (13 : ℕ) • g.2 = 0 := by
  obtain ⟨c, d⟩ := g.2
  exact Prod.ext (by simpa using smul13_zmod13 c) (by simpa using smul13_zmod13 d)

theorem eq_zero_of_addOrderOf_dvd_one {B : Type*} [AddGroup B] {g : B} (h : addOrderOf g ∣ 1) :
    g = 0 :=
  AddMonoid.addOrderOf_eq_one_iff.mp (Nat.dvd_one.mp h)

/-- `G[p] = 0` for every prime `p ∤ 39`; in particular for `p ∈ {2, 5, 7, 11}`. -/
theorem prime_torsion_free (p : ℕ) (hp : p.Prime) (hpd : ¬ (p ∣ 39)) (g : G) (hg : p • g = 0) :
    g = 0 := by
  have h1 : addOrderOf g ∣ 39 := addOrderOf_dvd_iff_nsmul_eq_zero.mpr (exponent_dvd g)
  have h2 : addOrderOf g ∣ p := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hg
  have hcop : Nat.gcd 39 p = 1 := Nat.Coprime.symm ((Nat.Prime.coprime_iff_not_dvd hp).mpr hpd)
  exact eq_zero_of_addOrderOf_dvd_one (hcop ▸ Nat.dvd_gcd h1 h2)

/-- The `3`-primary part is exactly `(ℤ/3)²`. -/
theorem three_primary_iff (g : G) : (∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0) ↔ g.2 = 0 := by
  constructor
  · rintro ⟨k, hk⟩
    have h2 : ((3 : ℕ) ^ k) • g.2 = 0 := by
      have := congrArg Prod.snd hk; simpa using this
    have hord : addOrderOf g.2 ∣ 3 ^ k := addOrderOf_dvd_iff_nsmul_eq_zero.mpr h2
    have h13 : addOrderOf g.2 ∣ 13 := addOrderOf_dvd_iff_nsmul_eq_zero.mpr (snd_exponent g)
    have hcop : Nat.gcd (3 ^ k) 13 = 1 :=
      Nat.Coprime.pow_left _ (by norm_num [Nat.coprime_iff_gcd_eq_one])
    exact eq_zero_of_addOrderOf_dvd_one (hcop ▸ Nat.dvd_gcd hord h13)
  · intro h
    refine ⟨1, ?_⟩
    obtain ⟨⟨a, b⟩, c⟩ := g
    simp only at h
    subst h
    exact Prod.ext (Prod.ext (by simpa using smul3_zmod3 a) (by simpa using smul3_zmod3 b))
      (by simp)

/-- `#G[3^∞] = 9`, matching the retained `3`-primary input. -/
theorem card_three_primary : Nat.card {g : G // ∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0} = 9 := by
  have e : {g : G // ∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0} ≃ (ZMod 3 × ZMod 3) :=
    { toFun := fun g => g.1.1
      invFun := fun a => ⟨(a, 0), (three_primary_iff (a, 0)).mpr rfl⟩
      left_inv := by
        rintro ⟨⟨a, b⟩, hb⟩
        have hb0 : b = 0 := (three_primary_iff (a, b)).mp hb
        simp [hb0]
      right_inv := fun a => rfl }
  rw [Nat.card_congr e]
  simp [Nat.card_eq_fintype_card]

/-- Every primary order away from `3` is a square (Cassels–Tate square order holds for `G`). -/
theorem even_factorization (p : ℕ) (hp3 : p ≠ 3) : Even ((Nat.card G).factorization p) := by
  rw [card_G]
  have h : (1521 : ℕ) = 3 ^ 2 * 13 ^ 2 := by norm_num
  rw [h, Nat.factorization_mul (by norm_num) (by norm_num),
    Nat.Prime.factorization_pow (by norm_num), Nat.Prime.factorization_pow (by norm_num)]
  by_cases h13 : p = 13 <;> simp [h13, hp3]

/-! ### The alternating pairing on each primary part -/

/-- The standard symplectic pairing on `(ℤ/n)²`. -/
def pair (n : ℕ) (x y : ZMod n × ZMod n) : ZMod n := x.1 * y.2 - x.2 * y.1

theorem pair_alternating (n : ℕ) (x : ZMod n × ZMod n) : pair n x x = 0 := by
  simp [pair, mul_comm]

theorem pair_nondegenerate (n : ℕ) {x : ZMod n × ZMod n} (h : ∀ y, pair n x y = 0) : x = 0 := by
  have h1 : x.1 = 0 := by have := h (0, 1); simpa [pair] using this
  have h2 : x.2 = 0 := by
    have := h (1, 0)
    simp only [pair, mul_zero, mul_one, zero_sub, neg_eq_zero] at this
    exact this
  exact Prod.ext h1 h2

/-! ### The sharpness statement -/

/-- **`1521` is sharp.**  `G = (ℤ/3)² ⊕ (ℤ/13)²` satisfies every hypothesis of the gap theorem
`SeedBSD.Gap.card_eq_nine_or_ge_1521` — including the newly imported `11`-primary vanishing — and
carries a nondegenerate alternating pairing on each primary part, yet has order `1521 ≠ 9`.  So
no threshold above `1521` follows from these inputs, and the bound `#Ш < 1521` cannot be weakened
abstractly. -/
theorem threshold_1521_is_sharp :
    (∀ g : G, (2 : ℕ) • g = 0 → g = 0) ∧
    (∀ g : G, (5 : ℕ) • g = 0 → g = 0) ∧
    (∀ g : G, (7 : ℕ) • g = 0 → g = 0) ∧
    (∀ g : G, (11 : ℕ) • g = 0 → g = 0) ∧
    Nat.card {g : G // ∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0} = 9 ∧
    (∀ p : ℕ, p.Prime → p ≠ 3 → Even ((Nat.card G).factorization p)) ∧
    (∀ x : ZMod 3 × ZMod 3, pair 3 x x = 0) ∧
    (∀ x : ZMod 13 × ZMod 13, pair 13 x x = 0) ∧
    (∀ x : ZMod 3 × ZMod 3, (∀ y, pair 3 x y = 0) → x = 0) ∧
    (∀ x : ZMod 13 × ZMod 13, (∀ y, pair 13 x y = 0) → x = 0) ∧
    Nat.card G = 1521 ∧ Nat.card G ≠ 9 :=
  ⟨fun g hg => prime_torsion_free 2 (by norm_num) (by norm_num) g hg,
   fun g hg => prime_torsion_free 5 (by norm_num) (by norm_num) g hg,
   fun g hg => prime_torsion_free 7 (by norm_num) (by norm_num) g hg,
   fun g hg => prime_torsion_free 11 (by norm_num) (by norm_num) g hg,
   card_three_primary,
   fun p _ hp3 => even_factorization p hp3,
   pair_alternating 3, pair_alternating 13,
   fun _ h => pair_nondegenerate 3 h, fun _ h => pair_nondegenerate 13 h,
   card_G, card_G_ne_nine⟩

end ThresholdSharpness

end SeedBSD
