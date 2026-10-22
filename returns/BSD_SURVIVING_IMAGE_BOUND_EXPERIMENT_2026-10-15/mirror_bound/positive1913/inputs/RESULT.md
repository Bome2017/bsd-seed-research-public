# 1913b1: actual positive unit-supported control

Status: COMPLETE_SOURCE_WITH_TWO_EXACT_GLOBAL_AND_LOCAL_CLASSES, subject to the specified p=3 descent theorem and independently checked algebraic rank bound. This is a rank-zero, full-mod-3-image, good-at-3 control. It is not a rank-two analogue or a new result about the original seed.

The curve is [1,1,0,-34,-135], conductor1913. Its point field is w^8+6w^4+43w^2-3. `bnfcertify` returned1 in58.4seconds, and the class group is trivial. A complete S-unit source for S={3,1913} has dimension9. Valuation-zero classes are precisely the four-dimensional global-unit space.

The full joint necessary kernel has dimension2, lies inside the global units, and contains no point direction because the independently run algebraic2-descent gives `ellrank(E,0)=[0,0,0,[]]`; rational torsion has order2. The analytic Sha label was used only for candidate selection. It enters none of the source construction, exact roots, local image or algebraic rank computations.

This is more than finite additivity acceptance. For both surviving unit directions, `affine_norm.gp` constructs the actual affine-line norm in the dual degree-eight field and finds literal cube roots. `norm_cube_check.gp` independently forms the 3x3 multiplication matrices and checks their determinants against those cube roots. All four unit/source-coordinate identities are themselves verified by exact cube roots. The source-field and short-Weierstrass embeddings, division-polynomial relation and coordinates are explicitly checked. Scalar compatibility is checked in the actual source matrix.

The local images have dimensions1 at3 and0 at1913. The zero-image place imposes all evaluation rows, not an empty condition. Fresh samples at45-digit precision reproduce the retained rowspaces. Two exact rational Hensel certificates authenticate the samples; minimum local cube-class precision margin is86. OutsideS and at infinity the standard p=3 descent local conditions apply.

Combining these exact global/local tests with Schaefer–Stoll Corollary7.9, Proposition7.10 and the complete source yields a two-dimensional3-Selmer group. The independently computed rank zero and rational torsion prime to3 then give Sha[3] isomorphic to F3^2. No order or finiteness of the entire3-primary group is claimed.

The structural data are therefore: admitted unit dimension2, admitted class dimension0, point-unit dimension0, and unit-supported excess dimension2. This tests the accepted-unit component directly: its two surviving directions need not be rational-point directions, even for good-at-3 full residual image and trivial class group. It supplies no estimate for the original seed outside its known coefficient prime. FIN, ORDER9 andQ36 are unchanged.

The first norm script used a GP variable below the dual-field variable; strict stderr rejected that run despite its later completion marker. The rejected artifacts are preserved in `failed_norm_variable_priority/`. The accepted script uses the correct variable, and both cube identities and multiplication-matrix replay pass. The independent matrix checker also needed the zero-class-column shape normalized; its original is retained. Neither failed attempt is accepted evidence.
