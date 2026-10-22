# Review of the returned Macias Castillo–Sano check

2026-09-21. **NO GLOBAL ARROW ESTABLISHED; REPORTED STRUCTURAL NO-GO REJECTED.**

The [returned report](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/MCS_APPLICATION_VERDICT.md) does not establish an applicable global BSD theorem. Its stopping decision can stand. Several reasons it gives cannot: they would incorrectly exclude mathematics that the paper actually supplies. The original report remains unmodified evidence. Its author subsequently filed the [retraction](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/RETRACTION_AND_CORRECTED_VERDICT.md) and updated STATE/RESUME to make that retraction govern. The old mathematical fields retained in the external STATE are historical and must be read subject to its explicit retractions.

## Source corrections

Primary source: [Macias Castillo–Sano, arXiv:2603.23978v1](https://arxiv.org/html/2603.23978v1), §3.2.

| Returned claim | Source correction |
|---|---|
| No Greenberg/Kummer comparison supplied | Proposition 3.7 identifies the classical Selmer groups under its non-anomalous hypothesis. |
| Core-vertex hypothesis is simply left unproved | Lemma 3.8 establishes it, including core rank zero, under Hypothesis 3.6. |
| Torsion of the base Heegner point annihilates the construction | Theorem 3.9 uses the tower \(y_\infty\); Definition 3.10 specializes its determinant basis. Remark 3.11 says the resulting Stark system is a basis. |
| Claimed decisive rank-two exclusion | The omitted literal obstruction is Hypothesis 3.6(iii): squarefree conductor. |

These corrections do **not** assert that Hypothesis 3.6 holds for this seed. In fact the retained conductor

\[
N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843
\]

fails its squarefree requirement. Theorem 1.7/3.12 is therefore not directly importable as stated. This is an applicability failure, not a proof that an extension is impossible. No extension is attempted here.

## Exact failure of the torsion argument

Even granting the report's Gross–Zagier calculation for the base point, its next implication is invalid:

\[
y_K\text{ torsion}\quad\not\Longrightarrow\quad y_\infty=0.
\]

Vanishing under one specialization does not imply vanishing in a family. For example, in \(\Lambda=\mathbf Z_p[[T]]\), the element \(T\) is nonzero and has zero augmentation. Likewise the fraction-field isomorphism sending a basis \(e\) of \(\Lambda e\) to \(T^2\) is not an isomorphism of the integral lattices: after specialization its image is zero, while \(e\bmod T\) remains a basis. These are elementary algebraic counterexamples to the inference, not a computation of this curve's tower or a new BSD result.

The returned conclusion that every anticyclotomic Heegner construction inherits a fatal rank-two obstruction must not be added to the no-resurrection register. The report's stated reading grade—introductory statements, without the application proof—does not support that conclusion.

## What remains unknown

An abstract determinant-module isomorphism does not evaluate its relevant arithmetic coordinates. No seed-specific coordinate estimate, all-prime bound, or real regulator comparison has been obtained here. Nor has an identification of the paper's coordinates with the particular WC witness been proved merely by calling both of them coordinates. The retained WC equivalence stays unchanged.

An auxiliary quadratic field is not by itself a fatal obstruction either. For odd \(p\), restriction on primary Sha is injective: local triviality is preserved, and corestriction after restriction is multiplication by 2, an automorphism on a \(p\)-primary group. This observation supplies no bound on Sha over the auxiliary field and no seed application of the paper.

## Threshold and custody

The arithmetic threshold correction is valid: **under finiteness**, the retained small-primary results give order 9, or order at least \(9\cdot13^2=1521\). The bound \(<1089\) remains sufficient but is no longer the sharp threshold implied by those inputs. A historical sealed packet remains historical; it should not be presented as the current state without this qualification. The claimed count of stale occurrences was not independently checked here. Current references should identify master §3 and its bound inputs, not rely solely on a movable line number.

This review read the relevant statements and local proofs in §§2–3, including the precise application hypotheses and determinant specialization. It did not independently reprove the cited Heegner main conjecture, replay the arithmetic certificates, or establish applicability after changing a hypothesis. FIN, ORDER9 and Q36 remain open. No successor research operation is authorized or launched by this correction.

## Author retraction integrated

The later September 21 retraction accepts the three source corrections and withdraws the unsupported identification with the WC coordinate. Its original verdict hash remains 53f4e349f9432d0689276dd2feacd1a4cc7cd181417a2f8cdb16f859e07e26b1. The supplied PDF text, §3.2, was checked against the specific corrected statements.

The phrase “one reason now” is retained only as a reference to a sufficient, verified obstruction to importing this theorem literally. It is not a count of the mathematical tasks remaining for full BSD. Removing squarefreeness would still require checking all other hypotheses and extracting an independently useful arithmetic bound; the good-ordinary scope does not cover every prime regime, and no real leading-term comparison has been supplied. This integration neither assesses a nonsquarefree extension nor verifies the claimed parallel with Dickson–Neururer and Berger–Betina. Repeated hypothesis failures do not, by themselves, establish a common repair.

**Subsequent bounded source composition:** [MCS_NONSQUAREFREE_JOIN.md](MCS_NONSQUAREFREE_JOIN.md) now supplies the application at base layer, for every primary depth, in its explicitly restricted ordinary, non-anomalous regime. It uses BCK's already nonsquarefree main-conjecture theorem and the retained seed local inputs. The printed MCS hypothesis still prevents a literal citation, but the proof can be assembled without it at that scope. No numerical Sha bound or real comparison follows from this composition alone.
