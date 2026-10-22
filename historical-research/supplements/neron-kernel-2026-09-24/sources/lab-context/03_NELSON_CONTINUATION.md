# 03 — Continuation: the cusp constant-term aggregate for the definite theta kernel

Instruction: `work/CURRENT_TASK.md` (packet `PROMPT.md`, Phase 2). Inputs: `01` (Theorem A,
`M = <psi,psi>`), `02` (corrected). Nelson arXiv:1210.1243 is **not readable here** (egress
policy); every identity below is derived from definitions or from the standard imports
named in place. Status line and summary are at the end of this file (§9, written last).

Notation. `N = 2^3*3*2243*4547^2*5843`, `f = f_E` (newform, `a_1 = 1`, real coefficients),
`G in M_2(Gamma_0(N))` a norm-theta series (`Theta_{x,y}`, or `Theta(z_p,z_p)` by bilinearity),
`F_G(z) = y^2 G(z) conj(f(z))`. For `tau = [[a,b],[c,d]] in SL_2(Z)`,
`(h|_2 tau)(z) = (cz+d)^{-2} h(tau z)`, `e(x) = exp(2 pi i x)`, `T = [[1,1],[0,1]]`.

## 1. Lemma 1 — cosets, cusps, widths and multiplicities (exact)

**Counting correction.** The aggregate is a sum over the
`[SL_2(Z) : Gamma_0(N)] = mu_N = 13,017,263,840,621,568` cosets. The number 145,536 counts
**cusps**, i.e. orbits of these cosets under `Gamma_inf = ±<T>`; it is not the number of terms.

> **Lemma 1.**
> (a) `Gamma_0(N) tau -> (c : d) mod N` is a bijection `Gamma_0(N)\SL_2(Z) -> P^1(Z/NZ)`, so there
> are `mu_N` cosets.
> (b) Right multiplication by `T` acts by `(c:d) -> (c : d+c)`; its orbits are the cusps of
> `Gamma_0(N)`, the cusp of the orbit of `tau` being `tau(inf) = a/c`. For each `c | N` there are exactly
> `phi(gcd(c, N/c))` orbits with `gcd(c, N) = c`, each of size (width) `w_c = N / gcd(c^2, N)`.
> Hence `#cusps = sum_{c|N} phi(gcd(c,N/c)) = 145,536` and
> `sum_{c|N} phi(gcd(c,N/c)) w_c = mu_N`.
> (c) (Local structure.) Via CRT, `P^1(Z/N) = prod_q P^1(Z/q^{a_q})` compatibly with `T`. Locally,
> for `i = min(v_q(c), a_q)` there are `phi(q^{min(i, a_q - i)})` local cusps of local width
> `q^{a_q - min(2i, a_q)}`; a global cusp is a tuple of local cusps and its width is the product of
> the local widths.
> (d) (Aggregate.) For `h` of period `w` put `CT^{(w)}[h](y) := (1/w) int_0^w h(x+iy) dx`. Then
> `y^2 (G|_2 tau)(z) conj((f|_2 tau)(z)) = F_G(tau z)`, which depends only on the coset of `tau`, and
>
>     C_G(y) := sum_{tau in Gamma_0(N)\SL_2(Z)} CT^{(1)}[ F_G∘tau ](y)
>             = sum_{cusps A} w_A * CT^{(w_A)}[ F_G∘tau_A ](y)  =  CT^{(1)}[ Tr F_G ](y),
>
> with `Tr F_G = sum_tau F_G∘tau` (`SL_2(Z)`-invariant), for any choice of `tau_A` with `tau_A(inf) = A`.

*Proof.* (a) `Gamma_0(N)` is the preimage of the upper-triangular group `B(Z/N)` under the
surjection `SL_2(Z) -> SL_2(Z/N)`, and `B(Z/N)\SL_2(Z/N) -> P^1(Z/N)`, `g -> bottom row`, is a
bijection. `|P^1(Z/N)| = prod q^{a-1}(q+1) = mu_N`.
(b)–(c) By CRT it suffices to treat `P^1(Z/q^a)`. Points with `c` a unit are `(1 : y)`,
`y in Z/q^a`, and `T^n` sends `(1:y)` to `(1 : y+n)`: one orbit of size `q^a` (local class `i = 0`).
Otherwise `d` is a unit and the point is `(x : 1)` with `x = q^i u`, `i >= 1`. Since `1 + nx` is a
unit, `T^n(x:1) = (x/(1+nx) : 1)`; for `i < a`, writing the point as `u mod q^{a-i}`, this is
`1/u -> 1/u + n q^i (mod q^{a-i})`. The orbits therefore have size `q^{a-i}/q^{min(i,a-i)} =
q^{a-min(2i,a)}` and are indexed by the unit classes of `1/u mod q^{min(i,a-i)}`:
`phi(q^{min(i,a-i)})` of them. For `i = a` (`x = 0`) there is one fixed point. The diagonal action
of `Z` on a product of finite orbits of pairwise coprime sizes has orbits equal to products of
orbits (CRT on `Z/prod w_q`), giving the global counts; the global class of `(c:d)` is
`gcd(c,N) = prod q^{i_q}`. The cusp of `Gamma_0(N) tau` is `tau(inf) = a/c`, and right
multiplication by `T` (or `-I`) does not change it.
(d) `Im(tau z) = y/|cz+d|^2`, so `y^2 (cz+d)^{-2} G(tau z) conj((cz+d)^{-2} f(tau z)) = Im(tau z)^2 G(tau z) conj(f(tau z))`.
`F_G` is `Gamma_0(N)`-invariant. For the orbit `{Gamma_0(N) tau_A T^j : 0 <= j < w_A}` of a cusp `A`,
`sum_j int_0^1 F_G(tau_A T^j (x+iy)) dx = int_0^{w_A} F_G(tau_A(x+iy)) dx = w_A CT^{(w_A)}[F_G∘tau_A](y)`,
and `F_G∘tau_A` has period `w_A` because `tau_A T^{w_A} tau_A^{-1} in ±Gamma_0(N)`. Replacing `tau_A` by
`gamma tau_A T^k` (`gamma in Gamma_0(N)`) leaves the right side unchanged. ∎

**Exact table for the seed** (`work/scripts/cusp_widths.py` → `work/cusp_widths_output.json`):

| `q^a` | local class `i` | local cusps `phi(q^{min(i,a-i)})` | local width | Atkin–Lehner type |
|---|---|---|---|---|
| `2^3` | 0, 1, 2, 3 | 1, 1, 1, 1 | 8, 2, 1, 1 | yes, **no**, **no**, yes |
| `q ∈ {3, 2243, 5843}` | 0, 1 | 1, 1 | `q`, 1 | yes, yes |
| `4547^2` | 0, 1, 2 | 1, 4546, 1 | `4547^2`, 1, 1 | yes, **no**, yes |

Totals: 96 divisor classes; 145,536 cusps, of which 32 are Atkin–Lehner images of `inf`
(`gcd(c, N/c) = 1`) and 145,504 are not. The Atkin–Lehner cusps carry
9,760,801,706,156,160 cosets and the others 3,256,462,134,465,408 (sum `mu_N`).

