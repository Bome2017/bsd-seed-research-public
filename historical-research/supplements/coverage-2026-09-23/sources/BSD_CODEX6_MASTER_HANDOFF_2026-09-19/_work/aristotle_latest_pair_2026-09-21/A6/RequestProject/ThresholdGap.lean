import Mathlib

/-!
# The order gap after the `11`-primary input, and the new sharp threshold

## What this file uses from outside Lean

The project record fixed its endgame threshold at `1089 = 9 · 11²`: under the retained primary
inputs `Ш[2^∞] = 0`, `#Ш[3^∞] = 9`, `Ш[5^∞] = 0`, `Ш[7^∞] = 0` and Cassels–Tate square order,
the possible finite orders are `#Ш = 9t²` with `gcd(t, 210) = 1`, so the first order after `9`
is `9 · 11² = 1089`; and the record's own sharpness witness for that threshold was the abstract
group `(ℤ/3)² ⊕ (ℤ/11)²`.

The imported arithmetic input for this file is the completed local certified computation

    C₁₁ := [T²] L₁₁(E, T) ≡ 8 (mod 11)   in the ω₁ convention  (4 in the full-real-period
                                          convention Ω_E = 2ω₁),

whose fixed-prime consequence is `Ш(E/ℚ)[11^∞] = 0`, with the retained rank, residual-image,
modular-symbol-lattice, Manin-constant and computational qualifications.  **That input is not
verified in Lean**; see `IMPORTED_C11_INPUT.md` for its exact statement and trust boundary.  It
enters the Lean statements below only as an explicit hypothesis (`h11`), never as an axiom.

## What is proved here

The `11`-primary input is exactly what the threshold argument was missing: it deletes the record's
own sharpness witness.  This file machine-checks the resulting **gap theorem** in the general form

    if the finite abelian group `A` has `#A[3^∞] = 9`, `A[p] = 0` for every prime `p ≠ 3` below a
    bound `q`, and every primary order away from `3` is a square, then `#A = 9` or `#A ≥ 9q²`,

together with its instance at `q = 13` — the first prime not yet excluded — giving

    #Ш = 9   or   #Ш ≥ 1521,

so that the sufficient bound for order nine is relaxed from `#Ш < 1089` to `#Ш < 1521`, and the
new threshold is again sharp: `(ℤ/3)² ⊕ (ℤ/13)²` satisfies every retained input, including
`11`-primary vanishing, and has order `1521`.

Nothing here proves finiteness, order nine, or any vanishing statement: the arithmetic premise
that remains is `Ш[p] = 0` for every prime `p ≥ 13`, and it is untouched.
-/

namespace SeedBSD

namespace Gap

variable {A : Type*} [AddCommGroup A]

/-! ### The `p`-primary part and its order -/

/-- The `p`-primary part of an abelian group, as a subgroup. -/
def primaryPart (A : Type*) [AddCommGroup A] (p : ℕ) : AddSubgroup A where
  carrier := {a | ∃ k : ℕ, (p ^ k) • a = 0}
  zero_mem' := ⟨0, by simp⟩
  add_mem' := by
    rintro a b ⟨k, hk⟩ ⟨l, hl⟩
    refine ⟨k + l, ?_⟩
    have ha : (p ^ (k + l)) • a = 0 := by rw [pow_add, mul_comm, mul_smul, hk, smul_zero]
    have hb : (p ^ (k + l)) • b = 0 := by rw [pow_add, mul_smul, hl, smul_zero]
    rw [smul_add, ha, hb, add_zero]
  neg_mem' := by
    rintro a ⟨k, hk⟩
    exact ⟨k, by rw [smul_neg, hk, neg_zero]⟩

theorem mem_primaryPart {p : ℕ} {a : A} : a ∈ primaryPart A p ↔ ∃ k : ℕ, (p ^ k) • a = 0 :=
  Iff.rfl

