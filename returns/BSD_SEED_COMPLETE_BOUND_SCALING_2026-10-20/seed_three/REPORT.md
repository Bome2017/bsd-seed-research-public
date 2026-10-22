# Actual seed at three: existing complete bound is already attained

**Status: no new upper bound; old arithmetic replayed; no repeated expensive
certification.**

The new `1664n1` control calculation does not create a new rejection at the
actual seed's coefficient prime three. This is the exceptional prime where
the accumulated record already supplies positive excess.

The existing four exact source representatives have independent residue
classes. Their ordinary ideal-class image matrix is

    [0 2 2 2;
     0 0 2 2] mod 3,

of rank two. Their actual affine incidence norms are literal cubes. The
ordinary unit norm kernel has dimension two. The source presentation gives
the ordinary minus 3-class group `C3 x C3`, **conditional on the old
GRH-dependent class completeness**.

Consequently the old complete ordinary norm-kernel bound is

    unit kernel 2 + class kernel 2 - connecting rank 0 = 4.

It is attained by the four representatives. The full containing S-source
also has dimension four under the retained class and index inputs: the
S-prime classes absorb the ordinary class contribution into the S-unit
presentation. Adding the ordinary class dimension again to the S-unit rank
would double-count it. These statements, including the companion groups
`C3^3` and `C3^2`, were already derived on October 18.

Thus an experiment at this prime should not seek an upper bound of two or
three. The existing representatives already obstruct that target. This
conclusion concerns the known actual source elements, not a conjectural
Sha order. Their all-place membership remains its separately retained
certificate; this lane only replays finite matrix data.

## The unfinished completeness step

The original source class computation reports `[12,6,2]` and used a
GRH-dependent BNF search. Its later class-quotient certification invoked
`bnfcertify(B,1)`, printed a Zimmert bound of
`226849291805255087108915200`, and timed out at 90 seconds. A successful
flag-one certificate would suffice for a class upper bound; it would not
certify fundamental units automatically. No certificate was returned.

We inspected this failure before allowing any retry. The installed PARI
interface offers flag zero/full certification or flag one/class-quotient
certification, not a flag certifying just the 3-primary part. No changed
bounded certification method was implemented here, so the same job was not
restarted with a slightly larger time limit.

An exact relation matrix does not alone prove that its named primes
generate the true class group. The existing point-supported classes show
the incidence and connecting maps vanish on the known two-dimensional
class sector. They do not bound an undiscovered class sector.

The possible alternatives—certify generation of the source S-class group,
bound the relevant ordinary class-map kernel independently, or prove a
complete relative class presentation—still need their own generating or
index bound. The current explicit relations do not supply one. This is a
statement about the inspected computation, not a claim that such an
algorithm or theorem cannot be constructed.

## Effect on the current experiment

This lane prevents spending the new scaling test on an already attained
positive-excess exception. It contributes no new small-bound evidence at
larger coefficient primes. The actual-seed tests at primes at least five
must be assessed separately, keeping all unit, ordinary-class and
valuation terms.

`recheck.py` independently replays the saved matrix solve, four-dimensional
residue independence, class-image rank and zero saved valuation/local rows.
It does not rerun the literal norm-cube or all-place Selmer certificates.
`RESULT.json` preserves those boundaries. FIN, ORDER9 and Q36 are unchanged.

## Sources inspected

- `/Users/bsm/BSD_SMALL_BOUND_CONTINUATION_2026-10-18/class_control/PROOF.md`
- `/Users/bsm/BSD_SMALL_BOUND_CONTINUATION_2026-10-18/class_control/inputs/MATRICES.json`
- `/Users/bsm/BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15/seed_class/REPORT.md`
- `/Users/bsm/BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15/seed_class/source_quotient_cert/RECEIPT.json`
- `/Users/bsm/BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/RETURN.md`
- Installed PARI/GP `?bnfcertify` help, checked 2026-10-20.
