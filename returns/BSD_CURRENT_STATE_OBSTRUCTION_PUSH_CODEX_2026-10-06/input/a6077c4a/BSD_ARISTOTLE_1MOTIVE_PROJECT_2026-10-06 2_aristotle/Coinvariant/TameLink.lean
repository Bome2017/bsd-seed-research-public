import Mathlib
import Coinvariant.DetectorRule

/-!
# The one open link of the tame route: `x_p ≡ W (mod p)`

Abstract logic only; every arithmetic input is a named hypothesis. Record facts used as
hypotheses (not re-derived here, see `FRONTIER.md`, "Record facts imported 2026-10-06"):

* **G2** gives, for each `p` outside a finite set, an admissible `ℓ` with `(a_ℓ − 2)·R_{p,ℓ} ≢ 0`.
* **Theorem W** gives one scalar `x_p` per prime with `C_2(p,ℓ) ≡ (a_ℓ − 2)·x_p·R_{p,ℓ} (mod p)`.
* **Record fact 4** (BKS II): `x_p = x_{ℚ,Σ}·#Ш[p^∞]` up to a `p`-adic unit, and `x_p = 0` when the
  Selmer corank exceeds 2. We encode this as `x p ≡ xK p * s p * v p (mod p)` with `v p` a
  `p`-unit and `p ∣ s p ↔ Ш[p] ≠ 0` (`s p` a representative of `#Ш[p^∞]`, or `0`).

Notation: `Z p` stands for `Ш(E/ℚ)[p] = 0`; `B` is a finite exceptional set of primes.

Results:
* `dvd_x_iff`, `bad_dvd_x`: under record fact 4, `p ∣ x_p ⟺ p ∣ x_{ℚ,Σ} ∨ Ш[p] ≠ 0`.
* `link_detects`: the link `x_p ≡ W·u_p` (`W ≠ 0` fixed, `u_p` a `p`-unit) alone puts every bad
  prime outside `B` among the prime factors of `W`. G2, Theorem W and `C_2` are **not** needed for
  detection; they only make `x_p` computable.
* `link_iff_fin_and_kato` (**main**): the existence form of the link (some fixed `W ≠ 0`, arbitrary
  `p`-units) holds **iff** FIN holds **and** `x_{ℚ,Σ}` is a `p`-adic unit for all but finitely many
  `p`. So the link contains FIN outright; its `Ш`-free remainder is the Kato-unit statement.
* `x_eq_of_tame`, `C2_zero_iff`: at a G2 auxiliary prime, `x_p = C_2/((a_ℓ−2)R)` and
  `C_2(p,ℓ) ≡ 0 ⟺ p ∣ x_{ℚ,Σ} ∨ Ш[p] ≠ 0`.
* `nine_primes_good`: where `x_p ≡ 288` (the nine audited primes `17, …, 47`), `Ш[p] = 0` and
  `x_{ℚ,Σ}` is a `p`-unit. This is per-prime certification, not a tail bound.
-/

namespace TameLink

open Frontier

/-- Under record fact 4 at one prime: `p ∣ x ⟺ p ∣ xK ∨ p ∣ s`. -/
theorem dvd_x_iff (p : ℕ) (hp : p.Prime) (x xK s v : ℤ) (hfac : x ≡ xK * s * v [ZMOD p])
    (hv : ¬ (p : ℤ) ∣ v) : (p : ℤ) ∣ x ↔ (p : ℤ) ∣ xK ∨ (p : ℤ) ∣ s := by
  have hpr := Nat.prime_iff_prime_int.mp hp
  rw [Int.ModEq.dvd_iff hfac]
  constructor
  · intro h
    rcases hpr.dvd_or_dvd h with h | h
    · exact hpr.dvd_or_dvd h
    · exact absurd h hv
  · rintro (h | h)
    · exact Dvd.dvd.mul_right (Dvd.dvd.mul_right h _) _
    · exact Dvd.dvd.mul_right (Dvd.dvd.mul_left h _) _

/-- Record fact 4 makes `x_p` a detector with an automatic bridge: `Ш[p] ≠ 0 ⇒ p ∣ x_p`. -/
theorem bad_dvd_x {Z : ℕ → Prop} (p : ℕ) (hp : p.Prime) (x xK s v : ℤ)
    (hfac : x ≡ xK * s * v [ZMOD p]) (hv : ¬ (p : ℤ) ∣ v) (hs : (p : ℤ) ∣ s ↔ ¬ Z p)
    (hbad : ¬ Z p) : (p : ℤ) ∣ x :=
  (dvd_x_iff p hp x xK s v hfac hv).2 (Or.inr (hs.2 hbad))

