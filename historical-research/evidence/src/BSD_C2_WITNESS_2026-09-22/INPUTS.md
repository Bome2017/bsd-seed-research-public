# INPUTS — retained facts. Inputs, not things to re-derive.

## 1. The curve, the field, the quaternion algebra

    E / Q :  y^2 = x^3 - 22735 x^2 + 106272484 x      (minimal; reduced form [0,-1,0,-66020924,-65074271436] via x = X + 7578, u = 1)
    N = 2^3 · 3 · 2243 · 4547^2 · 5843 = 6503188012738584
    rank E(Q) = 2 = analytic rank                          [PROVED]
    E(Q)_tors = Z/2                                        => a_p even at every odd good p
    non-CM                                                 [j = 1322372123614064/689197281363 not integral;
                                                            v_q(j) < 0 at q = 3, 2243, 5843]
    rho-bar_{E,p} surjective for every p >= 3              [Sage non_surjective() = [2]]

    K = Q(sqrt -7),  h(-7) = 1,  disc K = -7
    N^- = 3 · 2243 · 5843   (inert in K; odd count => DEFINITE)
    N^+ = 2^3 · 4547^2       (split in K)
    B = definite quaternion algebra ramified at 3, 2243, 5843, infinity; Eichler level N^+

**Certified (2026-09-22):** `L(E^{-7}, 1) ∈ [9.054319, 9.054421]`, so by GZK `rank E^{-7}(Q) = 0` and
`Sha(E^{-7}/Q)` finite. Hence `(r^+, r^-) = (2, 0)` and `rank E(K) = 2`.

Supersingular primes of `E` below 2000: `23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823`
(infinitely many, by Elkies). They are **excluded** from this lane.

## 2. The bridge — FORWARD implication only

    for each p >= 5, p ∤ 7N, E ordinary at p :   c_2(p) ∈ Z_p^x   ==>   Sha(E/Q)[p^inf] = 0

It rests on: BD Annals 2005 Cor 3 (lower order); BLV (arXiv 2306.17784) ordinary equality `(L_p) = (Char_p)`; the
BLV↔BD module identification; BD *Derived p-adic heights* 2.18(5) / 2.23 / Cor 2.24 / Lemma 3.1; the exponent bound
`v_p #Sha(E/K)[p^inf] <= 2c`, `p^c = exp Sha(E^{-7}/Q)[p^inf]`; the odd-`p` descent
`Sha(E/K)[p^inf] = Sha(E/Q)[p^inf] ⊕ Sha(E^{-7}/Q)[p^inf]`; and Cassels–Tate on the finite twist summand.

**Status:** two independent Aristotle audits agree, and an **independent external read-only source audit
(2026-09-22) found the forward bridge intact.** Conditional prime by prime. **Not Lean-verified.**

**No converse is asserted.** In particular it is **false** to infer `c_2(p)` a unit from "`Sha(E/K)[p^inf]` finite
and `#Sha(E/K)[p^inf] · R_der(p)` a unit" alone: `R_der` is the product of the regulators of *every* filtration step,
so `R_der != 0` only says the filtration ends at *some* nondegenerate height, i.e. `sigma = rho_p` (BD Def 2.20,
Cor 2.24) — not `rho_p = 4`. Shape of the gap (illustrative, not a claim about this seed): a square-root series
beginning `u·T^4 + …`, `u` a unit, has a unit leading coefficient and `c_2 = 0`. A converse needs the extra hypothesis
`rho_p = 4`.

## 3. Size of the object

Eichler mass of the definite Shimura set carrying the eigenfunctional:

    (1/12) · prod_{p | N^-} (p - 1) · prod_{p^e || N^+} p^{e-1}(p + 1)
      = (1/12) · 26,195,528 · 248,157,072  =  541,717,127,331,168  ≈ 5.42e14

    DIRECT_GROSS_SET_ENUMERATION = INFEASIBLE