*Checks run* (exact, 1.7 s): the formula table reproduces 145,536 and `mu_N`; brute-force
`T`-orbit enumeration on `P^1(Z/q^a)` for `2^1..2^6, 3^1..3^4, 5^1..5^3, 7^2, 11^2` confirms (c)
class by class; direct enumeration of `P^1(Z/N)` for `N = 72, 200, 360` confirms (a)–(b).
Scope: combinatorics of `Gamma_0(N)\SL_2(Z)` only.

## 2. Lemma 2 — Parseval at each cusp

> **Lemma 2.** For a cusp `A` with representative `tau_A` and width `w = w_A`,
>
>     (G|_2 tau_A)(z) = sum_{n>=0} g_A(n) e(nz/w),    (f|_2 tau_A)(z) = sum_{n>=1} a_A(n) e(nz/w),
>
> and
>
>     CT^{(w)}[F_G∘tau_A](y) = y^2 sum_{n>=1} g_A(n) conj(a_A(n)) exp(-4 pi n y / w).
>
> Consequently, with Lemma 1(d),
>
>     C_G(y) = y^2 sum_{cusps A} w_A sum_{n>=1} g_A(n) conj(a_A(n)) exp(-4 pi n y / w_A).        (2.1)
>
> The products `g_A(n) conj(a_A(n))` do not depend on the choice of `tau_A`.

*Proof.* `-I in Gamma_0(N)` and the weight is even, so every cusp is regular:
`tau_A T^w tau_A^{-1} in ±Gamma_0(N)` makes `G|_2 tau_A` and `f|_2 tau_A` invariant under `z -> z + w`.
Holomorphy at the cusp gives the expansions; cuspidality of `f` removes `n = 0` from `f|_2 tau_A`.
The coefficients grow polynomially, so for fixed `y > 0` both series converge absolutely and
uniformly in `x`. By Lemma 1(d), `F_G(tau_A z) = y^2 (G|_2 tau_A)(z) conj((f|_2 tau_A)(z))`, and
`(1/w) int_0^w e(nx/w) conj(e(mx/w)) dx = delta_{nm}`, while
`|e(nz/w)|^2 = exp(-4 pi n y/w)`. The constant term `g_A(0)` meets no `m = 0` term of `f`. Replacing
`tau_A` by `gamma tau_A T^k` (`gamma in Gamma_0(N)`) fixes both slashes up to the common factor
`e(nk/w)` on the `n`-th coefficients, which cancels in `g_A(n) conj(a_A(n))`. ∎

At `A = inf` (`tau_A = I`, `w = 1`): `g_inf(n) = a_n(G)` (for `G = Theta_{x,y}`, `a_n = B_{x,y}(n)`) and
`a_inf(n) = a_n(f)`. The remaining work is to make `g_A` and `a_A` explicit at the other
145,535 cusps (§§4–5) and to group the sum (§6).

## 3. Lemma 3 — an explicit integration identity (derived here)

Nelson's Theorem 5.6 could not be read. The identity below is derived from definitions with
standard imports (the level-one Eisenstein series); it is of the same type as the audit's
description (trace to `SL_2(Z)`, no level-`N` scattering matrix) but is **not** asserted to
coincide with Nelson's statement.

Let `F` be continuous on `Gamma_0(N)\H` with `F(tau_A z) = O(e^{-cy})` as `y -> inf` at every cusp.
`F_G` qualifies: `|F_G(tau_A z)| <= y^2 |G|_2 tau_A| |f|_2 tau_A|` and `f` is cuspidal. Put
`I(F) = int_{Gamma_0(N)\H} F dmu` (`dmu = dx dy/y^2`), `C(y) = CT^{(1)}[Tr F](y)`,
`M(s) = int_0^inf C(y) y^{s-2} dy`, `xi(s) = pi^{-s/2} Gamma(s/2) zeta(s)`.

> **Lemma 3.** (i) `I(F) = int_{SL_2(Z)\H} Tr F dmu`.
> (ii) `M(s)` converges for `Re s > 1` and `int_{SL_2(Z)\H} Tr F(z) E(z,s) dmu = M(s)` there, with
> `E(z,s) = sum_{Gamma_inf \ SL_2(Z)} Im(gamma z)^s`. Hence `I(F) = (pi/3) Res_{s=1} M(s)`.
> (iii) (Exact contour form.) For any `B > 0`, with `K_B(s) = (s - 1/2) exp((s - 1/2)^2 / B)` and any
> `sigma_1 > 1`,
>
>     I(F) = 4 e^{-1/(4B)} (1/2 pi i) int_{(sigma_1)} pi^{-s} Gamma(s) zeta(2s) M(s) K_B(s) ds.        (3.1)
>
> (iv) For `F = F_G`, inserting (2.1) and expanding `zeta(2s)`,
>
>     I(F_G) = 4 e^{-1/(4B)} sum_{cusps A} w_A^2 sum_{n>=1} ( g_A(n) conj(a_A(n)) / n ) sum_{m>=1} W_B(n m^2 / w_A),  (3.2)
>     W_B(x) = (1/2 pi i) int_{(sigma_1)} (4 pi^2 x)^{-s} Gamma(s) Gamma(s+1) K_B(s) ds / (4 pi),
>
> and `lambda_f(G) = I(F_G) / I(F_f)` (`I(F_f) = <f,f>`, Petersson norm on `Gamma_0(N)\H`).

*Proof.* (i) `SL_2(Z) = ⊔ Gamma_0(N) tau`, so `Gamma_0(N)\H` is tiled by the `tau(D)` for a fundamental
domain `D` of `SL_2(Z)`; `dmu` is invariant. (ii) `Tr F` is bounded and rapidly decreasing at the
cusp, so `int_{Gamma_inf\H} |Tr F| y^{sigma-2} dx dy < inf` for `sigma > 1` and the unfolding is
justified. **[import: level-one Eisenstein series]** `E(z,s)` continues meromorphically, with a
simple pole at `s = 1` of constant residue `3/pi`; `E*(z,s) = xi(2s) E(z,s)` satisfies
`E*(z,s) = E*(z,1-s)`, is holomorphic except for simple poles at `s = 1, 0` with residues `1/2`, `-1/2`
(constant in `z`; `xi(2) = pi/6`), and has at most polynomial growth in vertical strips on the Siegel
domain away from the poles. (iii) Put `Lambda(s) = int Tr F E*(.,s) dmu = xi(2s) M(s)`. By (ii) it is
holomorphic except at `s = 1, 0` with residues `I/2` and `-I/2`, satisfies `Lambda(s) = Lambda(1-s)`, and is
polynomially bounded in vertical strips; `K_B` is entire with Gaussian decay in vertical strips.
Shifting from `Re s = sigma_1` to `Re s = 1 - sigma_1`:
`(1/2 pi i)(int_{(sigma_1)} - int_{(1-sigma_1)}) Lambda K_B = (I/2)(K_B(1) - K_B(0))`. The substitution
`s -> 1-s` turns the second integral into `int_{(sigma_1)} Lambda(s) K_B(1-s) ds`. Here `K_B(1-s) = -K_B(s)`
and `K_B(1) - K_B(0) = e^{1/(4B)}`, so `I e^{1/(4B)}/2 = (1/2 pi i) int_{(sigma_1)} 2 Lambda K_B`.
(iv) For `sigma_1 > 1`, `zeta(2s) = sum m^{-2s}` and, by (2.1) and Fubini (absolute convergence:
coefficients polynomially bounded),
`M(s) = Gamma(s+1) (4 pi)^{-s-1} sum_A w_A^{s+2} sum_n g_A(n) conj(a_A(n)) n^{-s-1}`. Interchanging the
absolutely convergent sums with the contour integral gives (3.2). The ratio formula is
Proposition R2 of `02` rewritten: the Eisenstein and other cuspidal components of `G` are
Petersson-orthogonal to `f`, so `I(F_G) = lambda_f(G) <f,f>`. ∎

