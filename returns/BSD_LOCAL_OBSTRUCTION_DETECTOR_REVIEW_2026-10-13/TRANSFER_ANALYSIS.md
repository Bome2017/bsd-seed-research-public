# Transfer to full residual image: a faithful family, not an upper bound

2026-10-13. Written deduction under the retained seed rank/basis and full residual-image inputs. No Sha-finiteness input, new covering, or coefficient computation is used.

## Answer to the admission question

Yes: for p>=5 with residual image GL2(Fp), the collection of good-place maps in the submitted §8 detects every nonzero Sha[p] class. It suffices to use good primes q at which E(Q_q)/p has dimension1 and both rational basis points are locally p-divisible. Such places exist for every nonzero class to be detected.

This is not a new bound mechanism. The archive already contains the same joint-cocycle/Chebotarev mechanism in other coordinates. Its immediate useful role here is to specify how to test **an actually constructed covering class** in the full-image setting, without copying the control's quadratic-field isogeny descent.

## Precise detector

Let V=E[p], S=Sel_p(E/Q), and W=E(Q)/p, with a saturated rank-two basis. At good q!=p, identify the finite local condition with E(F_q)/p. Localization and quotienting by loc_q(W) give a canonical map

D_q : S/W -> (E(F_q)/p)/loc_q(W).

Here S/W=Sha(E/Q)[p], without assuming that the primary or full Sha group is finite. This is localization of a Selmer lift modulo global-point localization; it is not localization of a Sha torsor in H1(Q_q,E), which is zero.

Define P_p to consist of good q!=p such that

q != 1 mod p,
p divides n_q=#E(F_q),
[n_q/p]P1=[n_q/p]P2=O in E(F_q).

The first two conditions make residual Frobenius semisimple with distinct eigenvalues1 and q mod p. Its fixed space has dimension1, so the p-primary reduction group is cyclic. For a finite group with cyclic p-primary part, P belongs to pG if and only if [#G/p]P=0. Thus the final two tests are exactly loc_q(W)=0. For q in P_p the target of D_q is a one-dimensional Fp-space.

## Joint injectivity proof

Put K=Q(V), G=Gal(K/Q)=GL2(Fp). The central scalar -I acts by -1 on V. Sah's cocycle identity gives H1(G,V)=0, so restriction H1(Q,V)->H1(K,V) is injective. Over K a restricted cocycle is an actual homomorphism to V.

Take any independent classes c1,...,cd in H1(Q,V). Their joint restriction has G-stable image J in V^d. The particular module V^d is a direct sum of simple modules, even though p divides |G|. If J were proper, its semisimple quotient would admit a nonzero map to V. Since End_G(V)=Fp, this would produce a nonzero linear combination of the ci restricting to zero, contradiction. Hence J=V^d.

The combined affine cocycle representation therefore has full image V^d semidirect G: it projects onto G, and every fiber has the entire translation group V^d. No group-cohomological H2 splitting theorem is needed here, because the cocycle representation already maps into the explicit semidirect product.

Now choose c in S outside W and apply this to the independent classes kappa(P1),kappa(P2),c. Fix g=diag(1,a) with a in Fp* and a!=1. Choose translation vectors v1,v2 in (g-1)V and v3 outside (g-1)V. A Frobenius element with these data has trivial local images of both points and nontrivial local image of c in V/(g-1)V.

Chebotarev supplies infinitely many good rational primes with Frobenius conjugate to this element. The zero/nonzero conditions modulo (g-1)V are invariant under affine conjugation: changing a cocycle representative adds an element of (g-1)V, and G-conjugation transports the quotient isomorphically. These primes belong to P_p and have D_q([c])!=0.

Consequently

intersection over q in P_p of ker(D_q)=0.

Since Sha[p] is finite-dimensional, some finite subcollection is injective. This assertion does not give that subcollection effectively, certify its completeness, or bound its size independently of the unknown Selmer dimension. The same argument realizes any desired tuple of scalar evaluations against an independent list of Sha classes, after choosing identifications of the local one-dimensional spaces.

## Exact density and practical choice of primes

The matrices in GL2(Fp) with eigenvalues1,a!=1 comprise p-2 conjugacy classes, each with centralizer of size(p-1)^2. Their proportion is (p-2)/(p-1)^2. For each such matrix, vanishing of each of the two independent point evaluations is one independent linear condition, so the density of P_p is

(p-2)/(p^2(p-1)^2).

For a fixed nonzero Sha class, a further independent evaluation is nonzero with conditional proportion1-1/p. Its detecting primes therefore have density

(p-2)/(p^3(p-1)).

At p=17 these are15/73984 and15/78608. These are asymptotic Chebotarev densities, not a runtime guarantee or a certified finite search bound.

Demanding complete splitting in Q(E[p],p^-1P1,p^-1P2) would also work, but has density1/(p^4 |GL2(Fp)|), needlessly much smaller. The semisimple probe test above only requires point counts and finite-group scalar multiplication, avoiding construction of that enormous field.

Primary source for the density theorem: J.S. Milne, Algebraic Number Theory, Theorem8.31, printed p147/current PDF page148, https://www.jmilne.org/math/CourseNotes/ANT.pdf . The joint-cocycle proof and counting above are deductions, not quotations from Milne.

## Collision with prior work

I read these actual retained files in the local lab:

1. work/returns/BSD_SEED_ARISTOTLE_2026-10-05/working_set/BSD_LOCAL_EXACTNESS_PUSH_REVIEW_CODEX_2026-10-04/input/BSD_SECOND_TORSION_LOCAL_EXACTNESS_PUSH_2026-10-03/PENCIL_TAILS.md. Its joint prime-and-tail realization already obtains every tuple against independent receiver directions. Its tails balance the selected-prime values; complete detection was explicitly not a relation-rank bound.
2. work/returns/BSD_SEED_ARISTOTLE_2026-10-05/sources/governing/RECEIVER_ADDITIVE.md. Completely split primes already detect arbitrary actual receiver classes. The good-prime residue-degree-p cancellation is a distinct statement and must not be applied to the present semisimple probes.
3. work/returns/BSD_SEED_ARISTOTLE_2026-10-05/working_set/BSD_MECHANISM_B_RETURN_REVIEW_CODEX_2026-09-30/CYCLIC_DETECTION_REPAIR.md. This proves joint affine-cocycle surjectivity and simultaneous detection using nonidentity unipotent primes. The semisimple adaptation here selects simpler local probe conditions; it does not supply a new upper bound.

The construction remains possible for every finite excess dimension. It therefore cannot force that dimension to be zero just from the existence of many detecting primes.

## An admissible next experiment, and the unacceptable substitute

A useful inexpensive preparation is to compute several q in P_p for one unresolved seed coefficient prime, retaining exact n_q and point-multiplication receipts. This constructs local test sites, not Sha classes and not a Sha bound.

The discriminating experiment must then supply an independently constructed full-p covering/cocycle candidate and compute its local Kummer signature at those sites. A nonzero signature proves it is outside the rational-point image **only after its global Selmer membership is established**. Zero signatures at finitely many sites do not prove it trivial.

For controls with an explicit complete Selmer presentation, one can compute the matrix of these signatures, compare its kernel to the actual rational-point image, and test whether a proposed arithmetic operation changes a torsor class or merely its presentation. That is a finite exact test of a proposed construction. Merely enumerating more primes, or treating zero targets/signatures as an upper bound without a completeness theorem, repeats the old detection-only lane.

No independent arithmetic upper bound is obtained here. FIN, ORDER9, Q36 and seed prime coverage remain unchanged.
