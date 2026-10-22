import Mathlib

/-!
# A2 — Primary support: frozen definitions

FROZEN (SHA-256 recorded in `ACCEPTANCE_TESTS.md`). Do not edit; add helper lemmas in new files.

Source of truth: Codex, `~/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/`:
`WITNESS_CONTENT_THEOREM.md` §1 (J_E and finite support), §4 (countermodels, descent to ℤ),
`ALGEBRAIC_REDUCTION_LEMMAS.md` §B (global lattice descent) and §H (FIN does not determine the order),
`FORMALIZABLE_GAPS.md` A3 (integral content) and B3 (abstract primary assembly).
Nothing here mentions elliptic curves.
-/

namespace PrimarySupport

/-- The `p`-primary part `G[p^∞] = {x | ∃ k, p ^ k • x = 0}` (same definition as package A1). -/
def primaryPart (G : Type*) [AddCommGroup G] (p : ℕ) : AddSubgroup G where
  carrier := {x | ∃ k : ℕ, p ^ k • x = 0}
  zero_mem' := ⟨0, by simp⟩
  add_mem' := by
    rintro x y ⟨a, ha⟩ ⟨b, hb⟩
    refine ⟨a + b, ?_⟩
    have h1 : p ^ (a + b) • x = 0 := by
      rw [pow_add, mul_comm, mul_smul, ha, smul_zero]
    have h2 : p ^ (a + b) • y = 0 := by
      rw [pow_add, mul_smul, hb, smul_zero]
    rw [smul_add, h1, h2, add_zero]
  neg_mem' := by
    rintro x ⟨k, hk⟩
    exact ⟨k, by rw [smul_neg, hk, neg_zero]⟩

/-- The primes outside a finite exceptional set `S0`. -/
def primesOutside (S0 : Finset ℕ) : Set ℕ := {p | p.Prime ∧ p ∉ S0}

/-- `v_p(a)` with the convention `v_p(0) = ∞`. -/
noncomputable def vInf (p : ℕ) (a : ℤ) : ℕ∞ :=
  if a = 0 then ⊤ else ((padicValInt p a : ℕ) : ℕ∞)

/-- The set cut out by a depth function `h` (Codex's `J_E` with `h = h_p`):
`J(P, h) = {a ∈ ℤ : v_p(a) ≥ h(p) for all p ∈ P}`. -/
def JOf (P : Set ℕ) (h : ℕ → ℕ∞) : Set ℤ := {a | ∀ p ∈ P, h p ≤ vInf p a}

/-- The primes of `P` of positive depth. -/
def posSupport (P : Set ℕ) (h : ℕ → ℕ∞) : Set ℕ := {p | p ∈ P ∧ h p ≠ 0}

/-- Content of a vector of the finite free lattice `ℤ^n`: the normalized (nonnegative) gcd of its
coordinates (Codex `FORMALIZABLE_GAPS.md` A3). -/
def content {n : ℕ} (z : Fin n → ℤ) : ℤ := Finset.univ.gcd z

/-- Reduction of a lattice vector modulo `m`. -/
def reduceMod {n : ℕ} (m : ℕ) (z : Fin n → ℤ) : Fin n → ZMod m := fun i => (z i : ZMod m)

end PrimarySupport
