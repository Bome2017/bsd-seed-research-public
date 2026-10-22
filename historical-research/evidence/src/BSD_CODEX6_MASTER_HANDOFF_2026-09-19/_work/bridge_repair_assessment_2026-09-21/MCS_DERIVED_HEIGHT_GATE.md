# The join audit, derived heights, and removal of the point contribution

2026-09-21. Written deductions at the source and seed grades of [the join](MCS_NONSQUAREFREE_JOIN.md). No numerical calculation, new primary vanishing, FIN, ORDER9, or Q36. These are elementary consequences and corrections, not a literature-novelty claim.

The [returned audit](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/JOIN_AUDIT_AND_NEXT_QUESTION.md) supports the restricted nonsquarefree composition. Its proposed height operation needs the correction below. Its description of BCK as the single external dependency is too narrow: Kataoka–Sano, MCS, and the retained image/local inputs remain load-bearing. A second model's partial review does not become an independent audit of their proofs.

## 1. What the existing tower already implies

Work in the exact regime (P) of the join. Put \(\Lambda=\mathbf Z_p[[t]]\), with \(t=\gamma-1\), \(I=(t)\), \(C_\infty\) the specified Iwasawa Selmer complex, and \(S=H^1(C_\infty)\).

[Kataoka–Sano, Proposition 5.11](https://jamathr.org/index.php/jamr/article/download/Vol-2Issue-2Paper-1/Vol-2Issue-2Paper-1/38199) supplies freeness of \(S\) of rank one; the retained Heegner main-conjecture input supplies \(y_\infty\ne0\). Consequently
\[
e=\max\{j:y_\infty\in t^j S\}<\infty,\qquad
y_\infty=t^e v_\infty,\quad v_\infty\notin tS.
\tag{1}
\]
Indeed, write \(y_\infty=g(t)b\) in a basis of \(S\). A nonzero power series has a first nonzero coefficient. This proves finite depth without computing it or assuming FIN. If the base specialization is zero, as in the report's Heegner specialization argument, then \(e\ge1\).

The coefficient after removing \(t^e\) need not be a \(p\)-adic unit. For example \(t^e\) and \(p^a t^e\) have the same augmentation order for every \(a\ge0\). Depth alone therefore does not supply integral content.

The triangle for multiplication by \(t\), followed by the retained base-change comparison, gives
\[
0\longrightarrow S/tS\longrightarrow S_p(E/K)
 \longrightarrow H^2(C_\infty)[t]\longrightarrow0.
\tag{2}
\]
In particular \(v_\infty\) specializes to a nonzero class \(\bar v\) which lifts to the entire tower. This does not assert that \(\bar v\) is primitive or is the Kummer class of a rational point.

## 2. A precise correction to the suggested height computation

**Lemma (tower lifts are annihilated by the derived Bocksteins).**
For a complex with the \(I\)-adic filtration, a class represented by an actual cocycle in the full complex has zero outgoing derived Bockstein on every page on which its specialization is considered. In the above Selmer setting,
\[
\beta^{(j)}(\bar v)=0,\qquad
h_j^{\rm Nek}(\bar v,w)=0
\tag{3}
\]
for every \(j\ge1\) and every \(w\) in the appropriate height domain. The Bertolini–Darmon heights likewise vanish for \(1\le j\le p-1\).

**Proof.** Represent \(v_\infty\in H^1(C_\infty)\) by a cocycle \(a\), so \(da=0\). Reducing this same cocycle modulo every \(I^j\) supplies compatible lifts. The derived Bockstein is the class of \(da\) in the relevant quotient, and is therefore zero. The height is obtained by cupping that Bockstein with the second input, proving (3).

This is the formula in [MCS, Appendix A, proof of Proposition A.4](https://arxiv.org/html/2603.23978v1#A1.SS1). The source's Theorem 4.2 identifies the Bertolini–Darmon pairing with the negative of the Nekovář pairing in its stated range. Its Hypothesis 4.1 holds here: the join already supplies the non-anomalous condition, prime-to-\(p\) Tamagawa product, and full residual image. Thus zero transfers to that pairing as well. \(\square\)

The proposed instruction to evaluate a height on a class in \(Q_e=I^e/I^{e+1}\) also confuses its input and output. \(Q_e\) is the target; the leading term of \(y_\infty\) belongs to
\[
I^eS/I^{e+1}S\simeq(S/IS)\otimes_{\mathbf Z_p}Q_e.
\]
Its Selmer factor is precisely the tower-lifted class in (3). Pairing that factor does not recover its integral leading coefficient.

**Scope.** This does not rule out height pairings on other Selmer directions, a regulator on an appropriate quotient, or an additional leading-term theorem. It corrects this proposed computation only. Theorem 4.2 compares two height constructions; it does not compute the unevaluated Stark ideals. No conclusion that all derived-height routes fail is warranted.

## 3. The twist refinement gives an exact conditional quotient formula

Suppose, additionally, an actual field \(K\) satisfying the join's conditions is supplied with a rigorous certificate that its quadratic twist has analytic rank one. The usual Gross–Zagier/Kolyvagin rank-one theorem, applied to the twist, gives rank one and finite Sha for the twist. Rational eigenspace decomposition then gives
\[
\operatorname{rank}E(K)=3.
\]
The join already proves \(E(K)[p]=0\). Hence \(E(K)/p^nE(K)\simeq R_n^3\), where \(R_n=\mathbf Z/p^n\), for every \(n\ge1\). There is no additional index restriction for this full point group; an index condition arises only if a chosen unsaturated sublattice replaces it.

**Lemma (remove the three point directions).** Under these conditions, for every \(i\ge0\),
\[
\boxed{\operatorname{Fitt}^{\,i}_{R_n}
 \bigl(\Sha(E/K)[p^n]^*\bigr)
 = I_{i+3}(\epsilon^{\rm Hg}_{n,0}).}
\tag{4}
\]
No finiteness of the full Sha group is required.

**Proof.** Dualize the finite Kummer exact sequence. Duality over \(R_n\) is exact on finite modules (equivalently, use Pontryagin duality), giving
\[
0\to\Sha(E/K)[p^n]^*\to
\operatorname{Sel}_{p^n}(E/K)^*\to R_n^3\to0.
\]
The surjection splits because \(R_n^3\) is projective. Adding a free summand of rank three shifts Fitting ideals by three; this follows directly from the presentation minors. Apply identity (J) from the join. \(\square\)

In particular, at \(n=1\),
\[
I_3(\epsilon^{\rm Hg}_{1,0})=\mathbf F_p
\ \Longleftrightarrow\ \Sha(E/K)[p]=0
\ \Longrightarrow\ \Sha(E/\mathbf Q)[p^\infty]=0.
\tag{5}
\]
The first equivalence is the zeroth Fitting-ideal criterion for a finite module to vanish. For the implication, restriction on Sha is injective at odd \(p\), since corestriction composed with restriction is multiplication by two. A nonzero \(p\)-primary torsion group has a nonzero element killed by \(p\).

This identifies the precise ideal that would suffice, not a method of evaluating it. The unit-ideal test is stronger than seed vanishing: it also rules out \(p\)-torsion from the twist, whose Sha is finite but not automatically trivial.

Two further qualifications matter. First, even with rank three the compact Selmer sequence remains
\[
0\to E(K)\otimes\mathbf Z_p\to S_p(E/K)
 \to T_p\Sha(E/K)\to0;
\]
one cannot replace the compact Selmer group by the point lattice without another argument. Second, unknown twist rank was not fatal to every upper-bound argument: the known two point directions already give a lower bound on the point contribution. Rank three permits the exact shift (4).

No suitable rank-one twist is certified in this operation. Root-number consistency is not such a certificate; a numerical test must rigorously exclude zero for the twist derivative. No twist search or height computation is launched.

## 4. Endpoint and grade

The independent missing input is an arithmetic evaluation or bound on the ideals in (4), together with a suitable certified \(K\) if this refinement is used. Pairing the divided Heegner class is not that evaluation by (3). The derivations above clarify and extend the restricted join, without a strict difficulty reduction or new BSD endpoint. Ordinary-prime coverage and the real regulator comparison remain as qualified in the join. The returned audit is preserved unchanged; this note governs only its subsequent height and quotient claims.

## 5. Author acceptance and two wording clarifications

The author has [accepted the correction additively](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/DERIVED_HEIGHT_CORRECTION_ACCEPTED.md), withdrawing the proposed height computation while preserving the join and conditional twist refinement. This acceptance changes no theorem grade or endpoint.

Two phrases in the acceptance should not be inherited literally. Division by \(t^e\) did not destroy a formerly detectable Bockstein signal: the argument is that the resulting class still lifts to the full complex, so all its Bocksteins vanish. And a proved statement \(\operatorname{ord}_{s=1}L(E^\chi,s)=1\) already is a rigorous analytic rank-one input. With central vanishing known, certifying \(L'(E^\chi,1)\ne0\) proves that statement; it is not a stronger mathematical hypothesis. The distinction is between a proved input and an unverified numerical expectation. The chosen \(K\) must also satisfy the join's local hypotheses.
