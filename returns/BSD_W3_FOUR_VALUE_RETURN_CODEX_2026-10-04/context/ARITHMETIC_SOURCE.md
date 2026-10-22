# An actual integral Euler-system source for the jet

Grade: IMPORTED_SOURCE_INSTANTIATED_UNDER_RETAINED_HIDA_INPUTS. No novelty is claimed for the source theorem. No seed coefficient is evaluated here.

## 1. Domain and the source theorem

Work at ordinary good primes p outside the fixed finite exceptional set in the retained cofinite Hida-control proof and outside {19,59,487}. For the new ten-point application we may additionally exclude p≤13. This changes only a fixed finite set. Retain the seed's full residual image, saturated rank-two Mordell–Weil lattice, bad-prime comparisons, and parity.

The retained Hida result supplies I=Z_p[[T]], an integral rank-two ordinary representation, free signed family symbol lines, and the free ordinary filtration. These results still carry their prior written-derivation grade.

Ochiai, Compositio 142 (2006), Theorem 6.11 constructs an integral family Euler system from optimized Beilinson–Kato classes; Corollary 6.17 relates its local Coleman image to the associated family p-adic L-function. The construction is restated, with proof and nonsolvable residual-image hypothesis, in arXiv:1802.06427v3, Theorem 4.12 and equation (4.12). Use this arithmetic construction, not an arbitrarily chosen element of local cohomology.

The source conditions needed here are met conditionally on the retained datum:

* I is a normal regular local ring; the two-variable ring is normal and Gorenstein.
* The ordinary representation and its two graded lattices are free.
* The signed symbol modules have primitive I-bases.
* The residual image contains SL_2(F_p); it is absolutely irreducible and nonsolvable for p≥5.

The full two-variable main-conjecture equality is not used. In particular, no converse Euler-system divisibility or Skinner–Urban equality is imported to obtain the new index estimate.

## 2. Specify the representation before selecting a component

In the source construction set the ordinary cohomological representation to V(T)^vee. Base-change the tautological cyclotomic character to chi nu_S. Then the coefficient representation of the resulting integral Euler system is

    (V(T)^vee tensor chi nu_S)^vee(1)=V(T)nu_S^(-1)=U.

This fixes the dual, twist and tame character independently of competing conventions for interpolation variables. It uses the omega component and the source coordinate X=p+(1+p)S. When a source writes a cyclotomic involution in its L-function formula, that involution must also be transported. We do not substitute the untransported complex L-value formula for the cohomology class.

Choose and retain the primitive signed symbol bases and the ordinary de Rham basis used in the source theorem. Its compatible arithmetic classes give

    Z_p(r) in H^1(Q(mu_r),U),

with the stated Euler-system norm relations, for squarefree r away from the fixed ramification set. Define

    F_p(T,S)=Col_p(pr_- loc_p Z_p(1)) in R.

This is a definite arithmetic source once these integral bases are fixed. It is not an evaluated power series. Changing a primitive local basis multiplies F_p by a unit and does not affect membership in m^4.

## 3. What happened to smoothing and to the period comparison?

The raw Chern classes of modular units have smoothing parameters and extra factors. We do not declare these factors to be units. Ochiai's theorem constructs the optimized integral Euler system by compatible linear combinations and integral gluing of actual Beilinson–Kato systems. The assertion of integrality is imported from that theorem, not deduced by dividing a computed local value by a nonunit. Its proof and provenance must accompany any implementation of this normalization.

Nakamura, arXiv:2006.13647v2, Proposition 3.15 and (42), provides a separate integral modular-cohomology zeta-map construction; Theorem 3.16 gives the norm relations and Proposition 3.17 the higher-weight compatibility. These corroborate the availability of genuine arithmetic zeta maps. We do not invoke that paper's full universal-deformation theorem: its extra local residual hypotheses were not verified for every seed ordinary prime. Nor do we silently divide a full-level-to-Gamma_1 trace by a p-power.

No equality Z_p(p,p)=r_p z_g with r_p a unit, or even integral, is asserted for the old fixed normalization. Instead VARIABLE_WEIGHT_INDEX.md applies the integral Euler-system bound to Z_p itself. This is the alternative explicitly allowed by the submitted NEXT.md. Write b^Z for its index; do not silently replace it by the old b_p.

There is consequently no need to infer eta_p is a unit. We have an arithmetic class with its own justified sufficient index bound. It remains possible that its local value is highly divisible by p.

## 4. Exact grade

The global arithmetic source is supplied at imported-theorem grade after the displayed coefficient matching. The application to the seed remains conditional on the retained cofinite Hida and seed inputs. This packet does not freshly certify those inputs or the published construction. F_p modulo m^4 is defined, but its ten coefficients have not been computed or proved nonzero.
