# RS2 CROSS-CUSP A_2 PROJECTION GATE — final output

Date 2026-09-20. Object:

    P(w; z) = (y^{-1} / 2 pi) * E*_{0,infinity}(z, 1 - (w-1)/2) * E*_{2,0}(z, -(w-1)/2)   for Gamma_0(N),
    P(w; z) = sum_{j >= -1} A_j(z) (w-1)^j,      x := w - 1.

No new candidates, no L2 arithmetic survey, no seed computation (no a_p evaluated).

## RETURN: `RS2_A2_OPEN_AT_EXACT_LEMMA`

**First unsupported equation (task order):** the level-N, cross-cusp analogue of Diamantis-O'Sullivan 2010 eq. (2.10),

    < f , y^{-k/2} E*_{k_1,a}(., 1-u) E*_{k_2,b}(., 1-v) >  =  (explicit constant) * L(f (x) E_b(.,v), w),

with the constant derived rather than transplanted. It is unsupported because the normalization of the cross-cusp
Fourier coefficient `Y_{ba}(l,s)` — Iwaniec, *Spectral Methods*, (3.21)-(3.22), cited but **not read in this run** — is the
one factor that cannot be recovered from the level-1 chain. Everything else in Task A is now in hand (see §1).

**First *substantive* unsupported equation (the one that actually matters):** `H_2 := pi^{reg}_{cusp}(A_2)` is defined and
satisfies `<H_2,g> = <A_2,g>_{reg}` for all `g in S_2(Gamma_0(N))`. §3 shows `A_2` has constant term `O(y log^3 y)` at the
cusp infinity, so the hypotheses of every classical weight-2 holomorphic-projection theorem **fail as stated**.

---

## 0. The three corrections, applied

1. **Naming.** The object is `P_{infinity,0}(w)`, not "the general-level double Eisenstein series". ANT Theorem 10.1 identifies
   the **diagonal** (a = b) product with `E*_{s,k-s,a}(z,w)`; for `a != b` the paper supplies only the **pairing formula** in
   the proof. Used accordingly throughout.
2. **Normalization debt.** Recorded as `CROSS_CUSP_NONZERO_FACTORIZATION = PROVED`,
   `EXACT_COMPLETED_CONSTANT = OPEN_SMALL`. §1 reduces the debt to one named factor but does not clear it.
3. **"Closes the loop" withdrawn as stated.** §2 confirms your algebra: the `x^2` coefficient is
   `R_{-1}B_3 + R_0B_2 + R_1B_1 + R_2B_0`, so a **third** Taylor coefficient of the weight-2 factor enters. `A_2` is related
   to the old `E^(2)` tower but is not that object with a cusp label changed.

## 1. Task A — the normalization chain, and the one factor still missing

The chain is now explicit and I have both primary sources in full.

**Diamantis-O'Sullivan 2010 (arXiv:0904.2179), level 1, `k_1, k_2` even `>= 0`, `k = k_1 + k_2`, all `s, w` in C:**

    Prop 2.1 (2.7):   2 * pi^{k/2} L*(f,s) L*(f,w) = (-1)^{k_2/2} < f, y^{-k/2} E*_{k_1}(., ubar) E*_{k_2}(., vbar) >
    (2.8)/(2.10):     < f, y^{-k/2} E*_{k_1} E*_{k_2} > = (-1)^{k_2/2} zeta(2u) Gamma(s) Gamma(w)
                                                          / ( 2^{k-2+2u} pi^{k/2-1+2u} ) * L(f (x) E(.,v), w)
    (2.11):           L(f (x) E(.,v), w) := sum_n a_f(n) sigma_{2v-1}(n) n^{-w} = L(f,s) L(f,w) / zeta(2u)
                      -- proved "by comparing Euler products".

