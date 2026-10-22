# Bounded isogeny-control discovery

Adaptive continuation after the published-table admission screen, 2026-10-12.
Base E=[0,-1,1,-10,-20], conductor 11, with rational 5-isogenies.
Take the first 60 positive odd fundamental discriminants d>1 coprime to 55,
with d=1 mod 4 and (d/5)=-1. These twists have good ordinary non-anomalous
reduction at 5. Compute algebraic rank bounds by PARI descent. Stop at the
end of these 60; no analytic Sha or p-adic numerator is an admission input.
For exact rank-two cases, examine the 5-isogeny point/local indices for an
independent lower bound on Sha[5]. A numerical BSD quotient cannot certify it.
No full large-conductor modular-symbol space is to be constructed.
If a control is admitted, test its p-adic numerator via the conductor-11
quadratic-twist symbol, with all period factors proved before interpreting
its coefficient-height quotient. Reducible residual image is an explicit
difference from the seed, not an application of the seed Kato theorem.

## Adaptive extension (before its computation)
The first 60 gave rank-two d=273,553,617,697, all with neutral relative
Sha-kernel difference from the exploratory point-index calculation.
Extend to the first 1000 admissible discriminants under the same rule,
starting after d=753; stop at the first nonzero difference. Keep every
rank bound, including unresolved bounds. Only exact [2,2] cases proceed
to saturation at primes <7 and point-index screening. Floating height
ratios merely nominate a candidate; exact map/lattice checks are required
before a positive-control claim. No numerator is computed by this screen.

## Structure-guided screen (registered before execution)
The 1000-twist run found 62 exact rank-two cases including the initial four;
none had a nonzero relative isogeny-kernel difference. On those 62, six
quadratic class groups had 5-torsion, but the ideal class above 11 killed
that 5-part in every case. This does not exclude common Sha content.
New filter: positive fundamental d<=100000, (d/5)=-1, (d/11)=1,
d=1 mod 4, squarefree. Compute Cl(Q(sqrt(d)))[1/11] and select nonzero
5-torsion before rank calculations. Stop at first exact rank-two case or
20 such field candidates. A theorem-to-data audit of the isogeny descent
remains mandatory; class torsion alone is not declared Sha.
