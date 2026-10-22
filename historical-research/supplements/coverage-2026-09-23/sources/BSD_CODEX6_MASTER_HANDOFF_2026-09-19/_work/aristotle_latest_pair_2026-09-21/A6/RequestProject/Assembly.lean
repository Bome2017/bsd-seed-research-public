import Mathlib

/-!
# Assembly: what actually suffices for `#Ш = 9`

The project record lists three sufficient forms of `FIN`, the first being

    (A)  #Ш[n] < 1089 for every n ≥ 1,

with an abstract sharpness example `(ℤ/3)² ⊕ (ℚ₁₁/ℤ₁₁)²` said to show that a bound on `Ш[p]`
for *primes* alone is insufficient, and a Cassels–Tate square-order argument producing the
threshold `1089 = 9 · 11²`.

This file machine-checks that, **given the already-proved primary inputs**, none of that
apparatus is needed.  The weakest sufficient statement is the purely prime-by-prime one

    Ш[p] = 0 for every prime p ≠ 3,

and it implies `#Ш = 9` directly: no square-order hypothesis, no Cassels–Tate pairing, no
threshold, and no quantification over all `n`.  The apparent obstruction from a divisible part
`(ℚ₁₁/ℤ₁₁)²` does not arise, because a nonzero `p`-primary group always contains an element of
order exactly `p`; so `Ш[p] = 0` already kills the whole `p`-primary component, divisible or not
(`three_primary_of_no_other_prime_torsion`).

Only the abstract group theory is formalised.  The identification of `Ш(E/ℚ)` as a torsion
abelian group with `#Ш[3^∞] = 9` is an input from the record, not reproved here.
-/

namespace SeedBSD

variable {A : Type*} [AddCommGroup A]

/-- If `a ≠ 0` has finite additive order, every prime dividing that order produces a nonzero
element killed by that prime. -/
theorem prime_dvd_addOrderOf_eq_of_no_torsion {q : ℕ}
    (hp : ∀ p : ℕ, p.Prime → p ≠ q → ∀ b : A, p • b = 0 → b = 0)
    (a : A) (ha : 0 < addOrderOf a) {p : ℕ} (hpP : p.Prime) (hpd : p ∣ addOrderOf a) :
    p = q := by
  by_contra hpq
  obtain ⟨k, hk⟩ := hpd
  have hk0 : 0 < k := by
    rcases Nat.eq_zero_or_pos k with h0 | h0
    · rw [h0, Nat.mul_zero] at hk; omega
    · exact h0
  have hkill : p • (k • a) = 0 := by
    rw [smul_smul, ← hk, addOrderOf_nsmul_eq_zero]
  have hzero : k • a = 0 := hp p hpP hpq _ hkill
  have hdvd : addOrderOf a ∣ k := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hzero
  have hle : addOrderOf a ≤ k := Nat.le_of_dvd hk0 hdvd
  have h2 : 2 ≤ p := hpP.two_le
  nlinarith [hk, hle, hk0, h2]

/-- **No hidden divisible part.**  If `A` is torsion and `A[p] = 0` for every prime `p ≠ q`,
then every element of `A` is killed by a power of `q`.  In particular the counterexample
`(ℤ/3)² ⊕ (ℚ₁₁/ℤ₁₁)²` is already excluded at the level of primes: it has `11`-torsion. -/
theorem three_primary_of_no_other_prime_torsion {q : ℕ}
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (hp : ∀ p : ℕ, p.Prime → p ≠ q → ∀ b : A, p • b = 0 → b = 0) (a : A) :
    ∃ k : ℕ, (q ^ k) • a = 0 := by
  obtain ⟨m, hm, hma⟩ := htor a
  have hdvd : addOrderOf a ∣ m := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hma
  have hpos : 0 < addOrderOf a := Nat.pos_of_ne_zero fun h => by
    rw [h] at hdvd; omega
  have hkey : ∀ {d : ℕ}, d.Prime → d ∣ addOrderOf a → d = q := fun {d} hd hdd =>
    prime_dvd_addOrderOf_eq_of_no_torsion hp a hpos hd hdd
  have := Nat.eq_prime_pow_of_unique_prime_dvd (p := q) hpos.ne' hkey
  exact ⟨(addOrderOf a).primeFactorsList.length, by rw [← this, addOrderOf_nsmul_eq_zero]⟩

/-- **The assembly theorem.**  Let `A` be a torsion abelian group (the role of `Ш(E/ℚ)`) with

