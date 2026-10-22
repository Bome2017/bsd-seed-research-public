# Same curve at a larger coefficient prime

Status: UNIT_AND_VALUATION_PROFILE_CERTIFIED_CLASS_TERM_UNRESOLVED.

We tested the SAME rank-two curve 1664n1 (y²=x³−4x+16) at coefficient 5, after the preceding complete coefficient 3 calculation. No further curve panel was collected.

The degree 24 torsion point field and scalar action were constructed exactly. The full faithful unit space has dimension 3. Actual units were authenticated by 332 exact factor-ideal reconstructions and integer divisor cancellation over 291 prime ideals; a separate replay passed. Projected unit residues have rank 3, so they span the entire faithful unit space. Actual affine-line incidence norm residues have rank at least1, giving a full unit-kernel upper bound 2. This does not assume a fundamental-unit basis.

Every faithful valuation component above S={2,5,13} is zero, checked on the actual primitive prime ideals. Thus the unconditional containing-source bound is

    2 + dim_F5 Cl(A)[5]^chi.

The BNF computation provisionally reports C3. If independently certified, this would make the complete bound at most2. Its unconditional class quotient certification hit the 110-second alarm and was rejected; no class term has been removed by assumption. This is a computational certification limit, not a mathematical claim that the class term is nonzero or that scaling fails.

This is genuinely a same-curve scaling test, with the complete unit sector bounded and valuation sector excluded. It is not yet a complete source bound at 5. The previous p=3 bound is retained; no new seed-prime or FIN conclusion follows.

Replays: `replay_units.gp` verifies all actual-unit identities; `evaluate.py` reconstructs finite-field incidence residues from exported compact factors; `check_profile.py` independently checks all saved matrix ranks, archimedean character dimensions and valuation dimensions. Source class output remains explicitly provisional. The runtime receipt for class certification is failed despite GP exit 0 because it has an error and lacks its success marker.
