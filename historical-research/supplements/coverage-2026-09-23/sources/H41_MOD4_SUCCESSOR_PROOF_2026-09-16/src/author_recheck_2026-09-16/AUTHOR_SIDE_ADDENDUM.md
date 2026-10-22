# H41 successor: author-side source audit and explicit bridge lemmas

Date: 16 September 2026.

**Status:** Author-side recheck and proposed proof amendments. This is not an independent referee report, not a canonical freeze, and not a report on the external referee that the user says is still running. The preceding reconstruction was produced in this same conversation.

**Snapshot examined:** the uploaded `PROOF.md`, SHA-256
`0cf7a5f9e598d8d8f722fc2a238d03e7cd24dacdafd6c57631c6c01f7c955043`.
The original file is preserved unchanged under `inputs/`. The claimed nine-entry successor manifest was not attached; this package does not certify it.

## 1. Finding and boundary

The source correction concerning the Manin constant is correct. I read the stated theorem in arXiv:1703.02951v3, including its actual quantifiers. The previously proposed replacement based on 1604.02165 was not a correction to that citation: it was an alternative argument from a different paper.

The supplied arithmetic regression script runs successfully here, without ecdata. Its non-database output agrees with the supplied output, after removing only the explicitly database-dependent suffixes. This is a replay of the supplied implementation, not another independent implementation.

The two especially compressed geometric passages can be expanded as below:

* the functoriality in G2 follows by lifting the quotient to analytic universal covers, identifying its torus character, and checking tropicalization on the torus and on the compact identity subgroup;
* the fine chart in G1 can be obtained from the fine Gamma_1(6 ell) model by an explicitly finite-etale forgetting map on the elliptic locus. Only a local coarse quotient near supersingular points is needed. Its tame invariant ring can be computed by choosing an eigenparameter.

These are proposed author-side derivations to be checked by the independent referees. They are not verbatim H41 theorems printed in the cited papers. No additional family-wide arithmetic hypothesis is introduced by them.

The literal project imports I1-I5 and I12, and the negative graph input, remain imports. A targeted Library search recovered the W-audit but not the complete original proof/freeze packets for all these assertions. Hence this recheck does not independently certify G7 or the complete composed BSD theorem.

## 2. Manin constant: corrected source attribution

Source [C17], Theorem 1.2 (= Theorem 2.13), says that for a **new elliptic optimal quotient**

\[
 \pi:J_H\twoheadrightarrow E,\qquad \Gamma_1(N)\subset H\subset\Gamma_0(N),
\]

and a prime p with p^2 not dividing N, one has v_p(c_pi)=0; it also asserts smoothness of the induced map on Neron models over Z_p.

The single-prime statement is not literally `c_pi = +/-1`. That conclusion follows by applying the theorem at every prime when N is squarefree. Both N=2p and N=6 ell in the proposed H41 statements are squarefree, including the exceptional base of conductor 114. The large exponent of 3 in the exceptional discriminant is not an exponent in its conductor.

Thus I7 may remain:

> C17, Theorem 1.2 / 2.13; new elliptic optimal quotient; squarefree conductor; therefore c_pi = +/-1.

C16 Theorems 1.4 and 1.5 provide the separately identified alternative. No repair of the mathematical Manin input is required.

## 3. The missing functoriality sentence in G2: an explicit proof

Use R_0=W(Fbar_2), K_0=Frac(R_0), and retain the normalization v(2)=1. For the analytic argument pass to a complete algebraically closed valued extension K of K_0. Do not renormalize the valuation after this extension. The split torus character lattices are still the same integral lattices.

Let A be the source abelian variety (in the application J) and let E be the target split multiplicative elliptic curve. Write their analytic uniformizations as

\[
 p_A:\mathcal E_A^{an}\longrightarrow A^{an},\qquad
 p_E:\mathbf G_m^{an}\longrightarrow E^{an}.
\]

Let T_A be the torus in the Raynaud extension and A^0 the compact analytic identity subgroup embedded in that extension. These objects and their properties are supplied by BR sections 4.1-4.2. In particular the formal torus in A^0 and T_A have the same character lattice as the toric part of the special fibre of the Neron model.

