# Recovered class-control input: bound the joint repair space

The Claude continuation and its prior Codex reconciliation contain a useful input that a norm-only scaling test omits: **a complete arithmetic source whose class group is nonzero, but whose joint global/local admitted space is zero.** This was already computed in mirror389 on October15. It is newly applied here, not newly discovered.

All nine control matrix files match the hashes in the earlier reconciliation. The Claude continuation contributed five additional rank-two controls, eight total; its original six/nine counts were corrected previously. The later mirror389 calculation is a distinct rank-zero control. Source class/unit completeness and local-image authentication retain their prior grades; no BNF or exact number-field producer was rerun.

Fresh independent calculation from the complete raw matrices gives:

| Cases | admitted units | admitted classes after all repairs | admitted valuation directions | complete upper bound |
|---|---:|---:|---:|---:|
| Eight rank-two controls | 1 | 1 | 0 | 2 |
| mirror389 | 0 | 0 | 0 | 0 |
| seed at3 (conditional source completeness) | 2 | 2 | 0 | 4 |

For mirror389 the previous ordinary norm/class/divisor upper bound was3. The global screen alone still leaves1 class and2 valuation directions; the local conditions remove those after global compatibility is imposed. Both marginal tests separately permit a unit repair of the class, but their unique repairs differ. This is an actual whole-source improvement3 to0 under retained arithmetic, not detection of only a supplied class. It is an old control result, not new prime coverage.

The corrected across-prime sufficient bound is based on the stacked map R=(global,local):

    dim screened source = (d-rank R_on_units)
                         +(class_rank-rank induced_class_defect)
                         + surviving_valuation_rank.

Here d=(p+1)/2 is the faithful-character ordinary unit dimension. The induced class defect is taken modulo every unit image, so only irreparable class directions are subtracted. A complete source presentation or an independent complete upper bound is essential. This changes the scaling question: the necessary rejection rank can come from the combined maps and compatible class repairs; it need not all come from the norm map alone.

`check_filtered_bound.py` and `FILTERED_BOUNDS.json` reconstruct the result without reading producer coupling ranks or Sha orders. All ordinary-unit and class fibers are included; the H0 enumeration checks all243 elements on each control and729 on the seed. The point comparison occurs after the upper bound is computed. See PROOF.md for the exact sequence, scope and source grades.

No higher-coefficient-prime joint rank or seed cofinite bound has been computed. FIN, ORDER9 and Q36 remain unchanged.
