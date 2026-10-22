# Sage/Kato check on `E^{-7}` — the Aristotles' `5843` is wrong, and the exceptional set is `{7, 4547}`

Date 2026-09-22. Run in the recovered `run040/tools/sage-env` (SageMath 10.9, PARI 2.17.3).
**Nothing here claims `#Sha(E^{-7}/Q) = 49`.** See §5 for exactly what is and is not established.

---

## 1. The theorem, read at source — split multiplicative is NOT excluded

`Sha.bound_kato` docstring, verbatim:

> **THEOREM:** Suppose `L(E,1) != 0` and `p != 2` is a prime such that
> - `E` does not have **additive** reduction at `p`,
> - either the `p`-adic representation is surjective or has its image contained in a Borel subgroup.
>
> Then `ord_p(#Sha(E))` is bounded from above by the `p`-adic valuation of
> `L(E,1)·#E(Q)_tor^2 / (Omega_E · prod c_v)`.

`Sha.p_primary_bound` likewise excludes **additive** reduction (plus side conditions at non-split multiplicative and
at `p = 3`). **Neither excludes split multiplicative reduction.** The user's correction stands; both Aristotle runs
treated `p = 5843` as an exceptional-zero hole and both were wrong on that point.

## 2. Reduction and image data, from Sage's own `local_data`

    p       Kodaira   c_p   additive   split mult
    2       I1*       2     TRUE       -
    3       I2        2     -          TRUE
    7       I0*       2     TRUE       -
    2243    I1        1     -          -            (non-split multiplicative)
    4547    III       2     TRUE       -
    5843    I2        2     -          TRUE

    additive primes        = {2, 7, 4547}
    multiplicative primes  = {3, 2243, 5843}      <- 5843 is MULTIPLICATIVE, not additive
    non_surjective()       = [2]                  <- rho-bar_p is SURJECTIVE for every p >= 3
    isogeny class size     = 2  (degrees 1, 2)
    minimal model          = [0, 1, 0, -3235025292, 22326945153120]   (matches PARI exactly)
    torsion = 2,  prod c_v = 32,  root number = +1,  real components = 2

The image condition of the theorem therefore holds at **every** `p >= 3`. The only exclusions are `p = 2` and the
three additive primes.

## 3. Sage cannot evaluate the bound here — but we can

`L_ratio`, `sha.an()` and `sha.bound_kato()` all fail with a **PARI stack overflow**, not a timeout. Reading
`lseries_ell.py` shows why, and shows the algorithm is usable by hand:

    t = torsion order;  d = _multiple_of_degree_of_isogeny_to_optimal_curve();  C = 8*d*t
    eps = omega/C ;  k = 2*isqrt(N) + 10
    loop: L1, error_bound = at1(k);  if error_bound < eps: n = round(L1*C/omega); return (n/C)/real_components

So it is **numerical evaluation plus rounding against a proven denominator bound** `C = 8dt`. It fails only because
`2*isqrt(N) ~ 1.13e9` terms overflow the PARI stack. **We already have that L-value, certified, to better precision
than Sage would reach.** Running Sage's own algorithm on our certificate:

    t = 2,  d = 2,  real_components = 2   =>  C = 8*d*t = 32
    omega_1 = 0.011548941266157222748917603067270380053596934957191939001661   (Sage, 200 bits)
    eps = omega_1/C = 3.609044146e-4
    our certified half-width = 5.1e-5          PRECISION SUFFICIENT (margin 7.07x)

    L*C/omega over the whole certified interval [9.054319, 9.054421] = [25087.8588, 25088.1414]
    both endpoints round to n = 25088          <- the rounding is RIGOROUS on the certified interval

    L_ratio = (n/C)/real_components = 25088/32/2 = 392
    #Sha_an = L_ratio * t^2 / prod c_v = 392 * 4/32 = 49 = 7^2

**Independent confirmation of the period convention.** Sage's source returns `quo / real_components`, i.e.
`Omega_BSD = omega_1 * (number of real components) = 2*omega_1`. That is exactly the normalisation deduced earlier
from the perfect-square self-check (`omega_1` alone gives 98, not a square; `2*omega_1` gives 49, which is).
Two independent routes, same convention.

## 4. The corrected fixed-twist support theorem

