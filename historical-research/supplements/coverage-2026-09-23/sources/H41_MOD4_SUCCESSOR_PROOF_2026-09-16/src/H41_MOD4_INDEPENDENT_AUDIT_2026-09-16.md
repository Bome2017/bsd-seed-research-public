# H41 mod-4 analytic bridge: independent reconstruction and completion draft

**Date:** 16 September 2026  
**Status:** New conventional mathematical derivations and independent exact computations. Not Lean-certified, not independently refereed after this reconstruction, and not a modification of any canonical freeze.  
**Scope:** The uploaded positive-H41 argument, its integral residue/character bridge, the corresponding negative-branch consequence, and the precise interface to the retained twist/BSD assembly.

## Executive finding

The coefficient calculation survives independent reconstruction. More importantly, the integral residue step has a concrete proof from nonarchimedean uniformization and tropical Abel–Jacobi compatibility. The stronger formal local factorization designated P2 is unnecessary: the analytic unit theorem and slope formula give exactly the required residues. A tame-cover construction provides a positive-graph derivation rather than merely an analogy with the negative case.

This gives a **candidate complete conventional analytic bridge relative to the explicitly retained arithmetic inputs**: the four-vertex classification, the stated minimal discriminant valuations, the cusp-image torsion bound and period identity, and the previously certified descent/local BSD composition. Its decisive proposed endpoint is

\[
 E_0=E,\qquad \operatorname{ord}(q([0]-[\infty]))=2,\qquad
 4\,L(E,1)/\Omega_{E,\mathbb R}\text{ is odd}
\]

on the positive branch. Here \(E_0\) is the actual connected optimal quotient, not a selected isogenous model. The geometric instantiation and the composed proof must still pass a fresh referee before a family-wide freeze changes. No new open-ended literature search is needed to formulate that review.

## 1. Custody and retained context

The uploaded `02_T1_L2_POSITIVE_PROOF.md` explicitly calls itself a first-author, unrefereed draft. Its theorem labels do not themselves certify its conclusions. The older `00_RESULT.md` is a computation-stage predecessor, not an additional independent proof.

The Library's `H41_W_MECHANISM_AUDIT.md` was read in full. It supplies the full-real-period convention, the exceptional positive index, the four-position period/torsion table, the exact cusp/winding identities, and the distinction between eight exact L-value certificates and optimality data. Its September 13 “blocked” status predates this new proposed mechanism; it is not treated as a later veto or as a proof of impossibility.

Memory was used for continuity, including the instruction not to redo the completed 62a1/66b1 assemblies. Full canonical successor archives, the proofs and custody records of all named A/B/G/M/D3 inputs, and all other chats were not available as one fully replayed corpus. This report does not claim that replay.

Of the ten entries in the supplied checksum manifest, eight have mounted backing files. **All eight match.** `ROOT_ARITHMETIC.md` was not mounted; the W-audit was retrieved as Library text, not as manifest-verified bytes. The two unavailable-byte entries are explicitly recorded, not counted as passed checks.

Public PDFs and Cremona rows were read through the web tool. Direct container downloads failed at DNS resolution. Therefore the package contains a source register and a provenance-labelled transcription of ten numerical rows, not purportedly downloaded PDFs or a complete database snapshot.

## 2. Notation and exact scope

Write

\[
 E_r:y^2=x^3+(1-2r)x^2+r^2x,\quad D=1-4r,\quad r=\varepsilon2^m,
\]

with the retained odd \(m\ge3\). The minimal model used in the input is

\[
 Y^2+XY-bY=X^3-bX^2,\qquad b=-r/4,\qquad
 \Delta_{\min}=b^4(1+16b).
\]

The positive branch has \(r=-2^m\), normally \(D=3\ell\) with \(\ell\) prime and \(\ell\equiv3\pmod8\), and conductor \(6\ell\). The exceptional case is

\[
 m=7,\quad D=513=27\cdot19,\quad N=114.
\]

