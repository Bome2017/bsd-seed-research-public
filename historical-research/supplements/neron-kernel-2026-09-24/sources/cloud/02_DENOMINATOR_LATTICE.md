# Phase 2 — explicit reconstruction lattice for the normalized scalar

Phase 1 passed (`01_NORMALIZATION_REVIEW.md`), so this construction is admitted.

**Target.** An explicit `B` with `B · K_E(G) ∈ Z` for the integral theta cusp forms of the weighted
packet, `G = Theta(z,z)` (and generally `G = Theta(z,w)`), where:
- `z, w ∈ Z[X]` and `deg z = 0`;
- `K_E(G) := (4 pi^2/A_E) P_G = (ed/c_E^2) lambda_f(G)` (Phase 1, (1.1)).

**Result.**

    D0 · omega_G ∈ H^0(J_0(N)^Neron, Omega^1)  with  D0 = 2 · 4547,

and consequently

    2^10 · 4547 · K_E(G) ∈ Z,   in particular   2^17 · 4547 · K_E(G) ∈ Z  (the join form, b = 1).

`b = 1` at 4547 is an upper bound. Its sharpness was not investigated.

## 1. The retained 2-local join: checked, objects match

Appendix `F_lattice_proof.tex` §"Reduction to an integral differential lattice" fixes
- `R = Z_(2)` and `S = S_2(Gamma_0(N), R)`, the **whole** lattice of forms integral at `infty`;
- `H = H^0(X_0(N)_R, omega_{X/R})`,

and proves `2^8 S ⊆ H`.

**H is the Néron lattice.** The identification uses CNS Thm 6.12(c) and Prop 6.2, checked in the
offline text:
- 6.12(c): `X_0(N)_{Z_(2)}` has rational singularities when `p = 2` and some `p' | N` has `p' ≡ 3 (mod 4)`.
  Here `p' = 3` qualifies.
- Prop 6.2: `H^0(J^Neron, Omega^1) ⊆ H^0(X, Omega)`, with equality iff the singularities are rational.
  It applies to `X_0(N)_{Z_(p)}` by Example 6.3.

**The estimate.** `e' <= 8` rests on the listed Katz–Mazur/adjunction imports. The appendix and
`SECOND_REVIEW.md` state that these were not independently replayed; that grade is kept.

**Consequence.** For every `G ∈ S_2(Gamma_0(N), Z)`, `2^8 omega_G ∈ H`. By §4 below this gives
`v_2(K_E(G)) >= -8 - v_2(c_E) >= -17`.

**Mismatch search.** None found. `S` is the whole integral-at-`infty` lattice, not the `f`-line. `H` is
the Néron lattice at 2. `c_E | 2^9` refers to the same chosen map `phi_E`.

## 2. Lemma N1 — the packet forms are integral cusp forms at every cusp

Let `L = L(x,y)` with `Theta_{x,y} = theta_L/2`. `L` is even, positive, of rank 4 and Gram determinant `N^2`,
and is locally `(O_q, u_q nrd)`.

- **Constant terms.** By `work/03_NELSON_CONTINUATION.md` Lemma 4, the constant term of
  `Theta_{x,y} |_2 gamma` at `gamma = [[a,b],[c,d]]` (`c >= 1`) is `-(1/(2 N c^2)) Gs(a,0;c)`, since only `l = 0` has `Q(l) = 0`.
  - By Lemma 4', `Gs(a,0;c) = prod_{q|c} Gs_q(0)`, where `Gs_q(0) = q^{3 v_q(c)}` (Eichler) or `-q^3` (division).
    This is **independent of the pair `(x,y)`**, since the local unit `u_q` drops out at `l = 0`.
  - Hence the constant term of `Theta(z,w) = sum z_x w_y Theta_{x,y}` at every cusp `a/c` is
    `-(1/(2Nc^2)) Gs(a,0;c) deg(z) deg(w)`. At `infty` it is `deg(z)deg(w)/2`.
  - So `deg z = 0` makes `Theta(z,w)` cuspidal at **every** cusp.
  - This is a direct proof from the explicit expansions, not merely vanishing at `infty`. It agrees with the
    retained Eisenstein statement (`context/01_THETA_KERNEL.md` §2: the constant vector is the only
    Eisenstein vector).
- **Integrality at infinity.** For `n >= 1` the coefficient of `q^n` in `Theta_{x,y}` is `#{b : Q(b) = n}/2 ∈ Z`, pairing `b`
  with `-b`. So `Theta(z,w) ∈ S_2(Gamma_0(N), Z)`, and in particular `k_G = r lambda_f(G) ∈ Z`.

## 3. Lemma N2 — p-adic size of theta expansions at every cusp

Let `p | N`, `n := v_p(N)`, and let the cusp be `a/c` with `c | N` (CNS denominator `L = c`) and `e := v_p(c)`.

