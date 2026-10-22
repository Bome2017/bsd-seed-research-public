# An arithmetic upper bound that retains units and ideal classes

2026-10-15. **INDEPENDENT CONTROL UPPER BOUNDS COMPUTED; NO NEW SEED BOUND.**

This run changed the object of the experiment from detecting named classes to bounding the entire containing global source. It derived and evaluated a companion-field class-group bound at coefficient3. It also tested, and refuted with actual excess classes, a shortcut that would have discarded the image of the reverse norm.

The work is a written deduction under retained source and number-field inputs, with exact arithmetic replays and a separate same-team mathematical review. It is not a novelty claim, formal verification, or independent recertification of all earlier descent inputs.

## The upper bound

Let A be the nonzero3-torsion point field, B its affine-line companion field, and S the common rational ramification set, using all primes above it. The residual representation is required to have full GL2(F3) image. Let K_A be the scalar-compatible global incidence-norm kernel containing the actual Selmer group.

Let t_D be the integral incidence-norm index on **primitive anti-invariant divisor lattices** above S. Let c_AS and c_BS be the Z3-lengths of the minus S-class groups, and r_AS the3-rank of the source S-class group. The proved inequality is

    dim_F3 K_A <= 1+t_D+c_BS-(c_AS-r_AS)
                 <= 1+t_D+v3(#Cl(B,S)).

The class-supported part is not discarded. The ordinary-unit index formula and the exact S-unit valuation sequence give

    S-unit norm-kernel dimension = 1+t_D+c_BS-c_AS.

Adding at most r_AS class-supported directions yields the bound above. Thus the source class contribution cancels against the denominator in the unit-index formula; its possible higher-exponent deficit improves the bound further. This uses the ordinary number-field class-number formula, not BSD, an L-value, or a known Sha order. The full proof is [independent_index/PROOF.md](independent_index/PROOF.md).

The arithmetic inputs are distinct from the Selmer admission matrix: prime-decomposition norms and a companion S-class group. The new producer neither uses local Kummer rows nor feeds in the known norm-kernel dimension or Sha answer.

The historical control outcomes were already available to the researchers. This is not a blinded experiment. Independence means the upper-bound calculation does not use those outcomes as arithmetic inputs; literal replays and the written inequalities, rather than blinding, support the conclusions.

## Executed tests

| Control | Independent arithmetic | Global-source upper bound | Comparison made afterward |
|---|---|---:|---|
|389a1|t_D=0; companion S-class3-length1|2|The two retained independent points exhaust it.|
|Its -3 mirror|t_D=2; companion S-class3-length0|3|All three possible global directions remain permitted; local restrictions are still required.|
|1913b1|Divisor matrix(-1); source class group trivial; ordinary antiunit rank2|2|The retained rank-zero curve has two genuine excess classes, filling the bound.|
|Seed, coefficient3|Primitive divisor matrix diag(1,3), hence t_D=1|2+c_BS, with companion minus S-class length still uncontrolled|This is an actual seed input, not a completed numerical upper bound.|

For389/mirror the forward primitive divisor matrix is diag(1,-1); the compatible reverse is diag(3,-3). Cached certified class groups are trivial and C3, and all primes in S have trivial class. The matrices were calculated from exact valuations of actual incidence norms on weak-approximation representatives of primitive prime differences. They were not inferred from the known surviving spaces.

For1913 the unit divisor index and trivial source class group force every norm-admitted class to have an ordinary-unit representative. The signature then gives the independent bound2. No companion class-group computation, Selmer row, point rank, or supplied excess class enters this upper-bound calculation. Those retained classes are used only afterward as a sharpness check.

These are bounds on entire sources, so they cover undiscovered classes within the authenticated source. They do not merely separate the already listed classes. They are coefficient3 control results, not new coverage of a seed prime.

The seed divisor calculation used its actual torsion-field geometry and exact valuations. It needed neither a new class-group computation nor the saved four Selmer columns. It determines the divisor term only. In particular, it does not justify deleting the companion S-class contribution or inferring it from the desired answer.

## The adaptive test that changed the plan

Actual paired norm maps on389 and its mirror have ranks2 and2, with zero composites modulo3. Their homology dimensions are0 and1. The mirror homology is class-supported, while its reverse-norm image has two valuation directions. Nine literal cube identities authenticate these maps.

This suggested a shortcut: perhaps the reverse-norm image consists of points, leaving only homology to bound excess. We tested that suggestion on the genuine positive control1913. A missing companion unit basis initially blocked direct extraction. We then used the already saved forward cube roots to construct reverse preimages, and verified them with the actual transpose incidence cubic.

The result is two exact identities

    v(beta_1)=alpha_1,   v(beta_2)=alpha_2,

where both alpha classes are the retained independent, genuine, unit-supported excess classes on the rank-zero curve. All four elements are checked to be global antiunits. No new BNF was needed.

Therefore the reverse-norm image can contain genuine excess. Counting homology alone would miss it. The companion-class/index bound retains that image and survives this test. See [mirror_bound/REPORT.md](mirror_bound/REPORT.md) and its positive1913 certificate.

## What this says about the seed

The completed experiment has produced an independently computable upper-bound input, not just a better detector. It shows concretely how unit and class-supported contributions can be bounded together. It also shows why removing norm boundaries would be mathematically wrong.

It has not supplied a small bound for the seed at unresolved coefficient primes. The displayed constant1 is proved here for the coefficient3 minus component. For larger primes the relevant scalar character and its inverse must be kept distinct; the full minus component is larger. No uniform estimate for the required companion class components or norm indices is proved here. The seed's retained3-primary excess, containing both unit and class-supported directions, must remain permitted by any proposed extension.

The next admissible extension is therefore precise: derive the bound in the actual scalar character for larger coefficient primes and obtain its arithmetic inputs independently, retaining the complete S-class and divisor terms. Merely substituting a known Selmer rank into those inputs, or bounding only norm homology, would not continue this result. The present work gives no evidence that the needed companion class terms are uniformly small.

FIN, ORDER9, Q36 and seed-prime coverage are unchanged. No claim is made that this mechanism will complete the seed.

## Review and custody

The separate [bound review](source_screen/BOUND_REVIEW.md) checks the lattice indices, source-class cancellation, minus-component qualifications, and distinction between class lengths and ranks. The [reflection screen](source_screen/REFLECTION_SCREEN.md) checks a repaired prime-to3 application of Gras; its coarse bound is weaker than the incidence calculation. A group check tests the underlying incidence and compositum conventions at3,5,7, without pretending to compute arithmetic class groups there.

The frozen input certifications remain retained. Replays verify the new computations and literal identities, not all historical descent computations. Failed implementation trials are preserved with their corrections. The root replay receipt and manifest record execution and custody separately from mathematical scope.