The negative branch has \(r=2^m\), \(p=2^{m+2}-1\) prime, and conductor \(2p\). Its prime satisfies \(p\equiv7\pmod8\). No infinitude of base parameters is asserted.

Use \(\pi:J_0(N)\twoheadrightarrow E_0\) for the optimal quotient, \(\phi=\pi\circ\mathrm{AJ}_\infty\), and \(c=[0]-[\infty]\). The letter \(q\) below is reserved for a twisting prime. Set

\[
 \lambda_E=\frac{L(E,1)}{\Omega_{E,\mathbb R}},\qquad
 \Omega_{E,\mathbb R}=\int_{E(\mathbb R)}|\omega_E|.
\]

This is not the least positive real period when the real locus has two components.

## 3. T1: independent uniform reconstruction

### 3.1 Eta side

For positive \(N=6\ell\), take the input exponent vector

\[
 (r_d)=(6\ell+1,-3\ell-2,-2\ell-3,\ell+6,-\ell-6,2\ell+3,3\ell+2,-6\ell-1)
\]

on divisors \((1,2,3,6,\ell,2\ell,3\ell,6\ell)\). Its logarithmic derivative has coefficients

\[
 \theta=qF'/F,\quad \theta_0=-(\ell^2-1),\qquad
 \theta_n=-\sum_{d\mid n}r_dd\,\sigma_1(n/d)\quad(n>0).
\]

The comparison Eisenstein form is

\[
 \mathcal E^+=-\frac1{24}(1-2V_2)(1-V_3)(1-V_\ell)E_2.
\]

Its coefficient convolution has weights
\((1,-2,-1,2,-1,2,1,-2)\). Substitution \(\ell=4k+3\) shows that every difference \(-r_dd-w_d\) is a polynomial divisible by four. Independently expanding those polynomials reproduced the input table.

For \(n=2^a3^b\ell^ct\), \((t,6\ell)=1\), the comparison coefficient is

\[
 \mathcal E^+_n=3^b\ell^c\sigma_1(t).
\]

The negative vector gives the analogous **negative** congruence to
\(-\frac1{24}(1-2V_2)(1-V_p)E_2\). The constant terms are divisible by four, indeed by eight for the retained parameters.

**Necessary correction retained:** \(\theta\) itself is not a Hecke eigenform. At \(\ell=11\), its first two positive-index coefficients are \(-67,-131\). Only the congruence to the comparison eigenform is used.

### 3.2 Newform side

The point \(P=(r,r)\) doubles to \((0,0)\). At every good odd prime it therefore forces \(a_v\equiv1+v\pmod4\). The Euler recurrence propagates this to prime powers, and multiplicativity supplies the remaining coefficients.

At 2 the minimal model has split nodal tangent cone \(Y(Y+X)\), so \(a_2=1\). At an odd bad prime dividing \(D\), reduction has the form \(y^2=x(x+1/4)^2\); its node has tangent coefficient \(-1/4\). All retained odd bad primes are 3 modulo 4, so the reduction is nonsplit and the bad coefficient is \(-1\). This remains true at 3 in the exceptional \(m=7\) case; its discriminant exponent is three, not its conductor exponent.

Thus, as full q-expansions at infinity,

\[
 \omega_f\equiv d\log F\pmod4\quad(D>0),\qquad
 \omega_f\equiv-d\log F\pmod4\quad(D<0).
\]

### 3.3 Independent numerical checks

A newly written program, importing no supplied executable, used raw-model point counts at odd primes and the minimal equation at 2. It found no mod-4 discrepancy through coefficient 1,000 at all ten levels. The first mod-8 discrepancy is coefficient 1 in every case. These 10,000 tests are regression controls; the polynomial and Euler arguments, not the tests, establish uniform T1.

All cusp orders were separately recomputed from the eta exponents at all ten levels and agree with the supplied two-cusp divisor. No symbolic proof of the entire retained cusp-order/classification corpus is being claimed from these finite checks.

