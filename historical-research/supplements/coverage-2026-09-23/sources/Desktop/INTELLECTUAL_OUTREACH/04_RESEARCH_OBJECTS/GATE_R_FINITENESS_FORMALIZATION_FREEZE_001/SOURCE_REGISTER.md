# Source register

| Slot | Content |
|---|---|
| `00_handoff/` | `ARISTOTLE_GATE_R_FINITENESS_V1` exactly as released. Archive `3d1db03e1f8e7fa2c45a545b730db0ff7da1d32adf7540c43f730047cb76e573`. |
| `01_run_A/tree/` | Run A working tree as delivered. Wrapper `ca281665-83e0-477e-bb37-b680549bcda5-aristotle.tar.gz`, sha256 `70cf6a5ccd85b4e6aeacd46dbb6fbbda217fd7466588d4f172bc219dd1b7dc80`. Returned `Finiteness.lean`: 164 lines, 0 code `sorry`. |
| `02_run_B/tree/` | Run B working tree as delivered. Wrapper `60597b64-4229-4673-8907-c9ee7a20e746-aristotle.tar.gz`, sha256 `b910a3211b1ab6a63478b47f6f6dbeb3a9f80ff76bc3c25c84b988cff4b56844`. Returned `Finiteness.lean`: 170 lines, 0 code `sorry`. |
| `0*/preserved_input_archive/` | The input archive each wrapper carried. Both hash to the released packet. **Neither wrapper carried an extracted copy of the input**, so there is no nested-skeleton trap in this pair. |
| `receipts/` | Claude's external verification, with the tools that produced it: the corrected scanner, its injected axiom control, the type-identity audit, the footprint elaborator, and the withheld reachability module. |

Both runs shipped their own construct scanner with an injected axiom control, as `TASK.md` required.
Run A's aborts with FAIL if the control is not detected and deletes the control afterwards. Those
files are preserved inside `0*/tree/verif*/` as delivered. They are the runs' own evidence and are
not substituted for mine.

Upstream: `GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001` (`5cf07602…`) supplies the certified base
including the five Gate-R theorems. `ULTRA_WHOLE_PROGRAM_AUDIT_FREEZE_001` (`0687eb63…`) is the audit
that identified this consequence and recommended it as the next bounded target.