That is all the mass proves. It does **not** rule out compressed computation (`GATE.md` K2).

## 4. The witness, bound to BLV's construction

All notation is BLV's (arXiv 2306.17784v2, §2.5 and §§4.1–4.2).

**Gross points.** `P̃_n(L)` is a compatible sequence of special points of conductor `p^n`, defined over the ring class
field `K̃_n`. The point on layer `K_n` is the **trace**

    P_n(L) = Σ_{σ∈Δ} σ( P̃_{n+1}(L) ) ∈ J(K_n),      n >= -1.

So **layer `K_n` uses Gross points of conductor `p^{n+1}`**. The first degree-`p` layer `K_1` uses **conductor `p^2`**.
(Consistent with the ring-class-field arithmetic: the ring class field of conductor `p` has degree `p ± 1` over the
Hilbert class field, prime to `p`, so it meets no layer of the `Z_p`-extension.)

**Eigenfunctional.** `ψ_g : J ⊗ Z_p → R` with `ψ_g(t·x) = g(t)·ψ_g(x)`, required to be **surjective**, and determined
by `g` up to multiplication by a `p`-adic unit. Surjectivity *is* primitivity. Consequence: **the unit status of
`c_2(p)` is normalization-independent within BLV's convention, and changes if `ψ_g` is rescaled by a non-unit.** Do
not rescale.

**Square-root `p`-adic L-function (ordinary), BLV §4.2:**

    calL_{g,n} = α_p(g)^{-n} Σ_{σ∈G_n} ( ψ_g(σ P_{n-1}(L)) − α_p(g)·ψ_g(σ P_n(L)) ) · σ   ∈ Λ_n,
    calL_g = lim_n calL_{g,n},        L_p(g) = calL_g · calL_g^ι.

**Definition of the witness.** Let `G_1 = Gal(K_1/K) = <γ> ≅ Z/p`, `t = γ − 1`, `I = (t)`. **`c_2(p) ∈ Z_p` is the
coefficient of `t^2` in the image of `calL_{g,1}` in `Z_p[G_1]/I^3`.** Its reduction is what the witness asks about.

**Reduction formula.** At `n = 1`, `P_0` lies on `K_0 = K`, so `σ P_0 = P_0` for every `σ ∈ G_1`, and the first term is
`α^{-1}ψ_g(P_0) · N` with `N = Σ_{j=0}^{p-1} γ^j = p + C(p,2) t + C(p,3) t^2 + …`. For `p >= 5`, `N ∈ pΛ + I^3`, so the
stabilization term vanishes mod `(p, I^3)` (`BRANCH_THETA.md` §2). Expanding `γ^j = (1+t)^j = Σ_k C(j,k) t^k` in the
second term:

    c_2(p)  ≡  − Σ_{j=0}^{p-1}  C(j, 2) · ψ_g( γ^j P_1(L) )     (mod p),      P_1 = traced conductor-p^2 Gross point.

The overall sign is BLV's convention and does not affect unit status.

## 5. Known neighbouring literature, and the mismatch

| | published | needed here |
|---|---|---|
| Burungale–He–Kobayashi–Ota, arXiv 2408.13932 | self-dual Hecke character (CM); `p` fixed; treats `ℓ = p`, incl. `p` inert with signed theory | non-CM eigenfunctional; `p` varying; `ℓ = p` |
| Burungale–He–Tian–Ye, arXiv 2508.19706 | self-dual Hecke characters over CM fields; all but finitely many **characters**; auxiliary ordinary `ℓ` fixed | all but finitely many **primes** `p`, with `ℓ = p` |
| Bertolini–Longo–Venerucci, arXiv 2306.17784 | non-CM; `p` split or inert; ordinary or supersingular; main conjecture | used in the bridge; gives no nonvanishing at the trivial character with vanishing `L`-value |

This table records the known gap. It is **not** a prediction of your answer.