## 4. L2 is a general two-component divisibility lemma

**Lemma.** Let \(\mathcal X/R\) be a normal flat model over a DVR, with two reduced irreducible components in the special fibre. Let \(\mathcal L\) be an invertible sheaf. Suppose an involution exchanges the two vertical generic points and preserves the relevant local lattices. A global section \(\delta\) transforming by a unit scalar and having expansion divisible by \(2^k\) at a smooth cusp on one component is globally divisible by \(2^k\), provided that the cusp expansion detects that local lattice.

**Proof.** For \(k=1\), faithful flatness of completion gives divisibility at the cusp and hence at its component's generic point. The involution gives the same at the other generic point. At every horizontal codimension-one point, 2 is a unit. Normality and invertibility of \(\mathcal L\) then imply that \(\delta/2\) is a global section. Its expansion is divisible by \(2^{k-1}\), and its transformation property is unchanged. Induct.

For H41 take **\(\mathcal L=\omega_{\mathcal X/R}(\mathrm{cusps})\)**. The logarithmic differential of the unit has genuine cusp poles in characteristic zero; calling it a holomorphic differential without qualification is incorrect. Its vertical integrality follows by writing \(F=2^A v\) at a vertical generic point with \(v\) a unit, since the relative logarithmic differential of \(2^A\) vanishes. Away from cusp horizontal divisors it is regular. Normality extends this codimension-one statement.

Česnavičius, §2.6 and Lemma 2.7 of `1604.02165`, provide the normal semistable two-component framework and integral normalized newform. The prime-to-2 Atkin–Lehner factor preserves components; the 2-factor exchanges them. The exponent relation \(r_{N/d}=-r_d\) gives

\[
 F\circ w_N=C/F,\qquad w_N^*(d\log F)=-d\log F.
\]

The newform also has full Fricke eigenvalue \(-1\). Apply the lemma to \(\omega_f-d\log F\) positively and \(\omega_f+d\log F\) negatively. This proves the global log-lattice congruence modulo four, once these model identifications are fixed. It does not rely on an invalid lifting of the older \(w_2\)-only mod-2 formula.

## 5. Positive graph: an explicit tame-cover derivation

This is the proposed geometric instantiation to submit to the referee, not a claim that a source prints this H41 lemma verbatim.

### 5.1 Fine cover and removal of wild stabilizers

On the elliptic locus use the fine level structure \((E,C_2,C_3,P_\ell)\), where \(P_\ell\) has exact order \(\ell\). The \(\ell\)-level point kills automorphisms. It is obtained near the supersingular locus from the fine \(\Gamma_1(6\ell)\) model by forgetting the choice of generator of \(C_3\). That forgetting map is finite étale: the 3-torsion is étale in characteristic 2. Consequently the regular semistable fine chart descends to a chart

\[
 R[[u,v]]/(uv-2).
\]

The remaining effective diamond quotient has group

\[
 G=(\mathbb Z/\ell\mathbb Z)^\times/\{\pm1\},\qquad |G|=(\ell-1)/2,
\]

which is odd. The central \(\pm1\) must be removed before calling this quotient tame.

The automorphism calculation can be made explicit on the characteristic-2 supersingular model \(y^2+y=x^3\). Its 24 automorphisms have the form

\[
 x\longmapsto a^2x+s^2,\qquad
 y\longmapsto a^3y+a^2s x+t,
 \quad a\in\mathbb F_4^\times,\ s\in\mathbb F_4,
 \quad t^2+t=s^6.
\]

There are two choices of t; the central involution interchanges them. The 3-division polynomial is \(x^4+x\), so the four order-3 cyclic subgroups correspond to the four x-values in \(\mathbb F_4\). The effective action is its affine group of order 12, namely \(A_4\).

