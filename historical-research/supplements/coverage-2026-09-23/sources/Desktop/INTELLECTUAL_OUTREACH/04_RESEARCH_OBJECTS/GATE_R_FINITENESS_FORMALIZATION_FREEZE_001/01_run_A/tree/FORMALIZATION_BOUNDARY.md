# Formalization boundary

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO
    PRIOR_ART_BLOCKER        = UNRESOLVED

## Already certified in this tree

    E_q(Q) / 2 E_q(Q)  ~=  Z/2Z                        P04c.two_descent_quotient
    exists C >= 1, forall P, H(P)^4 <= C * H(P+P)      R1.h41_multiplicative_duplication_height
    an abstract proper-height two-descent torsion thm  R0.properHeightTwoDescentTorsion
    height sublevel sets are finite                    GateR.height_sublevels
    every rational point is torsion                    GateR.every_point_torsion
    rank_Z E_q(Q) = 0, cardinal-valued                 GateR.h41_rank_zero

All of these are theorems in the tree you have.  None of them is to be reproved.

## What this job adds, and what it does not

**Adds:** finiteness of the actual rational point group.  This is strictly stronger than rank zero
and, on the route this packet expects, needs no Mordell–Weil and no new arithmetic input.

**Does not add:** the order of the group, its exponent, its isomorphism type, its 2-primary
subgroup, or any identification of `E_q(ℚ)` with `{O, T}`.  Finiteness does not by itself determine
any of those, and none of them is authorised here.

Note in particular that `|E_q(ℚ)/2E_q(ℚ)| = 2` together with finiteness does **not** pin the
2-adic valuation of the group order: `C₄` is finite, has quotient of order two, and has
`v₂(|C₄|) = 2`.  Pinning it needs a further fact about the marked point, which is out of scope.

Success establishes exactly the one displayed statement for the `H41` family.  It is not a
classification of the rational points, not a statement about any larger family, and not a BSD
result.
