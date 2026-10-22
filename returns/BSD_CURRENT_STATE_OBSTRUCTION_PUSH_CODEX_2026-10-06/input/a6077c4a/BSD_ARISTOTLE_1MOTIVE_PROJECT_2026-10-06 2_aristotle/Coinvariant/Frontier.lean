import Mathlib

/-!
# The frontier: one-sided detectors controlled by a fixed integer

Abstract logic for the diagnosis "easy quantities are too weak, strong quantities collapse to FIN".
Throughout, `Z p` stands for the per-prime statement `Ш(E/ℚ)[p] = 0`, and `T p` for a candidate
per-prime target (receiver bound, `h_p ≤ 2`, `ν_p ≤ 2`, a W3 coefficient being a `p`-unit, ...).

* `CollapsesCofinitely T Z`: `T p ↔ Z p` for all but finitely many `p`. Then a cofinite theorem
  for `T` is literally a cofinite theorem for `Z` (`cofinite_iff_of_collapse`).
* A single prime with `Z p ∧ ¬ T p` (the `p = 17` behaviour of `ℓ₂`) shows `T` does not
  characterize `Z` (`not_iff_of_false_alarm`). It does **not** stop `T` from being a useful
  one-sided detector; only the size of the false-alarm set matters (`finite_of_detector`).
* The intermediate theorem being looked for (`bad_primes_dvd_fixed_integer`): if
  `Λ_p ≡ I · u_p (mod p)` with `I ≠ 0` fixed and `u_p` a `p`-unit, **and** `Ш[p] ≠ 0` forces
  `p ∣ Λ_p`, then every bad prime divides `I`, so the bad primes are finite.

The second hypothesis (the detection bridge) is not implied by the congruence; it must be proved
separately for whatever `Λ` is used. It is one-sided, which is why it can be easier than FIN.
-/

namespace Frontier

open Filter

variable {T Z : ℕ → Prop}

/-- A per-prime target `T` collapses to `Z` if they agree for all but finitely many primes. -/
def CollapsesCofinitely (T Z : ℕ → Prop) : Prop := ∀ᶠ p in cofinite, (T p ↔ Z p)

/-- A collapsing target gives nothing beyond `Z` on the infinite tail. -/
theorem cofinite_iff_of_collapse (h : CollapsesCofinitely T Z) :
    (∀ᶠ p in cofinite, T p) ↔ (∀ᶠ p in cofinite, Z p) := by
  constructor
  · intro hT; filter_upwards [hT, h] with p hp hiff using hiff.1 hp
  · intro hZ; filter_upwards [hZ, h] with p hp hiff using hiff.2 hp

/-- One prime where `Z` holds but the target fails shows the target does not characterize `Z`. -/
theorem not_iff_of_false_alarm (h : ∃ p, Z p ∧ ¬ T p) : ¬ ∀ p, (T p ↔ Z p) := by
  rintro hall
  obtain ⟨p, hz, ht⟩ := h
  exact ht ((hall p).2 hz)

/-- A one-sided detector suffices: if every bad prime raises the alarm `D` and only finitely many
primes raise it, the bad primes are finite — whatever the false alarms are. -/
theorem finite_of_detector {D : ℕ → Prop} (hdet : ∀ p, ¬ Z p → D p)
    (hfin : {p | D p}.Finite) : {p | ¬ Z p}.Finite :=
  hfin.subset fun p hp => hdet p hp

/-- The intermediate theorem template. If `Λ p ≡ I * u p (mod p)` with `u p` a `p`-unit, and a
nonzero `Ш[p]` forces `p ∣ Λ p`, then every bad prime divides the fixed integer `I`. -/
theorem bad_prime_dvd (Λ u : ℕ → ℤ) (I : ℤ) (p : ℕ) (hp : p.Prime)
    (hcong : Λ p ≡ I * u p [ZMOD p]) (hunit : ¬ (p : ℤ) ∣ u p)
    (hdet : ¬ Z p → (p : ℤ) ∣ Λ p) (hbad : ¬ Z p) : (p : ℤ) ∣ I := by
  have h1 : (p : ℤ) ∣ I * u p :=
    (Int.ModEq.dvd_iff hcong).1 (hdet hbad)
  have hpr : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  rcases hpr.dvd_or_dvd h1 with h | h
  · exact h
  · exact absurd h hunit

/-- With `I ≠ 0`, the bad primes lie among the prime factors of `I`; in particular they are
finitely many. -/
theorem bad_primes_dvd_fixed_integer (Λ u : ℕ → ℤ) (I : ℤ) (hI : I ≠ 0)
    (hcong : ∀ p : ℕ, p.Prime → Λ p ≡ I * u p [ZMOD p])
    (hunit : ∀ p : ℕ, p.Prime → ¬ (p : ℤ) ∣ u p)
    (hdet : ∀ p : ℕ, p.Prime → ¬ Z p → (p : ℤ) ∣ Λ p) :
    {p | p.Prime ∧ ¬ Z p} ⊆ (I.natAbs.primeFactors : Set ℕ) ∧
      {p | p.Prime ∧ ¬ Z p}.Finite := by
  have hsub : {p | p.Prime ∧ ¬ Z p} ⊆ (I.natAbs.primeFactors : Set ℕ) := by
    rintro p ⟨hp, hbad⟩
    have hd := bad_prime_dvd Λ u I p hp (hcong p hp) (hunit p hp) (hdet p hp) hbad
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp hd, Int.natAbs_ne_zero.mpr hI⟩
  exact ⟨hsub, (Finset.finite_toSet _).subset hsub⟩

/-- The congruence alone is not enough: without the detection bridge, a target with
`Λ p ≡ I · u p` can hold at a bad prime. Concretely, with `Λ = I = u = 1` and every prime bad,
the congruence and unit conditions hold but no prime divides `Λ p`. -/
theorem congruence_without_bridge_insufficient :
    ∃ (Λ u : ℕ → ℤ) (I : ℤ), I ≠ 0 ∧ (∀ p : ℕ, p.Prime → Λ p ≡ I * u p [ZMOD p]) ∧
      (∀ p : ℕ, p.Prime → ¬ (p : ℤ) ∣ u p) ∧ ¬ ∀ p : ℕ, p.Prime → (p : ℤ) ∣ Λ p := by
  refine ⟨fun _ => 1, fun _ => 1, 1, one_ne_zero, fun p _ => by simp [Int.ModEq], ?_, ?_⟩
  · intro p hp h
    have := Int.eq_one_of_dvd_one (by positivity) h
    exact hp.one_lt.ne' (by exact_mod_cast this)
  · intro h
    have := Int.eq_one_of_dvd_one (by positivity) (h 2 Nat.prime_two)
    norm_num at this

/-- Instance: if `ν_p = 1 + dim Ш[p]` and `dim Ш[p]` is even for all but finitely many `p`, then
`ν_p ≤ 2` collapses to `Ш[p] = 0`. -/
theorem nu_collapses (ν sha : ℕ → ℕ)
    (hν : ∀ᶠ p in cofinite, ν p = 1 + sha p) (hpar : ∀ᶠ p in cofinite, Even (sha p)) :
    CollapsesCofinitely (fun p => ν p ≤ 2) (fun p => sha p = 0) := by
  filter_upwards [hν, hpar] with p h1 ⟨k, hk⟩
  omega

end Frontier
