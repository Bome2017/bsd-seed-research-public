# The four divisor orbits and the local midpoint condition

**CANONICAL_FAMILY_REMAINS. The midpoint completion is unique only after imposing the additional condition (MC) in §5.**

The original Atkin–Lehner and constant-term conditions alone have an affine family of dimension **two over the field of meromorphic germs**. They do not select the old completion. The usual local newness and \(U_{4547}\)-eigenvector conditions do not select a completion either. A different, intrinsically defined local condition does: invariance under the maximal compact attached to the midpoint of the local level-\(4547^2\) lattice segment. It selects the middle orbits, with exact coefficients and residual in §6.

Uniqueness here includes (MC) as an explicit extra hypothesis. Neither the original symmetry requirements nor the conductor of the elliptic newform implies (MC). This result does not claim a uniquely mandatory choice among every possible extra normalization.

This is a written analytic/local-algebra calculation, with small exact algebra checks. No residual period was evaluated, set to zero, or used to choose coefficients. No real-height comparison or BSD endpoint is proved.

## 1. Scope and all four orbits

Use the series \(E(z,s)\), Fourier expansion, and ray normalization of the [preceding experiment](AUTOMORPHIC_SECOND_JET_EXPERIMENT.md), §§2–5. Put
\[
p=4547,\quad N=2^3\cdot3\cdot2243\cdot p^2\cdot5843,
\quad t=\sqrt N\,y.
\]
This classification concerns the divisor-scaling space
\[
V=\operatorname{span}_{\mathcal M}\{E(dz,s):d\mid N\},
\]
where \(\mathcal M\) is the field of meromorphic germs at \(s=0\). It is not a classification of all Eisenstein series with other inducing characters.

Define
\[
D_e=\{3^a2243^bp^{2c}5843^e:a,b,c,e\in\{0,1\}\},
\quad D_m=\{3^a2243^bp5843^e:a,b,e\in\{0,1\}\},
\]
\[
O_{e,0}=D_e\cup8D_e,\quad O_{e,1}=2D_e\cup4D_e,
\quad O_{m,0}=D_m\cup8D_m,\quad O_{m,1}=2D_m\cup4D_m.
\]
Let \(F_j=\sum_{d\in O_{e,j}}E(dz,s)\) and
\(G_j=\sum_{d\in O_{m,j}}E(dz,s)\).

**Lemma 1.** These are exactly the four orbits, and \(F_0,F_1,G_0,G_1\) are a basis of \(V^{\mathrm{AL}}\) over \(\mathcal M\).

