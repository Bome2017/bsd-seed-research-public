# Fixed local Kummer calibration

Before execution: use the actual seed and q=1783, coefficient5. Construct the full5-torsion over F_(1783^4), choose the lexicographically first nonzero Frobenius-eigen3 torsion point, and evaluate its reduced Tate pairing on R=(3,872) and the two retained basis reductions. Require the R value nontrivial and both point values1. Independently implement the Miller function to check the Sage pairing. This constructs local coordinates only. It neither constructs a global relaxed dual class nor excludes a global Selmer signature by itself.
