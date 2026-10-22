# Independent 66b1 reconstruction and receipts

## Separation of stages

PRE_COMPARISON_RECONSTRUCTION.md is the unchanged Stage-I mathematical record.
STAGE_I_FREEZE.json records its digest and the limited withheld-README exposure.
STAGE_II_OPEN.json records subsequent reads of the withheld arithmetic files and capsule.
STAGE_II_LOCAL_DESCENT.md is an explicitly later derivation, not a revision of the
blind prediction. It gives the local upper bounds and the independently specified
full-real-period BSD(2) comparison. No BSTW-dependent full-strong-BSD claim is made.

## Reproduce exact point counts

Requires a C++17 compiler and Python 3. The supplementary numerical period check
also requires mpmath; it is NOT an exact modular-symbol certificate.

```sh
g++ -O3 -std=c++17 independent_counts.cpp -o independent_counts
./independent_counts 100000 > independent_counts.csv
python summarize_counts.py
python independent_literal_and_period.py
```

The C++ program uses an exact Eratosthenes sieve and direct square-root counts
of two independently derived cubic polynomials, evaluated by finite differences.
The smaller Python test enumerates literal pairs on both curve equations and
checks coordinate maps, tangent-law duplication, and halving.

Expected: 9,589 good odd primes below 100,000; 600 proposed-family primes;
38 proposed-family primes below 4,000; zero exception lists. The literal check
uses 92 good primes below 500, with 21,504 affine points per model.

The input packet's counts_66b1.py is copied under PK66/03_arithmetic_receipts;
supplied_rerun.txt matches its supplied output byte for byte. No part of that
script was imported into the independent implementations.

The period cross-check uses 100-digit arithmetic and 700 Fourier coefficients.
Its decimal coincidences do not prove the exact rational L-value ratio. Exact
base data and analytic theorems are separately identified in SOURCE_LEDGER.md.
