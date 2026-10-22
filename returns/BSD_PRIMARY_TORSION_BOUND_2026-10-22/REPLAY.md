# Replaying the October 22 continuation

The top-level manifest binds this packet. Subdirectory manifests and source
bindings also record their original work sessions; downloaded third-party
paper copies are not bundled, and their hashes/URLs remain recorded. Consult
`SOURCE_COPY_OMISSIONS.json` for those exclusions. Their absence does not prevent
the arithmetic checks below.

Run in a fresh copy, because some checkers write their output JSON:

```sh
python3 verify_manifest.py
python3 arithmetic/verify_and_replay.py
python3 arithmetic/scaling_check.py
python3 theory/check_primary_packing.py > /tmp/primary-packing-replay.json
python3 review/independent_primary_packing_check.py
python3 review/check_pro_norms.py
```

The first command needs PARI/GP 2.17.3, with its executable supplied in `BSD_GP`
if the recorded host path does not exist. It uses fresh temporary directories,
a 512 MB PARI stack, and a 130-second bound for each GP invocation. The norm
recheck needs SymPy. The independent packing and scaling checks use only the
Python standard library. No computation uses a known Sha dimension or order as
an input.

The supplied Pro packet has its own `inputs/BSD_FIN_SOURCE_EXPERIMENTS_2026-10-21/REPLAY.md`
and original 45-entry manifest. Its full raw arithmetic data is preserved here.
The supplied private-support C checker needs GMP; this return records its replay
separately in `review/PRO_PACKET_CHECKS.json`. Compiler binaries are not bundled.

The mathematical review is `review/PRIMARY_PACKING_REVIEW.md`; successful code
execution alone does not establish the antecedent field, regulator, or analytic
theorems. No complete class group at coefficient primes greater than five was
computed. FIN, ORDER9, and Q36 remain open.
