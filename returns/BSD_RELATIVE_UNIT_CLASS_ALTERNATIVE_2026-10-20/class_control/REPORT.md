# Actual-seed relative class-control result

Date: 2026-10-20. Status: **NO_NEW_COMPLETE_CLASS_BOUND**.

The proposed cheaper class calculation was tested on the actual seed's
scalar tower, not on another control curve. Its degree-six and degree-twelve
fields are explicitly constructed in `../relative_source/fields.gp`.

For the degree-24 point field A, the scalar sigma(T)=2T has order four.
Let F2 be its square-fixed degree-twelve field. Ordinary ideal extension
and norm give the unconditional decomposition

    Cl(A){5} = j Cl(F2){5} direct_sum R5,
    R5 = ker N_{A/F2} = (Cl(A){5})^{sigma^2=-1}.

The desired faithful scalar component is inside R5. Both proper scalar
subfield norms annihilate it. Moreover the ordinary field-norm unit
indices have exponent dividing two or four, hence no five-primary
part. Thus those lower-field class and unit-index computations cannot
supply an upper bound on the missing faithful five-class contribution.
This is a scoped exclusion of direct lower-field transfer, not of
relative class algorithms or the sibling relative norm-one unit search.

The countercontrol realizes arbitrary five-rank and length in a faithful
C4 module while all these proper-subfield invariants and norms remain
zero. Its 80 exact finite cases passed; these are algebra controls, not
realized seed class groups. The written arbitrary-rank calculation is
in `PROOF.md`.

The complete source bound still retains the class term:

    dim K <= 3 - r_U + dim R5[5]^chi,

or its refinement by the actual incidence class map and connecting
obstruction. New actual relative units can improve r_U. An upper bound
on the surviving relative class term still requires an authenticated
relative ideal-class presentation or another independent arithmetic
bound. Neither lower-field class numbers nor a collection of relations
without a generation certificate supplies that upper bound.

The sibling's bounded degree-six BNF attempt is rejected by its own
receipt: stack overflow at 256,000,000 bytes after 26.23 seconds, empty
stdout, and `accepted: false`, notwithstanding GP's zero exit status.
No class number or unit system is inferred from that attempt. Its
failure is computational, not a proof that relative algorithms fail.
This lane ran no additional BNF computation.

The proof is an elementary written deduction requiring review; no proof
assistant was used. It establishes no new seed prime, no complete seed
source bound, and no FIN, ORDER9, or Q36 result.