> **Lemma N2.** Every Fourier coefficient `a_G(m; gamma)` of `G = Theta(z,w)`, with `m >= 1` (CNS (4.2.1)–(4.2.2),
> same slash normalization `(cz+d)^{-2} G(gamma z)`), satisfies
>
>     val_p(a_G(m; gamma)) >= e - n   if p | N^+,      val_p(a_G(m; gamma)) >= e - 1   if p | N^-.

*Proof.* By Lemma 4,
`a_G(m;gamma) = -(1/(2Nc^2)) sum_{x,y} z_x w_y sum_{l ∈ L(x,y)^#, Q(l) = m/w} Gs(a,l;c) e(dQ(l)/c)`.

- The summands for `l` and `-l` coincide, because `Gs(a,-l;c) = Gs(a,l;c)` (substitute `r -> -r`) and `Q(-l) = Q(l)`.
  So the factor `1/2` cancels against pairing.
- `val_p(1/(Nc^2)) = -n - 2e`.
- `Gs(a,l;c) = prod_{q|c} Gs_q(l)`. By Lemma 4', `Gs_p(l) = p^{3e}·(root of unity or 0)` if `p | N^+` (`e <= n`), and
  `-p^3·(root of unity or 0)` if `p | N^-` (`e <= 1`).
- For `q ≠ p`, `Gs_q(l)` is a `p`-adic unit or 0, and `e(dQ(l)/c)` is a root of unity.
- A finite sum of terms of valuation `>= -n - 2e + 3e` has valuation `>= e - n`. ∎

*Checks of the input.*
- Lemma 4 was numerically compared with direct summation (prefactor `-1/(sqrt(det) c^2)`, `det = N^2`).
- Lemma 4'(a) was enumerated at levels `2^3, 3^2, 5` (`work/scripts/lemma4b_local_gauss_check.py`). It was
  checked again here by brute force at levels `5^2, 7^2, 11^2` (`e = 1`) and `5^2` (`e = 2`):
  166 random cases, max abs. difference `2.7e-8` (`output/scripts/gauss_level_p2_check.py`,
  `output/gauss_level_p2_check_output.json`, 1.1 CPU s).

## 4. Proposition N3 — `D0 = 2·4547` puts every packet differential in the Néron lattice

**Import:** CNS Prop 5.14. Statement read in the offline text; its thresholds were re-derived from
(5.9.1) and (5.12.1): `d(a,b)/e(a,b) = b - 1/(p-1)` for `a, b >= 1`. It says that
`omega_G ∈ H^0(X_0(N)_{Z_p}, Omega)` iff, for each `ell = 0..n` and some cusp with `v_p(L) = ell`,

    val_p(G|_c) >= -n (ell = 0),   >= -(n-ell) + 1/(p-1) (0 < ell < n),   >= 0 (ell = n).

Comparison with Lemma N2 (`ell = e`):

| prime | `n` | `ell = 0` | `0 < ell < n` | `ell = n` | smallest `t` with `p^t omega_G` regular |
|---|---|---|---|---|---|
| `p ∤ N` | 0 | — | — | `>= 0` at `infty` ✓ | 0 |
| `q ∈ {3,2243,5843}` | 1 | `>= -1` ✓ | — | `>= 0` ✓ | 0 |
| 2 | 3 | `>= -3` ✓ | `>= e-3`, need `e-2` | `>= 0` ✓ | **1** |
| 4547 | 2 | `>= -2` ✓ | `>= -1`, need `-1 + 1/4546` | `>= 0` ✓ | **1** |

At the intermediate components (Katz–Mazur `(1,1)` at 4547, multiplicity `phi(4547) = 4546`), the bound is short
by exactly `1/(p-1)`. One factor of `p` suffices.

**Rational singularities** (CNS Thm 6.12, checked):
- (a) all `p >= 5`, including 4547, 2243, 5843;
- (b) `p = 3`, `v_3(N) = 1 <= 2`;
- (c) `p = 2`, since `3 | N` with `3 ≡ 3 (mod 4)`.

So Prop 6.2 gives `H^0(X_0(N)_{Z_(p)}, Omega) = H^0(J_0(N)^Neron_{Z_(p)}, Omega^1)` at every prime. The lattices are
compatible with completion (flat base change, `M = (M ⊗ Z_p) ∩ (M ⊗ Q)`).

> **Proposition N3.** For all `z, w ∈ Z[X]` with `deg z = 0`,
> `2 · 4547 · omega_{Theta(z,w)} ∈ H^0(J_0(N)^Neron, Omega^1)`.
> Thus PROOF.md (12) holds for the packet's theta forms with **`D0 = 9094 = 2·4547`**.

This is a statement about theta forms. It is not an inclusion of the whole lattice `S`: for an
arbitrary integral cusp form the expansions at the other cusps are not controlled by N2. The
normalized-newform theorem (CNS 5.15) is not used.

## 5. Theorem N4 — the reconstruction lattice

