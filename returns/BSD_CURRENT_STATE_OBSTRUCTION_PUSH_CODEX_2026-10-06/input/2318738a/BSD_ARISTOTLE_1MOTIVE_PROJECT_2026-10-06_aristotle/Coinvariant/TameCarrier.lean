import Mathlib

/-!
# The tame (Ota) detector with a global scalar `W`, and the `W = 8q` interval argument

Abstract logic for the route "tame Ota detector + K288 global scalar". Nothing here is a
statement about the curve; the arithmetic inputs appear as named hypotheses.

* `Sha0 p` stands for `Ш(E/ℚ)[p] = 0`.
* `C2 p ℓ : ZMod p` is the tame quantity `C_2(p, ℓ) mod p`, `a ℓ` is `a_ℓ`, `R p ℓ` is
  `R_{p,ℓ} mod p`, `u p ℓ` the unit `u_{p,ℓ}`, and `W` the candidate global scalar.
* `Adm p ℓ` says the auxiliary prime `ℓ` is admissible for `p` (the hypotheses under which the
  Ota bridge is available).

Results:
* `tame_bad_prime_dvd_W`: the missing identity `C_2 = (a_ℓ - 2) R W u (mod p)` at one admissible
  `ℓ` with `a_ℓ - 2`, `R`, `u` nonzero mod `p`, together with the Ota bridge
  `Ш[p] ≠ 0 ⇒ C_2(p, ℓ) ≡ 0`, forces `p ∣ W`.
* `tame_tail_of_W_eq_288`: with `W = 288 = 2⁵·3²`, `Ш[p] = 0` for every prime `p ≥ 5` outside
  the exceptional set `B`.
* `W_eq_288_of_eq_eight_q`: if `W = 8q` with `W ∈ ℤ` and `35.99427 < q < 36.00573`, then
  `W = 288` and `q = 36`.
* `W_eq_288_of_small_denominator`: the same conclusion if only `d W ∈ ℤ` for some `1 ≤ d ≤ 21`.
* `denominator_22_not_enough`: the bound `21` is sharp: `288 - 1/22 = 8q` for a `q` in the
  interval.
* `integer_pinned_by_nine_residues` / `rational_pinned_by_nine_residues`: an integer `W` with
  `|W| < M`, or a rational `a/b` with `|a| + 288|b| < M`, that is `≡ 288` modulo each of the
  nine primes `17, …, 47` equals `288`; here `M = 17·19·23·29·31·37·41·43·47 = 20475850236047`.
* `carrier_unique`: two integer carriers agreeing modulo infinitely many primes are equal.
-/

namespace TameCarrier

open Filter

/-- **One prime.** The tame identity at one admissible auxiliary prime, with the other factors
nonzero mod `p`, plus the Ota bridge, forces `p ∣ W` at a bad prime. -/
theorem tame_bad_prime_dvd_W (Sha0 : Prop) (p : ℕ) [Fact p.Prime] (C2 R u a W : ZMod p)
    (hid : C2 = (a - 2) * R * W * u) (ha : a - 2 ≠ 0) (hR : R ≠ 0) (hu : u ≠ 0)
    (hota : ¬ Sha0 → C2 = 0) (hbad : ¬ Sha0) : W = 0 := by
  have h := hota hbad
  rw [hid] at h
  simp only [mul_eq_zero] at h
  tauto

/-- **The non-vanishing of `R` is part of the target.** If at some prime both `C_2(p, ℓ)` and
`R_{p,ℓ}` vanish for every auxiliary `ℓ`, the tame identity holds there for *every* scalar `W`
(for instance `W = 1`), so it detects nothing at that prime. Hence the tail theorem needs, for
each `p` outside `B`, some `ℓ` with `R_{p,ℓ} ≠ 0`, proved independently of `Ш[p]`. -/
theorem identity_vacuous_if_R_vanishes (p : ℕ) (C2 R u a : ℕ → ZMod p)
    (hC : ∀ ℓ, C2 ℓ = 0) (hR : ∀ ℓ, R ℓ = 0) :
    ∀ W : ZMod p, ∀ ℓ, C2 ℓ = (a ℓ - 2) * R ℓ * W * u ℓ := by
  intro W ℓ; rw [hC, hR]; ring

