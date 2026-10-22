# Replay and custody

The uploaded archive has SHA256 `6b7dd0ef38624e5bf33bf14581c39c4e5d2bc708ff7dea9df8ec56938e2a244a`.
It contains eight files, including its seven-entry SHA256SUMS. All entries verify.
The complete added-file patches read from GitHub at commit
`0048c241f4737ddc5b6d4044a04599d3910a96da` reconstruct the same eight files byte-for-byte.
See `checks/REMOTE_CHECK.json` and `checks/CUSTODY_CHECK.json`.

Commands from this return's root:

```sh
python3 input/BSD_LOCAL_OBSTRUCTION_DETECTOR_2026-10-13/checks/verify.py
sage -python audit/independent_local.py
python3 seed_probe/verify_seed_probe.py
```

For a fresh producer scan, from `seed_probe/`:

```sh
gp -q scan.gp > scan.out 2> scan.err
python3 verify_seed_probe.py
```

The audit was executed with the installed Sage environment's Python at
`/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python`.
The producer used PARI/GP 2.17. The independent seed checker uses Python's standard library.
The supplied checker reproduces its saved JSON byte-for-byte. Separate implementations
reproduce the four signatures, exact compositum identity, and all 47 admitted seed scan rows.
`checks/REPLAY.json` records successful independent replay with empty stderr.

The probe's `PRE_RUN.sha256` seals its protocol and producer before execution.
These files preserve a same-session experiment record; hashes do not supply independent
timestamp certification. The independent checker verifies arithmetic, not rank, saturation,
Selmer membership or a BSD theorem. Review scope and imported grades are stated in AUDIT.md.
