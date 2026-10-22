# Exact global admission at p=3

2026-10-15. Primary source read freshly: Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, long version dated June13,2001, printed pp.15--19 and24--27. Downloaded PDF SHA256:

`d1900c03c034d7ba7a5a02b4a7096a03613926f79e54c6e856cf2d636c42a81f`.

Source: <https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf>.

## Source conclusion

Corollary7.9 and Proposition7.10 characterize the image of H1(Q,E[p]) in the nonzero-torsion-point algebra: scalar compatibility and the affine-line norm must both hold modulo pth powers. Proposition7.8 proves the needed cohomological exactness. This includes p=3; there is no additional p=3 exception. Section10.1 gives the explicit3-descent algorithm: impose scalar compatibility, the complete local images at S, and finally the exact norm-cube condition. Its final space is the Selmer group. The source expressly permits checking cubes directly in the line algebra instead of computing its class and unit groups.

Thus **an actual affine-line norm cube test suffices for the missing global condition**, provided it uses the source's genuine incidence algebra and the scalar condition is already established. A finite set of residue additivity rows alone is only a necessary screen.

## Precise objects for implementation

Use a short model

    Y^2 = X^3 + aX + b,     a != 0.

The point algebra A is the algebra of functions on E[3] minus its zero point. The line algebra B is the algebra of functions on affine lines in E[3] which do not contain zero. These are not the four linear lines through zero. Under full mod-3 image both A and B are fields of degree8.

Write

    phi(X) = X^4 + 2aX^2 + 4bX - a^2/3,
    B = Q[m]/(s(m)),
    s(m) = phi(-m^2) = m^8 + 2am^4 - 4bm^2 - a^2/3.

The incidence algebra D has degree3 over B. A direct polynomial division gives

    g(X) = phi(X)/(X+m^2)
         = X^3 - m^2 X^2 + (m^4+2a)X - (m^6+2am^2-4b).

In D=B[X]/g(X), set

    t = -(m^4+a)/(2m),     Y = mX+t.

The condition a != 0 guarantees m is invertible. The relation s(m)=0 shows that these X,Y satisfy the curve equation. The three conjugate pairs are the three torsion points on the selected affine line. The inclusion A->D is therefore the actual incidence map.

For a nonzero source representative z in A, its required obstruction is

    u(z) = Norm_{D/B}(z in D) modulo B^{*3}.

An explicit b_z in B with b_z^3=u(z) proves the norm condition. Since the norm is multiplicative, checking a basis of the surviving source subspace suffices; cube roots for products are then products of the saved roots. No BNF computation for B is logically required for these positive tests. For a failed test, lack of a numerical root is not a noncube certificate; use an exact complete root routine or a rigorous residue/valuation obstruction.

## Binding an existing degree-eight source field

The implementation must not identify two octic fields by their degrees. For a general Weierstrass model with coefficients a1,a2,a3,a4,a6, use

    X = x + b2/12,
    Y = y + (a1*x+a3)/2,
    a = -c4/48,     b = -c6/864.

Starting with the saved actual torsion coordinates in A, construct their short-model Y. If `1,Y,...,Y^7` is a Q-basis, solve the exact basis-change matrix to express every saved source element as a polynomial h(Y). Evaluate h(mX+t) in D and take the determinant of its3-by-3 multiplication matrix over B. Alternatively bind another explicit field isomorphism. Check the torsion and curve relations after transport.

These are rational algebra changes, not permission to rescale descent functions. The local Kummer evaluations still need their matched normalization; a noncube scalar cannot be dropped. Coefficient denominators in the short model also do not justify erasing local information at3.

## Acceptance evidence for the concrete experiment

A positive complete3-Selmer computation should retain: the complete finite unramified source; its scalar-condition certificates; the precise incidence map; exact norm values and cube roots for a surviving basis; authenticated local Kummer samples spanning the independently known full local-image dimensions; and a proof that all other places are automatic for the selected S. The source allows S consisting of3 and primes with Tamagawa number divisible by3; a larger retained set is acceptable if its conditions are handled consistently.

An independent Mordell--Weil upper bound then controls the rational-point quotient. For the chosen1913b1 control, the separate fresh algebraic2-descent returns rank0. Neither the candidate's predicted Sha=9 nor a numerical L-value is part of the global norm test or that rank bound.

This supplies a complete arithmetic acceptance rule for the fixed control. It is not a uniform estimate, a seed transfer, or a claim that merely writing the rule proves that any candidate survives.
