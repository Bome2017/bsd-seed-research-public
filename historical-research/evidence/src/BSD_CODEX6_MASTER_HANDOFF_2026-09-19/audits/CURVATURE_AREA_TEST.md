# The curvature-area pairing and its exact vanishing class

**BROAD_CURVATURE_ORTHOGONALITY_THEOREM.**

For the actual midpoint jet, the absolutely convergent full-domain pairing is
\[
\boxed{\mathcal A=\int_{Y_0(N)}\alpha_f\wedge dJ=0.}
\tag{1}
\]
The curvature remains nonzero as a differential form. Its integral vanishes because it is the differential of a global one-form with zero cusp boundary flux. This proves a broader statement than orthogonality caused by the missing multiples of 4547: every smooth, automorphic **scalar function** with moderate growth of its first derivatives has this vanishing pairing with every holomorphic weight-two cusp form. No Fourier-support hypothesis is needed for the full-domain theorem.

The original cusp-to-cusp path does not bound a relative two-chain on the modular curve. The vanishing of its one chosen differential period is not a homology relation. Both points are proved below, together with the Fourier signs, the Eisenstein unfolding, and the exact limit of a two-variable change.

## 1. Inputs, scope, and the new implication

Use the fixed level \(N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843\), \(p=4547\), and the existing midpoint section. Set
\[
X=X_0(N)(\mathbf C),\quad S=X\setminus Y_0(N),\quad
\alpha=2\pi i f(z)\,dz,\quad
J(z)=\mathcal E_{\rm mid}''(z,0),\quad L=\log(\sqrt N y).
\]
Here \(J\), rather than \(R_{\rm mid}=J-L^2\), is the automorphic scalar function. The [Green-kernel report](MIDPOINT_GREEN_KERNEL_TEST.md) proves its reality, its explicit Fourier expansion, and its differentiated Eisenstein identity. The [secondary-descent report](MIDPOINT_SECONDARY_DESCENT_TEST.md) proves
\[
\Omega=d(-J\alpha)=\alpha\wedge dJ\ne0.
\tag{2}
\]
The [local trace report](MIDPOINT_UP_TRACE_TEST.md) supplies \(a_{pn}=0\). The [classification](AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md) specifies the finite divisor-scaled Eisenstein family defining \(J\).

The collision check covered current master §5.7, its automorphic/midpoint/secondary reports, and the two linked Mellin and logarithmic-realization folders. These contain nonclosedness, cusp nonextension, and one-dimensional period obstructions, but no full modular-domain curvature integral or its vanishing theorem. This is an addition to the project record using elementary integration and unfolding, not a claim of a new general principle in the literature. Neither positive residual certificate is changed.

The exact new implication is: replacing the ray functional by the unweighted full-domain integral in (1) annihilates the entire moderate-growth scalar-jet class, including both vertex sections and the regular members of the classified family. It supplies no nonzero arithmetic comparison with a real height determinant.

## 2. Relative homology: the path does not bound

Orient \(c=\{0,\infty\}\) from 0 to infinity. The opposite orientation used for some previous integrals only changes signs. The long exact sequence of the pair \((X,S)\) contains
\[
0\longrightarrow H_1(X;\mathbf Z)\longrightarrow H_1(X,S;\mathbf Z)
\xrightarrow{\partial}\widetilde H_0(S;\mathbf Z)\longrightarrow0,
\]
and
\[
\boxed{\partial[c]=[\infty]-[0]\ne0.}
\tag{3}
\]
The cusps are distinct: if an element of \(\Gamma_0(N)\) sent infinity to zero, its upper-left entry would be zero, and determinant one would force its lower-left entry to be \(\pm1\), contradicting its divisibility by \(N>1\).

Thus \([c]\) has infinite order in relative homology, and no relative two-chain has boundary \(c\). This conclusion also holds with rational or complex coefficients. Adding chains supported at the cusps cannot change the connecting boundary in (3). Closing the path with some other path introduces an additional boundary integral; it does not supply a filling of the original relative class alone.

For the present form, the retained Mellin identity gives
\(\int_c\alpha=-L(f,1)=0\). This is one linear functional vanishing on a nonzero relative class. It does not imply \([c]=0\), even though the path's image on the elliptic quotient has the separate null-homotopy proved in the earlier report. A filling downstairs cannot be lifted to a filling upstairs by this argument.