At a supersingular point, the projective automorphism group is \(A_4\). Fixing the order-3 subgroup means fixing a point of \(\mathbb P^1(\mathbb F_3)\), whose stabilizer is cyclic of order three. Imposing the \(\ell\)-line leaves effective stabilizer order \(e_x=1\) or 3. A tame stabilizer preserves the branches and can be diagonalized with inverse characters. Its invariant chart is

\[
 R[[U,V]]/(UV-2^{e_x}).
\]

The source-supported inputs are regularity/semistability of the fine model and its fine-moduli interpretation. The construction, identification with the chosen coarse model, and the invariant-chart calculation should be written together in the freeze; saying only “the negative proof adapts” omits this necessary argument.

### 5.2 Counts and component group

The supersingular configurations are \(A_4\)-orbits on
\(\mathbb P^1(\mathbb F_3)\times\mathbb P^1(\mathbb F_\ell)\). Orbit–stabilizer gives

\[
 \sum_x\frac1{e_x}=\frac{4(\ell+1)}{12}=\frac{\ell+1}{3}.
\]

There are two order-three stabilizer orbits when \(\ell\equiv1\pmod3\), and none when \(\ell\equiv2\pmod3\). An independent simultaneous binary-tetrahedral matrix action reproduced these counts for \(\ell=11,19,43,683,2731\).

Resolve each thickness-\(e_x\) node into a path of \(e_x\) unit edges. In the reduced graph Laplacian, each internal path block has determinant \(e_x\), an odd unit in \(\mathbb Z_2\). Eliminating those blocks leaves the one-by-one Schur complement

\[
 \sum_x1/e_x=(\ell+1)/3.
\]

Since \(\ell\equiv3\pmod8\), its 2-adic valuation is two. Moreover the surviving endpoint basis vector is the class of the difference of the principal components. Therefore

\[
 \Phi_J[2^\infty]\simeq\mathbb Z/4\mathbb Z,
\]

and the specialization of \([0]-[\infty]\) generates it. Independent Smith forms at \(\ell=11,19,43\) agree. Component genera do not introduce additional graph-component-group factors.

## 6. P2 can be replaced by a weaker, sufficient analytic statement

The retained divisor is

\[
 \operatorname{div}(F)=(\ell^2-1)([0]-[\infty]).
\]

Baker–Payne–Rabinoff, `1404.0279`, Proposition 2.2 and Theorem 5.15, supply the analytic unit normal form and the slope/divisor relation. They allow the following direct argument.

The potential \(v_2(F)\) is affine along every annular edge, because there are no zeros or poles in its interior. If its endpoint values are \(A,B\), its slope on an edge of length \(e_x\) is \((B-A)/e_x\). The two-cusp divisor and conservation of slopes give, up to one consistent global orientation,

\[
 (B-A)\sum_x1/e_x=\ell^2-1,
\]

hence \(B-A=3(\ell-1)\). On a closed subannulus an analytic unit has the form

\[
 F=\gamma U^{s_x}(1+h),\quad |h|_{\sup}<1.
\]

The logarithm of \(1+h\) converges, so its differential has zero residue. Thus

\[
 \operatorname{Res}_x(d\log F)=s_x=\frac{3(\ell-1)}{e_x}\equiv2\pmod4.
\]

Only this residue assertion is needed. A factorization by a unit of the entire completed coarse local ring is stronger and need not remain a gate.

## 7. L1: exact integral residue/character compatibility

### 7.1 Statement with all normalizations

Work after completion of the maximal unramified extension at 2, and extend the analytic ground field further when needed. Normalize \(v(2)=1\). Let \(\Gamma\) be the metric skeleton, with the coarse edge through \(UV=2^{e_x}\) having length \(e_x\). Identify

\[
 M=X_J=H_1(\Gamma,\mathbb Z).
\]

Let \(\xi\) be the character of the target Tate torus corresponding to coordinate \(T\), and put

\[
 u=\pi^*\xi\in M,\qquad \omega_{E_0}=a\,dT/T,\quad a\in R^\times.
\]