**Proof.** The matrix identity in §3 of the preceding experiment gives
\[
W_Q:E(dz,s)\longmapsto E(d'z,s),\qquad
d'=Qd_R/d_Q,\quad d=d_Qd_R,\quad Q\parallel N.
\]
Thus each prime exponent is independently reflected in its conductor exponent. At 2 the two orbits are \(\{0,3\}\), \(\{1,2\}\); at \(p\) they are \(\{0,2\}\), \(\{1\}\); each remaining prime has one orbit \(\{0,1\}\). The four products above have sizes \(32,32,16,16\), exhausting all 96 divisors.

There are no linear dependencies hidden by this permutation description. Suppose a meromorphic linear combination of the \(E(dz,s)\) is zero, and choose its smallest divisor with nonzero coefficient. At that Fourier frequency, all smaller-divisor contributions vanish and its own first Fourier coefficient is a nonzero meromorphic function of \(s\) and \(y\). This is a contradiction. Equivalently, the Fourier-frequency matrix on divisors ordered increasingly is triangular with nonzero diagonal. Invariants in this permutation basis are exactly orbit sums.

At the single value \(s=0\), all \(E(dz,0)=1\). That specialization does not reduce the dimension of the space of meromorphic families. \(\square\)

The preceding report explicitly left other cusp combinations unclassified. This extends its two-orbit construction; it does not invalidate its identities. The inspected master §5.7 and preceding report contain neither this four-orbit classification nor (MC). This is a scoped collision check, not a literature novelty claim.

## 2. All normalized meromorphic families

Set
\[
r=r(s)=2^s+2^{-s}-1,\quad r_-=r(1-s),\quad D=r-r_-,
\]
\[
h=h(s)=p^s+p^{-s},\quad h_-=h(1-s),
\]
\[
B=B_1(s)=
(2^{s/2}+2^{-s/2})
\prod_{q\in\{3,2243,5843\}}(q^{s/2}+q^{-s/2}).
\]
The incoming divisor sums are
\[
B_0=rB,\quad B_1=B,\qquad A_0=hrB,\quad A_1=hB.
\]
In particular \(B(0)=16\), \(B'(0)=0\), \(D(0)=-1/2\), \(h(0)=2\).

For
\[
\mathcal E=u_0F_0+u_1F_1+v_0G_0+v_1G_1
\]
the constant term at infinity is
\[
C_{\rm in}(s)t^s+\varphi(s)C_{\rm sc}(s)t^{1-s},
\]
with
\[
C_{\rm in}=B\{h(ru_0+u_1)+rv_0+v_1\},
\tag{2.1}
\]
\[
C_{\rm sc}=B_1(1-s)\{h_-(r_-u_0+u_1)+r_-v_0+v_1\}.
\tag{2.2}
\]
Here \(C_{\rm sc}\) excludes the common factor \(\varphi(s)\). Vanishing with or without that factor is equivalent as a meromorphic identity, although \(\varphi(0)=0\). Merely evaluating the scattered term at zero would miss a constraint.

Define the old coefficients
\[
u_0^*=\frac1{hBD},\qquad u_1^*=-\frac{r_-}{hBD}.
\]
**Every** meromorphic solution of \(C_{\rm in}=1,\ C_{\rm sc}=0\) is
\[
\begin{pmatrix}u_0\\u_1\end{pmatrix}
=
\begin{pmatrix}u_0^*\\u_1^*\end{pmatrix}
+L(s)\begin{pmatrix}v_0\\v_1\end{pmatrix},
\quad (v_0,v_1)\in\mathcal M^2,
\tag{2.3}
\]
\[
L(s)=\frac1D
\begin{pmatrix}
r_-/h_- -r/h&1/h_- -1/h\\
rr_-(1/h-1/h_-)&r_-/h-r/h_-
\end{pmatrix}.
\tag{2.4}
\]
Indeed, divide (2.1) by \(Bh\) and (2.2) by \(B_1(1-s)h_-\), and solve the two equations with row vectors \((r,1)\), \((r_-,1)\). Their determinant is \(D\ne0\) near zero. All entries of \(L\) are holomorphic there. This proves both completeness and the affine dimension two.

For later use, define the homogeneous families
\[
K_j=G_j+L_{0j}F_0+L_{1j}F_1,\qquad j=0,1.
\tag{2.5}
\]
Then
\[
\mathcal E_{\mathbf v}=\mathcal E_*+v_0K_0+v_1K_1,
\tag{2.6}
\]
and each \(K_j\) has identically zero incoming and scattered terms at infinity.

## 3. Meromorphic coefficients versus a genuine second jet

Let \(\mathcal O\) denote holomorphic germs at zero and put \(P=p+p^{-1}\). Evaluation of (2.4) gives
\[
L(0)=
\begin{pmatrix}
1-3/P&1-2/P\\
-3/2+3/P&-3/2+2/P
\end{pmatrix}.
\tag{3.1}
\]
Since each column sums to \(-1/2\), \(K_j(z,0)=16-32/2=0\).

Their first jets are linearly independent. To see this, write \(\mathscr F(dz,s)\) for the nonconstant Fourier part of \(E(dz,s)\). Since the constant terms of \(K_j\) vanish identically and \(\mathscr F(dz,0)=0\),
\[
K_j'(z,0)=
\sum_{d\in O_{m,j}}\mathscr F'(dz,0)
+L_{0j}(0)\sum_{d\in O_{e,0}}\mathscr F'(dz,0)
+L_{1j}(0)\sum_{d\in O_{e,1}}\mathscr F'(dz,0).
\]
The functions \(\mathscr F'(dz,0)\) are independent by the same smallest-frequency argument as in Lemma 1: their first coefficients are nonzero. The two middle-orbit coordinates of \(K_0',K_1'\) are the two standard basis vectors. Consequently no nonzero constant combination of these two jets vanishes.

It follows that
\[
\boxed{\mathcal E_{\mathbf v}\text{ is holomorphic at }0
\quad\Longleftrightarrow\quad
(v_0,v_1)\in s^{-1}\mathcal O^2.}
\tag{3.2}
\]
For the forward direction, if the largest pole order of \(v_0,v_1\) were \(k\ge2\), their leading coefficients would produce a nonzero term of order \(s^{1-k}\) by the independence just proved. Conversely, simple poles multiply families vanishing at least to order one. Thus all meromorphic solutions have been classified, including precisely which have an ordinary second jet. Higher-pole solutions have no such jet; no finite-part convention is imposed.

Write an admissible pair as
\[
v_j(s)=a_{j,-1}s^{-1}+a_{j,0}+a_{j,1}s+O(s^2).
\]
Then \(\mathcal E_{\mathbf v}(z,0)=1+\sum_j a_{j,-1}K_j'(z,0)\).
If the extra normalization \(\mathcal E_{\mathbf v}(z,0)=1\) is required,
independence forces both residues to vanish. Thus that additional normalization
restricts the family to holomorphic coefficient germs.

Then the full residual is exactly
\[
\boxed{
R_{N,\mathbf v}=R_*+
\sum_{j=0}^1\left\{
\frac{a_{j,-1}}3 K_j'''(z,0)
+a_{j,0}K_j''(z,0)+2a_{j,1}K_j'(z,0)
\right\}.}
\tag{3.3}
\]
The factor \(1/3\) comes from \(2!\,[s^2](s^{-1}K_j)\). Holomorphic coefficient families have \(a_{j,-1}=0\). The ordinary second jet of a general regular family thus depends on at most six Laurent coefficients, not on arbitrarily many coefficients of the two free germs.

Here is a direct Fourier specification for (3.3), also covering the simple-pole case. Set \(w_d=u_j\) on \(O_{e,j}\) and \(w_d=v_j\) on \(O_{m,j}\), and write
\[
w_d(s)=w_{d,-1}/s+w_{d,0}+w_{d,1}s+O(s^2).
\]
Then
\[
R_{N,\mathbf v}(z)=
\sum_{d\mid N}\left\{
\frac{w_{d,-1}}3\mathscr F'''(dz,0)
+w_{d,0}\mathscr F''(dz,0)
+2w_{d,1}\mathscr F'(dz,0)\right\}.
\tag{3.4}
\]
All terms in this expression are specified by the Fourier series of the preceding experiment. More explicitly, use its
\[
\kappa=\log(4\pi)-\gamma_{\rm E},\quad
S_n=\sum_{a\mid n}a,\quad T_n=\sum_{a\mid n}a\log a,
\]
\[
h_n(v)=\kappa-\log n+2T_n/S_n+e^{4\pi nv}E_1(4\pi nv).
\]
On the ray,
\[
\mathscr F'(iv,0)=-4\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi nv},
\quad
\mathscr F''(iv,0)=8\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi nv}h_n(v).
\tag{3.5}
\]
If a residue is present in (3.4), the required third jet is explicit as well. Put
\[
Q_n(v,s)=n^{s-1/2}\sigma_{1-2s}(n)K_{s-1/2}(2\pi nv),
\quad
a_3=\frac{\pi^2}{6}-\kappa^2-4\log^2(2\pi)-8\zeta''(0).
\]
Taylor expansion of \(1/Z(s)\) gives
\[
1/Z(s)=-2s+2\kappa s^2+a_3s^3+O(s^4),
\]
and hence
\[
\mathscr F'''(iv,0)=24\sqrt v\sum_{n\ge1}
\{-Q_n''(v,0)+2\kappa Q_n'(v,0)+a_3Q_n(v,0)\}.
\tag{3.6}
\]
The derivatives in (3.6) use only the finite divisor sum and the explicit convergent integral
\[
K_\nu(x)=\int_0^\infty e^{-x\cosh u}\cosh(\nu u)\,du.
\]
Order derivatives are obtained by differentiating \(\cosh(\nu u)\), so (3.6) contains no unspecified spectral or arithmetic term. Off the ray insert \(\cos(2\pi ndx)\) in the Fourier terms for \(\mathscr F(dz,s)\).

In particular, for holomorphic coefficient quadruples, (3.4) simplifies to
\[
R_{N,\mathbf v}(iy)=
8\sum_{d\mid N}\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi ndy}
\{w_d(0)h_n(dy)-w_d'(0)\}.
\tag{3.7}
\]

For every regular family,
\[
\mathcal E_{\mathbf v}''(z,0)=\log^2(\sqrt N y)+R_{N,\mathbf v}(z),
\]
\[
\boxed{
\int_\gamma\alpha_f\,\mathcal E_{\mathbf v}''(z,0)
=M_2+\Delta(\mathbf v),\qquad
\Delta(\mathbf v)=2\pi\int_{N^{-1/2}}^\infty
f(iy)R_{N,\mathbf v}(iy)\,dy.}
\tag{3.8}
\]
Equivalently, if \(I_{j,k}=\int_\gamma\alpha_f K_j^{(k)}(z,0)\), then
\[
\Delta(\mathbf v)=\Delta_*+
\sum_{j=0}^1\{a_{j,-1}I_{j,3}/3+a_{j,0}I_{j,2}
+2a_{j,1}I_{j,1}\}.
\tag{3.9}
\]
These are derived Fourier-period formulas, not conditions imposed on the free parameters. The Fourier series and their finitely many derivatives converge on \(y\ge N^{-1/2}>0\); cusp decay of \(f\) justifies these integrations. No value or nonvanishing of any period in (3.8)–(3.9) is asserted.

## 4. What local newness and the U operator actually do

At \(p\), suppress the other divisor factors and write
\[
e_j(z,s)=E(p^jz,s),\qquad j=0,1,2.
\]
These are translates of the unramified spherical Eisenstein family. The elliptic newform's conductor exponent two does not make this different local representation ramified.

The level-\(p\) divisor space is spanned by \(e_0,e_1\). Its two degeneracy images at level \(p^2\) span
\[
\operatorname{span}\{e_0,e_1\}+\operatorname{span}\{e_1,e_2\}
=\operatorname{span}\{e_0,e_1,e_2\}.
\]
Thus the entire space under consideration is old at \(p\); its new quotient is zero. A nonzero \(p^2\)-new vector cannot be selected from it.

For an explicit operator test, use
\[
(U_pg)(z)=\frac1p\sum_{a=0}^{p-1}g((z+a)/p).
\]
Periodicity gives \(U_pe_1=e_0,\ U_pe_2=e_1\). The level-one identity
\[
\sum_{a=0}^{p-1}E((z+a)/p,s)+E(pz,s)
=(p^s+p^{1-s})E(z,s)
\]
follows directly from the constant terms and the divisor-sum recurrence
\(\sigma_k(pn)=(1+p^k)\sigma_k(n)-p^k\sigma_k(n/p)\),
with the last sum zero when \(p\nmid n\). Consequently
\[
U_pe_0=(p^{s-1}+p^{-s})e_0-p^{-1}e_1.
\tag{4.1}
\]
Atkin–Lehner symmetry at \(p^2\) requires a vector
\(A(e_0+e_2)+Be_1\). Its image under \(U_p\) is
\[
\{(p^{s-1}+p^{-s})A+B\}e_0+(1-p^{-1})Ae_1.
\]
If this were \(\lambda\{A(e_0+e_2)+Be_1\}\), comparison at \(e_2\) gives \(\lambda A=0\). If \(\lambda\ne0\), comparison at \(e_0\) then forces \(B=0\). If \(\lambda=0\), comparison at \(e_1\) first forces \(A=0\), then \(B=0\).

Therefore **no nonzero fully symmetric family in this space is a \(U_p\)-eigenvector**, for any meromorphic eigenvalue, including zero. The same proof works with the other-prime coefficient space as spectator. Rescaling \(U_p\) does not alter this conclusion.

## 5. An intrinsic extra local condition that does select a line

There is nevertheless a local geometric datum at a square level that does not require a newvector of conductor \(p^2\). The level group fixes the two endpoint lattice classes
\[
\Lambda_0=\mathbf Z_p e_1\oplus\mathbf Z_p e_2,\qquad
\Lambda_2=\mathbf Z_p e_1\oplus p^2\mathbf Z_p e_2.
\]
Their length-two lattice segment has a unique midpoint
\[
\Lambda_1=\mathbf Z_p e_1\oplus p\mathbf Z_p e_2.
\]
For an elementary description, modulo \(p^2\) the quotient
\(\Lambda_0/\Lambda_2\) is cyclic of order \(p^2\); its unique subgroup of order \(p\) determines this intermediate lattice. Thus the midpoint is fixed by exchanging the endpoints; it does not depend on an orientation or on any period.

Let \(K=\mathrm{GL}_2(\mathbf Z_p)\), \(D_p=\operatorname{diag}(p,1)\), and
\[
K_{\rm mid}=D_p^{-1}KD_p.
\]
Up to central homothety this is the maximal compact stabilizing the midpoint. It contains \(K_0(p^2)\): conjugating a matrix whose lower-left entry is divisible by \(p^2\) by \(D_p\) gives an integral invertible matrix. The local Fricke matrix \(W=\left(\begin{smallmatrix}0&-1\\p^2&0\end{smallmatrix}\right)\) satisfies
\[
D_pWD_p^{-1}
=p\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
It therefore preserves the midpoint, and acts trivially on its spherical line in this trivial-central-character family.

The additional condition is
\[
\boxed{\text{(MC): the local Eisenstein section at }p
\text{ is fixed by }K_{\rm mid}
\text{ as a meromorphic family.}}
\]
This condition is independently defined by the local level segment. Its one-dimensional fixed space follows directly from unramified induction: in the level-one principal-series model, the Iwasawa decomposition \(G=BK\) determines a right-\(K\)-invariant section by its value at the identity, since the inducing characters are unramified. Conjugation gives a one-dimensional \(K_{\rm mid}\)-fixed space. In the present classical realization its generator is \(e_1=E(pz,s)\).

There is also a direct check within our exact finite-dimensional space, avoiding any issue at the reducible specialization \(s=0\). The midpoint group contains the translation \(\left(\begin{smallmatrix}1&1/p\\0&1\end{smallmatrix}\right)\). Thus (MC) implies
\[
\mathcal E(z+1/p,s)=\mathcal E(z,s).
\tag{5.1}
\]
The Fourier coefficient at frequency 1 in the general family forces \(u_0=0\). Frequency 2 then forces \(u_1=0\). These deductions hold as meromorphic identities, not just after specializing at zero. Conversely, every middle-orbit term \(E(pd'z,s)\), \(p\nmid d'\), is a midpoint spherical translate and satisfies (5.1). Thus within the classified space,
\[
\text{(MC)}\quad\Longleftrightarrow\quad u_0=u_1=0.
\tag{5.2}
\]

This derives an applicable local selection condition; it does not transfer a property of the ramified elliptic newform to the Eisenstein family. Nor does it assert that (MC) follows from the original two constant-term conditions. For example, symmetrizing the endpoint spherical line instead gives \(e_0+e_2\), a different natural convention recovering the old completion. The unique midpoint supplies the particular extra condition specified here, without consulting \(\Delta\).

## 6. The uniquely normalized midpoint completion and its residual

Combining (5.2) with (2.1)–(2.2) gives the unique family satisfying (MC):
\[
\boxed{
\mathcal E_{\rm mid}(z,s)=
\frac{G_0(z,s)-r(1-s)G_1(z,s)}
{B_1(s)[r(s)-r(1-s)]}.}
\tag{6.1}
\]
Thus \(u_0=u_1=0\), \(v_0=1/(BD)\), \(v_1=-r_-/(BD)\). These coefficients are regular at zero and
\[
v_0(0)=-1/8,\quad v_1(0)=3/16,\qquad
v_0'(0)=-3\log2/8,\quad v_1'(0)=3\log2/8.
\tag{6.2}
\]
The normalization remains \(s_0=0\), \(A=1\), with constant term exactly \(t^s\).

As another exact description, put \(M=N/p^2\) and
\[
H_j(w,s)=\sum_{d\in O_{m,j}}E((d/p)w,s),\qquad
\mathcal C_M(w,s)=\frac{H_0(w,s)-r_-H_1(w,s)}{BD}.
\]
Then
\[
\mathcal E_{\rm mid}(z,s)=\mathcal C_M(pz,s),\qquad
\mathcal E_*(z,s)=
\frac{\mathcal C_M(z,s)+\mathcal C_M(p^2z,s)}{p^s+p^{-s}}.
\tag{6.3}
\]
This identifies both choices independently of \(f\): the first uses the midpoint, the second symmetrizes the endpoints.

Substituting (6.2) into (3.7) yields
\[
\boxed{\begin{aligned}
R_{\rm mid}(iy)={}&
\sum_{d\in O_{m,0}}\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi ndy}
\{-h_n(dy)+3\log2\}\\
&+\sum_{d\in O_{m,1}}\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi ndy}
\{3h_n(dy)/2-3\log2\}.
\end{aligned}}
\tag{6.4}
\]
Off the ray insert the Fourier cosines. In particular,
\[
\boxed{\int_\gamma\alpha_f\,\mathcal E_{\rm mid}''(z,0)
=\frac{L''(E,1)}2+\Delta_{\rm mid},\quad
\Delta_{\rm mid}=\int_\gamma\alpha_f R_{\rm mid}(z).}
\tag{6.5}
\]

All Fourier frequencies of \(R_{\rm mid}\) are divisible by \(p\). Its coefficient at frequency \(p\) is
\[
e^{-2\pi py}\{-\kappa-e^{4\pi py}E_1(4\pi py)+3\log2\},
\]
which is not identically zero as a function of \(y\). Thus this normalization changes the Fourier correction and does not cancel it pointwise. This proves neither vanishing nor nonvanishing of its period. The old residual period and this new one are both unevaluated.

## 7. Exact extent of the result

The four orbit sizes and complement action were enumerated over all 96 divisors; the two homogeneous columns at zero were checked with exact rational arithmetic. Symbolic algebra verified both constant-term equations for (2.3)–(2.4) and their midpoint specialization. A numerical derivative check corroborated the Taylor coefficient \(a_3\); it did not evaluate a period. The general identities follow from the derivations above, not from numerical checks. This report is not a formal proof-assistant or independent-referee certificate.

The preceding experiment's two-orbit section remains valid. Its uniqueness within the full divisor-scaling space would be false; it did not claim that uniqueness. The full normalized meromorphic family, the regularity restriction needed for its second jets, and the midpoint condition are the additional results here.

The endpoint effect is the exact analytic identity (6.5) for an independently selected completion, together with the classification (2.3). No residual period has been shown to disappear, and no comparison with \(\det(\langle P_i,P_j\rangle_{\rm NT})\) follows. No successor or arithmetic-intersection operation is begun.
