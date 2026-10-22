# The 4547 trace of the midpoint residual periods

**TRACE_ZERO_BUT_I0_NOT_FORCED.**

For this seed, \(U_{4547}f=0\), and the requested trace identity is exact:
\[
\boxed{\sum_{a\bmod4547}I_a=0.}
\]
It removes the trivial additive-character component. The individual value \(I_0\) is the sum of the surviving nontrivial components, not the trivial component itself. The available symmetries do not identify the truncated rays or supply an invariant period functional that annihilates those components. A nonzero matrix-coefficient example in the actual local representation demonstrates the non-forcing explicitly in §5.

Neither \(I_0=0\) nor \(I_0\ne0\) is proved. No residual period was evaluated numerically. This is the end of the bounded trace test.

## 1. Inputs, headline correction, and the exact U relation

Use the [four-orbit classification](AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md), its midpoint section (6.1), and its residual (6.4). Its headline has been corrected: the original normalization leaves a family; uniqueness holds only after the extra midpoint condition MC. The old heading and complete preceding state are preserved in the provenance archive for this operation. No formula or proof in that report was changed.

Put \(p=4547\), \(M=N/p^2\), \(y_0=N^{-1/2}\), and \(R(z)=R_{\rm mid}(z)\). The retained identity is
\[
\mathcal E_{\rm mid}(z,s)=\mathcal C_M(pz,s).
\]
Consequently
\[
R(z+1/p)=R(z),\qquad
R(x+iy)\in\mathbf R,\qquad R(-x+iy)=R(x+iy).
\tag{1.1}
\]
Here \(R\) is the second jet minus \(\log^2(\sqrt N y)\). Its periodicity does not imply invariance under every Atkin–Lehner transformation.

The exact seed is \(y^2=x^3+a_2x^2+a_4x\), with
\[
a_2=-5p,\qquad a_4=4p\cdot5843.
\]
Direct integral arithmetic gives
\[
c_4=16p(25p-12\cdot5843),\quad
\Delta=2^8 3^2\cdot2243\cdot p^3\cdot5843^2,
\]
\[
v_p(c_4)=1,\quad v_p(c_6)=2,\quad v_p(\Delta)=3.
\]
The model is minimal at \(p\) since its discriminant valuation is less than 12. These valuations give the retained type III and conductor exponent two; its reduction is the cuspidal cubic \(y^2=x^3\), with additive local Euler factor 1. These are exact local data, not an inference merely from a chosen Eisenstein level. See [the retained seed record](../SEED_PROVED_STATE.md), §0.

