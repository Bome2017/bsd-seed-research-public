# Targeted review of the completed comparison attempt

Read REPORT.md, CLOSED_CYCLE_AUDIT.md, SOURCED_TARGET.md, then MIXED_COMPARISON_ATTEMPT.md. This is a completed attempt, not a launch instruction.

The highest-priority mathematical checks are:

1. Verify the integral operator coefficients 2-p^2, 2+p(p-2), 2,...,2 and the factorization through pi_* modulo p. Check that this yields R_p=2u(T_p^2-1)v on full homology, not just after evaluating the period.
2. Verify the factor eta=2c_E between z_E(C_(a,n)) and the complete total-period Kurihara symbol. No silent choice of half-sums modulo sign is permitted.
3. Verify that the polarized closed sequence gives -2XY, while applying the extra differences to the true packet in J^2 gives zero in the mixed quadratic quotient. The source forward shifts correspond to (g^(-1)-1)^2; this causes no leading-degree sign change.
4. Verify the exact scope of the degree-two norm-kernel and the four-old-transfer matrix. Neither is a statement about arbitrary homology or all arithmetic correspondences.
5. Verify that the retained scalar law handles the requested *ideal*, not merely one pair, and that the argument leaves an independent proof of C_p!=0 possible.

The uniform target -2 in I_p^(2) is still open in this return. Do not promote the nonzero formal mixed class to an admitted witness or describe these checks as new primary vanishing. Conversely, do not promote the tested failures to a general impossibility theorem.

Replay the self-contained exact controls with Python 3.9 or newer:

    python3 checks/check.py

They overwrite checks/RESULTS.json deterministically. The proofs of the retained arithmetic imports are not replaced by those controls.
