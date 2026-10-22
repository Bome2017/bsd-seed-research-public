# Proof of the complete-unit bound and retained class term

Let E be the new control 11a1, p=7, A=Q(T) for a nonzero 7-torsion point, sigma(T)=3T, and chi(sigma)=3. S={7,11}. Work with the retained Schaefer-Stoll source injection from H1(Q,E[7]) to A*/A*7 and its scalar/affine-incidence description.

## Ambient dimension, independently of a unit generator list

The exact irreducible degree-48 point polynomial and primitive multiplicative transvection at 11 establish the full GL2(F7) image using the retained subgroup theorem; determinant is cyclotomic. The control has discriminant -11^5, so the transvection is nontrivial modulo7. The source field has signature (6,21), in particular a real embedding and no seventh roots of unity.

Equivariant Dirichlet identifies the free unit representation with the permutation representation on archimedean places, minus the trivial representation. On the faithful scalar component the constant representation contributes nothing. The functions on nonzeroV=F7^2 have scalar-character dimension 8, one per projective line. Complex conjugation has trace 0 on this component: its two fixed projective lines contribute chi(1)+chi(-1)=1-1, and the remaining lines are paired. Its invariant space has dimension 4. Scalar order 6 is prime to 7, so the integral character projection and reduction retain this dimension. Thus dimF7 U_chi=4 for U_chi=(O_A*/O_A*7)^chi.

The integral polynomial6+2sigma+3sigma^2+sigma^3+5sigma^4+4sigma^5 is the chi projector modulo7. Applying it to actual units gives actual units in this character component. No division of an arithmetic source by7 is used.

## Authentication and necessary constraints

For each of 26 compact products, exact finite-ideal factorization and reconstruction prove its divisor is zero over Z; hence it is a global unit. The checker retains all negative and large exponents. Exact source-binding checks ensure the evaluated products are precisely these authenticated units.

The split-prime residues of an incidence norm must be seventh powers for a genuine global cohomology source. Therefore the three displayed independent affine-line residue rows vanish on every such source. At coefficient 7, good ordinary nonanomalous reduction identifies the Kummer image with the formal-line cohomology. Weil evaluation at formal torsionT kills that image. Thus the value on the degree6 formal branch is a local seventh power for every Selmer source. See LOCAL_CONDITION_REVIEW.md and local_rank/ for the finite quotient matching and actual point valuations.

The displayed 4-by-4 minor is invertible modulo7. It proves that the stacked necessary constraint map has rank at least 4 on U_chi. Since U_chi has dimension 4, its kernel is zero. This is a whole-unit-space result even without fundamental-unit completeness: four independent images already exhaust the independently known ambient dimension. The same minor also proves those four projected unit classes form a mod7 basis.

This does not assert that the true incidence norm kernel has dimension exactly 1 from finite split residues alone. The norm residue screen leaves dimension 1; the local row removes that final screened line. The genuine simultaneous kernel is contained in that zero space.

## Ordinary classes and valuations

Let A(S,7) be the subgroup of A*/A*7 represented by elements whose valuations are divisible by7 at every finite prime outside S={7,11}; this is the virtual-unit source unramified outside S. Define K as the subspace of A(S,7)^chi satisfying the ACTUAL incidence-norm seventh-power condition and the stated coefficient-local Kummer condition. In particular, K is not defined merely by the finite split-prime residue screens used to bound its unit intersection. The primitive divisor calculation establishes val(K)=0, so K lies in H0=A(empty,7)^chi. Retain the exact sequence

    0 -> U_chi -> H0 -> Cl(A)[7]^chi -> 0.

Since K intersects U_chi trivially, projection gives an injection

    K -> Cl(A)[7]^chi.

More precisely the image is constrained by the actual norm and unit-repair obstruction. No bound on that image follows merely from the injection. The provisional class-one output, if its completeness were assumed, would make K=0. Its attempted unconditional certificate did not complete, so no unconditional whole-source-zero assertion is made.

All true Selmer sources lie in K under the stated descent and local inputs. This experiment's supported unconditional arithmetic conclusion (relative to those written inputs) is the unit kernel zero and the retained class-supported injection, not a new seed Selmer value or endpoint.