* `A[p] = 0` for every prime `p ≠ 3`   (`hp`), and
* `#A[3^∞] = 9`                        (`h3`, the proved `3`-primary input).

Then `#A = 9`.

This is the honest minimal sufficient condition for `FIN`.  It uses neither Cassels–Tate square
order nor the threshold `1089`, and it does not quantify over all levels `n`. -/
theorem card_eq_nine_of_prime_torsion_free
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (hp : ∀ p : ℕ, p.Prime → p ≠ 3 → ∀ b : A, p • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9) :
    Nat.card A = 9 := by
  have huniv : ∀ a : A, ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0 :=
    three_primary_of_no_other_prime_torsion htor hp
  have e : {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} ≃ A :=
    { toFun := fun a => a.1
      invFun := fun a => ⟨a, huniv a⟩
      left_inv := fun a => rfl
      right_inv := fun a => rfl }
  rw [← h3, Nat.card_congr e]

/-- **The retained implication, in the form the review states it.**  Let `A` be a torsion
abelian group (the role of `Ш(E/ℚ)`) with

* `A[p] = 0` for every prime `p ≥ 11`      (`hbig`, the outstanding arithmetic premise),
* `A[2] = A[5] = A[7] = 0`                 (`h2`, `h5`, `h7`, the known small-primary inputs),
* `#A[3^∞] = 9`                            (`h3`, the known `3`-primary input).

Then `#A = 9`.

Note what this does and does not say.  It is a *conditional*: the premise `A[p] = 0` for all
primes `p ≥ 11` is exactly the outstanding arithmetic problem, and formalising its consequence
proves no instance of it.  Its only content is that, granting the premise, the endgame needs no
square-order argument, no `1089` threshold and no quantification over composite levels. -/
theorem card_eq_nine_of_large_prime_torsion_free
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (hbig : ∀ p : ℕ, p.Prime → 11 ≤ p → ∀ b : A, p • b = 0 → b = 0)
    (h2 : ∀ b : A, (2 : ℕ) • b = 0 → b = 0)
    (h5 : ∀ b : A, (5 : ℕ) • b = 0 → b = 0)
    (h7 : ∀ b : A, (7 : ℕ) • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9) :
    Nat.card A = 9 := by
  refine card_eq_nine_of_prime_torsion_free htor ?_ h3
  intro p hpP hp3 b hb
  rcases lt_or_ge p 11 with hlt | hge
  · -- the primes below `11` are `2, 3, 5, 7`, and `3` is excluded by hypothesis
    interval_cases p <;> first
      | exact absurd hpP (by decide)
      | exact absurd rfl hp3
      | exact h2 b hb
      | exact h5 b hb
      | exact h7 b hb
  · exact hbig p hpP hge b hb

/-! ## The all-`n` bound is an equivalent reformulation, not an independent statement

The record proposed as its strongest target

    (A)  #Ш[n] < 1089 for every n ≥ 1.

