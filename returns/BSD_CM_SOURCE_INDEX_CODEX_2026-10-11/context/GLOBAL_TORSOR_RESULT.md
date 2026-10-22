# Two exact global Kummer comparisons discovered from the mixed-place experiment

Status: **EXPLICIT_GLOBAL_KUMMER_COMPARISONS_COMPUTED**. Written proof with exact arithmetic checks; same-worker checked, not Lean-verified or independently accepted. These are comparisons of genuine point classes on the control curves. They are not the missing seed CM/Kato comparison and supply no seed bound.

## The identities

Retain the explicit torsion maps constructed in `../torsion/RESULT.md`. Let

    E = [1,1,1,3,12],  P1=(0,3), P2=(7,17).

Let C167=[1,1,1,1878418,-485198548] and Y167=(480,22723), and take

    f167 = ../torsion/map_167_0_0.json.

Then in H^1(Q,C167[5]),

    kappa_C167(Y167) = (f167)_* kappa_E(2*P1+P2).

Here 2*P1+P2=(7/4,-53/8). The map has Weil-pairing multiplier 3, retained explicitly.

Let C113=[1,1,1,-1669982047,-25795561267816] and

    Y113=(39736379971/293764,7496759272384463/159220088),
    f113 = ../torsion/SELECTED_SYMPLECTIC_MAP.json.

Then in H^1(Q,C113[5]),

    kappa_C113(Y113) = (f113)_* kappa_E(-P1)
                      = (f113)_* (4*kappa_E(P1)).

The latter map preserves the Weil pairing.

These identities explain the control experiment's auxiliary-place scalar patterns by global arithmetic. They are proved by explicit Galois-equivariant affine isomorphisms of the two genuine 5-division torsors, not extrapolated from matching local values. Consequently they remain true after restriction to every completion and every extension field (with the same maps).

## Construction of the affine torsor maps

For a non-2-torsion rational point P on E, let X5,E(x) denote the x-coordinate of [5]Q as a rational function of x(Q). Form

    F_P(x) = numerator(X5,E(x)-x(P)), normalized monic.

It has degree 25. Although the x-equation also occurs for the fiber of -P, it gives precisely the 25 x-coordinates of [5]^{-1}P, since the two fibers have opposite points with the same x-coordinates. The y-coordinate is recovered by the invariant differential, rather than by an arbitrary square-root choice.

Write v=y+(a1*x+a3)/2. Since [5]^*(dx/(2v))=5 dx/(2v),

    v(Q) = 5*v(P)/X5,E'(x(Q)).

For both specified P, F_P is verified irreducible. Set K=Q[u]/F_P. The above formula constructs an actual point Q in E(K), and the exact elliptic group law verifies [5]Q=P.

For the target point Y, form G_Y in the same way. Factor G_Y over K. In both cases it has exactly one root r in K. Recover

    v(R) = 5*v(Y)/X5,C'(r),

and verify [5]R=Y by the exact group law. The saved coefficients express r and v(R) as rational polynomials in u. The minimal polynomial of r has degree 25, so this construction induces a bijection of the two sets of 25 torsor points over Qbar. Rational coefficients make the bijection h G_Q-equivariant.

The input polynomials and the coordinate functions are saved in `TORSOR_INPUT*.json` and `TORSOR_MAP*.json`. The source points and target points are not supplied as a formal free torsor: they are the specified rational points on the actual elliptic curves.

Finding the field map is not enough. Its action on torsion must be matched to f113 or f167. The next argument does that.

## Affinity lemma: why the torsor bijection has a single global linear part

Let V=E[5] and identify C[5] with V using the already-proved torsion isomorphism f. Let K0=Q(E[5]). Because f is G_Q-equivariant, K0 is also Q(C[5]).

1. **V is irreducible.** The irreducible degree-12 polynomial psi5,E was checked in the torsion computation. A G_Q-stable line in V would give a G_Q-stable two-element set of x-coordinates of its four nonzero points. That would produce a rational degree-2 factor of psi5,E. Hence no such line exists.

2. **The source torsor has all translations over K0.** On G_K0 the Kummer cocycle is a homomorphism into V, with G_Q-stable image. The image is therefore either zero or V. If it were zero, the Galois action on the 25 source torsor points would factor through a subgroup of GL2(F5). Its order divides 480, which is not divisible by 25. It could not act transitively on 25 points. This contradicts the irreducibility of F_P. Thus the image is all V.

