import WitnessContent.Defs

/-!
# A1 — frozen target statements

Every target of package A1 is a `Prop` defined here. `Targets.lean` must prove each of them
*with exactly these statements*. This file is FROZEN (SHA-256 in `ACCEPTANCE_TESTS.md`).

Hypothesis tags used in the comments (full table in `ASSUMPTIONS.md`):
* `[FORMAL_ASSUMPTION]` — a modelling hypothesis at the formal boundary, justified in the docs;
* `[PROVED_IN_PACKAGE]` — a hypothesis of an abstract target that another target of this package
  discharges for the concrete model;
* `[IMPORTED_ARITHMETIC_THEOREM]` — a published arithmetic theorem (or standard fact) about the curve,
  entered as a hypothesis, NOT proved here;
* `[NOT_PART_OF_THIS_TASK]` — the open arithmetic antecedent of WC (`A ≠ 0`, `A ∈ J_E`): an explicit
  hypothesis at the formal boundary, never to be proved here.

WARNING. Formalizing WC proves only the implication from the stated witness-content antecedent.
It does not establish that the antecedent is easier than FIN or that FIN has been reduced.
-/

namespace WitnessContent
namespace Spec

/-! ## T1. Lemma A, commutative case (Codex `ALGEBRAIC_REDUCTION_LEMMAS.md` §A;
`FORMALIZABLE_GAPS.md` A1). Ota's `G_S` is abelian, so this is the case used by WC. -/
def LemmaA_comm : Prop :=
  ∀ (R : Type) [CommRing R] (G : Type) [CommGroup G] (e : ℕ),
    (∀ g : G, g ^ e = 1) →
    ∀ r : ℕ, 1 ≤ r → ∀ x ∈ (augIdeal R G) ^ r, e • x ∈ (augIdeal R G) ^ (r + 1)

/-! ## T2. The graded piece `I^r/I^(r+1)` is killed by the exponent. -/
def Gr_killed_by_exponent : Prop :=
  ∀ (R : Type) [CommRing R] (G : Type) [CommGroup G] (e : ℕ),
    (∀ g : G, g ^ e = 1) → ∀ r : ℕ, 1 ≤ r → ∀ y : gr R G r, e • y = 0

