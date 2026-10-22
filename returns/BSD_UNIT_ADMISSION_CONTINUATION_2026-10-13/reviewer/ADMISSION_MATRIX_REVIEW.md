# Independent replay of admission matrices

`check_admission_matrices.py` reads the actual `data/MATRICES.json`, binds its
SHA-256, and computes all ranks over F3 independently. It does not use the
producer's dimension report as input.

The local annihilator for each prime was reconstructed from the supplied
local image matrix. When the Kummer image is zero the annihilator is the
entire dual local target, so all source-evaluation rows must be imposed.
This independently validates the repair at 2, 2243 and 4547. Repeating the
old skip gives kernel dimension 7; the corrected local constraints give 4.
The reconstructed row spaces agree exactly with the producer's repaired
blocks. This is an audit of the finite matrices, not a regeneration of the
underlying local logarithms/residue arithmetic.

The four reconstructed actual classes are independent and lie in every
displayed constraint kernel. The 15-dimensional cached source has:

| Conditions | Kernel dimension |
| --- | ---: |
| All valuations divisible by 3 | 6 |
| Exact tau anti-invariance | 4 |
| Sampled split-prime additivity | 5 |
| Corrected local Kummer conditions | 4 |
| All of these | 4 |

The exact norm kernel and corrected local kernel are equal and spanned by
the four actual classes. On the four-dimensional unit source the norm,
sampled additivity, and local conditions each select the same plane, spanned
by the two known unit classes. Two class-source lifts can be repaired by
the displayed unit vectors; the repaired vectors satisfy all three maps.
The independent quotient-coupling rank is zero, including local conditions.

These facts do not make a finite split-prime sample sufficient in general.
For the known two-dimensional unit plane, all-place membership is supplied
instead by the actual point and cubic classes. The exact signature argument
in `REPRESENTATION_SCREEN.md` proves this plane is the entire genuine
norm-one unit space without a class-group-completeness assumption.

The cached 15-generator source's completeness retains its prior grade.
Nothing in this replay certifies that no omitted field class exists outside
that source, or supplies a new prime or uniform upper bound.

Output: `ADMISSION_MATRIX_CHECK.json`.