The modular form attached to \(E\) is a normalized weight-two newform of exact level \(N\) and trivial nebentypus. The newform theorem states that when the character factors through \(N/p\) and \(p^2\mid N\), \(a_p=0\), and that \(a_{pn}=a_pa_n\). The hypotheses apply here. The inspected source is [Ribet–Stein, Theorem 9.1.10(1), (2b), printed pp. 74–75](https://wstein.org/books/ribet-stein/main.pdf#page=84); this is an imported Atkin–Lehner–Li theorem, not a claim to have reproved all newform theory.

With the explicit classical normalization
\[
(U_pf)(z)=\frac1p\sum_{b=0}^{p-1}f((z+b)/p)
=\sum_{n\ge1}a_{pn}e^{2\pi inz},
\]
we have
\[
\boxed{U_pf=0,\qquad a_{pn}=0\quad(n\ge1).}
\tag{1.2}
\]
The independently retained value \(a_{4547}=0\) agrees with this application.

## 2. The trace calculation

Define precisely the periods requested:
\[
I_a=2\pi\int_{y_0}^{\infty} f(a/p+iy)R(a/p+iy)\,dy.
\]
By (1.1), the residual in every integral is the same \(R(iy)\). Also
\[
\sum_{a=0}^{p-1}f(a/p+iy)=p(U_pf)(ipy)=0.
\]
The argument \(ipy\) matters: there is no change in the integration cutoff or a missing scaling factor. Absolute convergence follows from cusp decay and the explicit residual Fourier series. Thus
\[
\sum_a I_a
=2\pi\int_{y_0}^{\infty}R(iy)
\sum_a f(a/p+iy)\,dy=0.
\tag{2.1}
\]
This proves the trace, including its normalization and endpoints.

## 3. The exact surviving additive-twist data

Let \(\zeta=e^{2\pi i/p}\). For \(r\in\mathbf F_p\), define
\[
F_r(z)=\frac1p\sum_{a\bmod p}\zeta^{-ar}f(z+a/p)
=\sum_{\substack{m\ge1\\m\equiv r\ (p)}}a_m e^{2\pi imz},
\]
\[
J_r=\frac1p\sum_a\zeta^{-ar}I_a
=2\pi\int_{y_0}^{\infty}F_r(iy)R(iy)\,dy.
\tag{3.1}
\]
Then (1.2) gives \(F_0=0\) and \(J_0=0\), while Fourier inversion gives
\[
\boxed{I_a=\sum_{r\in\mathbf F_p^\times}\zeta^{ar}J_r,
\qquad I_0=\Delta_{\rm mid}=\sum_{r\in\mathbf F_p^\times}J_r.}
\tag{3.2}
\]
Every \(J_r\) is real because \(a_m\) and \(R(iy)\) are real. Hence the exact reality relation is
\[
I_{-a}=\overline{I_a},\qquad
I_0+2\sum_{a=1}^{(p-1)/2}\operatorname{Re}I_a=0.
\tag{3.3}
\]
It is not \(I_{-a}=I_a\) unless that particular period is real.

For a specification entirely in existing Fourier data, put
\[
W_m=2\pi\int_{y_0}^{\infty}e^{-2\pi my}R(iy)\,dy.
\]
These weights do not involve \(f\) or the target period. Then
\[
I_a=\sum_{\substack{m\ge1\\p\nmid m}}a_mW_m\zeta^{am},
\qquad
J_r=\sum_{\substack{m\ge1\\m\equiv r\ (p)}}a_mW_m.
\tag{3.4}
\]
The weights can be written without any unspecified integral. Use \(S_n,T_n,\kappa,E_1\) from the preceding report, set
\[
k_n=\kappa-\log n+2T_n/S_n,\quad
(b_d,e_d)=
\begin{cases}(-1,3\log2),&d\in O_{m,0},\\
(3/2,-3\log2),&d\in O_{m,1},
\end{cases}
\]
and for \(k=nd\) define
\[
\mathcal K_{m,k}=
\frac{e^{-2\pi(m-k)y_0}E_1(4\pi ky_0)
-E_1(2\pi(m+k)y_0)}{2\pi(m-k)}.
\]
Only \(p\nmid m\) is needed, whereas \(p\mid k\), so \(m=k\) never occurs. Termwise integration of the known residual gives
\[
W_m=2\pi\sum_{d\in O_{m,0}\cup O_{m,1}}\sum_{n\ge1}\frac{S_n}{n}
\left\{(b_dk_n+e_d)\frac{e^{-2\pi(m+nd)y_0}}{2\pi(m+nd)}
+b_d\mathcal K_{m,nd}\right\}.
\tag{3.5}
\]
All these series converge absolutely. Formula (3.5) follows by integrating the exponential term and integrating the \(E_1\) term by parts, as in the preceding experiment. It has not been evaluated.

One can also express the same obstruction with truncated Eichler integrals:
\[
A_a(y)=\sum_{m\ge1}\frac{a_m}{m}\zeta^{am}e^{-2\pi my},
\quad A_a'(y)=-2\pi f(a/p+iy),
\]
\[
I_a=A_a(y_0)R(iy_0)
+\int_{y_0}^{\infty}A_a(y)\frac{d}{dy}R(iy)\,dy.
\tag{3.6}
\]
The endpoint \(a/p+iy_0\) is an interior point. These are weighted, truncated additive-twist data; they are not ordinary cusp-to-cusp modular symbols with their usual homology relations.

## 4. Why the geometric symmetries do not identify the rays

Write \(H(z)=\mathcal E_{\rm mid}''(z,0)\) and
\(L(z)=\log(\sqrt N\,\operatorname{Im}z)\). Then \(H\) is Atkin–Lehner invariant, but \(R=H-L^2\). For every actual Atkin–Lehner representative \(w\),
\[
\boxed{R(wz)=R(z)+L(z)^2-L(wz)^2.}
\tag{4.1}
\]
For \(w=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) of positive determinant \(Q\),
\[
L(wz)-L(z)=\log\frac{Q}{|cz+d|^2}.
\]
Thus the residual alone is generally not invariant. Since
\(w^*\alpha_f=\lambda_w\alpha_f\), a path change gives the exact identity
\[
\int_{w\gamma_a}\alpha_fR
=\lambda_w\int_{\gamma_a}\alpha_f
\{R+L^2-(L\circ w)^2\},
\tag{4.2}
\]
where \(\gamma_a:a/p+i\infty\to a/p+iy_0\).
The left side normally uses a different curved path and the right side contains an explicit extra weight. It is not an equation identifying two of the \(I_a\).

A holomorphic Möbius transformation carrying one of these truncated rays onto another must fix their sole boundary endpoint \(\infty\). It therefore has \(c=0\); equality of the cutoff heights then makes it a translation. In \(\Gamma_0(N)\) such translations are integral and do not change \(a\bmod p\). A nontrivial exact-divisor Atkin–Lehner coset has no such representative: in its standard integral matrix, setting the lower-left entry to zero would force \(Qae=1\), impossible for \(Q>1\). The group generated by \(\Gamma_0(N)\) and these involutions therefore does not transitively identify the displayed rays. Complex conjugation gives exactly (3.3).

At the unshifted ray the full Fricke involution has a simpler effect, but still no vanishing. Here \(L(W_Niy)=-L(iy)\), so \(R\) is unchanged on that axis. The seed's root number \(+1\) gives \(f|_2W_N=-f\). Fricke carries the upper half-ray to the oppositely oriented lower half-ray. The two downward-oriented half-ray integrals are therefore equal, and the full-ray integral is \(2I_0\), not zero.

Cusp equivalence does not remove the problem: it does not identify the interior endpoints, and the weighted differential is not closed:
\[
d(R\alpha_f)=dR\wedge\alpha_f\not\equiv0.
\]
Indeed \(R\) is real, nonconstant and real analytic, so its antiholomorphic derivative is not identically zero. The usual homology relations for the holomorphic differential cannot be transferred to this weighted differential.

## 5. The smallest local module, and a non-forcing certificate

The local representation can be identified without computing any periods. The retained type III inertia has eigencharacters \(\psi,\psi^{-1}\) of order four. Since \(p\equiv-1\bmod4\), Frobenius interchanges these distinct characters. The two-dimensional Weil representation is irreducible and its monodromy operator is zero. Its local automorphic representation \(\pi_p\) is therefore supercuspidal. A scalar twist remains irreducible and cannot have conductor exponent below two: an irreducible two-dimensional Weil representation has no inertia-invariant line. Hence this conductor-two representation is twist-minimal.

Let \(v\) be its nonzero newvector, with trivial central character, and put \(D=\operatorname{diag}(p,1)\). The local type theorem identifies the span of the translates of \(v\) by \(n(a/p)\) with the irreducible type for \(D^{-1}\mathrm{GL}_2(\mathbf Z_p)D\). Its dimension is \(p-1\), and its restriction to the upper unipotent group contains each nontrivial character of \(\mathbf F_p\) once. The inspected precise source is [Loeffler–Weinstein, Theorems 3.5–3.6, §3.2](https://arxiv.org/pdf/1008.2796#page=7), published in Mathematics of Computation 81 (2012), 1179–1200. Only this local theorem is imported here; no modular-symbol or arithmetic-height formula is inferred from it.

Here is also the elementary part of that dimension calculation in our coordinates. Choose the right-translation convention
\[
v_a=\pi_p(n(-a/p))v,
\]
so that its classical restriction is \(f(z+a/p)\). The local \(U_p\) relation, multiplied by a diagonal matrix, gives \(\sum_a v_a=0\). Translation permutes these vectors by addition of indices. Every \(t_u=\operatorname{diag}(u,1)\), \(u\in\mathbf Z_p^\times\), fixes \(v\) and sends \(v_a\) to \(v_{ua}\). Thus their span is a nonzero quotient of
\[
\mathbf C[\mathbf F_p]\big/\mathbf C\sum_a[a]
\]
for the affine group \(\mathbf F_p\rtimes\mathbf F_p^\times\). This quotient is irreducible: its distinct nontrivial additive characters are permuted transitively by the multiplicative group. Its dimension is \(p-1\). The conductor-two type theorem supplies stability under the rest of the midpoint compact group, including its Weyl element.

The weighted ray integral is a linear functional \(\Lambda_R\) on this local space after fixing the other automorphic factors. Its coordinate vector is \((I_a)=(\Lambda_R(v_a))\). Consequently the exact local ambient space is the dual type, represented in these coordinates as
\[
\mathcal A=\{(x_a)\in\mathbf C^p:\sum_a x_a=0\},
\quad \dim_{\mathbf C}\mathcal A=4546.
\tag{5.1}
\]
Reality cuts out the real form \(x_{-a}=\overline{x_a}\), of real dimension 4546. Under translations alone, the cyclic span of the actual vector is
\[
\bigoplus_{\substack{r\ne0\\J_r\ne0}}\mathbf C(\zeta^{ar})_{a}.
\]
Under the full local type action, its smallest stable span is zero if all periods vanish and is the entire irreducible dual type otherwise. No nonvanishing of the actual vector is asserted. This distinguishes a classified local representation from unknown coordinates in it.

Crucially, the midpoint invariance of the Eisenstein factor is not midpoint invariance of \(\Lambda_R\). A single truncated ray is not an average over that compact group. Transforming the form transforms the path or the chosen finite component of the period functional; it does not assert that its numerical value stays fixed.

There is an explicit local countermodel to the inference \(I_0=0\) from the stated representation relations. Choose a midpoint-compact-invariant positive Hermitian form on this finite type and normalize \(\langle v,v\rangle=p-1\). Define \(\Lambda(x)=\langle x,v\rangle\), linear in the first argument. Unit diagonal matrices fix \(v\) and permute all nonzero indices, so \(\Lambda(v_a)\) is constant for \(a\ne0\). Applying \(\Lambda\) to \(\sum_a v_a=0\) gives
\[
\boxed{(\Lambda(v_a))_{a\bmod p}=(p-1,-1,-1,\ldots,-1).}
\tag{5.2}
\]
This is trace zero, satisfies the reality relation, and has nonzero zeroth coordinate. It is a matrix coefficient of the actual local type, not an arbitrarily invented representation. It even respects the diagonal-unit invariance and the Fricke eigencharacter of the newvector: if \(\pi_p(w)v=\epsilon v\), then \(\Lambda(\pi_p(w)x)=\epsilon\Lambda(x)\).

Equation (5.2) is not claimed to equal the actual period vector. It proves that these local symmetry relations permit a nonzero zeroth coordinate. Proving that the specific \(\Lambda_R\) annihilates \(v\) requires an additional identity for the explicit quantities (3.1)–(3.6).

## 6. Scope and stop

The inspected current master and the two automorphic experiment files contain the inputs but no prior trace calculation for this residual. Two targeted source checks supplied the standard newform coefficient theorem and the conductor-two local type theorem. No literature survey or new construction was performed.

The new closed identity is \(\sum_a I_a=0\). The exact unresolved scalar is
\[
\Delta_{\rm mid}=\sum_{r=1}^{4546}J_r
=\sum_{\substack{m\ge1\\4547\nmid m}}a_mW_m.
\]
The trace removes \(J_0\), which already vanishes from \(a_{pm}=0\); it does not remove this displayed sum. The period functional needed for that further annihilation is not furnished by MC, Fricke symmetry, trivial nebentypus, cusp equivalence, or the local type.

This result neither evaluates \(\Delta_{\rm mid}\) nor gives a real Néron–Tate regulator comparison. The bounded operation terminates here. There is no successor operation.
