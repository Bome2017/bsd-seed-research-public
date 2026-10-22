# Primary-source version ledger

The sources below were read from the actual PDFs. Their constants are not silently assigned the value one.

1. Ellenberg–Venkatesh, *Reflection Principles and Bounds for Class Group Torsion*, author PDF, Lemma 3 (printed p6). The extension degree in the cutoff is [K:K0]. It admits individual unramified prime ideals of norm at most N(D_K/K0)^delta, delta<1/(2 ell(d-1)), not extended from an intermediate subfield. The conclusion is an implicit-constant bound for the ABSOLUTE Cl(K)[ell]. For A/K quadratic and ell=5, the supremal norm cutoff is delta_relative^(1/10), between242 and243. The arithmetic lane found52 eligible A-primes arranged in26 tau-pairs. A pair count26 is conservative if used in the original individual-prime lemma; it is not the same counting convention.

   URL: https://people.math.wisc.edu/~ellenberg/Scholz-submit-july17.pdf

2. Lemke Oliver–Wang–Wood, author-hosted version, *The average size of 3-torsion in class groups of 2-extensions*, Lemma2.1. Its statement explicitly sets [L:K]=d and requires theta<1/(4 ell(d-1)). It uses PAIRS over the same K-prime and bounds RELATIVE class torsion with a degree-dependent implicit constant. For A/K and ell=5, the supremal cutoff is delta_relative^(1/20), between15 and16. Exactly two tau-pairs, both of norm7 over distinct K-primes, are eligible.

   URL: https://wangjiuya.github.io/research/3tor2ext.pdf

   The returned bytes are bound in sources/BINDINGS.json. The label LOW_2021 identifies the author/preprint branch discussed in the record, not a freshly verified server publication date.

3. The published Forum of Mathematics, Pi version (2025), DOI10.1017/S2050508625000009, Lemma2.1, printed p7, instead prints d:=[L:Q]. Its proof later resets d=[L:K], and Lemma2.4 also uses relative degree. At the literal absolute-degree cutoff there are no eligible seed prime pairs. That stricter reading is valid as a source-scoped statement but is NOT grounds to reject the author version's relative-degree mechanism. The arithmetic ledger preserves both versions. We do not silently repair the published statement and then quote it as printed.

   DOI: https://doi.org/10.1017/S2050508625000009

4. Both relative-source arguments carry implicit degree-dependent constants and a sufficiently-large-discriminant threshold. Neither provides a numerical bound of 97/2, 97/26, or h_relative/26 on this seed. Prime counts are not ranks of known class images. In particular a set of distinct prime ideals can lie in one ordinary class after multiplication by ell; units intervene through the Arakelov torus.

The explicit norm-one ideal-group construction in EXPLICIT_PRIMARY_PACKING.md is a separate written deduction inspired by these methods. It keeps the norm-unit defect, fractional denominators, archimedean volume, and all constants explicit. It does not rely on resolving the source-version discrepancy or treating principal generators with norm a unit as though their element norm were one.

The October21 Pro packet's lower bound B_old>1000^d was read and retained only for its specified bound expression. SCALING_LIMIT.md extends its calculation to this explicitly defined packing budget; no arithmetic lower bound on actual class groups is asserted.
