# Reproduction

Use a fresh copy of this directory. Python 3 with SymPy, a C compiler, and GMP development headers/libraries are required. The executed environment used Python 3.13, SymPy 1.14.0 and GMP 6.3.0. No network, PARI or private external data is needed after the retained field polynomial is supplied.

Compile:

    cc -O2 -Wall -Wextra scripts/batch_gcd.c -lgmp -o scripts/batch_gcd
    cc -O2 -Wall -Wextra scripts/verify_private_direct.c -lgmp -o scripts/verify_private_direct

Run:

    python scripts/cayley_test.py
    python scripts/check_cayley_independent.py
    python scripts/private_support.py
    python scripts/combined_support.py
    scripts/verify_private_direct results/combined_norms.txt results/combined_certificate.txt
    python scripts/check_linear_mod5.py
    python scripts/analytic_ceiling_obstruction.py

The full saved package includes raw exact traces, raw norms, private cofactors, the twelve factor identities, independent checks and the plan sealed before the arithmetic. Elapsed-time fields can differ on replay; do not demand byte identity for time-bearing summary files. No compiled binaries are shipped. The source-field identification and local elliptic inertia remain retained mathematical inputs.

The linear mod-five checker applies SymPy integer_nthroot(P_i,5) to every private_norm_part of the rational entries in combined_support_rows.json; each exactness flag is false. This is not the same as a quadratic character-rank certificate, which is not asserted.

A compact GitHub publication may omit the multi-megabyte raw rows while supplying the proofs and compact rerun sources. The full archive supplied in the conversation includes those rows and has its own manifest. Publication scope must not be confused with arithmetic verification scope.