**Setup.** `i_E : E -> J_0(N)` is the dual of `pi_E = psi ∘ pi` (`psi = id` if `E = E_0`), and `pi_E ∘ i_E = [ed]`.
- Hecke equivariance: `T_l` is Rosati-invariant for `l ∤ N`, and the `f`-eigenspace is one-dimensional.
  Together these give `i_E^* omega_G = lambda_f(G)(ed/c_E) omega_E`: `i_E^*` kills `f^perp`, and
  `i_E^* pi_E^* omega_E = ed omega_E` with `pi_E^* omega_E = c_E omega_f`.
- `i_E` extends to Néron models, and `H^0(E^Neron, Omega^1) = Z omega_E`, where `omega_E` is the Néron
  differential (A.1(i)).

Hence `D0 · (ed/c_E) lambda_f(G) ∈ Z`, i.e.

    D0 · c_E · K_E(G) ∈ Z.                                        (13)

> **Theorem N4.** For `G = Theta(z,w)` with `z, w ∈ Z[X]` and `deg z = 0`, in particular `G = Theta(z,z)` for the
> lifted weighted packet:
>
>     B_theta := 2^10 · 4547 = 4,656,128  satisfies  B_theta · K_E(G) ∈ Z,
>
> using `c_E | 2^9`. The join form requested by the task also holds:
> `B_join := 2^17 · 4547^b = 595,984,384` with `b = 1`.
> - 2-part: retained `2^8 S ⊆ H` and `c_E | 2^9`.
> - 4547-part: N3; `c_E` is a 4547-unit.
> - Other primes: N3. Independently, ARS gives `v_q(r) = v_q(d)` for `q^2 ∤ N` and `k_G ∈ Z` (N1), so the
>   denominator of `K_E = e k_G/(c_E^2 s)` has support in `{2, 4547}`.
>
> `B_theta | B_join`.

*Cross-check of the two routes.* Both agree at 4547 (exponent 1) and at all odd `q ≠ 4547` (exponent 0).
At 2, the theta route (CNS 5.14 at `p = 2` + N2) gives `v_2(K_E) >= -1 - v_2(c_E) >= -10`. The join route (whole lattice)
gives `>= -17`. The join route does not use N2 at 2; the theta route does not use the retained `e' <= 8` estimate. Both
use the retained `c_E | 2^9`, which itself depends on that estimate through `c_0 | 2^8`.

**Unit test at a good prime.** For `p >= 5`, `p ∤ N`, `p ∤ B`. By Phase 1, `K_E(z,z) ∈ Z_p^x` iff
`psi(z) ≢ 0 (mod p)`, and `B·K_E(z,z)` is an integer.

## 6. Size and precision

| denominator | value | bit length | radius on `K_E` for exact identification of `B·K_E` |
|---|---|---|---|
| `B_theta = 2^10·4547` | 4,656,128 | 23 (`log2 = 22.15`) | `< 1/(2B) = 1.0739e-7` |
| `B_join = 2^17·4547` | 595,984,384 | 30 (`log2 = 29.15`) | `< 1/(2B) = 8.389e-10` |

**Interval rule.** A certified real enclosure of `K_E(z,z)` of radius below `1/(2B)` contains at most one
point of `B^{-1} Z`. Membership is guaranteed by N4. Rounding `B·K_E` then yields the integer, and the
`p`-unit test reads `p ∤ B·K_E` (valid since `p ∤ B`). A larger radius needs a different argument:
excluding every multiple of `p` from the scaled interval.

**Not applicable to the toy curve.** The toy interval `[2.999999500626, 3.000000499374]` belongs to the toy
curve `E_0` of the packet (`a2 = -11`, `a4 = -44`), not the seed. Neither `B` transfers to it without redoing
N2–N4 for its level. No value is rounded here.

## 7. Dependencies and grades

| input | grade |
|---|---|
| CNS Prop 5.14, Thm 6.12(a)(b)(c), Prop 6.2, Ex. 6.3 | published theorems, statements read offline, thresholds re-derived; proofs not replayed |
| `03` Lemma 4 (theta at cusps via Poisson) | written proof + numerical check (prior lab work) |
| `03` Lemma 4' (local Gauss sums) | written proof + enumeration (levels `2^3,3^2,5`; here `5^2,7^2,11^2`) |
| N1–N3, Theorem N4 algebra, Néron pullback, Hecke equivariance | replayed here |
| `c_E | 2^9`, chosen map, `e ∈ {1,2}` | retained (appendix / A.4), geometric grade unchanged |
| `2^8 S ⊆ H` at 2 (join route only) | retained written proof with named geometric imports |
| ARS Thm 2.1 (support cross-check only) | published theorem |

**What this does not do.**
- It evaluates no seed kernel value and gives no seed interval or witness.
- It supplies no `M`, `d`, `r` or `s`.
- It does not reduce the pair-enumeration cost.
- It neither uses nor supports ARS Conjecture 2.2 or Manin's conjecture.
- It claims no FIN, ORDER9 or Q36.
