# Rank-two 655a1 source evaluation

Status: **the admitted tangent family supplies zero rejecting rank**.

The new source consists of 24 ordinary units in the actual degree-48 point field at coefficient prime 7. The source lane authenticated the complete principal divisors of 14 rational tangent/vertical functions, transported these divisors through all six scalar conjugates, and formed the integer kernel of the resulting 142-by-84 divisor matrix. Its rank is 60. That procedure proves these 24 products are ordinary units; it does not prove they generate the ordinary-unit group.

I evaluated all 24 products independently of any known Sha value. At each of the three fully split primes 41413, 44843 and 63533, every raw seventh-power residue is zero at every one of the 48 embeddings. The raw rank, faithful-character rank and full affine-norm defect rank are all zero. The actual coefficient-7 formal-branch map also has raw and character rank zero, at both prime-ideal precisions 8 and 9. A nonpower calibration in the same quotient has nonzero image, and its seventh power has zero image.

The branch is rebound to this curve, not copied from 11a1: the model is [0,0,1,-13,18], its point count at 7 is 11, and the three branches have (e,f) equal to (6,1), (7,3), (7,3). The universal point on the degree-six branch has coordinate valuations (-2,-3), so it is the formal-torsion branch. Every compact product has exactly zero valuation there before its unit logarithm is used.

The bounded evaluator completed in 4.14 seconds. A separate integer-product replay reconstructs the local rows and their character projections from the saved factor logs and the full integer relation matrix. No fundamental-unit or class-group completeness assumption entered this rank calculation.

The source lane then evaluated the 24 products exactly in the number field: all are literally +1 or -1. This is stronger than the residue output and explains it. The finite residue checks alone did not establish that global conclusion. See the sibling tangent_source/exact_products.gp and exact_unit_products.gp, bound by SHA-256 in SOURCE_BINDINGS.json.

Thus this family leaves the available ordinary-unit kernel upper bound at 4. It supplies neither of the two rejecting directions that would lower that upper bound to 2. This failure is specific to these 14 functions and their scalar conjugates. It is not a theorem that no useful rank-two unit family exists.

The preparation also records a precise distinction about the known points. Their Kummer plane lies in the complete virtual-unit source after the retained support conditions. Its image in the ordinary class-group term is not known to vanish merely from the existence of rational points. Therefore one must not force the ordinary-unit kernel to have dimension at least 2, nor conclude a whole-source bound from an ordinary-unit bound alone. The complete-source target remains at most 2, or at most 3 with the separate retained parity input.

No seed prime, FIN, ORDER9 or Q36 is changed. The reusable evaluator is now applied only to a genuinely changed source, with a new model/field binding and admission proof. It is not rerun on this tangent family.