/-! ## T3. If prime-to-`p` integers are units in `R` (true for `R = ℤ_[p]`, see T10), the graded
piece is killed by `p ^ v_p(e)`: it is `p`-primary of bounded exponent (Codex: "M(p,S) is a finite
p-primary module"; only the bounded exponent is needed for depths). -/
def Gr_p_primary : Prop :=
  ∀ (R : Type) [CommRing R] (G : Type) [CommGroup G] (p e : ℕ),
    p.Prime → 0 < e → (∀ g : G, g ^ e = 1) →
    (∀ u : ℕ, ¬ p ∣ u → IsUnit (u : R)) →
    ∀ r : ℕ, 1 ≤ r → ∀ y : gr R G r, p ^ (e.factorization p) • y = 0

/-! ## T4. Bridge from Ota Thm 5.17's group-ring form `θ ∈ I^(min r p)` to the witness form. -/
def Bridge_517 : Prop :=
  ∀ (R : Type) [CommRing R] (G : Type) [CommGroup G] (θ : MonoidAlgebra R G) (r p : ℕ),
    2 ≤ r → 3 ≤ p → θ ∈ (augIdeal R G) ^ (min r p) →
      θ ∈ (augIdeal R G) ^ 2 ∧ (3 ≤ r → cls2 θ = 0)

/-- T4b. On `I²`, `cls2` is the genuine class, and it vanishes exactly on `I³`. -/
def Cls2_zero_iff : Prop :=
  ∀ (R : Type) [CommRing R] (G : Type) [CommGroup G] (θ : MonoidAlgebra R G),
    θ ∈ (augIdeal R G) ^ 2 → (cls2 θ = 0 ↔ θ ∈ (augIdeal R G) ^ 3)

/-! ## T5. Depth is well defined and attained on NONZERO elements of bounded `p`-power exponent. -/
def Depth_spec : Prop :=
  ∀ (M : Type) [AddCommGroup M] (p a : ℕ), p.Prime → (∀ x : M, p ^ a • x = 0) →
    ∀ t : M, t ≠ 0 → PDvd p (depth p t) t ∧ ¬ PDvd p (depth p t + 1) t ∧ depth p t < a

/-- T5b. The zero element is divisible by every power (why `depth 0` is junk). -/
def Zero_infinitely_divisible : Prop :=
  ∀ (M : Type) [AddCommGroup M] (p j : ℕ), PDvd p j (0 : M)

/-! ## T6. `h_p` characterisations: nonzero witness / bounded depth / depth zero. -/
def HInf_lt_top_iff : Prop :=
  ∀ (W : ℕ → Type) (M : (p : ℕ) → W p → Type) [∀ p S, AddCommGroup (M p S)]
    (t : ∀ p S, M p S) (p : ℕ),
    hInf t p < ⊤ ↔ ∃ S, t p S ≠ 0

def HInf_le_iff : Prop :=
  ∀ (W : ℕ → Type) (M : (p : ℕ) → W p → Type) [∀ p S, AddCommGroup (M p S)]
    (t : ∀ p S, M p S) (p : ℕ),
    p.Prime → (∀ S, ∃ a : ℕ, ∀ x : M p S, p ^ a • x = 0) →
    ∀ d : ℕ, hInf t p ≤ d ↔ ∃ S, ¬ PDvd p (d + 1) (t p S)

/-- T6c. `A ≠ 0`, `A ∈ J_E` bounds every `h_p` by `v_p(A)`; a prime not dividing `A` has `h_p = 0`. -/
def JE_bounds : Prop :=
  ∀ (W : ℕ → Type) (M : (p : ℕ) → W p → Type) [∀ p S, AddCommGroup (M p S)]
    (t : ∀ p S, M p S) (P : Set ℕ) (A : ℤ),
    A ≠ 0 → A ∈ JE t P →
      (∀ p ∈ P, hInf t p ≤ (padicValInt p A : ℕ)) ∧
      (∀ p ∈ P, p.Prime → ¬ (p : ℤ) ∣ A → hInf t p = 0)

/-! ## T7. THEOREM WC, abstract witness form (Codex `WITNESS_CONTENT_THEOREM.md` §2). -/
def WC_abstract : Prop :=
  ∀ (S0 : Finset ℕ) (Sha : Type) [AddCommGroup Sha]
    (W : ℕ → Type) (M : (p : ℕ) → W p → Type) [∀ p S, AddCommGroup (M p S)]
    (t : ∀ p S, M p S) (r : ℕ → ℕ),
    -- [FORMAL_ASSUMPTION; PROVED_IN_PACKAGE for the group-ring model by T3] bounded p-power exponent
    (∀ p ∈ primesOutside S0, ∀ S, ∃ a : ℕ, ∀ x : M p S, p ^ a • x = 0) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Sha is a torsion group
    AddMonoid.IsTorsion Sha →
    -- [IMPORTED_ARITHMETIC_THEOREM] Selmer: cofinite generation + corank = rank(=2) + corank Sha[p^∞]
    (∀ p ∈ primesOutside S0, ¬ (primaryPart Sha p : Set Sha).Finite → 3 ≤ r p) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Ota Thm 5.17, witness form (group-ring form ⇒ this: PROVED_IN_PACKAGE, T4)
    (∀ p ∈ primesOutside S0, ∀ S, 3 ≤ r p → t p S = 0) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Ota Thm 1.5 (special case of Thm 6.4): witness ∉ p·M ⇒ Sha[p] = 0
    (∀ p ∈ primesOutside S0, ∀ S, ¬ PDvd p 1 (t p S) → ∀ x : Sha, p • x = 0 → x = 0) →
    -- [NOT_PART_OF_THIS_TASK] open antecedent: a nonzero integer in J_E (never proved here)
    ∀ A : ℤ, A ≠ 0 → A ∈ JE t (primesOutside S0) →
      (∀ p ∈ primesOutside S0, (primaryPart Sha p : Set Sha).Finite) ∧
      (∀ p ∈ primesOutside S0, ¬ (p : ℤ) ∣ A → primaryPart Sha p = ⊥) ∧
      ((∀ p ∈ S0, p.Prime → (primaryPart Sha p : Set Sha).Finite) → Finite Sha)

/-! ## T8. THEOREM WC with Ota Thm 5.17 in its group-ring form `θ_S ∈ I^(min r p) ⊆ Z_p[G_S]`.
`Rp p` models `ℤ_[p]` (only property used: prime-to-p integers are units — T10), `G p S` models
`G_S = Gal(Q(μ_S)/Q) ≅ (ZMod S)ˣ` (T11), `θ p S` the Mazur–Tate element, `r p` the Z_p-corank of
`Sel(Q, E[p^∞])`. -/
def WC_groupRing : Prop :=
  ∀ (S0 : Finset ℕ) (Sha : Type) [AddCommGroup Sha]
    (W : ℕ → Type) (Rp : ℕ → Type) [∀ p, CommRing (Rp p)]
    (G : (p : ℕ) → W p → Type) [∀ p S, CommGroup (G p S)]
    (e : (p : ℕ) → W p → ℕ)
    (θ : (p : ℕ) → (S : W p) → MonoidAlgebra (Rp p) (G p S)) (r : ℕ → ℕ),
    -- [FORMAL_ASSUMPTION] 2 is excluded (Codex: S0 = {2,3,5,2243,4547,5843})
    2 ∈ S0 →
    -- [FORMAL_ASSUMPTION] G_S finite abelian of positive exponent e
    (∀ p ∈ primesOutside S0, ∀ S, 0 < e p S ∧ ∀ g : G p S, g ^ e p S = 1) →
    -- [FORMAL_ASSUMPTION] the coefficient ring behaves like Z_p on prime-to-p integers
    (∀ p ∈ primesOutside S0, ∀ u : ℕ, ¬ p ∣ u → IsUnit (u : Rp p)) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Sha is a torsion group
    AddMonoid.IsTorsion Sha →
    -- [IMPORTED_ARITHMETIC_THEOREM] corank of Sel(Q,E[p^∞]) ≥ rank E(Q) = 2
    (∀ p ∈ primesOutside S0, 2 ≤ r p) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Selmer: infinite Sha[p^∞] ⇒ corank ≥ 3
    (∀ p ∈ primesOutside S0, ¬ (primaryPart Sha p : Set Sha).Finite → 3 ≤ r p) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Ota Thm 5.17: θ_S ∈ I^(min(r_{p^∞}, p))
    (∀ p ∈ primesOutside S0, ∀ S, θ p S ∈ (augIdeal (Rp p) (G p S)) ^ (min (r p) p)) →
    -- [IMPORTED_ARITHMETIC_THEOREM] Ota Thm 1.5: class of θ_S ∉ p·(I²/I³) ⇒ Sha[p] = 0
    (∀ p ∈ primesOutside S0, ∀ S, ¬ PDvd p 1 (cls2 (θ p S)) → ∀ x : Sha, p • x = 0 → x = 0) →
    -- [NOT_PART_OF_THIS_TASK] open antecedent: a nonzero integer in J_E (never proved here)
    ∀ A : ℤ, A ≠ 0 →
      A ∈ JE (M := fun p S => gr (Rp p) (G p S) 2) (fun p S => cls2 (θ p S)) (primesOutside S0) →
      (∀ p ∈ primesOutside S0, (primaryPart Sha p : Set Sha).Finite) ∧
      (∀ p ∈ primesOutside S0, ¬ (p : ℤ) ∣ A → primaryPart Sha p = ⊥) ∧
      ((∀ p ∈ S0, p.Prime → (primaryPart Sha p : Set Sha).Finite) → Finite Sha)

/-! ## T9. Regression countermodels (Codex `WITNESS_CONTENT_THEOREM.md` §4). -/

/-- T9a. Uniform source denominators do not control image content: the source `ℤ ∋ 1` has content 1
(no denominator at all), the integral maps `n ↦ p²·n` land in `ZMod (p^3)`, every witness is nonzero,
yet `J = {0}`. -/
def CM_uniform_denominator : Prop :=
  (∀ p : ℕ, p.Prime → (zmultiplesHom (ZMod (p ^ 3)) ((p : ZMod (p ^ 3)) ^ 2)) 1 ≠ 0) ∧
  JE (W := fun _ => Unit) (M := fun p _ => ZMod (p ^ 3))
    (fun p _ => (zmultiplesHom (ZMod (p ^ 3)) ((p : ZMod (p ^ 3)) ^ 2)) 1) {p | p.Prime} = {0}

/-- T9b. The false shortcut "a nonzero (finite, bounded-exponent) witness at every prime ⇒ `J_E ≠ 0`"
is refuted. Aristotle must NOT prove any statement implying this shortcut. -/
def CM_nonzero_everywhere : Prop :=
  ¬ ∀ (W : ℕ → Type) (M : (p : ℕ) → W p → Type) [∀ p S, AddCommGroup (M p S)]
      (t : ∀ p S, M p S),
      (∀ p, p.Prime → ∀ S, Finite (M p S)) →
      (∀ p, p.Prime → ∀ S, ∃ a : ℕ, ∀ x : M p S, p ^ a • x = 0) →
      (∀ p, p.Prime → ∃ S, t p S ≠ 0) → ∃ A : ℤ, A ≠ 0 ∧ A ∈ JE t {p | p.Prime}

/-! ## T12. Non-vacuity: the hypotheses of T7 are jointly satisfiable with `A = 1 ∈ J_E`
(guards against an accidentally contradictory formalization). -/
def WC_abstract_nonvacuous : Prop :=
  ∃ (S0 : Finset ℕ) (Sha : Type) (_ : AddCommGroup Sha)
    (W : ℕ → Type) (M : (p : ℕ) → W p → Type) (_ : ∀ p S, AddCommGroup (M p S))
    (t : ∀ p S, M p S) (r : ℕ → ℕ),
    (∀ p ∈ primesOutside S0, ∀ S, ∃ a : ℕ, ∀ x : M p S, p ^ a • x = 0) ∧
    AddMonoid.IsTorsion Sha ∧
    (∀ p ∈ primesOutside S0, ¬ (primaryPart Sha p : Set Sha).Finite → 3 ≤ r p) ∧
    (∀ p ∈ primesOutside S0, ∀ S, 3 ≤ r p → t p S = 0) ∧
    (∀ p ∈ primesOutside S0, ∀ S, ¬ PDvd p 1 (t p S) → ∀ x : Sha, p • x = 0 → x = 0) ∧
    (1 : ℤ) ∈ JE t (primesOutside S0) ∧
    (∀ p ∈ primesOutside S0, ∃ S, t p S ≠ 0)

/-! ## T10–T11. Instantiation checks: the abstractions of T8 are satisfied by `ℤ_[p]` and `(ZMod S)ˣ`. -/
def PadicInt_units : Prop :=
  ∀ (p : ℕ) [Fact p.Prime] (u : ℕ), ¬ p ∣ u → IsUnit (u : ℤ_[p])

def Units_exponent : Prop :=
  ∀ (S : ℕ) [NeZero S], 0 < Nat.card (ZMod S)ˣ ∧ ∀ g : (ZMod S)ˣ, g ^ Nat.card (ZMod S)ˣ = 1

/-! ## Stretch targets (not required for A1_FULL). -/

/-- S1. Lemma A for an arbitrary (possibly non-commutative) group, over ℤ (Codex: "No commutativity
of G is needed"). -/
def LemmaA_general : Prop :=
  ∀ (G : Type) [Group G] (e : ℕ), (∀ g : G, g ^ e = 1) →
    ∀ r : ℕ, 1 ≤ r → ∀ x ∈ (augSubZ G) ^ r, e • x ∈ (augSubZ G) ^ (r + 1)

/-- S2. For a finite abelian group, the integral graded pieces are finite. -/
def Gr_finite_Z : Prop :=
  ∀ (G : Type) [CommGroup G] [Finite G] (r : ℕ), 1 ≤ r → Finite (gr ℤ G r)

/-- S3. ... and their rationalisation vanishes. -/
def Gr_rational_trivial : Prop :=
  ∀ (G : Type) [CommGroup G] [Finite G] (r : ℕ), 1 ≤ r →
    Subsingleton (TensorProduct ℤ ℚ (gr ℤ G r))

end Spec
end WitnessContent
