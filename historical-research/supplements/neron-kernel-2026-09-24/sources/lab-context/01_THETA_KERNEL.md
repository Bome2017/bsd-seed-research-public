# 01 — The definite norm/theta kernel and its exact projection to the seed line

Status of this file: written derivation. **Corrected 2026-09-24 in response to the
independent audit** (`work/AUDIT_RESPONSE.md`; original text in git history at `a38400a`).
Notation: `M := <psi,psi> = sum_x psi(x)^2`. Imported theorems are marked
**[import]** with the standard source; they are used at their published grade and are
not re-proved. Exact local data are produced by `work/scripts/local_data.py`
(output `work/local_data_output.json`).

## 0. Data and conventions

- `E : y^2 = x^3 + A x^2 + B x`, `A = -22735 = -5*4547`, `B = 106272484 = 2^2*4547*5843`,
  `A^2-4B = 3^2*2243*4547`, `Delta = 16 B^2 (A^2-4B) = 2^8*3^2*2243*4547^3*5843^2`,
  `c4 = 16(A^2-3B) = 2^4*43*1013*4547`, `N = 2^3*3*2243*4547^2*5843 = 6503188012738584`.
- `f = f_E in S_2(Gamma_0(N))` the newform; `a_n = a_n(f) in Z`.
- `K_0 = Q(sqrt(-7))`: 2 and 4547 split; 3, 2243, 5843 inert (Kronecker symbols computed).
- `B` = the definite quaternion algebra ramified exactly at `{3, 2243, 5843, infinity}`;
  `N^- = 3*2243*5843`, `N^+ = 2^3*4547^2`; `R` an Eichler order of level `N^+`
  (locally `R_q = [[Z_q, Z_q],[q^{a_q} Z_q, Z_q]]` for `q^{a_q} || N^+`).
- `X = B^x \ Bhat^x / Rhat^x`. For `x in Bhat^x` put `I_x = B ∩ x Rhat` (right `R`-ideal);
  `x -> [I_x]` identifies `X` with right ideal classes. `Gamma_x = B^x ∩ x Rhat^x x^{-1}`.

### 0.1 Local types (proof from the exact data)

*Primes `q | N^-`.* `q ∤ c4`, `v_q(N)=1`: multiplicative reduction, `pi_q` is an unramified
twist of Steinberg (discrete series), as Jacquet–Langlands requires at the ramified places.

*`q = 4547`.* `v_q(c4)=1`, `v_q(Delta)=3`, so reduction is additive, `v_q(j)=3-3=0 >= 0`
(potentially good), and the semistability defect is `e = 12/gcd(12,3) = 4`. For `q >= 5`
inertia acts on `V_l E` through a cyclic group of order 4 as `chi ⊕ chi^{-1}` with `chi` a
tame character of order 4. Frobenius acts on tame inertia by `t -> t^q`, and `q ≡ 3 (mod 4)`,
so it exchanges `chi` and `chi^q = chi^{-1}`: the Weil–Deligne representation is irreducible,
induced from the unramified quadratic extension. Hence `pi_4547` is the **depth-zero
supercuspidal** `c-Ind_{Z K}^{G}(sigma~)`, `K = GL_2(Z_q)`, `sigma` a cuspidal
representation of `GL_2(F_q)` of dimension `q-1 = 4546`, conductor exponent 2 (= `v_q(N)`).

*`q = 2`.* `v_2(N) = 3` is odd and the central character is trivial. A principal series
`pi(mu, mu^{-1})` has conductor exponent `2a(mu)`; `St ⊗ mu` with `mu^2=1` has exponent 1
(`mu` unramified) or `2a(mu) >= 4`. Hence **`pi_2` is supercuspidal**.

*Consequence (multiplicity one of the line).* At `q | N^+` the Eichler level equals the
conductor exponent (3 at 2, 2 at 4547), so **[import: Casselman]**
`dim pi_q^{K_0(q^{a_q})} = a_q - c(pi_q) + 1 = 1`. At `q | N^-` the JL transfer is a character
`chi_q ∘ nrd` with `chi_q` unramified, fixed by `R_q^x`. Hence the `f`-isotypic part of
`C[X]` is one-dimensional (Section 2).

### 0.2 Stabilizers are trivial; exact class number

