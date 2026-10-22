# A numeric companion upper bound obtained through the source

## 1. Inputs and grade

Use the original seed and full-GL2(F3) incidence construction retained in the parent return. Let A be its nonzero3-torsion point field and B its affine-line companion field. Let tau be scalar -1, and project all3-adic lattices and finite groups with the integral idempotent (1-tau)/2. Use all primes above the same rational set S={2,3,2243,4547,5843}.

The exact field A used by the cache is

    y^8-1188376638*y^4-7030398068360*y^2-117686586145348587.

The current companion field is

    z^8-171126235872*z^4+12148527862126080*z^2
       -2440349050309948300032.

The retained incidence identities vu=uv=3 hold on the complete minus unit/divisor lattices. The independent primitive divisor calculation gives t_D=1. The retained S-unit index identity is

    s_AS = 1+t_D+c_BS-c_AS,                         (1)

where c denotes actual minus3-class length and s_AS is the actual integral index length of u:U_AS^- -> U_BS^-; it is not a rank computed from a selected set of Selmer classes. The parent independent_index/PROOF.md supplies the derivation, including the number-field class-number formula and exact S-divisor correction. This written theorem is imported, not re-proved or independently recertified here.

The source cache has an unrecertified class presentation [12,6,2]. We retain precisely its existing GRH-dependent completeness grade. The conditional assertions below assume this presentation describes the full ordinary ideal class group with its named generators and prime-class coordinates. They do not assume a bound for Sha or a norm kernel.

## 2. Exact source arithmetic

The cached presentation records the involution

    T=diag(5,5,1)

on the generators of orders12,6,2. Its minus quotient has invariant factors [6,6,2], so the minus3-length is2. The source-prime class-coordinate matrix, with columns ordered as the exact idealprimedec outputs over S, is

    [3,9,6,2,10,0,9,0,6,6,0;
     3,3,0,4, 2,0,0,3,2,4,0;
     0,1,0,1, 1,0,0,1,1,1,0].

Adjoining these columns to diag(12,6,2) gives an integer lattice of index1. The exact independent integer checker takes the gcd of every maximal minor and obtains1. Thus, under presentation completeness, Cl(A,S)=0, including its minus3-part.

For the3-part alone it is enough to use columns4 and9: a prime of ramification3/residue-degree1 above2243, and a degree-one prime above5843. Their first two coordinates form

    [2,6;4,2],      determinant=-20,

which is invertible modulo3. The third cyclic factor has order2. This is a check of generation in the supplied presentation, not a standalone unconditional theorem that the displayed generators exhaust the true class group.

An exact number-field inspection gives signatures

    A:(2,3),       A^+:(2,1).

Therefore ordinary minus unit rank is (2+3-1)-(2+1-1)=2. Scalar -1 permutes the11 primes above S by

    [1,2,3,5,4,6,7,8,10,9,11].

There are exactly two exchanged pairs, hence the primitive minus S-divisor rank is2. The finite class quotient has rank0, so Dirichlet's S-unit theorem gives

    rank_Z3 U_AS^-=2+2=4.                          (2)

The full residual image also excludes mu_3 from A: the determinant character remains surjective on the point stabilizer. Thus roots of unity contribute no3-torsion to this minus unit calculation.

## 3. The companion bound

Since vu=3 on U_AS^- and uv=3 on U_BS^-, the cokernel of u is killed by3. Both lattices have rank4. Smith reduction over Z3 therefore gives

    0<=s_AS<=4.                                   (3)

No fundamental unit basis, selected unit list, or actual kernel dimension is needed for (3).

The conditional source S-class vanishing gives c_AS=0. Substituting t_D=1 into (1),

    s_AS=2+c_BS.

Combine this with (3):

    0<=c_BS<=2.                                   (4)

This is a numerical upper bound on the actual companion S-class contribution conditional on the independently supplied source class presentation and retained index theorem. We did not compute a companion class group or obtain its exact value.

## 4. The whole source bound, including class support

The exact global virtual S-unit sequence is

    0 -> U_AS^-/3 -> A(S,3)^- -> Cl(A,S)^-[3] ->0.

When Cl(A,S)^-[3]=0, every virtual class has an S-unit representative, whether or not it was originally represented through an ordinary ideal-class direction. Consequently A(S,3)^- has dimension4 by (2). In particular the full incidence-norm kernel K_A satisfies

    dim_F3 K_A<=4.                                (5)

Equivalently the retained combined bound gives

    dim K_A<=1+t_D+c_BS-(c_AS-r_AS)<=2+2=4.

The equality of these two derivations checks the treatment of class-supported directions. They have not been assumed absent; choosing S that kills the source class group allows them to appear inside the enlarged S-unit source. Local admission can only shrink this upper space.

The retained source embedding would then give dim Sel_3(E/Q)<=4 and dim Sha(E/Q)[3]<=2, using the known rank2 and absence of rational3-torsion. These are conditional upper deductions, not a new unconditional certification, and they concern an already studied coefficient prime. They do not establish ORDER9 (which would require full primary exponents and exclusion elsewhere), FIN, or Q36.

## 5. What certification did and did not establish

Two independent computational strategies to obtain a new class upper certificate were attempted within sealed bounds:

1. Actual companion B BNF, both the original polynomial/flag1 and a reduced polynomial/flag0: each timed out after120seconds. Neither produced a BNF or class invariants.
2. Existing source A BNF with bnfcertify(B,1): timed out after90seconds. This mode would certify that the true class group is a quotient of the computed one and does not require fundamental units. It returned no certificate.

A successful source quotient certificate plus authenticated relations of the named S-prime ideals could remove the GRH qualification from source S-class vanishing. That did not occur here. The exact lattice calculations cannot replace class-group completeness. No repeat beyond those sealed caps was made, and a timeout is not a negative mathematical result.

The numeric bound(4) is the outcome of the alternate source method. It is not obtained by feeding the known four-dimensional seed Selmer space back into the companion calculation.
