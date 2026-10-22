# RS2 A_2 POINCARE-PROJECTION GATE — final output

Date 2026-09-20. Scope: Tasks 1-4 only. No new candidates, no arithmeticity of shifted convolutions, no seed computation
(no `a_p` evaluated; only `a_p = 0` for `p^2 | N` and `a_p = ±1` for `p || N` are used).

## RETURN: `RS2_A2_POINCARE_OPEN_AT_EXACT_LEMMA`

**Task 1 closes — your `Y` formula is correct, and `kappa_N` is now derived, not matched.** But carrying it through produces
a structural correction that changes which Laurent coefficient the gate is about:

> **At level N the target is `A_{-3}`, not `A_2`.** `<P(w), f>` has a **pole of order 3** at `w = 1`.
> The four-term structure `A_2 = (y^{-1}/2 pi)(R_{-1}B_3 + R_0B_2 + R_1B_1 + R_2B_0)` is **correct at level 1 only**.

Tasks 2-4 are therefore not executed against `A_2`: they would extract the wrong coefficient. The Poincaré formulation itself
survives intact and is the right tool — redirected onto `A_{-3}`.

---

## 1. Task 1 — the cross-cusp normalization, closed

**1a. The double coset and the phase (derived, no Iwaniec needed).** With `sigma_0 = (0, -1/sqrt N; sqrt N, 0)` and
`gamma = (alpha, beta; N gamma', delta)` in `Gamma_0(N)`,

    gamma sigma_0 = ( beta sqrt N, -alpha/sqrt N ; delta sqrt N, -gamma' sqrt N ),

so `c = delta sqrt N` and `d = -gamma' sqrt N`. Left multiplication by `Gamma_infinity` fixes the bottom row of `gamma`; right
multiplication sends `d -> d + cm`. So the double coset `Gamma_inf \ Gamma_0(N) sigma_0 / Gamma_inf` is parametrised by
`delta > 0` with `(delta, N) = 1` together with `-gamma' mod delta`, and `det = 1` forces `gcd(gamma', delta) = 1`. Hence

    sum_{d mod c} e(n d / c) = sum_{gamma' mod delta, (gamma',delta)=1} e(-n gamma'/delta) = r_delta(n),

the **plain Ramanujan sum** — the anticipated `N^{-1} mod c` twist does not even arise in this parametrisation. Therefore

    Z_{0,infinity}(n,t) = sum_{(delta,N)=1} r_delta(n) (delta sqrt N)^{-2t} = N^{-t} sigma^{(N)}_{1-2t}(n) / zeta^{(N)}(2t),

with `sigma^{(N)}_alpha(n) = sum_{d|n,(d,N)=1} d^alpha` and `zeta^{(N)}(s) = zeta(s) prod_{p|N}(1 - p^{-s})`.

**1b. Your boxed formula is confirmed.** ANT's own normalization (stated in the proof of Thm 10.1 for a general Fuchsian
group, and uniform in the cusp pair because it is just the Iwaniec Fourier-coefficient normalization) is
`Y_{ba}(n,t) = zeta(2t) n^{t-1} Z_{ba}(n,t)`. So

    **Y_{0,infinity}(n,t) = N^{-t} * [ zeta(2t) / zeta^{(N)}(2t) ] * n^{t-1} * sigma^{(N)}_{1-2t}(n).**

And your prediction that there is **no hidden Gamma or pi** is right: with `theta(s) = pi^{-s} Gamma(s) zeta(2s)` and the
Iwaniec coefficient `pi^s |l|^{s-1}/Gamma(s) * Z(l,s)`, the `pi` and `Gamma` cancel exactly, leaving `zeta(2s) |l|^{s-1} Z`.
The only surviving extra factor is the **level-dependent ratio**

    zeta(2t) / zeta^{(N)}(2t) = 1 / prod_{p|N} (1 - p^{-2t}),

which is invisible at level 1 (empty product) and is the whole content of the correction below.

**1c. The correction.** At the target, `1 - v = -x/2 -> 0`, so that ratio is evaluated at `t -> 0`, where

    prod_{p|N} (1 - p^{x}) = (-x)^{omega(N)} prod_{p|N} log p * (1 + O(x)).

