# Primary sources and retained inputs

## Sources actually read

1. Otmar Venjakob, *On Kato's local epsilon-isomorphism conjecture for
   rank one Iwasawa modules*, arXiv:1204.4269v2.
   https://arxiv.org/pdf/1204.4269
   Appendix A, especially printed pp.26-30 and 32-36: the coefficient
   extension remark, (A.61), Proposition A.2(ii), (A.65), (A.67),
   (A.69), (A.72)-(A.74). The decisive pages 28, 30 and 35 were also
   visually inspected. This supplies the integral Coleman sequence and
   the finite-level dual-exponential formula; it supplies no uniform
   global Kato-index bound. In (A.72), pr_n is a projection, not p^rn.

2. Kazuya Kato, *p-adic Hodge theory and values of zeta functions of
   modular forms*, Asterisque 295 (2004), 117-290.
   https://www.numdam.org/article/AST_2004__295__117_0.pdf
   Printed p.242, section 14.13, was read in the original image to fix
   the period/reciprocity convention. The level hypothesis of 14.21
   was checked in text and is also bound in the retained review.
   The local Euler convention of 14.10 and the retained index proof
   are used. Section 14.21 is not applied to the ramified weight-three
   point. The local source PDF is the same hash as the retained one.

3. Tadashi Ochiai, *A generalization of the Coleman map for Hida
   deformations*.
   https://www.math.titech.ac.jp/top/~ochiai/coleman.pdf
   Theorem 3.13, Theorem 3.17, Corollary 4.13 and introductory
   conventions were read to check the suggested family comparison.
   Its integral hypotheses and pseudo-null cokernel were retained,
   not upgraded to a specialization isomorphism.

4. David Loeffler and Oscar Rivero, *Eisenstein degeneration of Euler
   systems*, author-hosted version.
   https://www.oscarrivero.org/_files/ugd/e8f31a_ccfac2809e094ddb85ef1d52d63b9f00.pdf
   Section A3.2 and B4.1-B4.4, especially Remark B4.2. The canonical
   rational family basis removes Ochiai's arbitrary rational-basis
   correction, but its integral lattice identification at the specific
   ramified point is not proved by those printed statements.

SOURCE_BINDINGS.json gives the exact PDF hashes and local cache paths.
The cache holds downloaded PDFs, extracted text and page images; whole
external papers are not duplicated in this return archive. The proof
here imports their indicated theorems, not their abstracts.

## Retained arithmetic

The seven context files are copied byte-for-byte and bound by
RETAINED_BINDINGS.json. The three original review manifests verify
53/53, 37/37 and 31/31. See checks/RETAINED_INTEGRITY.json.

The seed's rank, residual image, ordinary specialization, saturated
lattice, parity, normalized Kato class and reviewed inequality are
retained inputs. This turn does not independently re-certify them.
The p-local rational finite-subspace comparison and normalization
restrictions are in context/LOCAL_PREDECESSOR.md and
context/KATO_INDEX_DERIVATION.md. The earlier pairing review prevents
repeating the unsupported claim that the weight-three lane is ruled
out by a separate established height conjecture.

## Collision and verification scope

The available BSD_WEIGHT3 folders were searched for the explicit
ramified lattice and Venjakob comparison. The earlier index review
ends with an unspecified d_g; it does not contain (11) of the new
LOCAL_LATTICE.md. The integral saturation reduction and the basic
Taylor warning have predecessors and are labelled accordingly.
This is a project-collision check, not a literature-novelty survey.

checks/exact_controls.py verifies tame idempotents, Gauss orientation,
the two powers of p in the rank-one formula, Euler cancellation,
coefficient-ramification controls and formal analytic countercontrols.
It proves none of the imported cohomological theorems. No seed value
b_p, Selmer group, new witness or primary certificate was computed.
