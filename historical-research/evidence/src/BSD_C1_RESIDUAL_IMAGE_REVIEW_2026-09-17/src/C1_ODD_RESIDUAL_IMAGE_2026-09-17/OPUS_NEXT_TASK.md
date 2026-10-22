# Opus next task: review a POSITIVE uniform residual-image theorem

Inputs: PROOF.md, verify.py, EXACT_CHECK_RECEIPT.json, SOURCES.md, and the preserved latest central-involution review.

This is a new arithmetic proof, not another norm-channel audit or generic-radical search. Use Opus. Do not call Fable unless you isolate a precise disputed inference that needs independent adjudication.

## Statement to check

For every positive m,n with m, A=m+16n^2, B=m+25n^2 primes 11 modulo 24, the curve

    y^2=x^3-5Ax^2+4ABx

has full GL_2(F_ell) image for EVERY odd prime ell.

## Reconstruct before replay

1. Verify 12|n, A>163, invariants and multiplicative primes m (I1), B (I2).
2. Over Q_A^nr(u), u^4=A, reconstruct the good model and the actual inertia descent action (X,Y)->(-X,iY). Verify good-reduction comparison, T^2=-I, determinant one, trivial wild action, and F T F^-1=T^A=T^-1. Check absolute irreducibility for every odd ell != A, including ell=3. Do not infer a nonscalar order-four action from the Kodaira label alone.
3. Reconstruct the Tate-curve transvection argument at m or B, handling ell=m by switching to B and nonsplit multiplicative reduction by its unramified twist.
4. Prove the prime-field group lemma. Flag any accidental use over nonprime finite fields.
5. Check the sole coefficient exception ell=A: Mazur's rational prime-isogeny bound plus A>163 supplies irreducibility; then the transvection at m completes the proof. Preserve the source-reading qualification concerning Mazur's original paper.
6. Independently verify the C60 superfamily consequence and the example. C60 is NOT a rename, replacement or silent expansion of the canonical C1 lane. Preserve the original definition.

The checker verifies finite consequences, not the universal theorem. Reading its PASS is not the mathematical audit.

## Deliverable

One private report, with exact proof dependencies and one of:
  ALL_ODD_RESIDUAL_IMAGE_VERIFIED
  RESIDUAL_IMAGE_RESULT_REQUIRES_CORRECTION
  UNKNOWN

If the proof fails, quote the exact first invalid inference and give a counterexample or the missing hypothesis. Retain any proved narrower conclusion. Do not claim impossibility of all residual-image methods.

If it passes, propose a concise author-side addendum recording the positive theorem and that the old modulo-7 irreducibility restriction was sufficient but unnecessary. Do not pretend a new Galois-image theorem is a Sha bound or a valued arithmetic witness. Do not promote all individual mod-ell images to a full adelic product.

For the accepted central-involution review, the main agent can integrate ACCEPTED_REVIEW_NOTE.md through the usual custody process. This task itself writes no shared file.

## Resource / concurrency / scope

- Maximum 60 aggregate CPU-seconds, 1 GiB, one process/thread.
- Existing Python/Sage/PARI may be used for small symbolic/local checks; no installation.
- No number-field construction, class group, unit-group basis, bnfinit, bnfcertify, bnftestprimes, high-conductor modular symbols, or calibration.
- Do not repeat the exhausted subgroup-lattice/norm search or generic-radical analysis.
- No K33/STAR/TEN task.
- Private output directory; shared files, ledgers, seals and memory are read-only.
- No automatic next-stage escalation. The missing class/Sha arithmetic remains separate.
