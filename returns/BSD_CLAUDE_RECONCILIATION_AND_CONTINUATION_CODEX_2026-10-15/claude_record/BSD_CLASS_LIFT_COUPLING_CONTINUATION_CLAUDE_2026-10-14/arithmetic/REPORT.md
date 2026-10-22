# Complete nontrivial-class source calculations

The bounded initial scan considered24 rank-two candidate rows from Cremona's allgens data, excluding coefficient3 bad reduction and the three prior controls. It produced three certified fields with relevant ordinary anti-invariant3-class group C3:718b1,997c1,1070a1. All three exact joint calculations reached the two rational-point directions. None produced an unrepairable ordinary class direction.

## Search scope

`search/SCAN_STATE.json` distinguishes9 fully certified class3-zero fields,3 fully certified relevant C3 fields,8 provisional class3-zero screens without bnfcertify,3 timeouts, and1 nontransitive/reducible source rejection. Provisional class-group computations retain their GRH qualification and are not nonexistence certificates. Each GP process had alarm90 and a roughly1GB PARI stack ceiling; Python imposed a100-second outer timeout. The negative candidates were not used as upper-bound proofs. No Sha label or analytic value selected an outcome.

## Accepted arithmetic

| Curve | Point pair | Certified class group | Cl_S[3] | Full source | valuation-zero | units | joint admitted | admitted units | admitted classes |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
|718b1|(-1,2),(3,2)|C3|0|13|5|4|2|1|1|
|997c1|(3,0),(1,5)|C3|0|10|5|4|2|1|1|
|1070a1|(3,1),(-2,6)|C3|0|14|5|4|2|1|1|

The source retains all allowed S-prime valuations. Although Cl_S[3] vanishes, the ordinary Cl[3] direction occurs in the valuation-zero combinations of S-units; it was not discarded. The exact boundary was computed by factoring every generator, forming each cube-root ideal of every valuation-zero basis element, and mapping that ideal into the certified class group. Its kernel is exactly the full global-unit subspace. The boundary is surjective onto the ordinary C3.

The entire class group is anti-invariant under tau, verified by actual ideal automorphism and class coordinates. On each field the scalar antiunit component has dimension two. Six completely split residue-prime additivity tests reduce the admitted unit component to one. Actual local conditions also leave exactly one admitted unit direction. The full joint kernel has dimension two and the exact two point Kummer columns span it. Consequently the pair's mod3 saturation and rank-two conclusion follow under the retained Schaefer--Stoll source theorem; the database rank and point-height determinant were not used as the upper bound.

## Actual class repair, not only dimension counting

Let U1,...,U4 be the literal global units in each `witness_data.gp`; beta is the displayed ordinary class lift. Exact number-field cube-root checks establish:

|Curve|Literal unit repair|Kummer class after repair|Admitted point-unit class|
|---|---|---|---|
|718b1|U2^2 U4^2|P1+2P2|P2|
|997c1|U3^2 U4^2|2P1+P2|P1|
|1070a1|1|2P1+P2|P1|

For example,718's quotient `(beta*U2^2*U4^2)/(ftan(P1)*ftan(P2)^2)` has an exported literal cube root. A separate check verifies the class ideal I satisfies I^3=(beta). These identities show why the class group does not supply excess here: its actual admitted direction is already occupied by rational points.

For every block D tested—scalar; scalar+finite additivity; local; joint—the class-to-defect map modulo D(global units) is zero. Its unit repair matrices are exported. This is an observed zero boundary in three actual arithmetic examples, not a general claim that the boundary always vanishes.

## Actual change in the affine unit norm

Each field also has a literal norm-one unit rejected by an actual affine-line norm residue. The three selected nonzero3-torsion points sum toO, and the residue product of the unit along that line is not a cube:

|Curve|Split residue prime q|Product along affine torsion triple|Product^((q-1)/3) mod q|
|---|---:|---:|---:|
|718b1|829|714|125|
|997c1|223|165|39|
|1070a1|433|315|234|

The last entries differ from1. All field roots, torsion points, unit evaluations and the selected triple indices are saved. The calculation is on actual global units; it is not an arbitrary finite-dimensional matrix example.

One independent antiunit line is admitted because it is an actual point Kummer class. Another is excluded by this cubic-residue test. Therefore the affine-incidence norm has a one-dimensional kernel modulo3 on the complete antiunit component. Combined with the retained integral forward/reverse composition equal to3, its Smith factors are(1,3). This differs from the prior unit-only negative controls and seed3 positive span, which have factors(3,3). The source of the difference is now exhibited by a concrete norm residue.

## Local approximation authenticated

A new guard in `lib/selmer.gp` retains a sample only when its known p-adic precision proves the tangent-function class unchanged in every relevant ideal-star quotient. Independently, `local_certify.gp` recomputes exact rational Hensel inequalities for every saved sample: if F(x,y0) is nonzero, v(F)>2v(F_y) and N=v(F)-v(F_y). It verifies e*N-v(ftan)>=the required principal-unit depth at every prime ideal. Six samples at718, eight at997 and eight at1070 pass, with minimum excess precision35,44,32 respectively. Different samples at45 digits reproduce the earlier35-digit local row spaces. Zero local images retain all evaluation-zero equations.

The old library, class-lift principality guard and local-precision guard diffs are retained. The class-lift guard checks both the zero ideal-class coordinate and exact compact-factor ideal product; the selected three fields have Cl_S[3]=0, so this particular new branch was not needed for their sources.

## Limit of this panel

This experiment now has complete rank-two controls with a nonzero relevant class source and literal class repairs. It has not found a class defect that remains nonzero after every global-unit repair. No upper bound across coefficient primes follows from these three successes. Further searches must distinguish the class-to-defect map from the point-to-class map: a class may survive every admission condition without contributing any quotient beyond the known points.
