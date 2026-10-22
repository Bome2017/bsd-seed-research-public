# GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001

Two independent Aristotle proof searches returned complete proofs of the final Gate-R assembly.
Both were externally rebuilt, scanned and type-checked against the shipped specification.

**`rank E_q(ℚ) = 0` is Lean-certified for the H41 family, on mathlib's actual rational point
group, as cardinal-valued `Module.rank ℤ`.**

    STATUS.md          the disposition, the measurements, the boundary
    ERRATA.md          five findings, two of them against my own checks
    SOURCE_REGISTER.md what is in each slot, and the wrapper-layout warning
    00_handoff/        the input, byte-identical
    01_run_A/  02_run_B/   the returns as delivered, with the preserved input separated
    receipts/          external verification — nothing here is a run's own receipt
    MANIFEST.sha256    the authority
    DIGESTS.md         readable digests; omits its own entry

Read `receipts/REACHABILITY_DISCLOSURE.txt` before quoting the result. Reachability was
established before these runs were commissioned; a PASS confirms independent routes and
replication, not difficulty.
