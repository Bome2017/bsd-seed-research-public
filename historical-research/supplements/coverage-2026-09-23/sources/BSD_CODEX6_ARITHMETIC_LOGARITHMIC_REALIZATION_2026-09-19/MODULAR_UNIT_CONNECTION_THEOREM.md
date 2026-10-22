# L2: an actual algebraic modular-unit connection, with its exact missing comparison

This constructs the object proposed by the user on the punctured modular
curve. It does not identify its period with M1 and does not establish
algebraicity of the normalized leading term. All constructions precede FIN.

Let \(X=X_0(N)/\mathbb Q\), let D be the cusp divisor, and let
\(Y=X\setminus D\). The unchanged N is
\(2^3\cdot3\cdot2243\cdot4547^2\cdot5843\).
Write \(q_z=e^{2\pi iz}\), to distinguish the cusp parameter from
\(q_\infty\). Use

\[
\Delta(z)=q_z\prod_{n\ge1}(1-q_z^n)^{24},\qquad
u_N(z)=N^6\frac{\Delta(Nz)}{\Delta(z)}.
\]

The discriminant transformation and eta-product formulas are the
standard inputs. Their analytic normalization was checked against
[DLMF 23.17.8](https://dlmf.nist.gov/23.17#E8) and
[23.18.5](https://dlmf.nist.gov/23.18#E5); DLMF uses the nome
\(e^{\pi iz}\), whose square is our \(q_z\).

## L2a. The unit and its rationality/Fricke normalization

The function \(u_N\) belongs to \(\mathbb Q(Y)^\times\), with divisor
supported on D, and

\[
u_N(W_Nz)=u_N(z)^{-1},\qquad W_Nz=-1/(Nz).
\]

**Proof.** If \(\gamma=\left(\begin{smallmatrix}a&b\\Nc&d\end{smallmatrix}\right)\)
is in \(\Gamma_0(N)\), the matrix
\(\left(\begin{smallmatrix}a&Nb\\c&d\end{smallmatrix}\right)\) is in
\(\mathrm{SL}_2(\mathbb Z)\). Applying the weight-twelve transformation
to numerator and denominator proves invariance of their ratio. Both
discriminants have no zeros on the upper half-plane, and their
meromorphic extensions have divisors at cusps. Thus the ratio is a
modular unit.

Its definition over Q can also be seen without assigning arithmeticity
to an analytic period. For a cyclic isogeny \(\phi:E\to E/C\), choose
\(\omega'\) so that \(\phi^*\omega'=\omega\). The ratio of algebraic
discriminants
\(\Delta(E/C,\omega')/\Delta(E,\omega)\) is independent of scaling
omega and is defined over Q on the moduli problem. For
\(E_z=\mathbb C/(\mathbb Z+z\mathbb Z)\) and
\(C=\langle1/N\rangle\), its analytic value is
\(N^{12}\Delta(Nz)/\Delta(z)\): the isogeny is induced by
\(w\mapsto Nw\), and the target differential normalized by pullback
is \(dw/N\). Multiplication by \(N^{-6}\) gives precisely u_N.
This invariant weight-zero function descends to the coarse modular
curve. The standard modular moduli interpretation and algebraic
discriminant scaling are the algebraic inputs here.

Finally,
\(\Delta(-1/z)=z^{12}\Delta(z)\) gives

\[
\frac{\Delta(NW_Nz)}{\Delta(W_Nz)}
 =N^{-12}\frac{\Delta(z)}{\Delta(Nz)},
\]

which proves the asserted reciprocal identity. QED.

Let b be the point represented by \(z_0=i/\sqrt N\). It is algebraic:
it lies in the finite fixed locus of the nonidentity Q-defined
involution W_N on X. The involution is not the identity since it
interchanges the distinct cusps 0 and infinity. Thus the base field
needed for the marked point is the finite field \(K=\mathbb Q(b)\);
no degree bound for K is asserted or computed. On the imaginary axis
\(\Delta(iy)>0\), so \(u_N(z_0)=1\), with the positive sign selected
from the reciprocal identity.

Let \(U(z)=\log u_N(z)\) be the branch real on that axis with U(b)=0.
In the centered variable \(t=\sqrt N y\), it satisfies
\(U(i/(\sqrt N t))=-U(it/\sqrt N)\).

## L2b. Connections and the exact iterated period

The differential \(\omega_u=du_N/u_N\) is a Q-defined logarithmic
form on (X,D), with residue \(\operatorname{ord}_c(u_N)\in\mathbb Z\)
at each geometric cusp c. The rank-three connection
\(d-J\omega_u\), with \(J^3=0\) the standard lower Jordan block,
has horizontal column \((1,U,U^2/2)^t\) on the chosen lift.

To record the required integral against the elliptic differential,
use the **rank-four** connection on \(\mathcal O_X^4\)

\[
\nabla=d-A,\qquad
A=\begin{pmatrix}
0&0&0&0\\
\omega_u&0&0&0\\
0&\omega_u&0&0\\
0&0&\alpha_f&0
\end{pmatrix},\qquad
\alpha_f=\pi^*\omega_E/c_E.
\]

The retained modular parametrization makes alpha_f a Q-defined
holomorphic differential on X. Therefore this is an explicit Q-defined
logarithmic connection. It is integrable since algebraic two-forms on
a smooth curve vanish. Its filtration is unipotent, and its cusp
residues are nilpotent. No Sha group enters its definition.

The solution with initial column \((1,0,0,0)^t\) at b is

\[
s(z)=\left(1,U(z),\frac{U(z)^2}{2},V(z)\right)^t,
\qquad
V(z)=\int_b^z\alpha_f\,\frac{U^2}{2}.
\]

This defines the concrete candidate period

\[
\boxed{P_u=\frac1{144}\int_\gamma\alpha_f U^2
             =-\frac1{72}\lim_{z\to i\infty}V(z).} \tag{U}
\]

The limit in (U) converges: at infinity
\(U=6\log N+(N-1)\log q_z+O(q_z)\), whereas alpha_f has cusp decay.
Hence its integrand is bounded by a polynomial in y times
\(e^{-2\pi y}dy\). This is a convergent component, not an unspecified
regularized number. The branch, algebraic endpoint b, and orientation
are fixed. The rational factor 144 is a normalization choice motivated
by the weight twelve; it is not an inferred analytic equality.

Fricke symmetry gives
\(\int_\delta\alpha_f U^2=2\int_\gamma\alpha_f U^2\) and
\(\int_\delta\alpha_f U=0\). It supplies no equality between U and
the Mellin logarithm ell. At the cusp, U grows linearly in y while
ell grows as log y, so literal equality modulo constants already fails.

## Required comparison and endpoint gate

The first necessary comparison is

\[
P_u\stackrel{?}=H_2=\frac{L''(E,1)}2. \tag{U-M}
\]

The proposed local de Rham proof would require
\(\alpha_f\ell^2-\alpha_f U^2/144\) to be a constant lower Mellin
combination plus an admissible exact term. L3 proves this impossible
when the exact primitive also comes from finite algebraic connections
or finite iterated periods. An equality (U-M) solely for this one path
is not disproved, but has not been proved.

Even (U-M) would need an independent theorem putting
\(P_u/(\Omega\operatorname{Reg})\) in Q with bounded denominator,
or in a number field with the required conjugate control. No such
theorem is supplied by the connection's existence. There is no
specialization from this construction to primary Sha lengths.

**Endpoint:** neither branch closes upon construction. **Full intended
chain:** (U-M) plus quantitative arithmeticity implies q=36; adding
finite Sha of order nine gives FORMULA. **Still missing:** all those
additional arrows. **Kill condition triggered:** the admissible de Rham
bridge fails, and pursuing a bare scalar equality would leave both
the comparison and arithmeticity unsupported. The branch is stopped.
