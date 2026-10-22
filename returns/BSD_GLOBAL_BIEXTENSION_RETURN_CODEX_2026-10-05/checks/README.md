# Exact controls and scope

The controls cover the proposed construction, not new seed primary vanishing.

- `construction_check.py` (Python 3, SymPy 1.14): seven exact seed points, four rational denominator normalizers, the symbolic GL2 determinant identity and its primitive integral kernel, the torsor-scaling countercontrol, and finite group-ring extraction/idempotence controls. It writes `CONSTRUCTION_RESULTS.json`.
- `seed_points.gp` (PARI): independently computes the seven rational points. `PARI_POINTS.txt` and `POINTS_CROSSCHECK.json` record exact agreement with the separate rational group law. This does not verify the Neron model at bad primes.
- `retained_pairing_check.gp`: unchanged G2 normalization checker. `PAIRING_REPLAY.txt` reproduces all three cases. It uses exact rational points and divisor denominators with tame characters; no modular-symbol values are read by this checker.
- `retained_symbol_recombination.py`: recombines the 102 existing exact-identified symbols at p=17, ell=103 in the frozen convention. It checks their input hash against the receipt, unique labels, plus symmetry, and the three weighted coefficients. It does not rerun the original interval engine or coefficient corpus. `SYMBOL_RECOMBINATION.json` gives the result.

Run the Python programs from the return directory or any directory; their paths are relative to their own file. Run the two GP files with a suitable PARI executable; their output should match the saved text files. No production pipeline, new prime certificate, class group, external job, or model lane is launched by these programs.

The synthetic group-ring and symbolic identities are algebra controls. They are not seed modular-symbol samples. Conversely the p=17 recombination uses actual saved seed symbols but supplies no new cross-prime theorem. The two uses are kept separate in the outputs.