Any `u in Gamma_x` other than `±1` generates `Z[i]` or `Z[zeta_3]` inside the Eichler order
`O_l(I_x)` (the only imaginary quadratic orders with extra units). Locally at `q = 4547`
this order is Eichler of level `q^2`. The units of the maximal order of an **unramified**
quadratic `Q_q`-algebra fix exactly one vertex of the Bruhat–Tits tree, so that order embeds
in no Eichler order of level `q^a`, `a >= 1`. Both `Q(i)` and `Q(sqrt(-3))` are inert at
4547 (`(-1/4547) = (-3/4547) = -1`, computed). Therefore

    Gamma_x = {±1}  for every x in X,   w_x := |Gamma_x|/2 = 1.

**[import: Eichler mass formula]** then gives the exact class number

    |X| = (1/12)(3-1)(2243-1)(5843-1) * (2^2*3) * (4547*4548) = 541,717,127,331,168.

(The same argument at `q = 2` — `Q(i)` ramified, level `2^3`; `Q(sqrt(-3))` inert — shows
the class set `X'` of level `2^3` and maximal at 4547 also has trivial stabilizers, so
`|X'| = 2*2242*5842 = 26,195,528`; used in §5.4.)

No stabilizer denominators occur anywhere below.

## 1. The theta expression

For `x, y in Bhat^x` put

    L(x,y) = B ∩ x Rhat y^{-1}   (= I_x I_y^{-1} = { b in B : b I_y ⊂ I_x }),
    n(x,y) = positive generator of nrd(x) nrd(y)^{-1} Zhat ∩ Q,
    Q_{x,y}(b) = nrd(b)/n(x,y)   (b in L(x,y)),

and define

    Theta_{x,y}(tau) = (1/|Gamma_y|) sum_{b in L(x,y)} q^{Q_{x,y}(b)}
                     = (1/2) sum_{b in L(x,y)} q^{Q_{x,y}(b)} = sum_{n>=0} B_{x,y}(n) q^n.

*Well defined on classes:* `L(g x k, y) = g L(x,y)` for `g in B^x`, `k in Rhat^x`, and
`nrd(g) > 0` scales `n(x,y)`, so `Q` is unchanged; likewise in `y`.

*Ideal/norm/stabilizer meaning:* `b -> b I_y` is a bijection from `{b : Q(b)=n}/Gamma_y` to
the right `R`-ideals `J ⊂ I_x` with `[J] = [I_y]` and `nrd(J) = n nrd(I_x)`. So `B(n)` is the
Brandt matrix, i.e. the matrix of the Hecke correspondence `T_n` on `Z[X]`, with weight
`1/|Gamma_y| = 1/2`; `B_{x,y}(0) = 1/2`, and `B(1) = Id` because a norm-preserving `b` gives
`I_x = b I_y`, and `Gamma_x = {±1}`.

*Level.* `(L(x,y), Q_{x,y})` is an even positive quaternary lattice (bilinear form
`trd(b b'^bar)/n(x,y)`). Locally it is `alpha R_q beta^{-1}` with norm scaled by a unit
`u_q`; since `nrd(R_q^x) = Z_q^x`, it is isometric to `(R_q, nrd)`. The norm form of an Eichler
order of level `N^+` in `B` has determinant `N^2` and level `N` (locally: dual lattice
`P_q^{-1}` at `q | N^-`; `[[Z_q, q^{-a}Z_q],[Z_q, Z_q]]` at `q^a || N^+`). **[import: theta series
of even quaternary lattices]** `Theta_{x,y} in M_2(Gamma_0(N))` with trivial character
(square determinant). Bilinearly, for `xi, eta in Z[X]`:

    Theta(xi, eta) = sum_{x,y} xi_x eta_y Theta_{x,y},   a_n(Theta(xi,eta)) = xi^T B(n) eta.

*Hecke equivariance.* **[import: Brandt-matrix Hecke relations for Eichler orders, Eichler
1973 / Pizer 1980]** for primes `l ∤ N`, `B(m)B(l) = B(ml) + l B(m/l)` and `B(l)` is
symmetric (all `w_x = 1`). Hence, with `T_l` the classical Hecke operator on `M_2(Gamma_0(N))`,

    T_l Theta(xi, eta) = Theta(T_l xi, eta) = Theta(xi, T_l eta).        (1.1)

