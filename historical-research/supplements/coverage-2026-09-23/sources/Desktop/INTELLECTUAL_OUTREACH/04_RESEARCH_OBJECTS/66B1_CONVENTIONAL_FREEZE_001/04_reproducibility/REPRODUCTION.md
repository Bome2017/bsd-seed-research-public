# Reproduction

All four supplied verification programs replay clean in this tree.  Outputs are in
`_receipts/replay/`.

| script | how to run | result |
|---|---|---|
| `02_second_referee/frozen_stage_I/66b1_stage_I/verify_stage1.py` | `cd` there, `python3 verify_stage1.py` | exit 0 |
| `02_second_referee/hostile_comparison/66b1_comparison_audit/verify_audit.py` | `cd` there, `python3 verify_audit.py` | exit 0 |
| `01_first_model/continuation_receipts/verify_continuation.py` | **via the wrapper below** | exit 0 |
| referee `CHECKSUMS.sha256` | `04_reproducibility/checksums_replay/`, `shasum -a 256 -c CHECKSUMS.sha256` | 6/6 OK |

Requirements: Python 3 with `sympy`; `mpmath` for the first model's period script; a C++17 compiler
if you want to regenerate `referee_counts.csv` (not required — the CSV is retained).

## Environment-specific absolute paths — identified, not repaired in place

`01_first_model/continuation_receipts/verify_continuation.py` is **byte-identical to the first
model's original** and hardcodes two absolute paths from that model's sandbox:

    /mnt/data/pk66_continuation
    /mnt/data/pk66_independent/PRE_COMPARISON_RECONSTRUCTION.md

Per the freeze mandate the original was **not edited**.  `wrapper_verify_continuation.py` stages the
expected layout in a temporary directory, rebinds only the path prefix, and runs the retained logic
unchanged.  Reported exit status: **0**, with `"exceptions": []`.

No other retained script contains an absolute path.

## The referee's CHECKSUMS.sha256 lists a file its own archive does not ship

`66b1_stage_I/CHECKSUMS.sha256` includes an entry for
`ORIGINAL_INPUT/PK66B1_DESIGN_PACKET_2026-09-10.zip`, which is not inside that archive — the referee
checksummed the input packet it was given without redistributing it.  The five shipped entries
verify OK on their own; the sixth cannot be checked from the archive alone.

`checksums_replay/` reassembles the referee's expected layout by supplying the design packet from
`_external/originals/` at that relative path.  All **6/6** entries then verify, which confirms the
referee checksummed the same design packet that is frozen here.