The two theorems below make precise that this is *equivalent* to `#Ш = 9` under the retained
inputs, so it is a reformulation of the endpoint rather than a weaker statement: the forward
direction shows a uniform level-by-level bound already forces global finiteness with the same
bound, and the backward direction is immediate.  (The step from `#Ш < 1089` to `#Ш = 9` is the
Cassels–Tate square-order argument already machine-checked in the project's A1/A2 freeze.)

This does not make (A) worthless — an *independent proof* of an equivalent assertion still
solves the problem — but it does mean (A) cannot be advertised as a strictly easier target. -/

/-- **A uniform bound at every level forces global finiteness with the same bound.**
If `A` is torsion, each `A[n]` is finite, and `#A[n] < K` for every `n ≥ 1`, then `A` itself is
finite and `#A < K`.

Proof: a finite subset `s ⊆ A` lies in `A[n]` for `n = ∏_{a ∈ s} ord(a)`, so `#s < K`; a type all
of whose finite subsets have fewer than `K` elements is finite of cardinality `< K`. -/
theorem bounded_torsion_implies_finite (K : ℕ)
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (hfin : ∀ n : ℕ, 0 < n → Finite {a : A // (n : ℕ) • a = 0})
    (hbd : ∀ n : ℕ, 0 < n → Nat.card {a : A // (n : ℕ) • a = 0} < K) :
    Finite A ∧ Nat.card A < K := by
  have hord : ∀ a : A, 0 < addOrderOf a := by
    intro a
    obtain ⟨m, hm, hma⟩ := htor a
    have hd : addOrderOf a ∣ m := addOrderOf_dvd_iff_nsmul_eq_zero.mpr hma
    exact Nat.pos_of_ne_zero fun h => by rw [h] at hd; omega
  have key : ∀ s : Finset A, s.card < K := by
    intro s
    set n := ∏ a ∈ s, addOrderOf a with hn
    have hnpos : 0 < n := Finset.prod_pos fun a _ => hord a
    haveI := hfin n hnpos
    have hmem : ∀ a ∈ s, (n : ℕ) • a = 0 := fun a ha =>
      addOrderOf_dvd_iff_nsmul_eq_zero.mp (Finset.dvd_prod_of_mem _ ha)
    have hinj : Function.Injective
        (fun x : {x // x ∈ s} => (⟨x.1, hmem x.1 x.2⟩ : {a : A // (n : ℕ) • a = 0})) := by
      intro x y hxy
      exact Subtype.ext (by simpa using congrArg Subtype.val hxy)
    have h1 := Nat.card_le_card_of_injective _ hinj
    rw [Nat.card_eq_finsetCard] at h1
    have := hbd n hnpos
    omega
  have hAfin : Finite A := by
    rw [← Set.finite_univ_iff, ← Set.not_infinite]
    intro hinf
    obtain ⟨s, _, hcard⟩ := hinf.exists_subset_card_eq K
    have := key s; omega
  refine ⟨hAfin, ?_⟩
  haveI := Fintype.ofFinite A
  rw [Nat.card_eq_fintype_card, ← Finset.card_univ]
  exact key _

/-- The converse direction: a finite group of order `< K` satisfies the level-by-level bound. -/
theorem level_bound_of_card_lt [Finite A] (K : ℕ) (h : Nat.card A < K) (n : ℕ) :
    Nat.card {a : A // (n : ℕ) • a = 0} < K :=
  lt_of_le_of_lt (Nat.card_le_card_of_injective (fun x => x.1) Subtype.val_injective) h

/-- Contrapositive packaging: if `#A ≠ 9` while the `3`-primary part has order `9` and `A` is
torsion, then `A` has an element of prime order `p ≠ 3` — i.e. `Ш[p] ≠ 0` for some `p ≥ 11`
(the primes `2, 5, 7` being already excluded by the record). -/
theorem exists_bad_prime_of_card_ne_nine
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9)
    (hne : Nat.card A ≠ 9) :
    ∃ p : ℕ, p.Prime ∧ p ≠ 3 ∧ ∃ b : A, b ≠ 0 ∧ p • b = 0 := by
  by_contra hcon
  push_neg at hcon
  exact hne (card_eq_nine_of_prime_torsion_free htor
    (fun p hpP hp3 b hb => by
      by_contra hb0
      exact absurd hb (hcon p hpP hp3 b hb0)) h3)

/-- **Bookkeeping form of the retained implication after the `11`-primary input.**  Identical to
`card_eq_nine_of_large_prime_torsion_free` except that the `11`-primary component is now one of
the known inputs (imported from the completed `C₁₁` computation, see `IMPORTED_C11_INPUT.md`),
so the outstanding universal premise starts at `p ≥ 13`.

This is pure renumbering and is recorded only so that the file does not state a premise that has
been overtaken; the mathematical content added by the `11`-primary input is in
`RequestProject/ThresholdGap.lean` and `RequestProject/ThresholdSharpness.lean`. -/
theorem card_eq_nine_of_torsion_free_from_thirteen
    (htor : ∀ a : A, ∃ m : ℕ, 0 < m ∧ m • a = 0)
    (hbig : ∀ p : ℕ, p.Prime → 13 ≤ p → ∀ b : A, p • b = 0 → b = 0)
    (h2 : ∀ b : A, (2 : ℕ) • b = 0 → b = 0)
    (h5 : ∀ b : A, (5 : ℕ) • b = 0 → b = 0)
    (h7 : ∀ b : A, (7 : ℕ) • b = 0 → b = 0)
    (h11 : ∀ b : A, (11 : ℕ) • b = 0 → b = 0)
    (h3 : Nat.card {a : A // ∃ k : ℕ, ((3 : ℕ) ^ k) • a = 0} = 9) :
    Nat.card A = 9 := by
  refine card_eq_nine_of_prime_torsion_free htor ?_ h3
  intro p hpP hp3 b hb
  rcases lt_or_ge p 13 with hlt | hge
  · interval_cases p <;> first
      | exact absurd hpP (by decide)
      | exact absurd rfl hp3
      | exact h2 b hb
      | exact h5 b hb
      | exact h7 b hb
      | exact h11 b hb
  · exact hbig p hpP hge b hb

end SeedBSD
