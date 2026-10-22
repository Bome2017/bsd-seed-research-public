# Attempt at the requested uniform Hida step

Outcome: no uniform upper bound obtained. The local calculation in
LOCAL_LATTICE.md is a positive partial result. The following tests
limit specific proposed deductions, not all possible Hida arguments.

## 1. Correct the family and valuation quantifiers

For each coefficient prime p there is a p-adic ordinary family through
the seed and a retained weight-three point g_p. These are different
families as p varies. The brief's phrase "one ordinary family" is
valid within a fixed-p construction, not as an already constructed
cross-prime arithmetic object.

The actual coefficient ring O_p may be ramified. On the base weight
space, choose T=(1+p)^(k-2)-1; the weight-three value is T=p, so its
pi_p-valuation is e_p, not automatically one. A branch can itself be
ramified over weight space; no common local parameter or etaleness is
part of the retained datum.

Even if one proves, in the EXACT integral normalization of KATO_MATCH,

    F_p(T)=T^2 U_p(T),       A_{g_p}=F_p(t_3),

the index is

    b_p=2 v_pi(t_3)+v_pi(U_p(t_3)).

The displayed bound v_pi(U_p(t_3))<=1 implies b_p<=3 only with the
additional condition v_pi(t_3)=1 (and the specified exact comparison).
It does not do so for an arbitrary ramified branch or coefficient DVR.
No such Taylor identity, normalization equality or branch parameter
condition has been proved here. Analytic rank two alone is not their
proof.

## 2. Test the formal analytic properties, rather than declare a unit

Put S(T)=T^2/(1+T). For each integer m>=1 consider the integral series

    F_{p,m}(T)=p^m S(T)+S(T)^(m+1).

It has exact order two at T=0. It is integral and primitive (mu=0):
modulo p its first nonzero coefficient occurs at degree 2m+2 and is
one. It is invariant under T -> -T/(1+T), since S is invariant.
Its value at T=p is nonzero and

    v_p(F_{p,m}(p))=m+2,

because the two summands have distinct valuations m+2 and 2m+2.

Thus integral analytic interpolation, mu=0, a double zero, this common
functional symmetry, and nonzero weight-three specialization do not
imply b<=3 or any uniform upper bound. This is a countercontrol to
that FORMAL inference, not an actual seed L-function and not a
refutation of an arithmetic bound. The retained Taylor calculation
(context/LOCAL_PREDECESSOR.md, section F) and pairing review already
separated analytic nonzero from residual primitivity; this control is
not advertised as a new BSD obstruction.

## 3. What was actually advanced

The ramified local denominator, previously represented by an unknown
lattice generator d_g, is now p^{-2} in a specified Gauss-sum frame.
Its Euler cancellation reduces the index to v_pi(A_g). This changes
the calculation required by the brief: a worker no longer needs to
guess a ramified analogue of Kato 14.21 or an extension-class loss.

It does not establish an upper bound on A_g. No identity
A_g mod pi = old C_p has been proved, so W3_COLLAPSES_TO_CP would be
an unsupported verdict. Conversely, the one-way nature of the index
bound does not by itself make its upper estimate easier than the
previous target. Its extra lifting requirements in the retained
pairing review continue to apply.

## 4. Direct BSD consequence and remaining coverage

The existing argument, with the newly calculated local lattice, is

    independent v_pi(A_{g_p})<=3
      => dim_Fp Sha(E/Q)[p]<=1
      => (retained parity) Sha(E/Q)[p]=0
      => Sha(E/Q)[p^infinity]=0.

This is an ordinary-prime implication. An eventual cofinite ordinary
bound would still leave supersingular primes, which this packet has
not shown to be a finite set, as well as excluded and bad primes.
FIN, ORDER9 and Q36 do not follow from the present partial result.
