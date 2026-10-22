# Load-bearing mathematical audit

Status: CONFIRMED_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE. This is a separate reader's check of the added argument. Underlying arithmetic and structural theorems remain at their supplied grades.

## 1. Domain and residual coefficients

Work with k=F_p, V=E[p], the two-dimensional point subspace W, and distinct cyclic Kato auxiliaries. The finite and transverse local conditions are complementary self-annihilating lines. Every edge is interpreted in the same residual system. No residual class is presumed to lift to an integral Selmer class.

The no-local-p-torsion condition is essential: the finite and singular local spaces at p are one-dimensional, and the normalized singular exponential is an isomorphism. Thus z=0 on W means zero full localization of the point classes, not merely zero singular coordinate. The earlier invalid controls do not meet this profile; the corrected four-point controls do.

## 2. Degenerate pairs

Suppose delta_ab is nonzero. Reciprocity makes the singular localization of kappa_ab nonzero. Residual stub membership then forces the p-strict modified group to be zero. The relaxed modified group is one-dimensional, and kappa_ab spans it with nonzero singular coordinate. Its finite-p kernel S_ab is zero.

If D_ab were zero, a nonzero vector of W would have zero coordinates at both a and b. Its full local classes at a,b would be zero, since these point classes are finite and the finite coordinate is an isomorphism. It satisfies the transverse conditions as well and gives a nonzero element of S_ab, a contradiction.

Together with the retained direct criterion for D_ab!=0, this proves the all-pairs zero pattern. This argument does not divide by a determinant, assume finite Sha, or assert that every nonzero Kato class has nonzero reciprocity image.

## 3. Pair classes in a common space

Assume z=0. The kernel of one linear functional on W has dimension at least one, even when that functional is zero. Its elements are p-strict and zero at the auxiliary. Therefore S_0,a is nonzero and kappa_a=0 by residual stub membership.

Both edges from kappa_ab have zero singular value. Kappa_ab is transverse at a,b, so complementarity gives zero full localization there. Hence it is in the common unmodified relaxed space P, killed by ell_a and ell_b. This is an equality of local conditions, not a claim of local acyclicity at Kato primes.

## 4. The comparison branch and the interpolation

Assume Sha[p]=0 within this branch only. Then S=W. Since all of W is p-strict, the relaxed/strict dimension formula gives dim P=3. The singular kernel is W, so rho_p is onto. Choose y with rho_p(y)=1.

For extended rows a=(a1,a2,h_a), b=(b1,b2,h_b), the vector

    X_ab=(a2*h_b-h_a*b2, h_a*b1-a1*h_b, D_ab)

in the basis (w1,w2,y) is their cross product. It lies in the common kernel and has singular coordinate D_ab. When D_ab!=0, that kernel is a line and

    kappa_ab=(s_ab/D_ab) X_ab,
    ell_c(kappa_ab)=s_ab*Delta_abc/D_ab.

This divides only by a chosen nonzero point determinant. It never divides by an unknown Kato class or assumes one is nonzero. Replacing y by y+w for w in W changes the coordinates but leaves X_ab as a global class unchanged.

## 5. Three-prime reciprocity and signs

Pair kappa_abc with each w_i. The p-term is zero because w_i itself is locally zero. All three auxiliary terms survive; elsewhere the finite conditions are isotropic, including the retained bad-place conditions. The odd-primary infinite-place term vanishes.

With the fixed ordered transverse/finite pairing and Kim's edge convention, the identity is

    e_a ell_a(kappa_bc) a + e_b ell_b(kappa_ac) b
        + e_c ell_c(kappa_ab) c = 0.

Here a,b,c on the right are their two-dimensional point rows. Substituting the interpolation introduces signs +,-,+, since the extended determinant is cyclic in abc and changes sign when b and c are interchanged. After cancelling the nonzero Delta_abc, the coefficient relation is

    e_a*(s_bc/D_bc)*a - e_b*(s_ac/D_ac)*b
        + e_c*(s_ab/D_ab)*c = 0.

The kernel of the two-by-three row matrix is spanned by (D_bc,-D_ac,D_ab). Comparing these coefficient vectors gives exactly the three equal ratios s_ab/(e_a e_b D_ab^2), s_ac/(e_a e_c D_ac^2), s_bc/(e_b e_c D_bc^2). No extra global sign or first-power determinant arises.

The independent exhaustive finite calculation checks the reverse implication as well: these two equations have precisely that one-dimensional family of scalar solutions. The zero solution remains present, as it must.

## 6. Arithmetic availability of connecting rows

This step is valid for three independent global cohomology classes, not only Kummer classes of points.

Let L=Q(V), G=GL_2(k). The central element -I acts by -1 on V, so the central-cocycle identity makes every cocycle on G a coboundary when p is odd. Therefore H^1(G,V)=0 and restriction to G_L is injective.

The simultaneous restricted image H in V^3 is a k-subspace, since k is the prime field, and is G-stable by conjugation. V^3 is a semisimple module consisting of three copies of the simple natural module. This uses semisimplicity of this particular module, not semisimplicity of the entire modular representation category. End_G(V)=k. A proper H would therefore be killed by a nonzero G-linear map V^3->V, contradicting the independence of the three restricted classes. Thus H=V^3.

The combined cocycle representation consequently has full affine image V^3 semidirect G. Over a nonidentity unipotent U, the three translation classes in V/(U-1)V can be prescribed. The quotient is one-dimensional. Conjugation changes the three entries by a common scalar and translations by elements of (U-1)V. Projective row conditions therefore define unions of conjugacy classes. Chebotarev realizes them at actual cyclic Kato primes outside a finite excluded set.

For shared edges ab and ad, a third point row can avoid the at most three lines a,b,d in P^1(k). Its third coordinate then avoids at most two forbidden values. At p>=5 both choices are available. This gives nonzero extended determinants for both triples. For disjoint edges, an endpoint of the second pair must be independent of an endpoint of the first; insert that connecting edge and apply the shared-edge argument. This also respects distinct prime labels by the finite exclusion clause.

The argument proves connectivity, not an effective bound on auxiliary conductors.

## 7. Both Sha branches and the scalar

Choose a determinant-nonzero anchor pair using the retained two-class detection lemma. Define C_p by its actual normalized pair class divided by the known nonzero determinant and local factors. This defines a scalar without declaring it a unit. The triple proof establishes equality with every other anchor choice in the Sha[p]=0 branch.

When Sha[p]!=0, the retained witness-length theorem makes every pair coefficient zero. C_p=0 and the comparison holds there too. Degenerate pairs were handled separately above. The final formula therefore makes no Sha-vanishing assumption, although its proof appropriately treats both cases.

The result agrees with C_p=-mu_p for the old z!=0 convention. Changes of finite coordinates scale e_q by the inverse square and D_ab by the product, leaving e_a e_b D_ab^2 invariant. A point-basis change scales C_p by det(B)^(-2), while a single singular-coordinate change rescales it linearly. These checks confirm a coherent comparison, not a canonical real or rational number.

## 8. Endpoint boundary

The general formula is dim P=d+1-epsilon, with d=dim Sel_p and epsilon the localization rank of all of Selmer, not just W. The dimension-three interpolation is only used where S=W and z=0. Excess Selmer directions cannot be removed from that dimension formula to force nonvanishing.

The supplied endpoint attempt correctly stops there. Full-system primitivity permits a first unit at length four or later. The homogeneous triple equations do not turn an identically zero pair layer into a nonzero one. This is a limitation of the proposed inference, not a universal impossibility statement about future arithmetic relations.

No claim of literature priority is made. The source package and this audit do not constitute a complete novelty screen.
