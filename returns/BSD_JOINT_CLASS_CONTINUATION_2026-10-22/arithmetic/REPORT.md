# Torsion-coordinate S-unit admission on the actual seed

2026-10-22. **SCOPED_SOURCE_EXCLUDED; NO_NEW_CLASS_BOUND.**

A source with genuinely small prime support was tested before beginning a new unit/class search. This avoids the private primes that destroyed the earlier Cayley families, but fails a different exact admission condition: its faithful scalar component is zero.

In the retained degree-24 coefficient-five point field A, let P denote the universal nonzero five-torsion point, sigma(P)=2P and tau=sigma^2. The following seven actual elements were checked:

    x(P), x(2P), y(P), y(2P), x(P)-x(2P), y(2P)/y(P), x(2P)/x(P).

Their principal fractional ideals were reconstructed exactly using only prime ideals above {2,3,5,2243,4547,5843}. This is stronger than checking that their rational norms have that support: a fractional ideal can have norm one without being the unit ideal.

The tau ratio is +1 for five of the elements and -1 for y(P), y(2P). However -1 is a fifth power. Thus even those two geometrically odd elements define tau-even classes in A*/A*5. Both faithful scalar characters satisfy chi(tau)=-1, so every displayed element has zero faithful projection.

For chi(sigma)=2 and 3 the computation additionally constructs the literal fifth-power witness for every projected product. All14 identities hold in A. A fresh-directory replay reproduces the complete exact output byte-for-byte, checks both retained input hashes, and requires empty GP stderr and the completion marker.

This does not bound Cl(A)[5], its faithful component, or the joint unit/class contribution. It tells us not to invest in a large scalar-closed multiplicative search from these sources. No FIN, ORDER9, Q36 or seed-prime conclusion changes. The corresponding elementary parity statement, its saturation scope and the distinction from line-bundle-valued constructions are in PROOF.md.

## Relation to prior exclusions

The prior smaller-field norm screen already excludes universal transfer through fields of degree less than24; it was read and was not rerun. The archived geometric31-function family, relative196 rows and private-support Cayley families were also not rerun. The present test deliberately changes the producer to honest S-units. It does not claim that this particular parity observation is novel.

The arithmetic does not reveal an admitted next class-bound construction. The unmet requirement remains an independently controlled faithful class contribution, including classes absent from relation lists. This parity screen is a short failed admission test, not a substitute for that requirement.
