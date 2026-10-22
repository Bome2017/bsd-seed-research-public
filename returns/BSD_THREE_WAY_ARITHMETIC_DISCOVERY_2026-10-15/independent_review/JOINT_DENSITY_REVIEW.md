# Independent desk review of the joint evaluation and local signatures

Reviewed by the Frobenius subagent on 2026-10-15. Grade: supported written deduction under the stated full-image, genuine membership, independence and saturated-point inputs. This is not a fresh certification of those inputs. Exact file hashes at review time are in JOINT_DENSITY_REVIEW_BINDINGS.json.

I read local_signatures/JOINT_EVALUATION_DENSITY.md and PROOF.md, the implementation of point annihilators, the exact count output, and the main REPORT.md. The root worker separately replayed the source residues; I did not duplicate that arithmetic replay in this review.

## Joint surjectivity is justified

For V=E[3], the central −I computation really kills H¹(GL₂(F₃),V): its difference from the identity is invertible in F₃. Restriction of actual independent global classes to the torsion field therefore remains independent. No assumption that 3 is prime to the group order appears.

The key module statement is legitimate: V^d is semisimple because it is a direct sum of the simple natural module, although F₃[GL₂(F₃)] is not a semisimple algebra. A proper submodule has a nonzero quotient mapping to V. End_G(V)=F₃ makes that map a nonzero scalar combination of the coordinates. Applied to the joint cocycle image it would contradict the restricted-class independence. Thus the image on the torsion-field kernel is all V^d.

The proof constructs the extension using the cocycle homomorphism into V^d semidirect G. Once its image contains all V^d and surjects onto G, it equals that semidirect product. It does not need H²=0 or a theorem splitting an unrelated group extension.

## The density statistic is the correct quotient rank

At a good q≠3 splitting in the torsion field, Selmer classes are unramified and the local Kummer group is the two-dimensional V-valued unramified cohomology. The eight cube characters are an injective realization by Weil pairing. Changing a global lift by a point changes the local vector by the point columns, exactly what the annihilator construction removes.

For a known r+s-dimensional global span, the detector rank is therefore rank([W|C])−rank(W). Simultaneous left GL₂ action preserves this statistic, making its level sets conjugacy invariant. Chebotarev conditional on splitting in the torsion field gives the uniform finite-matrix count. Neither individual source embeddings nor a preferred cube-root coordinate are asserted to be canonical.

I independently obtained the seed counts without using the enumeration output: the 2×2 point matrices have rank counts1,32,48. For point rank2, all81 excess matrices give quotient rank0. For point rank1,9 excess matrices have both columns in the point line and72 do not. For point rank0, the excess ranks have counts1,32,48. Therefore rank-difference counts are

    0: 48·81+32·9+1=4177,
    1: 32·72+32=2336,
    2: 48.

The other stated rows follow similarly: (1,32,48)/81 at r=0,s=2; (73,608,48)/729 at r=1,s=2; and certainty of rank0 when s=0. These are relative asymptotic densities on the specified known subspace, not probabilities for independent successive-prime trials.

## Admission and source scope remain essential

The proof correctly requires genuine global cohomology/Selmer membership before interpreting a nonzero quotient signature as a Sha class. The mirror example demonstrates why this is necessary: it has local signatures but a noncube affine norm. It cannot be inserted as a new independent global cocycle in the density theorem.

The full point image, not just an arbitrary independent pair, is needed. The proof explicitly retains rank and 3-saturation; with full residual image there is no rational3-torsion. The maps are well-defined on S/W without assuming Sha finite. Local torsor classes in H¹(Q_q,E) remain zero; the retained E[3]-Kummer information is not that torsor localization.

The seed signatures certify rank two only on the four named global classes. The theorem permits arbitrary extra global classes; it therefore does not turn this detection into an upper bound or prove source completeness. The known positive span at bad coefficient3 does not supply good-prime or cross-prime coverage.

## Main report check

The Frobenius section agrees with the separately checked fixed-norm construction, degree9-over-K/degree432-over-Q field, sealed forty predictions and post hoc degree24 polynomial replay. The three-way distinction is accurate when read with its genuine-admission and full-point-lattice conditions. FIN/ORDER9/Q36 are correctly unchanged.

One clerical repair is needed in REPORT.md: the density proof is named `local_signatures/JOINT_EVALUATION_DENSITY.md`, not `JOINT_KUMMER_DENSITY.md`. No mathematical repair was identified in the two reviewed deductions.
