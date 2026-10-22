import Mathlib

/-!
# Target B, as stated, does not give order nine

The record listed as a sufficient form of its arithmetic endpoint:

> (B) `Ш[p] ≠ 0 ⇒ p ∣ C_E`, for an independently constructed explicit nonzero integer `C_E`,
> together with complete primary-depth control at every divisor of `C_E`.

That hypothesis proves **finiteness** of `Ш` (finite prime support plus finite primary parts).
It does **not** prove `#Ш = 9`.  This file machine-checks the countermodel

  `G = (ℤ/3)² ⊕ (ℤ/11)²`,  `C_E = 33`,

which satisfies every condition in (B) together with all four retained primary inputs
(`G[2^∞] = 0`, `#G[3^∞] = 9`, `G[5^∞] = 0`, `G[7^∞] = 0`), has completely known depth `1` at
both primes of its support, carries a nondegenerate alternating pairing on each primary part —
and has order `1089`, not `9`.

The repair is the one the review states: to earn order nine, the primary bounds must in addition
force every component away from `3` to vanish and the `3`-primary order to be `9`.  That is the
content of `RequestProject/Assembly.lean`.
-/

namespace SeedBSD

namespace TargetB

/-- The countermodel group `G = (ℤ/3)² ⊕ (ℤ/11)²`. -/
abbrev G : Type := (ZMod 3 × ZMod 3) × (ZMod 11 × ZMod 11)

/-- The proposed support integer `C_E = 33`. -/
def CE : ℕ := 33

theorem card_G : Nat.card G = 1089 := by
  simp [Nat.card_eq_fintype_card]

/-- The order is not nine. -/
theorem card_G_ne_nine : Nat.card G ≠ 9 := by rw [card_G]; norm_num

theorem smul33_zmod3 : ∀ x : ZMod 3, (33 : ℕ) • x = 0 := by decide
theorem smul33_zmod11 : ∀ x : ZMod 11, (33 : ℕ) • x = 0 := by decide
theorem smul11_zmod11 : ∀ x : ZMod 11, (11 : ℕ) • x = 0 := by decide
theorem smul3_zmod3 : ∀ x : ZMod 3, ((3 : ℕ) ^ 1) • x = 0 := by decide

/-- The exponent of `G` divides `C_E = 33`. -/
theorem exponent_dvd (g : G) : (33 : ℕ) • g = 0 := by
  obtain ⟨⟨a, b⟩, ⟨c, d⟩⟩ := g
  exact Prod.ext (Prod.ext (by simpa using smul33_zmod3 a) (by simpa using smul33_zmod3 b))
    (Prod.ext (by simpa using smul33_zmod11 c) (by simpa using smul33_zmod11 d))

/-- The second factor is killed by `11`. -/
theorem snd_exponent (g : G) : (11 : ℕ) • g.2 = 0 := by
  obtain ⟨c, d⟩ := g.2
  exact Prod.ext (by simpa using smul11_zmod11 c) (by simpa using smul11_zmod11 d)

theorem eq_zero_of_addOrderOf_dvd_one {A : Type*} [AddGroup A] {g : A} (h : addOrderOf g ∣ 1) :
    g = 0 :=
  AddMonoid.addOrderOf_eq_one_iff.mp (Nat.dvd_one.mp h)

/-- **(B)'s support condition holds**: `G[p] = 0` for every prime `p ∤ 33`.  Equivalently,
`G[p] ≠ 0 ⇒ p ∣ C_E`. -/
theorem prime_support (p : ℕ) (hp : p.Prime) (hpd : ¬ (p ∣ 33)) (g : G) (hg : p • g = 0) :
    g = 0 := by
  have h1 : addOrderOf g ∣ 33 := addOrderOf_dvd_iff_nsmul_eq_zero.mpr (exponent_dvd g)
  have h2 : addOrderOf g ∣ p := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hg
  have hcop : Nat.gcd 33 p = 1 := Nat.Coprime.symm ((Nat.Prime.coprime_iff_not_dvd hp).mpr hpd)
  exact eq_zero_of_addOrderOf_dvd_one (hcop ▸ Nat.dvd_gcd h1 h2)

