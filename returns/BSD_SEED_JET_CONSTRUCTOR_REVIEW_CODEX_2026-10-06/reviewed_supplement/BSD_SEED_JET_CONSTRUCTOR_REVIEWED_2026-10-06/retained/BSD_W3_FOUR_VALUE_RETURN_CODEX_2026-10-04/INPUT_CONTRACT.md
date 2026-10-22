# Input contract for symbol_values.py

This script is the finite arithmetic last step after the actual source symbols have been supplied. It does not build a Hida form or certify a modular-symbol table.

The input is JSON with:

- `p`: the good ordinary coefficient prime in the retained cofinite domain; the program checks primality, p>=17, p<=1000000, the known bad primes and {19,59,487}, but cannot check divisibility by the uncomputed D or verify ordinarity.
- `N`: exactly 6503188012738584.
- `convention`: exactly `source_phi_X_minus_zY_path_a_over_p_to_infinity`.
- `fibers`: exactly two keys, `"3"` and `"4"`.

Each fiber has `modular_weight=w+2`, `tame_character_exponent=-w`, and `symbols`, an array with exactly one entry for every a=1,...,p-1. An entry is `{"a":a,"coefficients":[c0,c1,c2,c3]}`. Supply canonical nonnegative residues modulo p^4,p^3,p^2,p respectively. They are coefficients of the literal primitive source symbol on `{infinity}-{a/p}` in the polynomial convention in ARITHMETIC_EXTRACTION.md. They are not moments without their binomial/sign conversion, values of the seed's weight-two symbol, or numerical approximations to complex integrals.

`alpha_mod_p4` is optional in each fiber. If supplied, it must be the actual U_p unit root to that precision. If absent, the script returns unit-scaled source residues sufficient for a nonzero test but leaves the corresponding `values` entries null. In either case source authenticity remains unverified by the script.

Run `python3 symbol_values.py <input.json>`. The output binds its input by SHA256 and includes the four residues in the ordered nodes (3,2),(3,3),(4,3),(4,4). A nonzero result is only a conditional arithmetic certificate until the Hida/source/Hecke/lattice and domain evidence is independently checked. The output always says `seed_primary_certificate=false` for that reason.

To use the submitted four-value coefficient reconstruction, provide the actual alpha values and a verified common family frame. The unit-scaled residues must not be fed into that reconstruction as though they were the common F-values.

No sample array is labeled as seed data in this packet. The exact calibration on Delta and the random formula tests live under checks/ and have separate scope labels.
