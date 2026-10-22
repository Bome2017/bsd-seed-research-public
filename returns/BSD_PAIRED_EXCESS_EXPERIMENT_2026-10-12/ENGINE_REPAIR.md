# Exact batching of PARI quadratic twist moments

The official PARI2.17.3 mspadicmoments implementation allocates all quadratic-character action matrices and path logs before evaluation. At d329233,n7 this overflowed the fixed4GB stack. It returned GP process exit0 but no coefficient; that output is rejected.

The patch in checks/pari_chunk.patch changes three summation ranges from 1<=b<|D| to lo<=b<hi and initializes the partial moment vector to zero rather than treating b=1 as special. A disjoint partition of that interval is summed modulo the original p^(n+vden). Actions and final coefficient conversions are linear at that modulus. Common alpha and metadata are retained once. No coefficient, precision exponent, Euler factor or source normalization is changed.

A separate source-level desk audit found no arithmetic or GC defect for these p5 runs. The initial driver uses literal5; the final precision8 driver additionally verifies common metadata/alpha and reads the prime from the metadata. Unused array slots are never traversed by the loops or explicit copying.

Full moment vectors match the unmodified producer exactly for d13,29,-7 and the saved d43737 control at precision5. These are stronger checks than comparing printed quotients. They are not independent modular-symbol implementations: the patch reuses PARI's construction.

The precision7 d329233 run completed with512MB in179.9seconds. It gives L2=O(5^4) and corrected Q=O(5^2), not exact valuations. The next digit is computed separately at precision8, with partial-sum checkpoints every20batches and300second cap.

The GPL-2.0-or-later source is included unmodified with its license and bound by SHA256; the small derivative patch and reproducible build script are supplied. The generated C source and binary are retained locally under build/ but excluded from the publication archive. No system PARI installation was modified.
