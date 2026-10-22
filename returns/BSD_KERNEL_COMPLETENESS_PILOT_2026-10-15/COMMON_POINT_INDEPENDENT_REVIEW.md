# Independent common-point repair calculation

The independent checker imports only standard-library Python, the saved seed source-coordinate matrices, and the saved source-residue rows. It imports neither pilot.py nor the previous finite-field helper. For each of the four known classes it tries all nine rational-point coefficient pairs. At each selected place there is exactly one repair, so the displayed two-by-four matrices are unambiguous in the retained (P1,P2) coordinates:

    A_1213 = [[1,0,2,1], [0,1,0,0]],
    A_1543 = [[1,0,2,1], [0,1,1,2]],
    A_1699 = [[1,0,1,1], [0,1,2,0]].

The first two columns are the identity at every place. Thus the point coordinate convention is shared, with no hidden point-basis change. Every equation E_q(W) A_q = E_q(C) is checked entry by entry.

The pair difference has the single nonzero row (0,0,2,1). Hence the residual non-point direction is beta1+beta2. Enumeration of all 81 known-class combinations confirms that all 81 separately admit point repairs at both places, while only 27 admit one common repair. Their images in the known quotient consist of 0, beta1+beta2 and twice that class.

Adding1699 contributes the row (0,0,1,0), so the difference rank becomes two. Exactly nine class combinations admit a common point repair at all three places: the rational point plane itself. The checker explicitly tries every possible common point coefficient pair rather than inferring this only from matrix rank.

This illustrates the distinction between quotienting by a separate copy of the point plane at each place and quotienting once after stacking the evaluations. The latter asks that one global point explain all the local Kummer lifts. It retains compatibility information that the separate quotients discard. On the four supplied known classes, it removes the two-place residual kernel at the third place. It makes no claim about classes outside that span or completeness of the seed's source.

Replacing an extra class by itself plus a fixed rational point adds the same coefficient column to every A_q, so all differences are unchanged. Changing the point basis by an invertible two-by-two matrix left-multiplies all differences by its inverse and preserves the kernel. The supplied full saturated point basis is a retained arithmetic input, not derived from these three local evaluations.

The first draft checker incorrectly asserted that the initial pair would already have rank two; that desired outcome was stronger than the sealed hypothesis and the assertion correctly failed. The rejected script and explanation are retained in independent_failed_pair_assertion/. The accepted checker reports the actual pair and triple kernels and passes all exhaustive checks. No new local evaluations were generated, and no old source was modified.
