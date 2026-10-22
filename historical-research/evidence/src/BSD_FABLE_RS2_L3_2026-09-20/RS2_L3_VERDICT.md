# RS2 L3 — final output. HARD STOP.

Date 2026-09-20. Scope: L3 only. Tasks 1-2 of the previous run not reopened. No master rewrite, no seed computation, no new
candidate. This is the terminal run of the RS2 thread.

## RETURN: `RS2_L3_REQUIRES_NEW_GENERAL_THEOREM`

## AND: the hard stopping rule **fires**. Task 5 can be answered now, independently of Tasks 1-4, and its answer is
## "shifted-convolution / Estermann / Bessel special values, nothing touching the regulator". **RS2 is archived.**

---

## 0. Correction applied and verified

Your correction is right and my §3.1 was wrong. The exact condition is `r_{p^j}(l) != 0 => v_p(l) >= j-1`, and `N | c` forces
`v_p(c) >= e = v_p(N)`, so a necessary condition for any surviving term is `v_p(l) >= e-1`. With `v_2(N) = 3` and
`v_{4547}(N) = 2`:

    **a_A(l,y) = 0 unless 2^2 * 4547 = 18188 divides l.**

I had used only the `p^2` lemma, which gives `v_p(l) >= 1` and hence the weaker `9094`. Verified numerically on a model level
with the same exponent pattern (`N_0 = 2^3 * 5^2 = 200`, predicted modulus `2^2 * 5 = 20`): over `c <= 40000`, the `l` with
`Z_{infinity,infinity}(l) != 0` are exactly `20, 40, 60, 80, 100, 120`, and every `l` that the weaker `p^2`-only prediction
would have allowed (`10, 30, 50, 70, 90, 110`) is **zero**. Every `9094` in the previous verdict is replaced by `18188`.
This doubles the sparsity and strictly helps L3.

## 1. Task 1 — interchange, provable

For `l != 0`, `a_A(l,y)` carries `2(|l|y)^{1/2} K_{1/2-x/2}(2 pi |l| y)` (and, after the `x^2` Laurent extraction,
`x`-derivatives of it, which produce `log|l|` factors and `d/d nu` of `K` but **not** worse decay). For `m != 0`,
`a_{E~}(m,y)` carries the weight-2 Whittaker function `W_{sgn(m), nu'}(4 pi |m| y)`. With `m = n - l`, the product decays like
`e^{-2 pi (|l| + |n-l|) y}`, and for `|l| > n` that is `e^{-2 pi (2|l| - n) y}`; against the Poincaré factor `e^{-2 pi n y}`
the total is `e^{-4 pi |l| y}`. Hence

    int_0^infty (...) e^{-2 pi n y} y^{Re r} dy  <<  |l|^{eps} * (4 pi |l|)^{-Re r - 3/2 + eps},

and summing over `l in 18188 Z` converges for `Re r > -1/2 + eps`. Convergence at `y -> 0` (where `K_nu(y) ~ y^{-|Re nu|}` and
`W ~ y^{1/2 - mu}`) holds for `Re r` beyond an explicit finite bound. **The interchange is valid in a non-empty right
half-plane.** This is standard and I regard it as settled.

## 2. Task 2 — the Mellin integrals and the Dirichlet series identified

Each term is

    int_0^infty y^{r} (|l| y)^{1/2} K_nu(2 pi |l| y) W_{kappa,mu}(4 pi |n-l| y) e^{-2 pi n y} dy,

a classical Bessel-times-Whittaker Mellin integral (Gradshteyn-Ryzhik 6.6/7.6 class) evaluating to a `2F1`/Meijer-G value in
the ratio `|l| / n`. So the shifted term is

    sum_{l != 0, 18188 | l}  c_A(l;x) * c_{E~}(n-l;x) * G_r(l/n),

with `c_A(l;x)` the level-restricted divisor-type sum coming from `Z_{infinity,infinity}(l, 1-x/2) = sum_{N|c} r_c(l) c^{-2+x}`
and `c_{E~}(m;x) = N^{x/2} |m|^{-x/2-1} sigma^{(N)}_{1+x}(m)` (times `theta_2(-x/2)` and the Whittaker normalization). That is
a **sparse shifted convolution of divisor sums with a hypergeometric archimedean weight** — an Estermann-type object,
identified exactly.

## 3. Task 3 — the gate, and why the return is what it is

The needed continuation to `r = 0` is precisely the continuation of a shifted divisor-sum Dirichlet series. The relevant
existing machinery is the one Diamantis himself invoked for exactly this step at level 1: Kıral's continuation of
`D_l(alpha,beta;s) = sum_{n>l} sigma_alpha(n) sigma_beta(n-l) n^{-s}`, and the Estermann-zeta / Motohashi spectral route.
Three extensions are required, and they are not equal in weight:

1. `sigma^{(N)}` in place of `sigma` — a finite linear combination over divisors of `N`. **Bookkeeping.**
2. The progression constraint `18188 | l` — substitute `l = 18188 l'` and absorb. **Bookkeeping.**
3. The archimedean weight `G_r(l/n)` is a Bessel-Whittaker `2F1` arising from **weight 2** at level `N`, not the weight
   occurring in the cited results. The archimedean weight is what decides which spectral expansion applies and where the
   continuation's poles sit. **This is a genuine extension, not bookkeeping.**

Because (3) is not covered by a theorem I can point to, and because inventing it is exactly what the instruction asked me to
avoid, the return is `RS2_L3_REQUIRES_NEW_GENERAL_THEOREM`. Stated honestly: what is needed is a **weight-2, level-N,
progression-restricted extension of Kıral-type shifted-divisor continuation** — a publishable lemma, not a new general theory,
and nothing found suggests it is false.

## 4. Task 4 — not the gate; it is Petersson's formula

Your Poincaré redirection is vindicated here. Once Task 3 holds, Task 4 needs no regularized-projection theorem at all:

* `P_n(z,r)` at `r = 0` for `n >= 1` is the classical Hecke-continued weight-2 Poincaré series, which is a **cusp form**
  (the weight-2 anomaly is at `n = 0`, the Eisenstein case);
* `<A~_2, P_n>` converges absolutely because `P_n` decays exponentially, regardless of `A~_2`'s `y log^3 y` growth;
* `P_n` being cuspidal, `<A~_2, P_n> = <pi_cusp A~_2, P_n>`, and Petersson's formula turns that into the `n`-th Fourier
  coefficient of `pi_cusp A~_2` times `Gamma(1)/(4 pi n)`.

So the `y log^m y` issue is confirmed to be a non-issue in this formulation, and the finite part at `r = 0` is simply the
continued value. **Task 4 is settled modulo Task 3.**

## 5. Task 5 — the coefficient class, stated exactly

This can be stated without Tasks 1-4 closing, because the class is fixed by the construction:

    c_n( pi_cusp A~_2 )  =  (explicit constant in Q(pi))
        x [ l = 0 term:  x^2-coefficient of  a_A(0;x) * sigma^{(N)}_{1+x}(n) * (Gamma, zeta, y^a log^b y data) ]
        + [ shifted term: x^2-coefficient of  sum_{l != 0, 18188 | l} c_A(l;x) c_{E~}(n-l;x) G_r(l/n) ].

Exhaustively, the ingredients are: `sigma^{(N)}` divisor sums and their `x`-derivatives (= log-weighted divisor sums);
`zeta` and `Gamma` values and derivatives at explicit points; `K`-Bessel and Whittaker values and their parameter
derivatives; and sparse shifted convolutions of divisor sums with hypergeometric weights — i.e. **Estermann / shifted-divisor
special values**.

**Nothing in that list touches the Neron-Tate regulator, Heegner points, a height pairing, a Beilinson regulator, or any
characteristic-zero BSD quotient.** No independently identified arithmetic structure appears.

## 6. Hard stopping rule: fired

The rule was: if the outcome yields only shifted-convolution / Estermann / Bessel special values with no independently
identified arithmetic structure touching the Neron-Tate regulator or the characteristic-zero BSD quotient, **archive RS2 and
do not start an arithmeticity successor**. §5 answers that question affirmatively and does so independently of whether Task 3
is ever closed. Closing Task 3 would produce a correct, explicit, L-free formula for an object whose coefficient class is
already known to be the same class the very first source audit identified as the terminal unknown.

    RS2 = ARCHIVED.

No arithmeticity successor is started. No master rewrite. Endpoint effect **NONE**, as it has been throughout.

## 7. What the RS2 thread actually produced (for the record)

Positive and durable:
* the original "Laurent coefficient has no motivic meaning" rejection refuted, not merely doubted;
* an exact cross-cusp kernel whose `f`-pairing is `kappa~_N L(f,2) L''(f,1)` with `kappa~_N != 0` explicit, sign resolved;
* the bad-Euler normalization `D_N` that removes five spurious poles identically and eliminates the `prod log p` artefact;
* two exact local facts about this seed: the diagonal cusps `{infinity, 0}` are annihilated by `p^2 | N`, and the surviving
  shifted convolution is sparse with modulus `18188`.

Negative and equally durable: the terminal object is an Estermann-class special value, the same wall reached in the very first
audit from the Jorgenson-O'Sullivan and Diamantis directions. The route was run to the end and did not escape it.

---

Sources across the thread: Diamantis-O'Sullivan ANT 7 (2013) 1883-1917 and arXiv:0904.2179 (both full text); Diamantis
arXiv:1611.06899 (full); Raum-Xia, Res. Number Theory 6 (2020) 32 (full); Kontsevich-Zagier *Periods* §7; Sreekantan
arXiv:0909.0714; Jorgenson-O'Sullivan. **Cited, never obtained:** Iwaniec *Spectral Methods* (3.21)-(3.22); Kıral, *Shifted
Divisor Sum Dirichlet Series*. Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim.