/-- **The link alone detects.** If `Ш[p] ≠ 0 ⇒ p ∣ x_p` and `x_p ≡ W·u_p` with `W ≠ 0` fixed and
`u_p` a `p`-unit (for `p ∉ B`), then every bad prime outside `B` divides `W`. -/
theorem link_detects {Z : ℕ → Prop} (B : Set ℕ) (x u : ℕ → ℤ) (W : ℤ)
    (hbridge : ∀ p : ℕ, p.Prime → p ∉ B → ¬ Z p → (p : ℤ) ∣ x p)
    (hlink : ∀ p : ℕ, p.Prime → p ∉ B → x p ≡ W * u p [ZMOD p])
    (hu : ∀ p : ℕ, p.Prime → p ∉ B → ¬ (p : ℤ) ∣ u p) :
    {p | p.Prime ∧ ¬ Z p} ⊆ B ∪ {p | p.Prime ∧ (p : ℤ) ∣ W} := by
  rintro p ⟨hp, hbad⟩
  by_cases hB : p ∈ B
  · exact Or.inl hB
  · right
    refine ⟨hp, ?_⟩
    have h1 : (p : ℤ) ∣ W * u p := (Int.ModEq.dvd_iff (hlink p hp hB)).1 (hbridge p hp hB hbad)
    rcases (Nat.prime_iff_prime_int.mp hp).dvd_or_dvd h1 with h | h
    · exact h
    · exact absurd h (hu p hp hB)

/-- The link as stated in the record: a fixed `W ≠ 0` with `x_p ≡ W·u_p`, `u_p` a `p`-unit, for
all primes `p ∉ B`. -/
def Link (B : Set ℕ) (x : ℕ → ℤ) : Prop :=
  ∃ W : ℤ, W ≠ 0 ∧ ∀ p : ℕ, p.Prime → p ∉ B →
    ∃ u : ℤ, ¬ (p : ℤ) ∣ u ∧ x p ≡ W * u [ZMOD p]

/-- Outside a finite exceptional set, the link is equivalent to finiteness of the alarm set. -/
theorem link_iff_finite_alarms (B : Set ℕ) (hB : B.Finite) (x : ℕ → ℤ) :
    Link B x ↔ (alarms x).Finite := by
  constructor
  · rintro ⟨W, hW, h⟩
    refine (hB.union (int_alarm_finite W hW)).subset ?_
    rintro p ⟨hp, hd⟩
    by_cases hpB : p ∈ B
    · exact Or.inl hpB
    · right
      obtain ⟨u, hu, hc⟩ := h p hp hpB
      refine ⟨hp, ?_⟩
      have h1 : (p : ℤ) ∣ W * u := (Int.ModEq.dvd_iff hc).1 hd
      rcases (Nat.prime_iff_prime_int.mp hp).dvd_or_dvd h1 with h | h
      · exact h
      · exact absurd h hu
  · intro hfin
    obtain ⟨I, u, hI, hc, hu⟩ := (exists_fixed_carrier_iff_finite_alarms x).2 hfin
    exact ⟨I, hI, fun p hp _ => ⟨u p, hu p hp, hc p hp⟩⟩

/-- **Main result.** Under record fact 4 (outside the finite set `B`), the existence form of the
open link is equivalent to

  FIN (finitely many `p` with `Ш[p] ≠ 0`)  **and**  `x_{ℚ,Σ}` a `p`-unit for almost all `p`.

