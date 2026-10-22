# Review of the explicit shifted-source search

2026-10-18. Scoped mathematical review and separate exact replay.

## Resultant and norm identity

Let D=psi_p have degree d=(p^2-1)/2 and leading coefficient p. Put C(x)=4x^3+b2*x^2+2b4*x+b6, w=2y+a1*x+a3, and h=w-mx-b. For each root x_i of D, the two w values are plus/minus sqrt(C(x_i)). Therefore their h-product is

    (m*x_i+b)^2-C(x_i)=Q(x_i).

Multiplication over all nonzero p-torsion points gives the exact total etale norm

    Norm_A/Q(h)=Res(D,Q)/p^3.

Here Q has degree three with leading coefficient -4. The producer's alternative

    norm(Mod(D,Q))*leading(Q)^d

is Res(Q,D). Since d is even, 3d is even, so it equals Res(D,Q), with no additional sign. The stored resultant itself can be negative: in the 37a1 p5 survivor it is -2^28, not +2^28.

The new replay_all_direct.gp independently uses polresultant(D,Q,x) on all nine direct tables and checks all 5,637 integer values. Every value matches. The root's earlier replay receipt covered four tables; this new replay covers all nine direct tables, including both additional control curves at every tested p.

## The source-support inference is sufficient and appropriately limited

Outside the declared set S (which includes 2,p and all bad-reduction primes), torsion coordinates and h are integral. If the rational norm is a unit there, nonnegative local ideal valuations force every local valuation of h to vanish. Thus an S-smooth nonzero resultant does certify h is an S-unit. Removing the denominator p^3 does not change that support conclusion.

Conversely, a nontrivial S-free factor excludes h itself as an S-unit. It does NOT exclude h/tau(h), its scalar projection, or a product of several failed candidates: ideal divisors can cancel. Any report claiming the entire projected family was killed by this test would be too strong. The root contract correctly retains this distinction.

The tabulated search is finite: p=5,7,11 with the declared slope/intercept sets. It is not a statement about every affine function or every coefficient prime.

## The one asymmetric survivor has an actual arithmetic defect

For 37a1, y^2+y=x^3-x, p=5, the surviving pair (-2,1) gives

    h=2(y+x), Norm(h)=-2^28/5^3.

Using the previously saved exact degree24 field, universal torsion point, scalar2 map, and maximal order, shifted_control37/authenticate.gp calculates the actual principal-ideal valuations of h and its four scalar translates. For the projected element

    a=h^4*sigma(h)^2*sigma^2(h)*sigma^3(h)^3,

the four degree-one primes above2 have valuations

    (16,18,24,22)=(1,3,4,2) mod5.

The five degree-four primes above2 have valuation10 each. The two primes above5 have valuations(-30,0). Thus a is not an ordinary virtual unit and is not in A({5,37},5), the original control's source. Its extra support at2 survives modulo fifth powers. Rational scaling cannot remove an odd-character divisor vector.

The other shifted survivor, (2,-1), is -tau(h), and its chi projection is the inverse of a modulo fifth powers. Their projected span is one-dimensional and its nonzero divisor vector injects into the above four prime coordinates. Therefore that span contains no nonzero ordinary virtual-unit class. This is an exact statement about the two surviving candidates, not all combinations of the candidates that failed the norm-support screen.

The projected survivor has a nontrivial affine norm, but it does not improve the ordinary-unit bound. A separate finite-field calculation at three actual full-splitting primes confirms this. At q=1181 one affine line has projected values

    905,1012,851,968,274,

whose product is403 and whose fifth-power residue is

    403^236=1172 !=1 mod1181.

The new norm direction occurs on a source enlarged by the prime2. It cannot be counted as a rank witness on the smaller ordinary-unit space. The calculation is in shifted_control37/NORM_RESIDUES.json and does not use class-group completeness.

## Verdict

The raw source-norm formula and all nine tables pass the scoped review. The two asymmetric raw S-units were followed past admission rather than assumed useful: their projected divisor class excludes them from the required ordinary-unit source. The search yields no new uniform rank bound and no new seed-prime result. It leaves projected combinations of raw failures open; they require an actual ideal-divisor calculation before being discarded or counted.
