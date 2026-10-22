module

public import Mathlib

/-!
# The middle-ground target: a fixed global integer controlling the family `Ш[p]`

New Lean source for the fourth 2026-10-06 continuation (see `research_return/REVISION_4.md`).

The frontier is: find a global object whose finite arithmetic controls the family of `Ш[p]`
without already being `Ш`.  The prototype is the W3 weight-direction test

  `Λ_p ≡ I_E · u_p (mod p)`,  `I_E ∈ ℤ \ {0}` fixed,  `u_p` a `p`-unit,

which, together with a one-way detection law `Ш[p] ≠ 0 ⇒ p ∣ Λ_p`, would give
`Ш[p] ≠ 0 ⇒ p ∣ I_E`.  This file records exactly what that template does and does not give.

A family `Λ_p` is modelled by a function `Λ : ℕ → ℤ` (an integer representative of `Λ_p mod p`).
The predicate "`Ш(E/ℚ)[p] ≠ 0`" is an abstract `shaNonzero : ℕ → Prop`; nothing about `Ш` is
assumed beyond the detection hypothesis stated in each theorem.

* `support_subset_of_fixedIntegerControl`, `support_finite_of_fixedIntegerControl`: the
  reduction of the infinite tail to the prime divisors of one integer.
* `exists_fixedIntegerControl_iff_finite`: **caveat** — the bare existence of such an `I_E` is
  equivalent to finiteness of `{p : p ∣ Λ_p}`.  So the displayed congruence has content only
  through a mechanism that produces `I_E` independently of `p` (e.g. a fixed global element);
  it cannot be confirmed by observing that `Λ_p ≢ 0 (mod p)` at finitely many primes.
* `RationalSpecialization`, `support_finite_of_rationalSpecialization`: the version with teeth —
  `Λ_p` is the reduction mod `p` of one fixed rational number `a / b`.
* `rational_reconstruction_unique`: a fixed rational of height `≤ H` is determined by its
  residues modulo `M = ∏ p` as soon as `2 H² < M`.  This is what makes a cross-prime test of the
  "fixed global element" hypothesis falsifiable.
* `support_subset_of_q36_control`: the Q36 template — a (missing) bridge turning the global
  leading term `36` into a support constraint would confine `Ш[p] ≠ 0` to `p ∈ {2, 3}`.
-/

@[expose] public section

namespace MiddleGround

