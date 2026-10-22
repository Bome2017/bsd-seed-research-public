# Fixed modular visibility: applicability and horizontal obstruction

Date: 2026-09-19, local time. This is a supporting proof for the single current record [MASTER_BSD_DAG.md](../../MASTER_BSD_DAG.md), not another current BSD map.

**Campaign verdict: `NO_HORIZONTAL_GAIN`.** The good-ordinary, nonsquarefree local gate can be passed using Zhang's published results, as the deduction below explains. The construction still supplies a different level-raised ambient for each residual prime. Two elementary obstructions rule out fixing its auxiliary levels and transporting its visibility to predetermined levels by morphisms that preserve the embedded \(E\) up to a \(p\)-unit. No integer bounding the seed's Sha-prime support is obtained.

The negative conclusion concerns these specified constructions. It does not prove that every possible fixed-level visibility theorem is false. Indeed, eventual vanishing would make such a theorem vacuously true.

## 1. Obligation, sources, and corrections to the proposed operation

The seed is

\[
E:y^2=x^3-22735x^2+106272484x,
\quad N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]

**Endpoint:** the finite-support part of FIN on the good ordinary tail. Even a successful ordinary-tail bound would leave supersingular support and the full depths at the surviving primes; it would not prove order nine or \(q_\infty=36\).

**Proposed implication:** independently fixed \(i:E\hookrightarrow A_0\), with every sufficiently large ordinary \(\Sha(E/\mathbf Q)[p]\) visible in \(A_0\), implies ordinary Sha support is contained in the prime divisors of one fixed integer (plus the stated finite initial exceptions). Section 4 proves this implication and its converse at the level of eventual vanishing.

**First unproved arithmetic arrow after the modularity gate:** passage from the varying ambient \(A_p\) to that independently fixed \(A_0\). Residual level lowering alone is not this arrow.

Primary sources inspected:

