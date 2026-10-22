# Independent Shii-to-seed control attempt

Date: 2026-10-11. Baseline lab `9793ff7bddd1214afe5d3567beeb27f1d59a0fc8`.

Grade: written deductions under the retained full residual image and Shii hypotheses; algebraic countercontrols, not seed realizations. No new primary value or uniform bound is established.

## Source actually used

Shii, arXiv:2503.09034v1, Theorem 1.2, Proposition 2.3, equations (2.9)–(2.14), plus the signed local conditions in §3. ARK, arXiv:2605.29783v2, Theorems A–C and finite group-ring invariant definitions. Primary HTML is in the previous source-delta private cache, hashes in its bindings. The retained `DEFINITE_THETA_ORDER.md` was read before interpreting any quadratic coefficient.

Fix a prime on the verified Shii seed domain and write

\[
R_n=\mathbf Z_p[G_n]=\mathbf Z_p[T]/((1+T)^{p^n}-1),\quad
\mathfrak m=(p,T),\quad
M_n=\operatorname{Sel}_{p^\infty}(E/K_n)^\vee.
\]

The actual published input is

\[
\theta_n\iota(\theta_n)\in\operatorname{Fitt}_{R_n,0}(M_n),\qquad
\iota(T)=-T/(1+T).
\]

The source contains the product of two theta elements, not the square-root theta in a Fitting ideal.

## 1. A direct finite-level implication, with no Tor cancellation

For a finitely generated module over a local ring, if its minimal number of generators is r, every maximal minor of a minimal presentation belongs to `m^r`. Hence

\[
f\in\operatorname{Fitt}_{R_n,0}(M_n),\quad f\notin\mathfrak m^{r+1}
\quad\Longrightarrow\quad
\dim_{\mathbf F_p}M_n/\mathfrak mM_n\le r.
\]

For the seed, `E(K_n)[p]=0`. Indeed, a nonzero vector in `E[p]` has orbit of size `p^2-1` under the retained full GL2 image. Its field of definition would have degree `p^2-1` dividing `[K_n:Q]=2p^n`, impossible for p≥5. Thus `E(K_n)[p^infinity]=0` as well.

Inflation–restriction consequently injects the seed's discrete p-primary Selmer group into the `G_n`-invariants of the Selmer group over `K_n` (first restrict to K, then K_n; the quadratic degree is prime to p). On p-torsion and dualizing,

\[
\dim_{\mathbf F_p}\operatorname{Sel}_{p^\infty}(E/\mathbf Q)[p]
\le \dim_{\mathbf F_p}M_n/(p,T)M_n.
\]

Therefore a Fitting element outside `m^3` would force the seed's Selmer dimension to be at most two. The known Kummer plane already has dimension two, so this gives `Sha[p]=0` and then `Sha[p^infinity]=0`.

In particular, for n≥1, if

\[
\theta_n\in(T),\qquad [T]\theta_n\in\mathbf Z_p^\times,
\]

then `theta_n iota(theta_n) = -u^2 T^2 mod m^3`, outside `m^3`, and the implication applies. The term `T^2` is nonzero in `gr_m^2 R_n` for p≥5: at n=1 the lowest group-ring relation is `pT`, and at n≥2 its degree is at least three.

**This is a sufficient criterion, not a proved arithmetic trigger. It is not the project's degree-two theta witness.** A degree-two theta coefficient produces degree four on the Fitting side.

## 2. The raw first-order trigger is unavailable at layers n≥2

This exclusion is a deduction using the actual seed points, not a speculative period argument.

The injection above and the two rational point directions imply that `M_n/TM_n` has Zp-rank at least two. Fitting ideals commute with base change, and a positive-rank Zp-module has zeroth Fitting ideal zero. Applying augmentation to the published inclusion gives

\[
\operatorname{aug}(\theta_n)^2=0,
\qquad\text{hence}\qquad\operatorname{aug}(\theta_n)=0.
\]

