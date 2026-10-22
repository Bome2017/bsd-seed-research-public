# Explicit quintic for the unit class at d = 43737

Status: exact equation construction and generic smoothness checked. The separate
Selmer calculation must supply all-place local solubility and nontriviality modulo
rational points. Neither follows just from the equations below.

## Source and orientation

Tom Fisher, *Explicit 5-descent on elliptic curves*, Open Book Series 1 (2013),
395–411, Theorem 5.3 on printed p. 402, gives a rational Pfaffian model for a
quadratic-character isogeny class represented by
`theta = (r+s*sqrt(d))/(r-s*sqrt(d))`. The page was visually inspected to bind all
matrix signs. Primary source:
https://msp.org/obs/2013/1-1/obs-v1-n1-p20-s.pdf

Here Fisher's isogeny runs from the twist of C_lambda to the twist of D_lambda.
At lambda = 11, these minimalize respectively to

- C_11: `[0,-1,1,-7820,-263580]`;
- D_11: `[0,-1,1,-10,-20]`.

Thus Fisher's isogeny is our dual isogeny F -> A, and its covering has Jacobian F,
not A. This direction matters for identifying the Sha group.

## Actual arithmetic class

Set d = 43737, r = 1464, s = 7. Then

```
r^2 - d*s^2 = 183,
(r+s*sqrt(d))/(r-s*sqrt(d)) = 23423 + 112*sqrt(d) = theta,
Norm(theta) = 1.
```

This is a specified class, rather than a search over formal Selmer dimensions.

## Actual equations

Let C be the projective subscheme of P^4 with coordinates x0,...,x4 cut out by the
five signed 4x4 Pfaffians of the following alternating matrix (the lower triangle
is minus the transpose):

```
0  11*x0  43737*(x2-x4)  -x1+x3          -x3
   0       -x1-x3          x2+x4           x4
           0              183*x0          1464*x1+306159*x2
                          0               7*x1+1464*x2
                                          0
```

The explicit five quadrics are saved without abbreviated coefficients in
`FISHER_MODEL.json`. By the source construction, this C is the hat-phi covering
class corresponding to theta in Fisher's coordinate. The natural kernel generator differs by sign from the descent function's generator; comparison may invert the class, which preserves nontriviality. See AUDIT.md. A formula in projective coordinates for the
covering map C -> A has not been extracted in this calculation; the class and
its target are identified by the source theorem.

The two twisted minimal models were independently computed from C_11 and D_11:

```
Jac(C) = F: [0,0,1,-14959712463303,-22270654620235278500],
base = A:   [0,0,1,-19766893413,-1937478573143510].
```

## Exact checks performed

`fisher_model.py` checks the norm identity, both minimal-model identifications,
the twist identifications, the Pfaffian syzygy q*M=0, and the Hilbert polynomial
5*t. `geometry_check.py` computes all 100 three-by-three minors of the five-by-five
Jacobian. In each of the five affine projective charts x_j=1, the ideal of the
quadrics and these minors has Groebner basis [1] over Q. Thus the model has no
geometric singular point in characteristic zero. Fisher's construction supplies
the genus-one/Jacobian interpretation, consistent with the Hilbert polynomial.
These are exact symbolic computations, not proof-assistant certificates.

`local_witnesses.py` exhibits nonsingular reduction points at 5,7,11,13,17,19.
Each receipt includes three independent equations, a unit Jacobian minor, and
a unit complementary entry of M. The syzygy then recovers the remaining two
equations, so multivariable Hensel lifting yields a Q_q point. For example:

- q=5: `(1:0:1:2:3)`, minor = 2 mod 5;
- q=11: `(1:0:6:0:6)`, minor = 5 mod 11.

The simple reduction search did not find a nonsingular point on this unminimized
integral presentation at 2,3,61,239. No local insolubility is inferred. The
separate isogeny-Selmer theorem calculation is needed for those places and for
the all-place statement; this finite list of successful checks is not that proof.

## Replay

Use the retained Sage environment Python:

```
/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python fisher_model.py
/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python geometry_check.py
/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python local_witnesses.py
```

No Magma service, paid computation, or remote job was used.
