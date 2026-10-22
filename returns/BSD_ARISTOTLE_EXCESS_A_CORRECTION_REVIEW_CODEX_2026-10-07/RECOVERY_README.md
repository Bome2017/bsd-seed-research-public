# Recovered certificate core and replay limits

The `certificate_core/` directory is an unchanged copy of all 1,070 entries of the historical certificate manifest, with that manifest included. Its source directory is

`/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21`.

All entries matched before copying. The copied directory includes C sources, a host-specific binary, build bindings, result and metadata files, original logs, all atomic units, and historical scripts. Those scripts are evidence, not instructions to restart a computation. The historical absolute paths have not been silently rewritten.

`checks/HOST_CERTIFICATE_RECOVERY.json` gives every recovered file's hash and size. `checks/HOST_METADATA_REPLAY.json` records a fresh run of the reviewed original metadata checker with its sole output write redirected here. The adaptation is explicit in `checks/replay_host_metadata.py`. The historical COMPLETION_REVIEW.json was not overwritten.

The original checker field `fresh_recombination_identical` compares the old run and old combine logs. Our separate `FRESH_COMBINE_RECEIPT.json` and `FRESH_COMBINE.log` record an actual combination performed on October 7, using the original hash-bound binary and saved units. The result matches the original combine log byte-for-byte. This recomputes the aggregation and tail enclosure, not all finite-sum terms.

The coefficient prefix remains external: 206 coefficient files, totaling 661,125,220 bytes, plus their verifier records. They were rehashed against the stored bindings during this review; they were not re-witnessed or copied into the small supplement. The original binary depends on the retained FLINT/MPFR/GMP runtime and is not a Linux portable binary. Do not describe this supplement as a self-contained full replay package.

The `checks/trace_workspace/` directory only recreates the specific archive members used by Aristotle's lightweight checker, preserving its archive-only view. That checker was inspected before execution. Its reproduced output is `D23_TRACE_REPLAY.json`; the comparison is `REVISED_PAYLOAD_CHECK.json`.

No new arithmetic obligation was solved. This recovery preserves an existing certified premise and makes the relevant missing evidence accessible for inspection.
