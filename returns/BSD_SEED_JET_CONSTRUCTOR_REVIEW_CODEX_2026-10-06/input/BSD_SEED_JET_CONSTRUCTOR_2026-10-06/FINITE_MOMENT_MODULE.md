# An explicit fourth-order integral coefficient module

Grade: **DERIVED — written proof in this session; independent mathematical review pending.** The tests check examples and implementation, not the universal statement. This note makes no assertion that a global Hida eigensymbol has already been constructed.

## 1. Definition

Let p>=17 be prime and let M be the module of bounded Z_p-valued measures on Z_p^2, with coordinates (u,z). Interpret these as the tame-trivial quotient of the primitive-pair chart

    x in Z_p^*, y in Z_p,
    u = log(x/omega(x))/log(1+p), z=y/x.

For i,j>=0 with i+j<=3 define

    m_(i,j)(mu) = integral binom(u,i) z^j dmu,
    known modulo p^(4-i-j).

All these functions are Z_p-valued. There are ten coordinates. Their total Z_p-length is

    1*4 + 2*3 + 3*2 + 4*1 = 20.

Define Q_p as the direct sum of these ten cyclic modules. At this precision the moment map M -> Q_p is surjective.

### Proof of surjectivity

Take the ten Dirac measures at integer nodes (u,z) with u+z<=3 and u,z>=0. Evaluate the ten functions binom(u,i)z^j at these nodes. With the degree-ordered coordinates and nodes used in `jet_module.py`, the resulting integer matrix has determinant 24. One can obtain this by replacing powers z^j with falling factorials: triangular Newton interpolation on the lower set gives the product of the z-factorials, namely 24. Alternatively ordinary elimination gives the same determinant, as checked over Q in the tests.

Since 24 is a p-unit, any ten prescribed Z_p moments can be realized by a Z_p-linear combination of these Dirac measures. Reduce the ten coordinates at their respective precisions. This proves surjectivity.

This is a **local measure** surjectivity statement. Arbitrary assignments of elements of Q_p to cusp divisors need not be modular symbols, Hecke eigenvectors, or values of the seed family.

## 2. Explicit semigroup action

Let gamma=[[a,b],[c,d]] have entries in Z_p, a a unit, c in pZ_p, and nonzero determinant. Right multiplication of primitive row pairs gives

    (x,y) gamma = (ax+cy,bx+dy).

Consequently the induced map of the chart is

    u' = u + L_gamma(z),
    z' = Z_gamma(z) = (b+dz)/(a+cz),
    L_gamma(z) = log((a+cz)/omega(a))/log(1+p).

Here omega(a+cz)=omega(a). Pushforward of measures defines the action. It descends to Q_p.

### Proof of descent, including the tail estimate

Write L(z)=L_0+sum_(n>=1) l_n z^n. For n>=1,

    l_n = (-1)^(n+1)(c/a)^n / (n log(1+p)),
    v_p(l_n) >= n-1-v_p(n).

For 1<=n<=3 this is at least n-1. For every n>=4 and p>=17 it is at least 3. Thus L can be replaced by its cubic truncation modulo p^3, uniformly on Z_p. This is enough in every output coordinate that contains L, because such an output has i>=1 and needs precision no greater than p^3.

Expand

    binom(u+L(z),i) = sum_(r=0)^i binom(u,r) binom(L(z),i-r).

All factorial denominators in this expansion are p-units. In the cubic truncation of L, the coefficient of z^k in binom(L(z),e) has valuation at least max(0,k-e): a product of at most e nonconstant L-coefficients has that valuation. The same estimate holds for every resulting coefficient of the finite polynomial, not just degrees <=3.

The coefficient of z^k in Z_gamma(z)^j has valuation at least max(0,k-j), by the geometric-series expansion of (a+cz)^(-j). For j=0 the expression is simply 1. Terms of Z_gamma(z)^j of degree >=4 can be discarded at the requested output precision when multiplied by the integral polynomial in L.

It follows that the coefficient A_((i,j),(r,n)) of binom(u,r)z^n in

    binom(u+L_gamma(z),i) Z_gamma(z)^j

has, after the justified truncations, valuation at least

    max(0,(r+n)-(i+j)).

If r+n>=4, this coefficient vanishes modulo p^(4-i-j). If r+n<=3, an ambiguity of size p^(4-r-n) in the input moment contributes a multiple of p^(4-i-j) to the output. Therefore all output moments are determined by the ten retained input moments. The action is well defined on Q_p.

