# Exact next operation and admission checks

The cheapest identified genuine secondary operation is to construct **one** plane cubic for the first explicit excess unit of 1913b1, then perform a second 3-descent. This has not been executed. No local Magma executable was found. The package does not recommend resubmitting a whole seed corpus or treating a software status line as a proof.

Inputs already present:

* curve E=[1,1,0,−34,−135];
* degree-eight torsion algebra and literal nonzero torsion point in `inputs/1913_data.gp`;
* first exact excess unit in entry 8 of `inputs/1913_norm.gp`;
* independently established first Selmer membership and rank-zero bound in the preceding return.

The documented conversion is `ThreeDescentCubic(E, <alpha> : ThreeTorsPts := <T>)`, where the field containing T is exactly the field containing alpha. This is an interface specification, not a tested Magma script: the PARI data must first be exported into Magma's elliptic-curve and number-field objects. The specified torsion point prevents an untracked algebra automorphism from relabelling the source.

Before using the output, require an exact source round trip: convert the cubic back with `ThreeSelmerElement`, identify its torsion algebra explicitly with the original one, and verify that the ratio to alpha or alpha⁻¹ is a cube. Retain the covering map, nonsingularity, and Jacobian identification. Do not substitute an arbitrary cubic with the same Jacobian.

Next, validate the required flex action and call `NineSelmerSet(C)`, preserving rigorous class/unit bounds. A returned −1 would certify the chosen Sha class is not 3-divisible. A nonempty result must be supported by the retained locally soluble covering data. A timeout, unsupported flex case, GRH-only class group, or missing normalization is an implementation outcome—not a mathematical zero/nonzero result.

A known point control should have a nonempty lift set. No value is preassigned to the 1913/28042 excess controls from their first Selmer calculations: those calculations determine 3-torsion, not the full primary exponent. Thus the experiment can distinguish exponent-three excess from higher-divisible excess rather than coding the desired answer into its acceptance test.

For a Cassels–Tate route instead, the corresponding new output must be a normalized function on this cubic, with its divisor and scalar/norm identities certified. The existing exact scalar/norm roots of the source **element** cannot be substituted for this function. The seed already has plane cubics, but its older normalized-function construction stopped at global matrix-algebra splitting. A smaller-control success would test that implementation; it would not automatically remove the seed's cost or construct a cofinite bound.
