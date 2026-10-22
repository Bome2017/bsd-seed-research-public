# Fresh Lean replay boundary

Lean 4.28.0 and the submitted lake-manifest.json pins were used. Four original source files were copied into a fresh replay tree and compiled in order: Curve, AuxPoint, Local4547, BadPrimes. The matching prebuilt dependency libraries were taken from the paths bound in checks/LEAN_DEPENDENCIES.json; Mathlib was not rebuilt. No returned olean files were used.

To repeat in a configured checkout of original_return/, with pinned dependencies available, compile those four modules and place Audit.lean at that checkout root. Run `lake env lean -s 65536 Audit.lean`. The separate audit proves the numeric projective residue assertion and prints axiom dependencies of all 26 original theorems plus that new assertion. The stored FRESH_AXIOM_AUDIT.txt is from the successful run.

Earlier audit attempts hit a recursion limit and a thread-stack limit. Their logs are retained as failures, not accepted proofs; a generated sorryAx in the first failed elaboration was never accepted. Increasing the permitted recursion depth and using a 64 MiB thread stack produced exit 0 and the final axiom lists with no sorryAx. The original four modules required no source modification.

The new residue assertion is an exact congruence on the submitted projective algorithm. Together with its unit-Z certificate it yields normalized residue 1274. The identification of that algorithm with the elliptic-curve group law is still a written argument, not formalized here.
