module

public import Mathlib
public import RequestProject.Continuation.MiddleGround

/-!
# The frontier rule: one-sided detectors with finitely controlled zero sets

Lean source for `research_return/FRONTIER.md` and `research_return/REVISION_5.md`.

**Frontier rule.** An iff criterion is unnecessary and false positives are allowed. Success needs
a one-sided bad-prime detector `Ш[p] ≠ 0 ⇒ p ∣ Λ_p` together with finite or global control of the
detector's zero set. A candidate is not rejected just because it vanishes at a known-good prime.

As in `MiddleGround.lean`, "`Ш(E/ℚ)[p] ≠ 0`" is an abstract predicate `shaNonzero : ℕ → Prop`.
Every arithmetic input (Ota/Kato certificates, refined Mazur–Tate-type identities, rationality of
`q`) is an explicit hypothesis. Nothing about the seed curve is proved here.

* `detector_iff_certificate`: every certificate theorem "`X_p ≢ 0 (mod p) ⇒ Ш[p] = 0`" is
  *the same statement* as the one-sided detector "`Ш[p] ≠ 0 ⇒ p ∣ X_p`". So the record's
  certificate theorems are already detectors (Package A).
* `support_subset_zeroSet`: the support always lies inside the detector's zero set, whatever
  false positives that zero set contains. Only the zero set needs controlling.
* `TameCarrier`, `support_subset_of_tameCarrier`: the auxiliary-prime (K288) shape. The detector
  holds at every admissible auxiliary `ℓ`. The carrier needs only *one* admissible `ℓ` per `p`
  with `C(p,ℓ) ≡ (a_ℓ − 2)·W·R(p,ℓ)·u` for a fixed rational `W`. Then `Ш[p] ≠ 0 ⇒ p ∣ num W`.
* `support_subset_of_tameCarrier_288`: `W = 288` confines the support to `S₀ ∪ {2, 3}`.
* `support_subset_of_tame8q`: the Q36 bridge. If `q = a/b` is rational and the tame identity
  holds with `W = 8q`, the support lies in `S₀ ∪ primeFactors(8a)`. With `q = 36` this is `{2, 3}`.
* `k288_reconstruction_unique`: the nine recorded residues `w ≡ 288 (mod p)`, `p = 17, …, 47`,
  determine `288` among all rationals of height `≤ 3·10⁶`. This uses
  `MiddleGround.rational_reconstruction_unique`; the residues themselves are record data and are
  not recomputed here.
* `not_anomalous_of_even_trace`: at the seed, `a_p` is even (rational 2-torsion), so no good
  `p ≥ 7` is anomalous. The cyclotomic Euler factor `1 − 1/α_p` therefore adds no false positives.
* `dvd_of_valuationCarrier`: the valuation-threshold variant needed for the W3 four-value test,
  where the detector is `Ш[p] ≠ 0 ⇒ p^k ∣ V_p` rather than `p ∣ V_p`.
-/

@[expose] public section

namespace Frontier

/-- **Certificates are detectors.** For any family `X`, the certificate law
"`p ∤ X_p ⇒ Ш[p] = 0`" (outside `S₀`) is logically identical to the one-sided detector law
"`Ш[p] ≠ 0 ⇒ p ∣ X_p`". It says nothing about the converse, so false positives are allowed. -/
theorem detector_iff_certificate (shaNonzero : ℕ → Prop) (X : ℕ → ℤ) (S₀ : Set ℕ) :
    (∀ p : ℕ, p.Prime → p ∉ S₀ → ¬ (p : ℤ) ∣ X p → ¬ shaNonzero p) ↔
      (∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ X p) := by
  constructor
  · intro h p hp hpS hs
    by_contra hX
    exact h p hp hpS hX hs
  · intro h p hp hpS hX hs
    exact hX (h p hp hpS hs)

/-- The zero set of a detector: the primes `p` with `p ∣ X_p`. -/
def zeroSet (X : ℕ → ℤ) : Set ℕ := {p : ℕ | p.Prime ∧ (p : ℤ) ∣ X p}

