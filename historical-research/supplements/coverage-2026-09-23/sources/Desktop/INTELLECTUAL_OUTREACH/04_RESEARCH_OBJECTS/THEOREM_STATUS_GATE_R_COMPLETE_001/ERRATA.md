# ERRATA

Recorded, not hidden. One defect, mine, found and corrected before this object was released.

## E1 — a dangling file reference, and the superseded first archive

`receipts/CUSTODY_REPLAY.txt` was generated with a closing paragraph pointing at
`STATUS_VERIFICATION.txt`, a receipt that did not exist. The object was sealed and archived in
that state, producing archive

    c26a9745536c410acf94a3a7df04a58f0f11f48a42ee3965791297b9a14080e2   SUPERSEDED, never released

The defect was found immediately afterwards, during pre-release checking, and before the object
was delivered, cited or bound by anything.

This is the same defect family as E5 in `CODEX_GATE_R_BLIND_AUDIT_FREEZE_001/ERRATA.md`, where a
packet shipped a document citing a file it did not contain. Having recorded that against someone
else's document, shipping it in my own would not do.

**Correction:** the missing receipt was written with the object's actual verification figures —
it was genuinely wanted content, not a reference to be deleted — and the object was re-sealed and
re-archived. The superseded archive digest is recorded above so the record shows exactly what
happened rather than presenting the second archive as the only one there ever was.

No frozen object outside this one was touched. Nothing was repaired in place in any predecessor.

The same reference check, run properly, also found three cross-object references that were
attributed in prose but not path-qualified — to `THEOREM_STATUS.md`, to the handoff's `TASK.md`,
and to Codex's `HypothesisUsage.lean`. None was broken; each named a file that exists. All three
were qualified with their containing object before release, so an auditor can locate them without
guessing. That re-seal superseded a second archive:

    c26a9745536c410acf94a3a7df04a58f0f11f48a42ee3965791297b9a14080e2   first,  never released
    (second intermediate seal)                                          never released

Only the third and final archive was released. Both superseded digests are recorded here rather
than quietly dropped.

**Correction going forward:** when a generated receipt or document names another file, that name
must be checked against the object's own file list before sealing, and a name that belongs to
another object must be written with that object's path. The check is one line and it has now cost
two objects.
