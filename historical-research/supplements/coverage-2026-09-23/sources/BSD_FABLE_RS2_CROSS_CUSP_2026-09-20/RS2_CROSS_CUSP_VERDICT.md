# RS2 CROSS-CUSP (infinity, 0) GATE — final output

Date 2026-09-20. Scope: the mixed-cusp pairing in the proof of Diamantis-O'Sullivan Theorem 10.1, with a = infinity, b = 0,
for Gamma_0(N), N = 2^3 * 3 * 2243 * 4547^2 * 5843. Master not updated. No seed arithmetic launched (no a_p computed).

## RETURN: `RS2_CROSS_CUSP_OPEN_AT_EXACT_LEMMA`

Items 1-4 discharge **positively**. Item 5 discharges positively modulo normalization bookkeeping that is pinned by
consistency, not derived end-to-end. Item 6 is the single remaining lemma. **The diagonal obstruction does not extend: the
cross-cusp pairing is not termwise zero, and every bad-prime local factor is explicitly non-zero.**

---

## 0. Corrections accepted and applied

1. **`<A_j, f> = 0` gives only `e_f Pi_cusp A_j = 0`, not `Pi_cusp A_j = 0`.** The previous verdict's §3 is narrowed to the
   f-isotypic component. (`../BSD_FABLE_RS2_REG_KERNEL_2026-09-20/` is sealed and not edited; this file supersedes it there.)
   Note this correction *helps*: for our purpose only the f-component is ever needed, so the polar parts never have to die in
   the whole cusp space.
2. **The previous claim "the surviving cusps are precisely the inaccessible ones" is WITHDRAWN and was simply wrong.** The
   mixed-cusp formula carries `a_{g,a}(n)` with **a = infinity** — the *ordinary* Fourier coefficients of f. Only the
   Eisenstein series moves to the cusp 0. No cusp expansion of f at a hard cusp is needed anywhere.
3. The previous return is narrowed to **`RS2_DIAGONAL_CUSPS_{infinity,0} = OBSTRUCTED`**. That computation stands: same-cusp
   moduli satisfy N | c, every such c is divisible by p^2, r_c(n) = 0 off p | n, and a_n(f) = 0 on p | n.

## 1. Item 1-2: the scaling matrix and the allowed moduli (derived)

