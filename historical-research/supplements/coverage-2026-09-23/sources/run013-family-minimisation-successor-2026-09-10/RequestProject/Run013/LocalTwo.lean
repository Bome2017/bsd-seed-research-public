/-
Run013 — `LocalTwo.lean`

The exact `2`-adic exclusion in the `phi_q` orientation
(`src/local_2/LOCAL_2.md` §1, `evidence/DESCENT_DERIVATION.md` Lemma 3.2).

For `q ≡ 5 (mod 8)` and an odd square-class representative `D`, a `ℚ_2`-point of the
covering
  `C^{(phi)}_{q,D} : n^2 = D u^4 + 30 q u^2 v^2 - (31 q^2 / D) v^4`
forces `D ≡ 1 (mod 4)`, i.e. `D` lies in the local Kummer image `{1, q}` of `Q_2^*/Q_2^{*2}`.

The finite step is a kernel `decide` over the explicitly enumerated residues modulo `16`;
the reduction of the genuine `ℚ_2` statement to that finite check is proved.
-/
import RequestProject.Run013.PadicTools

namespace Run013

open PadicInt

/-- Squares modulo `16`. -/
lemma sq_mod16 (x : ZMod 16) : x ^ 2 = 0 ∨ x ^ 2 = 1 ∨ x ^ 2 = 4 ∨ x ^ 2 = 9 := by
  revert x; decide

lemma sq_mod16_mem (x : ZMod 16) : x ^ 2 ∈ ([0, 1, 4, 9] : List (ZMod 16)) := by
  rcases sq_mod16 x with h | h | h | h <;> simp [h]

lemma intCast_zmod_mod (n : ℕ) [NeZero n] (D : ℤ) : (D : ZMod n) = ((D % (n : ℤ) : ℤ) : ZMod n) := by
  rw [ZMod.intCast_eq_intCast_iff]
  exact (Int.emod_emod_of_dvd _ dvd_rfl).symm

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
/-- The finite mod-`16` core of the `2`-adic exclusion. -/
theorem local2_phi_mod16 :
    ∀ D ∈ ([1, 3, 5, 7, 9, 11, 13, 15] : List (ZMod 16)),
    ∀ q ∈ ([5, 13] : List (ZMod 16)),
    ∀ A ∈ ([0, 1, 4, 9] : List (ZMod 16)),
    ∀ B ∈ ([0, 1, 4, 9] : List (ZMod 16)),
    ∀ C ∈ ([0, 1, 4, 9] : List (ZMod 16)),
      (A = 1 ∨ B = 1) →
      C = D ^ 3 * A ^ 2 + 30 * q * D ^ 2 * A * B - 31 * q ^ 2 * D * B ^ 2 →
      (D = 1 ∨ D = 5 ∨ D = 9 ∨ D = 13) := by decide

set_option maxHeartbeats 2000000 in
/-- **Local exclusion at `2` for the `phi_q` covering.** -/
theorem local2_phi (q : ℕ) (hq : q % 8 = 5) (D : ℤ) (hDodd : ¬ (2 : ℤ) ∣ D)
    (h : Cov ℚ_[2] ((30 * q : ℤ) : ℚ_[2]) ((-31 * q ^ 2 : ℤ) : ℚ_[2]) ((D : ℤ) : ℚ_[2])) :
    D % 4 = 1 := by
  have hDne : D ≠ 0 := by rintro rfl; exact hDodd ⟨0, by ring⟩
  have hD0 : ((D : ℤ) : ℚ_[2]) ≠ 0 := Int.cast_ne_zero.mpr hDne
  rw [cov_iff_covM hD0] at h
  have h' : CovM ℚ_[2] ((((30 * q : ℤ)) : ℤ_[2]) : ℚ_[2]) ((((-31 * q ^ 2 : ℤ)) : ℤ_[2]) : ℚ_[2])
      ((((D : ℤ)) : ℤ_[2]) : ℚ_[2]) := by simpa using h
  obtain ⟨U, V, M, hUV, hM⟩ := covM_integral (((30 * q : ℤ)) : ℤ_[2]) (((-31 * q ^ 2 : ℤ)) : ℤ_[2])
    (((D : ℤ)) : ℤ_[2]) h'
  -- push the identity into `ZMod 16`
  have hf := congrArg (PadicInt.toZModPow 4 : ℤ_[2] →+* ZMod 16) hM
  simp only [map_mul, map_pow, map_add, map_intCast] at hf
  set u : ZMod 16 := (PadicInt.toZModPow 4 : ℤ_[2] →+* ZMod 16) U with hu
  set v : ZMod 16 := (PadicInt.toZModPow 4 : ℤ_[2] →+* ZMod 16) V with hv
  set m : ZMod 16 := (PadicInt.toZModPow 4 : ℤ_[2] →+* ZMod 16) M with hm
  have hfd : ((D : ℤ) : ZMod 16) = (D : ZMod 16) := by ring
  have key : m ^ 2 = (D : ZMod 16) ^ 3 * (u ^ 2) ^ 2
      + 30 * (q : ZMod 16) * (D : ZMod 16) ^ 2 * u ^ 2 * v ^ 2
      - 31 * (q : ZMod 16) ^ 2 * (D : ZMod 16) * (v ^ 2) ^ 2 := by
    rw [hf]; push_cast; ring
  -- the residue of `q`
  have hqmem : (q : ZMod 16) ∈ ([5, 13] : List (ZMod 16)) := by
    have h1 : q % 16 = 5 ∨ q % 16 = 13 := by omega
    have h2 : (q : ZMod 16) = ((q % 16 : ℕ) : ZMod 16) := (ZMod.natCast_mod q 16).symm
    rcases h1 with h | h <;> rw [h] at h2 <;> simp [h2]
  -- the residue of `D`
  have hDcast : (D : ZMod 16) = ((D % 16 : ℤ) : ZMod 16) := intCast_zmod_mod 16 D
  have hDmod : D % 16 = 1 ∨ D % 16 = 3 ∨ D % 16 = 5 ∨ D % 16 = 7 ∨ D % 16 = 9 ∨ D % 16 = 11
      ∨ D % 16 = 13 ∨ D % 16 = 15 := by
    have : ¬ (2 ∣ D) := hDodd
    omega
  have hDmem : (D : ZMod 16) ∈ ([1, 3, 5, 7, 9, 11, 13, 15] : List (ZMod 16)) := by
    rcases hDmod with h | h | h | h | h | h | h | h <;> rw [h] at hDcast <;> simp [hDcast]
  -- primitivity
  have hprim : u ^ 2 = 1 ∨ v ^ 2 = 1 := by
    rcases hUV with h | h
    · left; rw [hu, h]; simp
    · right; rw [hv, h]; simp
  have hconc := local2_phi_mod16 (D : ZMod 16) hDmem (q : ZMod 16) hqmem
    (u ^ 2) (sq_mod16_mem u) (v ^ 2) (sq_mod16_mem v) (m ^ 2) (sq_mod16_mem m) hprim key
  -- read off `D ≡ 1 (mod 4)`
  rcases hDmod with h | h | h | h | h | h | h | h <;> rw [h] at hDcast <;>
    rw [hDcast] at hconc <;>
      first
        | omega
        | (exfalso; revert hconc; decide)

end Run013