Then, for consistent edge orientations,

\[
 \boxed{\operatorname{Res}_x(\phi^*\omega_{E_0})=a u_x.}
\]

This is an equality before reduction, not only a mod-2 identification or an isomorphism after tensoring the character lattice with \(\mathbb Q\).

### 7.2 Proof and the missing factor-of-two check

The tropical Jacobian has universal real cover \(\operatorname{Hom}(M,\mathbb R)\), with period lattice supplied by the edge-length pairing. For an integral harmonic cycle \(z\), the tropical Abel–Jacobi map is integration against \(z\). Along the interior of an oriented edge, parametrized by \(t=v(U)\), its derivative evaluated on \(z\) is **\(z_x\)**. The length \(e_x\) appears upon traversing the full edge, not in this derivative.

Baker–Rabinoff, `1308.3864`, Proposition 6.1 and Theorem 2.9, identify this construction with analytic Abel–Jacobi and the integral character lattice. Under the lifted Raynaud map induced by \(\pi\), tropicalization is evaluation at \(\pi^*\xi=u\). Hence the slope of the composite map to the Tate skeleton is \(u_x\).

The Tate covering \(\mathbb G_m^{\mathrm{an}}\to E_0^{\mathrm{an}}\) is a topological analytic covering. An open annulus retracts to an interval, so the restriction of \(\phi\) lifts to an invertible analytic function \(g\). On a closed subannulus, Proposition 2.2 of Baker–Payne–Rabinoff gives

\[
 g=\gamma U^w(1+h),\qquad |h|_{\sup}<1.
\]

Its tropical slope is \(w\), and
\(\operatorname{Res}(d\log g)=w\). A change of lift multiplies \(g\) by a constant Tate period, so neither quantity changes. Therefore \(w=u_x\), proving the formula.

No assertion that the entire Jacobian has purely toric reduction is used. Only the elliptic quotient is a Tate curve; the Jacobian may have a good-reduction abelian part.

### 7.3 Application to the congruence

The optimal Manin relation gives

\[
 c_\pi\omega_f=\phi^*\omega_{E_0}.
\]

For these conductors, \(c_\pi=\pm1\) independently of which vertex is optimal: use Česnavičius Theorem 1.4 for odd primes and Theorem 1.5(i) for 2, since the squarefree conductor contains a prime that is 3 modulo 4. Theorem 1.2 in that particular paper is the \(J_1\) statement and should not be cited as the \(J_0\) theorem.

L2, the integral residue functional, and the positive slopes now give

\[
 a u_x\equiv c_\pi s_x\pmod{4R}.
\]

Both scalar factors are units. Since \(s_x\) has valuation exactly one, so does \(u_x\). Because \(u_x\in\mathbb Z\), this is exactly

\[
 \boxed{u_x\equiv2\pmod4\quad\text{for every edge}.}
\]

It is not legitimate to claim that every unit in \(W(\overline{\mathbb F}_2)\) is 1 modulo 2. The valuation-plus-integrality argument avoids that mistake.

## 8. Optimal vertex and cusp image

Write

\[
 n_0=\operatorname{ord}_2(\Delta_{\min}(E_0)).
\]

This is a positive integer; it must not be confused with \(v_2(n_0)\). For every \(z\in M\), its oriented coordinates satisfy \(\sum_xz_x=0\). Since all \(e_x\) are odd,

\[
 \langle z,u\rangle=\sum_xe_xz_xu_x
 \equiv2\sum_xz_x=0\pmod4.
\]

Conrad–Stein Lemma 6.3, with the surjectivity in Theorem 8.2 for an optimal quotient, gives

\[
 \langle M,u\rangle=n_0\mathbb Z.
\]

The result allows a semistable source with a non-toric part and applies at residue characteristic 2. Consequently \(4\mid n_0\).

The retained complete four-vertex classification has

\[
 v_2(n_E)=2,\quad v_2(n_B)=1,\quad v_2(n_F)=v_2(n_G)=0.
\]

