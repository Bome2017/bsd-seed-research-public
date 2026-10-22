# Certified endpoints

Every statement below is quoted from frozen source. The verbatim cuts are in
`receipts/CERTIFIED_STATEMENTS_VERBATIM.txt`.

## The family boundary — unchanged, not widened

```lean
structure Params (ε : ℤ) (m : ℕ) (q : ℕ) [Fact (Nat.Prime q)] : Prop where
  m_ge_three     : 3 ≤ m
  eps_unit       : ε = 1 ∨ ε = -1
  q_not_dvd_twoD : ¬ ((q : ℤ) ∣ 2 * DD ε m)
  q_mod_eight    : q % 8 = 5
  legendre_D_q   : legendreSym q (DD ε m) = -1
  odd_valuations : ∀ ℓ ∈ ellSet ε m, Odd (padicValInt ℓ (DD ε m))

def H41 (ε : ℤ) (m : ℕ) : Prop :=
  (DD ε m < 0 ∧ sCount ε m = 1) ∨
  (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3)
```

`m ≥ 3` is retained exactly, as its own doc comment records. Nothing in the Gate-R work widens
`m`, `ε`, `q`, `Params` or `H41`.

## H¹-free point-group endpoint — `P04c.two_descent_quotient`

Four conjuncts, of which the last two are the endpoint:

```lean
  Nat.card ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) = 2
∧ Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+ ZMod 2)
```

`twoE` is the range of doubling on the actual point group. The first two conjuncts supply the
connecting homomorphism from `E'(ℚ)/φ(E(ℚ))`, its surjectivity, its kernel, and the equivalence
to the explicit square-class quotient `GphiExp / KExp`.

**This is a point-group statement. It is not Sel₂ and must not be called Sel₂.**

## The two Gate-R inputs

```lean
theorem R1.h41_multiplicative_duplication_height
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m) :
    ∃ C : ℕ, 1 ≤ C ∧
      ∀ P : (Ecurve ε m q).toAffine.Point, height P ^ 4 ≤ C * height (P + P)
```

```lean
theorem R0.properHeightTwoDescentTorsion
    {G : Type*} [AddCommGroup G] (T : G) (hT : T + T = 0)
    (h : G → ℕ) (B : ℕ)
    (hfin : ∀ n : ℕ, {P : G | h P ≤ n}.Finite)
    (hhalve : ∀ P : G, ∃ Q : G, ∃ e : ℕ, e ≤ 1 ∧ P = Q + Q + e • T ∧ h Q ≤ max (h P) B) :
    ∀ P : G, ∃ n : ℕ, 0 < n ∧ n • P = 0
```

R1 is arithmetic and specific to the family. R0 is abstract: an arbitrary additive commutative
group, an arbitrary natural-valued height, no reference to curves at all. Note that R0's `hfin`
is about **sublevel sets** of `h`, never about `G`.

## The five Gate-R outputs

```lean
theorem GateR.height_sublevels (ε : ℤ) (m q n : ℕ) :
    {P : (P01.Ecurve ε m q).toAffine.Point | R1.height P ≤ n}.Finite

theorem GateR.halving_representatives … :
    ∀ P, ∃ Q, ∃ e : ℕ, e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP

def GateR.translateMax {G : Type*} [AddCommGroup G] (T : G) (H : G → ℕ) (P : G) : ℕ :=
  max (H P) (H (P + T))

theorem GateR.bounded_halving … :
    ∃ C : ℕ, 1 ≤ C ∧ ∀ P, ∃ Q, ∃ e : ℕ, e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP ∧
      translateMax (P01.Tpt hP) R1.height Q ≤ max (translateMax (P01.Tpt hP) R1.height P) C

theorem GateR.every_point_torsion … : ∀ P, ∃ n : ℕ, 0 < n ∧ n • P = 0

theorem GateR.h41_rank_zero … :
    Module.rank ℤ (P01.Ecurve ε m q).toAffine.Point = (0 : Cardinal)
```

`height_sublevels` takes no `Params` and no `H41`: properness of the height is a fact about the
curve's rational points at that height, independent of the family conditions. The other four
carry exactly `Params`, `H41` and the prime instance, and nothing was added to them.

## What `every_point_torsion` does and does not give

**Gives:** for each rational point individually, a positive integer annihilating it. Hence, via
root `rank_eq_zero_iff`, cardinal rank zero.

**Does not give:** a bound on those integers uniform in `P`; the exponent of the group;
finiteness of the group; the isomorphism type of the group; or the identification of `E_q(ℚ)`
with `{O, T}`. See `receipts/FINITENESS_SEARCH.txt` — no such theorem exists in the development.
