# Portable arithmetic replay

The executed arithmetic scripts and their manifest are frozen. The preparer validates all 42 arithmetic manifest entries, the five portable input bindings, and the complete file-dependency chain of the four production stages. It fails on an unmatched absolute source path or an intermediate input without a prior producer.

From this packet's root directory, first perform the read-only check:

```sh
python3 prepare_replay.py --check-only
```

Prepare a fresh replay directory, supplying the PARI/GP executable if it is not on PATH:

```sh
python3 prepare_replay.py --dest replays/verification-001 --gp /absolute/path/to/gp
```

Then execute the four ordered stages:

```sh
python3 replays/verification-001/run_all.py
```

`run_all.py` requires the recorded PARI/GP version 2.17.3. Alternatively, set `BSD_GP` before running it. No GP process is launched by the preparer itself. A preparation receipt is not a mathematical replay receipt.

The stage order is norm_screen, geometric_gcd, geometric_rank, geometric_units. Each uses a 120-second process-group wall limit and 512 MB PARI stack limit. A missing marker, a nonzero exit, a caught PARI error or a timeout prevents acceptance. run_all stops unless each stage's receipt says accepted.

All source reads are rewritten to the hash-bound files in inputs/. Every generated GP file is rewritten to the fresh replay directory, including intermediate reads and all optional outputs. The copied runner writes its logs and receipts beside itself. The original arithmetic directory is not changed. Do not move a prepared directory before execution, because prepared file paths are absolute; prepare again after relocating the packet instead.

Replaying into a directory with old outputs is rejected. Choose a new destination for another run. The saved results are never copied into the new replay directory.

The expected final arithmetic is:

- 31 distinct geometric functions, none individually supported entirely at bounded rational primes;
- 124 scalar elements and134 coprime ideal atoms;
- faithful full/outside ranks 20/20 for both characters, hence closed rank 0;
- 84 exact anti-divisor-kernel products equal 1.

These results reproduce the finite-family outcome. They do not certify a complete class-group computation or change FIN, ORDER9 or Q36.

Preparation check performed in this return: all hashes and transitive dependencies validated; generated Python source compiled; runtime-version guard checked on sample version strings. The four arithmetic stages were not rerun as part of preparing this helper.

## Quick exact arithmetic and custody checks

After sealing, run `python3 verify_packet.py --quick` from any directory. This checks the root, arithmetic and theory manifests and the portable field bindings, then reruns the producer's exact outward bound, the reviewer's separate rational bound, the parent's coarse recombination and the saved exact norm-cofactor screen. It does not run a class-group computation or certify the written proof.

The independent geometric review also reran actual principal ideals, scalar actions and all84 unit products; `review/FINAL_REVIEW.md` gives its scope. The original GP audit scripts retain their execution paths. To reproduce production in a new location, use the portable preparer above rather than editing those originals.