This proves augmentation vanishing without assuming primary Sha finiteness or using a nonzero interpolation factor.

Shii Proposition 2.3 gives the **integral** factorization

\[
\theta_n=C_n Q_n,
\]

where `C_n` is the product of opposite-parity cyclotomic factors `Phi_{p^j}(1+T)`. The quotient Q_n is defined in the stated quotient ring, whose relation has a factor T, so its augmentation is well-defined. Every factor has augmentation p; thus `aug(C_n)=p^{s_n}` is nonzero. It follows that `aug(Q_n)=0` as well.

Each cyclotomic factor belongs to m, while Q_n belongs to (T). Consequently

\[
\theta_n\in\mathfrak m^{s_n+1}.
\]

For even n, `s_n=n/2`; for odd n, `s_n=(n-1)/2`. Thus `s_n>=1` for every n≥2, so **every such raw theta belongs to m²** and cannot pass the first-order test of §1. The first layer n=1 has no opposite-parity factor. The recurrence alone does not decide its linear coefficient, but the separate finite-level inversion calculation in §2a below rules out a unit linear term there as well. This uses the raw spherical vector, not an ordinary order-of-vanishing theorem.

This is why moving to a deeper raw theta layer does not repair the missing seed upper bound. Removing C_n inside a group ring does not authorize canceling its product out of the Fitting inclusion.


## 2a. The first layer is ruled out too: raw theta inversion has positive sign

**Grade: written deduction from the finite Gross-point/Atkin–Lehner calculation, with the retained seed root number.** This is not an invocation of an ordinary Iwasawa theorem at a supersingular prime.

The additional primary source is Chida–Hsieh, *Special values of anticyclotomic L-functions for modular forms*, author PDF dated January 5, 2016, equations (2.1), (2.7), Lemma 3.7 and the finite-level proof of Theorem 4.8 on printed p.23:

https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf

Its introduction's Theorem B has sign `epsilon_p(f) epsilon(f)`. Its integral inverse-limit construction has an ordinary hypothesis. **That inverse-limit theorem is not imported here.** Instead, use the same finite Gross-point inversion on the raw, unregularized weight-two quaternionic form used by Shii/DI. The only potentially problematic place for this change is p, where the raw vector is spherical.

Here is that place's computation explicitly. The source labels points by ring conductor p^n; Shii/DI project conductor p^(n+1) points to the degree-p^n layer. Replacing n by n+1 below leaves the calculation and sign unchanged. In the source's notation, put `h=Tr(theta)` and suppress the scalar `sqrt(beta)`, which is a p-adic unit. For inert p, the displayed choices are

\[
J/\sqrt\beta=\begin{pmatrix}-1&h\\0&1\end{pmatrix},\qquad
s_n=\begin{pmatrix}0&1\\-p^n&0\end{pmatrix}.
\]

Therefore

\[
s_n^{-1}(J/\sqrt\beta)s_n
=\begin{pmatrix}1&0\\-p^nh&-1\end{pmatrix}
\in\operatorname{GL}_2(\mathbf Z_p).
\]

The raw good-p spherical vector is fixed by this matrix. **No division by a unit U_p-eigenvalue, ordinary filtration, or p-stabilization occurs.** The other local computations in the finite inversion proof are unchanged: Lemma 3.7 supplies the split bad-prime Atkin–Lehner factors and reciprocity translate. At an inert prime dividing the squarefree N-minus, the one-dimensional quaternionic representation contributes `a_q=-epsilon_q(f)`; there are an odd number of these primes. At infinity the weight-two quaternionic coefficient representation is trivial. Their combined sign is therefore the usual global root number, with the good-p factor `epsilon_p=1`.

It follows for the raw finite theta, after projection to the anticyclotomic p-group, that

\[
\iota(\theta_n)=\epsilon(E)\,\sigma_n\theta_n,
\qquad \sigma_n\in G_n.
\]

