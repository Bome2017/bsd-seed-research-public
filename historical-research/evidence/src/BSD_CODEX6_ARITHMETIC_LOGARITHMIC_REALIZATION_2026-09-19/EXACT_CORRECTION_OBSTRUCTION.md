# L3: the Mellin obstruction survives finite algebraic exact corrections

Status: ordinary mathematical proof, extending the predecessor's M2.
No kernel certificate, independent referee acceptance, or novelty claim
is asserted. The conclusion is a nonexistence theorem for a **local
differential comparison**, not for an equality between two numbers.

## L3a. The class stable under the proposed corrections

Fix a positive integer w and a sufficiently high half-plane
\(\mathfrak H_Y=\{z:\operatorname{Im}z>Y\}\). Functions below can be
meromorphic germs at this cusp: identities mean identities for all
sufficiently large Y. Let \(Tg(z)=g(z+w)\), and define

\[
\mathcal A_w=\left\{g:
 \dim_{\mathbb C}\operatorname{span}\{T^ng:n\in\mathbb Z\}<\infty\right\}.
\]

This is a condition of finite-dimensional translation span. It does
**not** require the monodromy group to be finite.

The following operations preserve membership in \(\mathcal A_w\):

1. Finite sums and products.
2. Differentiation with respect to z.
3. Multiplication by any w-periodic meromorphic function.

**Proof.** For sums use the sum of the two finite-dimensional spans.
For products use the span of all pairwise products of their basis
functions. Translation commutes with differentiation, so the derivatives
of a basis span all translates of the derivative. A periodic multiplier
can be factored out of every translate. These arguments also apply to
germs by increasing Y when necessary. QED.

Coordinates of horizontal sections of a finite-rank meromorphic
connection on the punctured curve, written in an algebraic meromorphic
frame, belong to this class near a cusp. In fact its pullback is
\(d-\mathcal B(z)dz\), with \(\mathcal B(z+w)=\mathcal B(z)\).
On the simply connected half-plane a fundamental solution matrix
\(\Phi\) satisfies

\[
\Phi(z+w)=\Phi(z)M
\]

for a constant invertible matrix M: both matrices solve the same
differential equation, so their ratio is constant. Every translate of
a coordinate of a horizontal section is consequently a linear combination
of finitely many entries of \(\Phi(z)\). This proof needs no assumption
of regular singularity; logarithmic connections are included.

An algebraic meromorphic change of frame has periodic coefficients and
preserves this property. On an algebraic finite cover one first takes
w to be a multiple of the cusp ramification index, so the frame and
connection coefficients are single-valued on the punctured disk.
Vector bundles admit meromorphic frames there. Additional finitely
many punctures do not affect this cusp argument.

Finite tensor operations and finite-rank extensions remain in the
same class. Finite iterated integrals of algebraic differentials also
qualify: include the finitely many prefixes of the words in question
as coordinates; their differentiation equations form a finite
triangular system with periodic coefficients. Coefficients of the
associated scalar differential forms then lie in \(\mathcal A_w\).

This includes the usual exact terms from twisted de Rham theory.
If s is an algebraic meromorphic section and v a horizontal dual
section, then

\[
d\langle v,s\rangle=\langle v,\nabla s\rangle .
\]

The scalar primitive \(G=\langle v,s\rangle\) has finite-dimensional
translation span by the preceding closure properties. Ordinary
algebraic exact primitives are the rank-one special case.

We call a scalar differential \(\beta=b(z)dz\) **admissible here**
when \(b\in\mathcal A_w\), and an exact correction dG admissible when
\(G\in\mathcal A_w\). This definition is broader than the finite
algebraic constructions just listed; it specifies exactly the class
tested by the next theorem.

## L3b. Nonexistence modulo admissible exact and lower terms

Let f be a nonzero holomorphic function on \(\mathfrak H\) periodic
under \(z\mapsto z+w\), let \(c>0\), and let
\(\ell(z)=\log(-ic z)\), with the branch on the right half-plane.
Put \(\alpha=2\pi i f(z)dz\).

There are no constants a,b in \(\mathbb C\), admissible differential
\(\beta\), and admissible primitive G for which

\[
\boxed{\alpha\ell^2=\beta+dG+a\alpha+b\alpha\ell} \tag{L3}
\]

