This project was edited by [Aristotle](https://aristotle.harmonic.fun).

To cite Aristotle:
- Tag @Aristotle-Harmonic on GitHub PRs/issues
- Add as co-author to commits:
```
Co-authored-by: Aristotle (Harmonic) <[contact-address-redacted]>
```

# ARISTOTLE_GATE_R_FINAL_ASSEMBLY_V1

One bounded target: the final Gate R assembly.

    TASK.md                             the mandate — read first
    FORMALIZATION_BOUNDARY.md           what this does and does not establish
    CUSTODY.md                          frozen sources and what may be touched
    CERTIFIED_STATEMENTS_ELABORATED.txt every already-proved theorem, full types
    gen_statements.lean                 the elaborator that generated that file
    RequestProject/GateR/Assembly.lean  THE JOB — five theorems, five sorries
    RequestProject/**                   the frozen certified base
    MANIFEST.sha256  DIGESTS.md         custody

The identical byte string of this packet is delivered to two independent proof
searches, which do not communicate.  Their returns are compared externally.