/-- **The tail theorem template.** Suppose that for every prime `p ≥ 5` outside `B` there is an
admissible auxiliary `ℓ` (changing `ℓ` is allowed when `R_{p,ℓ}` vanishes accidentally) at which
the tame identity holds with `a_ℓ - 2`, `R_{p,ℓ}`, `u_{p,ℓ}` nonzero mod `p`, and that the Ota
bridge holds at admissible `ℓ`. Then every bad prime `p ≥ 5` outside `B` divides `W`. -/
theorem tame_bad_primes_dvd_W (Sha0 : ℕ → Prop) (Adm : ℕ → ℕ → Prop)
    (C2 R u : (p : ℕ) → ℕ → ZMod p) (a : ℕ → ℤ) (W : ℤ) (B : Set ℕ)
    (hgood : ∀ p : ℕ, p.Prime → 5 ≤ p → p ∉ B → ∃ ℓ, Adm p ℓ ∧
      C2 p ℓ = ((a ℓ : ZMod p) - 2) * R p ℓ * (W : ZMod p) * u p ℓ ∧
      (a ℓ : ZMod p) - 2 ≠ 0 ∧ R p ℓ ≠ 0 ∧ u p ℓ ≠ 0)
    (hota : ∀ p ℓ, p.Prime → Adm p ℓ → ¬ Sha0 p → C2 p ℓ = 0) :
    ∀ p : ℕ, p.Prime → 5 ≤ p → p ∉ B → ¬ Sha0 p → (p : ℤ) ∣ W := by
  intro p hp h5 hB hbad
  haveI := Fact.mk hp
  obtain ⟨ℓ, hadm, hid, ha, hR, hu⟩ := hgood p hp h5 hB
  have := tame_bad_prime_dvd_W (Sha0 p) p (C2 p ℓ) (R p ℓ) (u p ℓ) (a ℓ) (W : ZMod p)
    hid ha hR hu (hota p ℓ hp hadm) hbad
  exact (ZMod.intCast_zmod_eq_zero_iff_dvd W p).mp this

/-- **`W = 288` closes the infinite tail.** Since `288 = 2⁵·3²` has no prime factor `≥ 5`, the
template gives `Ш[p] = 0` for every prime `p ≥ 5` outside `B`. -/
theorem tame_tail_of_W_eq_288 (Sha0 : ℕ → Prop) (Adm : ℕ → ℕ → Prop)
    (C2 R u : (p : ℕ) → ℕ → ZMod p) (a : ℕ → ℤ) (B : Set ℕ)
    (hgood : ∀ p : ℕ, p.Prime → 5 ≤ p → p ∉ B → ∃ ℓ, Adm p ℓ ∧
      C2 p ℓ = ((a ℓ : ZMod p) - 2) * R p ℓ * ((288 : ℤ) : ZMod p) * u p ℓ ∧
      (a ℓ : ZMod p) - 2 ≠ 0 ∧ R p ℓ ≠ 0 ∧ u p ℓ ≠ 0)
    (hota : ∀ p ℓ, p.Prime → Adm p ℓ → ¬ Sha0 p → C2 p ℓ = 0) :
    ∀ p : ℕ, p.Prime → 5 ≤ p → p ∉ B → Sha0 p := by
  intro p hp h5 hB
  by_contra hbad
  have hd := tame_bad_primes_dvd_W Sha0 Adm C2 R u a 288 B hgood hota p hp h5 hB hbad
  have hd' : p ∣ 288 := by exact_mod_cast hd
  have h288 : (288 : ℕ) = 2 ^ 5 * 3 ^ 2 := by norm_num
  rw [h288] at hd'
  rcases (Nat.Prime.dvd_mul hp).mp hd' with h | h
  · have := Nat.le_of_dvd (by norm_num) (hp.dvd_of_dvd_pow h); omega
  · have := Nat.le_of_dvd (by norm_num) (hp.dvd_of_dvd_pow h); omega

/-- **`W = 8q` with `W ∈ ℤ` forces `W = 288` and `q = 36`**, from the rigorous interval
`35.99427 < q < 36.00573`. -/
theorem W_eq_288_of_eq_eight_q (q : ℝ) (W : ℤ) (hW : (W : ℝ) = 8 * q)
    (hlo : 35.99427 < q) (hhi : q < 36.00573) : W = 288 ∧ q = 36 := by
  have h1 : (287 : ℝ) < W := by rw [hW]; linarith
  have h2 : (W : ℝ) < 289 := by rw [hW]; linarith
  have h1' : (287 : ℤ) < W := by exact_mod_cast h1
  have h2' : W < 289 := by exact_mod_cast h2
  have hW288 : W = 288 := by omega
  refine ⟨hW288, ?_⟩
  rw [hW288] at hW
  push_cast at hW
  linarith

/-- **Small denominator lattice suffices.** If `W = 8q` is only known to satisfy `d W ∈ ℤ` for
some `1 ≤ d ≤ 21`, the interval still forces `W = 288` and `q = 36`. -/
theorem W_eq_288_of_small_denominator (q W : ℝ) (d : ℕ) (k : ℤ) (hd1 : 1 ≤ d) (hd : d ≤ 21)
    (hk : (d : ℝ) * W = k) (hW : W = 8 * q) (hlo : 35.99427 < q) (hhi : q < 36.00573) :
    W = 288 ∧ q = 36 := by
  have hdpos : (0 : ℝ) < d := by exact_mod_cast hd1
  have hd21 : (d : ℝ) ≤ 21 := by exact_mod_cast hd
  have hlo' : (288 : ℝ) * d - 1 < k := by
    rw [← hk, hW]; nlinarith
  have hhi' : (k : ℝ) < 288 * d + 1 := by
    rw [← hk, hW]; nlinarith
  have e1 : (288 : ℤ) * d - 1 < k := by exact_mod_cast hlo'
  have e2 : k < (288 : ℤ) * d + 1 := by exact_mod_cast hhi'
  have hkeq : k = 288 * d := by omega
  have hW288 : W = 288 := by
    have : (d : ℝ) * W = (d : ℝ) * 288 := by rw [hk, hkeq]; push_cast; ring
    exact mul_left_cancel₀ hdpos.ne' this
  exact ⟨hW288, by linarith⟩