For `N = 2^3 * 3 * 2243 * 4547^2 * 5843`, `omega(N) = 5`, so this is a **zero of order 5**, i.e. `Y_{0,infinity}(n, -x/2)` has a
**pole of order 5** at `x = 0`, uniformly in `n` (the pole factors out of the `n`-sum). Verified symbolically:
`prod_{p|N}(1-p^x) ~ x^5 * (-log 2 log 3 log 2243 log 4547 log 5843)`, constant `-429.17455509538...`.

Meanwhile the `n`-sum contributes `L(f,2) L^{(N)}(f,1-x) / zeta^{(N)}(2-x)` and `L^{(N)}(f,1-x)` has only a **double zero**
(the depletion factor `prod_{p||N}(1 - a_p p^{x-1})` is regular and non-zero). Net:

    **ord_{w=1} < P(w), f > = -(5 - 2) = -3.**

This is a level-N phenomenon, structurally invisible at level 1, and it is the reason the previous run's `A_2` identification
must be withdrawn. Its mechanism is worth naming: **ANT applies the level-1 completion `theta_k(s) = pi^{-s} Gamma(s+|k|/2)
zeta(2s)` even for a general Fuchsian group**, so `E*_{k,a}` at level N is completed only in the level-1 sense and its
coefficients retain the uncancelled Euler factors `prod_{p|N}(1-p^{-2t})^{-1}`. Concretely: `B_0 = E*_{2,0}(z,0)` is **not
finite at level N**, so the second factor's Laurent expansion does not begin at `x^0` and the four-term convolution is not the
`x^2` coefficient of `(simple pole) x (Taylor series)`.

**1d. `kappa_N`, derived.** Taking `s = 0`, `k = 2`, `(k_1,k_2) = (0,2)`, `a = infinity`, `b = 0` in the printed mixed-cusp
pairing, and writing `x = w - 1`:

    < -P(w), f > = [ zeta(2-x) Gamma(1-x) N^{x/2} / (2 pi)^{3-x} ] * [ 1 / prod_{p|N}(1-p^{x}) ]
                   * L(f,2) * L(f,1-x) * prod_{p|N}(1 - a_p p^{x-1}) / zeta^{(N)}(2-x).

Every bracketed factor except the second is regular and non-zero at `x = 0`. With `L(f,1-x) = L''(f,1) x^2/2 + O(x^3)` and
`prod_{p|N}(1-p^x) = -x^5 prod log p (1 + O(x))`, the `x^{-3}` coefficient is

    **< A_{-3}, f > = kappa_N * L(f,2) * L''(f,1),**

    **kappa_N = prod_{p || N} (1 - a_p / p)  /  [ 2 (2 pi)^3 * prod_{p|N} (1 - p^{-2}) * prod_{p|N} log p ]**

(using `zeta(2)/zeta^{(N)}(2) = 1/prod_{p|N}(1-p^{-2})`, `Gamma(1) = 1`, `N^0 = 1`). For the seed the `p^2 | N` primes
`2` and `4547` contribute `1` to the first product, and `p || N` gives `a_p = ±1` at `3, 2243, 5843`, so each factor is
`1 ∓ 1/p != 0`. **`kappa_N != 0` for either sign, and no `a_p` had to be computed.**

Not determined by level-1 matching: the derivation uses only the ANT printed pairing, the scaling-matrix computation of §1a,
the `Y` normalization of §1b, and the depleted Rankin factorization.

**Residual named factor (small, honest).** Two things in §1b rest on uniformity I did not verify against Iwaniec
(3.21)-(3.22): the claim that `Y_{ba}(n,t) = zeta(2t) n^{t-1} Z_{ba}(n,t)` holds verbatim for `b != a`, and the overall
sign/orientation convention for which entry of `gamma sigma_0` supplies the phase. Neither can change the **pole order** or the
**non-vanishing** of `kappa_N`; both could change `kappa_N` by an explicit non-zero rational or a sign.

## 2. Tasks 2-4 — the Poincaré formulation is right, but aimed at the wrong coefficient

