# c_2(p) WITNESS — one theorem only

You are an independent hostile mathematical referee and problem-solver. Read `INPUTS.md` and `GATE.md` first.

## What is already established (conditional, prime by prime)

    for all p >= 5 with p ∤ 7N and E ordinary at p :    c_2(p) ∈ Z_p^x   ==>   Sha(E/Q)[p^inf] = 0

**`c_2(p) ∈ Z_p` is defined in `INPUTS.md` §4**, bound to BLV's construction: the `t^2` coefficient of BLV's
square-root element `calL_{g,1}` in `Z_p[G_1]/I^3`, `G_1 = Gal(K_1/K) = <γ>`, `t = γ − 1`, with `ψ_g` the **surjective
(primitive)** eigenfunctional. The first layer `K_1` uses **traced Gross points of conductor `p^2`**, not `p`. Mod `p`:

    c_2(p)  ≡  − Σ_{j=0}^{p-1} C(j,2) · ψ_g(γ^j P_1)      (P_1 = traced conductor-p^2 Gross point)

Work with `c_2(p)` as a `Z_p`-coefficient and distinguish its reduction. Do not rescale `ψ_g`.

The implication above is `READ_FIRST/ORDINARY_LANE_FREEZE.md` §1; its forward direction has been independently
source-audited. **Do not re-audit it** unless you find an actual dependency error (then `BRIDGE_DEPENDENCY_ERROR`).

## The question

> **Is `c_2(p) ∈ Z_p^x` provable — and for which set of ordinary primes — or what is the exact first missing
> theorem?**

## Admissible route classes

| class | content |
|---|---|
| **A. analytic / horizontal nonvanishing** | Gross-point equidistribution, toric-period mod-`p` methods |
| **B. algebraic** | congruences, integral heights, Euler/Kolyvagin input, explicit Selmer constructions — any argument *proved without assuming the desired unit statement* |
| **C. compressed computation** | Brandt / Hecke-eigenspace / trace-formula / quotient methods that **provably avoid** enumerating the Shimura set (see `INPUTS.md` §3) |
| **D. impossibility / first missing theorem** | exactly why A–C stop, stated precisely enough to be looked up or attacked |

## Quantifier discipline — state which level you reach

The target is the family `c_2(p)`, `p` ordinary, not one number. Distinguish:

1. one prime;
2. a positive-density set of ordinary `p` — does **not** reach FIN;
3. all but finitely many ordinary `p` — reaches the ordinary part of FIN *modulo* a finite-exception treatment;
4. every admissible ordinary `p` — closes the ordinary part of FIN outright.

## Verdicts — return exactly one

    UNIFORM_C2_UNIT_PROVED              every admissible ordinary p
    COFINITE_C2_UNIT_ONLY               all but finitely many (list them if explicit)
    POSITIVE_DENSITY_C2_UNIT_ONLY
    FIXED_P_C2_UNIT_ONLY                which p
    COMPRESSED_COMPUTATION_ROUTE        a concrete method + resource estimate, avoiding the 5.42e14 enumeration
    C2_NONUNIT_PROVED                   c_2(p) ≡ 0 (mod p) proved rigorously at a stated prime / set, with the consequence.
                                        This challenges the universal witness target; it does NOT refute the conditional
                                        bridge, which only runs forward from a unit.
    FIRST_MISSING_THEOREM: <exact statement>
    BRIDGE_DEPENDENCY_ERROR: <the first broken implication>

Then a theorem-by-theorem justification, every claim labelled per `GATE.md` K4.
