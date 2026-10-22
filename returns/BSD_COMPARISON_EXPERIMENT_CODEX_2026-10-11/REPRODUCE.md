# Reproduction and evidence boundary

Read REPORT.md, torsors/RESULT.md and geometry/GLOBAL_TORSOR_REVIEW.md first. The global comparison uses exact algebra together with a written Galois argument; output files alone are not its proof.

## Supplied data, no original host corpus required

`python3 checks/verify_saved_evidence.py` uses the supplied compressed coefficient vectors to recompute both stabilized Sturm comparisons and all sealed local predictions. It verifies their input hashes and checks the exact modulo-25 trace failure. This is saved-vector replay, not independent generation of every coefficient.

The following programs require SageMath (the executable used here was `/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python`). Use a Sage Python interpreter, not ordinary Python. Each program is run from its indicated folder:

- In `torsion/`: `verify_saved_maps.py`, `verify_addition_quotient.py`, `verify_pairing.py`. These check actual division-scheme maps, universal addition and the pairing multiplier. The earlier `verify_addition.py` is a superseded expensive exploratory method, not the source of the successful certificate.
- In `torsors/`: `verify_saved_torsors.py`, `verify_torsor_action.py`, `verify_torsor_action_113.py`. The saved verifier uses only supplied rational coefficients, without searching for new roots. It checks 16 exact facts per partner. The action programs check 25 distinct torsion translations per partner; their finite-field basis is checked with a nontrivial Weil pairing.
- In `checks/`: `mixed_instrument.py` and `mixed_instrument_held_out.py` recompute genuine fifth-division Kummer cocycles. They recreate outputs and elapsed times; run in a working copy if preserving manifest bytes.
- `python3 geometry/toric_mu5.py` is the independent standard-library nodal group control.

`torsors/find_torsor_map.py` and `find_torsor_map_113.py` reproduce the discovery by factoring the target degree-25 polynomial over the source field. The saved-map verifier is the simpler replay route. Running discovery rewrites phase-specific files, so use a working copy.

## Original full coefficient generation

`admission/run_admission.py` binds the historical partner-screen input and a host PARI/GP executable, runs all full coefficient generation, exact rank bounds and independent controls. These two host paths are external dependencies for that original reproduction command. The selected three curve equations, the executed GP input, exact transcript and complete resulting coefficient vectors are included; the large unrelated partner-screen file is not. `admission/executed.gp` contains the original absolute output paths. To rerun generation elsewhere, direct those outputs into the working-copy admission folder and use an installed PARI/GP with elliptic-curve functionality. Database elldata is not required because all curves are given by equations.

The original producer is not a second independent coefficient engine. The 274 direct point-count controls are independent of its elliptic arithmetic, but cover only their stated finite primes.

## Check grades

Rational and finite-field calculations are exact, using Sage/PARI. The parent independently replayed all 8 saved torsion coordinate maps, 4 universal group-law maps, the pairing checks, 32 saved torsor facts, and 50 distinct translation checks. A separate team agent reviewed the global affinity proof and local normalization and independently replayed the saved torsor facts, including another scalar check at the good prime 4261. Its verifier is geometry/replay_global_torsors.py. This remains same-team computational/written validation, not Lean or an external mathematical review.

The sealed-held-out receipt records predictions made after the discovery set and before eight further tests. It is a workflow record, not cryptographic proof of chronology against an adversarial author. Global validity rests on the torsor argument, not that chronology or any finite count of matching primes.

No actual CM trace or quotient component factor is in these outputs. No seed class or seed endpoint was computed.