**Lemma 2.2 (DO'S 2010), newly relevant:** for `k_1 >= 0`, `k_2 - 2 >= 0`,

    < f, y^{-k/2} E*_{k_1}(., ubar) E*_{k_2}(., vbar) > = - < f, y^{-k/2} E*_{k_1+2}(., ubar) E*_{k_2-2}(., vbar) >,

proved with the Maass raising/lowering operators. At `k = 2` this applies to exactly our split `(k_1,k_2) = (0,2)` and gives
`<f, y^{-1}E*_0 E*_2> = -<f, y^{-1}E*_2 E*_0>`. **So the choice of which factor carries the weight is not a real degree of
freedom**, and (2.9) reduces every split to `E*_k(., ubar) E*_0(., vbar)`. This is useful and it is also a warning: the
raising/lowering argument is a level-1 computation that must be redone for two *different* cusps before it can be used here.

**What transfers to level N, cross cusp.** (2.11) is the Euler-product step; its cross-cusp analogue is the depleted Rankin
factorization already established: `sum_n a_n(f) sigma^{(N)}_alpha(n) n^{-beta} = L(f,beta) L^{(N)}(f,beta-alpha) /
zeta^{(N)}(2 beta - alpha - k + 1)`, with local factors 1 at `p = 2, 4547` and `(1 - a_p p^{-beta})^{-1}` at
`p = 3, 2243, 5843`. That part is genuinely proved and is unaffected by the normalization debt.

**What does not transfer.** (2.10)'s constant comes from unfolding a *level-1, single-cusp* Eisenstein series. The level-N
cross-cusp unfolding is the one in the proof of ANT Thm 10.1, whose arithmetic input is `Y_{ba}(n, 1-v)` — defined in ANT (4-2)
but with its explicit shape deferred to **Iwaniec (3.21)-(3.22)**, which I did not obtain. The Ramanujan-sum content of that
coefficient is what I computed in the previous run; its **normalizing Gamma- and pi-powers** are not recoverable from the
level-1 chain, because at level 1 the cusp is unique and the cross-cusp normalization never appears.

Consequence, stated plainly: `kappa_N` cannot be produced honestly in this run, and I did not manufacture it by matching
level 1, per instruction.

**One further level-N precision point, not previously flagged.** ANT (2-7) `E*_k(z,s) = E*_k(z,1-s)` holds **at level 1 only**.
At level N the functional equation is (4-4), `E*_{k,a}(z,1-s) = sum_b Y_{ab}(1-s) E*_{k,b}(z,s)` — it **mixes cusps through the
scattering matrix**. DO'S 2010 uses arguments `(u,v)`; ANT §10 uses `(1-u, 1-v)`. At level 1 these agree by (2-7); at level N
they differ by the scattering matrix. Any end-to-end derivation must fix one convention and carry `Y_ab` through. This is a
second, independent reason the constant is not transplantable.

## 2. Task B — the four contributions, computed

With `x = w - 1`, `u = x/2`, `v = (w+1)/2`, so the two Eisenstein arguments are `1 - u = 1 - x/2` and `1 - v = -x/2`.

**Factor 1, the pole.** `theta(s) = pi^{-s} Gamma(s) zeta(2s)`, so `theta(1) = pi^{-1} * 1 * pi^2/6 = pi/6`. At level 1
`Res_{s=1} E(z,s) = 3/pi` (= 1/vol), hence `E*_0(z,s) ~ (pi/6)(3/pi)/(s-1) = (1/2)/(s-1)`. Since `s - 1 = -x/2`,

    **R_{-1} = -1**   (level 1; at level N, `R_{-1} = -1/[SL_2(Z) : Gamma_0(N)]`, still explicit and non-zero).

**Factor 2, the constant term.** `theta_2(s) = pi^{-s} Gamma(s+1) zeta(2s)`, so

    **theta_2(0) = pi^0 * Gamma(1) * zeta(0) = -1/2 != 0**,

and by (2-7) `E*_2(z,0) = E*_2(z,1)`, the Hecke-trick point: in this normalization `y^{-1}E_2(z,1) = sum (cz+d)^{-2}`, the
conditionally convergent weight-2 Eisenstein series, whose continuation is the non-holomorphic `E_2 - 3/(pi y)`. So

    **B_0 != 0**,

*provided* `E_2(z,s)` is regular at `s = 0` (equivalently, by the functional equation, at `s = 1`) — i.e. provided the residue
of the weight-k Eisenstein series at `s = 1` vanishes for `k != 0`. That is standard but it is **load-bearing** here: it is
what makes the pole of `P` simple rather than double. Flagged as an assumption to verify, not proved in this run.

**The x^2 coefficient.** Your algebra is confirmed exactly:

    **A_2 = (1/2 pi) y^{-1} [ R_{-1} B_3 + R_0 B_2 + R_1 B_1 + R_2 B_0 ].**

**Does anything kill or combine terms?** Checked, and **no**:
* `(2-7)` applied to factor 1 gives `E*_0(z, 1-x/2) = E*_0(z, x/2)`, and applied to factor 2 gives
  `E*_2(z,-x/2) = E*_2(z, 1+x/2)`. Both relate an expansion at one point to an expansion at *another* point (`t <-> 1-t`);
  neither is a parity statement at the expansion point, so neither annihilates any `R_j` or `B_j`.
* No special-value identity was found that combines them; `theta_2(0) = -1/2` and `theta(1) = pi/6` are both finite and
  non-zero, so no term degenerates.
* At level N, `(2-7)` is unavailable at a single cusp (see §1), so even these relations must be replaced by (4-4).

So all four terms survive, and in particular **`B_3`, a third derivative in the spectral parameter of the weight-2 Eisenstein
series at cusp 0, is genuinely present.** Your point stands: `A_2` is a new object, not the RS2 second jet relabelled.

## 3. Task C — growth at the cusps, and why this is the real gate

From ANT (4-3): `E*_{k,a}(sigma_b z, s) = delta_{ab} theta_k(s) y^s + theta_k(1-s) Y_{ab}(s) y^{1-s} + O(e^{-2 pi y})`.

At the cusp **infinity** (`b = infinity`):
* Factor 1 has `a = b`, so it carries **both** `theta(1-x/2) y^{1-x/2}` and `theta(x/2) Y_{infinity,infinity}(1-x/2) y^{x/2}`.
  Expanding `y^{1-x/2} = y * exp(-(x/2) log y)`, the `x^j` coefficient carries `y log^j y`; the second term carries `log^j y`;
  and `theta(x/2)` supplies the pole (`Gamma(x/2) ~ 2/x`), which is the analytic source of `R_{-1}`.
* Factor 2 has `a = 0 != infinity = b`, so `delta_{ab} = 0` and it carries **only**
  `theta_2(1+x/2) Y_{0,infinity}(-x/2) y^{1+x/2}`, whose `x^j` coefficient carries `y log^j y`.

Multiplying and dividing by `y`, the constant term of `A_2` at the cusp infinity is

    **O( y log^3 y ).**

Classical weight-2 holomorphic projection (Sturm; the Gross-Zagier IV.5 form) requires the input to **decay**, `O(y^{-epsilon})`,
at every cusp. `A_2` does the opposite. The published regularized versions in the weight-2 / shifted-convolution literature
extend this to inputs whose growth is an explicit finite sum of terms `y^alpha`; **growth of the form `y log^m y` with `m` up to
3 is outside what I was able to confirm any published theorem covers.** I did not obtain and read such a theorem in this run,
so I will not assert either that it exists or that it does not.

Two facts make this look like a technical lemma rather than an obstruction, and both should be stated as expectations, not
results: (i) all of the offending growth sits in the **explicitly known** constant terms above, with coefficients
`theta`, `theta_2`, `Y_{ab}` that are available in closed form, so the natural move is to subtract an explicit weight-2
Eisenstein-type combination; (ii) any such subtraction has **zero cuspidal projection**, so by the correction accepted in the
previous run (only `e_f Pi_cusp` is ever needed) it cannot disturb the f-coordinate.

**Cusp-by-cusp status: not done.** `Gamma_0(N)` with this non-squarefree `N` has `sum_{d|N} phi(gcd(d, N/d))` cusps; the growth
above was computed only at infinity. The remaining cusps need `Y_{ab}` for all `b`, i.e. the same Iwaniec input missing in §1.

## 4. Task D — not reached, with the structural expectation recorded

Not attempted, since it is contingent on Task C. What can be said without hand-waving: the Fourier coefficients of a **product**
of two Eisenstein series are **convolutions** of their coefficients, and each factor's coefficients are of divisor /
Kloosterman-zeta type (`sigma`-sums for the weight-0 factor at infinity; `Y_{0,infinity}(l,s)` for the weight-2 factor at
cusp 0). Laurent-expanding in `x` and applying the projection integral against `e^{2 pi i n z}` therefore produces **shifted
convolutions** of such coefficients against explicit archimedean integrals. That is the arithmetic class one should expect for
`a_n(H_2)` — and it would be reached **constructively**, not by analogy, which is the whole point of the requirement that the
formula must not define `H_2` spectrally. But it is an expectation, not a derivation, and no formula for `a_n(H_2)` is claimed.

## 5. Status to record

    CROSS_CUSP_NONZERO_FACTORIZATION      = PROVED          (previous run; unaffected)
    EXACT_COMPLETED_CONSTANT (kappa_N)    = OPEN_SMALL      (reduced here to one named missing input: Iwaniec (3.21)-(3.22))
    A_2 FOUR-TERM STRUCTURE               = PROVED          (this run; R_{-1} = -1, theta_2(0) = -1/2, no term killed)
    E_k(z,s) REGULAR AT s=1 FOR k != 0    = ASSUMED         (load-bearing for B_0 finite and for the pole being simple)
    WEIGHT-2 REG. PROJECTION AT y log^3 y = OPEN, THE REAL GATE
    a_n(H_2) EXPLICIT                     = NOT REACHED

Endpoint effect: **NONE**, unchanged. This is a strict reduction inside RS2, not movement toward FORMULA. A seed-level proof
run remains unwarranted: every open item above is a general statement about `Gamma_0(N)` and none is seed-specific.

---

Primary sources read in full: Diamantis-O'Sullivan, ANT 7 (2013) 1883-1917; Diamantis-O'Sullivan, arXiv:0904.2179
(= Math. Ann. 346 (2010) 897-929) — Prop. 2.1, (2.7), (2.8), Lemma 2.2, (2.9), (2.10), (2.11). **Cited but not obtained:**
Iwaniec, *Spectral Methods of Automorphic Forms*, (3.21)-(3.22); and any published weight-2 regularized holomorphic-projection
theorem covering `y log^m y` growth. Derived here: the four-term structure, `R_{-1}`, `theta_2(0)`, the absence of any killing
identity, and the `O(y log^3 y)` growth. Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim.