(Coefficient check: `a_m(T_l Theta_{x,y}) = B(ml)_{xy} + l B(m/l)_{xy} = (B(m)B(l))_{xy}`.)

## 2. The primitive line

Let `T^(N) = Z[T_l : l ∤ N]` act on `Q[X]` by Brandt matrices; with `w ≡ 1` the pairing
`<xi,eta> = sum_x xi_x eta_x` is unimodular on `Z[X]` and every `T_l` is self-adjoint, so
distinct `T^(N)`-isotypic components are orthogonal. Functions and formal sums are
identified by this pairing, so `psi(z) = <z, psi>` for `z in Z_p[X]`.

**[import: Jacquet–Langlands + strong multiplicity one + §0.1]** the subspace of `Q[X]` on
which `T_l` acts by `a_l` for all `l ∤ N` is one-dimensional. Let `psi in Z[X]` be a primitive
generator (unique up to `±1`). For every `p`, `psi` is primitive in `Z_p[X]`, so the task's
`psi_p` is `psi` up to `Z_p^x`. (The constant vector is the only Eisenstein vector: `nrd`
maps `Rhat^x` onto `Zhat^x` and `Q` has class number one.)

Let `e_f^V` be the orthogonal projection of `Q[X]` onto `Q psi`:
`e_f^V(delta_x) = (psi(x)/<psi,psi>) psi`.

Let `lambda_f : M_2(Gamma_0(N)) -> C` be the coefficient of `f` for the decomposition of
`M_2(Gamma_0(N))` into `T^(N)`-isotypic components. **[import: Atkin–Lehner–Li newform theory,
strong multiplicity one]** the `a_l`-isotypic component is exactly `C f`: oldforms `g(d tau)`
carry the eigencharacter of a newform of smaller level, distinct newforms have distinct
eigencharacters, and Eisenstein eigenvalues have size `>= l-1 > 2 sqrt(l)` for `l >= 7`.
`T^(N)` acts semisimply, so `lambda_f` is well defined, and it is `Q`-rational.

## 3. Theorem A (exact line)

> **Theorem A.** For all `x, y in X`,
>
>     K(x,y) := lambda_f(Theta_{x,y}) = psi(x) psi(y) / M,   M := <psi,psi> = sum_{x in X} psi(x)^2 in Z_{>0}.
>
> Moreover `Theta(psi, psi) = <psi,psi> f` coefficient by coefficient; in particular
> `<psi, B(n) psi> = <psi,psi> a_n` for **every** `n >= 1`, including `n` divisible by 2, 4547,
> or a prime of `N^-`.

*Proof.* By (1.1), `Theta(., delta_y)` and `Theta(delta_x, .)` are `T^(N)`-equivariant maps
`Q[X] -> M_2(Gamma_0(N))`, so each carries an isotypic component into the component with
the same eigencharacter. Write `delta_x = e_f^V delta_x + r_x` with `r_x` in the sum of the
other components, similarly `delta_y`. Then
`Theta(delta_x, delta_y) = Theta(e delta_x, e delta_y) + Theta(e delta_x, r_y) + Theta(r_x, delta_y)`;
the last two terms lie in the sum of non-`f` components, the first in the `a_l`-isotypic
component `C f`. Hence

    lambda_f(Theta_{x,y}) f = (psi(x) psi(y) / <psi,psi>^2) Theta(psi, psi).

`Theta(psi,psi)` is `T^(N)`-eigen with eigencharacter `a_l`, so `Theta(psi,psi) = kappa f`,
and `kappa = a_1(Theta(psi,psi)) = psi^T B(1) psi = <psi,psi>` because `B(1) = Id`.
The coefficientwise identity is `Theta(psi,psi) = <psi,psi> f`. ∎

*Remarks.*
1. No local theta integral, test-vector constant or Petersson norm enters: the scale is
   fixed globally by `a_1` and `B(1) = Id`. The only local inputs are multiplicity one
   (§0.1) and trivial stabilizers (§0.2).
2. For `q in {2, 4547}`, the raw norm-count matrix `B(q)` is the operator of a bi-`Rhat^x`-invariant
   set supported at `q`, so it commutes with `T^(N)` (operators at distinct places commute) and
   `B(q) psi = mu psi`; the coefficientwise identity of Theorem A gives `mu M = M a_q(f) = 0`, i.e.
   `B(q) psi = 0`. This uses no identification of raw `B(q)` with a classical `U_q` on other
   (possibly old) constituents; such an identification can fail (`work/AUDIT_RESPONSE.md`, F2).
