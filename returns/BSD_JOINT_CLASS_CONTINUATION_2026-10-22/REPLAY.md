# Replay and verification boundaries

Run `python3 verify_packet.py` from this folder. It verifies all manifest
entries and both sets of retained input bindings, then runs the three
checkers in a temporary copy. The original packet remains unchanged.

Requirements: Python3 with its standard library; PARI/GP2.17 compatible
with the supplied exact field syntax. Set `BSD_GP=/absolute/path/to/gp`
when GP is not on PATH. The arithmetic checker retains a local historical
fallback path for the producer host. No BNF computation is invoked.

The checks are:

1. Actual seed field/point/scalar identities; seven exact principal S-ideal
   reconstructions and fourteen literal fifth-power projection identities.
   The full algebraic result is compared byte-for-byte with the saved result.
2. Complete point/covector orbit enumeration at p=3,5,7,11,13, projected
   incidence identities modulo p^2, and36 finite multiplicity countercontrols.
   The finite rank check uses the degree-one Teichmueller character; it is
   not a number-field class map computation.
3. Exact rational outward arithmetic for the analytic reconstruction's
   four illustrative precision policies and optimistic absolute-L gate;
   five rational-spacing controls. No unit lattice or L-value is computed.

The checker does not prove the written mathematics, independently reconstruct
the retained maximal orders, or certify any FIN/ORDER9/Q36 conclusion.
The review files state their own reading and replay scopes. Same-session
agent review is not a human or proof-assistant certificate.