*Normalization check (NUMERICAL_EVIDENCE, level 1).* The weight-12 analogue of (3.1)–(3.2)
(`M(s) = sum tau(n)^2 Gamma(s+11)(4 pi n)^{-s-11}`, `B = 10`, `sigma_1 = 2`, `n <= 60`, `n m^2 <= 240`,
trapezoid rule on `|t| <= 45`) gives `1.0353620567634e-6` against the known
`<Delta,Delta> = 1.0353620568043e-6`: relative error `3.9e-11`
(`work/scripts/lemma3_delta_check.py`, 0.11 CPU s). This tests the constants of Lemma 3 (the
prefactor, residues, unfolding normalization); it is not a proof.

*Truncation behaviour (proved qualitatively; certified constants not yet derived).*
Shifting the contour in `W_B` to `Re s = A` gives `|W_B(x)| <= C_{A,B} x^{-A}` for every `A`, so the terms of
(3.2) with `n m^2 >> w_A` are negligible. An effective truncation therefore keeps, for each cusp,
indices `n` up to a multiple of `w_A` (times a slowly growing factor). Summed over cusps this is
of order `sum_A w_A = mu_N` terms. This counts **terms of the formula**; it is not a lower bound
for evaluating the sum, which §6 regroups.

## 4. Lemma 4 — the norm-theta series at an arbitrary cusp (explicit)

Let `L = L(x,y)` with `Q = nrd/n(x,y)`: even, positive, rank 4, Gram determinant `N^2`, level `N`,
dual `L^#`, bilinear form `(u,v) = Q(u+v) - Q(u) - Q(v)`; `theta_L(z) = sum_{b in L} e(Q(b) z)`, so
`Theta_{x,y} = theta_L / 2`.

