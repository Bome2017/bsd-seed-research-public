# Claude sources versus the growing unit-norm rank

Date: 2026-10-18. Scope: the four named Claude returns, their relevant producers, the preceding reconciliation, and the older norm-relations result. This is a targeted source reconciliation, not an exhaustive literature or host audit. No number-field computation or source rank was added in this pass.

## Finding

I found no omitted actual unit, integral unit-index theorem, or incidence-norm image matrix in these sources that improves the current bound as p grows. This is a statement about the inspected material, not a claim that these methods cannot supply such arithmetic. The four returns were already incorporated into the October 15 reconciliation. Their proposed sources remain mathematically different from the units needed to lower the present containing-space bound.

The distinction can be made at the level of the actual operations, rather than by rejecting the subjects wholesale.

| Inspected construction | What its producer actually calculates | Consequence for the present unit-rank problem |
|---|---|---|
| Invention panel L1, `e1_norm.gp` | Norm to Q of a cyclotomic evaluation of a tame modular-symbol element | This is not the incidence map between the torsion point and companion fields. Its scalar norm does not provide a nonzero image of an ordinary character-unit under that map. |
| Invention panel L3, `iso3.gp` and saved outputs | BNF class-group eigenspaces in the coefficient-3 Borel fixed field, under the stated completeness assumptions | These are class terms, not a unit norm matrix. The seed producer ends with exit 124 after stack growth; it supplies no seed class bound. Converting the conditional genus estimate into the current class contribution requires the actual maps; the symbols cannot simply be renamed. |
| Invention panel L4 | Eligible Kolyvagin auxiliary-prime coverage | The producer explicitly does not compute a derived Heegner point or an indivisibility index. More eligible primes therefore add no authenticated norm-rank witness. |
| Mock plectic `gross_side_v2.py` | A Brandt eigenvector and a discrete-log-weighted Gross-point sum, with arbitrary eigenline scale | The principal generators used in its quadratic fields are not units in the seed's torsion point field. No map to those units, much less an independent incidence-norm image, is constructed. |
| Mock plectic `global_side.py` | Rational points, local logarithms and a determinant | This tests the shape of known point directions. It is not a presentation of the full character-unit lattice. |
| Rank-two Kolyvagin bound attempt | A report proposing a uniform bottom-class index | The folder contains only the report. No bottom class, bounded index, unit, or comparison map was constructed. Its assertion about exact index requires the primitivity qualifications already recorded by the previous review. |

The `NEXT_PATHS` return explicitly records the earlier unit-norm Smith calculation and the uncontrolled number of p-factors. It is not a missing solution to that count. The previous plectic review also corrects the arbitrary-unit and Euler-system primitivity qualifications; these should be retained rather than repeated as new findings.

## An operation-level separation

Let A and B be the actual torsion point and companion algebras, let

\[
u:A^\times/A^{\times p}\longrightarrow B^\times/B^{\times p}
\]

be the retained affine incidence norm, and let \(w_1\) be the cohomological source map. The source identification retained from Schaefer--Stoll, Corollary 7.9 and Proposition 7.10, gives

\[
u\circ w_1=0.
\]

Consequently, **if** a CM, Kolyvagin or Kato construction has actually been matched to a class in \(H^1(\mathbf Q,E[p])\), its natural image cannot serve as a nonzero incidence-norm image witness. Sums and natural restriction/corestriction operations, when they produce another such matched global class, do not change this conclusion. This is immediate from the source theorem, not a new arithmetic vanishing theorem.

This identifies two different jobs. An explicit ordinary unit with nonzero incidence norm can increase the independently certified image rank and thereby bound the entire kernel. An Euler system can instead control that kernel through its arithmetic index and duality theorems. The second job remains possible, but the inspected reports supply neither a suitable primitive source nor a uniform index estimate. The implication above does not apply to an unmatched proxy merely because it is called a CM or Kato object, and it does not rule out extracting useful pre-admission units from its geometry.

For reference, the current bound remains

\[
\dim K_\chi\le (p+1)/2-r+t_D+k_C.
\]

Here r is a lower bound on the rank of the **actual** norm on ordinary character-units; \(t_D\) is the primitive divisor-kernel term; \(k_C\) is the actual ordinary class-map kernel. A whole-source upper bound of three therefore needs

\[
r\ge (p-5)/2+t_D+k_C.
\]

The preceding operation lemma explains why inserting already-admitted cohomology classes does not supply this growing r. It leaves the separate class-supported contribution fully present.

## Older norm relations: the precise reusable safeguard

I inspected `C1_ULTRA_PARALLEL_NORM_RELATIONS_001/RESULT.md` and `PROOF.md` Sections 0 and 10. Its p=5 faithful-character calculation excludes a particular strategy: obtaining the desired projector from norm/transfer/conjugation compositions through subfields of degree below 24 inside the fixed torsion Galois closure. The report also has positive controls and an upstairs construction.

This is relevant when proposing to recycle units from smaller subfields: their ability to generate the required faithful source must be proved, not presumed from a rational character identity. It is not a bound on the actual unit group, a statement for every p, or an exclusion of auxiliary fields, other arithmetic operations, Euler systems, or upper-bound inequalities. It was already a scoped negative result, and is not a newly discovered uniform obstruction.

## Disposition

No new small experiment was admitted: none of the recovered producers supplies an actual candidate that changes the present source bound. Re-running their norms, Gross proxies, eligible-prime scans or BNF jobs would repeat computations without testing the missing growing image rank.

The usable conclusion is the exact source separation above. A continuation claiming to use these Claude constructions must supply either (i) actual ordinary character-units with independent nonzero incidence norms, before imposing the global cohomology condition, or (ii) an independently controlled Euler-system index acting on the kernel. The inspected records supply neither yet. This does not claim those are the only possible arithmetic mechanisms.

**Status:** `CLAUDE_SOURCES_RECONCILED_NO_NEW_UNIT_RANK_INPUT`. Existing p=5 arithmetic and the conditional coefficient-3 class-control results are unchanged. No new seed-prime result, FIN, ORDER9 or Q36 conclusion follows. Source hashes and reading scope are recorded in `SOURCE_BINDINGS.json`; source papers were not freshly re-audited in this pass.
