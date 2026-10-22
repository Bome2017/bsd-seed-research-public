# Exact scope of the new norm-one source exclusion

Date: 2026-10-21. Written proof under the retained actual degree-24 seed point-field identification and scalar action. The experiment does not certify the class group or prove FIN.

## 1. Actual algebra and candidate families

Use the monic even polynomial F(w)=G(w²) in inputs/seed_polynomial.json, read from the seed coefficient-five field construction at lab commit 77d4b331885138eb1f3f93d8063b06d6d7eb730b. The retained identification is A=Q(w), with scalar automorphism σ of order four, σ²=τ, and τ(w)=−w. This is the fixed seed's point field, not a control curve. Its maximal-order construction and correspondence with E[5] were not rerun.

The first family is

    u_(a,b)=(bw+a)/(bw−a),
    1≤a≤2048, 1≤b≤16, gcd(a,b)=1.

It contains 20,180 elements. The second is

    v_(a,b,c)=(a+bw²+cw)/(a+bw²−cw),

where a ranges over 1,2,...,512 as powers of two, b over ±1,±2,±4,±8, and c over 1,4,16,64,256. Dividing triples by their integer gcd and deduplicating gives 272 candidates. Every denominator is nonzero; every candidate has relative norm one under τ. This does not imply integrality.

Exact trace formulae, with n=24 and z=w², are

    Tr_A/Q u_(a,b) = 24−2(a/b) F'(a/b)/F(a/b),
    Tr_A/Q v_(a,b,c) = 24+4c² Tr_Q[z]/G (z/((a+bz)²−c²z)).

All 20,452 traces are nonintegral. Thus none of these individual elements is an ordinary unit. Seventeen independently implemented 24-by-24 companion-matrix computations reproduce the sampled traces and relative norm-one identities. The quadratic field Q(sqrt(2)) gives a positive unit control with characteristic polynomial t²−6t+1; Q(sqrt(6)) gives the negative control trace 14/5. Trace integrality alone would not certify a unit, but nonintegrality rigorously rejects one.

## 2. Why checking products was necessary

Several nonintegral elements can multiply to a unit, so the preceding screen does not exclude their multiplicative closure. The adaptive test therefore examines all scalar translates and all integer products, rather than stopping at single elements.

For each quadratic candidate put α=a+bw²−cw. Exactly twelve α-polynomials factor over Q into two rational linear factors. Their roots occur, up to sign, in the first family's rational list, and exact polynomial multiplication verifies the corresponding identity v=u_(r1)u_(r2). Remove these redundant generators, retaining 20,180 linear and 260 quadratic generators α_i. For the linear case use α_i=bw−a; its Cayley element is −τ(α_i)/α_i. For the quadratic case it is τ(α_i)/α_i. The signs have no divisor contribution and the scalar-square inversion relation is exact.

The exact absolute norms are

    N_i=|b^24 F(a/b)|                       (linear),
    N_i=|Res_z(G(z),(a+bz)²−c²z)|           (quadratic).

For each N_i remove every factor supported at rational primes ≤65536 or dividing Disc(F). This gives M_i. An exact product/remainder tree computes gcd(M_i,product_(j≠i) M_j); repeated gcd division removes all primes shared with another M_j. The residual integer P_i satisfies

    P_i>1, P_i divides M_i,
    gcd(P_i,product_(j≠i) M_j)=1.

This holds for every one of the 20,440 nonredundant generators. All excluded-small-prime and polynomial-discriminant conditions are also exact. No factorization of P_i into primes is claimed or needed: every prime divisor of P_i has the required properties.

A separate C/GMP verifier forms the full product and checks every certificate by direct modular reduction, rather than the producer's product/remainder tree. It passes all 20,440 rows. A forged common factor in a two-row negative control is rejected.

## 3. The full scalar-closed family has no nontrivial ordinary units

For each i choose a prime q dividing P_i. It divides N_i and no N_j for j≠i, and q>65536 with q not dividing Disc(F). Localizing at q makes Z[w] the maximal unramified algebra: a prime of A at which α_i vanishes is visible in this étale algebra.

At such a prime, τ(α_i) cannot also vanish. For a linear α_i this would give 2a=0 modulo q. For a quadratic α_i it would give 2cw=0. All parameters are smaller than q. Also w is a unit at q: if q divided F(0), the even polynomial F would have a repeated root at zero modulo q, contradicting q not dividing Disc(F). Thus the divisor of the norm-one candidate has a nonzero q-supported anti-invariant part D_i, with σ²D_i=−D_i.

The vectors D_i and σD_i are Q-linearly independent: a rational relation σD_i=tD_i would imply t²=−1. No other generator or its scalar translates has any divisor at q, because its absolute norm is prime to q. These private rational prime supports separate the pairs for different i.

Hence the two scalar representatives per generator have rational divisor rank exactly

    2*20440 = 40880.

The other translates are their inverses, since σ²u=u^−1. Any integer product with zero divisor has zero exponent in each independent pair, and is exactly 1. The twelve omitted quadratic generators are already exact products of the first family. Consequently the whole tested scalar-closed multiplicative family Γ satisfies

    Γ ∩ O_A^* = {1}.

No non-torsion unit is hidden in integral saturation: if an ordinary unit x has x^m in Γ, then x^m=1. The retained real embedding of A makes its roots of unity ±1, both trivial modulo fifth powers.

This is a finite-family exclusion, not a statement that A has no faithful units. It does not compute the whole unit group, a regulator, or a class group. The number 40,880 is a rational divisor rank of this large finitely generated multiplicative family, NOT a class-group rank, Selmer dimension, or mod-five character rank.

## 4. A stronger mod-five statement for the rational subfamily only

For all 20,180 rational generators, the private residual P_i is not a perfect fifth power. Thus some private prime q occurs in N_i to exponent not divisible by five. A linear element bw−a vanishes at exactly one prime of A over q; that prime has residue degree one, because q does not divide Disc(F). Its norm exponent therefore equals its normalized ideal valuation.

The scalar orbit of this degree-one prime has four distinct primes. One way to see this is to use the Galois extension A/A^{<σ>}: at an unramified prime of absolute residue degree one, its decomposition group is trivial. On these four primes the divisors of u_i and σu_i have two independent nonzero anti-invariant vectors modulo five. The same private-support separation across i proves that the divisor map on Γ_linear/Γ_linear^5 is injective.

Therefore a product from this rational subfamily which is an ordinary virtual unit modulo fifth powers is already a fifth power within the family. It supplies no nonzero ordinary virtual-unit class. This mod-five conclusion is NOT extended to the 260 irreducible quadratic generators: their prime-supported valuation patterns need more characterwise information. A non-fifth-power rational norm alone does not prove both projected character ranks for a quadratic factor.

## 5. Endpoint boundary

No ordinary unit rejection rank r_U or compatible class-lift upper bound k_C has been increased or reduced by these exclusions. The original complete relative class-length bound 97 and source ceiling 100 remain unchanged. FIN, ORDER9 and Q36 remain open; no seed prime has been newly settled.