/-- The primary part, as a subgroup, has the same cardinality as the subtype of `p`-power torsion
elements used in the rest of the project. -/
theorem card_primaryPart_eq_card_subtype (p : ℕ) :
    Nat.card (primaryPart A p) = Nat.card {a : A // ∃ k : ℕ, (p ^ k) • a = 0} :=
  Nat.card_congr ⟨fun x => ⟨x.1, x.2⟩, fun x => ⟨x.1, x.2⟩, fun _ => rfl, fun _ => rfl⟩

/-- The `p`-primary part of a finite group has `p`-power order. -/
theorem card_primaryPart_eq_pow [Finite A] {p : ℕ} (hp : p.Prime) :
    ∃ k : ℕ, Nat.card (primaryPart A p) = p ^ k := by
  haveI : Fact p.Prime := ⟨hp⟩
  haveI : Fintype (primaryPart A p) := Fintype.ofFinite _
  refine ⟨_, Nat.eq_prime_pow_of_unique_prime_dvd (Nat.card_pos.ne') ?_⟩
  intro d hd hdvd
  rw [Nat.card_eq_fintype_card] at hdvd
  haveI : Fact d.Prime := ⟨hd⟩
  obtain ⟨x, hx⟩ := exists_prime_addOrderOf_dvd_card (G := primaryPart A p) d hdvd
  obtain ⟨k, hk⟩ := x.2
  have hx0 : (p ^ k) • x = 0 := Subtype.ext (by simpa using hk)
  have hdd : addOrderOf x ∣ p ^ k := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hx0
  rw [hx] at hdd
  exact (Nat.prime_dvd_prime_iff_eq hd hp).mp (hd.dvd_of_dvd_pow hdd)

/-- The quotient by the `p`-primary part has order prime to `p`. -/
theorem not_dvd_card_quotient [Finite A] {p : ℕ} (hp : p.Prime) :
    ¬ p ∣ Nat.card (A ⧸ primaryPart A p) := by
  haveI : Fact p.Prime := ⟨hp⟩
  haveI : Fintype (A ⧸ primaryPart A p) := Fintype.ofFinite _
  intro hdvd
  rw [Nat.card_eq_fintype_card] at hdvd
  obtain ⟨x, hx⟩ := exists_prime_addOrderOf_dvd_card (G := A ⧸ primaryPart A p) p hdvd
  induction x using QuotientAddGroup.induction_on with
  | H a =>
    have hzero : (p : ℕ) • (QuotientAddGroup.mk (s := primaryPart A p) a) = 0 := by
      have h := addOrderOf_nsmul_eq_zero (QuotientAddGroup.mk (s := primaryPart A p) a)
      rwa [hx] at h
    have hmem : p • a ∈ primaryPart A p := by
      have h2 : QuotientAddGroup.mk (s := primaryPart A p) (p • a) = 0 := by rw [← hzero]; rfl
      exact (QuotientAddGroup.eq_zero_iff _).mp h2
    obtain ⟨k, hk⟩ := hmem
    have hmem2 : a ∈ primaryPart A p := ⟨k + 1, by rw [pow_succ, mul_smul]; exact hk⟩
    have h0 : QuotientAddGroup.mk (s := primaryPart A p) a = 0 :=
      (QuotientAddGroup.eq_zero_iff _).mpr hmem2
    rw [h0, addOrderOf_zero] at hx
    exact hp.one_lt.ne hx

/-- **The primary order is the `p`-part of the group order.** -/
theorem card_primaryPart_eq_factorization [Finite A] {p : ℕ} (hp : p.Prime) :
    Nat.card (primaryPart A p) = p ^ ((Nat.card A).factorization p) := by
  obtain ⟨k, hk⟩ := card_primaryPart_eq_pow (A := A) hp
  have hsplit : Nat.card A = Nat.card (A ⧸ primaryPart A p) * Nat.card (primaryPart A p) :=
    AddSubgroup.card_eq_card_quotient_mul_card_addSubgroup _
  have hq0 : Nat.card (A ⧸ primaryPart A p) ≠ 0 := Nat.card_pos.ne'
  have hh0 : Nat.card (primaryPart A p) ≠ 0 := Nat.card_pos.ne'
  have hfac : (Nat.card A).factorization p = k := by
    rw [hsplit, Nat.factorization_mul hq0 hh0]
    simp only [Finsupp.coe_add, Pi.add_apply]
    rw [Nat.factorization_eq_zero_of_not_dvd (not_dvd_card_quotient (A := A) hp), hk,
      Nat.Prime.factorization_pow hp]
    simp
  rw [hk, hfac]

/-- If `A[p] = 0` then `p` does not divide `#A`. -/
theorem factorization_eq_zero_of_torsion_free [Finite A] {p : ℕ} (hp : p.Prime)
    (h : ∀ b : A, (p : ℕ) • b = 0 → b = 0) : (Nat.card A).factorization p = 0 := by
  haveI : Fact p.Prime := ⟨hp⟩
  haveI : Fintype A := Fintype.ofFinite _
  refine Nat.factorization_eq_zero_of_not_dvd ?_
  intro hdvd
  rw [Nat.card_eq_fintype_card] at hdvd
  obtain ⟨x, hx⟩ := exists_prime_addOrderOf_dvd_card (G := A) p hdvd
  have hpx : (p : ℕ) • x = 0 := by
    have := addOrderOf_nsmul_eq_zero x
    rwa [hx] at this
  have hx0 : x = 0 := h x hpx
  rw [hx0, addOrderOf_zero] at hx
  exact hp.one_lt.ne hx

/-- The `3`-primary input `#A[3^∞] = 9` says exactly that `3` divides `#A` to order two. -/
theorem factorization_three_of_card_three_primary [Finite A]
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9) :
    (Nat.card A).factorization 3 = 2 := by
  have h := card_primaryPart_eq_factorization (A := A) (p := 3) (by norm_num)
  rw [card_primaryPart_eq_card_subtype, h3] at h
  have h9 : (9 : ℕ) = 3 ^ 2 := by norm_num
  rw [h9] at h
  exact (Nat.pow_right_injective (by norm_num) h).symm

/-! ### The gap theorem -/

/-- **Order gap.**  Let `A` be a finite abelian group (the role of `Ш(E/ℚ)` under `FIN`) with

* `#A[3^∞] = 9`                                             (`h3`),
* `A[p] = 0` for every prime `p ≠ 3` with `p < q`            (`hsmall`),
* `#A[p^∞]` a square for every prime `p ≠ 3`                 (`hsq`, Cassels–Tate square order,
  recorded as evenness of the `p`-adic valuation of `#A`).

Then `#A = 9` or `#A ≥ 9q²`: there are no admissible orders strictly between.

The bound `q` is a parameter, so each newly settled primary component advances the threshold
automatically. -/
theorem card_eq_nine_or_ge_of_small_primes_vanish [Finite A] (q : ℕ)
    (hsmall : ∀ p : ℕ, p.Prime → p ≠ 3 → p < q → ∀ b : A, (p : ℕ) • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9)
    (hsq : ∀ p : ℕ, p.Prime → p ≠ 3 → Even ((Nat.card A).factorization p)) :
    Nat.card A = 9 ∨ 9 * q ^ 2 ≤ Nat.card A := by
  set n := Nat.card A with hn
  have hn0 : n ≠ 0 := Nat.card_pos.ne'
  have h3fac : n.factorization 3 = 2 := factorization_three_of_card_three_primary h3
  by_cases hall : ∀ p : ℕ, p.Prime → p ≠ 3 → n.factorization p = 0
  · -- every prime other than `3` is absent, so `n = 9`
    left
    refine Nat.eq_of_factorization_eq hn0 (by norm_num) fun p => ?_
    by_cases hp : p.Prime
    · by_cases hp3 : p = 3
      · subst hp3
        rw [h3fac]
        have : (9 : ℕ) = 3 ^ 2 := by norm_num
        rw [this, Nat.Prime.factorization_pow (by norm_num)]
        simp
      · rw [hall p hp hp3]
        have h9 : (9 : ℕ) = 3 ^ 2 := by norm_num
        rw [h9, Nat.Prime.factorization_pow (by norm_num)]
        simp [Ne.symm hp3]
    · rw [Nat.factorization_eq_zero_of_not_prime _ hp, Nat.factorization_eq_zero_of_not_prime _ hp]
  · -- some other prime occurs; it is `≥ q` and occurs to an even, hence `≥ 2`, order
    right
    push_neg at hall
    obtain ⟨p, hp, hp3, hpne⟩ := hall
    have hpq : q ≤ p := by
      by_contra hlt
      push_neg at hlt
      exact hpne (factorization_eq_zero_of_torsion_free hp (hsmall p hp hp3 hlt))
    have hpos : 1 ≤ n.factorization p := Nat.one_le_iff_ne_zero.mpr hpne
    have hge2 : 2 ≤ n.factorization p := by
      rcases hsq p hp hp3 with ⟨m, hm⟩
      omega
    have hdvd_p : p ^ 2 ∣ n := (Nat.Prime.pow_dvd_iff_le_factorization hp hn0).mpr hge2
    have hdvd_3 : 3 ^ 2 ∣ n :=
      (Nat.Prime.pow_dvd_iff_le_factorization (by norm_num) hn0).mpr (by rw [h3fac])
    have hcop : Nat.Coprime (3 ^ 2) (p ^ 2) :=
      Nat.Coprime.pow _ _ ((Nat.coprime_primes (by norm_num) hp).mpr (Ne.symm hp3))
    have hmul : 3 ^ 2 * p ^ 2 ∣ n := Nat.Coprime.mul_dvd_of_dvd_of_dvd hcop hdvd_3 hdvd_p
    have hle : 3 ^ 2 * p ^ 2 ≤ n := Nat.le_of_dvd (Nat.pos_of_ne_zero hn0) hmul
    have : 9 * q ^ 2 ≤ 3 ^ 2 * p ^ 2 := by
      have : q ^ 2 ≤ p ^ 2 := Nat.pow_le_pow_left hpq 2
      simpa using Nat.mul_le_mul_left 9 this
    omega

/-- **The new threshold, `1521`.**  With the retained inputs at `2, 5, 7` and the imported
`11`-primary vanishing, a finite `Ш` has order `9` or at least `1521 = 9 · 13²`. -/
theorem card_eq_nine_or_ge_1521 [Finite A]
    (h2 : ∀ b : A, (2 : ℕ) • b = 0 → b = 0)
    (h5 : ∀ b : A, (5 : ℕ) • b = 0 → b = 0)
    (h7 : ∀ b : A, (7 : ℕ) • b = 0 → b = 0)
    (h11 : ∀ b : A, (11 : ℕ) • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9)
    (hsq : ∀ p : ℕ, p.Prime → p ≠ 3 → Even ((Nat.card A).factorization p)) :
    Nat.card A = 9 ∨ 1521 ≤ Nat.card A := by
  have h := card_eq_nine_or_ge_of_small_primes_vanish (A := A) 13 ?_ h3 hsq
  · simpa using h
  · intro p hp hp3 hlt b hb
    interval_cases p <;> first
      | exact absurd hp (by decide)
      | exact absurd rfl hp3
      | exact h2 b hb
      | exact h5 b hb
      | exact h7 b hb
      | exact h11 b hb

/-- **The sufficient bound is relaxed from `1089` to `1521`.**  Any argument producing a finite
`Ш` of order `< 1521` now yields order nine; the record's threshold `1089` was the value of this
statement before the `11`-primary input. -/
theorem card_eq_nine_of_card_lt_1521 [Finite A]
    (h2 : ∀ b : A, (2 : ℕ) • b = 0 → b = 0)
    (h5 : ∀ b : A, (5 : ℕ) • b = 0 → b = 0)
    (h7 : ∀ b : A, (7 : ℕ) • b = 0 → b = 0)
    (h11 : ∀ b : A, (11 : ℕ) • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9)
    (hsq : ∀ p : ℕ, p.Prime → p ≠ 3 → Even ((Nat.card A).factorization p))
    (hlt : Nat.card A < 1521) :
    Nat.card A = 9 := by
  rcases card_eq_nine_or_ge_1521 h2 h5 h7 h11 h3 hsq with h | h
  · exact h
  · omega

end Gap

end SeedBSD
