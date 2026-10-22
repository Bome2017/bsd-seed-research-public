# Minimal local conductor and the natural-module ray contributions

This is the local proof supplement to [the reduction theorem](DIVISION_FIELD_REDUCTION_THEOREM.md). Throughout \(p\ge7\). The conductor computation at the coefficient prime assumes **good reduction at \(p\)**. At other rational primes it uses the seed's actual local types. No finite-prime numerical experiment is used.

## 1. Local cohomology at a good coefficient prime

Write \(V=E[p]\), \(F=\mathbf Q_p\), \(K_w=F(V)\), \(D=\operatorname{Gal}(K_w/F)\), and \(J\subset D\) for the inertia image. The seed has \(p\nmid\#\widetilde E(\mathbf F_p)\), as proved in the main document. Its local Kummer space \(L_p\) has dimension one.

For ordinary reduction the residual representation has the shape

\[
 V|_{G_F}\sim\begin{pmatrix}\chi\psi^{-1}&*\\0&\psi\end{pmatrix},
\]

where \(\chi\) is mod-\(p\) cyclotomic and \(\psi\) is unramified, with \(\psi(\operatorname{Frob}_p)=a_p\bmod p\ne1\). Its connected line is \(V^+=\mathbf F_p(\chi\psi^{-1})\). The inertia image is either a tame cyclic group of order \(p-1\), or

\[
 J=U\rtimes T,\quad U=\left\{\begin{pmatrix}1&b\\0&1\end{pmatrix}\right\},\quad
 T=\left\{\begin{pmatrix}a&0\\0&1\end{pmatrix}\right\}.
\]

In the tame case \(H^1(J,V)=0\) by prime-to-\(p\) averaging. In the wild case

\[
 H^1(U,V)=V/(u-1)V
\]

is the line represented by the second basis vector (the norm operator is zero for \(p\ge3\)). Conjugation by \(\operatorname{diag}(a,1)\), including its action on cochains, acts on this line by \(a^{-1}\). Thus \(H^1(U,V)^T=0\), proving again \(H^1(J,V)=0\).

The unramified quotient \(D/J\) has order dividing \(p-1\); hence inflation-restriction gives \(H^1(D,V)=0\). Also

\[
 H^1_{\mathrm{ur}}(F,V)=V^{I_p}/(\operatorname{Frob}_p-1)V^{I_p}=0.
\]

Here \(V^{I_p}=0\) in the wild case; in the tame case its Frobenius character is the nontrivial \(\psi\).

For supersingular reduction over the unramified ground field \(\mathbf Q_p\), inertia is the nonsplit Cartan \(\mathbf F_{p^2}^{\times}\), acting through the two fundamental characters of level two. Its order is \(p^2-1\). The decomposition group normalizes this Cartan and has quotient of order two, given by residue Frobenius. It follows that

\[
 e(K_w/F)=p^2-1,\quad f(K_w/F)=2,\quad
 H^1(J,V)=H^1(D,V)=0,\quad V^{I_p}=0.
\]

These are the standard good-reduction inertia descriptions; the supersingular tame vanishing is also used in [Prasad–Shekhar, proof of Theorem 4.1](https://arxiv.org/pdf/1912.12928). The ordinary cochain calculation above avoids importing their converse theorem with its separately stated hypotheses.

In both cases restriction of \(L_p\) to \(K_w\) is injective. If a nonzero restricted class were unramified over \(K_w\), its restriction to inertia over \(F\) would lie in \(H^1(J,V)=0\). It would therefore be unramified over \(F\), contradicting \(H^1_{\mathrm{ur}}(F,V)=0\). Every nonzero local Kummer class remains **ramified** over \(K_w\).

## 2. Ordinary reduction: exact conductor two

After a finite unramified extension \(F'/F\) of degree dividing \(p-1\), the étale quotient of \(E[p]\) is constant. By Cartier duality its connected subgroup is \(\mu_p\). There is an exact finite-flat sequence over \(\mathcal O_{F'}\)

\[
 0\longrightarrow\mu_p\longrightarrow E[p]\longrightarrow\mathbf Z/p\longrightarrow0.
\]

Consequently, over \(F'_0=F'(\mu_p)\), the torsion field is obtained by adjoining a \(p\)-th root of a unit \(u\in\mathcal O_{F'}^{\times}\). Indeed the fiber over a generator of the constant quotient is a finite-flat \(\mu_p\)-torsor over \(\mathcal O_{F'}\), and such torsors are units modulo \(p\)-th powers.

Every class in \(E(F)/p\) can be represented by a point in its formal group because \(p\nmid\#\widetilde E(\mathbf F_p)\). Factor multiplication by \(p\) as the connected isogeny followed by its dual étale isogeny. The latter is an isomorphism on formal groups over \(\mathcal O_{F'}\). A formal point therefore has a unique formal preimage under that étale isogeny. Its preimages under the connected isogeny form another integral \(\mu_p\)-torsor, represented by a unit \(v\in\mathcal O_{F'}^{\times}\). The Kummer extension under discussion is contained in

\[
 F'_0(u^{1/p},v^{1/p}). \tag{L1}
\]

Here \(F'/F\) is unramified and of degree prime to \(p\), so it neither destroys a nonzero local class nor changes a conductor exponent.

We now calculate ramification in (L1), rather than appeal to a general loose conductor bound. Since \(F'\) is unramified over \(\mathbf Q_p\), every unit class modulo \(p\)-th powers can be represented by \(1+pa\); a representative in \(1+p^2\mathcal O_{F'}\) is a \(p\)-th power by the logarithm. For a nontrivial such class, take \(z=(1+pa)^{1/p}-1\). Its valuation normalized by \(v(p)=1\) is \(1/p\).

In the degree-\(p\) extension \(M=F'_0((1+pa)^{1/p})\), normalized integral valuations give

\[
 v_M(z)=p-1,\quad v_M(\zeta_p-1)=p,
 \quad\pi_M=(\zeta_p-1)/z\text{ is a uniformizer}.
\]

For every nonidentity \(\sigma\in\operatorname{Gal}(M/F'_0)\),

\[
 v_M(\sigma z-z)=p,\qquad
 v_M(\sigma\pi_M-\pi_M)=p+p-2(p-1)=2.
\]

Thus its unique lower and upper break is one, and its conductor is two. Every nontrivial cyclic quotient of the elementary abelian extension in (L1) is given by a product of these unit classes and has the same property. The compositum therefore has a single ramification break one. Lower ramification groups restrict to subgroups, so its extension over the torsion field is weakly ramified as well. Any nontrivial subextension that occurs in the Kummer image has conductor at most two.

Section 1 showed that a nonzero restricted Kummer class is ramified. Its image is a \(p\)-group in residue characteristic \(p\); it cannot be a nontrivial tame extension. Its conductor is therefore at least two, proving **exactly two**.

This argument works whether the ordinary torsion extension itself is tame or wild. No assumption of split ordinary \(E[p]\) over \(F\) is made.

## 3. Supersingular reduction: exact conductor two

Choose a formal parameter \(t\) on a minimal good model. A generator \(P\) of \(E(F)/p\) may be represented with \(v_p(t(P))=1\). The height-two formal multiplication series shows

\[
 v_p(t(T))=\frac1{p^2-1}\quad(0\ne T\in E[p]),\qquad
 v_p(t(Q))=\frac1{p^2}\quad([p]Q=P).
\]

The second equality is the Newton polygon of \([p](X)-t(P)\): the coefficient of \(X^{p^2}\) is a unit and every lower coefficient has valuation at least one. Restriction of the nonzero Kummer class is injective by §1. Its nonzero image is a \(D\)-stable subspace of \(V\), hence all of \(V\), because the nonsplit Cartan acts irreducibly. Consequently \(M=K_w(Q)\) has degree \(p^2\) over \(K_w\). The displayed valuation forces this extension to be totally ramified.

With integral valuations on \(M\),

\[
 v_M(\pi_{K_w})=p^2,\quad v_M(t(Q))=p^2-1,\quad v_M(t(T))=p^2.
\]

Thus \(\pi_M=\pi_{K_w}/t(Q)\) is a uniformizer. For a nonidentity automorphism, \(\sigma Q=Q+T\) with \(T\ne0\). The integral formal group law gives

\[
 v_M(t(Q+T)-t(Q))=p^2;
\]

the coefficient of the linear \(t(T)\) term is a unit and the other terms have larger valuation. Hence

\[
 v_M(\sigma\pi_M-\pi_M)=p^2+p^2-2(p^2-1)=2.
\]

Again the only lower and upper break is one, so every nontrivial character of this elementary abelian extension has conductor two.

## 4. The representation of the surviving ray term at \(p\)

Write \(U^i=1+\mathfrak p_w^i\). The residue-field unit group has order prime to \(p\); the conductor-two source is exactly

\[
 U^1/U^2\simeq\mathfrak p_w/\mathfrak p_w^2.
\]

We prove

\[
 \boxed{\dim_{\mathbf F_p}\operatorname{Hom}_D(U^1/U^2,V)=1.} \tag{L2}
\]

### Ordinary case

Wild inertia acts trivially on \(\mathfrak p_w/\mathfrak p_w^2\). Its tame character is \(\chi\). To see the latter precisely, a nonzero connected torsion point has parameter valuation \(1/(p-1)\); its integral \(K_w\)-valuation is 1 in the tame case and \(p\) in the wild case. Its leading inertia character is \(\chi\). If \(\theta\) is the tame character on a uniformizer, this gives \(\theta=\chi\) or \(\theta^p=\chi\). Since \(\theta\) has order dividing \(p-1\), both give \(\theta=\chi\).

Every equivariant map to \(V\) must land in \(V^+\): this follows either from wild invariants, or from the distinct tame characters \(\chi\) and 1. Twist the source by \((V^+)^{-1}\). Inertia now acts trivially. For \(f=f(K_w/F)\), the quotient \(D/J=C_f\) acts on the residue field as Frobenius times a nonzero scalar. Its \(f\)-th power is one, so this scalar has norm one. Finite-field Hilbert 90 removes the scalar; the normal basis theorem then identifies this representation with the regular \(\mathbf F_p[C_f]\)-module. Its Hom space to the trivial character has dimension one. This proves (L2).

### Supersingular case

Every nonzero torsion parameter has integral \(K_w\)-valuation one. The map

\[
 E[p]\longrightarrow\mathfrak p_w/\mathfrak p_w^2,
 \qquad T\longmapsto t(T)\bmod\mathfrak p_w^2
\]

is additive, injective, and \(D\)-equivariant. Both sides have dimension two over \(\mathbf F_p\), so it is an isomorphism. The centralizer of the Cartan is \(\mathbf F_{p^2}\), and residue Frobenius acts on this field by its nontrivial involution. Therefore \(\operatorname{End}_D(V)=\mathbf F_p\), proving (L2) again.

Inducing from \(D\) to \(G\) and applying Frobenius reciprocity gives the identical dimension one for the sum over all primes above \(p\). This is a **nonzero possible local source**. Global units can impose relations on it; representation theory alone does not erase it.

## 5. Bad-prime ray terms: raw sources versus admitted sources

For \(q\ne p\), higher units are pro-\(q\) and have no exponent-\(p\) quotient. Because \(K\) contains \(\mu_p\), the only possible tame local ray source is

\[
 k_w^\times/(k_w^\times)^p\simeq\mathbf F_p(\chi|_{D_q}).
\]

Inertia acts trivially on this line; residue Frobenius acts as \(q\bmod p\). Frobenius reciprocity gives

\[
 \operatorname{Hom}_G(\operatorname{Ind}_{D_q}^{G}\mathbf F_p(\chi),V)
 =\operatorname{Hom}_{D_q}(\mathbf F_p(\chi),V).
\]

The symbolic result is:

| \(q\ne p\) | Representation calculation | Raw Hom dimension | Contribution admitted by Selmer |
|---|---|---:|---:|
| 2 | \(V^{I_2}=0\): additive connected fiber and component order 4 have no \(p\)-torsion over \(\mathbf Q_2^{ur}\) | 0 | 0 |
| 3 | Tate-invariant line \(\chi\tau\), with nontrivial unramified quadratic \(\tau\) | 0 | 0 |
| 2243 | Tate-invariant line \(\chi\); residual transvection is nontrivial | 1 | **0** |
| 4547 | inertia contains an element whose square is \(-I\), so \(V^{I_{4547}}=0\) | 0 | 0 |
| 5843 | Tate-invariant line \(\chi\tau\), with nontrivial unramified quadratic \(\tau\) | 0 | 0 |
| good coefficient prime \(p\) | \(U^1/U^2\), as in §4 | 1 | at most 1 globally; the local Kummer line is nonzero |

At 2243 the raw representation does admit \(V\) after induction. It is the *actual local Kummer condition*, proved in §4 of the main theorem, that eliminates it. Keeping this ray factor would therefore fail the minimal-conductor requirement.

At a good \(q\ne p\), any possible raw ray source is likewise eliminated by the Kummer condition; no such \(q\) enters the modulus. There is no archimedean source for odd \(p\).

The finite parameter set \(\{19,59,487\}\) in the main theorem concerns descent of *unramified* classes at bad rational primes. It is not a set of permitted ramification congruence classes. All away-from-\(p\) admitted ray contributions are zero even at those parameters.

## 6. What “minimal” does and does not assert

For every good \(p\ge7\), local solubility permits a nonzero class of conductor two, and the entire permitted local line has no conductor above two. Thus the exponent two in the local-condition modulus is minimal. A modulus exponent one would wrongly discard that line.

The compositum attached to the *actual global* Selmer group can nevertheless be unramified at \(p\) if its localization is zero. Its conductor is then zero there. Determining which of these two global possibilities occurs is part of the global arithmetic, and is recorded by \(r_p\in\{0,1\}\) in the exact dimension formula. No global ramification is inferred merely from local permission.

At the three coefficient primes of bad reduction, the good-reduction proof in §§1–4 does not apply. Their norm subgroups are defined, but their numerical exponents are not claimed by this tail theorem.
