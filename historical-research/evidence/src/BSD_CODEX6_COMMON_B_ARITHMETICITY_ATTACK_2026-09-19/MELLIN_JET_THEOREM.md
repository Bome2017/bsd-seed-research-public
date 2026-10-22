# The logarithmic Mellin jet: exact real realization and a scoped descent obstruction

Status: mathematical proofs using the retained modularity and analytic
rank-two inputs. These are not kernel certificates or novelty claims.
The construction is analytic and exists before FIN. It does **not**
construct a rational common certificate.

## 1. The actual candidate

Let \(f(z)=\sum_{n\geq1}a_n e^{2\pi inz}\) be the normalized weight-two
newform of E, so \(L(f,s)=L(E,s)\), and put

\[
\alpha_f=2\pi i f(z)\,dz,\qquad
\ell(z)=\log(-i\sqrt N z),\qquad
A_3=\mathbb C[\epsilon]/(\epsilon^3).
\]

On the upper half-plane use the holomorphic logarithm whose restriction
to the positive real axis is real; \(-iz\) has positive real part there.
The distinguished differential is the truncated Mellin jet

\[
\mathcal J_f=\alpha_f\left(1+\epsilon\ell+
                    \tfrac12\epsilon^2\ell^2\right).
\]

Its actual coefficient module is
\(\Omega^1_{\rm hol}(\mathfrak H)\otimes_{\mathbb C}A_3\), inside the
holomorphic de Rham complex on \(\mathfrak H\). This is infinite
dimensional over \(\mathbb C\). It is not a rational Selmer complex.
The real realization integrates the displayed differential on the
specified vertical ray. This construction uses neither Sha nor its order.

The proposed arithmetic upgrade was to put the literal coefficients
\(1,\ell,\ell^2\) into a finite rational local coefficient system on a
modular curve, then use its integral periods and arithmetic realization
to obtain B. Theorem M2 below kills that literal upgrade, including a
finite cover. It does not kill arbitrary corrected or derived objects.

## 2. M1: an exact leading-term period identity

Let \(\gamma\) be the oriented path from \(i\infty\) to \(i/\sqrt N\).
Then

\[
\boxed{\quad \int_\gamma \alpha_f\ell(z)^2=\frac{L''(E,1)}2.\quad} \tag{M1}
\]

Consequently, with the exact conventions in the contract,

\[
q=\frac{1}{\Omega R}\int_\gamma\alpha_f\ell^2
 =\frac{1}{c_E\Omega R}\int_\gamma\pi^*\omega_E\ell^2. \tag{M1a}
\]

Here \(\pi^*\omega_E=c_E\alpha_f\) is the retained modular
parametrization. Its power-of-two Manin factor is stated explicitly;
there is no change to the real regulator or period.

**Proof.** Define

\[
F(t)=f(it/\sqrt N),\qquad
\Lambda(s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s).
\]

Termwise integration in a right half-plane gives
\(\Lambda(s)=\int_0^\infty F(t)t^{s-1}dt\). Cusp decay at infinity,
and the Fricke transformation at zero, justify continuation and
differentiation of this integral near 1. Analytic order two and the
functional equation give root number +1; equivalently the weight-two
Fricke eigenvalue is -1. Hence
\(F(1/t)=t^2F(t)\). Substitution in the portion \(0<t<1\) gives

\[
\Lambda(1+u)=\int_1^\infty F(t)(t^u+t^{-u})\,dt.
\]

