# Independent printed-interval verifier

`../independent_verifier.py` is a separate implementation. It does not call or import the frozen acceptance checker, producer code, saved candidate rationals, printed `contains`/`unique` flags, or any regulator prediction.

It parses the plus-ball decimal midpoint and radius as exact Python `Fraction` values. For the closed interval `[lo,hi]`, it calculates `ceil(1024*lo)` and `floor(1024*hi)` and accepts identification only when they are equal. It then requires every label1,...,ell−1 exactly once, plus symmetry, exact c0=0 and c1=0modp. Coefficients are independently recomputed from the discrete logarithms. The entire calculation repeats with primitive root g^3 and checks c2 scales by3^(-2).

For83/167 use:

```
python3 independent_verifier.py PATH_TO_MSL.txt --p 83 --ell 167 --generator 5 --out independent_p83.json
```

The alternate generator is125. Both generators are checked by complete enumeration of their multiplicative cycles. Every recovered lattice numerator is retained in the output, together with a hash, source-output hash and verifier hash.

Historical calibration at43/173 recovers `c=(0,-13072,-227412)` and c2mod43=15 from the printed balls alone. With g^3=8 the residue is16, matching15*3^(-2)mod43. The saved prior report was used only to compare this historical output, not as an input to verification.

Eighteen controls pass. They include false printed candidates/flags (correctly ignored), missing/duplicate labels, empty/multiple lattice intersections, nonfinite or negative-radius fields, broken symmetry, nonzero c0, nonzero c1 with c0 preserved, invalid generators, and a synthetic zero83 table accepted only as inconclusive.

**Scope:** this checks arithmetic of the displayed intervals. It does not independently establish that the intervals enclose the true modular symbols, authenticate the coefficient corpus or tail estimate, or recheck the imported theorem assumptions. Those remain the producer, custody, frozen acceptance and theorem-profile obligations. Both a valid zero and a valid nonzero return process status0: the `mathematical_witness` field distinguishes them. Parse/arithmetic errors return2. It must not replace the frozen acceptance tool.

No actual83 table existed when this checker and its controls were written.