Take the standard scaling matrix for the cusp 0 of Gamma_0(N):  `sigma_0 = (0, -1/sqrt(N); sqrt(N), 0)`.
For `gamma = (alpha, beta; N gamma', delta)` in Gamma_0(N),

    gamma sigma_0 = ( beta sqrt(N), -alpha/sqrt(N) ; delta sqrt(N), -gamma' sqrt(N) ),

so the lower-left entry is `delta sqrt(N)`, and `det = 1` forces `alpha delta ≡ 1 (mod N)`, hence `gcd(delta, N) = 1`.

    **C_{infinity,0} = { c sqrt(N) : c >= 1, gcd(c,N) = 1 }.**

This is the whole point. **Same cusp: `N | c`. Cross cusp: `(c,N) = 1`.** The support condition flips, and the `p^2 | N`
annihilation that killed the diagonal kernel cannot occur, because no allowed modulus is divisible by p at all.

## 2. Item 3: the zero-argument Kloosterman sum reduces to a Ramanujan sum (derived)

With one argument zero, `S_{0,infinity}(0, n; c sqrt(N))` collapses to the Ramanujan sum `r_c(n * Nbar)` where
`Nbar = N^{-1} mod c`. Since `gcd(N,c) = 1`, multiplication by `Nbar` is a bijection of `Z/c` preserving `gcd(n,c)`, and
`r_c` depends on n only through `gcd(n,c)`; so **`r_c(n Nbar) = r_c(n)`** — the twist is harmless, as expected.

Hence, with `t` the spectral variable,

    sum_{c' in C_{infinity,0}} S(0,n;c') c'^{-2t}
        = N^{-t} sum_{c >= 1, (c,N)=1} r_c(n) c^{-2t}
        = N^{-t} * sigma^{(N)}_{1-2t}(n) / zeta^{(N)}(2t),                                   ... (R)

where `sigma^{(N)}_alpha(n) = sum_{d | n, (d,N)=1} d^alpha` and `zeta^{(N)}` is the N-depleted zeta. (R) follows from the
classical `sum_c r_c(n) c^{-2t} = sigma_{1-2t}(n)/zeta(2t)` by deleting the p | N Euler factors on both sides. **Non-zero.**

## 3. Item 4: Euler factorization with the five local factors (derived)

Both `a_n(f)` and `sigma^{(N)}_alpha(n)` are multiplicative, so `D(beta) = sum_n a_n(f) sigma^{(N)}_alpha(n) n^{-beta}`
factors as `prod_p D_p`. For `p` not dividing N, `sigma^{(N)}_alpha(p^j) = sigma_alpha(p^j)` and D_p is the usual Rankin local
factor. For `p | N`, the only divisor of `p^j` coprime to N is 1, so `sigma^{(N)}_alpha(p^j) = 1` and

    D_p = sum_{j>=0} a_{p^j}(f) p^{-j beta} = L_p(f, beta).

Therefore

    **sum_n a_n(f) sigma^{(N)}_alpha(n) n^{-beta} = L(f,beta) * L^{(N)}(f, beta-alpha) / zeta^{(N)}(2beta - alpha - k + 1).**

The five local factors at the seed's primes, at the p-depleted argument:

| p | v_p(N) | a_p(f) | local factor D_p | value |
|---|---|---|---|---|
| 2    | 3 | 0 (since p^2 \| N) | 1 | **non-zero** |
| 4547 | 2 | 0 (since p^2 \| N) | 1 | **non-zero** |
| 3    | 1 | ±1 (Atkin-Lehner) | (1 - a_3 3^{-beta})^{-1} | **non-zero** |
| 2243 | 1 | ±1 | (1 - a_2243 2243^{-beta})^{-1} | **non-zero** |
| 5843 | 1 | ±1 | (1 - a_5843 5843^{-beta})^{-1} | **non-zero** |

The two primes that destroyed the diagonal kernel, 2 and 4547, contribute the factor **1** here — harmless, not fatal.
No `a_p` was computed: for `p^2 | N` the value 0 is forced, and for `p || N` weight 2 forces `a_p = ±1`, which is all the
non-vanishing argument needs.

## 4. Item 5: the arguments, and consistency with the paper's own level-1 identity

ANT (2-16): `u = (s + w - k + 1)/2`, `v = (-s + w + 1)/2`. In the mixed-cusp pairing from the proof of Thm 10.1,

    < (-1)^{k_2/2} y^{-k/2} E*_{k_1,a}(., 1-u) E*_{k_2,b}(., 1-v) / (2 pi^{k/2}) , g >
        = 2^{eps_0 - 1} * zeta(2-2u) Gamma(k-s) Gamma(k-w) / (2 pi)^{2k-s-w}
          * sum_n Y_{ba}(n, 1-v) a_{g,a}(n) / n^{k-s-v}.

Using `Y(n,t) = zeta(2t) n^{t-1} * (c-sum)` at `t = 1-v`, the `n^{-v}` cancels against `n^{-(k-s-v)}` and the n-series becomes
`sum_n a_n(f) sigma^{(.)}_{alpha}(n) n^{-beta}` with

    **beta = k - s,   alpha = 2v - 1,   beta - alpha = k - w,   2 beta - alpha - k + 1 = k + 1 - s - w.**

The denominator `zeta(k+1-s-w)` **matches ANT (7-4) exactly** at level 1, which is the check that the variable bookkeeping is
right. So at level 1, same cusp, the series is `L(f,k-s) L(f,k-w) / zeta(k+1-s-w)`, which with the Gamma factors and the
functional equation (2-1) is Theorem 2.3's `L*(f,s) L*(f,w)`. At level N, cusps (infinity, 0), the same computation with (R)
gives

    **C_N(s,w) * L(f, k-s) * L^{(N)}(f, k-w) / zeta^{(N)}(k+1-s-w),**

with C_N collecting `2^{eps_0-1}`, the Gamma factors, `(2 pi)^{-(2k-s-w)}`, `zeta(2-2u)`, and the power `N^{-(1-v)}` from (R).
Applying the level-N functional equation to the *full* `L(f,k-s)` (which carries `N^{(k-2s)/2}` and the sign eps) converts it
to `L*(f,s)`; the depleted `L^{(N)}(f,k-w)` has no functional equation and stays where it is — which is harmless, because

    L^{(N)}(f, w') = L(f, w') * prod_{p || N} (1 - a_p p^{-w'}),

and at the central point `w' = 1` the correction `prod_{p || N} (1 - a_p/p)` with `a_p = ±1` and `p` in {3, 2243, 5843} lies in
`{1 ± 1/p}` — **non-zero, rational, explicit**. Hence `L^{(N)}(f,·)` has exactly the same double zero at the central point as
`L(f,·)`, and

    (L^{(N)})''(f,1) = L''(f,1) * prod_{p || N} (1 - a_p/p),     a non-zero rational multiple.

**Conclusion of item 5: C_N is regular and non-zero at the target point.** Bookkeeping caveat, stated plainly: the Gamma- and
N-power constants were pinned by requiring the level-1 specialization to reproduce Thm 2.3 and (7-4), not derived
independently line by line. The *non-vanishing* conclusion does not depend on those constants; the exact rational constant in
front of `L(f,2) L''(f,1)` does.

## 5. Item 6: where it actually stands, and the exact remaining lemma

Set `k = 2` and ask for L-arguments `{k-s, k-w} = {2, 1}`, i.e. **`(s,w) = (0,1)`**. Then

    1 - u = 1 - (s+w-k+1)/2  ->  1        and        1 - v = 1 - (-s+w+1)/2  ->  0   as w -> 1.

So the kernel is `y^{-1} E*_{0,infinity}(z, 1-u) E*_{2,0}(z, 1-v) / (2 pi)` with `k_1 = 0, k_2 = 2` — **a weight-0 times a
weight-2 real-analytic Eisenstein series at different cusps.** Note this side of Thm 10.1 only needs `k_1, k_2 >= 0` even; the
`k_1, k_2 >= 3` / `k >= 6` restriction belongs to the *holomorphic* double Eisenstein series (2-9), which we are not using.
The weight-2 barrier that closed the previous two runs is therefore absent from this object.

At the target, `E*_{0,infinity}` sits at spectral parameter 1, i.e. **at its simple pole**, while `L*(f,s) L*^{(N)}(f,k-w)`
has a **double zero** in `w` at `w = 1`. So the identity is an equality of Laurent series in `(w-1)`: a simple pole on the
left, a double zero on the right. Comparing coefficients, the `(w-1)^2` coefficient `A_2` of the kernel carries the target,
and the polar and low-order coefficients pair to zero against f automatically — by the correction in §0.1 this is exactly the
f-isotypic statement we need, and nothing more is required of them.

**This closes the loop with the original RS2 identity.** The expansion of `E*_{0,infinity}(z, 1-u)` in `(w-1)` as its argument
approaches 1 *is* the Laurent tower `residue, K_1 = E^(0), E^(1), E^(2)` of REOPEN_VERDICTS.md §1. The cross-cusp kernel is
not a new mechanism; it is the same mechanism with the second Eisenstein factor moved to the cusp 0, which is precisely what
repairs the local factors.

> **Exact remaining lemma (item 6).** Let `A_2(z)` be the `(w-1)^2` Laurent coefficient at `w = 1` of
> `y^{-1} E*_{0,infinity}(z, 1-u(w)) E*_{2,0}(z, 1-v(w)) / (2 pi)` with `(s,w) = (0,w)`. Prove that the regularized weight-2
> cuspidal projection `Pi_cusp A_2` is a well-defined element of `S_2(Gamma_0(N))` with computable Fourier coefficients, the
> simple pole of `E*_{0,infinity}` at spectral parameter 1 and the weight-2 quasimodular correction of `E*_{2,0}` at spectral
> parameter 0 both being absorbed; and identify the resulting `<Pi_cusp A_2, f>` with `C_N * L*(f,2) * (L^{(N)})''(f,1)/2`.

Nothing located so far obstructs it, and the user's point stands that regularized weight-2 holomorphic projection is
established technology rather than an invention problem. It was **not** attempted here, per "only if that succeeds".

## 6. Status to record

    RS2_DIAGONAL_CUSPS_{infinity, 0} = OBSTRUCTED        (previous run; stands, narrowed as in §0.3)
    RS2_CROSS_CUSP_(infinity, 0)     = OPEN AT ONE LEMMA (this run; arithmetic factor non-degenerate, local factors explicit)

This is the first time in this sequence that a positive step survives a bad-prime computation rather than dying at one. It is
**not** a claim of proximity to FORMULA: even with item 6, the route yields an arithmetic statement about
`L(f,2) L''(f,1) / (pi^4 <f,f>)`, and reaching `q = 36` still needs the Beilinson side for `L(f,2)` and the
`<f,f>` vs `Omega_E` comparison, exactly as recorded before. A seed-level proof run is still **not** warranted: item 6 is a
general statement about `Gamma_0(N)` with nothing seed-specific in it.

---

Primary source read in full: Diamantis-O'Sullivan, ANT 7 (2013) 1883-1917 — (2-9), (2-10), (2-16), Thm 2.3, Prop 2.5 with
(6-10), Def. 3.1/3.2, (4-1), (4-2), (4-3), (4-4), (4-5), Prop. 4.2, Prop. 4.3, (7-4), §10 Thm 10.1 with its proof, Cor. 10.2.
Derived here and **not** taken from a source: the scaling-matrix computation of `C_{infinity,0}`, the harmlessness of the
`Nbar` twist, identity (R), the Euler factorization and the five local factors, the argument bookkeeping, and the Laurent
structure at the target. Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim.
