# H41_ETA_EXTERNAL_CHECK_ADDENDUM_004

Custody of the external check on `H41_ETA_CHARACTER_TEST_ADDENDUM_003`, with Claude's audit and four
corrections against Claude.

    ADDENDUM.md            the corrections and the corrected conclusion
    01_external_check/     the archive (911bbae6…) and its unpacked scripts and outputs
    receipts/              CLAUDE_AUDIT.txt, and the normalization check at both levels
    MANIFEST.sha256  DIGESTS.md

**The substantive correction is against my work:** at `N = 254` my sample spanned only 61 of the 62
compact-homology directions, so my reported test did not cover full homology there, and my appeal to
gcd stability as evidence of spanning was unsound. Their repair — adjoining conjugates and cusp loops,
justified by the plus-eigenspace and cuspidality properties — gives an index-one generating set, and
the comparison then passes on complete Schreier generating sets (192 and 768 instances, 0
disagreements).

**Second correction:** `mslattice` is integral *cohomology*, so my "which of two lattices" residual was
mis-framed. `Hom(U₀,ℤ) = H¹(E₀,ℤ)^{τ=1}` — plus cohomology is the right dual object; verified here in
both directions, as is their factor-of-two counterexample.

Also recorded: the four-curve agreement is expected rather than independent corroboration, and my
"already implied by λ" remark understated the experiment. An evidence gap in `ADDENDUM_003` is closed.

**The H41 seed remains unproved.**
