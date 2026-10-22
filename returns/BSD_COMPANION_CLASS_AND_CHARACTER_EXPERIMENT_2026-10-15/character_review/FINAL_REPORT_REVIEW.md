# Final report and source-scope review

2026-10-17. Reviewed the final root `REPORT.md`, `p5_norm_upper/PROOF.md`, the seed companion proof, the p=5 full-image argument, the unit-authentication code and replay code/results. Exact file hashes are in `FINAL_REPORT_BINDINGS.json`.

**Verdict: SUPPORTED_UNDER_STATED_INPUTS. The unconditional unit bound and conditional whole-source bounds are correctly separated.**

1. The seed coefficient-three conclusion is conditional on the complete source class presentation and retained actual incidence index theorem. Killing that presented class group with S-prime classes is independently checked integer arithmetic, but it does not prove completeness of the presentation. The rank-four S-unit lattice and multiplication-by-three composition give the valid companion length bound `c_B,S^- <= 2`; the whole source is bounded by four on the same class-completeness condition. The report does not feed a known Selmer dimension into this argument.

2. For 389 at coefficient five, field irreducibility gives irreducibility of the torsion representation. A primitive multiplicative transvection and an irreducible conjugate give upper and lower nontrivial elementary unipotents in a suitable basis; their powers generate SL2(F5). The cyclotomic determinant then gives GL2(F5). This justifies the three-dimensional entire character-unit space, with no fifth-root-of-unity contribution.

3. The unit-authentication calculation checks principal fractional-ideal identities with full integer exponents. It does not depend on the BNF class group or on completeness of a fundamental-unit basis. The completed replay reports all 13 candidates, 317 distinct factors and 295 ideal factors. The code reassembles the exponent matrix from the original compact products. Its input seal hashes match the current compact-unit and number-field files.

4. Candidate nine in the finite-field export is the same ninth compact product among those authenticated. The exporter and authentication code read the same `units_compact.gp`; the exporter preserves the full exponent and factor ordering. The current `eval_data.json` hash matches the input hash in the independently derived minimal norm witness. A separate export replay can additionally check the literal JSON conversion; that is custody verification, not a new arithmetic assumption. The root is retaining that replay separately.

5. The independent non-fifth-power norm witness therefore yields a rank lower bound of one for the actual norm map on the complete three-dimensional character-unit space, hence kernel dimension at most two. This is unconditional with respect to GRH and unit/class completeness, under the explicitly written field/incidence framework. The rank-three residue calculation also proves that the projected candidates span the character-unit space; no guessed fundamental-unit assertion is used. Neither calculation asserts exact global norm rank one.

6. Injectivity of the primitive support-divisor map places every admitted class inside ordinary virtual units. The ordinary Kummer quotient retains all unknown class-supported directions. Consequently

       dim K <= 2 + dim Cl(A)[5]^chi

   is valid, and the final term can be replaced by the actual ideal-class norm kernel if that map is independently controlled. The bound `dim K <= 2` retains the current GRH-dependent class-zero condition. The report does not upgrade the timed-out class certifications into success.

7. The final scope labels are appropriate: actual field/unit arithmetic at p=5; geometric lattice tests only at p=7 and p=11; no all-prime bound, no newly settled original-seed coefficient prime, and no FIN, ORDER9 or Q36 conclusion.

This is a same-team independent desk audit and a previously executed independent minimal arithmetic witness. It is not human review, formal verification, a novelty certification, or a fresh unconditional class-number computation. The earlier addendum's pending unit-authentication condition is now discharged by the exact unit-identity return described above.
