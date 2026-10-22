# BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19 — canonical freeze root (A1 + A2)

## COMBINED RETURN: **A1_A2_FREEZE_PASS_WITH_CUSTODY_REPAIR**

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the
> antecedent is easier than FIN or that FIN has been reduced. What is and is NOT proved: `FORMALIZATION_BOUNDARY.md`.

```
A1: CONDITIONAL WC FINITE ALGEBRA = LEAN MACHINE-CHECKED          LEVEL = A1_FULL  (20/20, incl. 3 stretch)
A2: PRIMARY SUPPORT / CONTENT / ASSEMBLY = LEAN MACHINE-CHECKED   LEVEL = A2_FULL  (28/28, incl. 3 stretch)
ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED
FIN STATUS = UNCHANGED            FORMULA STATUS = UNCHANGED
#Sha = 9 t^2 (gcd(t,30)=1) formally checked under its exact abstract hypotheses — NOT #Sha = 9
```

| | A1 — witness content | A2 — primary support |
|---|---|---|
| freeze directory | `A1_WITNESS_CONTENT_FULL/` (MANIFEST 56 entries, 56/56 OK, exact file set) | `A2_PRIMARY_SUPPORT_FULL/` (MANIFEST 59 entries, 59/59 OK, exact file set) |
| final archive | `A1_WITNESS_CONTENT_FULL_FREEZE_2026-09-19.tar.gz` | `A2_PRIMARY_SUPPORT_FULL_FREEZE_2026-09-19.tar.gz` |
| SHA-256 | `baa0435220954626b3f14a82fb874062d44267447ff1400748175ea55b276de0` | `fd55eab35ef1e51e5caaadc729f2f99d986e6158b2f4ca54d0b31d224f5d541c` |
| size | 104 011 bytes | 101 462 bytes |
| Lean / mathlib | 4.28.0 (7e01a1bf5c70fc6167d49c345d3bf80596e9a79b) / `8f9d9cff6bd728b17a24e163c9402775d9e6a365` | same |
| fresh replay of the returned archive | FROZEN 6/6; `Build completed successfully (8037 jobs)`, 0 sorry / 0 warnings; `LEVEL: A1_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, stretch 3/3; axioms ⊆ {propext, Classical.choice, Quot.sound}; TypeIntegrity 20/20 | FROZEN 6/6; `Build completed successfully (8040 jobs)`, 0 sorry / 0 warnings; `LEVEL: A2_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, stretch 3/3; axioms ⊆ {propext, Classical.choice, Quot.sound}; TypeIntegrity 28/28 |
| fresh replay of the final freeze archive | manifest 56/56, exact file set; FROZEN 6/6; `Build completed successfully (8037 jobs)`, 0 sorry; `LEVEL: A1_FULL`, stretch 3/3; TypeIntegrity 20/20; 20 axiom lines, 0 sorryAx, no non-allowed axiom (`final_archive_replays/`) | manifest 59/59, exact file set; FROZEN 6/6; build OK, 0 sorry; `LEVEL: A2_FULL`, stretch 3/3; TypeIntegrity 28/28; 28 axiom lines, 0 sorryAx, no non-allowed axiom (`final_archive_replays/`) |
| frozen files vs original package | 6/6 byte-identical | 6/6 byte-identical |
| custody defect (repaired) | returned inner pre-run MANIFEST stale (21/24; 9 files unbound) — kept as a historical file | returned inner pre-run MANIFEST stale (21/24; 12 files unbound) — kept as a historical file |
| returned Aristotle archive | `provenance/0ee48359-…-aristotle.tar.gz`, `278588e0c570e39379e7dd2a495153d984be12e4269fee212e3830cc15e59948` | `provenance/319b9855-…-aristotle.tar.gz`, `92ba674767e56012572b357ca29e5e90fc6b057a016611808f457df59ed3db50` |
| original package (untouched) | `eba016585d080c5bf8578b3c4454d63a256712a6770ba50f3a0f671667a04763` | `36005a0c92b8c847aea601ca87e33b6284a967ff1d8e295a112ed783b6b79bef` |

The first A1 freeze archive (`dfe5f660d750cbe835f04369db052b6f8d3a5984322ea92a94863d0d9567e1ef`, replayed clean) is superseded
by the final A1 archive above. The `source/` tree is identical, and `A1_FORMAL_BOUNDARY.md` was updated with Codex O1 after the
A2 intake.

## Other contents
- `FORMALIZATION_BOUNDARY.md`: the combined immutable statement of what is and is NOT proved.
- `provenance/`: byte-identical copies of both returned Aristotle archives. The originals in `~/Downloads` are untouched.
- `final_archive_replays/`: fresh-unpack replay logs of both final archives, plus the replay of the first A1 archive.
- `handoff_patch_backup/`: the pre-A1-patch handoff (12 files).
- `handoff_patch_backup_2/`: the pre-A1+A2-patch handoff (12 files).
- `STATE.json`, `RESUME.md`, `MANIFEST.sha256`: container custody. The manifest binds everything here except itself.

## Handoff
`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19` is now `CODEX6_HANDOFF_PATCHED_A1_A2_FREEZE` (manifest 11/11). The exact patches are
listed in its STATE.json `patch_log`.

## Codex notification
**None sent.** No substantive mathematical discrepancy was found, and the A1/A2 formalizations do not change the arithmetic
frontier. Codex already records WC ≠ easier than FIN (Theorem O1) and itself authored the Albertson gate. A one-line
future-session note was added to the handoff instead.
