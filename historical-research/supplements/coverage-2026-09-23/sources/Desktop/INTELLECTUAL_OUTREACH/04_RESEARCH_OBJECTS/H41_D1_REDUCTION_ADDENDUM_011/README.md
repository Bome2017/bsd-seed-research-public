# H41_D1_REDUCTION_ADDENDUM_011

Records the outcome of the operator's retrieval of the two missing sources, and reduces `(D1)`.

**ARS validated.** *Agashe–Ribet–Stein, "The Modular Degree, Congruence Primes, and Multiplicity One"* —
Proposition 5.14 and Lemma 5.17 give `dim H⁰(X₀(N)_{F_r},Ω)[𝔪] ≤ 1` when `r ‖ N` and `U_r` acts by a
nonzero scalar, with **no odd-`r` restriction**; the Prop 5.10 proof notes `U_r = ±1`, nonzero also in
characteristic 2. At `r=2`, `N=2p`, `a₂=1`: `(D)` holds. Recorded from the operator's audit — the source
is not in this corpus and was not re-read here. Supersedes `ADDENDUM_010` §4's "unverified".

**Vatsal 1999 Thm 2.7 ruled out.** Its applicable case needs `ξ₁, ξ₂` distinct on `D_p`. **Corroborated
from frozen material:** the Vatsal 2003 proof quoted in `ADDENDUM_009` gives composition-factor characters
`χ` and `χ⁻¹ω` with `χ = 1` in the semistable case, and mod 2 the Teichmüller character is trivial — so
both are trivial, the semisimplification is `1 ⊕ 1`, and the hypothesis fails. The other cases are prime
level, or residue characteristic prime to `N`; the Eisenstein theorem assumes `p ≥ 3`. **Both Vatsal
failures are one phenomenon** — the `±`-eigenspace collapse of `ADDENDUM_009` and this character
coalescence are the same characteristic-2 degeneracy.

**`(D1)` reduced.** Of its three local cases, only one carries an arithmetic condition:

* vertical component: `F_p = 2^a u`, and `d(2) = 0` relatively, so `d log F_p = du/u` — **no condition**;
* node `xy = 2`: `dx/x = −dy/y` generates `ω`, and `(a−b)dx/x` is a section for **any** `a,b` — **none**;
* horizontal cusp: residue `M = ±k`, `k = (p²−1)/8`, and `v₂(k) = m ≥ 3`, so `8 | k` — **condition met**.

So `(D1)` is independent of vertical multiplicities, nodal branches and the exceptional `P¹`s, and reduces
to a parity that is proved uniformly with margin `2^{m−1}`. What is left is Deligne–Rapoport bookkeeping:
the local forms, disjointness of cusp sections, and integrality of `ω_η` in `ω(H)` (supported at `∞` by
the integral `q`-expansion `q^{−k}(1+O(q))`). **`(D1)` stays OPEN but can no longer die on the 2-adic
side.**

The remaining serious gap is `(D3) ⟹ (C)`, now with no citation behind it.

    ADDENDUM.md      the five sections
    computation/     verify_D1_inputs.py (symbolic in p)
    receipts/        D1_INPUTS

**The H41 seed remains unproved.**
