# Pairing and decision audit

Status: CONFIRMED_WITH_CORRECTIONS at the retained-input / imported-published-theorem grade. This is a new check of Claude's current section 6, not a promotion of its height interpretation.

## 1. Fixed domain and coefficients

Fix one retained weight-three specialization at a good ordinary seed prime p >= 5, excluding {19,59,487}. Write O for its coefficient DVR, pi for its uniformizer, k for its residue field, T for the specified lattice, U=T tensor L, A=U/T, and B=Sel_BK(A). Retain the checked global control and index formula:

    B[pi] = Sel_p(E/Q) tensor k,
    length B = b-a+h <= b,   h <= a,
    dim_k B[pi] = 2+s,   s=dim_Fp Sha(E/Q)[p] is even.

All lengths are O-lengths; no identification of pi-adic valuation with p-adic valuation is made. The rational points supply a two-dimensional subspace W of B[pi], whether or not Sha vanishes. The retained integral Kato adaptation and seed certificates are inputs, not re-proved here.

Set T^d=Hom_O(T,O)(1), U^d=T^d tensor L, A^d=U^d/T^d, B^d=Sel_BK(A^d). This O-dual convention matches Nekovar's coefficient convention (9.1.4); it avoids silently changing to a Z_p-dual without its coefficient dualizing lattice.

## 2. Step A: dual discrete control

Verdict: CORRECTED proof; the asserted isomorphism is valid on the retained domain.

The original ordinary filtration is

    0 -> O(alpha^-1 chi) -> T -> O(alpha chi^-1 omega) -> 0,
    alpha-bar != 1.

The dual filtration is

    0 -> (T^d)^+ = O(alpha^-1 chi^2 omega^-1)
      -> T^d -> (T^d)^- = O(alpha) -> 0.

Modulo pi its characters are alpha-bar^-1 chi-bar and alpha-bar, respectively. Thus its residual plus line is the same ordinary line under the Weil-pairing identification M^d=M=E[p] tensor k. This assertion concerns the residual representation, not a characteristic-zero self-duality of T.

The dual plus rational character has Hodge--Tate weight -2. Both it and its dual Tate twist have zero invariants, the latter having residual character alpha-bar. Local Euler characteristic and the Bloch--Kato dimension formula therefore give

    H_f^1(Q_p,(U^d)^+) = H^1(Q_p,(U^d)^+),   dimension 1.

The dual minus character has no invariants. Hence this plus cohomology injects into H^1(Q_p,U^d); its image is H_f^1(Q_p,U^d), also of dimension one. Integral local duality gives H^2(Q_p,(T^d)^+)=0: its discrete dual Tate twist has nontrivial residual unramified character alpha-bar. All invariants of (A^d)^+, (A^d)^-, A^d vanish. Consequently the propagated discrete finite condition is exactly

    image H^1(Q_p,(A^d)^+)
      = ker(H^1(Q_p,A^d) -> H^1(Q_p,(A^d)^-)).

Multiplication by pi identifies the pullback to M^d with image H^1(Q_p,(M^d)^+), the seed's Kummer line. Merely citing maximal isotropy of the residual line would not by itself prove this propagation statement; the invariant and H^2 vanishings supply it.

At bad q != p, the retained domain gives H^i(Q_q,M)=0 for i=0,1,2. The same holds for M^d and then H^1(Q_q,A^d)=0. At q not dividing Np, the representation is unramified; the image of rational unramified cohomology is the discrete unramified condition. Inertia injectivity for M^d -> A^d identifies its residual pullback with the usual unramified condition. At infinity p is odd. Residual irreducibility gives H^0(Q,A^d)=0, so global multiplication by pi is an isomorphism onto pi-torsion. These facts prove

    B^d[pi] = Sel_p(E/Q) tensor k.

In particular the same rational points define W^d inside B^d[pi] for every prime in the domain. Changes of the retained residual identifications by scalar units do not affect any rank or vanishing statement below.

## 3. Step B: an actual perfect pairing

Verdict: CORRECTED citation and applicability argument; perfectness holds.