* Matteo Tamiozzo, *Congruences of modular forms and modularity of Tate–Shafarevich classes*, [arXiv:2402.07317v1](https://arxiv.org/abs/2402.07317v1), 11 February 2024. The local [PDF](sources/Tamiozzo_2402.07317.pdf) has 17 pages. The [2026 publisher record](https://link.springer.com/chapter/10.1007/978-3-032-13123-2_13) identifies a proceedings publication, pp. 377–400, online 1 May 2026. The subscription chapter's full text was not obtained; theorem numbering and body statements here are bound to the public manuscript, not an assumed identical published revision.
* Wei Zhang, *Selmer groups and the indivisibility of Heegner points*, Cambridge Journal of Mathematics 2 (2014), 191–253, [published PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf), also preserved [locally](sources/Zhang2014_published.pdf). Journal page numbers are used below.

Exact original-file identities are in [DOWNLOADS.json](sources/DOWNLOADS.json); extracted text is an aid, not a replacement for the originals.

Three corrections matter:

1. Tamiozzo's **general Theorem 4.1.1 itself** assumes squarefree \(N\). This restriction is not confined to an introductory corollary. Direct citation of that theorem therefore fails for the seed.
2. Theorem 4.1.1 and Corollary 4.1.2 also have a **supersingular** case, with an additional ramified nonsplit local hypothesis. Describing the whole source as ordinary-only is inaccurate. The nonsquarefree deduction in §3 below is ordinary-only because it uses Zhang's ordinary rank-zero/rank-one inputs.
3. For a given \(p,K\), Tamiozzo already constructs **one ambient containing all** the relevant \(p\)-torsion Sha classes. The remaining dependence is on \(p\) and on auxiliary choices made using its Selmer group, not necessarily a different ambient for each individual class.

## 2. What changes relative to the historical failures

The mechanism search covered the existing local discovery inventory, with 50 relevant hits preserved in [HISTORICAL_COLLISION_HITS.txt](HISTORICAL_COLLISION_HITS.txt). It was not an exhaustive recovery of older tasks, Library, or Drive.

| Earlier mechanism | Direction or object | Failure | Change here |
|---|---|---|---|
| Classical visibility and congruence lower bounds | Congruent partner or point produces a Sha class | No coverage of every excess Selmer class | Tamiozzo does supply coverage under his hypotheses; the blanket wrong-direction label must be narrowed |
| Fixed modular degree / congruence integer | Annihilates classes already visible in a fixed ambient | No theorem putting all Sha classes there | Still the missing arrow; varying level does not supply it |
| Zhang/Heegner classes at auxiliary levels | Classes span a residual Selmer group after choices at that prime | No common bound across primes or full primary depths | This operation uses the coverage, but does not overcome the varying levels |
| GL(3)/Eisenstein comparison | Selected automorphic extensions map into Selmer | No upper bound on all excess classes | The coverage direction is different; the fixed integral control problem survives |
| LINE/WC and finite integral sources | A new condition at each prime | No independently established common integer | Fixed visibility would still need an independent horizontal theorem; §4 records the converse |

The older F3 mechanism report had already identified bounded-level visibility as the missing comparison. Its universal assertion that visibility only has a lower-bound direction is superseded **only** to the extent of the actual coverage theorem. No stopped Eisenstein or witness-content route is reopened.

## 3. The nonsquarefree ordinary applicability gate

### 3.1 Local hypotheses really do pass

Fix a good ordinary \(p\ge5\). Choose an imaginary quadratic field \(K\), unramified at \(Np\), in which all prime factors of \(N\) split. Such a field exists by prescribing finitely many quadratic local conditions. Here \(N^-=1\), \(N^+=N\); \(K\) need not be fixed independently of \(p\) for this applicability statement.

The imported seed residual theorem gives \(\bar\rho_{E,p}(G_{\mathbf Q})=\mathrm{GL}_2(\mathbf F_p)\). The multiplicative primes are \(3,2243,5843\), with minimal discriminant valuations \(2,1,2\), respectively. Since \(p\ge5\), the Tate-curve inertia extension is nonzero modulo \(p\) at all three primes. Thus

\[
\operatorname{Ram}(\bar\rho_{E,p})=\{3,2243,5843\}
\]

in Zhang's convention that this set only lists primes occurring exactly once in \(N\).

At the additive primes \(q=2,4547\), \(p\ne q\). The filtration of \(E(\mathbf Q_q)\) has pro-\(q\) kernel, additive residue quotient, and component group of order at most four. Multiplication by \(p>3\) is bijective on each quotient, so \(E(\mathbf Q_q)/p=0\). Equivalently \(E[p](\mathbf Q_q)=0\); local duality and the Euler characteristic for \(q\ne p\) then give

\[
H^0(\mathbf Q_q,E[p])=H^1(\mathbf Q_q,E[p])=0.
\tag{L}
\]

This is exactly Zhang Lemma 5.1, pp. 222–223. Because these \(q\) split in \(K\), the same vanishing applies at the corresponding completions of \(K\).

Consequently Zhang's Hypothesis \(\heartsuit\), p. 203, holds: all multiplicative factors in \(N^+\) are residually ramified; the nonsquarefree case has at least two such factors; and \(L\) holds at every \(q^2\mid N^+\). These hypotheses persist when raising the level at admissible primes: a new inert prime belongs to \(N^-\), is not \(\pm1\pmod p\), and therefore does not trigger the ramification requirement there. The three original ramified primes remain available. Ordinariness persists because the new form's \(a_p\) is congruent to the original nonzero \(a_p\pmod p\).

This is not an assertion that prime-to-\(p\) Tamagawa numbers alone fix every nonsquarefree theorem. We have checked the particular local cohomology and ramification conditions used by the source.

### 3.2 Source interfaces used in the extension

| Interface | Precise published input |
|---|---|
| New form at level \(N m\) congruent to the seed | Zhang Theorem 2.1, pp. 203–204, iterated at admissible primes; no squarefree-\(N\) assumption |
| Residual Selmer conditions after raising | Zhang Theorem 5.2, pp. 223–224: ordinary local condition away from the auxiliary primes, transverse condition at them, with \(\mathbf F_p\) structure |
| Actual residual module in the newform factor | Zhang Notations (vii)–(ix), pp. 201–202, and §3.7: \(A_m[\mathfrak p_m]\simeq E[p]\otimes_{\mathbf F_p}k_m\), after choosing the ring-of-integers action and the allowed isogeny representative |
| Rank zero for the raised form | Zhang Theorem 7.1, pp. 231–232: zero primary Selmer implies nonzero central \(L\)-value |
| Nonzero Kummer class when residual Selmer dimension is one | Zhang Theorem 7.2, pp. 232–234; its class is \(c(1)\), the underived Heegner-point class of §3.7, equation (3.22) |
| Nonsquarefree period comparison behind that theorem | Zhang Theorem 6.4, pp. 229–230, explicitly extends Pollack–Weston beyond squarefree \(N\) under \(\heartsuit\); §7.2 explains the cancellation of local factors |
| Choosing primes and changing a Selmer condition | Tamiozzo §§2.1.1–2.1.2, which require squarefree \(N^-\), not squarefree \(N\); Zhang Lemma 7.3 and §5 give the same inputs |
| Geometric visibility from a Kummer class on the partner | Anti-diagonal gluing, Tamiozzo §3.2 and §§4.2.3–4.2.5; proof included below |

The deduction does not replace \(J[p]/\mathfrak m\) by \(J[\mathfrak m]\) without proof. Instead it uses the residual subgroup of the actual newform factor and its Kummer class. Nor does it use Zhang's derived classes \(c(n,m)\) with \(n\ne1\) as though they were rational points.

### 3.3 Written deduction: varying-level visibility for this seed at good ordinary primes

**Proposition.** Relative to the retained seed image and local-data theorems, and the published inputs just listed, for every good ordinary \(p\ge5\), there is a quotient \(A_p/\mathbf Q\) of some \(J_0(NL_p)\) and an embedding \(i_p:E\hookrightarrow A_p\) such that every class of \(\Sha(E/\mathbf Q)[p]\) is visible in \(A_p\).

**Proof.** Put \(V=E[p]\), \(S=\operatorname{Sel}_p(E/K)\), and \(r=\dim_{\mathbf F_p}S\). For an admissible squarefree product \(m\), let \(S^{(m)}\) replace the unramified local condition by the transverse one at its prime factors. The local lines are distinct and meet in zero. Detection by admissible primes and global duality give a sequence of distinct admissible primes \(\ell_1,\ldots,\ell_r\) such that

\[
S^{(1)}\supset S^{(\ell_1)}\supset\cdots\supset
S^{(L)}=0,\qquad L=\prod_{j=1}^r\ell_j,
\]

each step having codimension one. At a decreasing step the new Selmer group is exactly the kernel of localization in the preceding one. Consequently

\[
S\longrightarrow\bigoplus_{j=1}^r H^1_{\rm ur}(K_{\ell_j},V)
\simeq\mathbf F_p^r
\tag{I}
\]

is an isomorphism: its kernel is \(S^{(L)}=0\), and both sides have dimension \(r\).

For \(m_i=L/\ell_i\), changing just the condition at \(\ell_i\) from \(S^{(L)}=0\) shows \(\dim S^{(m_i)}=1\). The one-dimensional subspace of \(S\) whose coordinates in \(I\) vanish except at \(i\) lies in \(S^{(m_i)}\), because zero satisfies both local conditions at every other \(\ell_j\). It must equal \(S^{(m_i)}\). Thus these \(r\) spaces lie in \(S\) and their nonzero vectors form a basis. This elementary argument supplies the needed basis without assuming an unproved nonsquarefree extension of Tamiozzo's particular coinvariant construction.

Level raising produces \(g_L\) and \(g_{m_i}\). Zhang Theorem 5.2 identifies their residual Selmer groups, after residue-field extension, with \(S^{(L)}\) and \(S^{(m_i)}\). A zero residual Selmer group implies zero full primary Selmer group, as used explicitly in Zhang §7.2. Theorem 7.1 gives \(L(g_L/K,1)\ne0\). Its root number is \((-1)^{r+1}\), by Zhang (1.4), since \(N^-=1\) initially. Hence \(r\) is odd and each \(m_i\) has an even number of prime factors, so its Shimura curve is indefinite. Also \(r\ge2\), from the two independent rational points and \(E[p](K)=0\), hence in fact \(r\ge3\).

For each \(m_i\), Theorem 7.2 provides a nonzero, underived Heegner-point Kummer class on a suitable newform factor \(F_i\) with ring-of-integers action. Write its residual field as \(k_i\). There is a \(G_{\mathbf Q}\)-equivariant injection

\[
j_i:V\hookrightarrow F_i[\mathfrak p_i]\subset F_i[p],
\qquad F_i[\mathfrak p_i]\simeq V\otimes_{\mathbf F_p}k_i.
\]

If \(c_i\) is any nonzero vector of \(S^{(m_i)}\), then this Heegner class is a nonzero \(k_i\)-multiple of \(j_{i,*}c_i\), since that Selmer group has dimension one over \(k_i\). Its image in \(H^1(K,F_i)\) is zero. The kernel of this cohomology map is stable under the ring-of-integers action; lifting the inverse of the nonzero residue scalar therefore shows that \(j_{i,*}c_i\) also maps to zero. This step uses the actual Kummer image, not just residual congruence of representations.

Now form

\[
A_p=(E\times\prod_{i=1}^r F_i)/V^r,
\quad (x_i)_i\longmapsto
(-\sum_i x_i,j_1x_1,\ldots,j_rx_r).
\tag{G}
\]

The restriction of the quotient map to \(E\times0\) is an embedding, since its intersection with this finite subgroup is trivial. In \(A_p\) the two images of \(x\in V\) from \(E\) and \(F_i\) agree. Thus the image of \(c_i\) in \(H^1(K,E)\) maps to zero in \(H^1(K,A_p)\). The \(c_i\) form a basis of \(S\), so all of \(\Sha(E/K)[p]\) is visible.

Each \(F_i\) is a factor belonging to a newform of exact level \(Nm_i\). These levels are distinct and different from \(N\). Together with \(E\), these pairwise nonisogenous newform factors occur in \(J_0(NL)\). Maps onto their product, followed by \(G\), give a surjection \(J_0(NL)\twoheadrightarrow A_p\); alternatively this follows by the same old/new argument as Tamiozzo §4.2.5.

Finally restriction \(H^1(\mathbf Q,A_p)[p]\to H^1(K,A_p)[p]\) is injective: restriction followed by corestriction is multiplication by (2), a unit on a group killed by odd \(p\). Every rational Sha class therefore vanishes already in \(H^1(\mathbf Q,A_p)\). This proves the proposition. ∎

**Grade and limit.** This is a written deduction from the cited source theorems with the seed hypotheses checked, not a direct quotation of Tamiozzo's squarefree theorem, a formal verification, or a claim of research novelty. It proves a coverage statement, not a new FIN bound. It uses no global finiteness of the seed's Sha and no 3-primary theorem. The finite rank-zero Selmer groups appearing in the proof belong to the auxiliary forms and follow from the explicit local-condition dimension drop.

## 4. Fixed visibility and the non-equivalence test

**Lemma 1 (annihilator of a fixed ambient).** Let \(i:E\hookrightarrow A_0\) be an embedding of abelian varieties over \(\mathbf Q\). There are a homomorphism \(r:A_0\to E\) and a positive integer \(d\) such that \(r\circ i=[d]\). In particular

\[
\operatorname{Vis}_i H^1(\mathbf Q,E)
:=\ker(i_*:H^1(\mathbf Q,E)\to H^1(\mathbf Q,A_0))
\]

is killed by \(d\), and it has no nonzero \(p\)-torsion if \(p\nmid d\).

**Proof.** Poincaré reducibility gives a retraction in \(\operatorname{Hom}_{\mathbf Q}(A_0,E)\otimes\mathbf Q\); clear denominators. On cohomology \(r_*i_*=[d]\), so \(i_*c=0\) implies \(dc=0\). ∎

The whole visible group is finite: for \(B=A_0/i(E)\), it is the image of \(B(\mathbf Q)/\pi A_0(\mathbf Q)\). This quotient is finitely generated by Mordell–Weil and is killed by \(d\), by the lemma and exactness. The integer depends on the **fixed embedding**, not merely a name for an unspecified varying modular variety. For the dual optimal embedding into \(J_0(N)\), the familiar retraction integer is the modular degree; the seed need not be silently identified with the optimal curve to use the general lemma.

**Corollary (the converse that must not be omitted).** For any fixed embedding \(i\),

\[
\begin{split}
&\exists p_0\ \forall\text{ good ordinary }p>p_0:
\Sha(E/\mathbf Q)[p]\subseteq\operatorname{Vis}_i\Sha(E/\mathbf Q)\\
&\hspace{15mm}\Longleftrightarrow
\exists p_1\ \forall\text{ good ordinary }p>p_1:
\Sha(E/\mathbf Q)[p]=0.
\end{split}
\tag{FV}
\]

The forward implication excludes the finitely many divisors of \(d\). The reverse implication is vacuous visibility of zero. It holds even for \(A_0=E\) with the identity embedding, which is modular. Therefore fixed visibility is logically a reformulation of this ordinary-tail component. It could still be useful if an independent geometric proof were available, but its statement alone is not evidence of lower difficulty. It is weaker than full FIN, which also needs the other regimes and depths.

## 5. No finite stock of admissible auxiliary primes

**Lemma 2.** For a prime \(\ell\nmid N\), put

\[
D_\ell=(\ell+1)^2-a_\ell(E)^2.
\]

Then \(D_\ell\ge(\ell-1)^2>0\), and admissibility of \(\ell\) for residual prime \(p\) implies \(p\mid D_\ell\).

**Proof.** Hasse gives \(a_\ell^2\le4\ell\). The divisibility is exactly the level-raising congruence \(a_\ell\equiv\pm(\ell+1)\pmod p\). ∎

For any predetermined finite set \(S\) of good auxiliary primes,

\[
C_S=\prod_{\ell\in S}D_\ell\ne0
\tag{C}
\]

has the consequence that **no** prime of \(S\) is admissible for any \(p\nmid C_S\). The empty product is 1. Thus a finite list of auxiliary levels cannot implement the nonempty level raisings in §3 for arbitrarily large \(p\). For the seed every partner there has \(r-1\ge2\) auxiliary prime factors.

The integer \(C_S\) is an obstruction to using a chosen auxiliary stock. It is **not** an integer containing all Sha primes. Reversing that interpretation would repeat the original support error.

## 6. Why functorial descent back to fixed levels loses the class

Merely proving that the construction must visit varying levels does not rule out a subsequent descent. The following result tests that additional step.

**Lemma 3 (the gluing obstruction).** Let \(V=E[p]\), let \(j_i:V\hookrightarrow F_i\) be finite subgroup embeddings, and let \(A_p\) and \(i_p:E\hookrightarrow A_p\) be \(G\). Suppose

\[
\operatorname{Hom}_{\mathbf Q}(F_i,A_0)=0\quad\text{for every }i.
\tag{H}
\]

Then every homomorphism \(h:A_p\to A_0\) kills \(i_p(E[p])\). Consequently, if \(i_0:E\hookrightarrow A_0\) is fixed and

\[
h\circ i_p=i_0\circ[u],\qquad u\in\mathbf Z,
\tag{T}
\]

then \(p\mid u\). In particular \(T\) is impossible for a \(p\)-unit \(u\).

**Proof.** Pull \(h\) back to \(E\times\prod F_i\). By \(H\) the resulting homomorphism is \((g,0,\ldots,0)\). It must kill the kernel of the quotient in \(G\). Applying it to \((-x,j_ix,0,\ldots)\) gives \(g(x)=0\) for every \(x\in E[p]\). If \(g=i_0[u]\), injectivity of \(i_0\) implies \([u]E[p]=0\), hence \(p\mid u\). ∎

The same obstruction holds for maps in \(\operatorname{Hom}\otimes\mathbf Z_{(p)}\), by clearing a denominator prime to \(p\). Allowing a denominator divisible by \(p\) does not give a defined \(p\)-unit map on the torsion classes.

**Theorem 4 (fixed-level transport obstruction).** Fix in advance finitely many levels \(M_1,\ldots,M_t\), and an abelian variety \(A_0\) which is a quotient of a product of the corresponding \(J_0(M_j)\). For all but finitely many residual primes \(p\), the ambients \(G\) produced in §3 admit no homomorphism to \(A_0\) satisfying \(T\) with \(p\nmid u\).

**Proof.** Let \(S\) be the primes dividing some \(M_j\) but not \(N\). Outside the finite support of \(C\), no admissible prime lies in \(S\). Every partner \(F_i\) has a nonempty auxiliary level and thus has a new prime \(\ell\nmid\prod_jM_j\). It is a \(\mathbf Q\)-simple newform factor of exact level \(Nm_i\), new at this \(\ell\). Its characteristic-zero representation is ramified there (Steinberg), whereas \(A_0\) has good reduction at \(\ell\). It cannot be an isogeny factor of \(A_0\). A nonzero homomorphism from a simple \(F_i\) would make it such a factor, so \(H\) holds. Lemma 3 applies. ∎

This rules out using modular correspondences or homomorphisms of these abelian varieties to carry the visibility proof to predetermined levels while retaining the \(p\)-torsion information. A map whose restriction is divisible by \(p\) only yields that an already \(p\)-torsion class becomes zero after multiplication by \(p\), which supplies no new control.

The theorem does not say that the same class could never be shown visible in \(A_0\) by an unrelated argument. Nor does it prove that every conceivable ambient realizing the class must have unbounded level. Those stronger conclusions do not follow and would conflict with the vacuous case in \(FV\).

## 7. Why local triviality does not lower away the visibility extension

The local Kummer sequence is

\[
0\longrightarrow E(K_v)/pE(K_v)\longrightarrow
H^1(K_v,E[p])\longrightarrow H^1(K_v,E)[p]\longrightarrow0.
\]

A Sha class is zero in the **last** term. A Selmer lift of it may be a nonzero local Kummer class in the **middle** term. In fact the nonzero localizations in \(I\) are the information used to construct the basis. Sha local triviality cannot be substituted for vanishing of those localizations.

Moreover the residual representation of every partner is already \(E[p]\), of base level \(N\). Level lowering that representation does not lower the point on the partner, the anti-diagonal extension \(G\), or its map on \(H^1\). Theorem 4 identifies the obstruction to the proposed geometric transport rather than merely observing this logical distinction.

## 8. Decision and permanent constraints

* **Applicability:** direct use of the printed general theorem fails at squarefree \(N\); the ordinary seed's actual local hypotheses permit the written Zhang-based transfer in §3. No claim about the inaccessible published revision is needed.
* **Fixed-level test:** fails for a predetermined auxiliary stock (Lemma 2), and for descent by homomorphisms preserving \(E\) up to a \(p\)-unit (Theorem 4).
* **Horizontal content:** `NO_HORIZONTAL_GAIN`. The construction covers every class at each covered prime but gives no fixed Sha-support integer.
* **Integer extraction:** not reached. Neither \(C_S\) nor the retraction integer of an ambient lacking class coverage can be relabeled \(C_E\).
* **Scope:** no prime computation, new primary-depth result, FIN, order-nine result, or scalar identity. The nonsquarefree extension proved here is ordinary-only; supersingular applicability would need a separately justified transfer of the different rank-zero inputs. Even such varying-level applicability would still face the uniformity obstruction.

The fixed-level statement \(FV\) is equivalent to eventual ordinary vanishing, so a successor requires an independently justified new comparison, not a renamed fixed-level conjecture. The tested geometric descent is stopped. No repair or successor is launched by this report.

This operation contributes a correction to the historical direction label and a **scoped no-go compression**: finite auxiliary stocks and \(p\)-unit functorial descent of these level-raised ambients do not supply the missing horizontal bound. The possibility of a wholly different fixed-level proof remains open; it is not counted as progress or proposed as a new target.
