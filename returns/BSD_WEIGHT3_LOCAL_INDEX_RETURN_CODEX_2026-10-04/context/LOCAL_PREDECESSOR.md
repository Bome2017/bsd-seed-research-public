# Independent calculations

## A. Balanced weights

For lambda=(A,B,C) dominant and rho=(1,0,-1), directly permuting lambda+rho and subtracting rho gives

    s_2 dot lambda = (A,C-1 | B+1),
    s_1 dot lambda = (B-1 | A+1,C).

Each GL2 block has highest-weight difference A-C+1, hence modular weight A-C+3. Since A>=C, this is at least three. A common shift does not alter the difference. At lambda=0 the (2,1) representatives in lengths 0,1,2 have blocks (0,0), (0,-1), (-1,-1), hence weights 2,3,2. This is an all-weight argument; the 286 finite cases only check the implementation.

Harder–Raghuram's combinatorial lemma assumes strongly-inner cuspidal data with disjoint cuspidal parameters. Its balanced condition is not a statement about every torsion or unbalanced construction. The independent GL3 calculation gives the necessary weight obstruction without dropping those distinctions.

## B. Ordinary specialization and coefficient conventions

Write L/Q_p for a coefficient field of g, O for its ring of integers, varpi for a uniformizer, and k for its residue field. Replace the shorthand Q_p in the supplied rank-one characters by L; this does not assume g has rational eigenvalues.

In the stated Hida convention, a branch through (2,1) with trivial nebentypus has theta=1. A specialization at (3,1) therefore has nebentypus omega^(-1). The finite-flat ordinary setup supplies such arithmetic points after finite coefficient extension. Classicality/control and residual absolute irreducibility give the retained residual representation, up to coefficient extension. No etaleness of the branch or computation of its eigenvalues is needed for this existence statement.

The determinant is chi^2 omega^(-1), and the ordinary quotient is the unramified character alpha. Thus after division by eta_1=chi omega^(-1), the two characters are exactly

    A=L(alpha^(-1)chi),   B=L(alpha chi^(-1)omega).

The use of geometric Frobenius in the L-function convention inverts the finite Galois character relative to its arithmetic Dirichlet notation. With that convention the s=2 criticality test is correct; it is not yet an identification of a normalized congruence scalar.

## C. Non-anomaly for this seed

The curve is y^2=x^3-22735*x^2+106272484*x. The point (0,0) is rational two-torsion and reduces to nontrivial two-torsion at every good odd prime. Thus #E(F_p) is even.

For p>=7, the Hasse bound gives 0 < #E(F_p) < 2p. If p divided this order it would equal p, which is odd, a contradiction. For p=5 the affine fibre sizes at x=0,1,2,3,4 are 1,1,2,2,1, respectively; adding infinity gives 8. Consequently p does not divide #E(F_p) at any good p>=5. In the ordinary case this ensures alpha-bar!=1. The two ordinary residual characters are distinguished on inertia because one has the cyclotomic factor and the other is unramified.

This concerns local torsion and the shape of local cohomology. It does not assert that any particular rational point has nonzero image in E(Q_p)/p.

## D. Rational local extension space

Use HT(chi)=-1. The weights of U are {-1,1}; its de Rham tangent quotient has dimension one. The residual characters of A and B have no invariants: bar(A)=bar(alpha)^(-1)bar(chi) is ramified, while bar(B)=bar(alpha) is unramified and nontrivial. In particular U has no invariants.

Bloch–Kato gives h_f^1(U)=1. For A, local Euler characteristic and absence of invariants in A and A^*(1)=L(alpha) give h^1(A)=1; its negative weight gives h_f^1(A)=1. Since H^0(B)=0, H^1(A) injects into H^1(U), and functoriality identifies its image with H_f^1(U).

Dualizing and twisting gives

    0 -> B^*(1)=L(alpha^(-1)chi^2 omega^(-1))
      -> U^*(1) -> A^*(1)=L(alpha) -> 0.

The submodule's crystalline module is zero because its finite inertial character is nontrivial. The quotient is unramified but has no phi=1 vector, since alpha is not 1. Left exactness therefore gives D_cris(U^*(1))^(phi=1)=0. The H_g dimension formula yields H_g^1(U)=H_f^1(U). U itself is not asserted crystalline.

## E. Integral reduction

Let T_U=T_g eta_1^(-1) with its saturated filtration 0 -> T_A -> T_U -> T_B -> 0. Since H^0(k(B))=0, H^1(T_B) has no varpi-torsion. Thus the image of H^1(T_A) in H^1(T_U) is saturated: the quotient embeds in H^1(T_B). It is exactly the inverse image of the rational subspace H^1(A), so it equals the integral H_g submodule.

Local duality and H^0(k(A)^*(1))=H^0(k(alpha))=0 give H^2(T_A)[varpi]=0. Therefore H^1(T_A) reduces onto H^1(k(A)). The latter injects into H^1(k tensor E[p]) because H^0(k(B))=0, and it has dimension one by local Euler characteristic.

The ordinary residual filtration matches that of E[p]. Repeating the rational calculation with the ordinary filtration of V_pE identifies this image with the reduction of H_f^1(T_pE), which is the classical Kummer line E(Q_p)/p. This proves the local claim independently, without asserting control of the discrete global Selmer group of U.

## F. Conditional length test and Taylor control

For a finite-length O-module A_g, length_O(A_g) >= dim_k A_g[varpi]. Thus a proved identification A_g[varpi] = Sel_p(E/Q) tensor k would imply length at least two. Any upper bound by v_varpi(L_g) would therefore force v_varpi(L_g)>=2. Neither the global identification nor that upper bound is supplied by local compatibility alone.

For integral F(T)=sum_{n>=2} c_n T^n and T=pu, termwise convergence gives F(pu)/p^2 = c_2*u^2 mod p. This proves the unit criterion, even if F(pu)=0 is allowed with infinite valuation.

For S(T)=T^2/(1+T), substitution T -> -T/(1+T) fixes S. At v_p(T)=1, v_p(S)=2. In F_p=p^3*S+S^2 the two terms have distinct valuations 5 and 4, so v_p(F_p)=4, while c_2=p^3. This is a proof for every p and every such T, not just the ten finite examples. It is a formal countermodel, not a seed p-adic L-function.

FIN, ORDER9 and Q36 are unchanged.
