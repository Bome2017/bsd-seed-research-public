# Definite-theta branch — strict reduction on the norm-coherence interface

2026-09-22. `returned_B_normcoherence.tar.gz`, sha256
`81c4d90d2a379f43836d67e8adcefaaa6ec41a6837533c02f674bdb1471c7ff8`. New `RequestProject/NormCoherence.lean`;
all eight Lean files `sorry`-free. **This removed the isolated obstruction rather than renaming it.**

## 1. The stabilization identity — verified independently

Given the three-term relation and `pr ∘ nu = p`, with `alpha` an ordinary unit root of `X^2 - a X + p`, set
`theta_n^alpha = theta_{n+1} - alpha^{-1} nu(theta_n)`. Then

    pr(theta_{n+1}^alpha) = alpha * theta_n^alpha.

Checked here from the Hecke polynomial: `alpha^2 - a*alpha + p = 0` gives `a = alpha + p/alpha`, hence
`a - p/alpha = alpha` exactly; substituting into
`pr(theta_{n+1}^alpha) = (a - p/alpha) theta_{n+1} - nu(theta_n)` gives `alpha * theta_n^alpha`. So after multiplying
by `alpha^{-(n+1)}` the family is **literally norm-coherent** (`twisted_family_coherent`). This is precisely the
interface the previous audit left open — `a_p`-coherence of the fixed system versus norm-coherence of the `p`-adic
measure — and the entire discrepancy is carried by the single explicit term `alpha^{-1} nu(theta_n)`.

## 2. The augmentation calculation — verified, and it is the substantive half

For the cyclic norm element `N = sum_{i=0}^{p-1} (1+t)^i`, hockey-stick summation gives

    N = C(p,1) + C(p,2) t + C(p,3) t^2 + ...  =  p + C(p,2) t + C(p,3) t^2   (mod I^3).

For `p >= 5` both `p | C(p,2)` and `p | C(p,3)` (the latter since `3 | (p-1)(p-2)` for `p` prime `>= 5`), so

    **N in p*Lambda + I^3.**

Confirmed by direct expansion at `p = 5, 7, 11, 13, 17`: `(5,10,10), (7,21,35), (11,55,165), (13,78,286),
(17,136,680)`. Consequence: the `alpha^{-1} nu(theta_n)` correction is **invisible in exactly the quotient that detects
the mod-`p` degree-two witness.** So the ordinary `p`-adic stabilization machinery is no longer the fundamental
obstruction.

## 3. Where the branch now sits

    from:  a mysterious p-adic theta measure
    to:    sum_sigma c_2(sigma) phi_E(x_{p^n}(sigma))  !=  0  (mod p)   for some n, uniformly in the ordinary primes

a finite-level, integral statement.

**Scope point to preserve.** This does **not** yet give the prime-independent ancestor. The finite-layer object at
conductor `p^n` still varies with `p`. What has been eliminated is the extra `p`-adic stabilization/measure
complication. The new obstruction is specifically **uniform mod-`p` distribution/nonvanishing of integral Gross-point
values** — narrower than before, still genuinely uniform arithmetic.

## 4. Supersingular analysis — correctly scoped

For `p >= 5`, supersingular over `Q` forces `a_p = 0` (Hasse: `|a_p| <= 2 sqrt p < p`), so the Hecke polynomial is
`X^2 + p`, whose roots have valuation `1/2 > 0`. **No ordinary unit-root stabilization exists**, so the ordinary
mechanism cannot be base-changed to supersingular primes. The relation collapses to `pr(theta_{n+2}) = -nu(theta_n)`,
giving `pr^2(theta_{n+2}) = -p theta_n` and `pr^4(theta_{n+4}) = p^2 theta_n` — the period-two structure a signed theory
would come from. All four verified here. The run **did not** claim to have constructed the signed half-logarithmic
quotients, which is the right restraint.

## 5. The gate before line 1 becomes arithmetic

`H1` — the published three-term norm relation — is carried as an **explicit hypothesis**, and the run states that the
arithmetic reading of the interfaces is **prose, not formalized**. So §1 is *conditional algebra*.

> **Required before `ORDINARY_NORM_COHERENCE` is recorded as arithmetic:** a source audit of `H1` with exact
> conventions — that the published Gross-point theta system used here satisfies precisely that three-term relation with
> the same `pr`, the same `nu`, the same level indexing and the same normalization. If it does, this interface is closed.

This is the same shape as the MCS lane: conditional algebra formalized, the arithmetic input still unverified prose.

## 6. Branch status

    ORDINARY_NORM_COHERENCE                          = PROVED, conditional on H1
    ORDINARY_STABILIZATION_INVISIBILITY mod (p, I^3) = PROVED
    FINITE_LAYER_GROSS_POINT_NONVANISHING            = OPEN      <- the new target
    SUPERSINGULAR_UNIT_ROOT_LANE                     = DEAD in the stated class C_3
    SUPERSINGULAR_SIGNED_CONSTRUCTION                = OPEN
    TAIL_FINITE_SUPPORT                              = OPEN
    FIN = OPEN    FORMULA = OPEN    THRESHOLD = 2601 (unchanged; the run also marked sharpness_1089 stale in its own docstring)

**Hold this Aristotle while the other finishes.** The successor is narrow: attack the finite-layer Gross-point sum
through its distribution relations and ask whether mod-`p` nonvanishing can be forced uniformly. Nothing further with
`p`-adic measures. No `p = 17`.
