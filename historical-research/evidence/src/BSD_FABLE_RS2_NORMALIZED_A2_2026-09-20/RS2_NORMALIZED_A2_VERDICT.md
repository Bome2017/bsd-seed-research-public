# RS2 BAD-EULER-NORMALIZED A_2 GATE — final output

Date 2026-09-20. Scope: Tasks 1-3 on the normalized kernel only. No pole-distribution computation (already settled, §0).
No arithmeticity. No seed computation (only `a_p = 0` for `p^2 | N` and `a_p = ±1` for `p || N` are used).

    D_N(t) := prod_{p|N} (1 - p^{-2t}),     D_N(-x/2) = prod_{p|N} (1 - p^x),
    P~(x; z) := D_N(-x/2) P(x; z),          P~(x; z) = sum_j A~_j(z) x^j.

## RETURN: `RS2_NORMALIZED_A2_OPEN_AT_EXACT_LEMMA`

Tasks 1 and 2 **close**, including the sign. Task 3 reaches an explicit, L-free structural formula for
`a_{A~_2}(n,y)` and one genuinely new structural fact (§3.1), and stops at a named analytic lemma.

---

## 0. Corrections accepted

* The sentence "consistency requires `m_1 + m_2 = 3`" is **withdrawn**. `ord_{x=0} <P(x),f> = -3` constrains only the
  f-isotypic component, not the kernel. Your orders are right: `m_1 = 1` (the ordinary simple Eisenstein pole) and
  `m_2 = 5` (the `n = 1` coefficient carries the proved factor `1/prod_{p|N}(1-p^x)`, with `theta_2(1) != 0` and no
  cancellation), so the unprojected product may start at `x^{-6}`. The double zero of `L(f,1-x)` forces
  `<A_{-6},f> = <A_{-5},f> = <A_{-4},f> = 0`, and `A_{-3}` is simply the **first f-visible** coefficient.
* The `prod_{p|N} log p` I flagged is therefore **not intrinsic**: it came from taking a Laurent coefficient before
  removing the five obvious bad Euler factors. It disappears under the normalization below. My flag was right that the
  constant was normalization-sensitive; the diagnosis of what it meant was wrong.
* Status recorded as: `UNNORMALIZED TARGET = A_{-3}` (proved), `BAD-EULER-NORMALIZED TARGET = A~_2`.

## 1. Task 1 — the normalizer works identically, not asymptotically

From the formula proved in the previous run,

    Y_{0,infinity}(n,t) = N^{-t} [ zeta(2t) / zeta^{(N)}(2t) ] n^{t-1} sigma^{(N)}_{1-2t}(n),
    zeta(2t)/zeta^{(N)}(2t) = 1 / prod_{p|N}(1 - p^{-2t}) = 1 / D_N(t),

so **`D_N(t) Y_{0,infinity}(n,t) = N^{-t} n^{t-1} sigma^{(N)}_{1-2t}(n)`** — an identity of meromorphic functions, with the
five bad-prime poles removed exactly and for every `n`, not term by term or asymptotically. `sigma^{(N)}_{1-2t}(n)` and
`N^{-t} n^{t-1}` are entire and non-vanishing near `t = 0`, so the normalized coefficients are **regular at `t = 0`**.

## 2. Task 2 — the normalized pairing and `kappa~_N`, sign resolved

Multiplying the pairing identity derived in the previous run by `D_N(-x/2) = prod_{p|N}(1-p^x)` cancels the offending factor
identically and gives exactly your expression:

    < -P~(x), f > = [ zeta(2-x) Gamma(1-x) N^{x/2} / ( (2 pi)^{3-x} zeta^{(N)}(2-x) ) ]
                    * L(f,2) * L(f,1-x) * prod_{p|N} (1 - a_p p^{x-1}).

Every factor except `L(f,1-x)` is regular and non-zero at `x = 0`, so **`ord_{x=0} <P~(x),f> = 2`**, hence
`<A~_0,f> = <A~_1,f> = 0` and, using `L(f,1-x) = L''(f,1) x^2/2 + O(x^3)`, `Gamma(1) = 1`, `N^0 = 1`, and
`zeta(2)/zeta^{(N)}(2) = 1/prod_{p|N}(1-p^{-2})`:

    **< A~_2 , f > = kappa~_N * L(f,2) * L''(f,1),**

    **kappa~_N = - prod_{p || N} (1 - a_p/p) / [ 2 (2 pi)^3 prod_{p|N} (1 - p^{-2}) ].**

