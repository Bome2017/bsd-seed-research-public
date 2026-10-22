# Run the dual mixed-row diagnostic

```
python3 theory/dual_overlap.py PATH/TO/matrices.json \
  --output theory/calibration/NAME.json
```

For freshly generated global blocks:

```
python3 theory/dual_overlap.py PATH/TO/matrices.json \
  --extra PATH/TO/fresh_blocks.json --output theory/fresh/NAME.json
```

The extra file has format

```
{"source_sha256":"SHA256_OF_INPUT_MATRICES_JSON", "blocks":[{"label":"ell_...", "rows":[[...], [...]]}]}
```

Rows must be in the same source-generator order as the authenticated input.
The arithmetic labels, field/source binding, generation rule and fresh
producer receipt belong alongside that file. This module does not produce
or authenticate a number-field source.

The program uses scalar conditions plus each auxiliary block, and each
local-prime block separately as well as the complete local block. Existing
additivity rows are partitioned into32-row blocks as in the actual p=3
torsion construction. Original row indices and coefficients are exported
for every dual mixed certificate. A dual certificate has sign
`global minus local`, so its value is minus the associated functional on
the repair difference `u_G-u_L`; zero/nonzero and rank are unaffected.

The original seed schema is supported directly. Its first two actual
columns are P1,P2, while *all four* actual columns are protected against
rejection. That distinction is essential. The saved source-completeness
grade is copied rather than replaced by a computed-rank assertion.

The original1525c1 file contains three point columns of rank two. The
program takes an independent column basis for the point span while checking
annihilation of all supplied point columns. An initial development run
failed its dimension assertion before this distinction was added; no
incorrect profile was accepted or exported.

`CALIBRATION_SUMMARY.csv` is the retrospective all-local comparison.
JSON outputs retain all per-local-block profiles and actual certificate
coefficients. The calibration arithmetic is not a fresh number-field
experiment and is not another proof of the whole seed.