/-- The `3`-primary part is exactly `(ℤ/3)²`. -/
theorem three_primary_iff (g : G) : (∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0) ↔ g.2 = 0 := by
  constructor
  · rintro ⟨k, hk⟩
    have h2 : ((3 : ℕ) ^ k) • g.2 = 0 := by
      have := congrArg Prod.snd hk; simpa using this
    have hord : addOrderOf g.2 ∣ 3 ^ k := addOrderOf_dvd_iff_nsmul_eq_zero.mpr h2
    have h11 : addOrderOf g.2 ∣ 11 := addOrderOf_dvd_iff_nsmul_eq_zero.mpr (snd_exponent g)
    have hcop : Nat.gcd (3 ^ k) 11 = 1 :=
      Nat.Coprime.pow_left _ (by norm_num [Nat.coprime_iff_gcd_eq_one])
    exact eq_zero_of_addOrderOf_dvd_one (hcop ▸ Nat.dvd_gcd hord h11)
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

/-- `G[p^∞] = 0` for `p ∈ {2, 5, 7}`, matching the other three retained primary inputs. -/
theorem other_primaries_vanish (p : ℕ) (hp : p = 2 ∨ p = 5 ∨ p = 7) (g : G) (k : ℕ)
    (hk : (p ^ k) • g = 0) : g = 0 := by
  have hcop : Nat.gcd (p ^ k) 33 = 1 := by
    rcases hp with rfl | rfl | rfl <;>
      exact Nat.Coprime.pow_left _ (by norm_num [Nat.coprime_iff_gcd_eq_one])
  have h1 : addOrderOf g ∣ p ^ k := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hk
  have h2 : addOrderOf g ∣ 33 := addOrderOf_dvd_iff_nsmul_eq_zero.mpr (exponent_dvd g)
  exact eq_zero_of_addOrderOf_dvd_one (hcop ▸ Nat.dvd_gcd h1 h2)

/-! ### Each primary part carries a nondegenerate alternating pairing -/

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

/-- **Target B is insufficient as stated.**  All of (B)'s conditions, and all four retained
primary inputs, hold for `G = (ℤ/3)² ⊕ (ℤ/11)²` with `C_E = 33`, yet `#G = 1089 ≠ 9`. -/
theorem target_B_does_not_give_order_nine :
    -- (B): explicit nonzero support integer, and `G[p] ≠ 0 ⇒ p ∣ C_E`
    CE ≠ 0 ∧
    (∀ p : ℕ, p.Prime → ¬ (p ∣ CE) → ∀ g : G, p • g = 0 → g = 0) ∧
    -- complete primary-depth control: the exponent is squarefree of known support
    (∀ g : G, (33 : ℕ) • g = 0) ∧
    -- the four retained primary inputs
    (∀ g : G, ∀ k : ℕ, ((2 : ℕ) ^ k) • g = 0 → g = 0) ∧
    Nat.card {g : G // ∃ k : ℕ, ((3 : ℕ) ^ k) • g = 0} = 9 ∧
    (∀ g : G, ∀ k : ℕ, ((5 : ℕ) ^ k) • g = 0 → g = 0) ∧
    (∀ g : G, ∀ k : ℕ, ((7 : ℕ) ^ k) • g = 0 → g = 0) ∧
    -- a nondegenerate alternating pairing on each primary part
    (∀ x : ZMod 3 × ZMod 3, pair 3 x x = 0) ∧
    (∀ x : ZMod 11 × ZMod 11, pair 11 x x = 0) ∧
    (∀ x : ZMod 3 × ZMod 3, (∀ y, pair 3 x y = 0) → x = 0) ∧
    (∀ x : ZMod 11 × ZMod 11, (∀ y, pair 11 x y = 0) → x = 0) ∧
    -- but the order is 1089
    Nat.card G = 1089 ∧ Nat.card G ≠ 9 := by
  refine ⟨by norm_num [CE], fun p hp hpd g hg => prime_support p hp (by simpa [CE] using hpd) g hg,
    exponent_dvd, fun g k hk => other_primaries_vanish 2 (Or.inl rfl) g k hk,
    card_three_primary, fun g k hk => other_primaries_vanish 5 (Or.inr (Or.inl rfl)) g k hk,
    fun g k hk => other_primaries_vanish 7 (Or.inr (Or.inr rfl)) g k hk,
    pair_alternating 3, pair_alternating 11,
    fun _ h => pair_nondegenerate 3 h, fun _ h => pair_nondegenerate 11 h,
    card_G, card_G_ne_nine⟩

end TargetB

end SeedBSD
