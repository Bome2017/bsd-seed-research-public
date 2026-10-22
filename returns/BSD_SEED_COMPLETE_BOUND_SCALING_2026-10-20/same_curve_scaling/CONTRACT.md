# Fixed-curve coefficient-prime scaling test

Curve: 1664n1, y^2=x^3-4x+16, previously tested at coefficient prime 3. This run fixes the same curve and tests prime 5. No additional curve search is permitted.

Success criterion: bound the full faithful-character source by including ordinary units, ordinary class contribution, and admissible valuations at S={2,5,13}. Unit norm rank alone is not a complete bound. BNF outputs remain provisional until certified; authenticated actual units plus the independent character-unit dimension may bound the full unit kernel without asserting their fundamentalness. If class certification cannot complete, record that unresolved term explicitly.

Pipeline: construct the degree-24 nonzero-five-torsion point field with exact torsion and scalar-action checks; attempt bounded BNF and class quotient certification; authenticate candidate units; use exact split finite-field incidence norms to certify a rank lower bound; calculate primitive-divisor allowance at S. Initial caps: each major GP stage <=120 seconds, <=2 GiB configured stack. Rejected runs and stderr are retained. No returned pass marker overrides errors. No known Sha/Selmer rank enters the arithmetic upper bound.

This tests scaling from 3 to 5 on one source. It does not prove an across-prime theorem or concern the original BSD seed.