3. **The Galois-equivariant bijection h is affine.** Fix Q in the source torsor and R=h(Q). For any v in V choose sigma in G_K0 with sigma Q=Q+v, and define

       L(v)=sigma R-R.

   This is well-defined: if two choices have the same effect on Q, their quotient fixes Q and hence fixes h(Q)=R. On G_K0 both torsion representations are trivial, so Kummer cocycles are homomorphisms. Thus L is additive and F5-linear. Equivariance of h makes L intertwine the two residual representations. It is an isomorphism because h is a bijection. Moreover h(Q+v)=R+L(v) for all v.

4. **The linear part is c*f for one c in F5*.** The source has discriminant -3^2*7^2*11^2 and c4=-143. At 7, c4 is a unit, so the displayed model is minimal multiplicative, of type I2. Tate uniformization over the unramified quadratic extension (the reduction is nonsplit) gives a nontrivial inertia transvection on V: its upper-right entry is proportional to v7(Delta)=2, which is nonzero modulo 5.

   An endomorphism commuting with this transvection has the form aI+bN, with N a rank-one nilpotent. If b were nonzero and the endomorphism commuted with the full residual Galois group, N would also commute with that group, and ker N would be a stable line. This contradicts irreducibility. Thus End_G(V)=F5, so L=c*f.

This proof does not require a separate full-GL2-image theorem, a numerical trace comparison, a saturated basis assumption, or a finiteness assumption on any Sha group. The standard imported local input is Tate's description of multiplicative-reduction torsion; the irreducibility and polynomial identities are exact computational inputs.

## Matching the scalar exactly

We use q=3061, where the source and both target curves have good reduction and the source five-torsion is fully rational. Both source division-fiber polynomials factor into five irreducible degree-5 polynomials over F_q. Working over F_(q^5), one root gives an actual Q with [5]Q=P. Apply the saved rational torsor map h.

For every T in E[5](F_q), we verify

    h(Q+T)-h(Q)=f(T).

All 25 translations pass for both partners. Since the affinity lemma already proves the global linear part has the form c*f, and nonzero prime-to-q torsion specializes injectively at good reduction, this identifies **c=1** globally. The finite-field computation is used only to select among four proved possible global scalars, not as an empirical proof of affinity or of the torsor bijection.

For a Galois automorphism sigma we now have

    sigma R-R = h(sigma Q)-h(Q) = f(sigma Q-Q).

This is equality of the actual Kummer cocycles, and establishes the displayed H^1 identities.

## What the experiment has discovered

The input was a local pattern. The output is a global affine arithmetic map explaining that pattern. The local scalar is not a separate number chosen at each auxiliary prime: for these point-class controls it comes from one global Kummer identity.

This closes the common-source comparison for these particular control-point classes. It gives a real test of the proposed discovery process: observe a relation, construct an exact torsor map, verify its linear part, and obtain a statement valid at all places.

It does not yet identify the CM divisor class with Y113 or Y167 with its integral multiplier; that separate arithmetic source identification must remain visible. It does not identify either control class with the seed's Kato derivative. It proves nothing uniformly as the coefficient prime varies. Neither a new seed Sha conclusion nor FIN, ORDER9, or Q36 follows.

## Reproduction and sources

The scripts use the same Sage/PARI runtime as the preceding torsion construction, all with exact rational or finite-field arithmetic. `find_torsor_map.py` handles 167; `find_torsor_map_113.py` handles 113. The two `verify_torsor_action*.py` scripts check irreducibility, primitive degree, and scalar matching. Root finding took less than one second for each curve on this host. No remote or paid computation was used.

For the imported multiplicative-reduction input, Tate uniformization and the resulting torsion representation can be checked in Samir Siksek, *Explicit Arithmetic of Modular Curves*, section “The mod N representation of a Tate curve”:
https://samirsiksek.github.io/siksek.github.io/modcurves2.pdf
and Serre's original treatment, IV, section on multiplicative reduction:
https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf

No claim of literature novelty is made. The finite-model identities may be instances of existing visibility/congruence constructions; the contribution to this experiment is their explicit, reproducible source matching.