Applying the §1 theorem with `#Sha_an = 49`:

    for every p >= 5 with p not in {7, 4547} :   ord_p #Sha(E^{-7}/Q) <= v_p(49) = 0,
    hence                                         Sha(E^{-7}/Q)[p^inf] = 0.

    EXCEPTIONAL SET  ⊆  {7, 4547}        (both ADDITIVE, hence outside the theorem)
    NOT in it: 5843, 2243, 3            (multiplicative — the theorem applies and gives 0)

**Intersecting with the BLV-admissible ordinary lane:**

| prime | why it leaves the exceptional set |
|---|---|
| `7` | `7 \| disc(K) = -7`, and BLV Hyp 1.1 requires `p ∤ disc(K)` |
| `4547` | `4547 \| N` (seed conductor `2^3·3·2243·4547^2·5843`), and BLV requires `p ∤ N` |

    => NO fixed-twist Sha exceptional prime survives inside the admissible ordinary lane.

Worth noting for robustness: `5843` and `2243` also divide `N`, so even had the Aristotles been right about `5843`
it would have been excluded from the lane anyway. Their error was real but **not load-bearing** for this conclusion.

## 5. The one hypothesis that does NOT hold automatically — stated plainly

`L_ratio`'s docstring: *"The result is provably correct if the Manin constant of the associated optimal quotient is
`<= 2`. This hypothesis on the Manin constant is true for all semistable curves (i.e. squarefree conductor), by a
theorem of Mazur."*

**Our conductor is not squarefree** — `Sage: conductor.is_squarefree() = False`, since
`49N = 2^3·3·7^2·2243·4547^2·5843`. So Mazur's semistable result **does not apply**, and
`Em.manin_constant()` raises `NotImplementedError` (it only works for curves in Cremona's tables; ours is ~`3.19e17`,
far beyond them).

Therefore:

    #Sha_an = 49    is RIGOROUS *conditional on* the Manin constant of the optimal quotient being <= 2.
    It is NOT unconditional, and #Sha(E^{-7}/Q) = 49 is NOT claimed at all -- Kato gives an upper BOUND.

Two things soften this, neither verified at source here:

* If the standard result "`p | c` implies `p^2 | N`" holds in the form I half-remember, then `c`'s prime support is
  contained in `{2, 7, 4547}` — precisely the primes already excluded — and `v_p(#Sha_an)` would be unchanged for
  every other `p`. **This needs checking at source (Mazur / Raynaud / Abbes–Ullmo / Edixhoven).**
* The precision margin is `7.07x`, so the rounding survives a denominator bound up to `C <= 224`. More certified
  `L`-digits would widen that: the tail at `T = 5e9` is `2.3e-19`, i.e. ~19 digits, for ~299 segments instead of 120
  (roughly 12 minutes on the machine that did the first run). That addresses the precision half of the problem but
  **not** the need for *some* proven bound on `c`.

## 6. Ledger

    KATO_THEOREM_HYPOTHESES         p != 2; not additive at p; image surjective-or-Borel   [READ AT SOURCE]
    IMAGE_CONDITION                 SATISFIED for all p >= 3   (non_surjective = [2])
    ADDITIVE_PRIMES                 {2, 7, 4547}               (Sage local_data)
    5843_IS_AN_OBSTRUCTION          FALSE -- split multiplicative, theorem applies   [BOTH ARISTOTLES WRONG]
    SAGE_CAN_EVALUATE               NO -- PARI stack overflow at 1.13e9 terms
    L_RATIO_ON_CERTIFIED_L          392, rounding rigorous on the whole certified interval
    SHA_AN                          49 = 7^2, CONDITIONAL on Manin constant <= 2
    MANIN_HYPOTHESIS                NOT automatic -- conductor is not squarefree      <- the residual gap
    TWIST_SHA_SUPPORT               ⊆ {7, 4547}, conditional as above
    INTERSECTION_WITH_BLV_LANE      EMPTY   (7 | disc K ; 4547 | N)
    ACTUAL_#SHA                     NOT determined -- Kato gives an upper bound only

---
**Downgrade, 2026-09-22 evening (see `~/BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_2026-09-22.md` §A):**
`5843_IS_AN_OBSTRUCTION = FALSE` is **downgraded to DISPUTED**. It rested only on the Sage `bound_kato` docstring, a
secondary summary of Kato/Grigorov. Four Aristotle runs (both ordinary-bridge audits, and both twist-Sha runs) hold
that at a split multiplicative prime the trivial zero kills the naive rank-0 bound unless the Greenberg–Stevens
L-invariant correction is handled. Primary sources not read. Off the critical path: 5843 | N, and the Cassels–Tate
shortcut does not need the twist's Sha support.
