# GATE_R_FINITENESS_FORMALIZATION_FREEZE_001

Two independent Aristotle proof searches returned complete proofs that the actual rational point
group is finite. Both externally rebuilt, scanned, type-checked and measured.

    E_q(Q) is finite, Lean-certified for the H41 family.

    STATUS.md            the disposition and the boundary
    SOURCE_REGISTER.md   what is in each slot
    00_handoff/          the input, byte-identical
    01_run_A/  02_run_B/ the returns as delivered
    receipts/            external verification, and the tools that produced it
    MANIFEST.sha256      the authority
    DIGESTS.md           readable digests; omits its own entry

Highlights. Zero shared private helper names between the two proofs — the cleanest separation
measured in this programme. Both derive `AddGroup.FG` internally rather than assuming it; adjudicated
in `receipts/AddGroup_FG_ADJUDICATION.txt`, which also records two defects of mine that the
adjudication exposed. Neither run took Claude's withheld route, and theirs is arguably better.
