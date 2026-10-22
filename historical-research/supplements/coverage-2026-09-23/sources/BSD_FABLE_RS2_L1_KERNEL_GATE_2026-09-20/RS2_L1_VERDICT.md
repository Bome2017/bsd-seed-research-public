# RS2 L1 KERNEL GATE — final output

Date 2026-09-20. Scope: existence of a weight-2, level-N analogue of the Diamantis-O'Sullivan two-variable product-L kernel.
No shifted-divisor arithmetic discussed. No seed-level run. Master not updated (no new theorem proved).

## RETURN: `RS2_L1_OPEN_WITH_EXACT_MISSING_LEMMA`

...but the gate as literally posed is **satisfiable trivially**, so the lemma has to be restated before it means anything.
That is the main finding of this run, and it is a correction to the task statement, not a result about the seed.

---

## 0. Correction carried in, and accepted

The passage in `../BSD_FABLE_RS2_ARITHMETIC_GATE_2026-09-20/RS2_GATE_VERDICT.md` §2 that set
`H := d_w^2 E*_{2,0}(.,w)|_{w=1}` and deduced `<H,f> = L(f,2)L''(f,1)/(8 pi^3)` **from Diamantis-O'Sullivan Theorem 2.1** is
**withdrawn**. The theorem assumes even k >= 6; k is not an analytically varying parameter; S_2(SL_2(Z)) = 0. One cannot set
k = 2 there and pair the result with a level-N weight-2 newform. Consequently the sentence "both independent routes terminate
at exactly L2" is **withdrawn**, and the dependency order is **L1 first, then possibly L2**.

Corroboration of the k >= 6 hypothesis from what was read here: Thm 2.1's own absolute-convergence region is
`2 < Re(s) < k - 2`, which is non-empty only for k > 4, i.e. (k even) k >= 6; the abstract of the ANT paper describes the
construction as a Rankin-Cohen bracket of two Eisenstein series at level 1; and the Hilbert-modular continuation of this line
(arXiv:2401.01282) requires even parallel weight >= 6 and never allows weight 2. **Gap: the ANT full text was not obtained**
(paywalled); the k >= 6 hypothesis is taken from the user's citation plus these three independent corroborations.

## 1. L1 as posed is trivially true, hence not the real gate

Posed target: `W_N(z;s,w) in S_2(Gamma_0(N))` near (s,w) = (2,1) with `<W_N(.;s,w), f> = C_N(s,w) L*_f(s) L*_f(w)`, C_N
explicit, regular and non-zero at (2,1).

`S_2^new(Gamma_0(N))` is **finite-dimensional**, and its newforms are pairwise orthogonal (multiplicity one). So define

    W_N(z; s, w)  :=  sum over the newform basis g of  [ L*_g(s) L*_g(w) / <g,g> ] * g(z).

This is a finite sum of entire functions of (s,w) with values in S_2^new(Gamma_0(N)); it satisfies
`<W_N(.;s,w), g> = L*_g(s) L*_g(w)` exactly, with `C_N == 1`, regular and non-zero everywhere; and `d_w^2 W_N(z;2,w)|_{w=1}`
is legitimate because the sum is finite. **L1 as written is proved in three lines.**

It is also **arithmetically vacuous**: the family is *defined* by the very L-values it is supposed to compute. Note the
consequence for the earlier record — the numerical identity `c_f = (3/2 pi) a_1(e_f H)` is *correct* if H is the spectral
object above, but then it is a tautology; what was wrong was attributing it to Diamantis-O'Sullivan Thm 2.1. Both halves of
that correction stand.

Indeed the follow-up literature (arXiv:2401.01282) *defines* the double Eisenstein series spectrally,
`E_{s,k-s}(.,w) := sum_{f in H_k} L(f,k-s) L(f,k-w)/<f,f> * f`. **The entire content of the Diamantis-O'Sullivan theorem is
that this spectral definition coincides with an independently constructed double Eisenstein series having a computable
q-expansion.** That coincidence, not the existence of the family, is what carries arithmetic information.

## 2. Restated lemma (L1')

