import Mathlib
import Coinvariant.Frontier

/-!
# The shared frontier rule for the parallel probes

Every probe works under one rule:

> An iff criterion is unnecessary. False positives are allowed. Success requires a one-sided
> bad-prime detector plus finite/global control of the detector's zero set. Do not reject a
> candidate merely because it vanishes at a known-good prime.

`Z p` stands for `Ш(E/ℚ)[p] = 0`, and `Λ p ∈ ℤ` for a candidate detector value at `p`
(a residual W3 coefficient, a normalized `p`-adic leading term, a fixed integer built from the
global leading term, ...). The alarm at `p` is `p ∣ Λ p`.

The results here make the rule precise and split the work into its two independent halves.

* `detector_architecture`: bridge (`¬ Z p → p ∣ Λ p`) plus a finite alarm set gives finitely many
  bad primes. Neither half needs the converse of the other.
* `false_alarms_harmless`: adding any finite set of false alarms, including alarms at primes known
  to be good, does not affect the conclusion.
* `exists_fixed_carrier_iff_finite_alarms`: the "fixed `I_E`" condition
  `Λ_p ≡ I_E u_p (mod p)` with `I_E ≠ 0` and `u_p` a `p`-unit is **equivalent** to the alarm set
  `{p ∣ Λ_p}` being finite. With `u_p` unconstrained, a fixed carrier carries no information beyond
  the finiteness of the alarm set. A structural carrier (determinant, resultant, congruence ideal,
  ...) is valuable because it *proves* that finiteness, not because the congruence itself says more.
* `per_prime_carrier_always_exists`, `per_prime_carrier_useless`: if the carrier may depend on `p`,
  the congruence always holds, even when every prime raises the alarm. So a "global object"
  assembled separately for each `p` proves nothing.
* `alarms_unit_mul`: rescaling a detector by `p`-units does not change its alarms, so the bridge
  and the zero-set control may use normalizations that differ by `p`-units.
* `int_alarm_finite`, `rat_alarm_finite`: for a detector of the form `p ∣ I` with `I` a fixed nonzero
  integer, or `p` dividing the numerator of a fixed nonzero rational, zero-set control is automatic.
  In that case (the global/Q36 lane) the whole problem is the bridge.
-/

namespace Frontier

variable {Z : ℕ → Prop}

/-- The alarm set of a detector `Λ`: primes `p` with `p ∣ Λ p`. -/
def alarms (Λ : ℕ → ℤ) : Set ℕ := {p | p.Prime ∧ (p : ℤ) ∣ Λ p}

/-- **The detector architecture.** One-sided bridge plus finite alarm set gives finitely many bad
primes. False alarms are allowed. -/
theorem detector_architecture (Λ : ℕ → ℤ)
    (bridge : ∀ p : ℕ, p.Prime → ¬ Z p → (p : ℤ) ∣ Λ p)
    (hfin : (alarms Λ).Finite) : {p | p.Prime ∧ ¬ Z p}.Finite :=
  hfin.subset fun p ⟨hp, hbad⟩ => ⟨hp, bridge p hp hbad⟩

/-- **False alarms are harmless.** If the alarm set is contained in a finite set `F ∪ G`, where
`G` may contain primes known to be good, then the bad primes are still finite. A candidate is not
disqualified by vanishing at a known-good prime. -/
theorem false_alarms_harmless (Λ : ℕ → ℤ) (F G : Set ℕ) (hF : F.Finite) (hG : G.Finite)
    (bridge : ∀ p : ℕ, p.Prime → ¬ Z p → (p : ℤ) ∣ Λ p)
    (hsub : alarms Λ ⊆ F ∪ G) : {p | p.Prime ∧ ¬ Z p}.Finite :=
  detector_architecture Λ bridge ((hF.union hG).subset hsub)

/-- A fixed carrier forces a finite alarm set: every alarm prime divides `I`. -/
theorem alarms_subset_of_carrier (Λ u : ℕ → ℤ) (I : ℤ)
    (hcong : ∀ p : ℕ, p.Prime → Λ p ≡ I * u p [ZMOD p])
    (hunit : ∀ p : ℕ, p.Prime → ¬ (p : ℤ) ∣ u p) :
    alarms Λ ⊆ {p | p.Prime ∧ (p : ℤ) ∣ I} := by
  rintro p ⟨hp, hd⟩
  have h1 : (p : ℤ) ∣ I * u p := (Int.ModEq.dvd_iff (hcong p hp)).1 hd
  rcases (Nat.prime_iff_prime_int.mp hp).dvd_or_dvd h1 with h | h
  · exact ⟨hp, h⟩
  · exact absurd h (hunit p hp)

