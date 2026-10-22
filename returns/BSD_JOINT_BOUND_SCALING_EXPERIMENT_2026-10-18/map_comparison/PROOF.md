# Full additivity is not an additional split-prime constraint

Scope: prevent claiming artificial rank gain from replacing the complete affine incidence map at one fully split prime by the complete additivity map there. This does not identify global and local constraints at other places.

For p odd let V=F_p^2 and let F consist of functions f:V -> F_p with f(0)=0 and f(aP)=a f(P). Its dimension is p+1. A residue of a faithful scalar arithmetic class at a prime q splitting the torsion field, with q congruent1 modp, defines such a function after choosing a generator of mu_p(F_q).

The incidence map sends f to the sums over all affine lines lambda(P)=1. The Schaefer-Stoll coefficient exact sequence immediately preceding Proposition7.8 identifies its kernel on the faithful scalar component with the two-dimensional space of linear forms V -> F_p. The full additive-function equations have the same kernel. Thus the two row spaces coincide. This is a primary-source application, not a new theorem or an arithmetic rank calculation.

Our independent exact check chooses p+1 projective representatives and constructs the two matrices directly, for p=3,5,7,11,13,17. Both ranks, and the stacked rank, are p-1 in all six cases. The two coordinate linear forms are explicitly checked to survive. Additivity against the two coordinate increments suffices since those increments generate the additive group of V.

Consequently this map substitution cannot make a nonzero kernel vector fail at the same split prime if every incidence row was already imposed. It can complete a partial previous row screen, but that is not an independent constraint. At the coefficient prime or bad places the actual Kummer local condition can be stricter; it must be calculated in its proper local algebra and cannot be replaced by these split-prime matrices.

Source read fresh: Edward F. Schaefer and Michael Stoll, How to do a p-descent on an elliptic curve, displayed coefficient exact sequence before Proposition7.8 and Propositions7.10–7.11, https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf . The relevant statements separate coefficient-module exactness, induced cohomology maps, incidence norms, and all-place Selmer conditions. No source finiteness or class completeness is inferred from these geometric matrices.
