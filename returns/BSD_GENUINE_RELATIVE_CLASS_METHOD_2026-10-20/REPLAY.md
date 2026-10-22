# Replay without modifying the sealed evidence

The original GP scripts preserve the absolute input paths actually used.
All five small input files are included and SHA-256-bound in
`inputs/BINDINGS.json`. Prepare a fresh working copy:

```sh
python3 prepare_replay.py /tmp/bsd-relative-replay
```

This checks the input hashes (and root manifest when present), copies the
packet, and changes only the named input paths in the copy. It does not
execute arithmetic. Original receipts continue to bind the original
scripts, not the rebound copy. `REPLAY_PATH_BINDINGS.json` records both.
It moves the four verifier-generated GP output files into `recorded_outputs/`
inside the copy, preventing GP's append semantics from duplicating their
objects on the first replay. Before repeating the verifier sequence, move
those four regenerated files aside again or prepare another fresh copy.
The old `rejected_*` directories are failed preflights retained as history;
they are not accepted results or replay targets.

Use PARI/GP 2.17.3 and Python 3.11 or newer. From the replay copy's `review/`
directory, the following independently check saved identities/support,
the unit kernel, and the support's position relative to the generator
cutoff:

```sh
gp -q -f -s 512M replay_relative.gp
gp -q -f -s 512M replay_support.gp
gp -q -f -s 512M replay_unit_kernel.gp
gp -q -f -s 512M replay_private_support.gp
python3 check_support_rank.py
python3 check_complete_accounting.py
```

Successful GP runs must print their completion markers without `***`
errors. GP's exit code alone is not acceptance. Saved `.out` and `.err`
files record the observed markers; timings need not reproduce.

The inexpensive algebraic/generator checks are:

```sh
cd ../theory
python3 check_bddf.py
cd ../scaling
python3 orbit_scaling.py
```

These recompute the rational criterion test, every saved seed point count,
and the finite Frobenius-orbit panel. They do not compute complete class
groups at p=7,11,13. To regenerate the prime inventory, use
`review/prime_orbits.gp`; the saved norm inventory includes all prime ideals,
not only faithful columns.

The producer's `write` calls append GP objects. Do not rerun producers on
populated output files without first moving their generated outputs aside
in the replay copy. In particular `relative_batch.gp` writes
`batch_rows.gp`; a second append would create duplicate rows. The original
profiler is macOS-specific and records its actual GP executable; it is
historical custody, not a portable launcher. The replay commands above
bypass it.

Hash verification proves custody. Exact identity and rank replays support
the bounded calculation. Neither establishes the retained global seed
hypotheses or an unconditional class-generation theorem.
