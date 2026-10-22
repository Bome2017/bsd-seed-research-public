# Quantitative algebraicity: a sharp small-degree certificate and a local-data obstruction

These are new deductions in this task, with elementary proofs. They are
not assertions that the seed's q is algebraic, integral, or of degree two.
No novelty claim is made. Let \(\varepsilon=573/100000\).

## A1. A sharp trace certificate in degree at most two

Suppose a real number x satisfies

1. \(|x-36|<\varepsilon\);
2. x is a totally positive algebraic integer of degree at most two;
3. if its degree is two, \(\operatorname{Tr}_{\mathbb Q(x)/\mathbb Q}(x)\le246\).

Then \(x=36\).

**Proof.** If the degree is one, x is an integer and the interval already
gives the assertion. Otherwise write \(x=36+\delta\), let y be its other
conjugate, and let \(s=x+y\in\mathbb Z\) be its trace. Total positivity
implies \(s>x>35.99427\), so \(36\le s\le246\). Therefore

\[
|36-y|=|72-s+\delta|\le174+\varepsilon.
\]

If f is the monic irreducible polynomial of x, then f(36) is a nonzero
integer, whereas

\[
|f(36)|=|36-x||36-y|
 <\varepsilon(174+\varepsilon)<1.
\]

The final inequality is exact; its rational value is recorded in
`EXACT_CHECKS.json`. This is a contradiction. QED.

**Sharpness of 246 in this format.** The two roots of

\[
f(X)=X^2-247X+7595=(X-36)^2-175(X-36)-1
\]

are positive algebraic integers of degree two. The smaller one is

\[
x_0=36+\frac{175-\sqrt{175^2+4}}2
   =36-\frac{2}{175+\sqrt{175^2+4}}.
\]

It belongs to \((36-1/175,36)\), and \(1/175<\varepsilon\).
The discriminant lies strictly between \(175^2\) and \(176^2\), so the
polynomial is irreducible over \(\mathbb Q\). Both roots are positive
(positive sum 247 and product 7595), and their trace is 247. Thus replacing
246 by 247 makes the certificate false.

This is a usable alternative *if its arithmetic hypotheses can be
established*: it requires no rationality assertion and uses a trace bound
rather than the explicit list of conjugates. None of those new arithmetic
hypotheses is known for the seed's q in this task. The real Neron--Tate
height matrix is not a proof of this algebraic trace bound.

## A2. Quadratic integral counterexamples with any prescribed finite p-adic precision

Let \(\eta>0\), let \(\mathcal P\) be a finite set of rational primes,
and prescribe integers \(k_p\ge1\). There is a totally positive real
quadratic algebraic integer x, different from 36, such that

\[
0<x-36<\eta
\]

and for each \(p\in\mathcal P\) there is an embedding
\(\mathbb Q(x)\hookrightarrow\mathbb Q_p\) under which

\[
v_p(x-36)=k_p.
\]

As an algebraic integer, x is integral at **all** finite places of its
number field, not only the chosen embeddings. The embeddings in the
display are explicitly existential and need not be the other p-adic
conjugate as well.

**Proof.** Set \(T=\prod_{p\in\mathcal P}p^{k_p}\), taking T=1 when
the set is empty. Choose an integer M coprime to T and large enough that

\[
M>2T+1,\qquad M>2T/\eta.
\]

There are arbitrarily large such M, for example in the residue class 1
modulo the product of the primes. Consider

\[
g(Y)=Y^2-MY+T,\qquad f(X)=g(X-36).
\]

Its discriminant \(M^2-4T\) lies strictly between \((M-1)^2\) and
\(M^2\), and hence is positive and nonsquare. Thus f is monic and
irreducible. Its smaller shifted root is

\[
\delta=\frac{M-\sqrt{M^2-4T}}2
       =\frac{2T}{M+\sqrt{M^2-4T}},\qquad 0<\delta<2T/M<\eta.
\]

Take x=36+delta. Its other conjugate is 36+M-delta, which is positive
because both roots of g are positive. At a prescribed prime p,
\(g(0)\equiv0\pmod p\) and \(g'(0)=-M\) is a p-adic unit. Hensel's
lemma supplies a root \(\delta_p\in p\mathbb Z_p\). Since
\(\delta_p(M-\delta_p)=T\), the factor \(M-\delta_p\) is a unit,
and \(v_p(\delta_p)=v_p(T)=k_p\). Sending x to 36+delta_p defines the
required embedding. QED.

The decisive quantitative identity for this example is

\[
|x-36|\,|36-x'|=\delta(M-\delta)=T\ge1.
\]

Thus the leading coefficient is already 1 and the distinguished root is
arbitrarily close to 36, but the other conjugate necessarily escapes far
enough to defeat the predecessor's separation criterion. No number of
finite congruences repairs the missing conjugate bound.

This disproves the proposed inference from the following *abstract
collection of properties*: small real error, degree two, algebraic
integrality at every finite place, total positivity, and arbitrary finite
p-adic precision at selected embeddings. It is not a counterexample to
BSD or a claim that these numbers are L-value quotients.

## A3. What has to be supplied for the actual scalar

The predecessor's general norm criterion remains the right exact target:
for the primitive irreducible polynomial of q, with leading coefficient a,

\[
C=|a|\prod_{j>1}|36-q_j|<1/\varepsilon=100000/573
\]

suffices. A weak inequality \(C\le C_0\) with
\(\varepsilon C_0<1\) also suffices. In degree one this is precisely
the reduced-denominator certificate, so these formats are not pairwise
logically incomparable. A1 is an explicit sufficient way to control C
in a special algebraic case. A2 shows why finite-place integrality and
precision cannot replace this control.

No proof of algebraicity, a denominator bound, or the trace bound for q
was obtained. Increasing analytic precision without an established
arithmetic bound would not close that gap.
