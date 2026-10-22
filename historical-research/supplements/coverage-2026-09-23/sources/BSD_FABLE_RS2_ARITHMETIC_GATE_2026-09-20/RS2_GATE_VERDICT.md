# RS2 ARITHMETIC GATE — final output

Date 2026-09-20. Narrow run: RS2 arithmetic gate only. No candidate generated. Master not updated (no new theorem proved).
Inputs: `~/BSD_FABLE_CANDIDATE_ENGINEERING_2026-09-20/reopen/REOPEN_VERDICTS.md` §1 (sealed, unedited) and the full body of
Diamantis, arXiv:1611.06899 = Proc. AMS 148 (2020) 5059-5070. Working notes: `20_DIAMANTIS_FULL_READ.md`,
`21_EXACT_COMPARISON.md`.

## RETURN: `RS2_DIAMANTIS_MISMATCH`

Task C (the level-389 experiment) was **not run**, per the instruction that it is contingent on Task B remaining open.

---

## 1. Exact definition of c_f

f = the weight-2 rational newform of E, level N = 2^3 * 3 * 2243 * 4547^2 * 5843. Q(f) = Q, so the Hecke projector e_f onto
the f-line is an idempotent of T tensor Q defined over Q.

    h := Pi_hol( g E^(2) ) in S_2(Gamma_0(N)),        e_f h = c_f f,

    c_f = <f,h> / <f,f> = 3 L(f,2) L''(f,1) / ( 16 pi^4 <f,f> )  =  a_1( e_f h ).

Adopted corrections to the previous record (both stand):

* The §8 equivalence in `reopen/16_RS2_VERDICT.md` — "h has algebraic Fourier coefficients <=> L(f,2)L''(f,1)/(pi^4<f,f>) is
  algebraic" — is **withdrawn**: the right-hand side controls only the f-isotypic coordinate. The gate is about c_f = a_1(e_f h),
  not about h. (The sealed file is not edited; `21_EXACT_COMPARISON.md` §B.0 records the supersession.)
* The weight-2 Sturm bound at level 389 is **65** (389 prime, index 390), not ~20; and failure of decimal recognition would not
  prove irrationality.

## 2. What the published theorem actually proves about c_f

**Nothing.** Three separate reasons, each independently sufficient, stated as the exact hypothesis or equation that blocks it:

* **(E1) — the first blocking equation.** Thm 2.1's kernel E*_{s,k-s}(z,w) is defined by absolute convergence on
  `2 < Re(s) < k - 2`. At our weight k = 2 that reads `2 < Re(s) < 0`: **empty**. Non-empty only for even k >= 6. There is
  nothing to continue analytically from at weight 2.
* **(E2)** Every statement in the paper is for a normalised cuspidal eigenform of weight k **for SL_2(Z)**, and
  S_2(SL_2(Z)) = 0 — the hypothesis class is empty at our weight — while the seed's f has level N. The paper contains no
  Gamma_0(N) statement at all.
