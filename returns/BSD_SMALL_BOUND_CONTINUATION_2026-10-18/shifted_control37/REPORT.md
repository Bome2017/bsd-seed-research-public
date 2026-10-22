# The asymmetric shifted control: exact source and norm follow-up

For 37a1 at coefficient5, the search found h=2(y+x), an S-unit for S={2,5,37}. Its exact norm is -2^28/5^3. The chi-projected class has valuations (1,3,4,2) modulo5 at the four degree-one primes above2, so it does not belong to the original A({5,37},5) source or the ordinary virtual-unit space.

The conjugate shifted candidate gives its inverse in the chi space. No nonzero combination of those two projected classes removes that divisor vector. The actual affine norm is nontrivial, as separately checked at split primes1181,3391,5581. This nontriviality cannot improve the ordinary-unit norm rank because its source lies outside that space.

Read ../rank_mechanism/SOURCE_SEARCH_REVIEW.md for the exact derivation and scope. No BNF completeness, Sha value, L-value, or unit-basis completeness is used. The existing exact point field, scalar map and maximal order remain retained inputs; no new expensive number-field search was run.

A diagnostic sign error in the first norm assertion was corrected before any bound: the norm is negative. The raw shifted-search JSON already had the correct negative resultant. diagnostic_norm_sign.gp records the diagnostic print version; authenticate.gp is the corrected assertion version.