## 3. The antiholomorphic derivative, including every Fourier sign

Write \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\); thus
\(\bar\partial J=(\partial_{\bar z}J)d\bar z\). Put
\[
h_J=\mathscr D_zJ=\frac1{2\pi i}\partial_zJ.
\]
Because \(J\) is real, the existing differentiated identity gives
\[
\boxed{\partial_{\bar z}J
=-\pi i\sum_{d\in\mathcal O}d
\left[b_d\overline{\mathsf E_2'(dz,1)}
 +(\kappa b_d+e_d)\overline{\mathsf E_2(dz,1)}\right]
=-2\pi i\,\overline{h_J}.}
\tag{4}
\]
The conjugation changes the sign of \(i\). A prime on \(\mathsf E_2\) is a parameter derivative. All coefficients \(b_d,e_d,\kappa\) are real. Here \(\mathcal O=O_{m,0}\cup O_{m,1}\), every \(d\) is divisible by \(p\), and
\[
(b_d,e_d)=(-1,3\log2)\quad(d\in O_{m,0}),\qquad
(b_d,e_d)=(3/2,-3\log2)\quad(d\in O_{m,1}).
\]

For a direct Fourier verification, use
\[
S_n=\sum_{a\mid n}a,\quad T_n=\sum_{a\mid n}a\log a,\quad
k_n=\kappa-\log n+2T_n/S_n.
\]
For each \((d,n)\), let
\[
\lambda=2\pi nd,\qquad B=b_dk_n+e_d,\qquad
F(y)=B e^{-\lambda y}+b_d e^{\lambda y}E_1(2\lambda y).
\]
The established expansion is
\[
J=L^2+\sum_{d,n}\frac{S_n}{n}F(y)\cos(\lambda x).
\]
The defining integral of \(E_1\) gives
\[
\frac d{dy}\left[e^{\lambda y}E_1(2\lambda y)\right]
=\lambda e^{\lambda y}E_1(2\lambda y)-e^{-\lambda y}/y.
\]
Consequently
\[
\boxed{\begin{aligned}
\partial_{\bar z}J={}&\frac{iL}{y}
+\frac i4\sum_{d,n}\frac{S_n}{n}\Bigl[
 b_d\bigl(2\lambda e^{\lambda y}E_1(2\lambda y)
             -e^{-\lambda y}/y\bigr)e^{i\lambda x}\\
&\hspace{42mm}-(2\lambda B+b_d/y)e^{-\lambda y}e^{-i\lambda x}
\Bigr].
\end{aligned}}
\tag{5}
\]
Indeed \(\partial_{\bar z}(F\cos\lambda x)
=i[(F'+\lambda F)e^{i\lambda x}+(F'-\lambda F)e^{-i\lambda x}]/4\).
This also checks (4) against the previously computed signed coefficients of \(\mathsf E_2\). The zero mode is \(iL/y\), not zero. Exponential decay of the Fourier summands gives local uniform convergence of the displayed derivatives on \(y>0\).

There is no additional invariant measure to insert. With the complex orientation,
\[
dz\wedge d\bar z=-2i\,dx\wedge dy,
\]
so the two-form and its Petersson normalization are
\[
\boxed{\Omega=4\pi f\,\partial_{\bar z}J\,dx\wedge dy
=-8\pi^2 i f\overline{h_J}\,dx\wedge dy,\qquad
\mathcal A=-8\pi^2i\langle f,h_J\rangle_2.}
\tag{6}
\]
Here \(\langle f,h\rangle_2=\int_{Y_0(N)}f\bar h\,y^2d\mu\),
\(d\mu=dx\,dy/y^2\). The pairing converges even if \(h_J\) itself is not square integrable. Automorphy of \(J\) implies the weight-two transformation law for \(h_J\).

## 4. The area theorem, with its exact boundary hypothesis

**Theorem.** Let \(\Gamma\) be a finite-index congruence subgroup, \(X_\Gamma\) its compactification, and \(\alpha=2\pi i f(z)dz\) the differential of a holomorphic weight-two cusp form with trivial multiplier. Let \(J\) be a globally defined \(C^1\) scalar function on \(Y_\Gamma\). It may be complex. Suppose in each cusp coordinate \(w=x+iy\) of width \(h_{\mathfrak a}\), uniformly for \(0\le x\le h_{\mathfrak a}\),
\[
|J_{\mathfrak a}(w)|+|\partial_xJ_{\mathfrak a}(w)|
+|\partial_yJ_{\mathfrak a}(w)|
\le C_{\mathfrak a}(1+y)^{A_{\mathfrak a}}
 (1+\log y)^{B_{\mathfrak a}}
\quad(y\ge2),
\tag{7}
\]
for some finite nonnegative exponents. Then
\[
\boxed{\int_{Y_\Gamma}\alpha\wedge dJ=0.}
\tag{8}
\]
The integral is absolutely convergent. For real \(J\), equivalently,
\(\langle f,(2\pi i)^{-1}\partial_zJ\rangle_2=0\).

More generally, for any such global \(C^1\) function for which \(\alpha\wedge dJ\) is absolutely integrable, define its horizontal cusp flux by
\[
B_{\mathfrak a}(T)=2\pi i\int_0^{h_{\mathfrak a}}
 f_{\mathfrak a}(x+iT)J_{\mathfrak a}(x+iT)\,dx.
\]
Then the exact necessary and sufficient boundary condition for (8) is
\[
\boxed{\int_{Y_\Gamma}\alpha\wedge dJ
=\lim_{T\to\infty}\sum_{\mathfrak a}B_{\mathfrak a}(T);
\quad \int\alpha\wedge dJ=0
\ \Longleftrightarrow\ \lim_T\sum_{\mathfrak a}B_{\mathfrak a}(T)=0.}
\tag{9}
\]
This statement concerns the sum of fluxes; it does not assume that each separate limit exists in the more general case.

**Proof.** In a cusp coordinate the transformed cusp form satisfies
\(f_{\mathfrak a}(w)=O(e^{-2\pi y/h_{\mathfrak a}})\).
Condition (7) makes both the absolute area integral and all boundary estimates convergent. Truncate every cusp at height \(T\). The quotient is a compact surface with boundary, and on it
\[
d(-J\alpha)=\alpha\wedge dJ
\]
because \(d\alpha=0\). Paired polygon sides cancel since \(J\alpha\) is globally defined. The top edge of each truncated cusp is oriented from \(h_{\mathfrak a}\) to zero. Therefore Stokes gives
\[
\int_{Y_{\Gamma,T}}\alpha\wedge dJ
=-\int_{\partial Y_{\Gamma,T}}J\alpha
=\sum_{\mathfrak a}B_{\mathfrak a}(T).
\]
The fluxes tend to zero exponentially under (7). Absolute integrability permits passing to the limit and proves both (8) and (9). Elliptic points introduce no boundary term: one may either use their smooth orbifold charts, or pass to a finite torsion-free cover, apply the argument, and divide by its degree. \(\square\)

**Application to the actual jet.** Each \(E(dz,s)\) has polynomial growth at every cusp, uniformly on compact parameter sets away from poles, with the same property for its first spatial derivatives. This can be checked without a new automorphic theorem. At a rational cusp, a level-one integral matrix sends the rational image of that cusp under \(z\mapsto dz\) to infinity. The composite with its cusp scaling is upper triangular, so it sends \(w\) to \(\lambda w+\mu\), \(\lambda>0\). The existing level-one Fourier expansion then has constant terms proportional to \(y^s,y^{1-s}\) and exponentially decreasing nonconstant terms. Taking finitely many parameter derivatives only introduces finite powers of \(\log y\).

The finite coefficient combination defining \(J\) thus satisfies (7) at **every** cusp, not just 0 and infinity. Finite Laurent-coefficient combinations of a meromorphic family also have this property whenever the selected jet is regular. This includes the full regular divisor-scaling family already classified, not only the midpoint. The cusp blow-up of the curvature coefficient in a \(q\)-chart from the earlier report does not contradict this: its density is integrable, and the boundary flux of \(J\alpha\) still tends to zero. Formula (1) follows.

This proves orthogonality for all such scalar functions and all cusp forms. The condition \(U_pf=0\), conductor exponent two, and the Fourier-support restriction are unnecessary for (8). For the class requested in the question, imposing those additional conditions gives a subclass of the same vanishing theorem.

## 5. What horizontal integration does, and actual unfolding

First isolate the Fourier issue without replacing a modular fundamental domain by a strip. On any horizontal strip away from the real axis, write locally absolutely differentiable Fourier series
\[
J(x+iy)=\sum_{k\in\mathbf Z}j_k(y)e^{2\pi ikx},\qquad
f(x+iy)=\sum_{m\ge1}a_m e^{-2\pi my}e^{2\pi imx}.
\]
Direct integration over one period gives
\[
\boxed{\int_0^1 f\,\partial_{\bar z}J\,dx
=\frac i2\sum_{m\ge1}a_m e^{-2\pi my}
 \left[j_{-m}'(y)-2\pi m j_{-m}(y)\right].}
\tag{10}
\]
It is the **negative** frequency of \(J\) that pairs with a positive frequency of \(f\). For (5), the diagonal is \(m=nd\), not \(m+nd\). Every such \(m\) is divisible by \(p\), so \(a_m=0\). The zero mode of \(J\) contributes nothing because \(f\) has no zero mode. Thus the horizontal integral in (10) vanishes at every \(y>0\) for this particular jet.

That proves a strip identity. A fundamental domain for \(\Gamma_0(N)\) is not the full strip, and the support information at infinity alone is not a proof of a modular-domain integral. The following unfolding computes the actual quotient integral from definitions and independently verifies (1).

For \(d\mid N\), initially \(\Re s>2\), let
\[
I_d(s)=\int_{\Gamma_0(N)\backslash\mathbb H}
 \alpha_f\wedge d_z E(dz,s).
\]
In this formula \(d_z\) is the exterior differential, not the integer divisor. Put \(w=dz\), \(D_d=\operatorname{diag}(d,1)\),
\[
H_d=D_d\Gamma_0(N)D_d^{-1}\subset G=\mathrm{SL}_2(\mathbf Z),
\qquad F_d(w)=d^{-1}f(w/d).
\]
The inclusion follows by multiplying matrix entries: the upper-right entry is divisible by \(d\), and the lower-left entry by \(N/d\). This is a finite-index subgroup. The differential becomes \(2\pi i F_d(w)dw\), and \(F_d\) is a weight-two cusp form for \(H_d\).

Trace it to level one, without averaging:
\[
T_d(w)=\sum_{\eta\in H_d\backslash G}(F_d|_2\eta)(w).
\]
It is a cusp form because each summand has zero constant term in its corresponding cusp expansion. Splitting the \(H_d\)-domain into translates of a \(G\)-domain gives exactly
\[
I_d(s)=\int_{G\backslash\mathbb H}2\pi iT_d(w)dw\wedge d_wE(w,s).
\]
Use the defining primitive Eisenstein sum, with \(\Gamma_\infty\) including the sign stabilizer,
\[
E(w,s)=\sum_{\eta\in\Gamma_\infty\backslash G}
 \operatorname{Im}(\eta w)^s.
\]
Termwise exterior differentiation and change of variables unfold the last integral to
\[
\boxed{I_d(s)=2\pi i s\int_0^\infty y^{s-1}
 \left(\int_0^1 T_d(x+iy)\,dx\right)dy=0.}
\tag{11}
\]
There is no unspecified constant or Euler factor: \(dw\wedge dy=dx\wedge dy\) and \(d(y^s)=s y^{s-1}dy\). The inner integral is the zero constant coefficient of a cusp form. One need not use the additional fact that level one has no weight-two cusp forms.

Here the unfolding is absolutely justified, not a formal continuation of a divergent double series. For a holomorphic weight-two cusp form \(T\), modular invariance and cusp decay bound \(y|T(w)|\) on the whole upper half-plane. Therefore the unfolded absolute integral near zero is bounded by a multiple of \(\int_0^1y^{\Re s-2}dy\); at infinity there is exponential decay. Choosing \(\Re s>2\) suffices, together with absolute local convergence of the Eisenstein sum and its exterior differential.

The cusp estimates in §4 give meromorphic continuation of the paired family and locally uniform bounds after its possible poles are removed. Thus (11) is a zero meromorphic identity. Multiply by the known meromorphic coefficients \(v_d(s)\), sum over \(d\), and take the regular second derivative at zero. Derivatives pass under the integral by those same estimates. This proves (1) from the definitions, independently of the Stokes proof.

Combining (4), (6), and (11), the requested Eisenstein-derivative pairing is precisely
\[
\mathcal A=-4\pi^2 i\sum_{d\in\mathcal O}d\left[
b_d\langle f,\mathsf E_2'(d\,\cdot,1)\rangle_2
+(\kappa b_d+e_d)\langle f,\mathsf E_2(d\,\cdot,1)\rangle_2\right]=0.
\tag{12}
\]
In fact each of these convergent cuspidal pairings is zero by the differentiated meromorphic identity: multiply (11) by the known completion factor \(Z(s)\), whose Eisenstein poles have constant spatial residues, and evaluate or differentiate the spatially differentiated identity at \(s=1\). No nonzero Rankin–Selberg value is left. Unfolding selects a cusp-form constant coefficient, not a product of two nonzero Fourier sequences.

## 6. The exact scope of a two-variable change

Changing only the Fourier-support condition cannot repair this integral: (8) never used it. Nor does adding a second **scalar** variable. If \(K(z,w)\) is globally scalar in \(z\), is \(C^1\) there, and satisfies (7) for each fixed \(w\), then
\[
\boxed{\int_{Y_\Gamma}\alpha(z)\wedge d_zK(z,w)=0
\quad\text{for every such }w.}
\tag{13}
\]
Auxiliary parameter derivatives and further integrations also give zero whenever their own dominated-convergence or Fubini hypotheses hold. A scalar kernel singular on a diagonal is outside these hypotheses at that diagonal and needs its boundary/current contributions computed; the presence of a second variable alone supplies no exception.

The actual obstruction is the use of a globally exact test one-form with zero boundary flux. A nonexact \((0,1)\)-kernel can have a nonzero diagonal pairing. For an explicit diagnostic, choose an orthonormal basis \(\omega_1,\ldots,\omega_g\) of holomorphic one-forms on compact \(X\), with
\[
\frac i2\int_X\omega_j\wedge\overline{\omega_k}=\delta_{jk}.
\]
The smooth differential kernel
\[
\mathcal K(z,w)=\sum_{j=1}^g\overline{\omega_j(z)}\otimes\omega_j(w)
\]
satisfies the exact finite-sum identity
\[
\boxed{\frac i2\int_{z\in X}\alpha(z)\wedge\mathcal K(z,w)=\alpha(w).}
\tag{14}
\]
This follows by expanding \(\alpha\) in the orthonormal basis. Since the right side is not identically zero, \(\mathcal K\) is not a globally scalar \(\bar\partial_z\)-derivative with the zero-flux conditions above. It changes the exactness hypothesis, not merely Fourier support or the number of variables.

Equation (14) is only the elementary complex Hodge pairing. It does not contain the two independent rational points, local height contributions, or their Néron–Tate determinant. It is included to establish the exact logical boundary of (13), not as an arithmetic construction or a successor proposal. No arithmetic-height interpretation is asserted.

## 7. Verdict and verification grade

**BROAD_CURVATURE_ORTHOGONALITY_THEOREM.** The area integral for the actual jet is zero, and the same conclusion holds for the entire global moderate-growth scalar-function class with its exact cusp-flux extension (9). This includes all regular one-variable Eisenstein jets considered here, regardless of conductor, Fourier support, or normalization. The relative path obstruction (3) separately prevents identifying its ray period with such an area integral by inventing a filling.

The proof is a written derivation with two calculations of the area integral: Stokes with every cusp controlled, and absolutely convergent Eisenstein unfolding followed by justified parameter continuation. The Fourier derivative was checked directly against the existing signed coefficients. No numerical experiment, literature survey, new source theorem, subagent, or successor is used. This is not a formal proof-assistant certificate or independent referee review. The existing ray residuals and their rigorous positive intervals remain intact. No comparison with a real Mordell–Weil height determinant is obtained.