/-- **False positives are harmless.** Under a one-sided detector, the bad-prime support lies in
`S₀ ∪ zeroSet X`. Known-good primes in the zero set cost nothing. Only the size of the zero set
matters. -/
theorem support_subset_zeroSet (shaNonzero : ℕ → Prop) (X : ℕ → ℤ) (S₀ : Set ℕ)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ X p) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ zeroSet X := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · exact Or.inr ⟨hp, hdet p hp hpS hs⟩

/-- A detector whose zero set is finite gives a finite bad-prime support. -/
theorem support_finite_of_zeroSet_finite (shaNonzero : ℕ → Prop) (X : ℕ → ℤ) (S₀ : Set ℕ)
    (hS₀ : S₀.Finite) (hZ : (zeroSet X).Finite)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ∣ X p) :
    {p : ℕ | p.Prime ∧ shaNonzero p}.Finite :=
  (hS₀.union hZ).subset (support_subset_zeroSet shaNonzero X S₀ hdet)

/-- **The auxiliary-prime carrier (K288 shape).** For each prime `p ∉ S₀` there is *some*
admissible auxiliary `ℓ` with `p ∤ A(p,ℓ)` (this is `a_ℓ − 2`), `p ∤ R(p,ℓ)` (the tame regulator) and
`Wd · C(p,ℓ) ≡ Wn · A(p,ℓ) · R(p,ℓ) · u (mod p)` for a `p`-unit `u`. Here `W = Wn / Wd` is one fixed
rational number, independent of `p` and `ℓ`. -/
def TameCarrier (C A R : ℕ → ℕ → ℤ) (adm : ℕ → ℕ → Prop) (Wn Wd : ℤ) (S₀ : Set ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∉ S₀ → ∃ ℓ : ℕ, adm p ℓ ∧ ¬ (p : ℤ) ∣ A p ℓ ∧ ¬ (p : ℤ) ∣ R p ℓ ∧
    ∃ u : ℤ, ¬ (p : ℤ) ∣ u ∧ (p : ℤ) ∣ Wd * C p ℓ - Wn * A p ℓ * R p ℓ * u

/-- Pointwise step: the detector at the chosen auxiliary plus the carrier congruence give `p ∣ Wn`. -/
theorem dvd_num_of_tameCarrier {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (hc : TameCarrier C A R adm Wn Wd S₀) {p : ℕ} (hp : p.Prime) (hpS : p ∉ S₀)
    (hdet : ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) : (p : ℤ) ∣ Wn := by
  obtain ⟨ℓ, hadm, hA, hR, u, hu, hdiv⟩ := hc p hp hpS
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  have h1 : (p : ℤ) ∣ Wd * C p ℓ := dvd_mul_of_dvd_right (hdet ℓ hadm) Wd
  have h2 : (p : ℤ) ∣ ((Wn * A p ℓ) * R p ℓ) * u := by simpa using dvd_sub h1 hdiv
  rcases hpZ.dvd_or_dvd h2 with h3 | h3
  · rcases hpZ.dvd_or_dvd h3 with h4 | h4
    · rcases hpZ.dvd_or_dvd h4 with h5 | h5
      · exact h5
      · exact absurd h5 hA
    · exact absurd h4 hR
  · exact absurd h3 hu

/-- **The K288 template.** Suppose the detector holds at every admissible auxiliary: the
contrapositive of the Ota-type certificate "`C(p,ℓ) ≢ 0 ⇒ Ш[p^∞] = 0`" (`detector_iff_certificate`).
Suppose also the carrier holds with a fixed rational `W = Wn / Wd`, `Wn ≠ 0`. Then the bad-prime
support lies in `S₀ ∪ primeFactors(Wn)`. The carrier needs only one good auxiliary per `p`, so
regulator-type accidental zeros at a single auxiliary are avoided by changing `ℓ`. -/
theorem support_subset_of_tameCarrier {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hWn : Wn ≠ 0) (hc : TameCarrier C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ (Wn.natAbs.primeFactors : Set ℕ) := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · right
    have h := dvd_num_of_tameCarrier hc hp hpS (hdet p hp hpS hs)
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp h, by simpa using hWn⟩

/-- Finite version of the K288 template. -/
theorem support_finite_of_tameCarrier {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {Wn Wd : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hWn : Wn ≠ 0) (hS₀ : S₀.Finite)
    (hc : TameCarrier C A R adm Wn Wd S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    {p : ℕ | p.Prime ∧ shaNonzero p}.Finite :=
  (hS₀.union (Finset.finite_toSet _)).subset
    (support_subset_of_tameCarrier shaNonzero hWn hc hdet)

/-- The primes dividing `288 = 2⁵·3²` are `2` and `3`. -/
theorem primeFactors_288 : (288 : ℕ).primeFactors = {2, 3} := by
  have h : (288 : ℕ) = 2 ^ 5 * 3 ^ 2 := by norm_num
  rw [h, Nat.primeFactors_mul (by norm_num) (by norm_num),
    Nat.primeFactors_prime_pow (by norm_num) Nat.prime_two,
    Nat.primeFactors_prime_pow (by norm_num) Nat.prime_three]
  rfl

/-- **K288 with the observed multiplier.** If the carrier holds with `W = 288` (the value
observed at `p = 17, …, 47`, which is not proved), the bad-prime support lies in `S₀ ∪ {2, 3}`. -/
theorem support_subset_of_tameCarrier_288 {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hc : TameCarrier C A R adm 288 1 S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ {2, 3} := by
  have h := support_subset_of_tameCarrier shaNonzero (by norm_num) hc hdet
  have e : ((288 : ℤ).natAbs.primeFactors : Set ℕ) = {2, 3} := by
    rw [show (288 : ℤ).natAbs = 288 from rfl, primeFactors_288]
    simp
  rwa [e] at h

/-- **The Q36 bridge, from the tame side.** Suppose `q = a / b` with `a ≠ 0`, and the direct tame
identity `b·C(p,ℓ) ≡ 8a·(a_ℓ − 2)·R(p,ℓ)·u` (that is, `C ≡ (a_ℓ − 2)·8q·R·u`) holds at one good
auxiliary per `p`. Then together with the Ota-type detector, `Ш[p] ≠ 0 ⇒ p ∣ 8a`. Rationality of
`q` and the identity are both hypotheses here; neither is proved. -/
theorem support_subset_of_tame8q {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop} {a b : ℤ}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (ha : a ≠ 0) (hc : TameCarrier C A R adm (8 * a) b S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ ((8 * a).natAbs.primeFactors : Set ℕ) :=
  support_subset_of_tameCarrier shaNonzero (by simpa using ha) hc hdet

/-- With `q = 36` exactly, the tame `8q` identity confines the support to `S₀ ∪ {2, 3}`. -/
theorem support_subset_of_tame8q_36 {C A R : ℕ → ℕ → ℤ} {adm : ℕ → ℕ → Prop}
    {S₀ : Set ℕ} (shaNonzero : ℕ → Prop) (hc : TameCarrier C A R adm (8 * 36) 1 S₀)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → ∀ ℓ : ℕ, adm p ℓ → (p : ℤ) ∣ C p ℓ) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ {2, 3} :=
  support_subset_of_tameCarrier_288 shaNonzero (by simpa using hc) hdet

/-- **Valuation-threshold carrier (W3 four-value shape).** Suppose the detector has the form
`Ш[p] ≠ 0 ⇒ p^k ∣ V_p` with `k ≥ 1`, and the carrier is `V_p ≡ p^(k-1) · I · u (mod p^k)` for a
`p`-unit `u`. Then `p^k ∣ V_p` forces `p ∣ I`. The first digit beyond `p^(k-1)` must be
controlled; a residue mod `p` alone is not enough. -/
theorem dvd_of_valuationCarrier {p k : ℕ} (hp : p.Prime) (hk : 1 ≤ k) {V I u : ℤ}
    (hu : ¬ (p : ℤ) ∣ u) (hcar : (p : ℤ) ^ k ∣ V - (p : ℤ) ^ (k - 1) * I * u)
    (hV : (p : ℤ) ^ k ∣ V) : (p : ℤ) ∣ I := by
  have hpZ : Prime (p : ℤ) := Nat.prime_iff_prime_int.mp hp
  have hk' : k = (k - 1) + 1 := by omega
  have h1 : (p : ℤ) ^ k ∣ (p : ℤ) ^ (k - 1) * (I * u) := by
    have := dvd_sub hV hcar
    simpa [mul_assoc] using this
  rw [hk', pow_succ] at h1
  have hp0 : ((p : ℤ) ^ (k - 1)) ≠ 0 := pow_ne_zero _ (by exact_mod_cast hp.ne_zero)
  have h2 : (p : ℤ) ∣ I * u := (mul_dvd_mul_iff_left hp0).mp h1
  rcases hpZ.dvd_or_dvd h2 with h | h
  · exact h
  · exact absurd h hu

/-- Support version of the valuation-threshold carrier with a fixed nonzero integer `I`. -/
theorem support_subset_of_valuationCarrier (shaNonzero : ℕ → Prop) (V : ℕ → ℤ) (k : ℕ)
    (hk : 1 ≤ k) (I : ℤ) (hI : I ≠ 0) (S₀ : Set ℕ)
    (hcar : ∀ p : ℕ, p.Prime → p ∉ S₀ →
      ∃ u : ℤ, ¬ (p : ℤ) ∣ u ∧ (p : ℤ) ^ k ∣ V p - (p : ℤ) ^ (k - 1) * I * u)
    (hdet : ∀ p : ℕ, p.Prime → p ∉ S₀ → shaNonzero p → (p : ℤ) ^ k ∣ V p) :
    {p : ℕ | p.Prime ∧ shaNonzero p} ⊆ S₀ ∪ (I.natAbs.primeFactors : Set ℕ) := by
  rintro p ⟨hp, hs⟩
  by_cases hpS : p ∈ S₀
  · exact Or.inl hpS
  · right
    obtain ⟨u, hu, hc⟩ := hcar p hp hpS
    have h := dvd_of_valuationCarrier hp hk hu hc (hdet p hp hpS hs)
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    exact ⟨hp, Int.natCast_dvd.mp h, by simpa using hI⟩

/-- **Cross-prime reconstruction of the K288 multiplier.** Let `M = 17·19·23·29·31·37·41·43·47`.
Suppose a rational `a/b` with `|a|, |b| ≤ 3·10⁶` reduces to `288` modulo each of these primes, in
CRT form `M ∣ 288·b − a`. Then `a/b = 288`. So, if the recorded residues are correct and the
normalization is fixed globally, no other small-height rational fits the nine primes. A random
family would be matched by a rational of height about `√(M/2) ≈ 3.2·10⁶`. -/
theorem k288_reconstruction_unique {a b : ℤ} (ha : |a| ≤ 3000000) (hb : |b| ≤ 3000000)
    (h : (20475850236047 : ℤ) ∣ b * 288 - a) : a = 288 * b := by
  have := MiddleGround.rational_reconstruction_unique (M := 20475850236047) (x := 288)
    (a := a) (b := b) (a' := 288) (b' := 1) (H := 3000000) h (by norm_num) ha hb
    (by norm_num) (by norm_num) (by norm_num)
  linarith

/-- **No anomalous primes for an even trace.** If `a_p` is even and satisfies the Hasse bound
`a_p² ≤ 4p` with `p ≥ 7`, then `p ∤ a_p − 1`. The seed has a rational 2-torsion point, so `a_p` is
even at every odd good prime and no such prime is anomalous. -/
theorem not_anomalous_of_even_trace {p : ℕ} {a : ℤ} (hp7 : 7 ≤ p) (heven : Even a)
    (hHasse : a ^ 2 ≤ 4 * (p : ℤ)) : ¬ (p : ℤ) ∣ a - 1 := by
  rintro ⟨k, hk⟩
  have hk0 : k ≠ 0 := by
    rintro rfl
    obtain ⟨r, hr⟩ := heven
    omega
  have hp : (7 : ℤ) ≤ p := by exact_mod_cast hp7
  have hk1 : 1 ≤ |k| := Int.one_le_abs hk0
  have habs : (p : ℤ) ≤ |a - 1| := by
    rw [hk, abs_mul, abs_of_nonneg (by linarith : (0 : ℤ) ≤ p)]
    nlinarith
  have hsq : ((p : ℤ) - 1) ^ 2 ≤ a ^ 2 := by
    have h1 : (p : ℤ) - 1 ≤ |a| := by
      have := abs_sub (a) 1
      simp at this
      linarith
    have h2 : (0 : ℤ) ≤ (p : ℤ) - 1 := by linarith
    calc ((p : ℤ) - 1) ^ 2 ≤ |a| ^ 2 := by gcongr
      _ = a ^ 2 := sq_abs a
  nlinarith

end Frontier

end