/-- `Λ_p ≡ I · u_p (mod p)` with `u_p` a `p`-unit, for every prime `p` outside a finite
exceptional set `S₀`. -/
def FixedIntegerControl (Λ : ℕ → ℤ) (I : ℤ) (S₀ : Set ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∉ S₀ → ∃ u : ℤ, ¬ (p : ℤ) ∣ u ∧ (p : ℤ) ∣ Λ p - I * u

/-- Under fixed-integer control, `p ∣ Λ_p` forces `p ∣ I`. -/
theorem dvd_of_fixedIntegerControl {Λ : ℕ → ℤ} {I : ℤ} {S₀ : Set ℕ}
    (hc : FixedIntegerControl Λ I S₀) {p : ℕ} (hp : p.Prime) (hpS : p ∉ S₀)
    (hΛ : (p : ℤ) ∣ Λ p) : (p : ℤ) ∣ I := by
  obtain ⟨u, hu, hdiv⟩ := hc p hp hpS
  have hIu : (p : ℤ) ∣ I * u := by
    have := dvd_sub hΛ hdiv
    simpa using this
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  rcases hpZ.dvd_or_dvd hIu with h | h
  · exact h
  · exact absurd h hu

/-- **The intermediate theorem template.**  If `Ш[p] ≠ 0 ⇒ p ∣ Λ_p` outside `S₀` and `Λ` is
controlled by a fixed nonzero integer `I`, then every prime with `Ш[p] ≠ 0` lies in `S₀` or divides `I`. -/
theorem support_subset_of_fixedIntegerControl {Λ : ℕ → ℤ} {I : ℤ} {S₀ : Set ℕ}
    (shaNonzero : ℕ → Prop) (hI0 : I ≠ 0) (hc : FixedIntegerControl Λ I S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ Λ p) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ (I.natAbs.primeFactors : Set ℕ) := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · right
    have hI := dvd_of_fixedIntegerControl hc hp hpS (hdet p hp hpS hs)
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp hI, by simpa using hI0⟩

/-- Finite version: with `I ≠ 0` and `S₀` finite, `{p : Ш[p] ≠ 0}` is finite. -/
theorem support_finite_of_fixedIntegerControl {Λ : ℕ → ℤ} {I : ℤ} {S₀ : Set ℕ}
    (shaNonzero : ℕ → Prop) (hI0 : I ≠ 0) (hS₀ : S₀.Finite) (hc : FixedIntegerControl Λ I S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ Λ p) :
    {p : ℕ | p.Prime ∧ shaNonzero p}.Finite :=
  (hS₀.union (Finset.finite_toSet _)).subset
    (support_subset_of_fixedIntegerControl shaNonzero hI0 hc hdet)

/-- **Caveat.**  Over all primes, the existence of a nonzero `I` with fixed-integer control is
equivalent to the finiteness of the vanishing set `{p : p ∣ Λ_p}`.  Hence the congruence
`Λ_p ≡ I_E u_p` is, by itself, just a restatement of "`Λ_p ≢ 0 (mod p)` for cofinitely many
`p`"; its value lies entirely in a `p`-independent mechanism producing `I_E`. -/
theorem exists_fixedIntegerControl_iff_finite (Λ : ℕ → ℤ) :
    (∃ I : ℤ, I ≠ 0 ∧ FixedIntegerControl Λ I ∅) ↔
      {p : ℕ | p.Prime ∧ (p : ℤ) ∣ Λ p}.Finite := by
  constructor
  · rintro ⟨I, hI, hc⟩
    refine (Finset.finite_toSet I.natAbs.primeFactors).subset ?_
    rintro p ⟨hp, hΛ⟩
    have h := dvd_of_fixedIntegerControl hc hp (Set.notMem_empty p) hΛ
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp h, by simpa using hI⟩
  · intro hfin
    set S := hfin.toFinset with hSdef
    refine ⟨((∏ q ∈ S, q : ℕ) : ℤ), ?_, ?_⟩
    · have : (∏ q ∈ S, q : ℕ) ≠ 0 := by
        rw [Finset.prod_ne_zero_iff]
        intro q hq
        have := ((Set.Finite.mem_toFinset hfin).mp hq).1
        exact this.ne_zero
      exact_mod_cast this
    · intro p hp _
      by_cases hpS : p ∈ S
      · refine ⟨1, ?_, ?_⟩
        · intro h
          have : (p : ℤ) ∣ 1 := h
          exact hp.one_lt.ne' (by exact_mod_cast Int.eq_one_of_dvd_one (by positivity) this)
        · have hΛ := ((Set.Finite.mem_toFinset hfin).mp hpS).2
          have hI : (p : ℤ) ∣ ((∏ q ∈ S, q : ℕ) : ℤ) :=
            Int.natCast_dvd_natCast.mpr (Finset.dvd_prod_of_mem _ hpS)
          simpa using dvd_sub hΛ hI
      · have hΛ : ¬ (p : ℤ) ∣ Λ p := fun h =>
          hpS ((Set.Finite.mem_toFinset hfin).mpr ⟨hp, h⟩)
        set I : ℤ := ((∏ q ∈ S, q : ℕ) : ℤ)
        have hpI : ¬ (p : ℤ) ∣ I := by
          intro h
          have h' : p ∣ ∏ q ∈ S, q := Int.natCast_dvd_natCast.mp h
          obtain ⟨q, hq, hpq⟩ := (Prime.dvd_finset_prod_iff hp.prime _).mp h'
          have hqp : q.Prime := ((Set.Finite.mem_toFinset hfin).mp hq).1
          have : p = q := (Nat.prime_dvd_prime_iff_eq hp hqp).mp hpq
          exact hpS (this ▸ hq)
        haveI : Fact p.Prime := ⟨hp⟩
        have hIz : (I : ZMod p) ≠ 0 := by
          rwa [Ne, ZMod.intCast_zmod_eq_zero_iff_dvd]
        have hΛz : (Λ p : ZMod p) ≠ 0 := by
          rwa [Ne, ZMod.intCast_zmod_eq_zero_iff_dvd]
        refine ⟨Λ p * I ^ (p - 2), ?_, ?_⟩
        · rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
          push_cast
          exact mul_ne_zero hΛz (pow_ne_zero _ hIz)
        · rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
          push_cast
          have hferm : (I : ZMod p) ^ (p - 1) = 1 := ZMod.pow_card_sub_one_eq_one hIz
          have hp2 : p - 1 = (p - 2) + 1 := by have := hp.two_le; omega
          rw [hp2, pow_succ] at hferm
          linear_combination (-(Λ p : ZMod p)) * hferm

/-- `Λ_p` is the reduction mod `p` of one fixed rational number `a / b`, for every prime `p`
outside a finite set `S₀`: `p ∣ b Λ_p − a`. -/
def RationalSpecialization (Λ : ℕ → ℤ) (a b : ℤ) (S₀ : Set ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∉ S₀ → (p : ℤ) ∣ b * Λ p - a

/-- A fixed rational specialization with nonzero numerator vanishes mod `p` only at the finitely
many primes dividing the numerator (or lying in `S₀`); so with a detection law,
`{p : Ш[p] ≠ 0}` is finite. -/
theorem support_finite_of_rationalSpecialization {Λ : ℕ → ℤ} {a b : ℤ} {S₀ : Set ℕ}
    (shaNonzero : ℕ → Prop) (ha : a ≠ 0) (hS₀ : S₀.Finite)
    (hspec : RationalSpecialization Λ a b S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ Λ p) :
    {p : ℕ | p.Prime ∧ shaNonzero p}.Finite := by
  refine (hS₀.union (Finset.finite_toSet a.natAbs.primeFactors)).subset ?_
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · right
    have h1 : (p : ℤ) ∣ b * Λ p := dvd_mul_of_dvd_right (hdet p hp hpS hs) b
    have h2 : (p : ℤ) ∣ a := by simpa using dvd_sub h1 (hspec p hp hpS)
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp h2, by simpa using ha⟩

/-- **Falsifiability of the cross-prime test.**  If `x` is a residue modulo `M` (e.g. the CRT lift
of the observed `Λ_p mod p` over a batch of primes with product `M`) and two rationals `a/b`,
`a'/b'` of height `≤ H` both match it, then they are equal as soon as `2 H² < M`.  Thus residues
at enough primes determine the candidate fixed global element, and a random family of residues
generically admits no small-height match. -/
theorem rational_reconstruction_unique {M x a b a' b' H : ℤ}
    (h1 : M ∣ b * x - a) (h2 : M ∣ b' * x - a')
    (ha : |a| ≤ H) (hb : |b| ≤ H) (ha' : |a'| ≤ H) (hb' : |b'| ≤ H)
    (hM : 2 * H ^ 2 < M) : a * b' = a' * b := by
  have hdvd : M ∣ a' * b - a * b' := by
    have := dvd_sub (dvd_mul_of_dvd_left h1 b') (dvd_mul_of_dvd_left h2 b)
    have e : (b * x - a) * b' - (b' * x - a') * b = a' * b - a * b' := by ring
    rwa [e] at this
  have hH : 0 ≤ H := le_trans (abs_nonneg a) ha
  have habs : |a' * b - a * b'| < M := by
    calc |a' * b - a * b'| ≤ |a' * b| + |a * b'| := abs_sub _ _
      _ = |a'| * |b| + |a| * |b'| := by rw [abs_mul, abs_mul]
      _ ≤ H * H + H * H := by
          gcongr
      _ = 2 * H ^ 2 := by ring
      _ < M := hM
  have := Int.eq_zero_of_abs_lt_dvd hdvd habs
  linarith

/-- The only primes dividing the global leading term `36` are `2` and `3`. -/
theorem prime_dvd_thirtySix {p : ℕ} (hp : p.Prime) (h : p ∣ 36) : p = 2 ∨ p = 3 := by
  have h36 : (36 : ℕ) = 2 ^ 2 * 3 ^ 2 := by norm_num
  rw [h36] at h
  rcases (Nat.Prime.dvd_mul hp).mp h with h | h
  · exact Or.inl ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp (hp.dvd_of_dvd_pow h))
  · exact Or.inr ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_three).mp (hp.dvd_of_dvd_pow h))

/-- **The Q36 template.**  If a (currently missing) rank-two bridge gave the support law
`Ш[p] ≠ 0 ⇒ p ∣ 36` outside a finite set `S₀`, then every prime with `Ш[p] ≠ 0` lies in `S₀`
or is `2` or `3` — whose primary parts are already certified separately in the record. -/
theorem support_subset_of_q36_control (shaNonzero : ℕ → Prop) (S₀ : Set ℕ)
    (hbridge : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → p ∣ 36) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ {2, 3} := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · exact Or.inr (prime_dvd_thirtySix hp (hbridge p hp hpS hs))

end MiddleGround

end
