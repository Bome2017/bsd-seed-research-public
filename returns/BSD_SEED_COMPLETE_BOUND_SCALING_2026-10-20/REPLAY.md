# Replay and custody

Use copies for executable replays because some producers overwrite their
JSON/output files. The supplied manifests bind the original outputs.

The validated PARI executable used here is recorded in the lane receipts:
`/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp`.
Python uses the standard library.

- `seed_three/recheck.py`: saved matrix arithmetic only; no BNF or source
  theorem re-audit.
- `seed_five/replay.py`: authenticated field/scalar/divisor/local stages,
  in temporary directories; no class-group rerun.
- `same_curve_scaling/replay_units.gp` and `check_profile.py`: literal unit
  products and whole-unit/valuation profile. BNF is only a candidate
  generator, not a completeness premise for the accepted unit argument.
- `review/replay_fields_and_units.gp`, `run_field_replay.py`,
  `replay_export.gp`, `replay_residues.py`: separately implemented
  authentication and residue extraction. The associated receipts record
  their exact scope.
- `uniform_valuation/check_uniform_valuation.py`: construct actual finite
  vector/covector orbits and primitive incidence matrices, then compare
  with the predicted local formula. Timing fields vary. It is a same-code
  replay, distinct from the written uniform proof.

Do not relaunch the rejected class-group jobs merely to replay a manifest.
The original failure receipts are evidence of unsuccessful execution,
not arithmetic outputs. In particular an exit code0 with GP alarm text
and no completion marker is rejected.

No new p7 point-field run is hidden in this packet. The scaling test is
p3 to p5 on the same curve, plus actual seed p5 and the uniform local
calculation. Existing earlier p7 source and class failures were inspected
before choosing the present bounded tests.

Root MANIFEST.sha256 includes all nested files except itself and disposable
Python caches. Nested manifests are preserved and independently checked.
Publication custody is stored outside the sealed packet.
