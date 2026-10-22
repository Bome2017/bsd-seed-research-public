# Arithmetic push reviewed and extended

**CONFIRMED_AT_RETAINED_INPUT_GRADE.**
**PRODUCT_RELATIONS_CONSTRUCTED; NO_NEW_UNIFORM_BOUND.**

The prime-to-p descent, coverage, and bounded-tail theorem have no blocking error in this review. The source norm/Minkowski statements match their uses. All 60 submitted manifest entries and the 33-entry embedded handoff verify; all four supplied computational outputs reproduce exactly. No input file was changed.

## What survives

The degree-(p-1) norm detects every equivariant receiver map. The oriented stabilizer field is correctly specified. The bounded prime-ideal set covers the receiver in the claimed Hom-detection sense, and the large-prime relation has coefficient one with all other prime factors controlled. This applies to all good seed p>=5 on the retained forward-receiver inputs, without ordinarity or an assumption about localization of the rational points.

This is an actual arithmetic comparison and construction. It gives no new bound on excess Sha. Finite generation was already available in principle by applying Minkowski directly to L; the new content is the specific scalar descent and controlled-tail presentation.

## Work beyond the audit

I tested the immediate way to obtain relations on the OLD generators, rather than more independent new-column pivots. Reduce ideals a and d separately and also reduce their product:

    (alpha_a)=a c_a, (alpha_d)=d c_d, (alpha_ad)=ad c_ad,
    N(c_a), N(c_d), N(c_ad) <= b_J.

Then the actual field element gamma=alpha_ad/(alpha_a alpha_d) satisfies

    (gamma)=c_ad/(c_a c_d).

All three tail ideals use the old factor base. Thus every receiver functional satisfies

    lambda(c_ad)-lambda(c_a)-lambda(c_d)=0.

This supplies an explicit family of old-generator rows with a proved norm bound. Tiny exact examples show these rows can be nonzero. The formula and the conditional rank implication to the uniform target are in PRODUCT_RELATIONS.md.

I also tested conjugated norm correspondences N*g*j. Their receiver eigenvalue is (p-1)*rho(g)_11. Combining these identities does not itself bound multiplicity: V^r satisfies them for every r. That calculation is in MIXED_NORM_TEST.md.

## What still fails

Neither construction proves that the actual seed rows have enough independent standard-representation content. No independent estimate on their residual rank was obtained.

There is a concrete check against inferring the missing rank from the norm bounds alone: Q(sqrt(-37363)) has p-inverted class group (Z/5)^2. It obeys the same general ideal-reduction/product identities and five is inert. This was certified in a tiny exact control. It rules out that generic inference, not the seed route or a theorem exploiting its additional arithmetic.

The remaining implication is therefore precise:

    an arithmetic bound on the receiver image after the old-generator rows
      -> dimension at most one
      -> Sha[p]=0 by the reviewed injection and retained parity
      -> the uniform portion of FIN.

The first bound is still unproved. A new presentation or a formal verification of these identities would not provide it. No seed-scale field computation, fixed-prime campaign, or Aristotle run is justified merely by this return.

The result is a checked arithmetic partial lemma plus one further constructed relation family. There is no new seed primary result or cofinite conclusion. The finite exceptional primary obligations, exact order nine, and Q36 remain separate.

FIN, ORDER9 and Q36 are unchanged.
