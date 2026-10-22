# Uniform ambient division does not give Selmer division

**Candidate tested:** use a published uniform divisibility theorem to force the higher pairing radicals to exhaust the receiver, then combine with an independent termination bound.

**Disposition: NO_BOUND_MECHANISM from this theorem and the supplied inputs.** Neither the required preservation of the Selmer condition nor the termination bound has been supplied.

Çiperiani–Stix, *Weil–Châtelet divisible elements in Tate–Shafarevich groups II: On a question of Cassels*, Theorem B(2) and Corollary 30, imply ambient p-divisibility when E[p] is irreducible, p is odd, and [Q(ζ_p):Q] is not two. The retained seed image meets these conditions for p≥5. Their conclusion permits division in H¹(Q,E), not necessarily in Sha. Their Theorem D instead concerns classes locally zero in finite-coefficient H¹, a different local condition from the Selmer Kummer condition. [Primary source](https://arxiv.org/pdf/1308.4528).

Here is the missing step explicitly. For x in Sha[p], ambient division supplies y in H¹(Q,E)[p²] with py=x. Its local images satisfy p loc_v(y)=0. They need not be zero. Replacing y by y+z, with z in H¹(Q,E)[p], makes y locally trivial only if

    loc_v(z) = -loc_v(y) for all v.

Existence of this correction is equivalent to x belonging to p Sha[p²]. In the reviewed pairing notation, that is precisely x in rad(b_0). The ambient theorem gives no such correction. The receiver's local exactness describes the p-level restriction kernel; it does not assert this global correction exists at the next level.

Even if every x admitted all such corrections, the intersection of the higher radicals would be D[p], the p-torsion of the maximal divisible subgroup. An additional independent argument would still have to control that subgroup. Proving only ambient divisibility therefore cannot supply the announced dimension bound.

The comparison has a clear failure before any large computation: the theorem's ambient group is different from the group whose lifting filtration matters. No claim is made that every possible use of the source is exhausted. No prior-art novelty conclusion follows from not locating this exact citation in the two project documents searched.