3. **Rank one.** `K = <psi,psi>^{-1} psi ⊗ psi` has rank one on the primitive line of the
   retained local types. It is not a sum over congruent eigensystems: `lambda_f` is a
   characteristic-zero projection, and congruences enter only through the scale (§4).
   Because `a_q = c(pi_q)` at `q | N^+`, it is not a sum over an oldform subspace either.
   If the Eichler level exceeded the conductor at some `q`, the same construction would
   produce the projection to an `(a_q - c_q + 1)`-dimensional oldform space: that is the
   precise failure mode the retained local types avoid.

### 3.1 Sufficient finite recognition theorem

`lambda_f` is defined by all `T_l`, not by finitely many tests. Any implementation that
isolates the line by Hecke tests must certify it by a theorem such as the following.

> **Proposition A'.** Let `phi in R[X]` be a common eigenvector of the Brandt matrices
> `B(n)` for all `1 <= n <= S_N := mu_N/6` (all `n`, including `(n,N) > 1`), with eigenvalue
> `a_n(f)`, where `mu_N = [SL_2(Z) : Gamma_0(N)]`. Then `phi in R psi`.

*Proof.* For a prime `l ∤ N`, `l <= S_N`, the constant vector `1` satisfies `B(l) 1 = (l+1) 1`
(each ideal has `l+1` sub-ideals of index `l`), `B(l)` is symmetric and `a_l != l+1`, so
`<phi, 1> = 0`. Put `F = Theta(phi,phi)`: `a_0(F) = <phi,1>^2/2 = 0` and
`a_n(F) = <phi, B(n) phi> = a_n(f) <phi,phi>` for `1 <= n <= S_N`. **[import: Sturm]**
`F - <phi,phi> f in M_2(Gamma_0(N))` has order `> S_N` at infinity, hence is 0. Write
`phi = c psi + r` with `r ⊥ psi`. By the equivariance used in Theorem A, `Theta(psi, r)`,
`Theta(r, psi)` and `Theta(r, r)` lie in the sum of non-`f` isotypic components, so
`c Theta(psi,r) + c Theta(r,psi) + Theta(r,r) = 0`. Its `q^1` coefficient is
`c<psi,r> + c<r,psi> + <r,r> = <r,r>` (as `B(1) = Id`), so `r = 0`. ∎

For this seed `mu_N = 13,017,263,840,621,568` (exact), so the sufficient test uses
`S_N = 2,169,543,973,436,928` indices. Proposition A' is a **sufficient** recognition theorem
only: no minimality is proved, and a proved generating set of the Hecke algebra or an exact
multiplicity certificate could use fewer tests. Matching a few eigenvalues without such a
theorem is not a proof of the line.

## 4. Theorem B (the integral scale is the order `M` of a lattice quotient)

> **Theorem B.** Let `p` be prime and `K = lambda_f ∘ Theta` as in Theorem A. Then
> `K(x,y) = c psi(x)psi(y)` with `c = <psi,psi>^{-1}`, and:
>
> 1. `K` is globally `p`-integral (every entry in `Z_(p)`) **iff** `p ∤ <psi,psi>`; in that
>    case `c in Z_p^x`, so integrality and the unit property of `c` coincide for this
>    kernel.
> 2. If `p ∤ <psi,psi>` then for every `z in Z_p[X]`, `K(z,z) = psi(z)^2/<psi,psi>`, so for
>    `z = z_p`:  `K(z_p,z_p) in Z_p^x  <=>  M_2(p) != 0`  (two-sided at such `p`).
> 3. `<psi,psi> = #C_psi`, `C_psi := Z[X] / (Z psi ⊕ (psi^⊥ ∩ Z[X])) ≅ Z/<psi,psi>`, and
>    `p | <psi,psi>` iff `psi ≡ phi (mod p)` for some `phi in psi^⊥ ∩ Z[X]`.
> 4. *(Prime-to-level only.)* If `p | M`, there is a characteristic-zero eigencharacter
>    `lambda_g != lambda_f` of the prime-to-level algebra `T^(N) = Z[T_l : l ∤ N]` occurring in
>    `(psi^⊥) ⊗ Q-bar_p`, congruent to `lambda_f` at every `T_l`, `l ∤ N`, modulo the maximal ideal of
>    `Z-bar_p`. For odd `p` it is cuspidal. Hence: **if `f` has no away-from-level mod-`p`
>    congruence with another constituent of the `N^-`-new part of `S_2(Gamma_0(N))`, then
>    `p ∤ M`.** No statement about the bad coefficients `a_n`, `(n, N) > 1`, of that constituent
>    is proved: raw norm-count matrices at bad primes are not identified with classical
>    `U_q` on old constituents.