> **(L1')** Construct `W_N(z;s,w) in S_2(Gamma_0(N))`, jointly holomorphic in (s,w) near (2,1), with
> `<W_N(.;s,w), f> = C_N(s,w) L*_f(s) L*_f(w)` for all newforms f, C_N explicit and non-zero/regular at (2,1), **such that the
> q-expansion of W_N is given in closed form by a construction independent of the L-values of S_2(Gamma_0(N))** — concretely,
> as an explicit, (s,w)-analytic combination of products of at most two Eisenstein-series cusp expansions.

Only (L1') licenses reading Fourier coefficients off the kernel, which is the only way the route can ever reach arithmetic.

## 3. Status of (L1'): OPEN, not obstructed. Exact findings.

**(A) The obstruction that would have killed it is gone.** Dickson-Neururer's weight-2 theorem, as formulated in Raum-Xia
eq. (1.1), is

    span_C { f in S_2^new(Gamma_0(N)) : L(f,1) != 0 }  subset  E_2(N)_inf + E_1(N)_inf * E_1(N)_inf ,

valid when N is a product of two prime powers and a squarefree integer. **The seed's level satisfies that level hypothesis
exactly** — N = 2^3 * 3 * 2243 * 4547^2 * 5843 = (2^3)(4547^2)(3 * 2243 * 5843), two prime powers times a squarefree integer —
**and fails its L-value hypothesis**, since the seed has a double zero at s = 1. The seed sits precisely in the gap.

Raum-Xia (Res. Number Theory 6 (2020) 32, Thm 1) closes it: for positive integers k, l, N there is N_0 with

    M_{k+l}(Gamma(N))  subset  E_{k+l}(N) + E_k(N_0) * E_l(N_0),                                  (1.2)

with **no condition on central L-values and no condition on N**; Remark (2) covers Gamma_0(N) and Gamma_1(N). Taking k = l = 1:
the seed's f **is** a linear combination of products of at most two Eisenstein-series cusp expansions. So there is no
"the target is unreachable from Eisenstein products" obstruction, and `RS2_L1_OBSTRUCTED` is **not** the correct return.

**(B) But Raum-Xia cannot be converted into (L1') as it stands.** Four exact reasons, from the paper:

1. **No spectral parameters.** (1.2) is a spanning statement about a fixed finite-dimensional space. It produces no family in
   (s,w) and therefore nothing to differentiate in w.
2. **Ineffective exactly at weight 2.** For k + l >= 3 the level N_0 is explicit (their Thm 4.4) and the Eisenstein term can be
   dropped (their Thm 5.2, eq. (1.3)). For **k + l = 2** neither holds: Remark (5) says an explicit bound for N_0 "could be
   obtained from an effective bound on gaps in the Fourier expansion of weight 3/2 modular forms" — i.e. it is currently
   **not effective** — and Remark (6) says the stronger (1.3) at k + l = 2 is supported only by computer experiment.
3. **Auxiliary level.** The decomposition lives at N_0 (and lcm(N_0, N N_1)), not at N; a kernel must be pushed back to level N.
4. **Cusp expansions, not level-N Eisenstein series.** E_k(N) means expansions at *all* cusps, with fractional exponents, as
   opposed to E_k(N)_inf. A q-expansion at infinity must be reassembled from them.

**(C) The naive series construction is unavailable at weight 2 at every level (derived here, level-independent).** In the
double series `sum_{gamma,delta} (c_{gamma delta^{-1}})^{w-1} (j(gamma,z)/j(delta,z))^{-s} j(delta,z)^{-k}` the two sums over
B\Gamma contribute `|j(gamma,z)|^{-Re(s)}` and `|j(delta,z)|^{Re(s)-k}`, and a sum of `|cz+d|^{-sigma}` over Gamma_inf\Gamma
converges iff sigma > 2 — a threshold that does **not** improve with level. Absolute convergence therefore needs
`Re(s) > 2` **and** `k - Re(s) > 2`, i.e. `k > 4`. At k = 2 the region is empty for **every** Gamma_0(N). So (L1') cannot be
obtained by transcribing (1) to level N; it requires a Hecke-type regularisation in an auxiliary variable (the device
Diamantis used in arXiv:1611.06899 (11) for a different convergence failure) whose continuation must then be shown regular at
(s,w) = (2,1). On top of that, weight-2 holomorphic projection carries its own anomaly (the quasimodularity of E_2), which
must be controlled rather than assumed.

## 4. The exact missing lemma

> **(L1'-missing)** An **effective, (s,w)-analytic** form of the Raum-Xia decomposition for the spectral kernel: exhibit
> explicit functions `c_j(s,w)`, holomorphic near (2,1), and Eisenstein cusp expansions `A_j, B_j` of weight 1 (plus a weight-2
> Eisenstein term) at an **explicitly bounded** level, such that `sum_j c_j(s,w) A_j B_j` lies in S_2(Gamma_0(N)) and pairs
> against every newform f to `C_N(s,w) L*_f(s) L*_f(w)` with C_N explicit, regular and non-zero at (2,1).

Its two identified sub-obstacles, both currently open: the **effectivity of N_0 at k + l = 2** (equivalently, an effective gap
bound for weight-3/2 Fourier expansions), and a **weight-2 regularisation** of the double Eisenstein series that is regular at
(2,1), with the weight-2 holomorphic-projection anomaly controlled.

## 5. Consequences for the route

* `RS2_L1_OBSTRUCTED` is **wrong**: the central-L-value obstruction that would have excluded the seed is removed by Raum-Xia,
  and the seed's level even satisfies Dickson-Neururer's level hypothesis.
* `RS2_L1_PROVED` is **wrong** in substance, although the literal statement is provable in three lines by the spectral
  definition. The task statement needs the independence clause of (L1').
* The seed-level proof run remains **not warranted**, unchanged: (L1') is a general construction problem about
  S_2(Gamma_0(N)) for arbitrary N and about weight-3/2 effectivity. It is not seed-specific, and the seed contributes nothing
  to it.
* L2 (shifted-divisor arithmetic) was **not discussed**, per instruction, and is now correctly downstream: until (L1') is
  proved, the Fourier-coefficient class of a weight-2 level-N kernel is unknown, and a weight-2 positive-level regularisation
  may well produce local correction terms, cusp terms, oldform projections, or different shifted convolutions than the level-1
  theory does.

---

Sources actually read in this run: Raum-Xia, *All modular forms of weight 2 can be expressed by Eisenstein series*,
Res. Number Theory 6 (2020) 32 (full text, `source_raum_xia_2020.txt`, 972 lines, via research.chalmers.se); Diamantis,
arXiv:1611.06899v1 (full text, read in the previous run); arXiv:2401.01282v1 (introduction and theorem hypotheses, via fetch);
msp.org abstract page for ANT 7 (2013) 1883-1917. **Not obtained:** the ANT full text, and Dickson-Neururer in the original —
its weight-2 statement is quoted here as formulated by Raum-Xia, eq. (1.1). Nothing merged. No novelty claim.