### 3.1 Lift the actual morphism

The composite pi o p_A lifts uniquely, with the identity as chosen base point, to

\[
 \widetilde\pi:\mathcal E_A^{an}\longrightarrow\mathbf G_m^{an}.
\]

This follows from the universal-cover property in BR 4.1. Since both covering maps are local analytic isomorphisms, the lift is analytic. Uniqueness of the identity-preserving lift, applied to the multiplication diagram, shows it is a group homomorphism. This is a topological-cover argument, not an assertion that all etale coverings are topological coverings.

Its restriction to T_A is an analytic character, hence an algebraic character. BR explicitly uses the algebraicity of analytic torus characters in the proof of Proposition 4.7. Call this character u.

**Identification with the actual Neron pullback.** The map pi extends to the Neron models and takes their identity components into one another. Completing these identity components gives the canonical map A^0 -> E^0. For the Tate target, E^0 is the image of the unit affinoid torus T_{E,0} under the Tate cover, and that restriction of the cover is an isomorphism. Therefore the restriction of the identity-preserving lift to A^0 agrees with the generic fibre of this formal map. On the formal torus, reducing the character u gives exactly the map on special-fibre tori induced by pi. Hence

\[
 u=\pi^*\xi\in X_A,
\]

where xi is the character T of the target torus. This comparison identifies the **character lattice**, not the period lattice of the analytic covering.

### 3.2 Verify tropicalization, rather than assuming it

Consider the two real-valued homomorphisms on points of the covering group:

\[
 y\longmapsto v(\widetilde\pi(y)),\qquad
 y\longmapsto \operatorname{trop}_A(y)(u).
\]

On T_A(K) they agree by the definition of the character u and of tropicalization in BR 4.2.

On A^0(K) the second is zero by definition. The first is zero as well: A^0 is compact, so the continuous real-valued function v o tilde-pi is bounded on A^0; its values on the subgroup A^0(K) form an additive subgroup of R. A bounded additive subgroup is zero (otherwise integral multiples of a nonzero value are unbounded).

BR's proof of Proposition 5.3 uses the decomposition

\[
 \mathcal E_A(K)=T_A(K)+A^0(K).
\]

For a general split Raynaud extension this is the same pushout decomposition from BR 4.1-4.2. Thus the two homomorphisms agree everywhere. Applying the argument over valued extensions, or using continuity and density of classical points over K, gives the analytic identity

\[
 \boxed{\operatorname{trop}_E(\widetilde\pi(y))(\xi)
       =\operatorname{trop}_A(y)(\pi^*\xi).}
\]

This supplies the sentence marked `REFEREE GATE` at the end of successor section 6. It does not require A to have purely toric reduction, nor require pi to be an isogeny.

### 3.3 Residue and length normalization

BR Proposition 6.1 and Theorem 2.9 identify the tropical Abel-Jacobi map with integration of integral harmonic forms along the metric graph. For the edge parametrized by t=v(U), differentiation of integration against u is u_x. Therefore the slope of the lifted target Tate coordinate is u_x.

By BPR Proposition 2.2, on a closed subannulus its analytic lift is

\[
 g=\gamma U^{w}(1+h),\qquad |h|_{sup}<1.
\]

In characteristic zero log(1+h) converges there, so

\[
 \operatorname{Res}(d\log g)=w.
\]

The slope of v(g) is the same integer w. Consequently, if the minimal differential pulls back to a dT/T with a in R_0^*, then

\[
 \boxed{\operatorname{Res}_x(\phi^*\omega_E)=a u_x.}
\]

A different Tate lift multiplies g by a constant power of the Tate period. It changes neither slope nor residue. There is no edge-length factor in this derivative. Traversing the full edge of length e_x produces e_x u_x.

**Regular versus coarse graph.** BR Theorem 2.3 is stated in its discrete discussion for a regular model, with unit edges. A coarse node UV=2^e is handled either by the metric form of Theorem 2.9 or by resolving it into e unit edges. The integral cycle identification repeats the same coefficient on all edges of the resulting path. Thus its pairing contribution is e z_x u_x, with no lattice index or extra factor of two. The proof should record this bridge instead of applying the regular-model formulation verbatim to a singular total space.

