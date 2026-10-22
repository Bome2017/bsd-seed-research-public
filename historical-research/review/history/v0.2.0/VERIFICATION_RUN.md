# Verification run

Run at 2026-09-23 12:04:25 PDT with `python3 tools/verify_release.py --record`.

| check | result | detail |
|---|---|---|
| evidence hashes (3365 files) | PASS |  |
| claim evidence bound to provenance (207 items, 76 claims) | PASS |  |
| generated consistency: build_index.py | PASS | 76 claims OK; kinds {'FACT': 2, 'THEOREM': 24, 'EQUIVALENCE': 3, 'CONDITIONAL': 12, 'OPEN': 5, 'OBSTRUCTION': 17, 'HISTORICAL': 5, 'WITHDRAWN': 8}; evidence items 207 |
| generated consistency: build_brief.py | PASS | brief written: 76 propositions |
| manuscript claim IDs resolve (not a semantic proof check) | PASS | [] |
| review replay bindings | PASS |  |
| replay curve_invariants.py | PASS | 0.2 s |
| replay coefficients_from_symbols.py | PASS | 0.0 s |
| replay coefficient_verifier_regression.py | PASS | 0.0 s |
| replay lattice_local_checks.py | PASS | 0.0 s |
| replay archive_privacy_regression.py | PASS | 0.0 s |
| replay receipt_join.py | PASS | 0.1 s |
| lattice-local failure control is rejected | PASS |  |
| paper-review exact arithmetic consistency replay | PASS | 0.2 s; no large numerical certificate replay |
| replay 2243-adic height certificate (certify_d5.py) | PASS | det/p^2 = 2181 mod 2243, valuation 2; 0.0 s |
| replay 2243-adic height verifier (verify_d5.py) | PASS | verdict ALL_CHECKS_PASS; 0.1 s |
| replay F_2243 relation rank (compression obstruction) | PASS | 1.0 s |
| replay W_Q pairing on certified m = 27, 81 tables | PASS |  |

18/18 checks passed.
