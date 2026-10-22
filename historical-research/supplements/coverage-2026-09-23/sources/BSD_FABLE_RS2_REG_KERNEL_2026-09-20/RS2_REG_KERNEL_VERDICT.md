# RS2 DIRECT REGULARIZED-KERNEL GATE — final output

Date 2026-09-20. Scope: cuspidal finite-part kernel problem only. Raum-Xia effectivity not continued. L2 arithmetic not
discussed. Master not updated. No seed arithmetic launched.

## RETURN: `RS2_REGULARIZED_L1_OBSTRUCTED`

**The obstruction is an exact local computation at the seed's level, it sits in the arithmetic (c-sum) factor, and the
auxiliary regularization parameter u cannot reach it.** Tasks 2-4 are therefore not entered: Task 1 already fails, and it fails
before any continuation question arises.

---

## 0. Corrections carried in, and accepted

* Effective N_0 is a Raum-Xia implementation obstacle, **not** the intrinsic gate; dropped from the lemma. Not used below.
* Weight-2 regularized holomorphic projection is established technology; the question is identifying and removing quasimodular
  and polar corrections. Accepted — and it turns out not to be reached.
* The earlier "naive series needs k > 4" computation refutes only **absolute convergence of the naive representation**; it does
  not obstruct meromorphic continuation or a Hecke-trick finite part. Accepted, and **superseded**: §10 of the ANT paper gives
  the continuation unconditionally (Cor. 10.2), so that earlier point is now irrelevant rather than merely too strong.
* The ANT paper is publicly readable at msp.org. **Obtained and read in full** (2090 extracted lines,
  `source_diamantis_osullivan_ANT_2013.txt`). Theorem 2.3's hypothesis "**k >= 6 even**" is now confirmed from the primary
  source, not from corroborations.

## 1. What the source actually provides at general level (this replaces the guesswork)

The construction already exists for arbitrary Fuchsian groups of the first kind, and the paper's §10 is exactly the
level-N question:

* **Prop. 4.2** states convergence for a general group Gamma with cusp a, with the same constraints `2 < sigma < k-2`.
* **Theorem 10.1** proves, for even k_1, k_2 >= 0 with k = k_1 + k_2,

      E*_{s,k-s,a}(z,w) = 2^{eps_0 - 1} * pi_hol[ (-1)^{k_2/2} y^{-k/2} E*_{k_1,a}(., 1-u) E*_{k_2,a}(., 1-v) / (2 pi^{k/2}) ]

  i.e. the double Eisenstein series **is** the holomorphic projection of a product of two completed real-analytic Eisenstein
  series at the cusp a with spectral parameters 1-u, 1-v.
* **Corollary 10.2** gives meromorphic continuation of E*_{s,k-s,a}(z,w) to all s,w in C, with values in S_k(Gamma), **for an
  arbitrary Fuchsian group of the first kind**, using only Selberg's continuation of E*_{k,a}(z,s). No Hecke operators.

So the object the gate asks for is not missing at level N. What has to be checked is the **pairing**, and the proof of
Thm 10.1 hands it over explicitly:

      < E*_{s,k-s,a}(.,w), g >
          = 2^{eps_0 - 1} * zeta(2-2u) Gamma(k-s) Gamma(k-w) / (2 pi)^{2k-s-w}
            * sum_{n>=1} Y_aa(n, 1-v) a_{g,a}(n) / n^{k-s-v}                                    ... (P)

where a_{g,a}(n) are the Fourier coefficients of g at the cusp a and Y_aa is the Kloosterman-type zeta function defined by

      sum_{gamma in Gamma_inf \ Gamma_a / Gamma_inf, c_gamma > 0}  e^{2 pi i n d_gamma / c_gamma} / c_gamma^{2s}
          = Y_aa(n,s) / ( zeta(2s) n^{s-1} ).                                                    ... (K)

