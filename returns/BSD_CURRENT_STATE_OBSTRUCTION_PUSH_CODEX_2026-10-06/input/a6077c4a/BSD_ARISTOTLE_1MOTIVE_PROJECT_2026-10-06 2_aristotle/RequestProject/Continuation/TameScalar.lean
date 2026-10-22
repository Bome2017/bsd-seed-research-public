module

public import Mathlib
public import RequestProject.Continuation.TamePointCounts

/-!
# The tame scalar `W`: K288 custody audit and the `W = 8q` lattice criterion

Lean source for `research_return/REVISION_6.md`.

**Custody audit (§1).** For each of the nine singleton certificates `p = 17, …, 47` this file
records one row `(p, ℓ, #E(𝔽_ℓ), i, D, C₂)`:

* `#E(𝔽_ℓ)` is recounted by the kernel (`TamePointCounts.lean`);
* `i = [ℤ² : L]` and `D = det` of the tame-height Gram matrix on a reduced basis of the kernel
  lattice `L ⊂ ℤ P₁ ⊕ ℤ P₂` were recomputed for this run by new exact-arithmetic Python
  (`research_return/k288_audit/`), so `R_{p,ℓ} = D / i²` (mod `p`);
* `C₂` is the raw certified degree-two coefficient copied from the record (not recomputed).

`k288_rows_check` proves, for all nine rows at once, that `(a_ℓ − 2)·R_{p,ℓ}` is a unit mod `p` and
`C₂ ≡ (a_ℓ − 2)·288·R_{p,ℓ} (mod p)`, i.e. `w_{p,ℓ} ≡ 288`. Here `a_ℓ − 2 = ℓ − 1 − #E(𝔽_ℓ)`.
The tame heights themselves are not evaluated in Lean.

**Lattice criterion (§2).** `eq_288_of_mem_lattice`: if `W = 8q` with `35.99427 < q < 36.00573`
and `W ∈ (1/D)ℤ` for some `1 ≤ D ≤ 21`, then `W = 288` and `q = 36`. `lattice_bound_sharp`:
for `D = 22` the conclusion fails, so `21` is the exact denominator threshold.

**Circularity (§3).** `carrier_conclusion_of_sha_factor`: if `W = K·S` and every prime with
`Ш[p] ≠ 0` divides `S` (as for `S = #Ш`), then `Ш[p] ≠ 0 ⇒ p ∣ W` holds with no tame input at all.
So a carrier `W` derived with the refined Mazur–Tate constant `K_E = 32·#Ш` yields no information.

`Ш[p] ≠ 0` is an abstract predicate; nothing about the seed's Sha is proved here.
-/

@[expose] public section

namespace TameScalar

/-- One K288 row: coefficient prime `p`, auxiliary prime `l`, `#E(𝔽_l)`, kernel-lattice index
`i`, tame Gram determinant `D` on the lattice, and the recorded raw coefficient `C₂`. -/
structure K288Row where
  p : ℕ
  l : ℕ
  nE : ℕ
  idx : ℕ
  detGram : ℤ
  C2 : ℤ
deriving DecidableEq

/-- The nine rows. `nE` is kernel-checked in `TamePointCounts.lean`; `idx`, `detGram` from
`research_return/k288_audit/tame_regulator_lattice.out.json`; `C2` from the record. -/
def k288Rows : List K288Row :=
  [ ⟨17, 103, 106, 212, 10, 46298⟩,
    ⟨19, 191, 202, 404, 18, -30432⟩,
    ⟨23, 47, 44, 88, 6, 103854⟩,
    ⟨29, 233, 248, 248, 19, -98942⟩,
    ⟨31, 311, 296, 296, 15, 330990⟩,
    ⟨37, 149, 160, 160, 20, 762756⟩,
    ⟨41, 83, 92, 92, 14, -83420⟩,
    ⟨43, 173, 196, 196, 31, -227412⟩,
    ⟨47, 283, 288, 576, 20, 596378⟩ ]

/-- `a_l − 2 = l − 1 − #E(𝔽_l)`. -/
def K288Row.aMinus2 (r : K288Row) : ℤ := (r.l : ℤ) - 1 - r.nE

/-- The audited row predicate: `p ∥ l − 1`, `p ∤ idx`, `(a_l − 2)·D` a unit mod `p`, and
`C₂·idx² ≡ 288·(a_l − 2)·D (mod p)`, i.e. `C₂ / ((a_l − 2) R) ≡ 288` with `R = D/idx²`. -/
def K288Row.ok (r : K288Row) : Bool :=
  r.p.Prime ∧ r.l.Prime ∧ (r.l - 1) % r.p = 0 ∧ (r.l - 1) % (r.p * r.p) ≠ 0 ∧
  r.idx % r.p ≠ 0 ∧ (r.aMinus2 * r.detGram) % r.p ≠ 0 ∧
  (r.C2 * (r.idx : ℤ) ^ 2 - 288 * r.aMinus2 * r.detGram) % r.p = 0