The bibliographic reference is Flach, J. reine angew. Math. 412 (1990), 113-127, not Inventiones 99. This audit verified the construction and its duality in Nekovar, Selmer complexes: 10.8.1-10.8.7 (comparison with Flach), together with 10.2.3. It did not obtain and re-read Flach's original full article.

Bloch--Kato Proposition 3.8 supplies rational finite-condition orthogonality and compact/discrete orthogonality. The preceding ordinary calculation realizes the two p-local conditions by exactly orthogonal saturated submodules. At bad primes in Sigma, the full local complexes are acyclic: their reductions are acyclic and integral local cohomology is of finite type. They cause no local duality error. Outside Sigma the global complex imposes unramifiedness. The odd-p hypothesis removes the real-place complication.

Thus the ordinary Selmer complexes for T and T^d have exact dual local conditions, with zero duality-error complexes. Nekovar 10.2.3, with i=j=2 and R=O, gives perfect duality on their torsion H^2 groups. Over a DVR the pseudo-null qualification contributes no nonzero finite-type modules. The vanishing invariant terms identify the classical discrete Selmer groups modulo divisible parts with these torsion groups. Nekovar 10.8.7 identifies this pairing with Flach's, up to the harmless displayed sign.

Kato 14.2(1) applies to the retained direct twist r=1 and to its dual, r=2 for the dual weight-three form. Both are noncentral; B and B^d are finite. Their divisible subgroups vanish. We therefore obtain an O-bilinear perfect pairing

    C : B x B^d -> L/O.

Kato 14.16(1) is a compatible equality of orders. Equality of orders alone would not establish the pairing.

## 4. Step C: restriction to pi-torsion

Verdict: CONFIRMED.

Choose cyclic generators x_i and their perfect dual generators y_i, with orders pi^e_i and C(x_i,y_j)=delta_ij pi^(-e_i) modulo O. The pi-torsion generators are pi^(e_i-1)x_i and pi^(e_i-1)y_i. Their paired value is delta_ij pi^(e_i-2) modulo O. It is nonzero precisely when e_i=1. Hence

    rank_k C restricted to B[pi] x B^d[pi] = #{i : e_i=1}.

Values are identified with k via j_pi:(L/O)[pi] -> k, sending x+O to pi*x modulo pi*O, using a representative x in pi^-1 O. Multiplication by pi *inside L/O* would give zero and is not the identification meant here.

This is valid for ramified coefficient DVRs too; no alternation or characteristic-zero self-duality of T is assumed.

## 5. Step D and the repaired proposition

Verdict: CORRECTED definition; the implications hold.

Define beta on W x W^d for every admitted prime by pulling back j_pi o C under the two Kummer/control embeddings. Call this the restricted generalized Cassels--Tate pairing. Its identification with a particular deformation Bockstein or p-adic height is a separate issue.

If b<=3, then length B<=3 and even s force s=0. Thus B[pi]=W, B^d[pi]=W^d, and B has exactly two cyclic summands. Their exponents are either (1,1) or (1,2). Step C gives beta of rank 2 or 1. If b<=2, the exponents must be (1,1) and beta is nondegenerate. Accordingly:

    b<=3 => Sha[p^infinity]=0 and rank beta>=1;
    b<=2 => Sha[p^infinity]=0 and rank beta=2;
    beta=0 => b>=4.

The last implication is now meaningful even when Sha[p] is nonzero, because beta was defined on the point subspaces without assuming Sha=0. Vanishing of Sha[p] kills the whole p-primary group: any nonzero p-primary torsion group contains an element of order p.

There is no converse asserted. Even with s=0, B=O/pi plus O/pi^n, n>=3, has rank beta=1 and length at least 4. With s>0, a nondegenerate restriction on W can coexist with additional directions in B. No new prime or uniform bound follows.

## 6. A precise lifting interpretation, requiring no height formula

For any perfect finite-module pairing, the radical on the left of its restriction to pi-torsion is

    B[pi] intersect pi B = pi B[pi^2].

Indeed B^d[pi] is the dual of B/pi B; intersect its annihilator pi B with B[pi]. If x=pi y is killed by pi, then y is killed by pi^2, which gives the second equality.