holds as an identity on a cusp neighborhood. The same conclusion
holds if \(\ell^2-b\ell-a\) is replaced by any nonconstant polynomial
in ell.

**Proof.** If (L3) held, closure under addition and differentiation
would give

\[
2\pi i f(z)P(\ell(z))\in\mathcal A_w,\qquad
P(X)=X^2-bX-a .
\]

Thus finitely many distinct translates would have a nontrivial
constant linear relation. Since f is periodic and nonzero, division
on an open set where it does not vanish would give

\[
\sum_{n\in I} c_n P(\log(-ic(z+nw)))=0
\]

on that open set, for a finite set I and constants not all zero.
The functions displayed are holomorphic on all of \(\mathfrak H\),
so this relation extends to all of \(\mathfrak H\) by the identity
theorem. This continuation concerns only these explicit logarithms;
no continuation of beta, G, or their connection is needed.

For a chosen n in I let \(z=-nw+iy\), \(y\downarrow0\).
The nth polynomial is \(P(\log(cy))\), whose absolute value tends to
infinity. Every other polynomial has a finite limit: its logarithm
approaches a nonzero point of the imaginary axis from the right
half-plane. Consequently \(c_n=0\). Repeating at each n contradicts
the nontrivial relation. This is exactly the boundary mechanism of M2,
now applied after closure under the admissible corrections. QED.

The theorem applies to the fixed modular form with \(c=\sqrt N\).
For a finite cover choose an integer cusp width w for which f and
the algebraic data are periodic.

## Application to the explicit unit and to its finite replacements

For \(u_N=N^6\Delta(Nz)/\Delta(z)\), the cusp expansion gives

\[
U(z+w)=U(z)+2\pi i\,w(N-1),\qquad U=\log u_N .
\]

Indeed subtract the term \((N-1)\log q_z\) from U; its remaining
q-series and constant term are periodic. Thus \(U^2\) has translation
span contained in \(\operatorname{span}_{\mathbb C}\{1,U,U^2\}\),
and
\(\beta=\alpha_f U^2/144\) is admissible.

L3 therefore rules out the proposed comparison

\[
\alpha_f\ell^2-\alpha_f U^2/144
   =a\alpha_f+b\alpha_f\ell+dG
\]

for every admissible G. The same argument rules out replacing beta
by any finite sum of coordinates obtained from algebraic modular
units, finite-rank connections, or finite iterated integrals in the
stated frames. Adding an admissible correction to the Mellin
representative also does not help: it can be absorbed into beta.

This local obstruction occurs before integration. Passing to the
full ray to cancel both lower moments, or arranging algebraic
endpoint values for G, cannot repair a local identity that does not
exist.

## Why an unrestricted primitive does not evade the arithmetic problem

On a simply connected domain any holomorphic difference of the forms
has a primitive:

\[
G(z)=\int_{z_0}^z
 \bigl(\alpha_f\ell^2-\beta-a\alpha_f-b\alpha_f\ell\bigr).
\]

Such a G gives a tautological analytic identity. L3 proves that G
cannot belong to the finite class above. Moreover, where the
endpoint limits exist, its boundary difference is exactly the
unproved period difference (with the lower moments subtracted).
Requiring that boundary difference to vanish is the original scalar
comparison again, not new arithmetic information.

## Scope, fixed endpoint, and stop

**Endpoint:** neither FIN nor FORMULA. The result is **no-go
compression**: it eliminates a class of proposed proof mechanisms.

**Exact role in the BSD chain:** the unit connection gives \(P_u\);
its proposed local comparison with \(L''/2\) is now impossible in
this class. An independently proved scalar comparison, followed by
quantitative arithmeticity of \(P_u/(\Omega\operatorname{Reg})\),
would still give q=36 by the retained separation theorem. FIN and
order nine would still be needed for FORMULA.

**Not proved:** that \(P_u\ne L''/2\); that the leading term is not a
period of another object; that all mixed, derived, or motivic
identities fail; or that every common-B architecture is impossible.
A period identity on one specified path need not arise from a local
identity of differentials. A gauge outside the specified algebraic
class is also not covered merely by its name.

**Kill condition met:** retire this finite algebraic modulo-exact
comparison. The remaining one-path identity has no independent
proof or usable arithmeticity theorem in this task. It is not
promoted into a successor target. Any later route must pass the
difficulty-reduction gate using genuinely new mathematical input.