The apparent high-degree failure of a naive family filtration has not been ignored. In the full series, a z^p logarithm coefficient loses one power of p relative to the naive n-1 estimate. Our argument uses the actual n-1-v_p(n) estimate and only fourth-order precision. It is not an arbitrary-depth family filtration theorem.

Because the action is induced by pushforward of actual measures, it satisfies the semigroup law. Surjectivity of M -> Q_p makes this a law on all of Q_p, not only on Dirac examples.

## 3. Exact finite computation of the action

Evaluate the ten transformed functions at the ten interpolation nodes and multiply by the inverse of the evaluation matrix. The determinant 24 is a p-unit, so this introduces no p-denominator. Reduce each output row at its own precision. The preceding proof shows that the resulting interpolated matrix is the actual quotient action, not merely an interpolation fit at ten points.

`principal_log` evaluates L at these nodes by exact digit lifting in the principal-unit group. It verifies its power identity; it does not use floating-point logarithms. The implementation supports integer matrices in the displayed semigroup and rejects other matrices. A Manin presentation involving matrices outside this semigroup requires the appropriate coset/induced-module treatment; the implementation does not silently apply those matrices here.

The central scalar matrix diag(1+p,1+p) sends u to u+1 and leaves z unchanged. Therefore

    m_(i,j) -> m_(i,j)+m_(i-1,j),

with the second term omitted for i=0. This checks the weight-coordinate convention directly.

## 4. The existing four source functionals factor through Q_p

Let Xi be an actual integral measure-valued family symbol on the tame-trivial branch through the weight-two seed, with the signed primitive source normalization required by the retained W3 construction. The existence, localization, integral comparison and computation of this Xi are **hypotheses here**, not conclusions of Sections 1–3.

Write

    D_a = {infinity}-{a/p}, 1<=a<=p-1,
    t_w = (1+p)^w-1,
    M_j(D_a;T) = integral (1+T)^u z^j dXi(D_a).

Then

    M_j(D_a;t_w) = sum_(i=0)^(3-j) t_w^i m_(i,j)(Xi(D_a))
                       modulo p^(4-j).

The tail vanishes because t_w is in pZ_p and all binomial moments are integral. In the usual polynomial symbol convention, the specialized coefficient satisfies

    c_(w,a,j) = (-1)^j binom(w,j) M_j(D_a;t_w).

For (w,s) in {(3,2),(3,3),(4,3),(4,4)} define

    V_(w,s) = (-1)^s sum_(a=1)^(p-1) omega(a)^(-s)
                 sum_(j=0)^min(s,3) binom(s,j) a^(s-j) (-p)^j
                     sum_(i=0)^(3-j) t_w^i m_(i,j)(Xi(D_a))
                     modulo p^4.                                      (F)

Substitution in the retained modular-symbol extraction identity gives

    V_(w,s) = alpha_w F_p(t_w,t_s) modulo p^4,

where alpha_w is the ordinary U_p unit. Thus omitting alpha_w changes no valuation or nonvanishing test. It does change the common numerical source coordinate and cannot be ignored for reconstructing a functional equation across different weights.

The coefficient of m_(i,j) in (F) is divisible by p^(i+j), exactly matching its precision p^(4-i-j). Terms with i+j>=4 vanish. The weight variable is T, not T/p. Dividing it by p would destroy this argument.

The tame character at a classical weight must also be transported correctly. Specialization on the fixed tame-trivial weight-space component uses the principal-unit character <x>^w; it is not the unrestricted character x^w with trivial nebentypus at every weight. In particular the odd-weight fiber must carry its appropriate character. No arithmetic source identification is claimed until this convention is checked against the retained Xi.

## 5. What the proof does and does not supply

Sections 1–3 give an explicit finite arithmetic coefficient construction for every prime p>=17. Section 4 proves factorization of the four functionals **conditional on the actual source comparison**.

Nothing here forces those four functionals to be nonzero on the seed. The determinant 24 is an interpolation determinant, not a Selmer bound. The local module admits both zero and nonzero assigned values. Global relations, source normalization, eigenconditions and a genuine low-index estimate remain essential.

## 6. Negative control

A nonzero local assignment can have all four functionals zero. Set all moments to zero except m_(3,0)(D_1)=1 and m_(3,0)(D_2)=-1 modulo p. Because (a/omega(a))^s=1 modulo p and t_w^3 is divisible by p^3, the two contributions cancel modulo p^4 at all four pairs. The tests check this at all six test primes. This is not a global source or a Sha counterexample; it directly blocks the invalid inference from local primitivity to the desired W3 bound.