/-- For a fixed nonzero integer `I`, the primes dividing `I` are finite. -/
theorem int_alarm_finite (I : ℤ) (hI : I ≠ 0) : {p : ℕ | p.Prime ∧ (p : ℤ) ∣ I}.Finite := by
  refine (Finset.finite_toSet I.natAbs.primeFactors).subset ?_
  rintro p ⟨hp, hd⟩
  simp only [Finset.mem_coe, Nat.mem_primeFactors]
  exact ⟨hp, Int.natCast_dvd.mp hd, Int.natAbs_ne_zero.mpr hI⟩

/-- For a fixed nonzero rational `q`, the primes dividing its numerator are finite. -/
theorem rat_alarm_finite (q : ℚ) (hq : q ≠ 0) :
    {p : ℕ | p.Prime ∧ (p : ℤ) ∣ q.num}.Finite :=
  int_alarm_finite q.num (Rat.num_ne_zero.mpr hq)

/-- **Fixed carrier ⟺ finite alarm set.** A fixed nonzero `I` and `p`-units `u_p` with
`Λ_p ≡ I u_p (mod p)` for every prime exist exactly when only finitely many primes divide `Λ_p`. -/
theorem exists_fixed_carrier_iff_finite_alarms (Λ : ℕ → ℤ) :
    (∃ (I : ℤ) (u : ℕ → ℤ), I ≠ 0 ∧ (∀ p : ℕ, p.Prime → Λ p ≡ I * u p [ZMOD p]) ∧
        (∀ p : ℕ, p.Prime → ¬ (p : ℤ) ∣ u p)) ↔ (alarms Λ).Finite := by
  constructor
  · rintro ⟨I, u, hI, hcong, hunit⟩
    exact (int_alarm_finite I hI).subset (alarms_subset_of_carrier Λ u I hcong hunit)
  · intro hfin
    classical
    set S := hfin.toFinset
    set I : ℤ := ∏ q ∈ S, (q : ℤ)
    have hmemS : ∀ q, q ∈ S ↔ q.Prime ∧ (q : ℤ) ∣ Λ q := by
      intro q; simp [S, alarms]
    have hI : I ≠ 0 := by
      refine Finset.prod_ne_zero_iff.mpr fun q hq => ?_
      exact_mod_cast ((hmemS q).1 hq).1.ne_zero
    -- a prime outside `S` does not divide `I`
    have hnotdvd : ∀ p : ℕ, p.Prime → p ∉ S → ¬ (p : ℤ) ∣ I := by
      intro p hp hpS hd
      obtain ⟨q, hq, hpq⟩ :=
        (Prime.dvd_finset_prod_iff (Nat.prime_iff_prime_int.mp hp) _).1 hd
      have hqp := ((hmemS q).1 hq).1
      have : p ∣ q := Int.natCast_dvd_natCast.mp hpq
      have hpq' : p = q := (Nat.prime_dvd_prime_iff_eq hp hqp).1 this
      exact hpS (hpq' ▸ hq)
    refine ⟨I, fun p => if p ∈ S then 1 else Λ p * I ^ (p - 2), hI, ?_, ?_⟩
    · intro p hp
      by_cases hpS : p ∈ S
      · simp only [hpS, if_true, mul_one]
        have h1 : (p : ℤ) ∣ Λ p := ((hmemS p).1 hpS).2
        have h2 : (p : ℤ) ∣ I := Finset.dvd_prod_of_mem _ hpS
        exact (Int.modEq_zero_iff_dvd.mpr h1).trans (Int.modEq_zero_iff_dvd.mpr h2).symm
      · simp only [hpS, if_false]
        have hcop : IsCoprime I p := by
          have hpr := Nat.prime_iff_prime_int.mp hp
          exact ((Prime.coprime_iff_not_dvd hpr).mpr (hnotdvd p hp hpS)).symm
        have hferm := Int.ModEq.pow_card_sub_one_eq_one hp hcop
        have hp2 : p - 1 = (p - 2) + 1 := by have := hp.two_le; omega
        have : I * (Λ p * I ^ (p - 2)) = Λ p * I ^ (p - 1) := by
          rw [hp2, pow_succ]; ring
        rw [this]
        calc Λ p = Λ p * 1 := (mul_one _).symm
          _ ≡ Λ p * I ^ (p - 1) [ZMOD p] := (Int.ModEq.mul_left _ hferm).symm
    · intro p hp
      by_cases hpS : p ∈ S
      · simp only [hpS, if_true]
        intro h
        have := Int.eq_one_of_dvd_one (by positivity) h
        exact hp.one_lt.ne' (by exact_mod_cast this)
      · simp only [hpS, if_false]
        intro h
        have hpr := Nat.prime_iff_prime_int.mp hp
        rcases hpr.dvd_or_dvd h with h | h
        · exact hpS ((hmemS p).2 ⟨hp, h⟩)
        · exact hnotdvd p hp hpS (hpr.dvd_of_dvd_pow h)

/-- A carrier that may depend on `p` always exists, for any `Λ`: take `I_p = Λ_p + p` when that is
nonzero, otherwise `I_p = 2p`, and `u_p = 1`. -/
theorem per_prime_carrier_always_exists (Λ : ℕ → ℤ) :
    ∃ I : ℕ → ℤ, ∀ p : ℕ, p.Prime → I p ≠ 0 ∧ Λ p ≡ I p * 1 [ZMOD p] := by
  classical
  refine ⟨fun p => if Λ p + p = 0 then 2 * p else Λ p + p, fun p hp => ?_⟩
  have hp0 : (p : ℤ) ≠ 0 := by exact_mod_cast hp.ne_zero
  by_cases h : Λ p + p = 0
  · simp only [h, if_true, mul_one]
    refine ⟨by positivity, ?_⟩
    have hΛ : Λ p = -p := by linarith
    rw [hΛ]
    exact (Int.modEq_zero_iff_dvd.mpr (by simp)).trans
      (Int.modEq_zero_iff_dvd.mpr (dvd_mul_left _ _)).symm
  · simp only [h, if_false, mul_one]
    refine ⟨h, ?_⟩
    simp [Int.ModEq, Int.add_emod_right]

/-- **Per-prime carriers prove nothing.** Even for `Λ = 0`, where every prime raises the alarm,
nonzero per-prime carriers satisfying the congruence exist. -/
theorem per_prime_carrier_useless :
    ∃ (Λ : ℕ → ℤ) (I : ℕ → ℤ), (∀ p : ℕ, p.Prime → I p ≠ 0 ∧ Λ p ≡ I p * 1 [ZMOD p]) ∧
      ¬ (alarms Λ).Finite := by
  obtain ⟨I, hI⟩ := per_prime_carrier_always_exists (fun _ => 0)
  refine ⟨fun _ => 0, I, hI, ?_⟩
  have : alarms (fun _ => (0 : ℤ)) = {p | p.Prime} := by
    ext p; simp [alarms]
  rw [this]
  exact Nat.infinite_setOf_prime

/-- **Normalizations may differ by `p`-units.** If `Λ' p = v p * Λ p` with `v p` a `p`-unit, the two
detectors raise exactly the same alarms. So the bridge (probe A) and the zero-set control (probe B)
may be proved for different normalizations of the same quantity, provided they differ by `p`-units.
-/
theorem alarms_unit_mul (Λ v : ℕ → ℤ) (hv : ∀ p : ℕ, p.Prime → ¬ (p : ℤ) ∣ v p) :
    alarms (fun p => v p * Λ p) = alarms Λ := by
  ext p
  simp only [alarms, Set.mem_setOf_eq]
  constructor
  · rintro ⟨hp, h⟩
    rcases (Nat.prime_iff_prime_int.mp hp).dvd_or_dvd h with h | h
    · exact absurd h (hv p hp)
    · exact ⟨hp, h⟩
  · rintro ⟨hp, h⟩
    exact ⟨hp, dvd_mul_of_dvd_right h _⟩

end Frontier