Your reasoning for the Poincaré route is accepted in full and is unaffected by §1c: `<A_j, g>` converges for every cusp form
`g` despite polynomial-logarithmic growth, so existence of the cuspidal component was never the issue; the issue is getting it
**constructively**; and unfolding

    < A_j , P_n(., rbar) >,   P_n(z,r) = sum_{Gamma_inf \ Gamma_0(N)} (Im gamma z)^r e^{2 pi i n gamma z} j(gamma,z)^{-2},

against a **positive-frequency** Poincaré series selects `a_{A_j}(n,y)` and never sees the constant term. That bypasses the
`y log^3 y` issue exactly as you said, and I withdraw "weight-2 regularized projection at `y log^3 y`" as the gate.

What I will not do is run Tasks 2-4 on `A_2`. By §1c, `<A_2, f>` is **not** `kappa_N L(f,2) L''(f,1)`; it is one of the
regular terms after a third-order pole, and extracting its Fourier coefficients would answer a question we no longer want to
ask. The same three tasks, verbatim, are the right programme for `A_{-3}`:

* unfold `< A_{-3}, P_n(., rbar) > = C_n(r) int_0^infty a_{A_{-3}}(n,y) e^{-2 pi n y} y^r dy` in a region of absolute
  convergence;
* continue to `r = 0` and identify `FP_{r=0}` with the `n`-th coefficient of the cuspidal projection, for finitely many `n`
  spanning the dual of `S_2(Gamma_0(N))`;
* derive `a_{A_{-3}}(n,y)` from the two Eisenstein Fourier expansions.

**The exact lemma the gate now turns on** is the replacement for the four-term structure:

> Determine the exact orders `m_1, m_2` of the poles of `E*_{0,infinity}(z, 1-x/2)` and `E*_{2,0}(z, -x/2)` at `x = 0` for
> `Gamma_0(N)`, and give the Laurent coefficients of the second factor explicitly. Equivalently: compute the level-N
> completion that cancels `prod_{p|N}(1-p^{-2t})^{-1}`, and re-derive the convolution expressing `A_{-3}` in terms of the two
> towers. Consistency requires `m_1 + m_2 = 3` on the f-isotypic component; §1c gives `5` from the arithmetic factor and `2`
> back from the double zero, but it does **not** yet say how the 3 is distributed between the two factors, and the weight-2
> normalization `theta_2 = t * theta` suggests one order is absorbed there.

That is the first unsupported equation: **the distribution of the order-3 pole between the two Eisenstein factors, and hence
the explicit Laurent coefficients of `E*_{2,0}(z,-x/2)` at level N.**

## 3. Status to record

    CROSS_CUSP_NONZERO_FACTORIZATION   = PROVED       (unchanged)
    Y_{0,infinity}(n,t) FORMULA        = PROVED       (this run; your boxed formula, derived)
    EXACT_COMPLETED_CONSTANT kappa_N   = DERIVED      (this run; explicit, non-zero; up to one named sign/uniformity factor)
    TARGET COEFFICIENT                 = A_{-3}, NOT A_2   (this run; pole of order 3 = omega(N) - 2)
    FOUR-TERM STRUCTURE FOR A_2        = LEVEL 1 ONLY (withdrawn at level N)
    POINCARE POSITIVE-FREQUENCY ROUTE  = ACCEPTED as the correct extraction method, not yet executed
    a_n(H) EXPLICIT                    = NOT REACHED

Endpoint effect: **NONE**, unchanged. Note that `kappa_N` contains `prod_{p|N} log p` — a transcendental-looking constant that
did not appear at level 1 and that will matter later when the arithmetic nature of the coefficients is finally asked about.
That is flagged, not analysed, since arithmeticity is out of scope here.

---

Sources: Diamantis-O'Sullivan ANT 7 (2013) 1883-1917 (full text, previously obtained) — (2-5), (2-7), (4-2), (4-3), (4-4),
§10 Thm 10.1 and its proof; Diamantis-O'Sullivan arXiv:0904.2179 (full text) — Prop 2.1, (2.8)-(2.11), Lemma 2.2.
**Cited, not obtained:** Iwaniec, *Spectral Methods*, (3.21)-(3.22) — see the residual named factor in §1d.
Derived here: §1a scaling and phase, §1b `Y` formula, §1c pole order (with a symbolic check), §1d `kappa_N`.
Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim. All predecessor folders sealed and unedited.