**At level 1 this c-sum is `sum_{c>=1} r_c(n) c^{-2s} = sigma_{1-2s}(n)/zeta(2s)`, a divisor function, and Rankin's identity
then turns (P) into `L*(f,s) L*(f,w)`.** That divisor structure is the entire source of the product-of-two-L-values shape.
It is a level-1 accident, not a general fact.

## 2. Task 1, executed: the local factor at the seed's level is identically zero at the cusp infinity

For Gamma_0(N) at a = infinity we have Gamma_a = Gamma_0(N), and Gamma_inf \ Gamma_0(N) / Gamma_inf is parametrised by
c > 0 with **N | c** and d mod c with gcd(d,c) = 1. So the c-sum in (K) is

      Z_N(n,s) = sum_{c > 0, N | c} r_c(n) c^{-2s},        r_c(n) = Ramanujan sum.

**Lemma (exact).** If p^2 | c and p does not divide n, then r_c(n) = 0.
*Proof.* r is multiplicative in c; write c = p^j m with j >= 2, gcd(p,m) = 1. For j >= 1, r_{p^j}(n) = phi(p^j) if p^j | n,
= -p^{j-1} if v_p(n) = j-1, and = 0 if v_p(n) <= j-2. Here v_p(n) = 0 <= j-2, so r_{p^j}(n) = 0, hence r_c(n) = 0. []
(Checked numerically over p in {2,3,5,7}, 2 <= j <= 4, several m and all n < 40 coprime to p: **0 counterexamples**.)

The seed has **N = 2^3 * 3 * 2243 * 4547^2 * 5843**, so p^2 | N for p = 4547 and for p = 2. Every c occurring in Z_N is
divisible by N, hence by p^2. Therefore

      Z_N(n,s) = 0   for every n with p not dividing n.                                          ... (Z)

On the other side, f is a newform of level N and p^2 | N, so **a_p(f) = 0**, hence a_{p^j}(f) = a_p(f)^j = 0 for all j >= 1,
hence

      a_n(f) = 0   for every n divisible by p.                                                   ... (A)

(Z) and (A) have complementary support. Therefore **every term of the Dirichlet series in (P) vanishes**, and

      < E*_{s,2-s,infinity}(.,w), f >  ==  0   identically in (s,w),

while L*(f,s) L*(f,w) is not identically zero. The only C_N(s,w) compatible with (P) is **C_N == 0**. The requirement
"C_N explicit and non-zero/regular at (2,1)" fails in the strongest possible way — not a zero at a point, but the zero function.

Two independent primes force this for the seed: p = 4547 (exponent 2) and p = 2 (exponent 3). Either alone suffices.

**Cusp 0 gives nothing new.** The Fricke involution W_N normalises Gamma_0(N), so for a = 0 the conjugated group
sigma_a^{-1} Gamma_0(N) sigma_a is again Gamma_0(N); the c-sum is again Z_N, and a_{f,0}(n) = +/- a_f(n) by the Fricke
eigenvalue. The same vanishing holds.

## 3. Why the regularization parameter u cannot repair this

This is the decisive point for the gate as posed. In the proof of Thm 10.1 the unfolding separates cleanly into

      (archimedean integral)  x  (arithmetic c-sum)  x  (Fourier coefficients a_{g,a}(n)),

with the archimedean factor `I_k(s) = int int y^{k-2} e^{-2 pi i x - 2 pi y} (x + i y)^{-s} dx dy` evaluated by Laplace's
formula. Inserting a Hecke-type parameter — `Im(gamma z)^u`, `Im(delta z)^u`, or a global `y^u` — changes the integrand only
through the power of y, i.e. it replaces `I_k(s)` by `I_k(s;u)`. **It does not touch the c-sum (K).** The vanishing (Z) is a
statement about the c-sum alone. Hence for every u in the region of absolute convergence the pairing is still identically
zero, and so is every coefficient of its Laurent expansion at u = 0 — including the finite part.

