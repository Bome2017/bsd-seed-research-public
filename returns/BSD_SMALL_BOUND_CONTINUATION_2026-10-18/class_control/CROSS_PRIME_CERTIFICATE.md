# The class contribution in a small-source certificate

This specifies a computational upper certificate and records exactly which part was tested. It does not claim that its input can presently be produced uniformly in p.

Let A,B be the point and companion fields and chi the faithful scalar character. Put

    r = dim Cl(A,S)[p]^chi,
    s = dim ker(u on U_AS/p)^chi,
    k = dim ker(u_C on Cl(A,S)[p]^chi).

For actual source/target class maps and the Kummer connecting map partial,

    dim K_chi = s+k-rank(partial).

Local admission is a further linear map L from K_chi to local quotients. If an independent bound dim K_chi<=D is established and ell independent images are exhibited, then dim ker L<=D-ell. A complete basis of K_chi is not necessary for that inequality: a certified dimension upper bound plus a witnessed image-rank lower bound suffices. When an actual complete presentation is available, the full matrix gives equality dim ker L=dim K_chi-rank L. Selected source elements alone supply only a rank lower bound; the independent whole-space upper bound is what makes the calculation cover undiscovered directions.

For a rank-two seed, admitted upper bound2 suffices directly to give Sha[p]=0. Upper bound3 suffices only with the separately retained evenness theorem on its stated domain. Thus, for example, s<=2 plus k<=1 is already sufficient on that parity domain: one need not prove every relevant ideal class absent. No parity premise is imported for an arbitrary prime outside that domain.

## A class-map upper certificate that does not require a companion BNF

Suppose an independently certified basis a_1,...,a_r of Cl(A,S)[p]^chi is given. Choose actual ideals representing it. Let psi_1,...,psi_t be independently authenticated homomorphisms from Cl(B,S) to F_p. One way to supply them is via explicit cyclic degree-p extensions of B, unramified at finite primes and split at S, with their Artin symbols; this is arithmetic class-field input, not an arbitrary residue function.

Compute the matrix

    M_ij = psi_i(u_C(a_j)).

Then

    k <= r-rank(M).                                     (A)

Indeed ker u_C lies in ker M. The target class group need not be enumerated or its order certified. Only each psi must genuinely factor through the ordinary/S-class group, and the source p-torsion presentation must be complete. A finitely sampled residue functional on elements is not automatically such a class character.

This certificate bounds the entire class kernel when complete source information is supplied. Without that completeness it merely detects images of named classes, which is the earlier limitation the user asked to avoid.

Degree-p target characters can miss an order-p image buried in p Cl(B,S): the injection Z/p -> Z/p² taking1 to p is invisible to every homomorphism Z/p² -> F_p. This is a precision issue, not evidence that u_C has a kernel. A valid stronger version uses characters psi_i into Z/p^{e_i}; on a source p-torsion class their outputs are multiples of p^{e_i-1}, and these canonical p-torsion coordinates give the same F_p matrix test(A). Such characters can be authenticated through cyclic degree-p^{e_i} unramified extensions. The source's p-torsion and the target character precision must both be retained.

If the supplied source is an upper presentation of the whole finite class group, care is needed: surjectivity G->Cl(A,S) does NOT imply surjectivity G[p]->Cl(A,S)[p] (Z/p²->Z/p is a counterexample). A valid implementation must provide a cover of the actual p-torsion, or track the relations and higher exponents explicitly. This safeguard prevents an apparently complete matrix from missing hidden p-torsion lifts.

## What the seed p3 experiment says about (A)

The fresh actual class-image and norm-cube calculation proves u_C=0 on the whole source p3 class group under the same class completeness hypothesis. Therefore every legitimate target class-character matrix M is zero here. No choice of more target characters can reduce k=2 on this control. The failure is now an exact map statement, not failure to find a detector.

The S-version has source S-class group zero, but its two former class directions reappear inside the enlarged S-unit lattice; the total bound remains4. Changing S does not erase arithmetic directions.

## A smaller S and its precise use

Freshly checked Schaefer--Stoll, Proposition4.6, Corollary7.1 and Corollary7.9: Sel_p may be represented by classes unramified away from p and primes where a Tamagawa number is divisible byp, and then local conditions need only be imposed at this S. The source's retained total Tamagawa product is16. Thus every odd coefficient prime permits S={p} in this theorem, with the actual incidence/scalar conditions still imposed.

For the seed at3, the saved primes over3 have no minus divisor contribution and their class coordinates have no3-primary component. Passing to S={3} therefore leaves ordinary minus unit rank2 and class rank2; their total dimension4 is unchanged. This refinement avoids counting irrelevant S-prime generators but supplies no new arithmetic upper bound.

For larger p, an actual local decomposition calculation may similarly show that the faithful character has no p-divisor contribution. Such a result permits ordinary class computations instead of a larger S-class computation. It does not make the ordinary class kernel zero.

## A proposed lower-degree shortcut that cannot implement (A)

For any nontrivial scalar subgroup H of F_p^*, the norm from B to B^H annihilates the faithful chi^-1 component. On its Z_p class module it is the operator sum_{h in H}chi(h)^(-1)=0. Thus the natural scalar-fixed, lower-degree field norms cannot serve as the characters in (A) on the target component. This scoped statement does not rule out other explicitly constructed class-field characters or other correspondences.

## Outcome

This return executes the class-map experiment at the seed's coefficient3, obtains exact companion minus class groups, and verifies that the two class directions genuinely survive. It does not construct a nonzero matrix M at larger p or certify a complete source class presentation there. A cross-prime theorem would have to supply such arithmetic control or another independent bound; no current conditional class computation is promoted to that theorem.

Primary source freshly opened:
https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf
Proposition4.6 (printedp7), Corollary7.1 (printedp13), Corollary7.9 and Proposition7.10 (printedpp18-19). All statements here are paraphrased; incidence-index and seed arithmetic hypotheses are separately retained.
