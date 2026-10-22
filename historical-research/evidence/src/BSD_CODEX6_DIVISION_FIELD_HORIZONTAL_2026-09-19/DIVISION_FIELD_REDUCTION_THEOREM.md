# The exact division-field obstruction for the fixed seed

Date: 2026-09-19. Status: mathematical derivation, not machine formalization or an independent referee audit. The seed inputs are retained from the current project record; no FIN assumption is used.

## 1. The theorem actually established

Let

\[
 E:y^2=x^3-22735x^2+106272484x,\qquad
 \mathcal T=\{19,59,487,2243,4547,5843\}.
\]

For every prime \(p\ge7\) outside \(\mathcal T\), put

\[
 V=E[p],\quad K=\mathbf Q(E[p]),\quad
 G=\operatorname{Gal}(K/\mathbf Q)=\mathrm{GL}_2(\mathbf F_p),
\]
\[
 A=\mathrm{Cl}(K)/p\mathrm{Cl}(K),\quad
 C=\operatorname{Hom}_G(A,V),\quad m_p=\dim_{\mathbf F_p} C.
\]

Then

\[
 \boxed{\Sha(E/\mathbf Q)[p]=0\quad\Longleftrightarrow\quad m_p\le2.} \tag{1}
\]

In fact \(m_p\ge1\), and the stronger exact dimension relation is

\[
 \boxed{\dim\Sha[p]=2\left\lfloor\frac{m_p-1}{2}\right\rfloor.} \tag{2}
\]

Thus the assertion \(C=0\) is false for this seed throughout this range, even if Sha vanishes. The correct object is its contribution in excess of the everywhere unramified Mordell–Weil classes, defined in §7.

For every good prime \(p\ge7\), the minimal modulus permitted by the *local Kummer conditions*, before imposing global existence, is

\[
 \boxed{\mathfrak m=\prod_{w\mid p}\mathfrak p_w^{,2}.} \tag{3}
\]

There are no modulus factors away from \(p\), including at the five bad primes. At \(p\notin\mathcal T\), with \(R=\mathrm{Cl}_{\mathfrak m}(K)/p\), there are canonical identifications

\[
 \operatorname{Hom}_G(R,V)\simeq\operatorname{Sel}_p(E),\qquad
 C\simeq\ker\bigl(\operatorname{Sel}_p(E)\longrightarrow E(\mathbf Q_p)/p\bigr). \tag{4}
\]

The conductor-two assertion and the local representation calculation are proved in [LOCAL_CONDUCTOR_AND_MODULES.md](LOCAL_CONDUCTOR_AND_MODULES.md).

**Range boundary.** In particular (1)–(4) hold for every prime \(p>5843\). This is a cutoff for a proved *reduction*, not a cutoff beyond which Sha has been shown to vanish. The general filtered construction in §8 also defines the exact object at the six excluded parameters. The explicit conductor-two calculation is for good \(p\); it is not asserted at \(p=2243,4547,5843\). Those finitely many parameters are excluded from the tail theorem, not silently treated as solved. No exceptional-prime Sha computation is performed.

## 2. Retained seed input and what it does

The current [seed record](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/SEED_PROVED_STATE.md) supplies:

* \(E(\mathbf Q)=\mathbf Z/2\oplus\mathbf Z^2\), with saturated free basis \(P_1=(4547,327384)\), \(P_2=(5184,281520)\).
* Full residual image \(\mathrm{GL}_2(\mathbf F_p)\) for every odd prime.
* Bad reduction and component data in the table below; root number \(+1\) and analytic rank two.

| Rational prime \(q\) | Reduction | Rational Tamagawa number | Geometric component order |
|---|---|---:|---:|
| 2 | additive \(I_1^*\) | 2 | 4 |
| 3 | nonsplit multiplicative \(I_2\) | 2 | 2 |
| 2243 | split multiplicative \(I_1\) | 1 | 1 |
| 4547 | additive III, potentially good supersingular | 2 | 2 |
| 5843 | nonsplit multiplicative \(I_2\) | 2 | 2 |

At 4547, for coefficient primes \(p\ne4547\), tame inertia has order four and its square acts as \(-I\). At the multiplicative primes, \(p\ge7\) does not divide the relevant minimal-discriminant valuations 1 or 2, so the residual inertia contains the Tate transvection. These statements about inertia at 4547 are not statements about its own 4547-adic representation.

