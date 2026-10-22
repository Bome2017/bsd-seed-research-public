# Replay and limits

Run `python3 verify.py` for read-only hashes, nested manifests and saved-outcome consistency. The script does not launch a source search, BNF, new factorization or norm/local evaluation. Review arithmetic and its replay instructions are in `review/PROOF_REVIEW.md`.

The six files under inputs/ are bound to sealed lab commit79fe49d73acf7f134c3d4344481095b2f1a8184f. The previously complete producer factorizations are retained inputs: the current gate transports their prime ideals under the exact scalar automorphism, reconstructs the divisor matrices and computes ranks. It does not freshly certify the original maximal order, rank, residual image, or factorization engine.

`arithmetic/GATE_CORE.json` contains the closed prime HNFs, scalar permutation, unprojected columns, all translated columns and the three projected matrices. Its exact layout is documented by CORE_SCHEMA.json. The larger GP representation is also retained. The only producer stderr warning is automatic stack growth; its completion marker and resource receipt establish that the gate finished.

The separate review checks the actual generator, prime action, character convention, rank, and finite-family consequence. It does not turn a divisor rank into r_U for the whole ordinary-unit group. No source reached the existing norm/local evaluator.

A full-rank gate was an explicit stop condition. No larger family or successor calculation remains running. FIN, ORDER9, Q36 and all seed-prime coverage are unchanged.