* **(E3)/(E4)** The arithmetic theorems are about **ratios of non-critical values** L*_f(k+r)/L*_f(k+r'), r,r' >= 1, with
  L*-values in denominators (Prop. 2.2 needs L*_f(s), L*_f(s_0) != 0; Prop. 2.3 needs L*_f(k/2) != 0). The seed has a **double
  zero** at the central point, and our arguments are s = k and w = k/2. Verified by grep over the full text: "derivative" and
  "Laurent" occur **zero** times; the paper treats values only.

**And the conclusion would not be algebraicity even if it applied.** Thm 1.1 returns membership in D_r D_{r'} Q(f), where D_m
is generated **over Q(pi, i)** by values D_l(alpha,beta;n) of shifted divisor-sum Dirichlet series — and Diamantis writes in §1
that determining the arithmetic nature of those values, so as to get information about quotients of L-values, "would be
interesting", i.e. is open. No Deligne or Manin period is divided out.

**What the paper does give, and it is not nothing.** Thm 2.1 is an identity of functions holomorphic in (s,w) on all of C^2:
`<E*_{s,k-s}(.,w), f> = L*_f(s) L*_f(w)`. Differentiating twice in w at the central point is legitimate inside its hypothesis
class, and with H := d^2_w E*_{2,0}(.,w)|_{w=1} one gets, exactly (all cross terms vanish because L_f(1) = L'_f(1) = 0),

    <H, f> = L*_f(2) (L*_f)''(1) = L_f(2) L''_f(1) / (8 pi^3),      hence   c_f = (3 / 2 pi) * a_1(e_f H).

So **c_f is, up to a factor in Q(pi), the f-coordinate of the second central w-derivative of an independently published
two-variable cusp-form kernel**, and Diamantis eq. (8) independently identifies that kernel as a holomorphic projection of a
product of Eisenstein series — the same architecture as Pi_hol(g E^(2)). The RS2 object is confirmed to be a natural object
that the literature has reached from another direction. It is a **structural** confirmation, not an arithmetic one.

## 3. First remaining open arrow

One lemma, and it is not the level-N construction:

> **(L2)** Determine the arithmetic nature of the special values of shifted divisor-sum Dirichlet series
> `D_l(alpha, beta; nu) = sum_{n > l} sigma_alpha(n) sigma_beta(n - l) n^{-nu}` (equivalently the Estermann-zeta special values,
> equivalently Jorgenson-O'Sullivan's `L_m^{+/-}(1)`) at the relevant integer arguments: are they algebraic, periods in the
> Kontsevich-Zagier sense, or provably not?

This is the gate for the whole RS2 family, because **both** independent routes terminate there: Diamantis's field D_m is
generated over Q(pi,i) by exactly these values, and JO'S's second-order Fourier coefficients are exactly these values. Until
(L2) is answered, constructing the level-N kernel would only re-express c_f in the same unknowns.

Prerequisite, needed to phrase (L2) at our weight and level but arithmetically empty by itself:

> **(L1)** Construct a two-variable family W(z; s, w) of cusp forms in S_2(Gamma_0(N)), holomorphic in (s,w) near (2,1), with
> `<W(.;s,w), f> = L*_f(s) L*_f(w)` for all newforms f — i.e. the weight-2, level-N analogue of Diamantis-O'Sullivan Thm 2.1,
> whose stated convergence region is empty at weight 2.

Scope caution that survives regardless: even `RS2_ARITHMETIC_GATE_PROVED` would give an arithmetic statement about
L(f,2)L''(f,1)/(pi^4 <f,f>), not about q = L''(E,1)/(2 Omega_E R) = 36. Reaching q additionally needs the Beilinson side for
L(f,2) and the <f,f> <-> Omega_E comparison. RS2 is a ratio-of-regulators route; that has not changed.

## 4. Should RS2 receive a serious seed-level proof run?

**No — and the reason is sharper than "not yet".**

1. The gate is not passed: no published theorem says anything about c_f.
2. In the one setting where the machinery exists (level 1, even k >= 6), its terminal output is a field generated by shifted
   divisor-sum values whose arithmetic the author explicitly leaves open. **A fully successful execution of this architecture
   returns the same unknown we already have.** That is the decisive point against spending now.
3. Both missing inputs (L1) and (L2) are general — a kernel construction and a theorem about Dirichlet-series special values.
   **Neither is seed-specific**, so the seed contributes nothing to either and would consume effort that buys no progress.
4. The level-389 experiment is likewise not the right spend: at level 1 weight 2 there are no cusp forms, so 389 cannot be
   compared against the published kernel, and a numerical recognition of c_f to 65 certified coefficients would at best produce
   a conjecture about the same D_l values that (L2) asks about directly.

**Recommended disposition:** RS2 stays an open mechanism with an exact object, not a proof route. The one bounded thing worth
doing, if anything in this direction is funded, is a literature decision on (L2) — Estermann-zeta / shifted-divisor special
values — which gates RS2 and the JO'S route simultaneously and is a self-contained question in analytic number theory. It is
**not** started here.

---

Nothing merged. No novelty claim. No FIN or FORMULA claim. `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19` untouched;
`~/BSD_FABLE_CANDIDATE_ENGINEERING_2026-09-20/` untouched (its `reopen/` manifest stays sealed and valid).