/-- **Sharpness of the denominator bound.** With denominator `22` the interval no longer
identifies `W`: `W = 288 - 1/22` satisfies `22 W ∈ ℤ` and `W = 8q` with `q` in the interval. -/
theorem denominator_22_not_enough :
    ∃ q W : ℝ, (22 : ℝ) * W = (6335 : ℤ) ∧ W = 8 * q ∧ 35.99427 < q ∧ q < 36.00573 ∧
      W ≠ 288 := by
  refine ⟨(288 - 1 / 22) / 8, 288 - 1 / 22, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- The product of the nine tested coefficient primes. -/
def nineModulus : ℤ := 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47

lemma nineModulus_eq : nineModulus = 20475850236047 := by norm_num [nineModulus]

lemma dvd_nineModulus_of_forall (n : ℤ)
    (h : ∀ p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℤ), p ∣ n) :
    nineModulus ∣ n := by
  have c : ∀ a b : ℤ, IsCoprime a b → a ∣ n → b ∣ n → a * b ∣ n :=
    fun a b hab ha hb => hab.mul_dvd ha hb
  simp only [Finset.mem_insert, Finset.mem_singleton, forall_eq_or_imp, forall_eq] at h
  obtain ⟨h17, h19, h23, h29, h31, h37, h41, h43, h47⟩ := h
  unfold nineModulus
  refine c _ _ ?_ (c _ _ ?_ (c _ _ ?_ (c _ _ ?_ (c _ _ ?_ (c _ _ ?_ (c _ _ ?_
    (c _ _ ?_ h17 h19) h23) h29) h31) h37) h41) h43) h47 <;>
    · rw [Int.isCoprime_iff_gcd_eq_one]; rfl

/-- **The nine residues pin an integer carrier.** An integer `W` with `|W| < M - 288` that is
`≡ 288` modulo each of the nine primes `17, …, 47` equals `288`. -/
theorem integer_pinned_by_nine_residues (W : ℤ) (hsize : |W| < 20475850236047 - 288)
    (h : ∀ p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℤ), W ≡ 288 [ZMOD p]) :
    W = 288 := by
  have hM := dvd_nineModulus_of_forall (W - 288) (fun p hp => (Int.ModEq.dvd (h p hp).symm))
  rw [nineModulus_eq] at hM
  obtain ⟨c, hc⟩ := hM
  rcases abs_lt.mp hsize with ⟨h1, h2⟩
  have : c = 0 := by
    rcases lt_trichotomy c 0 with hc0 | hc0 | hc0
    · nlinarith
    · exact hc0
    · nlinarith
  rw [this] at hc; linarith

/-- **The nine residues pin a small-height rational carrier.** If `W = a/b` with
`a ≡ 288 b` modulo each of the nine primes and `|a| + 288|b| < M`, then `a = 288 b`. -/
theorem rational_pinned_by_nine_residues (a b : ℤ)
    (hsize : |a| + 288 * |b| < 20475850236047)
    (h : ∀ p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℤ), a ≡ 288 * b [ZMOD p]) :
    a = 288 * b := by
  have hM := dvd_nineModulus_of_forall (a - 288 * b)
    (fun p hp => (Int.ModEq.dvd (h p hp).symm))
  rw [nineModulus_eq] at hM
  obtain ⟨c, hc⟩ := hM
  have habs : |a - 288 * b| < 20475850236047 := by
    calc |a - 288 * b| ≤ |a| + |288 * b| := abs_sub _ _
      _ = |a| + 288 * |b| := by rw [abs_mul]; norm_num
      _ < _ := hsize
  rw [hc] at habs
  rcases abs_lt.mp habs with ⟨h1, h2⟩
  have : c = 0 := by
    rcases lt_trichotomy c 0 with hc0 | hc0 | hc0
    · nlinarith
    · exact hc0
    · nlinarith
  rw [this] at hc; linarith

/-- **Uniqueness of an integer carrier.** If two integers agree modulo infinitely many primes,
they are equal. So the value of a global integer carrier is determined by its residues; the open
question is its *existence*, not its value. -/
theorem carrier_unique (W W' : ℤ)
    (h : {p : ℕ | p.Prime ∧ (W : ZMod p) = (W' : ZMod p)}.Infinite) : W = W' := by
  by_contra hne
  have hsub : {p : ℕ | p.Prime ∧ (W : ZMod p) = (W' : ZMod p)} ⊆
      ((W - W').natAbs.primeFactors : Set ℕ) := by
    rintro p ⟨hp, he⟩
    have : (p : ℤ) ∣ W - W' := by
      rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]; push_cast; rw [he, sub_self]
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp this, Int.natAbs_ne_zero.mpr (sub_ne_zero.mpr hne)⟩
  exact h ((Finset.finite_toSet _).subset hsub)

end TameCarrier