> **Lemma 4.** For `gamma = [[a,b],[c,d]] in SL_2(Z)` with `c >= 1`,
>
>     (theta_L |_2 gamma)(z) = -(1/(N c^2)) sum_{l in L^#} Gs(a,l;c) e(d Q(l)/c) e(Q(l) z),
>     Gs(a,l;c) = sum_{r in L/cL} e( (a Q(r) + (l,r)) / c ).
>
> Hence at a cusp `A = a/c` (`c | N`, `gcd(a,c) = 1`, `tau_A = [[a,b],[c,d]]`), in the notation of Lemma 2,
>
>     g_A(n) = -(1/(2 N c^2)) sum_{l in L^#, Q(l) = n/w_A} Gs(a,l;c) e(d Q(l)/c),            (4.1)
>
> and the terms with `Q(l) not in (1/w_A) Z` cancel in total.

*Proof.* `gamma z = a/c - 1/(c(cz+d))`. Write `b = r + c lambda`, `r in L/cL`, `lambda in L`. Then
`Q(b) a/c ≡ a Q(r)/c (mod 1)`, so `theta_L(gamma z) = sum_r e(aQ(r)/c) sum_lambda e(tau' Q(lambda + r/c))` with
`tau' = -c/(cz+d) in H`. **[import: Poisson summation for a positive quadratic form]**
`sum_{lambda in L} e(tau' Q(lambda + x)) = (det)^{-1/2} (i/tau')^2 sum_{l in L^#} e(-Q(l)/tau' + (l,x))`, with
`det = N^2`, `(i/tau')^2 = -(cz+d)^2/c^2` and `-1/tau' = (cz+d)/c = z + d/c`. Collecting gives the formula.
`G|_2 tau_A = theta_L|_2 tau_A / 2`. By Lemma 2 the left side is a power series in `e(z/w_A)`, so by
uniqueness of Fourier expansions the coefficients of exponents outside `(1/w_A)Z` vanish. ∎

*Check (NUMERICAL_EVIDENCE):* `work/scripts/lemma4_theta_cusp_check.py` compares both sides by
direct summation for `A_2 ⊕ A_2` (det 9), `2I_4` (det 16) and a Hurwitz-type norm form (det 4),
`gamma in {S, [[1,0],[2,1]], [[1,0],[3,1]], [[2,1],[3,2]], [[1,0],[4,1]], [[3,2],[4,3]]}`: maximal relative
difference `4.5e-6`, attained where `Im(gamma z)` is small (direct-sum truncation); most cases
agree to `1e-10`–`1e-14`. At `gamma = S` it reproduces `theta_L|_2 S = -(1/N) theta_{L^#}` (the Weil
representation's `e(-sig/8)/sqrt|D|`).

### 4.1 Lemma 4' — local factorization and closed forms of `Gs`

Write `c = p^e c'` with `p ∤ c'`, and `ubar_p := c'^{-1} mod p^e`. CRT on `L/cL = prod_p L_p/p^e L_p` gives
`Gs(a,l;c) = prod_{p | c} Gs_p(l)`, `Gs_p(l) = sum_{r in L_p/p^e L_p} e( ubar_p (a Q(r) + (l,r)) / p^e )`.
Fix `L_p ≅ (O_p, u_p nrd)` with `u_p in Z_p^x` (§1 of `01`).

> **(a) `p | N^+`** (Eichler, `O_p = [[Z_p, Z_p],[p^{a_p} Z_p, Z_p]]`, `0 <= e <= a_p`). Write
> `l = [[l_1, l_2 p^{-a_p}],[l_3, l_4]]` (`l_i in Z_p`). Then
>
>     Gs_p(l) = p^{3e} * 1[ l_2 ≡ l_3 ≡ 0 (mod p^e) ] * e( -u_p ubar_p l_1 l_4 / (a p^e) ).
>
> For `e = a_p` the support condition is `l in L_p`, and the phase is `e(-ubar_p Q(l) / (a p^{a_p}))`.
>
> **(b) `p | N^-`** (maximal order `O_p` of the division algebra, `e = 1`):
>
>     Gs_p(l) = -p^3 * 1[ l in L_p ] * e( -ubar_p Q(l) / (a p) ).

*Proof.* (a) With `r = [[r_1, r_2],[p^{a_p} r_3, r_4]]`, `Q(r) = u(r_1 r_4 - p^{a_p} r_2 r_3)` and
`(l,r) = u trd(l adj(r)) = u(l_1 r_4 + l_4 r_1 - l_2 r_3 - l_3 r_2)`. Since `e <= a_p`, the term
`p^{a_p} r_2 r_3/p^e` is integral. The `r_2`- and `r_3`-sums give `p^e 1[l_3 ≡ 0]` and `p^e 1[l_2 ≡ 0]`. The
`r_4`-sum forces `a r_1 ≡ -l_1`, contributing `p^e e(-u ubar l_1 l_4/(a p^e))`. For `e = a_p`, `l_2 l_3 p^{-a_p} in p^{a_p} Z_p`,
so `Q(l) ≡ u l_1 l_4 (mod p^{a_p})`. (b) Split `r = r_0 + r_1`, `r_1 in P/pO`. `Q(P) ⊆ pZ_p` and `trd(P) ⊆ pZ_p`,
so `Q(r) ≡ Q(r_0)`, and the `r_1`-sum is `p^2 1[(l, P) ⊆ pZ_p] = p^2 1[l in p P^# = O_p]` (`O_p^# = P^{-1}`,
`P^# = P^{-2} = p^{-1} O_p`). For `l in O_p`, `Q ≡ u N_{F_{p^2}/F_p}` on `O/P = F_{p^2}` and
`(l, x) ≡ u Tr(lbar sigma(x))`. Completing the square, `a u N(x) + u Tr(lbar sigma(x)) = a u N(x + lbar/a) - u N(lbar)/a`, and
`sum_{x in F_{p^2}} e(t N(x)/p) = -p` for `t in F_p^x`. ∎

*Check (EXACT enumeration, float comparison):* `work/scripts/lemma4b_local_gauss_check.py`
compares (a) with the full sum over `O_p/p^eO_p` for Eichler orders of level `2^3, 3^2, 5` (all
`e`, random units and dual vectors; max abs. difference `1.7e-7` on values of size up to `p^{3e}`),
and (b) with the full sum for the maximal order `<1, i, (1+j)/2, (i+ij)/2>` of `(-1,-3)_Q` at
`p = 3` (all `l in O^#/3O^#`; max difference `4e-13`). 7.8 CPU s.

At a prime `p | c` of the second kind, `Gs_p` depends on `l` through `Q(l)` only when
`e = a_p` (Atkin–Lehner local cusps) or `p | N^-`. At the non-Atkin–Lehner local cusps
`0 < e < a_p` (`p = 2`, `e in {1,2}`; `p = 4547`, `e = 1`) it depends on the coordinate product `l_1 l_4`:
there the theta side is **not** a function of the norm value alone.

## 5. The newform at an arbitrary cusp

### 5.1 Lemma 5a — adelic dictionary and the Atkin–Lehner-type local cusps

Conventions: `psi = prod_v psi_v` on `A/Q`, `psi_inf(x) = e(x)`, `psi_q(x) = e(-{x}_q)` (conductor `Z_q`).
`phi_f` is the adelic lift of `f` (right `K_0(N)^`-invariant, trivial central character), with
Whittaker function `W = W_inf prod_q W_q`, `W(n(x) g) = psi(x) W(g)`, normalized by `W_q(1) = 1` and
`prod_q W_q(diag(n,1)) = a_n/n` (`n >= 1`). For `q ∤ N`, `W_q(diag(xi,1) k) = a_{q^v}/q^v` (`v = v_q(xi) >= 0`,
else 0) for `k in GL_2(Z_q)`. For `q | N`, `W_q` is the local newform (`K_0(q^{a_q})`-invariant), with
Atkin–Lehner eigenvalue `eps_q`: `W_q(g [[0,1],[-q^{a_q},0]]) = eps_q W_q(g)`.

> **Lemma 5a.** (i) For `tau = [[a,b],[c,d]] in SL_2(Z)`, the coefficient of `e(xi z)` (`xi in Q_{>0}`) in
> `f|_2 tau` is `xi prod_q W_q(diag(xi,1) tau_q^{-1})`; it vanishes unless `xi in (1/w)Z` (`w` = width).
> (ii) At a local class `i = a_q` (`q^{a_q} | c`): `W_q(diag(xi,1) tau_q^{-1}) = W_q(diag(xi,1))`, which is
> `1_{Z_q^x}(xi)` if `pi_q` is supercuspidal (`q = 2, 4547`) and `(a_q(f)/q)^{v(xi)} 1_{v(xi) >= 0}` if `q || N`.
> (iii) At a local class `i = 0` (`q ∤ c`):
>
>     W_q(diag(xi,1) tau_q^{-1}) = eps_q * psi_q(-xi d / c) * W_q(diag(q^{a_q} xi, 1)),
>
> so it is supported on `v_q(xi) = -a_q` (supercuspidal) or `v_q(xi) >= -1` (`q || N`).
> (iv) For `q || N`, `eps_q = -a_q(f) in {±1}` (split: `a_q = 1`; nonsplit: `a_q = -1`).

*Proof.* (i) `phi_f(g_z) = y f(z)` for `g_z = [[y^{1/2}, x y^{-1/2}],[0, y^{-1/2}]]`. For `tau in SL_2(Z)`, left
`GL_2(Q)`-invariance gives `y (f|_2 tau)(z) = phi_f(tau_inf g_z) = phi_f((g_z, tau_fin^{-1}))`. Expand
`phi_f = sum_{xi in Q^x} W(diag(xi,1) g)`. With `W_inf(diag(t,1)) = t e^{-2 pi t} 1_{t>0}` (weight 2) and
`W_inf(n(x)g) = e(x) W_inf(g)`, this gives `sum_{xi > 0} xi e(xi z) prod_q W_q(diag(xi,1) tau_q^{-1})`. The
normalization is fixed at `tau = I`. Lemma 2 gives the support.
(ii) `tau_q^{-1} = [[d,-b],[-c,a]] in K_0(q^{a_q})`, and the central character is trivial. The Kirillov
newform of a supercuspidal is `1_{Z_q^x}`, and for `q || N` it is `(a_q/q)^{v}` (arithmetic normalization,
`a_{q^m} = a_q^m`).
(iii) Put `k = tau_q^{-1} = [[alpha, beta],[gamma', delta]]`, `gamma' = -c in Z_q^x`, `alpha = d`. Then
`k = n(alpha/gamma') w' b` with `w' = [[0,-1],[1,0]]` and `b = [[gamma', delta],[0, 1/gamma']] in K_0(q^{a_q})`. Also
`w' = diag(-1, -q^{-a_q}) [[0,1],[-q^{a_q},0]]`. Hence
`W(diag(xi,1) k) = psi_q(xi alpha/gamma') eps_q W(diag(-xi, -q^{-a_q})) = psi_q(-xi d/c) eps_q W(diag(q^{a_q} xi, 1))`.
(iv) **[import: Atkin–Lehner eigenvalue = local root number for an unramified twist of
Steinberg]** `eps_q = eps(1/2, pi_q) = -a_q`. ∎

The Steinberg primes (`3, 2243, 5843`) have only Atkin–Lehner local cusps, so their local
factors are explicit given `a_q(f)` (computed: `work/scripts/local_signs.py`, §5.2). The
non-Atkin–Lehner local cusps are `i = 1` at 4547 (4546 local cusps) and `i = 1, 2` at 2.

### 5.2 Local signs (exact computation + derivation)

`work/scripts/local_signs.py` (0.04 CPU s):

- Multiplicative primes, by counting points of the reduction (including the node):
  `a_3 = -1` (nonsplit), `a_2243 = +1` (split), `a_5843 = -1` (nonsplit); hence
  `eps_3 = +1`, `eps_2243 = -1`, `eps_5843 = +1` (Lemma 5a(iv)).
- `q = 4547`. The inertial type forces `pi_q = c-Ind_{ZK}^G sigma~_theta`, where `theta` is a character of
  `F_{q^2}^x` of order 4, trivial on `F_q^x`, i.e. `theta(x) = chi(x^{q-1})` for `chi` of order 4 on the
  norm-one group `U = mu_{q+1}` (`4 | q+1 = 4548`). The extension `sigma~` to `ZK` is unique because the
  central character is trivial. Hence `pi_4547` is **uniquely determined**, up to `theta <-> theta^q = theta^{-1}`,
  which gives the same representation. No further local datum is needed at 4547.
  *Gauss sum.* Fibering `F_{q^2}^x -> F_{q^2}^x/F_q^x` and summing `e(t Tr(x)/q)` over `t in F_q^x` gives
  `tau(theta) := sum_x theta(x) e(Tr(x)/q) = q theta(delta)`, with `delta` the trace-zero class; also
  `theta(delta) = chi(-1) = i^{(q+1)/2} = -1` for `q = 4547` (`(q+1)/2 = 2274 ≡ 2 mod 4`). Brute force
  confirms `tau(theta) = q theta(delta)` and `theta(delta) = i^{(q+1)/2}` for `q = 3, 7, 11, 19, 23, 43`.
  **[import: epsilon factor of a depth-zero supercuspidal, `eps(1/2, pi_theta, psi) = -tau(theta)/q` for
  `psi` of conductor `Z_q`]** gives `eps_4547 = -theta(delta) = +1`. This agrees with **[import: Rohrlich's
  formula `W_q = (-2/q)` for potentially good reduction with `e = 4`, `q >= 5`]**:
  `(-2/4547) = +1`. The sign convention of the imported epsilon formula was not independently
  re-derived, so the agreement of the two imports is recorded as a consistency check only.
- `q = 2`: `eps_2` is not determined by the local methods of this section (§5.4). It is
  determined globally in `04` (Prop. 7'): `eps_2 = +1`.

### 5.3 Lemma 5b — the 4546 non-Atkin–Lehner local cusps at `q = 4547` (explicit)

Let `sigma = sigma_theta` (§5.2), realized in its finite Kirillov model on `C[F_q^x]` with
`psi_0(t) = e(-t/q)`: `sigma(n(b))phi(x) = psi_0(bx)phi(x)`, `sigma(diag(a,1))phi(x) = phi(ax)`, trivial centre, and
`sigma(w)phi(x) = sum_{y in F_q^x} j(xy) phi(y)` for `w = [[0,1],[-1,0]]`, with Bessel function

    j(t) = -(1/q) sum_{u in F_{q^2}^x, N(u) = t} theta(u) psi_0(Tr u),      jhat(s) = sum_{t in F_q^x} j(t) psi_0(s t).

> **Lemma 5b.** Let `tau = [[a,b],[c,d]] in SL_2(Z)` with `v_q(c) = 1`, `c = q c'`. Then
>
>     W_q(diag(xi,1) tau_q^{-1}) = 1[v_q(xi) = 0] * J_0 * jhat( c' a / xi mod q ),      J_0 = -theta(delta) = +1.
>
> In particular it depends on the local cusp only through `c' a mod q` (one of the 4546 local
> cusps), and on `xi` only through `xi mod q` on the unit group.

*Proof.* (1) With `g = diag(1,q)`, `g^{-1} K_0(q^2) g = K_T` (`01` §5.4, audit-corrected), and the
newvector is `pi(g) v_T`, so `W_q(h) = W_T(h g)`, where `W_T` is the Whittaker function of `v_T`.
(2) `tau_q^{-1} g = [[d, -bq],[-c, aq]] = q * diag(1/q, 1) * k''`, `k'' = [[d, -bq],[-c', a]] in GL_2(Z_q)` (determinant
`ad - bc = 1`). The centre acts trivially, so `W_q(diag(xi,1)tau_q^{-1}) = W_T(diag(xi/q, 1) k'')`.
(3) `pi^{K(1)} = sigma` (Mackey; cuspidality kills the other double cosets). In the Kirillov model
w.r.t. `psi_q`, `v_T = 1_{q^{-1} Z_q^x}`. Indeed `pi(g) v_T` is the newvector `1_{Z_q^x}` and `pi(g)` acts by
`phi(y) -> phi(y/q)` modulo the centre. Hence `pi^{K(1)}` is the space of functions on `q^{-1} Z_q^x` invariant
under `1 + qZ_q`, identified with `C[F_q^x]` by `y = u/q -> u mod q`. Under it `n(x)` (`x in Z_q`) acts by
`psi_q(xu/q) = psi_0(x u)` and `diag(alpha,1)` by `u -> alpha u`: this is the finite Kirillov model of `sigma`.
Thus `W_T(diag(y,1)k) = (sigma(kbar) 1)(qy mod q)` for `y in q^{-1}Z_q^x` and 0 otherwise. So the value is
`1[v(xi) = 0] (sigma(kbar'') 1)(xi mod q)` with `kbar'' = [[d, 0],[-c', a]]`.
(4) `kbar'' = w [[a, c'],[0, d]] w^{-1}`, `sigma(w^{-1}) = sigma(-1) sigma(w) = sigma(w)`, and `sigma(w) 1 = J_0 1`: `sigma(w)1` is
torus-invariant, hence constant, with constant `sum_t j(t) = -(1/q) tau(theta) = -theta(delta)` (§5.2). Then
`sigma([[a,c'],[0,d]]) 1 = psi_0(c' x/d)`, and `(sigma(w) psi_0(c'./d))(x) = sum_y j(xy) psi_0(c'y/d) = jhat(c'/(dx))`.
Finally `d^{-1} ≡ a (mod q)` since `ad - bc = 1` and `q | c`. ∎

*Checks (NUMERICAL, exact-structure):* `work/scripts/lemma5b_sigma_check.py` builds this model for
`q = 3, 7, 11, 19` (`theta` of order 4, trivial on `F_q^x`), with `sigma(g)` for all `g` via the Bruhat
decomposition. It verifies (1) the homomorphism property on random pairs (error `<= 2e-15`),
(2) the character `-(theta(u) + theta(u^q))` on an elliptic element (exact), (3) `sigma(w)1 = J_0 1` with
`J_0 = -theta(delta)` (`+1` for `q ≡ 3 mod 8`, `-1` for `q ≡ 7 mod 8`), and (4) the closed form of step (4)
(error `<= 1.3e-15`). The p-adic steps (1)–(3) are derivations, not numerically tested.

*Cost of the local table (exact count).* One pass over `F_{q^2}^x` (`q^2 - 1 = 20,675,208`
elements) tabulates `j(t)` for all `t`; `jhat` is a length-`(q-1)` additive Fourier transform. The
full local table (4546 values) costs `O(q^2)` field operations.

### 5.4 Lemma 5c — supercuspidal newforms at intermediate cusps; the prime 2

For a supercuspidal `pi` of `GL_2(Q_p)` with conductor exponent `n`, trivial central character and
Kirillov newform `phi_new = 1_{Z_p^x}`, write `xi_{nu,m}(y) = nu(y_0) 1[v(y) = m]` (`y = p^{v(y)} y_0`, `nu` a character
of `Z_p^x`), and `Phi_i(y) := W(diag(y,1) [[1,0],[p^i,1]])`, `0 < i < n`.

> **Lemma 5c.** (i) With `w = [[0,1],[-1,0]]`: `pi(w) xi_{nu,m} = eps(1/2, pi ⊗ nu^{-1}, psi_p) xi_{nu^{-1}, -m - a(pi ⊗ nu^{-1})}`.
> (ii) For `0 < i < n`,
>
>     Phi_i(y) = eps(1/2, pi) sum_{nu : a(nu) <= n-i} c_nu^{(i)} eps(1/2, pi ⊗ nu^{-1}) nu^{-1}(y_0) 1[ v(y) = n - a(pi ⊗ nu^{-1}) ],
>     c_nu^{(i)} = avg_{u in Z_p^x} psi_p(-p^{i-n} u) nu^{-1}(u).
>
> (iii) At `p = 2`, `n = 3` (`pi = pi_2`): `Phi_2(y) = -1_{Z_2^x}(y)` (no unknown datum), and
>
>     Phi_1(y) = i * eps_2 * eps_2' * chi_{-4}(y_0) * 1[ v(y) = 3 - a' ],
>     eps_2 = eps(1/2, pi_2),  eps_2' = eps(1/2, pi_2 ⊗ chi_{-4}),  a' = a(pi_2 ⊗ chi_{-4}).
>
> With `a' = 4` (below) and `eps_2 eps_2' = +1` (`04`): `Phi_1(y) = i chi_{-4}(y_0) 1[v(y) = -1]`.

*Proof.* (i) **[import: Jacquet–Langlands local functional equation for `GL_2`, supercuspidal
case (`L = 1`)]** `Z(pi(w)phi, chi^{-1}, 1-s) = eps(s, pi ⊗ chi, psi) Z(phi, chi, s)` with
`Z(phi,chi,s) = int phi(y) chi(y) |y|^{s-1/2} d^x y`. For `chi` with `chi|_{Z^x} = nu^{-1}` and `chi(p) = z`,
`Z(xi_{nu,m}, chi, s) = vol * z^m p^{-m(s-1/2)}`. Also `eps(s, pi ⊗ chi) = eps(1/2, pi ⊗ nu^{-1}) z^a p^{-a(s-1/2)}` with
`a = a(pi ⊗ nu^{-1})` (unramified twist, `psi` of conductor `Z_p`). Comparing both sides as functions of
`(z, s)` gives (i). At `nu = 1, m = -n` this reproduces the Atkin–Lehner eigenvalue `eps(1/2, pi)`.
(ii) `[[1,0],[p^i,1]] = w^{-1} n(-p^i) w` and `pi(w^{-1}) = pi(-1) pi(w) = pi(w)`. Then
`pi(w) phi_new = eps(1/2,pi) xi_{1,-n}`, and `pi(n(-p^i))` multiplies by `psi_p(-p^{i-n} u)` on `v(y) = -n`, a function of
`u mod p^{n-i}` that expands over the characters with `a(nu) <= n-i` with coefficients `c_nu^{(i)}`.
Apply (i) again. (iii) The characters of `Z_2^x` with `a(nu) <= 1` are trivial, and
`psi_2(-u/2) = -1` (`u` odd), so `c_1^{(2)} = -1` and `Phi_2 = -eps(1/2,pi)^2 1[v = 0]`. Here `eps^2 = 1` (self-dual, trivial
central character). With `a(nu) <= 2`, `nu in {1, chi_{-4}}`, and `psi_2(-u/4) = i, -i` for `u ≡ 1, 3 (mod 4)`, so
`c_1^{(1)} = 0` and `c_{chi_{-4}}^{(1)} = i`. ∎

*Cross-check of (i)–(ii) against Lemma 5b (NUMERICAL, error 0.0):*
`work/scripts/lemma5c_crosscheck.py` evaluates (ii) for the depth-zero `pi_theta` (`n = 2, i = 1`),
using `eps(1/2, pi_theta ⊗ nu^{-1}) = -tau(theta^{-1} (nu o N))/q` (Tate's `chi^{-1}` convention; `theta~(p) = eta_{L/Q_p}(p) = -1`
from the trivial central character). For `q = 3, 7, 11, 19` it reproduces `J_0 jhat(-1/xi)` of Lemma 5b
exactly. A first coding with `nu` in place of `nu^{-1}` failed for `q >= 7`, which confirms that the check
discriminates conventions.

**The prime 2.** `pi_2` is supercuspidal (`01` §0.1) and **not dihedral**. For `L/Q_2` unramified,
`a(Ind theta) = 2a(theta)` is even. For `L` ramified (`d(L) in {2,3}`), `O_L^x/(1+p_L)` is trivial, so a character
`theta != theta^sigma` has `a(theta) >= 2` and `a(Ind theta) = d(L) + a(theta) >= 4`. Hence `pi_2` is an exceptional
(primitive) supercuspidal, and the dihedral formulas used at 4547 do not apply. By Lemmas 5a, 5c
the local factors at 2 are:

| local class `i` (width) | `W_2(diag(xi,1) tau_2^{-1})` | datum (value) |
|---|---|---|
| 3 (1) | `1_{Z_2^x}(xi)` | none |
| 2 (1) | `-psi_2(-xi b/a) 1_{Z_2^x}(xi)` (reduction of `k` via `n(-b/a) diag(1/a,a) [[1,0],[-c/a,1]]`) | none |
| 1 (2) | `psi_2(-xi b/a) Phi_1(xi/(a^2 u))`, `u = -c/(2a)` | `eps_2 eps_2' = +1` (`04`), `a' = 4` |
| 0 (8) | `eps_2 psi_2(-xi d/c) 1[v(xi) = -3]` | `eps_2 = +1` (`04`) |

**Computed datum `a' = 4`.** `pi_2 ⊗ chi_{-4}` is the 2-component of the quadratic twist
`E^{(-1)} : y^2 = x^3 + 22735 x^2 + 106272484 x` (twist by `Q(i)`, whose character has 2-component `chi_{-4}`).
`work/scripts/tate_conductor.py` implements Tate's algorithm (Silverman IV.9.4; brute-force
coordinate changes at `p = 2, 3`). It reproduces the known conductors of 13 test curves (11a1,
14a1, 15a1, 20a1, 24a1, 27a1, 36a1, 37a1, 48a1, `y^2 = x^3 ± x`, `y^2 = x^3 ± 4x`). For `E` it returns
exactly the seed's `N` (at 2: type `I_1*`, `f = 3`), and for `E^{(-1)}` type `I_0*`, `f = 4` at 2. Hence
`a' = 4`, and `Phi_1` is supported on `v(y) = -1`. *Consistency:* the supports of the local factors
(`v(xi) = -3, -1, 0, 0` at `i = 0..3` for `p = 2`; `-2, 0, 0` at `i = 0, 1, 2` for 4547) match exactly the
local widths `8, 2, 1, 1` and `4547^2, 1, 1` of Lemma 1.

**The two remaining local signs.** `eps_2 = eps(1/2, pi_2) = W_2(E)` and
`eps_2' = eps(1/2, pi_2 ⊗ chi_{-4}) = W_2(E^{(-1)})` (local root numbers at 2) are well defined (`±1`:
self-dual, trivial central character). No local formula or table for root numbers at 2 was
available here (Halberstadt/Rizzo tables, the Dokchitsers' formula). The first version of this
file (`0f6d4df`) therefore left them open. They are now determined in `work/04_TWO_ADIC_SIGNS.md` by
a global route: 2-isogeny local cokernels (exact) and the 2-parity theorem for Selmer coranks (an
import). Neither the parity conjecture nor any rank is used. **Result: `eps_2 = eps_2' = +1`.**

(The rows `i = 1, 2` use `k = tau^{-1} = n(-b/a) diag(1/a, a) [[1,0],[-c/a,1]]`,
`[[1,0],[2^i u,1]] = diag(1,u)[[1,0],[2^i,1]]diag(1,u^{-1})` and `K_0(8)`-invariance.) Note
`eps_2 = W(E)` via the product formula with the computed signs (`W_inf = -1`,
`eps_3 eps_2243 eps_5843 eps_4547 = -1`). `04` proves `W(E) = +1` from Selmer-corank parity. It uses
neither the parity conjecture nor `rank E(Q) = 2`; the value merely agrees with the parity
expectation for rank 2.

## 6. Lemma 6 — the local-factor grouping (proved; not a product formula)

For `l in L^#` put `xi = Q(l)`, write `m(l)` for the prime-to-`N` part of `xi` (an integer, since
`Q(L^#) ⊆ N^{-1}Z`), and fix local isomorphisms `L_q ≅ (O_q, u_q nrd)`. At `q | N^+` use coordinates
`l_q = [[l_1, l_2 q^{-a_q}],[l_3, l_4]]`.

> **Lemma 6.** For `y > 0`,
>
>     C_G(y) = -(y^2/2) sum_{l in L^#, l != 0} Q(l) (a_{m(l)}(f)/m(l)) e^{-4 pi Q(l) y} prod_{q | N} S_q(l_q),        (6.1)
>
>     I(F_G) = -2 e^{-1/(4B)} sum_{l in L^#, l != 0} (a_{m(l)}(f)/m(l)) prod_{q | N} S_q(l_q) sum_{k >= 1} W_B(Q(l) k^2),    (6.2)
>
> for `G = Theta_{x,y}` with `L = L(x,y)`, where `S_q = sum over the local cusp classes of the local term
> t_q = w_{A_q} kappa_q conj(W_q)`, each `t_q` depending only on the local class. Explicitly (`v = v_q(xi)`):
>
> - `q in {3, 2243, 5843}` (`a_q = ±1`, `eps_q = -a_q`):
>   `S_q = -(a_q/q)^v (1/q + 1[l_q in L_q])` for `v >= 0`, and `S_q = -a_q` for `v = -1`.
> - `q = 4547` (`eps = J_0 = +1`):
>   `S_q = 1[v = -2] + 1[l_q in L_q] 1[v = 0]
>         + (J_0/q) 1[q | l_2, q | l_3] 1[v = 0] sum_{s in F_q^x} e(-u_q (l_2/q)(l_3/q)/(s q)) conj(jhat(s/xibar))`.
> - `q = 2` (`l_(2)` is the local component at 2, not the coordinate `l_2`):
>   `S_2 = eps_2 1[v = -3] + 1[l_(2) in L_2] 1[v = 0] - (1/2)(-1)^{(l_2/4)(l_3/4)} 1[4 | l_2, 4 | l_3] 1[v = 0]
>         - (1/2) eps_2 eps_2' (-1)^{l_1 l_4} 1[l_2 ≡ l_3 ≡ 2 (mod 4)]`.
>   With `eps_2 = eps_2' = +1` (`04`, Prop. 7'):
>   `S_2 = 1[v = -3] + 1[l_(2) in L_2] 1[v = 0] - (1/2)(-1)^{(l_2/4)(l_3/4)} 1[4 | l_2, 4 | l_3] 1[v = 0]
>         - (1/2)(-1)^{l_1 l_4} 1[l_2 ≡ l_3 ≡ 2 (mod 4)]`.
>
> By bilinearity the same holds for `G = Theta(z_p, z_p)`, with `sum_l` replaced by
> `sum_{P,Q} z_P z_Q sum_{l in L(P,Q)^#}` and the local coordinates of each `L(P,Q)`.

*Proof.* (1) *Per-cusp product formula.* Choose each cusp representative `tau_A = [[a,b],[c,d]]` with
`c = c_A = prod_q q^{i_q}` (`c | N`). By Lemmas 2, 4 and 5a the coefficient pairing of cusp `A` at exponent `xi` is
`w_A (1/2) sum_{Q(l)=xi} [-(1/(N c^2)) Gs(a,l;c) e(d xi/c)] * conj(xi prod_q W_q(diag(xi,1) tau_q^{-1}))`. The product formula
`e(x) = prod_q e({x}_q)` (valid for `x in Q`, since `x - sum_q {x}_q in Z`), CRT on `L/cL`, `1/N = prod q^{-a_q}` and
`w_A = prod w_{A_q}` give `-(1/2) xi (a_m/m) prod_{q|N} t_q` with
`t_q = w_{A_q} q^{-a_q - 2i_q} Gs_q e({d xi/c}_q) conj(W_q(...))` and `Gs_q = sum_{L_q/q^{i_q}L_q} e({(aQ(r)+(l,r))/c}_q)`. For `q ∤ N`,
`W_q` is `K`-invariant and gives `a_m/m`.
(2) *Locality.* `t_q` depends only on the local class. At `i_q = 0` the phase of `kappa_q` and that of `conj(W_q)`
(Lemma 5a(iii)) cancel exactly, leaving `eps_q W_q(diag(q^{a_q} xi, 1))`. At `i_q = a_q`,
`Gs_q = ±q^{3a_q} 1[l in L_q] e({-xi/(ac)}_q)` (Lemma 4'; sign `-` at `N^-`), and the remaining phase is
`e({xi b/a}_q) = 1` because `xi in Z_q`. At the non-Atkin–Lehner classes the closed forms above follow
from Lemmas 4'(a), 5b, 5c by the same cancellations, using `d ≡ a^{-1} (mod c)`. At 4547 the value
depends on the class through `s = c'a mod q` only. At `q = 2`, `i = 1`, the support forces
`l_2 ≡ l_3 ≡ 2 (mod 4)`, and then `chi_{-4}` and the phase combine into `(-1)^{l_1 l_4}`.
(3) *Factorization.* By Lemma 1(c) the cusps are the tuples of local classes, and CRT lets the
representative realize any tuple (prescribe `a mod q^M` for each `q | N`; complete `b, d`). Hence
`sum_A prod_q t_q = prod_q sum_{A_q} t_q = prod_q S_q`. (6.2) follows from (6.1) and Lemma 3 as (3.2) did. ∎

*Checks (NUMERICAL):* `work/scripts/grouping_local_check.py` (28 CPU s) computes `t_q` **from the
definitions**: brute-force local Gauss sums, product-formula phases, and Whittaker values from Lemmas
5a–5c. It uses 4–6 random global representatives per class and random dual vectors and local scalars `u_q`.
- `q = 2` (all four sign choices): invariance within each class and agreement with the closed forms,
  max error `9e-16` (120 cases per choice).
- `q = 11` (depth-zero stand-in for 4547, same `q ≡ 3 mod 8` structure): max error `1.4e-15`
  (153 cases). The class `i = 2` uses the separately verified Lemma 4'(a).
- The `N^-` factor uses the same cancellations with the verified Lemma 4'(b); it was not separately
  brute-forced.

*What Lemma 6 is not.* (6.1)–(6.2) are **not** product formulas: the sum over `l in L^#` is global, and the
local factors only weight congruence classes of `l`. Nor is the grouping a demonstrated saving:
it replaces the 145,536-cusp double sum by a single sum over the dual lattice, but that sum is not
smaller. `S_q` vanishes on some congruence classes (at 4547: `v in {-2, 0}` only; at 2: `v in {-3, -1, 0}`
only), yet the retained part of `L^#` has positive density. By (6.2) and the decay of `W_B`, the
effective range is `Q(l) <= X_0` for a constant `X_0` fixed by the precision. The dual lattice has Gram
determinant `N^{-2}`, so the MODEL count is `2 pi^2 X_0^2 N ≈ 1.28e17 * X_0^2` vectors **per Gross pair**
(continuous volume, not a lattice-point count or bound). This is the same scale as the first run's
model.

## 7. Truncation, error and resources — proved statements vs. models

**Proved (this file):**
- (6.2) is exact, and every ingredient is explicit (`eps_2 = eps_2' = +1` by `04`): the dual lattice
  `L(P,Q)^#`, `Q`, the local coordinates, `a_m(f)`, the local factors `S_q` (closed forms), and `W_B`
  (an explicit contour integral).
- `W_B(x) = O_A(x^{-A})` for every `A` (contour shift). With `|a_m/m| <= tau(m) m^{-1/2}` (Deligne) and
  bounded `|S_q|`, the tail of (6.2) over `Q(l) > X` is controlled by an explicit multiple of
  `sum_{Q(l) > X} tau(m(l)) m(l)^{-1/2} |W_B(Q(l))|`. A **certified** tail bound additionally needs
  (i) explicit constants for `W_B` (computable by rigorous quadrature) and (ii) a proved
  lattice-point count for `L^#` in shells (a standard Gauss-circle-type estimate). Neither was
  carried out: *certified truncation is not established here*.
- `I(F_f) = <f,f>` has the same shape with local factors `S_q^{ff}(xi) = sum_{A_q} w_{A_q} |W_q(...)|^2`, which
  do **not** involve `eps_2, eps_2'` (only `|.|^2`).

**MODEL only (continuous volumes and square-root conductors; not bounds, not measurements):**

| item | model size | basis |
|---|---|---|
| dual vectors per Gross pair with `Q(l) <= X_0` | `2 pi^2 X_0^2 N ≈ 1.28e17 X_0^2` | Gram det of `L^#` is `N^{-2}` |
| Gross pairs | `p(p-eps)(p(p-eps)+1)/2` (465 at `p = 5`) | exact |
| Hecke eigenvalues needed | `a_m(f)` for `m <= X_0 N ≈ 6.5e15 X_0` | `m(l) <= N Q(l)` |
| local tables | `O(4547^2) = 2.1e7` field ops for `jhat`; `O(1)` per vector for `S_2`, `S_{N^-}` | exact counts |
| `<f,f>` by the same method | same scale (`~N` terms); via `L(Sym^2 f)`: `~1.4e12` (sqrt-conductor) | model |

Against the allowances: the coefficient range alone (`~10^16`) requires the seed's coefficient
corpus far beyond anything present here, and extending it is not authorized. The lattice
enumeration exceeds the class-set size `|X| = 5.4e14` by more than two orders of magnitude per
pair in the model. The 2 CPU-hour cap is exceeded by many orders of magnitude. **No evaluation of
(6.2) at the seed was attempted.**

**Arithmetic scale (separate obligation, unchanged):** (6.2) yields the real number
`lambda_f(G) = psi(x)psi(y)/M`. A residue mod `p` still needs (INT_p) (`p ∤ M`) **and** a proved
denominator/height bound (or an exact arithmetic implementation). `M` is unknown. The
analytic formula is therefore not an arithmetic evaluator.

## 8. Conditional small comparison: not started

`PILOT_IF_FORMULA.md` becomes appropriate only after "an explicit kernel formula with the exact
line and global integrality is supplied and independently reviewed". Global integrality needs
`p ∤ M`, which is unknown. The formula here (with both 2-adic signs now determined in `04`) has
not been independently reviewed. The gate is therefore **not met**, and no pilot was run. A small
comparison would also need a small level reproducing the seed's features: an exceptional prime
of conductor exponent 3 and a depth-zero prime of exponent 2, together with a Brandt computation.
That is a separate construction, not undertaken.

## 9. Continuation status: `EXPLICIT_AGGREGATE_PROVED`

(Revised after `04`. The first version of this section, at `0f6d4df`, had `PARTIAL_LOCAL_FORMULA_PROVED`
with the two 2-adic signs as the first unresolved step.)

**Derived and proved** (standard imports named in place; Nelson's text not read):
- Lemma 1: the exact coset/cusp/width bookkeeping (index `mu_N = 13,017,263,840,621,568`, 145,536
  cusps, widths per local class).
- Lemma 2: Parseval per cusp.
- Lemma 3: an explicit integration identity by tracing to `SL_2(Z)` (kernel `K_B`).
- Lemmas 4, 4': the norm-theta series at every cusp, with closed-form local Gauss sums.
- Lemma 5a: the newform at every cusp as a product of local Whittaker values, with all local
  signs at `3, 2243, 5843, 4547` (§5.2).
- Lemma 5b: the explicit depth-zero Bessel factor at the 4546 non-Atkin–Lehner cusps of 4547.
- Lemma 5c: the Jacquet–Langlands intermediate-cusp formula, giving the prime-2 table.
- Lemma 6: the grouped aggregate (6.1) and integral (6.2), with explicit local factors `S_q`.
- `04` (Lemma 7, Prop. 7'): the two 2-adic signs `eps_2 = eps_2' = +1`.

**Result:** `C_G(y)` and `lambda_f(G) = I(F_G)/I(F_f)` are explicit in three kinds of data, with **no
unevaluated local parameter left**:
- the Fourier coefficients of `f`;
- the dual-lattice data of `L(P,Q)^#`;
- finite local factors at every `q | N`.

The 4547 factor is complete: `pi_4547` is uniquely determined by `e = 4`, `q ≡ 3 (mod 4)` and trivial
central character. At 2 the data are `a' = 4` (Tate's algorithm) and `eps_2 = eps_2' = +1` (`04`).
The two signs are graded PROVED modulo the imports named in `04` §2: Greenberg–Wiles,
Cassels–Tate, and the 2-parity theorem for Selmer coranks. They rest on two independent
exact local computations and a 160-curve numerical validation of the method. As the packet
specifies, this status asserts no global integrality, affordable evaluation, certified
truncation or seed nonvanishing.

**First unresolved step (now):** a certified evaluation of (6.2). The first item is certified
truncation: explicit constants for `W_B` and a proved dual-lattice shell count (§7). After that
comes the evaluation itself. By MODEL (§7) it needs `a_m(f)` for `m` up to `~10^16` and `~10^17`
dual vectors per Gross pair. That is far beyond the class-set size and all allowances of this run,
so it was not attempted.

**Separate obligation:** the arithmetic scale `p ∤ M` plus a denominator/height bound. Without it
the real output is not a residue mod `p`.

**Endpoint implication:** none new. No kernel value, `M_2(p)`, or `Sha` statement was evaluated at
any prime. The retained fixed-prime forward bridge is unchanged. This is an analytic formula,
not an arithmetic certificate, and has no measured cost advantage. No conclusion about FIN,
ORDER9 or Q36 follows.