`prod_{p|N} log p` is gone, as you predicted.

**The sign is determined, not left open.** The minus is the factor `(-1)^{k_2/2}` in the ANT left-hand side with `k_2 = 2`.
The three candidate sources of further sign ambiguity are each neutral here:
1. *Phase orientation.* The cross-cusp phase sums to a Ramanujan sum, and `r_delta(n)` is real and even
   (`r_delta(-n) = r_delta(n)`), so the orientation of `e(±n d/c)` does not matter.
2. *Choice of `sigma_0`.* Replacing `sigma_0` by `-sigma_0` acts identically on H and changes `j(sigma_0,z)^{-k}` by
   `(-1)^k = +1` for even `k`.
3. *`±I`.* `-I in Gamma_0(N)` gives `eps_0 = 1`, so ANT's `2^{eps_0-1} = 1`; and the printed cross-cusp formula carries no
   such factor in any case.

Numerically, for the seed: `prod_{p|N}(1-p^{-2}) = 0.66666648238...`, `2(2 pi)^3 = 496.10042688...`, so the denominator is
`330.7335265007...`; the numerator is `0.66625539991...` if all three `a_p = +1` and `1.33415607032...` if all three are `-1`
(`p || N` at `3, 2243, 5843`; `p^2 | N` at `2, 4547` contributes `1`). **Non-zero for every sign pattern**, and no `a_p` was
computed.

**One residual, unchanged and named:** that `Y_{ba}(n,t) = zeta(2t) n^{t-1} Z_{ba}(n,t)` holds verbatim for `b != a` rests on
the uniformity of the Iwaniec Fourier-coefficient normalization in the cusp pair — (3.21)-(3.22), still not obtained. It is a
normalization, not a sign, and it cannot affect `ord = 2` or the non-vanishing.

## 3. Task 3 — positive-frequency structure of `A~_2`

Write `P~(x;z) = (y^{-1}/2 pi) * A(x;z) * E~(x;z)` with `A(x;z) = E*_{0,infinity}(z, 1-x/2)` and
`E~(x;z) = D_N(-x/2) E*_{2,0}(z, -x/2)`. By Task 1 the non-constant Fourier coefficients of `E~` are regular at `x = 0`
(`theta_2(0) = zeta(0) = -1/2`, non-zero), and by §0 `A` has a simple pole. Since `n > 0`, the Poincaré unfolding
`< A~_2, P_n(., rbar) >` sees only positive frequencies and the constant term of `A~_2` never enters — the `y log^3 y` issue
stays withdrawn.

The `n`-th coefficient of a product is the convolution of the coefficients, so for `n >= 1`

    a_{P~}(n,y) = (y^{-1}/2 pi) * [ a_A(0,y) a_{E~}(n,y) + sum_{l != 0} a_A(l,y) a_{E~}(n-l,y) ],

and `a_{A~_2}(n,y)` is the `x^2` coefficient of this.

### 3.1 A new structural fact: the shifted convolution is sparse

`A` is the weight-0 Eisenstein series **at the cusp infinity**, so its `l`-th coefficient carries the *diagonal* sum
`Z_{infinity,infinity}(l,t) = sum_{N|c} r_c(l) c^{-2t}`. By the lemma proved in the diagonal run — `r_c(l) = 0` whenever
`p^2 | c` and `p` does not divide `l` — and since `N | c` forces `p^2 | c` for `p in {2, 4547}`:

    **a_A(l,y) = 0 unless 9094 | l,     9094 = 2 * 4547.**

So the shifted convolution runs only over `l ≡ 0 (mod 9094)`, and

    a_{P~}(n,y) = (y^{-1}/2 pi) [ a_A(0,y) a_{E~}(n,y)  +  sum_{l != 0, 9094 | l} a_A(l,y) a_{E~}(n-l,y) ].

This is the same local lemma that killed the diagonal kernel, reappearing in a completely different role: there it annihilated
the pairing, here it merely thins the convolution. It is a genuine simplification — the leading term is a clean product, and
the correction is supported on a sparse arithmetic progression.

