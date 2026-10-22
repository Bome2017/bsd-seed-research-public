# Producer readout: genuine unit admission on the seed

All accepted stages are computation on the actual seed at coefficient3. The exact source and point/cubic identities are checked by explicit cube roots, not merely by matching residue screens. No new BNF or fundamental-unit expansion was performed.

## Exact outputs

Columns G1,...,G15 are the retained source generators, in the last appended object of seed_ctx.bin. Complete valuations have rank9, leaving a six-dimensional unramified span H0. Its basis and ideal-class map are exported. Four actual point/cubic columns have exact coordinates in G, with explicit cube-root witnesses in actual_cube_roots.gp.

The action tau(w)=-w on G modulo cubes is authenticated by15 explicit identities in tau_cube_roots.gp. Thus the anti-invariant kernel has dimension4 on the saved15-dimensional span. All four actual certified classes span that kernel. The384 torsion-additivity rows from12 split primes have full-source rank10; intersecting with valuations or anti-invariance leaves exactly the same four-dimensional span. Finite additivity testing is a necessary screen, not a general sufficiency theorem. On this span sufficiency is supplied instead by equality with four already certified genuine classes.

The full table of all subset intersections is INTERSECTION_DIMENSIONS.json. The basic dimensions are:

| Source | No condition | Norm/anti-invariance | Additivity screen | Actual local conditions |
|---|---:|---:|---:|---:|
| Saved S-source |15|4|5|4|
| Unramified source span |6|4|4|4|
| Unit classes |4|2|2|2|

Combining the conditions does not reduce the final dimensions further.

## Actual admitted and rejected units

The unit-class basis is G12,G13,G14,G15, with exact tau action diag(1,-1,1,-1) over F3. These printed G values need not themselves be literal units; cube corrections are retained.

- An exact compact correction makes G12 a global unit. It is rejected by anti-invariance and by the coefficient-prime3 local condition.
- An exact compact correction does the same for G14, with the same two kinds of rejection.
- The previously constructed epsilon=a_beta1/(a_beta2*g^3) is an actual global unit with class G13. It is genuine, admitted excess.
- The new exact point-unit correction of kappa(P1) has class G13+G15. Its quotient by epsilon therefore realizes G15 as an actual global unit.

The compact witnesses for the rejected controls are rejected_unit_12_certificate.gp and rejected_unit_14_certificate.gp. point_unit_certificate.gp realizes the point direction. Their generator ideals are verified by summing complete prime factorizations, retaining all cancellation and avoiding huge-unit expansion. Corresponding cube identities and unit status do not require class-group completeness.

These four true unit classes are independent: their G coordinates are independent and the residue evaluation matrix has rank15. The field has signature(2,3), hence unit rank4, and its real embedding excludes3-torsion roots of unity. Consequently they form the full group of units modulo cubes without GRH. The anti-invariant unit plane is therefore exactly spanned by the point unit and epsilon, with one non-point direction. No additional unit direction is hidden outside this computed basis.

## Explicit class-to-unit repair

For the two class lifts in CLASS_LIFTS, the combined norm/additivity defects are repaired using G14. In the repair basis(G12,G14), the correction matrix is

    [0 0]
    [2 1].

The producer verifies that adding these corrections makes every displayed defect row zero. Thus the induced obstruction from these two class directions into the quotient by unit defects has rank0. The local map gives the same admitted span. There is no extra obstruction furnished by combining these constraints on this source.

The unramified span has dimension6 and its full unit subspace has dimension4. Therefore these two ideal-class quotient directions inside the tested span are independent even without a GRH upper bound for the entire class group. What still depends on cached class-group completeness is the claim that this span is the entire unramified Kummer source. No such unconditional upper bound is asserted here.

## Historical local-row repair

The old local Kummer helper represents a zero-dimensional image by an empty matrix. The historical selmer3 wrapper then skipped its annihilator rows. The new direct local pass initially raised a dimension error, exposing this issue. Correct handling imposes all local evaluation rows whenever the local image is zero. The affected places are2,2243,4547.

After that repair the local-only kernel is4, not the historical7. The original explicit cubic solubility/independence certificate remains valid, and the old final global kernel dimension4 remains correct. The claim that global norm/additivity eliminated three *locally admissible* seed directions must be withdrawn for this particular saved calculation: the local-only7 was missing conditions. All error output is preserved in local_rejected_trial, and the accepted local pass is fail-closed.

## Independent-check inputs

MATRICES.json contains valuations, exact tau, all additivity/local rows, actual coordinates, source residue matrix, class map, unit bases and repair matrices. stage2_exact_maps.gp and its19 explicit cube roots allow direct arithmetic replay without BNF. Compact unit certificates likewise only need the exported nf for positive ideal checks. The BNF is used to find class/root data, not to justify exact identities after they are exported.

Measured accepted run times: stage1 0.39s; exact maps0.87s; source/class and point-unit work56.75s; local rows0.15s; rejected literal units19.49s. Each job stayed below its stated CPU cap. No new Selmer source was enumerated.

## Seed relevance and scope

This has identified and completely described the genuine unit-admission contribution at this coefficient prime. A unit-only exclusion is impossible on this positive control because it contains actual excess; an arithmetic bound must retain the point/excess distinction. It also tests a concrete class/unit coupling and finds it zero on the actual two class directions. Those are measured facts, not an assertion that coupling mechanisms always vanish.

Coefficient3 is a bad prime for this seed. These ranks are not transported to the good-prime p>=5 Kato or receiver domains. FIN, ORDER9 and Q36 are unchanged. The next experiment must introduce a constraint or comparison not already vanishing on this precisely authenticated admitted span.