In the displayed Chida–Hsieh orientation the translate is the image of `N-plus` inverted. Changing the Gross point, the compatible path or the reciprocity orientation changes this translate, not its augmentation or the sign. The primitive quaternionic generator's sign also does not affect the identity. This is why this zero-coefficient test does not require identifying an unknown p-adic period unit between the two presentations. The DI vertex construction and the adelic construction evaluate the same weight-two quaternionic newvector on the Gross-point torsor; for the present class-number-one K, the choices are related by the torsor translations just described.

For the seed, the retained root number is `epsilon(E)=+1`. Section 2 already proved `aug(theta_n)=0`, so theta_n belongs to the augmentation ideal I. Modulo I², inversion acts as multiplication by −1, whereas multiplication by a group element acts as +1. Hence

\[
-\theta_n=\theta_n\quad\text{in }I/I^2.
\]

Since p is odd and 2 is a unit, this forces

\[
\boxed{\theta_n\in I^2\quad\text{for every }n\ge1.}
\]

The finite-level qualification matters: `I/I² ≅ Z_p/p^n Z_p`; the statement is ideal membership, not an assertion that the coefficient of T in every arbitrary polynomial representative is literally zero in Zp. At n=1 it does imply that this coefficient is zero modulo p. Thus theta_1 lies in m², and its product with its involution lies in m⁴. The §1 first-order criterion cannot hold at n=1 either.

**Disposition:** there is no surviving raw first-order theta trigger for this seed on the present Shii domain. The linear criterion was useful for locating the missing control; it is not an admissible new computation or research campaign. This symmetry does not prove the quadratic coefficient is a unit or bound the excess quotient.

## 2b. Signed quotients: residual linear terms also vanish

Retain Shii's exact integral factorization `theta_n=C_n Q_n`. Write

\[
F_n=\gamma^{p^n}-1=C_nH_n,\qquad d_n=\deg C_n.
\]

Every cyclotomic factor is reciprocal, so

\[
\iota(C_n)=\gamma^{-d_n}C_n.
\]

Multiplication by C_n is an injection `Lambda/(H_n) -> Lambda/(F_n)`: cancellation is performed in the domain Lambda before passing to its indicated quotient. This is the integral quotient isomorphism underlying uniqueness of Q_n, **not cancellation of a scalar from a Fitting ideal**. The ideal (H_n) is stable under inversion. The raw functional equation `iota(theta_n)=sigma_n theta_n` therefore gives

\[
\iota(Q_n)=\gamma^{d_n}\sigma_nQ_n
\quad\text{in }\Lambda/(H_n).
\]

Section 2 already established the exact equality `Q_n(0)=0`. For positive even n (the plus quotient) or odd n (the minus quotient), H_n modulo p is a power of T of degree at least p. Thus for p≥5 there is no quotient relation affecting degrees zero, one or two modulo p. Write

\[
Q_n=a_nT+b_nT^2\pmod{(p,T^3)}.
\]

The linear coefficient of the involuted expression is −a_n; on the right it is a_n, since the multiplying group element has augmentation one. Consequently 2a_n=0, and

\[
\boxed{Q_n\equiv b_nT^2\pmod{(p,T^3)}.}
\]

The additional alternating signs used to normalize Shii's compatible signed theta elements do not change this conclusion. Accordingly, each signed theta's residual quadratic jet contains only its quadratic coefficient. This is a reduction of the correct source data, not a nonvanishing proof for b_n. In particular, it supplies no additional rank bound beyond the product/Fitting limitation in §3.

No literal integral linear vanishing in an arbitrary finite polynomial representative is asserted. The statement proved and needed here is modulo p. Compatibility allows the same modulo-(p,T³) statement for the corresponding signed inverse-limit series whenever that series and its source matching have been supplied.

## 3. A quadratic theta coefficient does not give the required dimension bound