*Proof.* (1) If `p ∤ <psi,psi>` the entries are `p`-integral. Conversely `psi` is primitive,
so some `psi(x_0)` is a `p`-unit and `K(x_0,x_0) = psi(x_0)^2/<psi,psi> ∉ Z_(p)` when
`p | <psi,psi>`. (2) `psi(z) = <z,psi>` and `M_2(p) = psi_p(z_p) mod p` with
`psi_p in Z_p^x psi`. (3) `Z[X]` is unimodular and `psi` primitive, so `u -> <u,psi>` maps
`Z[X]` onto `Z` with kernel `psi^⊥ ∩ Z[X]`, and the image of `Z psi ⊕ psi^⊥` is
`<psi,psi> Z`. If `<psi,psi> = pm`, pick `u` with `<u,psi> = 1` and put `phi = psi - p m u`;
then `phi ⊥ psi` and `phi ≡ psi`. Conversely `psi = phi + p lambda`, `phi ⊥ psi` gives
`<psi,psi> = p<lambda,psi>`. (4) `Lambda' = psi^⊥ ∩ Z[X]` is saturated. `T^(N)` is generated by the
commuting symmetric `B(l)`, `l ∤ N`, which fix `Q psi`, so `Lambda'` is `T^(N)`-stable. By (3),
`phi mod p = psi mod p` is a nonzero `T^(N)`-eigenvector in `Lambda'/p` with the reduction of
`lambda_f`. `Lambda' ⊗ Z_p` is finite free over a DVR with commuting endomorphisms, so
**[import: Deligne–Serre, Lemme 6.11]** lifts the eigenvalues (not necessarily the vector):
some eigencharacter `lambda_g` of `T^(N)` on `Lambda' ⊗ Q-bar_p` reduces to `lambda_f mod m`. It is not
`lambda_f` itself, because the `lambda_f`-isotypic part of `Q[X]` is `Q psi` and `Q psi ∩ psi^⊥ = 0`.
The only Eisenstein character on `Q[X]` is `l -> l+1` (the constant vector). It is excluded for
every odd `p`: `#E(F_5) = 8 = 1 + 5 - a_5` excludes all odd `p != 5`, and `#E(F_11) = 14` excludes
`p = 5` (each test prime differs from `p`; exact point counts in
`work/scripts/eisenstein_check.py` and the audit's independent check). By Jacquet–Langlands,
`lambda_g` is the prime-to-level eigencharacter of a cuspidal constituent of the `N^-`-new part. ∎

*What remains unsupplied.* `M = <psi,psi>` is the order of the **specified lattice quotient**
`Z[X]/(Z psi ⊕ Lambda')`. It is not identified here with a Hecke congruence ideal, a classical
congruence number, a modular degree or an integral Jacquet–Langlands comparison: even for a
positive unimodular lattice with self-adjoint Hecke action these can differ (audit countermodel
`psi = (1,1)`, `A = [[0,3],[3,0]]`, `T = Z[I,A]`: `M = 2` but the least `eta` with `eta e_+ in T` is 6).
Theorem B reduces global integrality of the unscaled kernel to the arithmetic input

    (INT_p)   p ∤ M,   sufficient: no away-from-level mod-p congruence between f and another
              constituent of the N^- -new part of S_2(Gamma_0(N)) (Theorem B(4)).

*Arithmetic reconstruction is a separate obligation.* Even under (INT_p), a **real** enclosure
of `K(z_p,z_p)` (e.g. from an analytic evaluation) is not a residue mod `p`: without a proved
denominator/height or discrete-lattice bound, `p`-adic units and non-units among `p`-integral
rationals are both dense in `R`. A mod-`p` certificate needs such a bound, or an independently
exact arithmetic implementation.

No value of `<psi,psi>` is known for the seed. (The project bibliography cites Agashe–Ribet–
Stein [ars] for the classical relation between congruence number and modular degree; that
relation, and any Ribet–Takahashi-type comparison of `<psi,psi>` with classical invariants
at a nonsquarefree `N^+`, were **not** checked in this session and are not used.)
An integral kernel exists without (INT_p): `e_f^V in T^(N) ⊗ Q` (it is a primitive idempotent of the
commutative semisimple algebra generated by the symmetric `B(l)`), so clearing denominators
gives a positive integer `eta` with `eta e_f^V` in the image of `T^(N)`; then
`<delta_x, eta e_f^V delta_y> = (eta/M) psi(x)psi(y)` is integral, and `M | eta` (since
`eta` kills `Z[X]/(Z psi ⊕ Lambda')`). No explicit construction of such an element, and no
bound on its support, is supplied (`02` §6.2).

## 5. What changes at the nonsquarefree primes 2 and 4547

5.1 **Line.** Supercuspidal at both primes, Eichler level = conductor, so the line is
exactly one-dimensional (§0.1). `B(q) psi = 0` for `q in {2, 4547}` (Remark 2). A larger
level at either prime would replace the line by an oldform space.

5.2 **Stabilizers.** The level `4547^2` alone forces `Gamma_x = {±1}` (§0.2); there are no
2- or 3-torsion stabilizer denominators, and `|X| = mass` exactly.

5.3 **Lattice level.** `Theta_{x,y}` has level `N = 6,503,188,012,738,584`, not squarefree.
`Gamma_0(N)` has `prod_q sum_{i<=a_q} phi(q^{min(i,a_q-i)}) = 4*2*2*2*4548 = 145,536` cusps.
The Atkin–Lehner group has order `2^5 = 32`, so there are at least `145,536/32 = 4,548`
Atkin–Lehner orbits of cusps (for squarefree level there would be one). The extra cusps have
denominators `2, 4` (2-part) and `4547` (4546 cusps). The expansion of `f` at them is not
`±f`: it is governed by the local Whittaker newvector of the supercuspidals at 2 and 4547
(epsilon factors of twists). This matters only for analytic realizations of `lambda_f`
(§6.3); Theorems A and B do not use it.

5.4 **Depth-zero type at 4547 (characteristic-zero dimension comparison).** Conjugating by `g = diag(1, q)`:
`g^{-1} K_0(q^2) g = K_T := { k in GL_2(Z_q) : k mod q is diagonal }`, which contains the
principal congruence subgroup `K(1)`. For the depth-zero supercuspidal, `pi^{K(1)} = sigma`
(Mackey: other double cosets contribute no `K(1)`-invariants because `sigma` is cuspidal), and
`sigma^{T(F_q)}` is one-dimensional (Kirillov model: torus-invariants with trivial central
character are the constants on `F_q^x`). Hence the `K_0(q^2)`-newvector is `pi(g) v_T` with `v_T`
spanning `sigma^{T(F_q)}`, and

    psi(x) = < Psi(x g_q), v_T >,   Psi : X' -> sigma,   Psi(x k) = sigma(k)^{-1} Psi(x)  (k in GL_2(Z_q)),

where `X'` is the class set of level `2^3` and maximal at 4547, `|X'| = 26,195,528`
(trivial stabilizers, §0.2). (Check of the direction: for `k in K_0(q^2)`,
`Psi(xkg) = Psi(xg * g^{-1}kg) = sigma(g^{-1}kg)^{-1} Psi(xg)` with `g^{-1}kg in K_T`, which fixes
`v_T`; e.g. `h = [[1,1],[0,1]]` has `g^{-1}hg = [[1,q],[0,1]] in K_T`, whereas `ghg^{-1}` has entry `1/q`.)
The complex dimension of the `sigma`-typed space containing `Psi` is
`|X'| (q-1) = 119,084,870,288`, versus `|X| = 541,717,127,331,168`; the exact ratio is
`q(q+1)/(q-1) = 4549 + 1/2273`. This is a **characteristic-zero dimension comparison only**:
it proves no runtime gain for any algorithm, and no primitive integral type projection or
integral normalization at a witness prime has been constructed. (A type at 2 changes the
local index `[GL_2(Z_2):K_0(8)] = 12` at most.)
