# Gate G2 — a fixed Poincaré-biextension construction

**Verdict: PROVED, as a written mathematical deduction from the bundle's saturated Mordell–Weil basis and residual-image hypotheses, and the published biextension/1-motive constructions specified below.**

This document does not prove the bundle's rank, saturation, or residual-image inputs afresh. It does not prove G1, construct the common arithmetic multiplier, or deduce any new Tate–Shafarevich conclusion. It is not a Lean proof or an independently reviewed human theorem. No claim of novelty is made.

## 1. Exact assertion

Use the minimal model and points in `PROMPT.md`:

\[
 E:y^2=x^3-x^2-66020924x-65074271436,
 \quad P_1=(-3031,327384),\quad P_2=(-2394,281520).
\]

The supplied inputs are that these points form a saturated basis modulo torsion, that the torsion has order two, that the Tamagawa product is 16, and that the odd residual representations are surjective. Put

\[
 S_0=\{2,3,5,2243,4547,5843\}.
\]

**Theorem G2.** For every prime \(p\notin S_0\), there exist infinitely many primes \(\ell\nmid pN\) such that

\[
 \ell\equiv 1+p\pmod {p^2},\qquad
 \rho_{E,p}(\operatorname{Frob}_\ell)=-1,
 \qquad R_{p,\ell}\ne0\quad\text{in }\mathbf F_p.
\]

Here \(R_{p,\ell}\) is exactly the determinant of the pairing computed in `mt_prescreen/tame_reg.gp`, extended from a prime-to-\(p\) multiple of the given basis and divided by the fourth power of that multiple. The scalar \(-1\) in the middle condition means the matrix \(-I_2\), so it is conjugacy-invariant.

In particular,

\[
 v_p(\ell-1)=1,\qquad
 \#E(\mathbf F_\ell)\equiv\det(1-(-I_2))=4\pmod p.
\]

Thus \(E(\mathbf F_\ell)[p]=0\). These primes satisfy the stronger, no-\(p\)-torsion version of Ota's cyclic auxiliary condition. The theorem is existential: there is no small-\(\ell\) bound or evaluation-cost assertion.

The theorem is obtained without any modular-symbol coefficient, any fitted value of \(K\), any assumption on \(\Sha\), or the refined Mazur–Tate leading-term conjecture.

## 2. Published inputs, and what they are used for

**[T]** K.-S. Tan, *Refined theorems of the Birch and Swinnerton-Dyer type*, Ann. Inst. Fourier **45** (1995), 317–374, DOI 10.5802/aif.1457. Use only the definitions/constructions of the canonical pairing: §2.1, Definition 2.2 and (L3)–(L4), printed pp. 329–331; Remarks 1–3 on p. 331; §2.2, Definition 2.6, p. 334. No BSD-dependent theorem from the later sections of that paper is used.

**[J]** P. Jossen, *On the Mumford–Tate conjecture for 1-motives*, Invent. Math. **195** (2014), 393–439, DOI 10.1007/s00222-013-0459-y; author manuscript arXiv:1107.5259. Use §1.4 (torsion realization and weight filtration), Proposition 1.8 and Remark 1.9 (Poincaré description), and Remark 1.10 (duality and realization). The proof below does not invoke Jossen's adelic image theorem: the necessary mod-\(p\) central subgroup is proved directly.

**[O]** K. Ota, arXiv:1509.00682v1, *Kato's Euler system and the Mazur–Tate refined conjecture of BSD type*. Theorem 1.2, p. 2, explicitly allows \(E(\mathbf F_\ell)[p]=0\) in its cyclicity condition. Its Sha conclusions are not used in this G2 proof.

**[Ch]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), Theorem 8.31 (PDF page 149). Use only the consequence that a nonempty conjugacy class in a finite Galois extension is realized at infinitely many unramified primes.

We also use the standard Kummer exact sequence and Hilbert 90. The mod-\(p\) Kummer-image and mod-\(p^2\) lifting facts needed here are proved below, rather than treated as unrestricted independence assumptions.

## 3. A fixed normalization before any auxiliary prime is chosen

Set \(m=16\) and \(Q_i=mP_i\). Each rational Tamagawa number divides 16. Therefore \(Q_i\in E^0(\mathbf Q_v)\) at every finite place \(v\). This avoids relying on the smaller component exponent used by the computational script.

Let \(\mathcal P\) be the rigidified Poincaré \(\mathbf G_m\)-biextension of \(E\times E^\vee\); identify \(E\) with its dual using the principal polarization. For \(j=1,2\), its restriction over the second point \(Q_j\) is a commutative algebraic group extension