/-- **K288 custody check.** All nine rows pass. -/
theorem k288_rows_check : k288Rows.all K288Row.ok = true := by decide +kernel

/-- The point counts used in `k288Rows` are the kernel-checked ones. -/
theorem k288_rows_counts :
    k288Rows.map (fun r => r.nE) =
      [affCountMin 103 + 1, affCountMin 191 + 1, affCountMin 47 + 1, affCountMin 233 + 1,
       affCountMin 311 + 1, affCountMin 149 + 1, affCountMin 83 + 1, affCountMin 173 + 1,
       affCountMin 283 + 1] := by
  rw [card_103, card_191, card_47, card_233, card_311, card_149, card_83, card_173, card_283]
  rfl

/-- The coefficient primes of the nine rows. -/
theorem k288_rows_primes : k288Rows.map (fun r => r.p) = [17, 19, 23, 29, 31, 37, 41, 43, 47] :=
  rfl

/-- Product of the nine coefficient primes. -/
theorem k288_modulus : 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47 = 20475850236047 := by norm_num

/-! ## §2 The denominator lattice that the `q`-interval resolves -/

/-- **Lattice criterion.** If `W = 8q`, `q` lies in the certified interval, and
`W = n / D` with `1 ≤ D ≤ 21`, then `n = 288·D` (so `W = 288`) and `q = 36`. -/
theorem eq_288_of_mem_lattice {q : ℝ} (hq1 : 35.99427 < q) (hq2 : q < 36.00573)
    {n : ℤ} {D : ℕ} (hD0 : 1 ≤ D) (hD : D ≤ 21) (hW : (n : ℝ) / D = 8 * q) :
    n = 288 * D ∧ q = 36 := by
  have hDpos : (0 : ℝ) < D := by exact_mod_cast hD0
  have hDle : (D : ℝ) ≤ 21 := by exact_mod_cast hD
  have hn : (n : ℝ) = 8 * q * D := by
    field_simp at hW; linarith
  have h1 : (n : ℝ) - 288 * D < 1 := by rw [hn]; nlinarith
  have h2 : -1 < (n : ℝ) - 288 * D := by rw [hn]; nlinarith
  have h1' : n - 288 * (D : ℤ) < 1 := by exact_mod_cast h1
  have h2' : -1 < n - 288 * (D : ℤ) := by exact_mod_cast h2
  have hnD : n = 288 * D := by omega
  refine ⟨hnD, ?_⟩
  have : (n : ℝ) = 288 * D := by exact_mod_cast hnD
  have hD' : (D : ℝ) ≠ 0 := ne_of_gt hDpos
  have : 8 * q * D = 288 * D := by linarith
  have := mul_right_cancel₀ hD' this
  linarith

/-- **Integral case.** `W ∈ ℤ` and `W = 8q` force `W = 288` and `q = 36`. -/
theorem eq_288_of_int {q : ℝ} (hq1 : 35.99427 < q) (hq2 : q < 36.00573) {W : ℤ}
    (hW : (W : ℝ) = 8 * q) : W = 288 ∧ q = 36 := by
  have := eq_288_of_mem_lattice hq1 hq2 (n := W) (D := 1) le_rfl (by norm_num)
    (by simpa using hW)
  simpa using this

/-- **Sharpness of 21.** With denominator `22` the interval no longer pins `W`: the value
`W = 288 − 1/22 ∈ (1/22)ℤ` corresponds to a `q` inside the certified interval with `q ≠ 36`. -/
theorem lattice_bound_sharp :
    ∃ q : ℝ, 35.99427 < q ∧ q < 36.00573 ∧ ((288 * 22 - 1 : ℤ) : ℝ) / (22 : ℕ) = 8 * q ∧
      q ≠ 36 := by
  refine ⟨(288 - 1 / 22) / 8, by norm_num, by norm_num, by push_cast; ring, by norm_num⟩

/-! ## §3 Why the carrier must be Sha-free -/

/-- **Circularity of a Sha-bearing constant.** If `W = K·S` and every prime with `Ш[p] ≠ 0`
divides `S` (true for `S = #Ш` whenever Sha is finite), then the carrier conclusion
`Ш[p] ≠ 0 ⇒ p ∣ W` holds with no tame identity and no detector. A comparison whose constant is
`K_E = 32·#Ш` therefore cannot bound the support. -/
theorem carrier_conclusion_of_sha_factor (shaNonzero : ℕ → Prop) (K S : ℤ)
    (hS : ∀ p : ℕ, p.Prime → shaNonzero p → (p : ℤ) ∣ S) :
    ∀ p : ℕ, p.Prime → shaNonzero p → (p : ℤ) ∣ K * S :=
  fun p hp hs => Dvd.dvd.mul_left (hS p hp hs) K

end TameScalar

end
