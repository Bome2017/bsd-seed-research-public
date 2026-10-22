# Replay guide

Start with `python3 verify.py`. It verifies all root/nested manifests and runs four small arithmetic checks in an isolated copy, comparing their results to the saved records. It requires Python3 standard libraries. The density-result path is normalized for the temporary copy; all mathematical fields must match.

The first two root-authored arithmetic implementations are independent of the producer's finite-field routines:
- `independent_review/check_local.py`: actual rational field polynomials, Hensel leading-unit characters, elliptic addition, quotient signatures and representative changes;
- `independent_review/check_frobenius.py`: actual source and norm polynomials, all40 fresh primes, all8 affine lines and32 nonzero-sum equations at each.

Additional PARI replays, already performed in this return:
- `frobenius/replay.py` reconstructs exact norms and literal source bindings in a temporary directory, including the fixed degree24 polynomial.
- `secondary/run_replay.py` checks exact norm roots and cube-rescaling countercontrols.
- `local_signatures/` retains the scan/export GP scripts, raw output, literal replay, and representative controls. Their execution receipts state the runtime, bound inputs and output markers.

These require PARI/GP and the supplied saved objects. The original runtime is recorded in receipts. No licensed Magma, new class-group certification, online job or paid service was used. The captured GP data include intermediate failed serialization/export attempts explicitly labelled as rejected; they are evidence of repairs, not accepted outputs.

The packet does not include the entire historical research corpus. Antecedent membership/rank/saturation proofs are retained at their original grades and pinned to the preceding lab return. Every new arithmetic input needed by the listed replays is supplied or identified by the per-lane binding.