The earlier \(p=3,5\) certificates, their provenance seams, and any FORMULA claim are not inputs to this theorem.

At every good \(p\ge7\), rational 2-torsion makes \(\#E(\mathbf F_p)\) even. Hasse's bound puts this order strictly between 0 and \(2p\). Its only possible positive multiple of \(p\) would be the odd number \(p\). Therefore

\[
 p\nmid\#E(\mathbf F_p),\quad E(\mathbf Q_p)[p]=0,\quad
 \dim E(\mathbf Q_p)/p=1. \tag{5}
\]

This seed-specific absence of anomalous primes is used for *every* good \(p\), ordinary or supersingular.

## 3. Restriction, inflation, and the necessary Mordell–Weil quotient

The center of \(G\) contains \(-I\). Its action on \(V\) is multiplication by \(-1\). The central-element cohomology identity says that \((-I)-1=-2\) annihilates \(H^i(G,V)\). Since \(-2\) is invertible in \(\mathbf F_p\),

\[
 H^i(G,V)=0\quad(i\ge0). \tag{6}
\]

This can also be proved by taking invariants under the prime-to-\(p\) central subgroup \(\{\pm I\}\): its higher cohomology and its invariants on \(V\) both vanish, and the Hochschild–Serre spectral sequence is zero. In particular *both* \(H^1\) and \(H^2\) vanish.

Consequently restriction is an isomorphism, not just an injection:

\[
 H^1(\mathbf Q,V)\xrightarrow{\sim}H^1(K,V)^G
 =\operatorname{Hom}_G(G_K^{\mathrm{ab}}/p,V). \tag{7}
\]

The action on the abelianized group is well-defined independently of a lift of an element of \(G\); inner conjugation by \(G_K\) disappears there.

A Sha class is an equivalence class of Selmer lifts. It does not have a preferred lift to \(H^1(\mathbf Q,V)\). With

\[
 W=\delta(E(\mathbf Q)/p),\qquad \dim W=2,
\]

the exact sequence is

\[
 0\longrightarrow W\longrightarrow\operatorname{Sel}_p(E)
 \longrightarrow\Sha[p]\longrightarrow0. \tag{8}
\]

A nonzero lift restricts to a nonzero equivariant homomorphism in (7), and its image is all of the simple module \(V\). But changing the lift by \(W\) changes that homomorphism. Any argument that puts *all* Selmer lifts in a class-field container and then proves that the container has no \(V\)-quotient would also incorrectly annihilate the two rational-point classes.

## 4. Removing ramification away from the coefficient prime

Fix \(q\ne p\). Over \(\mathbf Q_q^{\mathrm{ur}}\), multiplication by \(p\) is surjective on the formal group, on the connected special fiber, and on every geometric component group in the table. For the connected fiber this follows respectively from multiplication on \(\mathbf G_a\), \(\mathbf G_m\), or an elliptic curve over an algebraic closure of the residue field. All its required preimages are defined over a finite unramified extension. Therefore

\[
 E(\mathbf Q_q^{\mathrm{ur}})/p=0. \tag{9}
\]

Every local Kummer class of a rational point in \(E(\mathbf Q_q)\) thus restricts to zero in \(H^1(I_q,V)\). After passing to \(K\), its class-field homomorphism annihilates \(\mathcal O_{K_w}^{\times}\). The conductor exponent is **zero** at every \(w\mid q\), not one. This holds for all \(p\ge7\), including the three coefficient primes of bad reduction as long as \(q\ne p\).

At real places odd-primary cohomology is zero. Moreover \(K\) contains \(\mu_p\) by the Weil pairing and is totally imaginary. There is no archimedean ray condition.

The converse—unramified over \(K\) implies the Selmer condition over \(\mathbf Q\)—requires care at bad primes because restriction on local cohomology need not be injective. We avoid silently assuming it. The local Tate Euler characteristic gives, for \(q\ne p\),

\[
 \dim H^1(\mathbf Q_q,V)=2\dim E(\mathbf Q_q)[p]. \tag{10}
\]

At additive \(q=2,4547\), no such \(p\)-torsion exists. At multiplicative primes the component order is prime to \(p\), and any such torsion is in the torus. The only possible parameters are

\[
 p\mid2243-1=2\cdot19\cdot59,
 \quad p\mid5843+1=2^2\cdot3\cdot487;
\]

the nonsplit torus at 3 contributes only divisors of 4. This gives the three additional exclusions \(19,59,487\). For \(p\notin\mathcal T\), all bad-prime groups in (10) are zero. At a good \(q\ne p\), the usual unramified cohomology group is exactly the Kummer local condition, and \(K/\mathbf Q\) is unramified there. This proves the required converse away from \(p\) in the theorem's range.

## 5. The ray container and its single local contribution

The local proof establishes at a good \(p\ge7\):

1. The nonzero local Kummer line has conductor exactly two over \(K_w\).
2. If \(D_w=\operatorname{Gal}(K_w/\mathbf Q_p)\) and \(U_w^i=1+\mathfrak p_w^i\), then
   \[
   \dim\operatorname{Hom}_{D_w}(U_w^1/U_w^2,V)=1.
   \]
3. \(H^1(D_w,V)=0\), \(H^1(I_w^{\mathrm{image}},V)=0\), and \(H^1_{\mathrm{ur}}(\mathbf Q_p,V)=0\).

Here \(I_w^{\mathrm{image}}\) is the finite image of \(I_p\) acting on \(V\), not the absolute inertia group. Restriction therefore does not hide a local class or turn a ramified local class into an unramified one.

Frobenius reciprocity identifies the possible global ray source at \(p\) with this same one-dimensional Hom space:

\[
 \operatorname{Hom}_G\left(\bigoplus_{w\mid p}U_w^1/U_w^2,V\right)
 \simeq\operatorname{Hom}_{D_w}(U_w^1/U_w^2,V). \tag{11}
\]

Any descended cohomology class of conductor at most two restricts at \(p\) into a space of dimension at most one: restricting a homomorphism to units is injective, since an unramified equivariant homomorphism would take values in \(V^{D_w}=0\). The Kummer line already occupies that one-dimensional space. Thus the conductor-two condition is exactly the Kummer condition for descended classes.

Combining this with §4 proves the first identification in (4). For the ordinary class group, being unramified over \(K_w\) forces the descended class to be unramified over \(\mathbf Q_p\), using \(H^1(I_w^{\mathrm{image}},V)=0\). It is consequently zero by assertion 3. Conversely every Selmer class with zero localization at \(p\) is everywhere unramified over \(K\). This proves the second identification in (4).

The ray exact sequence gives a right-exact sequence

\[
 \bigoplus_{w\mid p}U_w^1/U_w^2\longrightarrow R\longrightarrow A\longrightarrow0.
\]

Global units and class-group relations can impose a kernel on its first arrow. We do **not** assert that this arrow is injective, nor that the sequence splits as a \(G\)-module. Applying Hom yields the exact beginning

\[
 0\longrightarrow C\longrightarrow\operatorname{Hom}_G(R,V)
 \longrightarrow\operatorname{Hom}_G\left(\bigoplus_{w\mid p}U_w^1/U_w^2,V\right).
 \tag{12}
\]

Thus the entire ray correction has dimension at most one; it is a genuine possible contribution, not a representation-theoretic zero.

## 6. Parity without assuming FIN; proof of the class-group criterion

Write \(s_p=\dim\Sha[p]\) and \(r_p=\dim\operatorname{loc}_p\operatorname{Sel}_p(E)\in\{0,1\}\). Equations (4) and (8) give

\[
 m_p=2+s_p-r_p. \tag{13}
\]

We require that \(s_p\) is even **without assuming Sha finite**. For completeness, write the cofinitely generated \(p\)-primary Sha group as

\[
 \Sha[p^\infty]\simeq(\mathbf Q_p/\mathbf Z_p)^{d_p}\oplus F_p,
\]

where \(F_p\) is finite. Unconditional \(p\)-parity for elliptic curves over \(\mathbf Q\) gives

\[
 2+d_p=\operatorname{corank}_{\mathbf Z_p}\operatorname{Sel}_{p^\infty}(E)
 \equiv\operatorname{ord}_{s=1}L(E,s)=2\pmod2.
\]

Hence \(d_p\) is even. The Cassels–Tate pairing is nondegenerate on the quotient by the maximal divisible subgroup and alternating for an elliptic curve. The elementary divisors of \(F_p\) are consequently paired, so \(\dim F_p[p]\) is even. Therefore \(s_p=d_p+\dim F_p[p]\) is even.

Sources for these two independent inputs: [Dokchitser–Dokchitser, Theorem 1.4 / 4.19](https://arxiv.org/pdf/math/0610290) and [Poonen–Stoll, Cassels–Tate pairing](https://math.mit.edu/~poonen/papers/sha.pdf). The first theorem is unconditional; the adjacent theorem concerning ordinary Mordell–Weil parity over general number fields has different hypotheses and is not used.

Now (13) says \(m_p\) is either \(s_p+1\) or \(s_p+2\). With \(s_p\) even, this proves (1) and (2). It also proves \(m_p\ge1\) without using any finiteness conjecture.

The surviving one-dimensional ray contribution cannot alone support a nonzero even-dimensional \(\Sha[p]\). This removes it from the *vanishing test*. It does not prove that the ray contribution itself vanishes.

Finally, \(\Sha[p]=0\) is equivalent to \(\Sha[p^\infty]=0\): a nonzero element of any \(p\)-power order has a nonzero multiple of order \(p\). No finiteness assumption is needed for this step.

## 7. A canonical corrected object \(X_p\)

We must use \(\mathrm{Cl}(K)/p\mathrm{Cl}(K)\), not replace it without justification by \(\mathrm{Cl}(K)[p]\). There is no canonical identification of those two \(\mathbf F_p[G]\)-modules in this modular situation. Nor is the multiplicity in an arbitrary semisimplification automatically the dimension of Hom to \(V\).

For a finite \(\mathbf F_p[G]\)-module \(M\), define its maximal \(V\)-isotypic semisimple quotient by

\[
 M^{(V)}=M/\bigcap_{\phi\in\operatorname{Hom}_G(M,V)}\ker\phi.
\]

Evaluation identifies it canonically with

\[
 M^{(V)}\simeq V\otimes_{\mathbf F_p}\operatorname{Hom}_G(M,V)^*.
\]

Indeed it embeds in a direct sum of copies of the simple module \(V\), and \(\operatorname{End}_G(V)=\mathbf F_p\). This does not assume that \(\mathbf F_p[G]\) is semisimple.

Let \(W_0=W\cap C\), the Kummer classes of rational points that are locally \(p\)-divisible at \(p\). It is determined by the given rational basis and the local condition, without knowing Sha. Define

\[
 \boxed{X_p=\ker\left(A^{(V)}\longrightarrow V\otimes W_0^*\right).} \tag{14}
\]

This is a canonical **submodule of a quotient** of the ordinary class group; it is not asserted to be a canonical quotient of the entire class group. In class-field terms it is the relative Galois group after removing the unramified extensions supplied by the rational-point classes, inside the maximal unramified elementary \(p\)-extension with \(V\)-isotypic Galois module.

Let \(I=\operatorname{loc}_p\operatorname{Sel}_p(E)\), \(I^{\mathrm{MW}}=\operatorname{loc}_p W\). The exact comparison is

\[
 \boxed{0\longrightarrow\operatorname{Hom}_G(X_p,V)
 \longrightarrow\Sha[p]\longrightarrow I/I^{\mathrm{MW}}\longrightarrow0.} \tag{15}
\]

To prove it, first identify \(\operatorname{Hom}_G(X_p,V)=C/W_0\) using (14), then quotient the kernel-image sequence for localization by the corresponding sequence for \(W\). The last term has dimension at most one.

There is generally no canonical injection in the *opposite* direction requested schematically in the brief. Nevertheless parity proves the exact endpoint equivalence

\[
 \boxed{\operatorname{Hom}_G(X_p,V)=0\quad\Longleftrightarrow\quad\Sha[p]=0.} \tag{16}
\]

We do not assume that the images of \(P_1,P_2\) span the local Kummer line for every \(p\). If their local span is zero, (15) still holds and parity still proves (16).

If an object with Hom *equal* to Sha is desired, the ray version is

\[
 X_p^{\mathrm{ray}}=\ker\left(R^{(V)}\longrightarrow V\otimes W^*\right),
 \qquad\operatorname{Hom}_G(X_p^{\mathrm{ray}},V)\simeq\Sha[p].
\]

This is an exact representation of (8), not a difficulty reduction. The ordinary object (14) is the sharper container for the vanishing test because (15) and parity have already disposed of the only allowed ray direction.

## 8. All-parameter construction and finite exclusions

For every \(p\ge7\), (7) and (8) remain valid. Write \(L_q=\delta_q(E(\mathbf Q_q)/p)\). For \(w\mid q\), local reciprocity turns the restriction of a class in \(L_q\) into a homomorphism \(K_w^\times/K_w^{\times p}\to V\). Define its common kernel

\[
 N_{q,w}=\bigcap_{c\in L_q}\ker(\operatorname{res}_{K_w}c\circ\operatorname{Art}_{K_w}).
\]

These are explicit local norm subgroups specified by actual Kummer conditions. The least conductor exponent is, by definition, the least \(n\ge0\) with \(U_w^n\subset N_{q,w}\), where \(U_w^0=\mathcal O_{K_w}^{\times}\). This gives the exact class-field modulus; no arbitrary large upper bound is substituted for the minimum. The calculations above determine \(n=0\) for \(q\ne p\), and the local supplement determines \(n=2\) for good \(p\).

Inside the Hom space of this ray class group, retain exactly those homomorphisms whose unique descent under (7) has localization in \(L_q\) at every \(q\). That is the exact filtered Selmer space. The same evaluation construction and quotient by \(W\) represents Sha, for every \(p\ge7\).

For \(p=19,59,487\), the good-prime modulus is still (3). The additional local descent filters at 2243 or 5843 must be retained. We have not promoted the unfiltered ordinary class group to the strict Selmer group at those parameters.

For \(p=2243,4547,5843\), the general norm-subgroup definition remains valid, but this operation does not evaluate the conductor exponent at \(q=p\). The good-reduction formal-group proof must not be applied there. This finite omission has no bearing on (1)–(16) for every \(p>5843\); it is an explicit boundary of this tail result, not a solved finite exception.

## 9. Attempted seed-specific upper bound and the first arithmetic wall

The remaining statement is precisely

\[
 \exists L\ \forall\text{ primes }p>L:\quad
 \dim\operatorname{Hom}_{\mathrm{GL}_2(\mathbf F_p)}
 \bigl(\mathrm{Cl}(\mathbf Q(E[p]))/p,E[p]\bigr)\le2. \tag{17}
\]

No independent proof of (17) was obtained. The local and representation-theoretic attack stops for identifiable reasons:

* The transvections and order-four inertia establish the residual image and remove the bad local possibilities. An *unramified extension of the division field* has no new inertia to contradict them. Its descended classes in \(C\) already satisfy all the local conditions.
* Full \(G\), its natural module, and all the displayed restrictions are compatible as representation data with arbitrary direct sums \(V^{\oplus n}\). This is not a claim that such modules are realized by the seed's class groups. It proves that the representation data alone give no bound \(n\le2\).
* The Weil pairing gives \(V^*(1)\simeq V\). A duality/reflection argument therefore does not exchange the unknown component for an independently controlled one here. The global unit or dual Selmer term still requires an arithmetic bound.
* The ray class sequence controls only the difference in (12). Bounds on that difference cannot bound its unramified kernel \(C\).
* The determinant character is cyclotomic, but a character-valued annihilator does not automatically annihilate the natural two-dimensional module. Congruence results for \(\operatorname{ad}^0(V)\) act on a different representation.
* A compatible family of Tate modules supplies no proved compatible family of these unramified class-field extensions or a characteristic-zero annihilator for their excess over Mordell–Weil.

The source audit checks the closest relevant results against the exact module and quantifiers in (17). Its outcome is bounded: no independently applicable horizontal upper-bound theorem was located, not that none can exist.

## 10. Converse and endpoint

Under the retained seed inputs, for all \(p\) in the theorem's range, (17) is equivalent to eventual \(\Sha[p]=0\). The pointwise assertion in (16) is likewise equivalent. This is **Stage D classification B**. A stricter assertion such as \(m_p=1\) would additionally require control of rational-point localization; no independent mechanism for that assertion was found either.

The operation therefore establishes an exact reduction, the compulsory Mordell–Weil correction, and removal of every local contribution from the tail vanishing test. It does not establish a strict reduction in difficulty or prove FIN. The varying fields and norm subgroups use actual locally soluble global Selmer classes; no fixed universal field, finite universal lift set, or trace-divisibility inference is used. The DM no-go theorems do not kill this corrected construction.

The first unresolved arithmetic assertion is (17). Work stops there.
