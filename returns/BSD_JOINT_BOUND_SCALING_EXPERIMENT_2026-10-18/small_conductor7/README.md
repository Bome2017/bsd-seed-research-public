# Changed coefficient-seven arithmetic source

Curve: 11a1, [0,-1,1,-10,-20]. This rank-zero control was selected after the registered rank-two 389a1 divisor families proved trivial. CONTRACT.md precedes the changed-source calculation. No rank or Sha answer is passed into the source or row constructors.

The point field has degree 48. `field.gp` binds its reduced polynomial, universal torsion point and scalar 3 map; `nf.gp` binds the maximal order. `check_field.gp.out` contains INDEPENDENT_FIELD_POINT_SCALAR_CHECK_PASS and its separate receipt records successful completion. `eval_data.json` carries the actual compact factors and integer exponents used by the root replay.

`bnf.bin` and `class_init.gp` contain a provisional class-one calculation. Its unit candidates were subsequently authenticated exactly in the sibling small_conductor_review directory; fundamental-unit and class completeness are not asserted. The separate quotient-only certification did not succeed. Do not infer class one from this binary or its initialization output.