Over `R_n/p = F_p[T]/T^{p^n}`, a unit quadratic coefficient of theta makes the product have order four, provided the lower coefficients vanish. The reduced Fitting inclusion can at best force the length of `M_n/pM_n` to be at most four in this case. It does not force the seed's two additional possible directions to disappear.

There is a stronger explicit integral countercontrol. For any a≥1, set

\[
M_a=(R_n/(T))^2\oplus(R_n/(p^a,T))^2.
\]

Then

\[
\operatorname{Fitt}_{R_n,0}(M_a)
=(T)^2(p^a,T)^2
=(p^{2a}T^2,p^aT^3,T^4).
\]

Taking `theta=T²`,

\[
\theta\iota(\theta)=T^4/(1+T)^2
\in\operatorname{Fitt}_{R_n,0}(M_a).
\]

The theta has μ=0 and a unit quadratic coefficient. Nevertheless

\[
M_a/TM_a\cong\mathbf Z_p^2\oplus(\mathbf Z/p^a)^2.
\]

The finite piece has arbitrary even length 2a. Thus even primary finiteness, parity and a unit product leading coefficient do not extract its vanishing from this Fitting inclusion.

A separate divisible control is `(R_n/(T))^4`: its Fitting ideal is `(T^4)`, and the same theta is compatible with corank four rather than the known rank-two plane alone. This is the finite-level version of the already recorded A2a control; it is not a new seed counterexample.

### Complex conjugation does not fix this purely algebraic gap

Equip each summand of M_a with complex conjugation acting as +1. Since T acts as zero, the relation `c gamma c^{-1}=gamma^{-1}` is satisfied. The finite pair `(Z/p^a)^2` has its usual perfect alternating pairing, preserved by this action. Thus the extra pair may sit entirely in the + eigenspace, alongside the two rational point directions. The anticyclotomic involution and parity alone do not force it into the twist component.

This does not assert that M_a is realized by the seed or satisfies every arithmetic property of a genuine Euler system. It establishes the precise logical limit of the **Fitting inclusion plus theta order plus these symmetries**.

## 4. Character evaluation and descent do not remove the same issue

At a primitive p-power character, `T` specializes to `zeta-1`, not a unit. The module `(Z/p^a)^2` above, after character base change through `(p^a,T)`, still contributes a pair; a character value does not by itself distinguish the seed's trivial constituent from its necessary specialization errors.

For an auxiliary extension of degree prime to p, restriction is injective because corestriction followed by restriction multiplies by a p-unit. However, a **nontrivial character projector** of that prime-to-p group kills the restricted classes from the base: they lie in its trivial component. Bounds for a nontrivial twist therefore do not bound the original Sha unless a separate arithmetic relation ties the components together.

The character argument does not prohibit auxiliary-field methods generally. It prevents the specific inference that a favorable nontrivial character value is automatically an upper bound for the original excess.

## 5. What would change this calculation

A new upper-control input would have to do more than remove signed factors in the scalar. Examples of genuinely additional data are:

- an actual derived presentation removing the two known point directions **with all Tor and local terms tracked**, followed by an integral divisibility statement for that quotient;
- a bipartite Euler-system comparison controlling the + multiplicity separately, beyond its scalar Fitting consequence;
- a stronger arithmetic relation involving the quadratic or higher theta data and the known point lattice, with an actual integral upper-bound consequence.

None has been constructed in this check. The first-layer linear alternative has now been excluded by the raw theta symmetry in §2a; it should not be sent for computation. The existing degree-two theta witness cannot be silently relabelled as linear.

## Outcome

Derived here: exact seed augmentation vanishing from the finite-level Fitting theorem; the signed-factor lower bound for n≥2; the raw finite theta inversion calculation giving I²-membership also at n=1; the direct finite-level generator criterion; and explicit integral/dihedral countercontrols to the hoped-for quadratic shortcut.

No upper estimate on an actual theta coefficient or derivative content was proved. No new primary component, FIN, ORDER9 or Q36 is settled. This is a finite-level interface calculation identifying what a substantive new arithmetic comparison must supply.