\[
 1\longrightarrow\mathbf G_m\longrightarrow G_j\longrightarrow E\longrightarrow0.
\]

For each \((i,j)\), choose a rational point \(r_{ij}\) of the fiber \(\mathcal P(Q_i,Q_j)\). Such a point exists: this is a \(\mathbf G_m\)-torsor over \(\mathbf Q\), and Hilbert 90 makes it trivial over \(\mathbf Q\).

For every finite \(v\), apply the unramified Néron splitting (L3) of [T] to \(r_{ij}\). Since the second argument is in \(E^0(\mathbf Q_v)\), its value

\[
 n_v(r_{ij})\in\mathbf Q_v^\times/\mathbf Z_v^\times\simeq\mathbf Z
\]

is an **integer**, not a fractional component correction. Almost all these integers are zero. Multiplying \(r_{ij}\) by

\[
 \prod_{v<\infty} v^{-n_v(r_{ij})}\in\mathbf Q^\times
\]

produces a point \(r_{ij}^0\) whose unramified Néron value is zero at every finite place. Two such normalized rational lifts differ by \(\pm1\). This ambiguity is a \(p\)-th power for every odd \(p\).

Now set

\[
 G=G_1\times_E G_2,
 \qquad R_i=(r_{i1}^0,r_{i2}^0)\in G(\mathbf Q),
 \qquad \mathscr M=[\mathbf Z^2\xrightarrow{e_i\mapsto R_i}G].
\]

