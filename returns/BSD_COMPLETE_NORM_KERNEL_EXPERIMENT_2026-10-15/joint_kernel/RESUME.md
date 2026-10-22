# Resume: full-source joint kernel

Complete. Read REPORT.md, then KERNEL_RESULTS.json, ADMISSION_FILTRATION.json and433_COMMON_REPAIR.json. No further prime scan is needed for this result.

Run `python3 replay.py` from any directory. It uses an isolated copy and checks five canonical outputs byte-for-byte. No GP, BNF, rank or upstream norm computation is rerun. All working inputs exclude the known excess columns; these are only in heldout/ and read by compare_holdout.py after KERNEL_RESULTS.json is written and hash-bound.

Original norm maps are copied into exact_global/ with source hashes. Fresh authenticated433 local rows are in inputs/433a1_matrices.json, with the previous retained rows also preserved; they are identical. Source containment/completeness remains conditional or unconfirmed for seed3/28042a1; do not infer whole-Selmer absence from their displayed-source kernel.

Fresh433 provenance: SCAN_CONTRACT.md andSCAN_SEAL.json precede the first-six-eligible scan. The unexecuted initial script seal was superseded only to add the explicit1GB stack ceiling. Accepted scan is433_scan/scan.gp, with receipt and raw output. Literal full-source element export and standard-library replay are retained there and in FRESH_433_LITERAL_REPLAY.json.

For a fresh GP replay, first copy the folder to a disposable directory and remove scan.gpdata from that copy's433_scan/ before invoking run_stage.py (GP write appends). Do not rerun into frozen originals. The stored run_stage.py uses stdin and the known local GP binary; scripts have alarms and the scan explicit stack cap.

No seed endpoint changed. The complete controls certify kernel coverage, not absence of the detected image. The source-compatible false columns live in the multiplicative residue target until global admission; only admitted Selmer columns have the elliptic Kummer interpretation.