## 4. Fine model and tame quotient in G1

This section expands the source-to-model passage; it is a derivation from C16 and the stated modular interpretation, not a claim that C16 prints this H41 quotient theorem.

### 4.1 Obtain the fine chart by an explicit etale map

On the elliptic locus, start with the fine Gamma_1(6 ell) curve. C16 section 2.6 gives

\[
 \Gamma_1(6\ell)=\Gamma_0(2)\cap\Gamma_1(3\ell),
\]

and gives the semistable, regular scheme description at 2; sections 3.1 and 3.8 further spell out representability and transversal intersections. As 3 ell >=5, the auxiliary point kills automorphisms.

By the prime-to-2 decomposition of its 3 ell-level point, the elliptic moduli are

\[
 (E,C_2,P_3,P_\ell).
\]

Forgetting the generator P_3 while retaining C_3=<P_3> gives

\[
 (E,C_2,P_3,P_\ell)\longmapsto(E,C_2,C_3,P_\ell).
\]

Its fibre is the scheme of generators of the nonzero cyclic 3-subgroup. This is finite etale of degree two over a base of residue characteristic two: the relevant group scheme is etale because 3 is invertible. **Degree two does not make this particular etale torsor ramified.** Near a geometric supersingular point the source and target completed strict local rings are consequently isomorphic. Thus the target fine model Y has chart

\[
 R_0[[x,y]]/(xy-2).
\]

This uses the explicit C16 source chain. I have not read KM 13.4.7 from the original book, and do not certify that locator. It is unnecessary to leave that unverified locator as the only support for I11.

### 4.2 Require only the local coarse quotient

Forgetting the choice of generator of C_ell gives the effective diamond group

\[
 G=(\mathbf Z/\ell\mathbf Z)^*/\{\pm1\}.
\]

The central -1 acts trivially on the fine moduli scheme, through the isomorphism [-1] between the corresponding marked elliptic curves. Hence the coarse quotient is Y/G on the elliptic locus. Its order (ell-1)/2 is odd. We only need this statement near supersingular points; a separate assertion about all compactification charts is unnecessary. Smooth cusps and the two global components are supplied by I8.

For completeness, on y^2+y=x^3 in characteristic two the origin-preserving automorphisms have the form

\[
 x\mapsto a^2x+s^2,\qquad
 y\mapsto y+a^2s x+t,
 \quad a\in\mathbf F_4^*,\ s\in\mathbf F_4,\ t^2+t=s^6.
\]

Substitution verifies these formulas, and comparison with a general Weierstrass change of coordinates gives all 24 automorphisms. The two t choices differ by the central involution. The four cyclic 3-subgroups correspond to the roots of x^4+x, and the effective x-action is AGL_1(F_4)=A_4. A stabilizer of C_3 is cyclic of order three. Imposing C_ell therefore leaves effective stabilizer 1 or 3, as in the submitted proof.

For a nontrivial order-three automorphism alpha, alpha^2+alpha+1=0 in End(E). On E[ell] its eigenvalues are the nontrivial cube roots when ell=1 mod3, and it has no eigenlines when ell=2 mod3. Thus it fixes two ell-lines or none. On E[3] it is nonidentity unipotent (alpha-1 has degree three, so cannot annihilate all nine points), hence has one fixed line. This also derives the uniform orbit counts, rather than extrapolating three finite tests.

### 4.3 An eigenparameter proves the invariant chart

For an order-three stabilizer of the fine nodal ring, its action preserves the two branches. Its tangent action is faithful: an order-prime-to-two automorphism trivial on the cotangent space is trivial successively on every power of the maximal ideal, and hence on the complete ring. The branch characters are nontrivial inverse cube roots, since xy=2 is invariant.

Choose a parameter x of one branch. Averaging x with the appropriate order-three character gives an eigenparameter x' in (x) with x'/x a unit. Put y'=2/x', which lies in (y) and is a parameter for the other branch. Then

