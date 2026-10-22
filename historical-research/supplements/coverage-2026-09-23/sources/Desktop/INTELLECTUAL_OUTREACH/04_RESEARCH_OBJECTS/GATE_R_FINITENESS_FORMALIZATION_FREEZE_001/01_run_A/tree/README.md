This project was edited by [Aristotle](https://aristotle.harmonic.fun).

To cite Aristotle:
- Tag @Aristotle-Harmonic on GitHub PRs/issues
- Add as co-author to commits:
```
Co-authored-by: Aristotle (Harmonic) <[contact-address-redacted]>
```

# ARISTOTLE_GATE_R_FINITENESS_V1

One bounded target, following the whole-program audit's recommended next formal step.

    TASK.md                             the mandate — read first
    FORMALIZATION_BOUNDARY.md           what this does and does not establish
    CUSTODY.md                          frozen sources and what may be touched
    CERTIFIED_STATEMENTS_ELABORATED.txt all 327 certified theorems, full elaborated types
    gen_statements.lean                 the elaborator that generated that file
    RequestProject/GateRFinite/Finiteness.lean   THE JOB — one theorem, one sorry
    RequestProject/**                   the frozen certified base, Gate R included
    MANIFEST.sha256  DIGESTS.md         custody

The identical byte string of this packet is delivered to two independent proof searches, which do
not communicate.  Their returns are compared externally.

The target:

    Finite ((P01.Ecurve ε m q).toAffine.Point)

under the existing `Params` and `H41`.  Everything it needs is already a theorem in this tree.
