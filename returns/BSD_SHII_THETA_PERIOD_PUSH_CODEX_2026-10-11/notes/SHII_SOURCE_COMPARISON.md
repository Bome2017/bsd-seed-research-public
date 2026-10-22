# The actual supersingular theta source in one integral convention

Date: 2026-10-11. Grade: written source comparison and derivation under the retained seed, Jacquet–Langlands, and Shii inputs. Not independent certification of the cited theorems or a new Selmer bound.

## Result

The old definite-theta branch can be supplied with an actual integral Gross-point source and its signed supersingular quotients, using one fixed primitive integral quaternionic eigenfunction. This does not require the missing integral comparison across **level-raised quaternion algebras**. It is a different, unraised source.

There is a concrete necessary correction to its extraction rule: at inert supersingular p, every raw anticyclotomic theta element at level n≥2 has zero quadratic jet modulo p. The quadratic jet of the **signed quotient** is instead a particular higher binomial moment of those same integral Gross-point values. The required division is defined integrally by a polynomial-factor isomorphism; no actual p-content is discarded.

With the additional finite raw inversion calculation in §7, the constant and residual linear terms vanish. Both signed quadratic jets are therefore determined by **two explicit residue-field digits from two source layers**, given in (7.7)–(7.8). Their nonvanishing is not proved, and is not promoted to a seed vanishing criterion.

Thus the previously open `SUPERSINGULAR_SIGNED_CONSTRUCTION` in `BRANCH_THETA.md` has an explicit source-level implementation on the inert domain. The arithmetic nonvanishing of the resulting signed coefficients is not supplied.

## 1. Sources actually used, and a repaired indexing convention

Primary sources read:

1. Ryota Shii, [arXiv:2503.09034v1](https://arxiv.org/html/2503.09034v1), §§2–4: (2.3)–(2.14), Theorem 3.5, Proposition 3.8, and (4.1)–(4.22).
2. Henri Darmon and Adrian Iovita, [*The anticyclotomic Main Conjecture for elliptic curves at supersingular primes*](https://mypage.concordia.ca/mathstat/iovita/paper.pdf), author PDF: §2.1, Theorem 2.2, Proposition 2.3; §2.2, pp.7–15, especially Lemmas 2.6–2.7 and Proposition 2.8.
3. Burungale–Büyükboduk–Lei, [arXiv:2211.03722v2](https://arxiv.org/html/2211.03722v2), §3.1 immediately after Proposition 3.1: the quaternionic form is chosen integral and not divisible by the coefficient-ring uniformizer. This is a targeted normalization check, not a re-audit of their main theorem.
4. Chida–Hsieh, [*Special values of anticyclotomic L-functions for modular forms*](https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf), author PDF, (2.1), (2.7), Lemma 3.7 and the finite-level calculation in the proof of Theorem 4.8. The ordinary inverse-limit theorem is **not** invoked at supersingular p; the raw spherical-vector replacement at p is checked in §7 below.

The DI text is the source explicitly cited by Shii for the finite theta recurrence and signed construction. It resolves two notation slips in Shii §2:

- Shii initially describes a function on oriented edges, then evaluates it on vertices. DI Definition 2.1 uses **vertices** throughout; that is the model used below.
- The torus orbit at distance m has order (p+1)p^(m−1). DI explicitly writes `G_n = tilde G_(n+1)/Delta` and `L_n = projection(tilde L_(n+1))`. Thus anticyclotomic degree p^n uses ring conductor p^(n+1). We retain that shift. An arbitrary adjacent walk is insufficient: the selected vertices form a nonbacktracking ray away from the distinguished vertex.

These are resolved conventions, not new arithmetic factors. The source comparison does not import Shii's imprecisely indexed formula literally.

Project sources: `BSD_EXACT_BD_CONSTANT_2026-10-07/construction/CONSTRUCTION.md` C0–C4, and the retained `BRANCH_THETA.md` and `DEFINITE_THETA_ORDER.md` in the W3 return. Exact reading-copy hashes are in `SHII_SOURCE_BINDINGS.json`.

## 2. A fixed integral eigenfunction, without a prime-dependent period choice

Keep K=Q(√−7), B the definite rational quaternion algebra ramified at infinity and

\[
N^-=3\cdot2243\cdot5843,
\qquad N^+=2^3\cdot4547^2.
\]

Fix an Eichler order O of level N⁺, with the fixed oriented CM data at the primes dividing N. Equivalently use the finite adelic class set

\[
X=B^\times\backslash\widehat B^\times/\widehat O^\times.
\]

Let L_Q be the simultaneous rational Jacquet–Langlands eigenspace for the seed, including the required local newvector conditions at N. Its dimension is one. Define

\[
L_Z=L_Q\cap\mathbf Z^X=\mathbf Z\varphi,
\qquad\gcd\{\varphi(x):x\in X\}=1.
\]

Fix its remaining sign once. This is the global primitive integral convention in DI, printed p.7. It is also the base-level primitive eigenfunction convention used in the existing BD construction. It is not the primitive **eigenfunctional** on the dual Brandt module; those two objects must not be interchanged without the Brandt pairing.

For any p, the same phi is primitive over Z_p, because an integer linear combination of all its values equals one. Hence any other primitive integral generator of this same characteristic-zero eigenline is u_p phi with u_p in Z_p^×. This proves the **unit property** when comparing such generators; it does not assert u_p=1. We avoid even that unspecified unit by constructing both sides with phi itself.

The BBL normalization underlying Shii Theorem 3.5 explicitly requires coefficient-ring indivisibility after its Proposition 3.1. For the rational seed coefficient field this is precisely the primitive Z_p lattice condition just verified. Thus this normalization screen does not leave an arbitrary power of p between the constructed unraised eigenfunction and that source convention.

No computation of the seed's huge Brandt vector is claimed. This is a specified mathematical source, with a finite integral definition. It does not use a rational idempotent or require knowing that p avoids the uncomputed J_f in the earlier level-raising construction.

## 3. Explicit torus-orbit theta elements

Now fix a good supersingular p≥5, p≠7, inert in K. The previous hypothesis screen verifies Shii's displayed hypotheses on this domain, under retained residual-image and conductor inputs.

Use the vertex model for O[1/p] at p. Its finite vertex quotient is the same unraised quaternionic class model, and the pullback h_p of phi satisfies

\[
\sum_{v'\sim v}h_p(v')=a_p(E)h_p(v)=0.
\tag{3.1}
\]

Choose an optimal embedding K→B compatible with the fixed CM orientations, a distinguished torus-fixed vertex v_0, and a ray v_m at distance m from v_0. Write

\[
\widetilde G_\infty=K_p^\times/\mathbf Q_p^\times,
\quad\widetilde G_m=\widetilde G_\infty/U_m,
\quad |\widetilde G_m|=(p+1)p^{m-1}\quad(m\ge1).
\]

Here U_m is the stabilizer of v_m. For K=Q(√−7), h_K=1 and the global units introduce no additional quotient beyond the rational units. Let Delta be the torsion subgroup, of order p+1, and

\[
G_n=\widetilde G_{n+1}/\Delta\simeq\mathbf Z/p^n\mathbf Z.
\]

Define the actual integral elements

\[
\widetilde\Theta_m
=\sum_{\sigma\in\widetilde G_m}
h_p(\sigma\star v_m)[\sigma^{-1}],
\qquad
\Theta_n=\operatorname{pr}_\Delta(\widetilde\Theta_{n+1})
\in\mathbf Z[G_n].
\tag{3.2}
\]

The projection is a **sum over Delta fibers**, not averaging by 1/(p+1). Thus there is no suppressed normalizing factor. In an adelic description these are the phi-values at the oriented Gross points of ring conductor p^(n+1), pushed to the anticyclotomic p-power quotient.

For fixed choices, (3.2) is literally Shii (2.3) followed by the DI layer shift and torsion projection, with h=phi. It is also the actual finite Gross-point system which the old `BRANCH_THETA` used as the hypothesis H1.

Changing the base ray by the torus translates Theta_n by a group element. Inverting reciprocity replaces Theta_n by its involution. Changing the sign of phi negates Theta_n. Each change leaves the product

\[
\mathcal P_n=\Theta_n\,\iota(\Theta_n)
\tag{3.3}
\]

unchanged (inversion fixes that product). The fixed CM orientation avoids additional identifications between differently oriented quaternionic sets. If an orientation change is implemented by an Atkin–Lehner operator acting on this eigenline by ±1, that sign also cancels in (3.3). No claim about arbitrary unrelated CM parametrizations is needed.

## 4. Proving the actual norm relation, including its lower layer

Fix m≥1 and a torus orbit at v_m. Its p outward neighbors are exactly the lifts of that orbit to v_(m+1). The remaining neighbor is v_(m−1). Equation (3.1) says that their phi-values sum to minus the value at that remaining neighbor. Summing over the orbit gives

\[
\operatorname{pr}_{m+1,m}\widetilde\Theta_{m+1}
=-\operatorname{Tr}_{m-1,m}\widetilde\Theta_{m-1}.
\tag{4.1}
\]

After the Delta projection and layer shift, for n≥1 this is

\[
\operatorname{pr}_{n+1,n}\Theta_{n+1}
=-\xi_n\Theta_{n-1},
\qquad
\xi_n=\sum_{a=0}^{p-1}\gamma^{a p^{n-1}}.
\tag{4.2}
\]

The element on the right is independent of the chosen lift of Theta_(n−1). This is the transfer, not scalar multiplication by p inside the group ring. Its augmentation is multiplication by p.

At the initial torus orbit, all p+1 neighbors of v_0 occur once. Hence

\[
\Theta_0=\sum_{\sigma\in\widetilde G_1}h_p(\sigma v_1)
=a_p(E)h_p(v_0)=0.
\tag{4.3}
\]

The next augmentation is `aug(Theta_1)=−(p+1)h_p(v_0)`. This follows by summing (4.1) at m=1; one must not replace its initial p+1 by p. No nonvanishing or vanishing of h_p(v_0) has been assumed in constructing the source.

## 5. Signed division is an integral map, not rescaling by a p-power

Set Lambda=Z_p[[T]], gamma=1+T,

\[
\omega_n=(1+T)^{p^n}-1,
\quad\Phi_j(T)=\Phi_{p^j}(1+T),
\quad \Lambda_n=\Lambda/(\omega_n).
\]

Let epsilon_n be plus for even n and minus for odd n. Define

\[
A_n=\prod_{\substack{1\le j\le n\\j\not\equiv n\pmod2}}\Phi_j(T),
\qquad
H_n=T\prod_{\substack{1\le j\le n\\j\equiv n\pmod2}}\Phi_j(T),
\quad \omega_n=A_nH_n.
\tag{5.1}
\]

DI Lemma 2.7 gives the exact isomorphism

\[
\Lambda/(H_n)\xrightarrow[\sim]{\;\times A_n\;}
A_n\Lambda/(\omega_n).
\tag{5.2}
\]

Indeed, if A_n a belongs to A_nH_n Lambda, cancellation in the integral domain Lambda gives a in H_n Lambda. The same proof works after reducing modulo p^r, using the monic polynomial factor and the explicit quotient; DI states this integral finite-precision version too.

The recurrence (4.2) gives H_n Theta_n=0. Equivalently, Theta_n lies in the image of (5.2), so there is a **unique** class

\[
Q_n\in\Lambda/(H_n),\qquad \Theta_n=A_nQ_n.
\tag{5.3}
\]

This is DI Proposition 2.8. Multiplying Q_n by (−1)^(n/2) for even n, respectively (−1)^((n+1)/2) for odd n, gives compatible families under n→n−2, hence signed elements Q^+,Q^− in Lambda. These are the actual Shii/DI signed theta sources in the chosen primitive phi convention.

The operation removes only the prescribed polynomial factor A_n. It does not divide Q_n by its common p-content. For example, if all phi orbit sums in Theta_n carry an additional factor p, that factor remains in Q_n.

## 6. The correct finite weighted extraction, and why the raw quadratic jet fails

Define

\[
d_n=\deg A_n
=\sum_{\substack{1\le j\le n\\j\not\equiv n\pmod2}}p^{j-1}(p-1).
\]

Modulo p, the exact cyclotomic factor identity is

\[
A_n(T)\equiv T^{d_n}\pmod p.
\tag{6.1}
\]

Consequently, for n≥1 and k=0,1,2,

\[
[T^k]Q_n\bmod p=[T^{d_n+k}]\Theta_n\bmod p.
\tag{6.2}
\]

These coefficients are well-defined because d_n+2<p^n for p≥5,n≥1. The finite group ring modulo p is F_p[T]/T^(p^n).

Write Theta_n=Σ_(a=0)^(p^n−1) b_(n,a) gamma^a, where b_(n,a) is the sum of phi at the Gross points mapping to gamma^(−a) in (3.2). The actual extraction is

\[
\boxed{[T^k]Q_n\equiv
\sum_{a=0}^{p^n-1}b_{n,a}\binom{a}{d_n+k}\pmod p,
\qquad k=0,1,2.}
\tag{6.3}
\]

This supplies a genuine finite modular/quaternionic sum, with specified integer weights and source normalization. A sign must be applied if one wants Q^epsilon rather than the unsigned Q_n.

For n≥2, d_n≥p−1≥4. Therefore

\[
\boxed{\Theta_n\equiv0\pmod{(p,T^3)}\quad(n\ge2).}
\tag{6.4}
\]

The raw degree-two moment of deeper supersingular layers is automatically zero. Increasing n cannot repair it. The signed degree-two coefficient is the higher moment of order d_n+2 in (6.3). At n=1, A_1=1, so there is no forced signed factor yet.

This corrects an otherwise misleading continuation of the old ordinary-only `BRANCH_THETA` finite-layer quadratic rule. It also provides the replacement computation before anyone generates more raw quadratic data. No seed Gross-point values have been evaluated here. The separate finite-ring checks in this return are controls on extraction, not seed coefficients.

### Two source layers suffice for both signed quadratic jets

The signed compatibility gives a further finite reduction. Modulo p,

\[
H_1\equiv T^p,\qquad H_2\equiv T^{p^2-p+1}.
\]

Both ideals are contained in (T³) for p≥5. Therefore the **entire** quadratic jets of the two infinite signed sources are already determined by

\[
\boxed{Q^-\equiv-\Theta_1\pmod{(p,T^3)},\qquad
Q^+\equiv-Q_2\pmod{(p,T^3)}.}
\tag{6.5}
\]

They require ring conductors p² and p³, respectively, with the convention of §3. There is no need to construct deeper theta layers to recover these jets.

At n=2, d_2=p−1. Write a=a_0+pa_1 with 0≤a_i<p. Lucas's binomial identity makes (6.3) particularly simple:

\[
\begin{aligned}
[T^0]Q_2&\equiv\sum_{a_0=p-1} b_{2,a},\\
[T^1]Q_2&\equiv\sum_a a_1 b_{2,a},\\
[T^2]Q_2&\equiv\sum_a a_0a_1 b_{2,a}\pmod p.
\end{aligned}
\tag{6.6}
\]

The filter a_0=p−1 applies only to the first sum. The latter two run over all a. The signed plus jet has the negatives of these values. For the minus jet the three weights are simply −1, −a, and −binom(a,2) on Theta_1. These are arithmetic source formulas; they neither imply that a coefficient is nonzero nor authorize dropping its true content.

## 7. What transfers to Shii's Fitting statement

With the same primitive phi, the same oriented Gross points, the DI layer shift, and the same reciprocity convention, Theta_n is the theta source of Shii's statement. Thus, under that source theorem and the already-screened seed hypotheses,

\[
\mathcal P_n=\Theta_n\iota(\Theta_n)
\in\operatorname{Fitt}_{\Lambda_n}
\operatorname{Sel}_{p^\infty}(E/K_n)^\vee.
\tag{7.1}
\]

This transfer is of the **element itself**, not an interpolation expression with an unknown period quotient. Shii's coarse interpolation formula (2.8) is not used. If another author uses a primitive generator u_p phi of the same lattice, the product changes by u_p² and its generated ideal is the same; that supports Fitting membership but cannot prove the exact tame 288 scalar.

The involution factor is also explicit: cyclotomic reciprocity gives iota(A_n)=gamma^(−d_n)A_n. Hence, in the named convention,

\[
\mathcal P_n=\gamma^{-d_n}A_n^2 Q_n\iota(Q_n).
\tag{7.1a}
\]

The group element gamma^(−d_n) is a specified unit. Shii (4.21) is an equality of generated ideals, where this factor legitimately disappears; it must remain visible in an equality of elements.

Do not cancel A_n² from (7.1) inside the finite group ring: it is a zero divisor there. Shii's proof obtains the signed comparison from the infinite-level signed Selmer groups first, then multiplies by the explicit local factors before passing to classical Selmer. In particular:

- the integral signed main-conjecture inclusion (3.12) and Fitting=characteristic equality (3.13) are imported;
- Proposition 3.8 uses actual restriction with finite local cokernels; those are not declared zero;
- the plus/minus-to-classical exact sequence (4.8) and its local quotient contribute the square of the appropriate omega factor in (4.12);
- (4.17)–(4.22) only then produce (7.1).

The printed arrow in Shii Proposition 3.8 is opposite to the restriction arrow in its proof's diagram. The direction used by its Fitting argument is finite-level signed Selmer injecting into the corresponding infinite-level specialization, so dualization is surjective. We follow the diagram and proof. This comparison is conditional on those established source inputs; no silent finite-error removal has been inserted.

### The signed constant terms vanish exactly for this seed

There is one immediate arithmetic specialization consequence of (7.1), also derived independently in `INDEPENDENT_SEED_CONTROL.md`. Put M_n=Sel_(p^∞)(E/K_n)^∨. Its Mordell–Weil quotient has trivial-character Q_p dimension at least two, from the two independent rational seed points. Consequently M_n⊗_(Lambda_n)Z_p has positive Z_p rank. Fitting ideals commute with base change, so

\[
\operatorname{aug}\bigl(\operatorname{Fitt}_{\Lambda_n}M_n\bigr)
=\operatorname{Fitt}_{\mathbf Z_p}(M_n\otimes_{\Lambda_n}\mathbf Z_p)=0.
\]

Applying augmentation to (7.1) gives aug(Theta_n)²=0 in Z_p, hence aug(Theta_n)=0 for n≥1. Since A_n(0) is a nonzero power of p, (5.3) gives Q_n(0)=0 as an equality in Z_p. Thus

\[
\boxed{Q^+(0)=Q^-(0)=0.}
\tag{7.2}
\]

This keeps the actual finite-level Selmer module; it does not discard a specialization kernel or assume primary finiteness. It also supplies a consistency check for the source: (4.3) and aug(Theta_1)=−(p+1)h_p(v_0) force h_p(v_0)=0. In (6.6), the first filtered sum must therefore be zero modulo p. Augmentation alone leaves the linear and quadratic coefficients; the next calculation removes the residual linear terms as well.

### Positive finite-level symmetry removes the residual slopes too

The independent derivation in `INDEPENDENT_SEED_CONTROL.md` §2a has been checked against the cited Chida–Hsieh formulas here. In their local notation, h=Tr(theta) and c is the **ring-conductor exponent**. At an inert good coefficient prime,

\[
J/\sqrt\beta=\begin{pmatrix}-1&h\\0&1\end{pmatrix},\qquad
s_c=\begin{pmatrix}0&1\\-p^c&0\end{pmatrix},
\]

so direct matrix multiplication gives

\[
s_c^{-1}(J/\sqrt\beta)s_c
=\begin{pmatrix}1&0\\-p^c h&-1\end{pmatrix}
\in\operatorname{GL}_2(\mathbf Z_p).
\tag{7.3}
\]

The raw quaternionic vector at p is spherical and is fixed by this matrix. The scalar sqrt(beta) is a p-unit in the source's choice and acts through the trivial central character. Hence the finite Gross-point inversion proof does not need ordinary stabilization at this place. At the other places its original local newvector/Atkin–Lehner calculation, including Lemma 3.7, remains in force.

With k=2, gcd(D_K,N)=1 and good p, the finite proof's sign is

\[
(-1)^{k/2}\prod_{q\nmid pD_K}\epsilon_q(f)
=\epsilon(E)=+1.
\]

Thus the actual raw theta in the chosen convention satisfies

\[
\iota(\Theta_n)=\sigma_n\Theta_n,\qquad \sigma_n\in G_n.
\tag{7.4}
\]

In the explicit Chida–Hsieh orientation sigma_n is the inverse Artin image of N⁺. A change of Gross-point/path convention changes that group translate, not its augmentation-one property or the sign. This is the finite raw calculation; it does not import the ordinary inverse-limit statement wholesale.

Now iota(A_n)=gamma^(−d_n)A_n and the ideal (H_n) is inversion-stable. Apply the injective map (5.2) to cancel **only the prescribed source factor**, obtaining

\[
\iota(Q_n)=\gamma^{d_n}\sigma_n Q_n
\quad\text{in }\Lambda/(H_n).
\tag{7.5}
\]

This cancellation does not divide a Fitting inclusion. It is exactly the proven quotient-module isomorphism. Since Q_n(0)=0, write Q_n=a_nT+b_nT² modulo (p,T³). For n≥1 the reduction of H_n is a power of T of degree at least p, so this truncated equality has no hidden relation in degrees ≤2. Its linear terms are −a_n on the left and +a_n on the right. Because p≥5,

\[
\boxed{Q_n\equiv b_nT^2\pmod{(p,T^3)}.}
\tag{7.6}
\]

The result concerns the residual slope. In a finite integral quotient an arbitrary polynomial representative can have a nonzero linear coefficient divisible by the linear coefficient of H_n. No literal integral slope-zero statement for such representatives is asserted.

Combining (6.5)–(6.6) and (7.6), the residual quadratic jets of both genuine signed sources reduce to **two digits**:

\[
\boxed{
Q^-\equiv\beta_p^-T^2,\quad
\beta_p^-=-\sum_{a=0}^{p-1}b_{1,a}\binom a2\pmod p,
}
\tag{7.7}
\]

\[
\boxed{
Q^+\equiv\beta_p^+T^2,\quad
\beta_p^+=-\sum_{a_0,a_1=0}^{p-1}a_0a_1 b_{2,a_0+pa_1}\pmod p.
}
\tag{7.8}
\]

The fixed source has additionally forced Σ_a a b_(1,a)=0 and Σ_a a_1 b_(2,a)=0 modulo p. These are source-consistency equations, not unit assertions. There is no theorem here that either beta digit is nonzero, nor that their nonzero values alone give the missing seed excess bound.

## 8. Which old objects are, and are not, identified

| Project object | Relation to (3.2) |
|---|---|
| Unraised definite Gross-point theta family of `BRANCH_THETA` | Same construction once its source H1, phi normalization, ray, and conductor shift are fixed as above |
| Ordinary stabilized theta | Same raw system, but ordinary stabilization is not used at a supersingular prime |
| Signed supersingular theta | Constructed here by (5.2)–(5.3); precise coefficient extraction (6.3) |
| Level-raised two-prime detector C(ell_1,ell_2) in the October 7 BD construction | Different quaternion algebra with discriminant N⁻ell_1ell_2, mod-p^r eigenform and CM conductor one; no equality or map supplied by Shii |
| Tame Mazur–Tate C₂(p,ell), ell auxiliary | Different abelian extension and conductor variable; no equality with the anticyclotomic p-power source is asserted |
| Actual divided cyclotomic Kato derivative | No comparison to (3.2) is supplied by this construction |

The useful completed interface is therefore the **unraised supersingular theta source and signed extraction**, not the level-raising reciprocity normalization or cyclotomic-to-anticyclotomic comparison.

## 9. Endpoint boundary and next genuine arithmetic input

All the expressions above are defined from the seed modular form and actual Gross points. Their values can still be zero or highly p-divisible. A primitive quaternionic eigenfunction does not make any particular weighted orbit sum primitive.

To obtain a seed conclusion one now needs independently controlled signed coefficients and a valid specialization/leading-term argument that removes the known Mordell–Weil directions while retaining finite local and H² errors. In particular, raw Fitting membership cannot be divided by its forced factors, and an ordinary derived-height theorem cannot be silently reused at inert supersingular primes.

The arithmetic construction is no longer left as an undefined “signed analogue.” The nonvanishing and excess-content bound remain unproved. No new primary component, cofinite tail, FIN, ORDER9, or Q36 is claimed.
