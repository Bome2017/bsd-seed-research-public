# Rank-two twist class and divisor audit

Date: 2026-10-18
Status: DIVISOR_ARGUMENT_PASSES; SHARED_X_FIELD_GIVES_NO_CLASS_TRANSFER_BOUND.

The actual prime-permutation data imply t_D,chi=0 at all of7,11,47. Independent matrix calculations verify the claim for both faithful characters. This controls the complete valuation layer, not only the found elements. The remaining class term is the ordinary Cl(A1)[7]^chi.

The quadratic twist has exactly the same degree-24 x-field, but this does not transfer an old class bound. In the degree-96 biquadratic compositum, original faithful classes lie in the (+1)-eigenspace for the quadratic twist involution and twisted faithful classes lie in its (-1)-eigenspace. Cross-norm to the old field annihilates the latter. The exact component identities and their proof are in PROOF.md. No class-group computation or known Selmer answer was used.

The root PROOF.md whole-source formula is mathematically correct under its stated source and local-map hypotheses:

    dim ker L = (4-r_U)+(c-r_C)

once the valuation allowance is zero. Here r_C must be the rank of the class-lift obstruction modulo the SAME unit image L(U), on a complete ordinary class source. Partial found units can lower-bound r_U, but their failure cannot upper-bound the kernel; neither a provisional class group nor a supplied class span determines c. The root proof states these qualifications and preserves the distinction that rational-point directions may be class-supported.

This audit adds no unit rank, no complete class bound, and no seed or cofinite conclusion. It validates the new valuation reduction and prevents the shared x-field from being mistaken for transfer of the missing class control.

Checks: exact twist cubic identity; full finite-field matrix kernels on three supplied prime-permutation spaces; independent extraction of old discriminant -7^47*11^36. Source NF/field arithmetic remains retained rather than recertified. No BNF, paid run, or publication was performed.
