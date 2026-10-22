# Attempt (iii): an independent upper bound on the Selmer dimension

## Retained structure and the endpoint

**DERIVED from v2 B.20–B.21.** At every good p>=5, d_p is a finite even integer at least two. The requested upper bound d_p<=3 is therefore exactly d_p=2. It eliminates both a finite excess primary part and a hypothetical divisible primary part, by split dual Kummer and Nakayama. It is not merely a bound on the Z_p-corank.

## Candidate III-A: transfer the certified 3-primary result through a common integral presentation

**DERIVED — sufficient finite-presentation criterion.** Let S be a fixed finite set of rational primes. Suppose one constructs a finitely generated module M over R=Z[1/S] and proves comparison isomorphisms

    M tensor_R Z_p ~= X_p=Sel_(p^infinity)(E/Q)^dual

for every p outside S. Suppose also that rank_R(M)=2. Then the target holds outside an explicit finite enlargement of S, once a presentation of M is known.

**DERIVED — proof.** The structure theorem over the PID R gives

    M ~= R^2 direct_sum T,

with T a finitely generated torsion R-module. Choose a nonzero Delta in R annihilating T, obtainable from an appropriate presentation minor. For p outside S and the numerator support of Delta, the comparison gives X_p~=Z_p^2. Dual Kummer surjects X_p onto Z_p^2 with kernel Sha[p^infinity]^dual. A surjection between free rank-two Z_p-modules is an isomorphism, so the kernel is zero. Equivalently d_p=2 and B.21 applies. If 3 is not in S and the common comparison also holds at p=3, then the certified X_3~=Z_3^2 direct_sum (Z/3)^2 determines rank_R(M)=2; it does not by itself construct M or the comparisons.

**DERIVED — actual missing step.** No such common module M or integral comparison maps were constructed. The Mordell–Weil lattice is a subobject, not the full Selmer dual. Common Frobenius polynomials of the Tate-module representations do not provide a common finite integral presentation of their global Selmer groups. Replacing the missing module by a product of the X_p gives a completed object and loses the finite-presentation input required in the proof.

**DERIVED — first failing test.** The conditional finite-presentation implication passes K-S: its conclusion excludes excess generators outside the finite determinant support. The proposed complete construction first fails K-P: there is no common finite presentation with proved comparisons outside one fixed finite set. This is a certificate format, not a new arithmetic reduction or a claim that a Sha-equivalent theorem is forbidden. An independent construction of M would be admissible.

## Candidate III-B: infer the bound from pairing, parity, and the settled primes

**DERIVED — paired-state test at an unsettled prime.** The modules

    X_0=Z_p^2,
    X_1=Z_p^2 direct_sum (Z/p)^2

have the same rank-two free quotient, the same Mordell–Weil rank, and even minimal generator numbers. The finite torsion of X_1 admits a nondegenerate alternating pairing: on its F_p^2 reduction use ((x_1,x_2),(y_1,y_2)) |-> (x_1 y_2-x_2 y_1)/p mod Z_p. Thus neither alternating duality nor parity excludes the second module.

For any chosen set U of unsettled good primes, assign X_1 at p in U and X_0 at the others; leave every retained settled-prime input unchanged. The corresponding higher Fitting patterns at each prime can satisfy eventual unit index and B.21. This is a family of abstract module models only. It is not asserted to arise from an elliptic curve, or from the actual modular symbols of this seed. Its role is to demonstrate that these selected structural inputs alone contain no cross-prime exclusion of U.

**DERIVED — first failing test.** K-S. The candidate endpoint uses relations that hold in both states. To use the finite 3-primary result for other primes one needs a new global comparison, such as the unconstructed one in III-A, not multiplication of the known order 9 into an unrelated scalar.

## Candidate III-C: import a nonzero rank-zero auxiliary twist

**DERIVED — idempotent obstruction to an automatic transfer.** Let H=C_2 and p be odd. In Z_p[H], put e_+=(1+h)/2 and e_-=(1-h)/2. A module Y decomposes as e_+Y direct_sum e_-Y. Prescribing strong control or vanishing on e_-Y puts no bound on e_+Y: both e_+Y=X_0 and e_+Y=X_1 from III-B are compatible with e_-Y=0. Consequently, even a separately proved rank-zero twist theorem does not control the seed's different isotypical component merely by placing them in one abelian extension.

**DERIVED — proposed new arrow and stopping point.** A genuine correspondence mixing the relevant Selmer conditions, with integral comparison and a uniform bound, could change this conclusion. No such correspondence was obtained. No nonzero twist theorem is being asserted here for a newly chosen curve; the obstruction tests the proposed automatic passage even after granting the favorable twist input.

**DERIVED — first failing test.** K-S. This is a scoped statement about projection to independent idempotents, not a theorem excluding every auxiliary-cycle or twist strategy.

## Coverage statement

**DERIVED.** No independent upper bound d_p<=3 was proved at an unsettled prime, nor on an infinite subset of unsettled primes. Attempt (i)'s comparison theorem covers all good p>=5, but cannot be counted as an infinite subset of primary vanishing. No exceptional set certifying the v2 endpoint has been constructed.