### 3.2 The pieces are explicit and L-free

Every ingredient is available in closed form and none refers to `L(f,2) L''(f,1)`:
* `a_A(0,y) = theta(s) y^s + theta(1-s) Y_{infinity,infinity}(s) y^{1-s}` at `s = 1-x/2`, with `theta(s) = pi^{-s}Gamma(s)zeta(2s)`
  — the source of the `y log^j y` terms, and of `R_{-1}`;
* `a_A(l,y) = Y_{infinity,infinity}(l, 1-x/2) W_{1-x/2}(lz)`-type, with `W_s(lz) = 2(|l|y)^{1/2} K_{s-1/2}(2 pi |l| y) e(lx)`,
  non-zero only for `9094 | l`;
* `a_{E~}(m,y) = theta_2(-x/2) D_N(-x/2) Y^{(2)}_{0,infinity}(m,-x/2)` times the weight-2 Whittaker function, with the
  arithmetic part `N^{x/2} m^{-x/2-1} sigma^{(N)}_{1+x}(m)` by Task 1.

So `a_{A~_2}(n,y)` is an explicit finite combination of: divisor sums `sigma^{(N)}`, powers of `y` and `log y`, `K`-Bessel
functions and their `s`-derivatives, and one sparse shifted convolution of Bessel products. **The determination asked for in
Task 3 is therefore affirmative at the structural level: the coefficient is computable without ever invoking the L-values.**

### 3.3 The exact remaining lemma

What is *not* done is the analysis, not the construction:

> **(L3)** Prove the unfolded identity `< A~_2, P_n(., rbar) > = C_n(r) int_0^infty a_{A~_2}(n,y) e^{-2 pi n y} y^r dy` in a
> region of absolute convergence; meromorphically continue the right-hand side to `r = 0`; and show
> `c_n = FP_{r=0}[...]` is the `n`-th Fourier coefficient of the cuspidal projection of `A~_2`, for finitely many `n`
> spanning the dual of `S_2(Gamma_0(N))`.

**First unsupported equation:** the continuation to `r = 0` of the **sparse shifted-convolution term**,

    int_0^infty [ sum_{l != 0, 9094 | l} a_A(l,y) a_{E~}(n-l,y) ] e^{-2 pi n y} y^r dy,

i.e. the interchange of the `l`-sum with the `y`-integral and the continuation of the resulting Bessel-product series past
`r = 0`. The `l = 0` term poses no such problem — it is an explicit `y^a (log y)^b` times a Bessel function, whose Mellin
transform continues by inspection. The difficulty is entirely in the shifted sum, which is the classical shifted-convolution
situation; the sparsity `9094 | l` is a help, not a substitute for the continuation.

## 4. Status to record

    UNNORMALIZED TARGET A_{-3}              = PROVED (previous run)
    FACTOR POLE ORDERS m_1 = 1, m_2 = 5     = SETTLED (your argument; not recomputed)
    D_N NORMALIZATION                       = PROVED, identical not asymptotic
    < A~_2, f > = kappa~_N L(f,2) L''(f,1)  = PROVED, sign resolved, kappa~_N != 0
    prod_{p|N} log p                        = ARTEFACT, removed
    a_A(l,y) SUPPORTED ON 9094 | l          = PROVED (new; thins the shifted convolution)
    a_{A~_2}(n,y) EXPLICIT AND L-FREE       = ESTABLISHED STRUCTURALLY
    (L3) POINCARE CONTINUATION AT r = 0     = OPEN, the gate

Endpoint effect: **NONE**, unchanged, and it stays NONE until the normalized coefficients acquire arithmetic content. A
seed-level run remains unwarranted: (L3) is a statement about `Gamma_0(N)` in general.

---

Sources: Diamantis-O'Sullivan ANT 7 (2013) 1883-1917 and arXiv:0904.2179, both previously obtained in full, plus the results
proved in the four preceding sealed folders. **Cited, not obtained:** Iwaniec, *Spectral Methods*, (3.21)-(3.22).
Derived here: Task 1 identity, Task 2 pairing and `kappa~_N` with sign, and §3.1. Numerical values checked symbolically.
Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim. All predecessor folders sealed and unedited.