\[
 \sigma(x')=\zeta x',\qquad \sigma(y')=\zeta^{-1}y',\qquad x'y'=2.
\]

The invariant monomials are generated by U=(x')^3, V=(y')^3 and x'y'=2. Therefore

\[
 (R_0[[x',y']]/(x'y'-2))^{\langle\sigma\rangle}
       \simeq R_0[[U,V]]/(UV-8).
\]

For trivial stabilizer the exponent is one. This gives the actual coarse thicknesses e_x in {1,3}.

The mass, Schur-complement and cusp-generator arguments in successor section 4 then apply. In particular h_3=2 when ell=1 mod3 and h_3=0 otherwise; h_1=(ell-1)/3 or (ell+1)/3 respectively. Thus h_1+h_3/3=(ell+1)/3 exactly.

The referee must still accept this modular-to-local-ring derivation; the finite group computation alone is not a proof of that passage.

## 5. An important wording repair: residue means Laurent constant coefficient

Successor line 105 calls the annular residue the constant term of g in

\[
 g\,dU/U,\qquad g\in R_0[[U,V]]/(UV-2^e).
\]

This must mean the Laurent constant coefficient after V=2^e/U, or the constant coefficient in the unique reduced normal form

\[
 g=c+\sum_{n\ge1}a_n U^n+\sum_{n\ge1}b_n V^n.
\]

It is **not** the coefficient a_00 of an arbitrary bivariate representative. If g is represented by sum a_ij U^i V^j, its residue is

\[
 \boxed{\sum_{i\ge0} a_{ii}\,2^{ei}\in R_0.}
\]

The sum converges 2-adically. For example UV dU/U has residue 2 when e=1, not zero. Neglecting that term would change a mod-4 residue.

This does not invalidate the present chain: it only uses R_0-linearity and integrality of the residue to send a differential divisible by four to 4R_0. Those facts follow immediately from the correct formula. It also uses the analytic-unit residue calculation, which is unaffected.

## 6. Component map: derive the exact image directly from Conrad-Stein

Let M=X_J and u=pi^*xi. Let n_0=ord_2 Delta_min(E_0), and write u=kappa v with v primitive and kappa>0. Conrad-Stein Lemma 6.3 and Theorem 8.2, for the actual optimal quotient, give

\[
 M\xrightarrow{z\mapsto\langle z,u\rangle}\mathbf Z
     \longrightarrow\Phi_{E_0}\longrightarrow0,
 \qquad\langle M,u\rangle=n_0\mathbf Z.
\]

In the compatible monodromy diagram the map on dual lattices is

\[
 \operatorname{Hom}(M,\mathbf Z)\longrightarrow\mathbf Z,
 \qquad f\longmapsto f(u).
\]

Its image is exactly kappa Z. Since the image of the monodromy sublattice is n_0 Z, one also obtains kappa | n_0. Therefore

\[
 \boxed{\operatorname{im}\Phi(\pi)=\kappa\mathbf Z/n_0\mathbf Z,
 \qquad |\operatorname{im}\Phi(\pi)|=n_0/\kappa.}
\]

This is the `gcd(kappa,n_0)` formulation with the divisibility made explicit. It avoids making the elliptic consequence depend on an unspecified reformulation of a separate project Lemma 4.1. On a two-vertex weighted graph one may equivalently write

\[
 n_0=\gcd_{x,y}(e_xu_x-e_yu_y),
\]

using the cycle basis consisting of differences of edges. This shows directly why the common mod-four value yields 4 | n_0. The source and target must remain the actual optimal quotient, not an arbitrary isogenous elliptic curve.

Positive branch: v_2(kappa)=1 and v_2(n_0)=2 yield image order two at its 2-part. Negative branch: v_2(kappa)=0 yields image order four. The retained cusp-generator and real-identity-component bounds give t=2 and t=4 respectively, and the retained real logarithm formula gives the two seeds.

## 7. Regression replay and a failure-detection defect

The original script completed in approximately five seconds. It reproduced the reported 4,000 coefficient checks, the graph cases ell=11,19,43, the 112 retained curve/prime pairs, and the Frobenius exclusions. The 112 count is a count of **curve-prime pairs**, not necessarily 112 distinct prime numbers.

The ecdata directory is not in the mounted packet. Consequently the current replay explicitly says `ecdata not supplied`; it does not recheck the database labels/optimality/Manin flags. The arithmetic portions of all output lines agree with the supplied output.

There is a real harness defect: the original script computes `ok` and prints it without raising when false. The component order/cyclicity and database flags are likewise printed without enforcing the expected values. Hence exit code zero is not, by itself, a reliable all-checks-pass certificate. The supplied output has the desired values; this finding is about failure detection, not a contrary numerical result.

The separately supplied `checks/run_all_checks_fail_closed.py` adds explicit exceptions for those outcomes and an explicit final database status. It does not alter the original script or proof. It runs successfully here and reproduces the same non-database results. The patch still retains some of the original assertions; run it with normal Python, not `-O`/`PYTHONOPTIMIZE`.

## 8. What the external referees must receive

Retain the first referee's no-repair review of its original hash. Do not retroactively describe a review of that hash as covering amendments added later. If this addendum is incorporated into a revised proof, both referees need to cover the final mathematical text, either directly or via an explicit review of the delta.

Bind I1-I5, I12, and the negative graph input to their actual statements and immutable source identifiers. Merely listing a local pathname is not a literal-import check. This is not an instruction to redo the established arithmetic proofs; it is an instruction to make the exact imported propositions available to the referee.

Operational status after this author-side pass:

```
MANIN_SOURCE_1703_02951_V3        = VERIFIED; EARLIER CITATION OBJECTION WITHDRAWN
G2_FUNCTORIALITY                 = EXPLICIT AUTHOR-SIDE PROOF SUPPLIED
G1_FINE_CHART                   = EXPLICIT FINITE-ETALE SOURCE BRIDGE SUPPLIED
G1_TAME_INVARIANT_CHART          = EIGENPARAMETER DERIVATION SUPPLIED
RESIDUE_INTEGRALITY              = VALID WITH LAURENT-CONSTANT WORDING
CONRAD_STEIN_COMPONENT_IMAGE     = DIRECT ELLIPTIC DERIVATION SUPPLIED
SUPPLIED_ARITHMETIC_REPLAY       = PASS; NOT A NEW INDEPENDENT IMPLEMENTATION
DATABASE_REPLAY                 = NOT PERFORMED; ECDATA NOT ATTACHED
LITERAL_IMPORTED_FREEZES         = NOT FULLY REPLAYED HERE
INDEPENDENT_REFEREE_COUNT_ADDED  = ZERO
CANONICAL_SEAL_CHANGE            = NONE
```

The candidate theorem still concerns the stated H41 bases and the exact retained prime twists. No novelty, infinitude of H41 bases, arbitrary-twist, general BSD, or H9 conclusion follows from this recheck.

## Source register

[C17] K. Cesnavicius, *The Manin constant in the semistable case*, arXiv:1703.02951v3, Theorems 1.2 and 2.13. Read through public PDF retrieval; theorem page visually checked.

[C16] K. Cesnavicius, *The Manin-Stevens constant in the semistable case*, arXiv:1604.02165, sections 2.6, 3.1, 3.8 and Lemma 2.7. Read through public PDF retrieval; section 3.8 visually checked. This source itself cites DR and KM. The original books were not independently inspected.

[BR] M. Baker and J. Rabinoff, arXiv:1308.3864v1, supplied text; sections 2.1 and 2.7, Theorems 2.3 and 2.9, sections 4.1-4.2, Proposition 4.7, proof of Proposition 5.3, Proposition 6.1.

[BPR] M. Baker, S. Payne and J. Rabinoff, arXiv:1404.0279v1, supplied text; Proposition 2.2 and Theorem 5.15. The statement of Theorem 5.15 was retrieved from the full attached file rather than inferred from a truncated extract.

[CS] B. Conrad and W. Stein, *Component groups of purely toric quotients*, supplied text dated April 21, 2003; sections 4.1 and 6, Lemma 6.3, Proposition 6.5, Theorem 8.2.

The additional public Gubler and Foster-Rabinoff-Shokrieh-Soto PDFs screened during the bounded search were not needed to establish an extra H41 theorem and are not made dependencies of this addendum.