This is one fixed 1-motive over \(\mathbf Q\), independent of \(p\) and \(\ell\). Its construction does not require an integer representing \(\#\Sha\), a zeta determinant, or any finiteness statement. It is a different object from the already-retained homology source: it keeps the multiplicative fibers which encode the tame pairing.

## 4. Why this object retains the actual tame height

### 4.1 A local quotient

Fix a good \(\ell\ne p\) with \(p\nmid\#E(\mathbf F_\ell)\). Multiplication by \(p\) is an automorphism on the formal group at \(\ell\) and on the reduction group. Thus

\[
 E(\mathbf Q_\ell)/pE(\mathbf Q_\ell)=0,
 \qquad E(\mathbf Q_\ell)[p]=0.
\]

Hilbert 90 makes \(G_j(\mathbf Q_\ell)\to E(\mathbf Q_\ell)\) surjective. Applying multiplication by \(p\) to this extension, the two displayed equalities give the canonical isomorphism induced by the torus:

\[
 \mathbf Q_\ell^\times/(\mathbf Q_\ell^\times)^p
 \ \xrightarrow{\sim}\ G_j(\mathbf Q_\ell)/pG_j(\mathbf Q_\ell).
 \tag{4.1}
\]

Let \(q_{j,\ell}\) be its inverse. Let \(\lambda_\ell\) send a unit to its discrete logarithm modulo \(p\), and send the uniformizer \(\ell\) to zero. The map

\[
 R\longmapsto\lambda_\ell(q_{j,\ell}(R))
 \tag{4.2}
\]

is the unique homomorphism on \(G_j(\mathbf Q_\ell)\) with values in \(\mathbf F_p\) that extends this character on the torus. Indeed, a difference of two such extensions factors through \(E(\mathbf Q_\ell)\), which is \(p\)-divisible.

The tame splitting (L4) of [T] is initially defined when the second argument lies in the formal group. Choose \(n\) prime to \(p\) with \(nQ_j\) in that formal group. The second biextension law maps the fiber over \(Q_j\) to the fiber over \(nQ_j\), and acts on the torus by the \(n\)-th power. Apply (L4) there, reduce to the tame character, and divide the resulting value by \(n\) in \(\mathbf F_p\). This extends the splitting to \(G_j(\mathbf Q_\ell)\), independently of \(n\). By the uniqueness just proved, that extension is (4.2). There is no local ordinary-reduction assumption at \(\ell\) in this argument.

The global Néron normalization of \(r_{ij}^0\) kills all the unramified contributions away from \(\ell\). The archimedean contribution to this odd-order character is trivial. Definition 2.6 of [T] therefore identifies the global tame pairing of \(Q_i,Q_j\), up to the common reciprocity sign convention, with

\[
 B_{ij}^{(p,\ell)}=\lambda_\ell(q_{j,\ell}(r_{ij}^0)).
 \tag{4.3}
\]

### 4.2 Comparison with `tame_reg.gp`, including the factor two

For clarity this comparison is made on a prime-to-\(p\) multiple lying in the formal group at \(\ell\); bilinearity then returns to the original basis.

For a minimal Weierstrass model let \(t=-x/y\) and write \(Q=(a/d^2,b/d^3)\), with the fractions in lowest terms and \(d>0\). For \(Q\in E^0\) at all bad finite places, the section of \(\mathcal O_E(O)\) at \(Q\) has unramified Néron valuation \(v(d)\). The diagonal pullback of the rigidified Poincaré bundle is

\[
 [2]^*\mathcal O_E(O)\otimes\mathcal O_E(O)^{-2}
 \simeq\mathcal O_E(O)^2.
\]

The rigidification is fixed by the minimal differential. Here the integral extension on the identity component is the cubical extension used in the Néron splitting. The divisor \((O)\) meets a rational section \(Q\) with multiplicity \(v(d)\): in the formal disc this is \(v(t(Q))=v(d)\), and elsewhere in the identity component both are zero. This fixes the unramified normalization, rather than leaving a local height constant unspecified. On the formal neighborhood of \(O\), the squared section has tame value \(t(Q)^2\), up to a principal unit. Its global unramified normalization divides by \(d^2\). Thus its tame logarithm is

\[
 B(Q,Q)=2\lambda_\ell\bigl(t(Q)/d\bigr)
        =2\operatorname{ind}_g(-a/b)\pmod p,
 \tag{4.4}
\]

up to the same common sign. The principal unit disappears under the tame character. This is precisely the script's quadratic function, doubled. Polarizing (4.4) shows that the biextension bilinear pairing is twice the bilinear form in the script; it is not inferred from the numerical calibration.

Consequently, on \(Q_i=mP_i\),

\[
 B_{ij}^{(p,\ell)}=\pm2m^2 H_{ij}^{(p,\ell)},\qquad
 \det B^{(p,\ell)}=4m^4 R_{p,\ell}.
 \tag{4.5}
\]

A different common identification of \(\mu_p\) with \(\mathbf F_p\) multiplies every entry by the same nonzero scalar; it multiplies the determinant by a square unit. Since \(p\ge7\) and \(m=16\), none of these factors affects nondegeneracy.

This removes the apparent obstruction caused by the varying multiplier \(M_\ell\): the script evaluates a canonical bilinear pairing on \(M_\ell P_i\), whereas (4.3) evaluates its fixed normalized biextension lift. Division by \(M_\ell^2\), and by \(M_\ell^4\) for determinants, is legitimate because \(p\nmid M_\ell\).

## 5. A Frobenius invariant in a fixed finite extension

For each fixed \(p\), take the finite Galois extension

\[
 L_p=\mathbf Q\bigl(\mathscr M[p],E[p^2]\bigr).
 \tag{5.1}
\]

Here \(\mathbf Q(\mathscr M[p])\) denotes the splitting field of the finite torsion realization defined in [J], §1.4. This field is fixed before \(\ell\) is chosen. In particular it is not a field obtained by adjoining denominators of the moving points \(M_\ell P_i\).

The weight-graded pieces of \(\mathscr M[p]\) have dimensions \(2,2,2\). In compatible bases the Galois action has the block form

\[
 g=\begin{pmatrix}
 \chi_p(g)I_2&b(g)&c(g)\\
 0&A(g)&a(g)\\
 0&0&I_2
 \end{pmatrix},
 \tag{5.2}
\]

where \(A(g)=\rho_{E,p}(g)\). The columns of \(a\) are the ordinary Kummer cocycles of \(Q_1,Q_2\). Put \(D=[\mathbf Z^2\to E]\), with the same two points. Under the principal polarization, \(G\) is \(\operatorname{Ext}^1(D,\mathbf G_m)\). The Hom/Ext realization compatibility in [J], Remark 1.10, identifies its torsion realization with \(\operatorname{Hom}(D[p],\mu_p)\). Therefore the upper extension is the dual of the lower one, not an independently selected extension. For \(A(g)=I_2\), this compatibility and the alternating Weil pairing give

\[
 b(g)=-a(g)^tJ,\qquad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \tag{5.3}
\]

Changing the convention for the principal polarization changes a common sign only. More explicitly, dualizing the quotient matrix \(\bigl(\begin{smallmatrix}A&a\\0&I\end{smallmatrix}\bigr)\), twisting by \(\chi_p\), and identifying \(E[p]^\vee(1)\) with \(E[p]\) yields the top extension block; at \(A=I\), it is (5.3). The extension class is fixed by the points \(Q_j\), so no independence between \(a\) and \(b\) is assumed.

If \(\chi_p(g)=1\) and \(A(g)-I\) is invertible, define

\[
 \beta(g)=c(g)-b(g)(A(g)-I)^{-1}a(g).
 \tag{5.4}
\]

To see its meaning, correct a lift of the \(i\)-th weight-zero basis vector by the middle vector \(-(A-I)^{-1}a_i\). The resulting Kummer cocycle has zero elliptic component and torus component \(\beta_i\). By (4.1), this is the multiplicative Kummer class of the normalized \(r_{ij}^0\).

At an unramified prime \(\ell\) with these conditions, a unit \(u\) has Frobenius Kummer value \(u^{(\ell-1)/p}\) in \(\mu_p\). Identifying \(g_\ell^{(\ell-1)/p}\) with 1 in \(\mathbf F_p\) identifies this with \(\operatorname{ind}_{g_\ell}(u)\). Equations (4.3)–(4.5) give

\[
 \det\beta(\operatorname{Frob}_\ell)\ne0
 \quad\Longleftrightarrow\quad R_{p,\ell}\ne0.
 \tag{5.5}
\]

The condition is conjugacy-invariant. Direct block multiplication gives

\[
 \beta(hgh^{-1})=\chi_p(h)\beta(g)
 \tag{5.6}
\]

for upper block-triangular \(h\) of the form (5.2); the weight-zero action is the identity and the torus action is the same scalar on both coordinates. Thus the zero/nonzero condition on its determinant descends to conjugacy classes of \(\operatorname{Gal}(L_p/\mathbf Q)\).

## 6. The required Kummer image is full

Let \(\Gamma_0=\ker\rho_{E,p}\). Restriction of \(a\) to \(\Gamma_0\) is a homomorphism with image

\[
 U\subseteq E[p]^2.
\]

It is stable under the full \(\mathrm{GL}_2(\mathbf F_p)\)-action. The two global Kummer classes of \(Q_i\) are independent: the supplied basis is saturated, and \(p\nmid m\#E(\mathbf Q)_{\rm tors}\).

We spell out the inflation issue. A central element acting on a module by a scalar \(z\ne1\) annihilates group cohomology after subtracting 1: for a 1-cocycle \(f\), the cocycle identities for \(zg=gz\) give \((z-1)f(g)=(g-1)f(z)\), making \(f\) a coboundary if \(z-1\) is invertible. Apply this to \(-I\) and the standard module to obtain

\[
 H^1(\mathrm{GL}_2(\mathbf F_p),E[p])=0.
\]

If \(U\ne E[p]^2\), some nonzero linear combination of the two coordinate maps vanishes on \(U\). Indeed, the standard module is simple with endomorphism ring \(\mathbf F_p\), and a direct sum of two copies is semisimple; any proper submodule is killed by a nonzero map to a copy of the standard module. The corresponding linear combination of Kummer classes then vanishes on \(\Gamma_0\). Inflation-restriction and the displayed cohomology vanishing make it zero globally, contradicting the independence of the points modulo \(p\).

Therefore

\[
 a(\Gamma_0)=E[p]^2=M_2(\mathbf F_p).
 \tag{6.1}
\]

## 7. Central commutators supply every symmetric matrix

For \(g,h\in\Gamma_0\), write \(\alpha=a(g)\), \(\alpha'=a(h)\). The matrices (5.2) are unipotent of class two. Their commutator is purely central, with top-right block

\[
 C=b(g)a(h)-b(h)a(g)
 =-\alpha^tJ\alpha'+\alpha'^tJ\alpha.
 \tag{7.1}
\]

Since \(J^t=-J\), this matrix is symmetric.

The image (6.1) lets us prescribe \(\alpha\) and \(\alpha'\) independently for two chosen Galois elements. Taking one nonzero column equal to the first standard basis vector and the same column of the second matrix equal to the second vector gives \(-2E_{11}\), or \(-2E_{22}\). Taking them in different columns gives \(-(E_{12}+E_{21})\). These three matrices span \(\operatorname{Sym}_2(\mathbf F_p)\), and products of central elements add their blocks. Hence the actual Galois image contains

\[
 z(C)=\begin{pmatrix}I&0&C\\0&I&0\\0&0&I\end{pmatrix}
 \qquad(C\in\operatorname{Sym}_2(\mathbf F_p)).
 \tag{7.2}
\]

Crucially these elements can be chosen to fix \(E[p^2]\). The matrices of \(g,h\in\Gamma_0\) on \(E[p^2]\) lie in \(1+pM_2(\mathbf Z/p^2)\), an abelian group. Their commutators, and products of those commutators, are therefore trivial on \(E[p^2]\). This proves compatibility with the exact congruence \(v_p(\ell-1)=1\); it is not an unproved disjointness assumption.

## 8. Simultaneous admissibility and nondegeneracy

For completeness the supplied mod-\(p\) surjectivity implies surjectivity modulo \(p^2\) here. Let \(H\subseteq\mathrm{GL}_2(\mathbf Z/p^2)\) be the image and \(W\subseteq M_2(\mathbf F_p)\) its principal-congruence kernel. Lift the transvection \(U=I+E_{12}\). For \(p\ge5\), its lift has \(p\)-th power \(I+pE_{12}\): the correction terms involve sums of polynomials of degree at most two in \(0,\ldots,p-1\), and these sums vanish modulo \(p\). Conjugating gives \(\mathfrak{sl}_2(\mathbf F_p)\subseteq W\).

If \(W\) had zero trace, the determinant character of \(H\) modulo \(p^2\) would factor through \(\mathrm{GL}_2(\mathbf F_p)\). Its abelianization has order \(p-1\), which has no quotient of order \(p\). This contradicts surjectivity of the cyclotomic determinant modulo \(p^2\). Thus \(W\) also contains a nonzero-trace element, and \(W=M_2(\mathbf F_p)\). This proves the claimed full image modulo \(p^2\).

Choose \(g_0\) in the image on \(L_p\) whose matrix on \(E[p^2]\) is

\[
 A_2=\begin{pmatrix}-1&0\\0&-(1+p)\end{pmatrix}.
\]

Then \(A(g_0)=-I\), \(\chi_p(g_0)=1\), and its cyclotomic character modulo \(p^2\) equals \(1+p\).

By (7.2), multiply \(g_0\) by a central \(z(tI)\) without changing its action on \(E[p^2]\). Equation (5.4) gives

\[
 \beta(z(tI)g_0)=\beta(g_0)+tI.
\]

The polynomial

\[
 \det(\beta(g_0)+tI)=t^2+\operatorname{tr}(\beta(g_0))t+\det\beta(g_0)
\]

is monic of degree two. Since \(p\ge7\), it cannot vanish for every \(t\in\mathbf F_p\). Choose a value at which it is nonzero. The resulting Galois element has all three desired properties: elliptic residual matrix \(-I\), determinant \(1+p\) modulo \(p^2\), and invertible \(\beta\).

Its conjugacy class is nonempty. Chebotarev supplies infinitely many unramified rational primes with Frobenius in that class, even after removing the finitely many primes of bad reduction of the model, 1-motive, and auxiliary presentation. Equations (5.5) and the determinant computation at the start prove Theorem G2. ∎

## 9. Scope and verification boundary

- This is an \(\ell\)-independent description in a fixed finite extension **for each \(p\)**. There is no claim of one finite extension encoding every \(p\).
- It explicitly uses the multiplicative extension in addition to ordinary elliptic division points. Ordinary mod-\(p\) Kummer classes alone disappear locally when \(p\nmid\#E(\mathbf F_\ell)\); this proof does not ignore that obstruction.
- The nonempty conjugacy class is constructed, not presumed from residual surjectivity alone.
- The all-prime quantifier comes from the saturated-basis and residual-image hypotheses and the algebra above, not from testing \(17,19,23,29\).
- The construction does not establish a unit multiplier relating \(R_{p,\ell}\) to a modular-symbol coefficient. Even an invertible tame regulator does not, without G1, give an Ota witness.
- No assertion is made that the prescribed auxiliary primes are small enough for the existing numerical corpus.
- A separate translated-divisor computation in `code/check_pairing_comparison.py` reproduces \(B=2H\) for two 389a1 cases (including a degenerate one) and the seed at \((17,103)\). It uses denominators of translated divisors, not the script's polarization formula. This is a normalization diagnostic, not the proof of §4.
- `code/check_g2_algebra.py` checks the block-matrix identities and spanning arguments over six finite fields. Those checks are diagnostic confirmation of the written algebra; they are not a substitute for the geometric identification in §4.
- The especially consequential review interface is §4: the globally normalized Poincaré lifts, their local multiplicative Kummer class, and the exact tame pairing. The construction states and proves that interface rather than importing the refined Mazur–Tate coefficient formula.

## Source links

- Tan: https://aif.centre-mersenne.org/item/10.5802/aif.1457.pdf
- Jossen author manuscript: https://arxiv.org/pdf/1107.5259 ; publication: https://doi.org/10.1007/s00222-013-0459-y
- Ota: https://arxiv.org/pdf/1509.00682

- Milne: https://www.jmilne.org/math/CourseNotes/ANT.pdf, Theorem 8.31.