So any proof of the link proves FIN; the part of the link not about `Ш` is exactly the statement
that Kato's coordinate `x_{ℚ,Σ}` is cofinitely a `p`-adic unit. -/
theorem link_iff_fin_and_kato {Z : ℕ → Prop} (B : Set ℕ) (hB : B.Finite) (x xK s v : ℕ → ℤ)
    (hfac : ∀ p : ℕ, p.Prime → p ∉ B → x p ≡ xK p * s p * v p [ZMOD p])
    (hv : ∀ p : ℕ, p.Prime → p ∉ B → ¬ (p : ℤ) ∣ v p)
    (hs : ∀ p : ℕ, p.Prime → p ∉ B → ((p : ℤ) ∣ s p ↔ ¬ Z p)) :
    Link B x ↔ ({p | p.Prime ∧ ¬ Z p}.Finite ∧ (alarms xK).Finite) := by
  rw [link_iff_finite_alarms B hB]
  have key : ∀ p, p.Prime → p ∉ B → ((p : ℤ) ∣ x p ↔ (p : ℤ) ∣ xK p ∨ ¬ Z p) := by
    intro p hp hpB
    rw [dvd_x_iff p hp _ _ _ _ (hfac p hp hpB) (hv p hp hpB), hs p hp hpB]
  constructor
  · intro hfin
    refine ⟨(hB.union hfin).subset ?_, (hB.union hfin).subset ?_⟩
    · rintro p ⟨hp, hbad⟩
      by_cases hpB : p ∈ B
      · exact Or.inl hpB
      · exact Or.inr ⟨hp, (key p hp hpB).2 (Or.inr hbad)⟩
    · rintro p ⟨hp, hd⟩
      by_cases hpB : p ∈ B
      · exact Or.inl hpB
      · exact Or.inr ⟨hp, (key p hp hpB).2 (Or.inl hd)⟩
  · rintro ⟨hbad, hK⟩
    refine ((hB.union hbad).union hK).subset ?_
    rintro p ⟨hp, hd⟩
    by_cases hpB : p ∈ B
    · exact Or.inl (Or.inl hpB)
    · rcases (key p hp hpB).1 hd with h | h
      · exact Or.inr ⟨hp, h⟩
      · exact Or.inl (Or.inr ⟨hp, h⟩)

/-- At a G2 auxiliary prime the tame data computes `x_p`: `x_p = C_2 / ((a_ℓ − 2) R)`. -/
theorem x_eq_of_tame (p : ℕ) [Fact p.Prime] (C2 a R x : ZMod p)
    (hid : C2 = (a - 2) * x * R) (hnd : (a - 2) * R ≠ 0) : x = C2 / ((a - 2) * R) := by
  rw [hid, eq_div_iff hnd]; ring

/-- At a G2 auxiliary prime, with record fact 4: `C_2(p,ℓ) ≡ 0 ⟺ p ∣ x_{ℚ,Σ} ∨ Ш[p] ≠ 0`.
So the computable tame alarm set is exactly the bad primes together with the non-unit primes of
Kato's coordinate. -/
theorem C2_zero_iff {Z : ℕ → Prop} (p : ℕ) [hp : Fact p.Prime] (C2 a R : ZMod p)
    (x xK s v : ℤ) (hid : C2 = (a - 2) * (x : ZMod p) * R) (hnd : (a - 2) * R ≠ 0)
    (hfac : x ≡ xK * s * v [ZMOD p]) (hv : ¬ (p : ℤ) ∣ v) (hs : (p : ℤ) ∣ s ↔ ¬ Z p) :
    C2 = 0 ↔ (p : ℤ) ∣ xK ∨ ¬ Z p := by
  rw [← hs, ← dvd_x_iff p hp.out x xK s v hfac hv, ← ZMod.intCast_zmod_eq_zero_iff_dvd, hid]
  constructor
  · intro h
    by_contra hx
    exact hnd (by
      have : (a - 2) * R * (x : ZMod p) = 0 := by rw [← h]; ring
      exact (mul_eq_zero.1 this).resolve_right hx)
  · intro h; rw [h]; ring

/-- `288 = 2⁵·3²` is a unit modulo each of the nine audited primes. -/
theorem two_eighty_eight_ne_zero :
    ∀ p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℕ), ¬ (p : ℤ) ∣ 288 := by
  decide

/-- **Nine-prime certification.** If `x_p ≡ 288` at an audited prime `p ∈ {17, …, 47}`, record
fact 4 gives `Ш[p] = 0` and `p ∤ x_{ℚ,Σ}`. This certifies those primes one at a time; it is not a
bound on the tail. -/
theorem nine_primes_good {Z : ℕ → Prop} (p : ℕ)
    (hp9 : p ∈ ({17, 19, 23, 29, 31, 37, 41, 43, 47} : Finset ℕ)) (x xK s v : ℤ)
    (hx : x ≡ 288 [ZMOD p]) (hfac : x ≡ xK * s * v [ZMOD p]) (hv : ¬ (p : ℤ) ∣ v)
    (hs : (p : ℤ) ∣ s ↔ ¬ Z p) : Z p ∧ ¬ (p : ℤ) ∣ xK := by
  have hp : p.Prime := by
    simp only [Finset.mem_insert, Finset.mem_singleton] at hp9
    rcases hp9 with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> norm_num
  have hnx : ¬ (p : ℤ) ∣ x := by
    rw [Int.ModEq.dvd_iff hx]; exact two_eighty_eight_ne_zero p hp9
  rw [dvd_x_iff p hp x xK s v hfac hv, hs] at hnx
  push_neg at hnx
  exact ⟨hnx.2, hnx.1⟩

end TameLink