Consequently the Task 2/Task 3 programme cannot be reached: it is not that some polar term `A_{-j}` survives in the cusp
space, it is that `Pi_cusp A_j = 0` for **every** j, finite part included, so `W_N^reg` is the zero cusp form and the
identity of Task 3 degenerates to 0 = 0. The rank-two double zero cannot rescue anything, because there is no non-zero
C_{N,f} for it to act on.

For completeness, the convergence window is genuinely non-empty before continuation — inserting y^u gives exponents
`Re(s) + 2u > 2` and `k + 2u - Re(s) > 2`, i.e. `2 - 2u < Re(s) < 2u`, non-empty for u > 1/2 and containing s = 2 for u > 1.
So the obstruction is not a convergence artifact: the kernel exists, converges, continues (Cor. 10.2), and pairs to zero.

## 4. What is *not* claimed

* **Not** claimed: that no weight-2 level-N product-L kernel exists. Claimed: **this** construction, at the cusps infinity and
  0, pairs identically to zero against the seed's newform, and no auxiliary archimedean regularization can change that.
* **Not** claimed: that the other cusps are dead. Gamma_0(N) with N non-squarefree has many cusps
  (sum_{d|N} phi(gcd(d, N/d))), and for a general cusp a the conjugate sigma_a^{-1} Gamma_0(N) sigma_a is not Gamma_0(N); the
  allowed moduli change and Y_aa is a genuine Kloosterman zeta. Two things must then be faced at once, and they pull against
  each other:
  1. Y_aa(n,s) is **not** a divisor function at a general cusp, and the Rankin factorisation that produces
     `L*(f,s) L*(f,w)` in (P) is a level-1 accident of the divisor structure. Without it the pairing is some
     Kloosterman-weighted Dirichlet series, not a product of two L-values — so the required *shape* fails even where the
     value does not vanish.
  2. The coefficients a_{f,a}(n) at those cusps are exactly the expansions that are hard to compute at non-squarefree level —
     which is the problem Raum-Xia's machinery addresses. The surviving cusps are precisely the inaccessible ones.

## 5. Consequences for the route

* The RS2 route via the Diamantis-O'Sullivan architecture is **blocked for this curve at the accessible cusps**, by a local
  computation that takes three lines and is immune to the regularization the gate was built around.
* The block is **specific to the seed's level structure** — it needs p^2 | N, which is what simultaneously forces a_p = 0 and
  kills the Ramanujan sums. A newform of squarefree level would not be obstructed this way. This is a genuine
  arithmetic obstruction attached to the seed, not a generic no-go.
* Seed-level proof run: **still not warranted**, now for a stronger reason than before — the natural construction is not merely
  unproven at weight 2, it provably returns zero for this N at the cusps one can actually compute with.
* The only surviving direction inside this architecture is the non-Fricke cusps, and it requires *both* a substitute for
  Rankin's identity at a general cusp *and* the cusp expansions of f at non-squarefree level. That is strictly harder than the
  gate just attempted, and it is not recommended.

---

Sources read in full in this run: Diamantis-O'Sullivan, *Kernels for products of L-functions*, ANT 7 (2013) 1883-1917
(msp.org, 2090 extracted lines) — Def. 2.2, (2-10), (2-12), Thm 2.3 (k >= 6 even), Thm 2.7, Def. 2.8, Thm 2.9, Def. 3.1,
Def. 3.2 with (3-3), Prop. 4.2, Prop. 4.3, §5A, §10 (Thm 10.1, Cor. 10.2 and the proof's pairing formula). Previously read:
Diamantis arXiv:1611.06899v1 in full; Raum-Xia 2020 in full. **Not needed and not read in this run:** the weight-2 regularized
holomorphic-projection literature — the gate failed upstream of it, at the arithmetic factor.

Nothing merged. No novelty claim. No FIN/FORMULA/BSD claim. Master untouched; all predecessor folders sealed and unedited.
