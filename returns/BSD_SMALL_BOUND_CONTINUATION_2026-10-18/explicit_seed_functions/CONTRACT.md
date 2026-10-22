# Explicit torsion functions: source test before norm tests

For E in {seed,389a1,37a1}, p in {5,7,11}, test h(T)=w(T)-m*x(T)-b where w=2y+a1*x+a3. Candidate m,b are specified in search.gp before calculation. S comprises p and prime factors of2*discriminant. Exact resultant is proportional to the rational norm by a p-power. If its S-free part is1, h is an S-unit because torsion coordinates are integral away2p. Test also h(T)/h(-T) or the scalar chi projector.

Do not infer norm-rank from source support. The default even/homogeneous torsion candidates have zero odd projection; include m=b=0 as a negative control. A failed rational norm support test excludes h itself as an S-unit, but does NOT exclude its ratio or projected class, since conjugate divisors can cancel. Repair: for failed h use prime-specific reduction and divisor/permutation checks when affordable; do not prematurely kill the projected candidate.

At most 2000 lines per curve/p, no polynomial factoring needed. Candidate coefficients small symmetric integers plus seed point-adapted intercepts. Preserve all resultant S-free parts. No known Sha answer or expected norm rank is an input.