Therefore \(E_0=E\). This conclusion uses the completeness of the retained classification, not just four sample models.

Write \(u=\kappa v\) with \(v\) primitive. The graph cycle lattice is saturated in the edge lattice, so \(\kappa\)'s 2-valuation is the minimum coordinate valuation, namely one. Evaluation of integral dual-lattice functionals at \(u\) has image \(\kappa\mathbb Z\). The induced image of the component map is therefore

\[
 (\kappa\mathbb Z+n_E\mathbb Z)/n_E\mathbb Z,
\]

whose 2-primary order is two. The source cusp specialization generates the source component 2-part, so the cusp image has nonzero component of order two. The retained positive-E bound \(t=\operatorname{ord}(\pi(c))\mid2\) now forces \(t=2\).

## 9. Seed without an additional winding computation

The retained real-logarithm identity is

\[
 z=\nu_0\delta_0\lambda_E/h,
\]

where the class of \(z\) modulo \(\mathbb Z\) is the real cusp image, \(\delta_0=\#\pi_0(E_0(\mathbb R))\), and \(h=\Omega_{0,\mathbb R}/\Omega_{E,\mathbb R}\).

At the now established positive vertex E, \(\delta_0=2\), \(h=1\), and \(\nu_0=\pm1\). Order two means \(z\equiv1/2\pmod\mathbb Z\). Hence

\[
 4\lambda_E\text{ is an odd integer},\qquad
 v_2(\lambda_E)=-2,\qquad L(E,1)\ne0.
\]

This rederives the relevant K5 row from the retained identity. It does not infer nonvanishing from a torsion-group cardinality or a finite L-value sample.

## 10. Transfer to the exact retained prime-twist family

Retain precisely

\[
 q\text{ prime},\quad q\nmid2D,\quad q\equiv5\pmod8,\quad (D/q)=-1.
\]

There is a short independent inclusion into Zhai's numerical hypothesis. The quadratic factor of the two-division polynomial has discriminant \(D\), so there is exactly one nonzero rational 2-torsion point over \(\mathbb F_q\). The 2-Sylow is cyclic. The point \(P=(r,r)\) has order four, while

\[
 (r/q)=(-2^m/q)=-1.
\]

For the raw equation, direct algebra gives

\[
 x(2Q)=\frac{(x(Q)^2-r^2)^2}{4y(Q)^2}
\]

whenever \(Q\) is not 2-torsion. Thus a point with nonsquare x-coordinate cannot be twice another point. P is not divisible by two, and a cyclic 2-Sylow containing an element of order four but not its half must have order four. Consequently

\[
 v_2(\#E(\mathbb F_q))=2.
\]

The duplication identity was also symbolically verified. This reasoning handles the exceptional base unchanged; it does not require \(D=3\ell\) literally.

For the positive base, \(\Omega_{E,\mathbb R}=2\Omega_E^+\), so

\[
 v_2(L(E,1)/\Omega_E^+)=-1.
\]

Zhai Theorem 1.7 therefore has exactly the required equality \(2=1-(-1)\). It gives nonvanishing for the twist and least-period valuation one. The positive twist still has two real components, so its **full-real-period valuation is zero**.

The upload invokes the retained Composition Theorem B and completed algebraic/local inputs to identify this with BSD\((E^{(q)},2)\). That invocation is logically compatible with the valuations. This audit has not re-run the original formalization or re-read every source proof underlying Theorem B; its certified endpoint must be imported literally into the successor package.

## 11. Banwait–Huang arithmetic predicates

Theorem 2.13 of `2601.16044v3` has no optimality assumption. It is the Zhai transfer above that needs the actual optimal curve. For positive H41:

* The original curve is semistable. For a retained q, the twisting discriminant is q, and it is coprime to \(3N\): the bad primes are 2 and primes that are 3 modulo 4, whereas q is 5 modulo 8.
* The bad coefficient is \(a_3=-1\).
* At 5, the possible raw r-residues are 2 and 3, with traces 2 and −2. The Frobenius discriminant is −16, a nonsquare modulo both 3 and 7. Hence rational 3- and 7-isogenies are excluded.
* At 7, the possible r-residues are 3, 5 and 6, with traces 4, 0 and −4. The discriminants −12 and −28 are nonsquares modulo 5, excluding a rational 5-isogeny. Both 5 and 7 are uniformly good, as the same residue calculation shows.
* For residual primes 2 and 3, the multiplicative prime \(\ell\) with \(v_\ell(\Delta)=1\) witnesses ramification. For residual prime \(\ell\), use 3, whose discriminant exponent is 1 or 3 and is not divisible by \(\ell>3\).
* At q, four-torsion gives \(a_q\equiv2\pmod4\), so \(a_q\ne0\). The Hasse bound for \(q\ge5\) implies \(|a_q|<q\), giving ordinary reduction.

The explicit local calculations were independently reproduced. Conditions (ii) nonvanishing and (iii) BSD(2) enter only after the analytic/descent assembly above. Preserve the qualification concerning external results in Banwait–Huang Remark 2.11; do not recast its conclusion as an entirely Lean-certified theorem.

## 12. Negative-branch implication and the older parked route

The same integral residue proof and full-Fricke lemma apply negatively. The retained negative graph/slopes give \(s_x\) odd and \(e_xs_x\) constant. Thus \(e_xu_x\) is constant modulo four (the common scalar is a unit), and the monodromy ideal is again contained in \(4\mathbb Z\). The retained vertex valuations then force \(E_0=E\), not merely \(E_0\in\{E,B\}\).

Here \(\kappa\) is odd. With the retained negative graph's cusp generator and the order-four target component 2-part, the cusp image has order four, yielding the negative seed through its retained K5 identity.

This is a new route around the earlier component-group-only blindness. Its new information is the **integral pulled-back character vector obtained from annular residues**. It is not an inference from the Eisenstein action on a component group that vanishes at the unwanted vertices. The earlier search failure therefore does not invalidate this argument, and this argument does not refute that earlier narrower obstruction.

No conclusion about the general H9 Mordell–Weil bridge follows from this special-family analytic argument.

## 13. Cremona verification and reproducibility repairs

Ten public `opt_man` rows were independently located, with optimality code 1 and Manin constant 1:

\[
 62a1,66b1,114c1,254d1,258d1,4098f1,16382b1,16386a1,262142c1,262146b1.
\]

The author's Table Eight documentation defines code 1 as optimal, not merely a candidate. All these conductors are below 400,000. A second new program verifies an explicit integral u=1 change of variables from each original H41 minimal model to the quoted database equation. This is stronger identification than matching conductors or trace samples, but it does not independently recompute Cremona's optimality certificates.

Required repairs to the supplied artifact:

1. The supplied `f_side_and_opt.py` hard-codes a local `/Users/bsm/...` path and contains only the first nine cases. Its later tenth-case and Frobenius output lines are not reproducible by running that file alone. The independent scripts remove that problem for this audit's checks.
2. The output labelled “levels below 500000” includes 1,048,578. Remove that out-of-range row. The exceptional 114 case must be explicitly included in the complete bounded list.
3. The 262146 base is \(m=15\), or \(n=m+2=17\). Do not substitute \(m=17\) into its model.
4. Do not silently apply \(3\ell=1+2^{m+2}\) at \(m=7\); use \(27\ell\) there.
5. Keep the eight exact L-value certificates distinct from the ten optimality records. No new exact L-value certificate was produced here.
6. Specify the actual Česnavičius paper/version when quoting “Theorem 1.2.” For the paper read here, the direct \(J_0\) route is Theorems 1.4 and 1.5(i).

The finite enumeration script scans odd m from 3 through 21; completeness over all H41 indices below the database conductor bound uses the retained index classification, not an assertion that finite scanning controls arbitrary larger m.

## 14. Recommended successor statuses and exact review gates

```
T1_UNIFORM = INDEPENDENTLY_REDERIVED
T1_REGRESSION = PASS_10000_COEFFICIENTS
L2_ABSTRACT_TWO_COMPONENT_LEMMA = PROVED_HERE
L2_H41_MODEL_INSTANTIATION = WRITTEN_SOURCE_SUPPORTED_DERIVATION_TO_REFEREE
L1_INTEGRAL_RESIDUE_CHARACTER = PROVED_HERE_FROM_EXPLICIT_UNIFORMIZATION_ARGUMENT
P1_POSITIVE_GRAPH = TAME_COVER_DERIVATION_PLUS_INDEPENDENT_ORBIT_AND_SMITH_CHECKS
P2_STRONG_FORMAL_FACTORIZATION = NOT_REQUIRED
P2_NEEDED_ANNULAR_RESIDUE = DERIVED_BY_SLOPE_FORMULA
POSITIVE_VERTEX_AND_SEED = CANDIDATE_COMPLETE_CONVENTIONAL_CHAIN_RELATIVE_TO_RETAINED_INPUTS
POSITIVE_BSD2 = CONSEQUENCE_AFTER_LITERAL_IMPORT_AND_REVIEW_OF_RETAINED_COMPOSITION
POSITIVE_FULL_BSD = EXTERNAL_LITERATURE_QUALIFIED_CONSEQUENCE_AT_SAME_REVIEW_GATE
CANONICAL_FREEZE_CHANGE = NONE_IN_THIS_SESSION
NOVELTY = NOT_ASSESSED
```

The fresh referee should check the explicit fine-cover/coarse-model identification in §5, the integral lattice and edge-length normalization in §7, the applicability of Conrad–Stein to the actual quotient, and the literal imported vertex/torsion/descent statements. These are substantive verification gates, not merely checksum work. They are also far more specific than reopening an unrestricted W literature search.

## 15. Source register

Primary sources actually read in this session:

* M. Baker and J. Rabinoff, *The skeleton of the Jacobian, the Jacobian of the skeleton, and lifting meromorphic functions*, arXiv:1308.3864. Sections 3–4, Proposition 6.1, Theorem 2.9 / §6.2. https://arxiv.org/pdf/1308.3864
* M. Baker, S. Payne and J. Rabinoff, *On the structure of nonarchimedean analytic curves*, arXiv:1404.0279. Proposition 2.2, Proposition 2.5, Theorem 5.15. https://arxiv.org/pdf/1404.0279
* B. Conrad and W. Stein, *Component groups of purely toric quotients*. Lemma 6.3, Proposition 6.5, Theorem 8.2. https://wstein.org/papers/compgrp/compgrp.pdf
* K. Česnavičius, *The Manin–Stevens constant in the semistable case*, arXiv:1604.02165, PDF dated October 16, 2018. Theorems 1.4 and 1.5(i), §2.6, Lemma 2.7, §3.1. https://arxiv.org/pdf/1604.02165
* S. Zhai, arXiv:1409.0231v2. Introduction's least-positive-period convention and Theorems 1.5/1.7. https://arxiv.org/pdf/1409.0231v2
* B. S. Banwait and X. Huang, arXiv:2601.16044v3. Theorem 2.13 and Remark 2.11. https://arxiv.org/pdf/2601.16044v3
* J. Cremona, ecdata, Table Eight documentation and the three relevant opt_man ranges. https://johncremona.github.io/ecdata/ ; exact row URLs are recorded in `checks/cremona_model_checks.json`.

Project inputs are the named uploaded files and the Library W-audit. The original Deligne–Rapoport and Katz–Mazur passages cited inside Česnavičius were not independently read from their original editions; the fine-model source chain is expressly mediated by the primary paper actually read. No uninspected original-source page is presented as having been checked.
