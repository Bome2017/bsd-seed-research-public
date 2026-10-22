# Rank-two point directions and the actual unit space

The rank-two goal is a sufficiently small **whole** containing source. A zero ordinary-unit kernel, as obtained on the rank-zero11a1 control, is not the default target for a rank-two curve. Nor do two rational points automatically force the ordinary-unit kernel to have dimension two.

Let U be the ordinary faithful-character unit quotient and V the ordinary virtual-unit quotient. Their exact sequence retains the class term:

\[
0\longrightarrow U\longrightarrow V\longrightarrow\mathrm{Cl}(A)[7]^\chi\longrightarrow0.
\]

Under the retained support and zero faithful divisor-kernel inputs, the rational-point Kummer plane W maps into V and satisfies the global and local conditions. The assertion W lies in U is an additional arithmetic statement: its class images must vanish. Therefore the rank-two point plane gives a lower bound on the **complete** surviving source, but gives a lower bound of two on the ordinary-unit kernel only when both point classes have actual independent unit representatives.

For the current d=4 ordinary-unit space, rank at least2 of the stacked necessary maps proves an ordinary-unit kernel upper bound2. It needs no fundamental-unit completeness if the rank witnesses themselves are authenticated. The unknown class contribution must still be added. A whole-source upper bound2 suffices for a rank-two Selmer conclusion; a whole-source upper bound3 needs the separately retained parity input. Neither conclusion follows from unit upper2 alone.

## A concrete point-source test, without assuming unit support

Let T be the universal nonzero7-torsion point, and choose a function f_T with divisor7(T)-7(O). For a rational point P, evaluate on the good degree-zero divisor (P+R)-(R):

\[
F_P(T)=f_T(P+R)/f_T(R).
\]

This cancels every constant normalization of f_T and represents the point's descent class in the retained function-evaluation convention. It supplies a virtual-unit class after the support/character comparison. It does **not** automatically supply a global ordinary unit.

For an explicit construction, write l_{A,B} for the line through A,B (the tangent when A=B), and v_A=x-x(A). Since7T=O,

\[
f_T=\left(\frac{l_{T,T}\,l_{2T,T}}{v_{2T}\,v_{3T}}\right)^2l_{3T,3T}.
\]

Its divisor is7(T)-7(O): the squared factor has divisor6(T)-2(3T)-4(O), while the final tangent has divisor2(3T)+(T)-3(O). These are actual elliptic functions, not formal norm-compatible classes.

The product over all48 nonzero torsion points has divisor7 times the divisor of psi7. Thus its unspecified constant cancels from the ratio, giving the exact norm identity

\[
N_{A/\mathbf Q}(F_P)
=\left(\frac{\psi_7(x(P+R))}{\psi_7(x(R))}\right)^7.
\]

For389a1, P=(0,0), R=(-1,1), P+R=(1,0), exact division-polynomial evaluation gives

\[
\psi_7(0)=-2357,\quad
\psi_7(-1)=-23\cdot726779,\quad
\psi_7(1)=18041.
\]

Consequently both point-source ratios obtained by exchanging P and R have rational norm different from±1. These particular raw representatives are not ordinary units. They could still become units after division by a seventh power if the relevant ideal seventh-root is principal; that principalization is exactly the unproved class-admission step. The norm identity does not establish or refute it.

The new rank-two control655a1 has model[0,0,1,-13,18] and retained points P=(1,2), R=(3,2), P+R=(-4,-3). Fresh exact values are

\[
\begin{aligned}
\psi_7(1)&=2197265625=3^2 5^{12},\\
\psi_7(3)&=-1831360821=-3\cdot2351\cdot259657,\\
\psi_7(-4)&=-11566477556396484375
=-3\cdot5^{12}\cdot1721\cdot9176117.
\end{aligned}
\]

The same raw-unit shortcut fails for these specified representatives. This is a scoped calculation on natural point representatives, not a claim that the point classes are class-supported or that no other units can represent them.

The small value at x=1 exposes a distinct candidate to the source lane. The primitive tangent at (1,2) is h=y+2x-4=(w+4x-9)/2, with w=2y+1. Its intersection polynomial in the w coordinate is 4(x-1)^2(x-2), and psi7(2)=-3^2·1741. Since psi7 has leading coefficient 7 and degree 24, its exact field norm is

\[
N(h)=\psi_7(1)^2\psi_7(2)/7^3.
\]

Thus the primitive tangent has finite support {3,5,7,1741}. The unscaled expression w+4x-9 has the additional rational factor 2 and norm factor 2^48; it must not be assigned the same raw divisor support. Rational factors vanish after faithful projection, but full integer-divisor admission must retain them or explicitly use h. The actual projected divisor must be checked before treating any quotient as a unit. This candidate was passed to the source agent, not admitted here.

No known Selmer or Sha answer enters these calculations. They clarify why the rational-point plane cannot be silently substituted for an authenticated ordinary-unit basis.