Thus
\[
\Lambda''(1)=2\int_1^\infty F(t)(\log t)^2\,dt
            =\frac{\sqrt N}{2\pi}L''(E,1).
\]
The last equality uses \(L(E,1)=L'(E,1)=0\); derivatives of the gamma
and conductor factors multiply these zeros. Finally the stated
orientation gives
\[
\int_\gamma\alpha_f\ell^2
=\frac{2\pi}{\sqrt N}\int_1^\infty F(t)(\log t)^2\,dt
=L''(E,1)/2.
\]
All differentiations are dominated by exponential cusp decay, with any
fixed power of \(\log t\). QED.

For completeness the integral of \(\mathcal J_f\) on the full ray
\(i\infty\to0\) is \((2\pi/\sqrt N)\Lambda(1+u)\), truncated at
order two in u and with u replaced by \(\epsilon\). Its \(\epsilon^2\)
coefficient is exactly \(L''(E,1)/2\). This is another description of
the same real scalar, not rationality of it.

## 3. M2: infinite translation orbit of the literal logarithmic weight

Let \(w>0\), \(c>0\), and \(P\in\mathbb C[X]\) be nonconstant. The
functions

\[
1,\quad P(\log(-ic(z+n w)))\quad(n\in\mathbb Z)
\]

are linearly independent on \(\mathfrak H\), in the sense that every
finite subcollection has no nontrivial linear relation.

**Proof.** In a putative finite relation choose one index n and let
\(z=-nw+iy\) with \(y\downarrow0\). Its logarithm is \(\log(cy)\),
which tends to \(-\infty\), so its nonconstant polynomial is unbounded.
For every other index m the logarithm has a finite limit, since
\(-ic((m-n)w+iy)\) tends to a nonzero point on the imaginary axis.
Every other term is bounded. The coefficient at n must therefore vanish.
Repeat at each index, and then the constant vanishes. QED.

The stronger version with arbitrary polynomials \(P_n\) of bounded
degree in a finite relation also holds: each nonconstant part must
vanish by the same boundary limit. Only the constants can cancel.

**Finite coefficient-system consequence.** Let \(f\ne0\) be a
weight-two modular form and let a finite-dimensional vector-valued
differential on \(\mathfrak H\) transform under a representation of a
finite-index subgroup of \(\Gamma_0(N)\) by constant matrices in a
flat trivialization. No fixed linear coordinate of this differential
can be

\[
\alpha_f P(\log(-ic z))
\]

for a nonconstant polynomial P.

Indeed such a subgroup contains a translation \(T^w:z\mapsto z+w\)
for some positive integer w. All translated coordinates would lie in
the span of finitely many component functions. But \(f(z+nw)=f(z)\),
so, after dividing by the nonzero function f on an open set and using
holomorphic continuation, M2 makes those coordinates linearly
independent. This is a contradiction.

In particular, adding finitely many literal coefficient functions cannot
repair \(\ell^2\). Replacing it by \(\ell^2+a\ell+b\) also fails.
That includes changes of the logarithm scale. The vanishing of the two
lower Mellin moments does not cancel the translation obstruction.

**Exact scope.** This proves nonexistence of the specified *literal
coordinate* realization. It does not prove that the number in (M1) is
not a period of some other finite object. It does not exclude adding
nontrivial automorphic correction terms, changing the integral by a
proved identity, derived realizations, mixed motives, non-flat gauges,
or exterior contractions. A descended representative modulo exact
forms would require a further construction, not merely M2.

## 4. M3: Tate characters have no nontrivial algebraic second jet

Let \(R_3=\mathbb Q[\epsilon]/(\epsilon^3)\). Any algebraic group
homomorphism

\[
\chi:\mathbb G_{m,R_3}\longrightarrow\mathbb G_{m,R_3}
\]

whose reduction modulo \(\epsilon\) is \(t\mapsto t^m\) is exactly
\(t\mapsto t^m\).

**Proof.** Its coordinate unit has the form
\(t^m(1+\epsilon a(t)+\epsilon^2 b(t))\), with a,b Laurent
polynomials over \(\mathbb Q\). Comparing the group law at first
order yields
\(a(xy)=a(x)+a(y)\). The only Laurent polynomial satisfying this is
zero: compare the coefficients of \(x^ny^n\) for \(n\ne0\), and
then the constant. The second-order law is then
\(b(xy)=b(x)+b(y)\), so b is zero too. QED.

Thus the analytic family \(t^{m+u}\), whose derivatives contain
\(\log t\), is not an algebraic infinitesimal family of Tate
characters over this ring. This gives a concrete reason that one
cannot obtain (M1a)'s arithmeticity merely by differentiating
critical-value algebraicity in a purported algebraic Tate-weight
family. It does not exclude logarithmic connections or Kummer
extensions; these are different constructions and still require the
specific height-determinant comparison.

In fact the rank-three logarithm connection itself is algebraic over Q:
on \(\mathbb G_m\), take \(\nabla=d-J\,dt/t\) with a rational
nilpotent matrix \(J^3=0\). Its horizontal solutions involve
\(\exp(J\log t)\). The obstruction is not the existence of that
connection. The proposed pullback uses the analytic function
\(t=-i\sqrt N z\), which is not invariant under \(z\mapsto z+1\)
and is not a function on the modular curve. M2 rules out repairing the
literal coordinate by finitely many flat coefficient functions. A
different gauge or period comparison is outside that assertion.

## 5. M4: the seed's half-ray dies in elliptic homology

With \(\gamma\) and \(\pi\) as above, the path \(\pi\circ\gamma\)
is a loop at the origin of E and is null-homotopic in the unpunctured
complex elliptic curve. Nevertheless,

\[
\int_\gamma\pi^*\omega_E\,\ell^2=c_E L''(E,1)/2\ne0.
\]

**Proof.** The same Fricke splitting with no logarithmic factor gives
\(\int_\gamma\alpha_f=L(E,1)/2=0\). Uniformization of the
parametrization normalized by \(\pi(i\infty)=O\) sends the terminal
point to the class of \(c_E\int_\gamma\alpha_f=0\) modulo the
period lattice. Hence the image path is a loop at O. Its lift to the
universal covering \(\mathbb C\to E(\mathbb C)\), starting at 0,
also ends at 0. Therefore it is null-homotopic (and in particular zero
in \(H_1(E(\mathbb C),\mathbb Z)\)). The weighted integral is nonzero
by M1 and the retained exact analytic order two. QED.

Thus **no linear functional on elliptic homology**, over any coefficient
field, can recover this logarithmic integral by evaluating the homology
class of the image half-ray. More generally a based, homotopy-invariant
holonomy construction for a flat connection on the unpunctured complex
elliptic curve has identity holonomy on this loop; its reduced value
cannot give the nonzero integral. This kills the specified factorization
through E. It does not address punctured curves, an enlarged modular
curve construction, arithmetic extensions, or a different period
identity. The path on X itself has distinct endpoints and is not being
misidentified as an absolute homology cycle on X.

## 6. Interface verdict and pivot

* **Defined before FIN:** the analytic jet and its path realization, yes.
* **Exact real identity:** (M1), yes.
* **Distinguished element of a finite rational arithmetic object:** not
  supplied. The literal finite coefficient-system proposal is killed
  by M2. The proposed algebraic Tate-character deformation is killed
  by M3. The direct factorization of the weighted half-ray through
  elliptic homology is killed by M4.
* **Integral arithmetic specializations / primary length bounds:** none
  constructed; this includes the three excluded bad primes.
* **Positive rational B:** not constructed. Naming the real quotient
  of (M1a) divided by four would only rename \(q/4\).

At the opening decision gate these failures triggered the arithmeticity
pivot. The rest of the task attacks quantitative rationality and
algebraicity and records exactly what information would still be
needed. No theorem rules out all common-B architectures.
