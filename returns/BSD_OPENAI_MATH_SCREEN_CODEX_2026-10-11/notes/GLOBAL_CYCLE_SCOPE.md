# Rational cycles, common scalars, and the seed

Source pin: openai/math fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb.
Grade: source applicability screen and elementary deductions, not validation of the manuscripts' main theorems.

## Sources actually inspected

1. Milne's rationality conjecture for abelian varieties (October 7): introduction and the common rational normalization passage in `build/sections/02_transport.tex`, lines 714–756.
2. The rational Hodge conjecture for CM abelian varieties (October 6): main theorem and proof overview in `01-introduction.tex`, and the full consequences section `07-consequences.tex`.

The local copies and URL/hash bindings are in `sources/global_cycles/`.

## A concrete normalization technique

The Milne manuscript first constructs rational divisor classes and a rational quasi-isogeny on one special fiber. After proving

    a*theta_B = lambda_v theta_*

in each realization, it pairs both sides with theta_*^(D-1). This gives

    lambda_v = deg(a*theta_B . theta_*^(D-1)) / deg(theta_*^D).

The denominator is nonzero by ampleness; both intersection numbers are rational and computed from the SAME divisors. Thus the local scalars are one rational scalar. This elementary comparison is a legitimate technique to reuse once its geometric inputs exist; it does not require accepting every theorem of that manuscript.

The corresponding seed application would need actual maps, a common line, and a nonzero rational testing functional. Separate one-dimensional spaces with independently chosen bases are insufficient. This is relevant to the current BD normalization problem, but the manuscript does not construct the seed maps or the tame Mazur–Tate/regulator comparison. It does not remove the recorded C3 or C8 gaps merely by being cited.

## Two different kinds of independence

The Milne theorem fixes a reduction place and obtains one rational value across coefficient realizations. Its introduction explicitly says that no comparison between different reduction places is required. Our target varies the coefficient prime p and the auxiliary prime ell. The theorem supplies no assertion that those varying data yield the SAME rational value, nor that their denominators are bounded by one fixed integer.

If a single rational correspondence over a fixed number field were already constructed, its denominators could be cleared once. That implication is useful, but constructing such a correspondence with the required seed realizations is the existing open arithmetic problem. It is not furnished by rationality at each special fiber separately.

## Why the Hodge/Tate headlines do not settle this seed

The CM-Hodge manuscript's main theorem concerns rational cycle classes in even Betti cohomology of CM abelian varieties. Its finite-field Tate consequence concerns algebraic cycles spanning Frobenius-invariant rational cohomology of an abelian variety over a finite field. Neither statement is a theorem on Selmer groups of the rank-two curve over Q or on its leading Taylor coefficient.

There is a direct type check. For a point P on an elliptic curve, the divisor [P]-[O] has degree zero, so its ordinary degree-two cycle class is zero, even when P has infinite order. The Kummer class, height, and arithmetic extension information needed here are not recovered from that zero ordinary cycle class. This observation excludes the proposed immediate substitution of point classes into an ordinary Hodge/Tate intersection theorem; it does not rule out more sophisticated constructions involving extensions or heights.

The finite-field proof also explicitly uses rational averaging by a field-extension degree m, even when the coefficient prime divides m. Such rational division cannot be imported as integral primitivity or as a bound on the derivative's excess p-content.

## Disposition

Keep the rational-intersection normalization technique as a comparison template for an actual geometric construction. Do not count these manuscripts as an independent uniform bound, a proof of the 288 identity, or a Q36 rationality theorem. No endpoint changes.