Define Sel_2 using A[pi^2] with local conditions pulled back from the fixed discrete group A. Since H^0(Q,A)=0, Sel_2=B[pi^2]. Under A[pi^n]=T/pi^n via division by pi^n, coefficient reduction T/pi^2 -> T/pi corresponds to multiplication by pi. Therefore the radical above is precisely the image of Sel_2 in the residual Selmer group.

If s=0, rank beta counts the point directions which do not lift from T/pi to T/pi^2 with these auxiliary local conditions. For s>0, use the full pairing on B[pi] x B^d[pi] for this radical statement; its restriction to W x W^d alone can have a larger radical.

This explains a concrete operation: test lifting Kummer cocycles in the actual T/pi^2 representation with propagated local conditions. It is not the automatic lifting of rational points in E[p^2]. No algorithm for this seed's varying representations, computed matrix, or uniform nonvanishing theorem is supplied by the present audit.

## 7. Why the proposed height identification is unproved

Residual agreement with E[p] does not specify an isomorphism or a first derivative modulo pi^2. The expression `T = T_E + p*(D_wt-theta) mod pi^2` needs a common integral deformation representation, coefficient identification, a first-order specialization map and compatible local splittings. None is constructed in section 6. A tangent in an endomorphism module is not automatically a scalar cyclotomic height direction. The local and global comparison with the chosen height pairing still requires proof.

Also p and pi need not agree. In ramification index at least two, p is already zero modulo pi^2. The printed expression cannot simply stand for every first-order deformation over the coefficient DVR.

A concrete normalization control: after finite ramified coefficient extension O -> O' of ramification e, finite flat base change gives B'=B tensor O' and exponents e*e_i. The corresponding a,h,b scale by e. For e>=2 the pairing restricted to pi'-torsion is identically zero, even if it was nondegenerate before extension. For example (O/pi)^2 becomes (O'/pi'^2)^2 when e=2. The seed's residual Selmer dimension is unchanged. This is compatible with all the propositions, but shows why the residue pairing and its threshold must be attached to the pinned coefficient lattice and specialization, not presented as an already normalized intrinsic height of the points.

Finally, nonzero matrix (rank>=1) and nondegenerate regulator (rank=2) are different statements. The b<=3 implication only gives the former. Even a valid cofinite nonvanishing theorem for this pairing would not by itself bound higher exponents or Kato's slack.

The assertion that the route must solve a separate known height conjecture, is necessarily harder, or cannot be a shortcut is not proved. A stronger sufficient condition can have an independently accessible proof. Parking a route for lack of such a proof is a resource judgment, not a consequence of the necessary-condition lemma.

## 8. Decision bundle: exact accounting and scope

The supplied zip's seven manifest entries verify. Its Claude snapshot is the earlier sections 1-5, not current section 6. Consequently its discussion of E1/E2 is not an audit of the new proposition. Its independent accounting does not need that proposition.

For each fixed admitted specialization define

    t=length B-dim_k B[pi]=sum_i(e_i-1)>=0,
    d=a-h>=0.

Then the retained identity immediately gives

    b=2+s+t+d,
    b<=3 iff s=0 and t+d<=1.

This is correct with retained even s. It neither identifies t with a height nor proves a converse from Sha=0. The examples in the zip realize the abstract rank-one exact sequence: take H=Q=O, H->Q multiplication by pi^e_1, H^2 the sum of the remaining cyclic summands, and z=pi^a in H. They are not asserted arithmetic realizations. All 1,475 supplied checks replayed exactly.

When s=0, the pairing rank sharpens the bookkeeping only as follows:

    rank beta=2 iff t=0;
    rank beta=1 implies t>=1, with no upper bound on t;
    rank beta=0 implies t>=2.

Thus the new pairing condition is consistent with the decision's diagnosis; it does not turn it into an impossibility theorem.

The pasted decision text reuses s_p first for dim Sha[p] and later for a residual scalar congruent to a rational m. That is a substantive notation collision. Replace the latter scalar by mu_p and include its independently proved nonvanishing implication. No equality between the existing differently normalized scalars is assumed. The zip's prose already avoids making that equality.

FIN, ORDER9 and Q36 are unchanged.
