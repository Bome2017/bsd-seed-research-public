# Reproduction and evidence grades

The aggregate replay runs in a temporary copy, without modifying the sealed result files:

```sh
python3 checks/replay.py --sage-python /path/to/sage/environment/bin/python
```

The completed run is recorded in `checks/REPLAY_RESULT.json`: all 11 selected result JSON files reproduced byte-for-byte. Each subprocess has a 120-second limit. This runs the small quartic class/unit calculation; it does not run a degree-24 seed class group or a production modular-symbol computation.

## Checks that were executed

- `explicit/admission.py`: proof-enabled quartic class/unit and Kummer spaces, exact torsion and automorphism, rational point descent evaluations, corrected auxiliary scan, ideal-class boundary. PARI `bnfcertify=1` is recorded. This is the producer's certified number-field computation, not independent software verification of that computation.
- `explicit/verify_local.py`: separate standard-library elliptic arithmetic, Miller evaluation, point count, all 11 corrected scan rows, and exhaustive finite-field matrix/image checks.
- `duality/audit_quartic.py`: separate Sage implementation of the field automorphism, torsion character, prime decomposition/permutation, class-row consequences and local interface. It does not recompute the class/unit-group basis independently.
- `local_pairing/check.py`: full seed 5-torsion over the degree-four residue extension, Frobenius eigendirections, Sage and separately implemented Miller pairing values, and 16 bilinearity checks.
- `duality/local_row.py`: local tame cocycle model, 30,000 cocycle identities and the pairing coordinates. This authenticates local algebra, not a global class.
- `local_pairing/line_source.py`: the affine-line polynomial and all 24 torsion-point valuation profiles, including the failed old profile. The simple-valuation premise is authenticated separately by the exact norm in `seed/line_source_probe.json`.
- `seed/principal_probe.py`, `leak_repair.py`, `line_source_probe.py`: exact source resultants and small-prime support checks. The remaining large cofactors are not fully factored.
- `seed/verify_principal.py`, `verify_line_source.py`: independent division-polynomial recurrences, 15-by-15 and 27-by-27 integer Bareiss resultants, entire rational norm comparisons and local residues, using Python's standard library.

The raw producer output, the initial incorrect scan, the corrected scan, and the audit are all retained. The historical scan's q-not-1-mod-5 rows are not evidence for fifth-power membership. The correction was made after the first trial; no claim of a prospectively sealed corrected prediction is made.

## Inputs and limitations

The control curves, rational isogeny, named points and local Tamagawa data are retained from the previous matched control. The new isogeny-kernel upper bound does not require a known Sha value, an L-value or a rank upper bound. The seed's full residual image and saturated global point basis remain retained project inputs. The direct source exclusions themselves use explicit local/norm arithmetic.

Miller–Stoll Theorem 11 and Schaefer–Stoll's full-descent embedding supply the mathematical source interfaces. Source URLs, reading scope and hashes appear in `SOURCE_BINDINGS.json`, `duality/SOURCES.md` and the proofs. Full downloaded source papers are excluded from the published package.

No whole-seed Selmer group, seed class group, coefficient–height bound, Kato coefficient, uniform theorem or BSD endpoint was computed. No Lean formalization was attempted. Repeated execution and file integrity are distinct from mathematical proof and source validity.
