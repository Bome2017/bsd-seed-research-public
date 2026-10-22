# The two 3-primary proof seams for the fixed seed

Date: 2026-09-19, America/Los_Angeles. Written proof and primary-source audit, including self-review; neither independent referee acceptance nor a proof-assistant certificate. This is an addendum to the existing mathematical record, not a competing BSD map.

## 1. Statement and scope

Put

\[
E:y^2=x^3-22735x^2+106272484x,
\qquad N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843,
\qquad f=f_E.
\]

The two obligations examined here are:

* **R1:** justify the algebraic Iwasawa leading-term calculation at the nonsplit multiplicative prime 3, including the height and logarithmic normalization, without presupposing the finiteness being deduced.
* **R2:** justify the integral canonical/Gross-period comparison used to transfer Chida–Hsieh's anticyclotomic μ-vanishing to the normalization in Skinner–Urban Proposition 12.3.6, at the weight-two specialization \(f\).

**Result: R1 is closed by source recovery and a noncircular ordering of the proof. R2 is closed for this seed by the integral character-module argument in §3.** The latter is a written specialization argument using published multiplicity one and the supersingular description of the character group. It does not apply Chida–Hsieh Proposition 6.1 outside its hypotheses.

Consequently the retained exact coefficient and height certificates give

\[
\boxed{\Sha(E/\mathbf Q)[3^\infty]\simeq(\mathbf Z/3\mathbf Z)^2}
\]

without the two former R1/R2 qualifications. Other imported inputs keep their existing scope and provenance. In particular, this does not remove the Zywina/preprint qualification on the retained global basis theorem, independently replay the coefficient computation, or formalize Skinner's main conjecture proof.

**BSD endpoint:** this hardens an existing primary component of FIN and FORMULA. It proves neither global FIN, global order nine, nor \(q_\infty=36\). No exceptional-prime computation is part of this operation.

## 2. R1: the nonsplit theorem and the order of inference

### 2.1 What Jones actually supplies

Jones's author page supplies *Iwasawa L-functions for multiplicative abelian varieties* as `extra-zeros.ps`. The author copy has 27 pages in reverse physical order; the reading-order extraction reverses pages without changing their contents. Its pagination is not the journal pagination 399–420.

The relevant locations in this **author copy** are:

| Location | Mathematical content used |
|---|---|
| §1, pp. 1, 3–4 | \(p\ne2\); ordinary semistable reduction at primes above \(p\); nonsplit multiplicative reduction is explicitly included in the finite-index universal-norm hypothesis. Finiteness of the base primary Sha is a standing hypothesis. |
| Proposition 1.1, p. 5 | Order of a characteristic series bounds the rank of its augmentation specialization. |
| §2, p. 8 | \(h_p=\log_p\kappa(\gamma)\,h_\gamma\). |
| Theorem 2.7, pp. 11–12 | Algebraic leading coefficient expressed through the height determinant, primary Sha, components, torsion, and a local factor. |
| Remark after Definition 2.9, p. 12 | The local factor for nonsplit multiplicative elliptic reduction is a \(p\)-adic unit. |
| Theorem 3.1 and its specialization, pp. 17–18 | Explicit nonsplit elliptic leading-term formula; no extra zero and no split Tate-period factor. |

Jones's published *p-adic heights for semi-stable abelian varieties*, Theorem 4.3, p. 49, identifies his algebraic height with the negative of Schneider's analytic height. Its hypotheses also allow \(p=3\). The sign does not affect determinant valuation. Stein–Wuthrich §4.2 and Theorem 6.1 identify the height used here with the canonical nonsplit height used by the retained regulator certificate. Their possible factor-of-two conventions are units at 3.

Sources: [Jones author page](https://hobbes.la.asu.edu/papers.html), [original author PostScript](https://hobbes.la.asu.edu/papers/extra-zeros.ps), [Jones 1990 published paper](https://www.numdam.org/item/CM_1990__73_1_31_0.pdf). The precise byte identities are in `sources/DOWNLOADS.json` and `sources/SOURCES.sha256`.

### 2.2 Finiteness comes before the Jones formula

Here is the required argument without assuming finiteness of \(\Sha[3^\infty]\). Write

\[
\Lambda=\mathbf Z_3[[T]],\quad
S_\infty=\operatorname{Sel}_{3^\infty}(E/\mathbf Q_\infty),\quad
X=S_\infty^\vee.
\]

The already checked local-condition comparison identifies this classical Selmer module with the module in Skinner's theorem. At 3 its unramified quotient has Frobenius (-1); the possible discrepancy is annihilated by the unit \(1-(-1)=2\), and is zero. The comparison is integral, not merely up to finite groups.

First,

\[
E[3^\infty](\mathbf Q_\infty)=0.
\tag{2.1}
\]

Indeed, \(E[3]^{G_{\mathbf Q_\infty}}\) is \(G_{\mathbf Q}\)-stable because \(\mathbf Q_\infty/\mathbf Q\) is Galois. Irreducibility makes it zero or all of (E[3]). The second case would make the image \(\mathrm{GL}_2(\mathbf F_3)\) a quotient of the procyclic pro-3 group \(\operatorname{Gal}(\mathbf Q_\infty/\mathbf Q)\), which is impossible. A nonzero point of higher 3-power order would give a nonzero point of order 3, proving (2.1).

Inflation–restriction therefore gives an injection on global \(H^1\), and restriction preserves local Kummer conditions. Thus

\[
\operatorname{Sel}_{3^\infty}(E/\mathbf Q)
\hookrightarrow S_\infty^\Gamma.
\tag{2.2}
\]

For every finitely generated torsion \(\Lambda\)-module \(X\),

\[
\operatorname{rank}_{\mathbf Z_3}(X/TX)
\leq\operatorname{ord}_{T=0}\operatorname{char}_\Lambda(X).
\tag{2.3}
\]

To see this, tensor with \(\mathbf Q_3\) and inspect the elementary divisors at \(T=0\): every block \(\Lambda/(T^e)\) contributes one to the left and \(e\ge1\) to the right. The finite errors of the structure theorem contribute to neither rank.

The Kummer exact sequence at the base gives

\[
2+\operatorname{corank}_{\mathbf Z_3}\Sha(E/\mathbf Q)[3^\infty]
=\operatorname{corank}_{\mathbf Z_3}\operatorname{Sel}_{3^\infty}(E/\mathbf Q)
\leq \operatorname{ord}_T\operatorname{char}_\Lambda(X).
\tag{2.4}
\]

Skinner's integral characteristic-ideal equality, with the R2 comparison justified below, and the retained certificate \(a_2\equiv9\pmod{27}\), show that the last order is at most two. Equation (2.4) shows it is at least two. Therefore it is exactly two and \(\Sha[3^\infty]\) has corank zero. This primary group is cofinitely generated, being a quotient of the base Selmer group, so corank zero means it is **finite**.

Only now apply Jones. The nondegeneracy hypothesis is supplied independently by the retained certified nonzero height determinant. This avoids using Jones's standing finiteness assumption to prove itself. No converse to Jones's conditional theorem is being silently imported.

### 2.3 Valuation and normalization

Take \(\kappa(\gamma)=4\). Passing from the \(s\)-variable to \(T=\kappa(\gamma)^{1-s}-1\) divides the rank-two leading coefficient by \((\log_3 4)^2\). Thus Jones gives the valuation formula

\[
v_3(F_E^*(0))=
v_3\#\Sha[3^\infty]
+v_3\!\left(\frac{\operatorname{Reg}_3(E)}{(\log_3 4)^2}\right)
+\sum_vv_3(c_v)-2v_3\#E(\mathbf Q)[3^\infty].
\tag{2.5}
\]

The nonsplit local multiplier is a 3-adic unit. In Stein–Wuthrich's notation it is \(\epsilon_3=1-a_3^{-1}=2\), also a unit. The statement is equality of valuations, not equality of leading coefficients with all unit factors fixed.

For the seed the retained inputs are

\[
v_3(F_E^*(0))=2,\quad
v_3(\operatorname{Reg}_3)=2,\quad
v_3(\log_3 4)=1,\quad
\prod_vc_v=16,\quad E(\mathbf Q)[3^\infty]=0.
\]

Consequently \(v_3\#\Sha[3^\infty]=2\). The finite primary group has its nondegenerate alternating Cassels–Tate pairing. A cyclic group of order nine cannot support such a pairing, so the group is \((\mathbf Z/3)^2\).

## 3. R2: an integral period comparison for the seed

Choose \(q=2243\), and put \(M=N/3\), \(m_q=N/q\). The two uses of level below are intentional: Wiles is applied at level \(3M=N\), and reduction at \(q\) identifies a character group with a definite quaternionic module of Eichler level \(m_q\), which **still contains 3**.

Let \(J=J_0(N)\), let \(\mathbb T\) be the full integral Hecke algebra, and let \(\mathfrak m\) be the maximal ideal given by \(f\bmod3\). Set

\[
A=\mathbb T_{\mathfrak m}^{\wedge},\qquad
\lambda:A\longrightarrow\mathbf Z_3,\qquad
I=\ker\lambda,\qquad
\eta_f(N)=\lambda(\operatorname{Ann}_A I).
\]

Here \(\eta_f(N)\) denotes an ideal; using a generator changes it by a unit. No numerical computation of \(A\) or of this ideal is needed.

### 3.1 Actual Jacobian multiplicity one at 3

Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Chapter 2 §1, Theorem 2.1(ii) and its two corollaries, applies:

* its standing assumption on p. 480 is \(p\ge3\), checked in the page image because OCR rendered it incorrectly as (p>3);
* \(3\nmid M\);
* \(\bar\rho_{f,3}\) is irreducible;
* \(U_3(f)=-1\) is a unit;
* the two ordinary residual characters at 3 are \(\bar\psi\bar\chi_3\) and \(\bar\psi\), with \(\psi\) unramified quadratic. Their restrictions to inertia differ because \(\bar\chi_3|_{I_3}\ne1\). Thus the maximal ideal is \(D_3\)-distinguished.

Wiles allows \(X_H\), including \(X_0\), explicitly on p. 480. Therefore

\[
\dim_{\mathbf F_3}J[\mathfrak m]=2,
\qquad T_3J_{\mathfrak m}\simeq A^2,
\qquad A\text{ is Gorenstein}.
\tag{3.1}
\]

These are conclusions about the **Jacobian and its Tate module**. The older characteristic-two inference from differential multiplicity one is not being used. Agashe Proposition 1.3 supplies a useful independent statement of the odd-prime \(p\Vert N\) case, but no unpublished theorem from that preprint is needed in place of Wiles here.

Source: [Wiles, published paper, pp. 480–488](https://sites.math.rutgers.edu/~zeilberg/EM22/AW1995.pdf).

### 3.2 Residual ramification forces rank one in the toric character module

Let 

\[
X_q=X^*(\mathcal T_q)\otimes\mathbf Z_3,
\]

where \(\mathcal T_q\) is the torus in the connected special fiber of \(J\) at \(q\). The retained local datum \(v_q(\Delta_{\min})=1\) gives nontrivial unipotent inertia on (E[3]), and hence

\[
\dim_{\mathbf F_3}J[\mathfrak m]^{I_q}=1.
\tag{3.2}
\]

There is no \(q\)-old Hecke factor after localizing at \(\mathfrak m\): an eigenform of level dividing (N/q) has an unramified residual representation at \(q\ne3\), whereas \(\bar\rho_{f,3}\) is ramified there. Thus the full localized algebra \(A\) equals its \(q\)-new quotient, and it acts faithfully on \((X_q)_{\mathfrak m}\).

The prime-to-\(q\) torsion of the special-fiber torus lifts into inertia-invariant torsion of the generic Jacobian. This is the usual finite-part statement for semistable reduction; equivalently, over the strict henselization multiplication by 3 is étale, and a torsion point of the special fiber has its unique torsion lift. The lift commutes with Hecke endomorphisms. Consequently

\[
\mathcal T_q[\mathfrak m](\overline{\mathbf F}_q)
\hookrightarrow J[\mathfrak m]^{I_q}.
\]

The dimension of the left side equals

\[
\dim_{\mathbf F_3}(X_q/\mathfrak m X_q),
\]

by torus/character duality. Faithfulness and Nakayama give a positive dimension, and (3.2) bounds it by one. Hence this dimension is one. Nakayama now gives a surjection \(A\to(X_q)_{\mathfrak m}\). Its kernel annihilates the whole target, and faithfulness makes that kernel zero. We have proved

\[
\boxed{(X_q)_{\mathfrak m}\simeq A.}
\tag{3.3}
\]

This is the ramified case of the character-module argument often called Mazur's principle. The proof above uses \(q\ne3\), genuine Jacobian multiplicity one, and residual ramification. It imposes neither squarefreeness of (N/q) nor \(3\nmid N\). Compare the mechanism in Pollack–Weston Theorem 6.2; their more restrictive global standing hypotheses are not asserted to hold here.

### 3.3 The definite module, including its small-prime denominators

Let \(B/\mathbf Q\) be definite of discriminant \(q\), and let \(R\subset B\) be an Eichler order of level \(m_q=N/q\). Denote its finite ideal-class set by \(\mathcal C\). Write \(D=\mathbf Z_3[\mathcal C]\) and \(S=\operatorname{Map}(\mathcal C,\mathbf Z_3)\).

Ribet's supersingular description, Proposition 3.1 and Proposition 3.3/Variant 3.4 on pp. 439–440, identifies the character lattice with the degree-zero supersingular divisor lattice at this Eichler level. It is an integral identification, not just a rational Jacquet–Langlands isomorphism. The quotient by the degree-zero lattice is a degree module on which good Hecke operators act by \(\ell+1\); localization at the irreducible residual representation kills it. Hence \(D_{\mathfrak m}=(X_q)_{\mathfrak m}\).

For a class \(s\), let \(w_s=\#\operatorname{Aut}(s)/2\). **Each \(w_s\) is a 3-adic unit in this example.** Indeed (q>3); 3-divisibility would give an order-three automorphism preserving the cyclic subgroup of order \(m_q\). Since \(2\mid m_q\), it would preserve a subgroup of order two. An order-three elliptic automorphism acts on 2-torsion with polynomial \(X^2+X+1\), irreducible over \(\mathbf F_2\), so no such subgroup exists. This also follows from Ribet's analysis of extra automorphisms in §4 of the component-group paper.

Thus the weighted pairing on functions, with the Atkin–Lehner operator \(\tau_{m_q}\),

\[
b_R(F,G)=\sum_{s\in\mathcal C}\frac{F(s)G(s\tau_{m_q})}{w_s},
\tag{3.4}
\]

is a perfect \(\mathbf Z_3\)-pairing. It is exactly the weight-two pairing of Chida–Hsieh (6.1). All Hecke operators are self-adjoint for this twisted pairing, as verified immediately after that equation. The twist is an integral permutation; it does not introduce an index.

Here is the variance check. Evaluation identifies functions with the integral dual of divisors. The correspondence induced by a Hecke double coset on divisors acts by its transpose on this dual; the Atkin–Lehner involution conjugates that transpose convention to the function convention in (3.4). This can be checked directly by counting the arrows of the double-coset correspondence, including their automorphism weights. The weights are units here, so no denominator is lost on localization. Thus the function module is the integral dual of the character module, up to the indicated integral Atkin–Lehner identification. By (3.3) it is isomorphic to \(\operatorname{Hom}_{\mathbf Z_3}(A,\mathbf Z_3)\); by the Gorenstein conclusion in (3.1), this is free of rank one over \(A\). In particular,

\[
\boxed{S_{\mathfrak m}\simeq A\quad\text{as Hecke modules}.}
\tag{3.5}
\]

The localized Hecke algebra on \(S\) is \(A\): the \(q\)-old part was excluded in §3.2 and the supersingular/Jacquet–Langlands identification matches the Hecke operators integrally. No transfer to a different indefinite Shimura Jacobian is required, since \(N^-=q\) has just one prime.

Sources: [Ribet 1990, pp. 439–441](https://math.berkeley.edu/~ribet/Articles/invent_100.pdf), [Ribet, component groups, §§3–4](https://math.berkeley.edu/~ribet/Articles/hk.pdf), [Chida–Hsieh, (6.1)](https://arxiv.org/pdf/1204.2427v3).

### 3.4 The pairing computes the congruence ideal

We use the following elementary integral lemma, spelling it out to avoid replacing the missing comparison by a name.

**Lemma.** Let \(A\) be a finite flat local \(\mathbf Z_3\)-algebra, \(\lambda:A\to\mathbf Z_3\) a surjection, and \(I=\ker\lambda\). Let \(S\simeq A\) carry a perfect \(\mathbf Z_3\)-bilinear pairing satisfying \(b(ax,y)=b(x,ay)\). If \(g\) generates the saturated eigenline (S[I]) over \(\mathbf Z_3\), then

\[
(b(g,g))=\lambda(\operatorname{Ann}_A I).
\tag{3.6}
\]

**Proof.** Choose an \(A\)-basis \(e\) of \(S\), and set \(\ell(t)=b(e,te)\). Perfection identifies \(A\) with its \(\mathbf Z_3\)-dual by \(a\mapsto[t\mapsto\ell(at)]\). The preimage \(a\) of the primitive functional \(\lambda\) satisfies \(\ell(at)=\lambda(t)\). This identifies \(\operatorname{Ann}_A I\) with \(\operatorname{Hom}_{\mathbf Z_3}(A/I,\mathbf Z_3)\), so \(\operatorname{Ann}_A I=\mathbf Z_3a\) and \(ae\) is primitive. Therefore \(g=u ae\), \(u\in\mathbf Z_3^\times\), and \(b(g,g)=u^2\ell(a^2)=u^2\lambda(a)\). This generates the stated ideal. □

Chida–Hsieh's p-adically normalized quaternionic form is a generator of precisely this integral eigenline (their normalization preceding §4.2). Applying (3.6) to (3.5) and (3.4) proves

\[
\boxed{(\xi_f(N/q,q))=\eta_f(N),\qquad
v_3\bigl(\eta_f(N)/\xi_f(N/q,q)\bigr)=0.}
\tag{3.7}
\]

In particular, freeness has actually been proved in the needed setting. It is not being inferred from residual ramification alone, from a rational Jacquet–Langlands correspondence, or from a general congruence/Selmer slogan.

### 3.5 Which canonical period is being compared

There are two canonical-period presentations to match: the congruence-ideal normalization in Chida–Hsieh §6 and the primitive cohomology periods \(\Omega_f^\pm\) in Skinner–Urban §3.3.3.

Here

\[
3\nmid\varphi(N)
=4\cdot2\cdot2242\cdot4547\cdot4546\cdot5842.
\tag{3.8}
\]

Thus the degree of \(X_1(N)\to X_0(N)\) is a 3-adic unit. Pullback and trace identify the trivial-diamond cohomology lattices integrally at 3. In particular a primitive eigenclass remains primitive: applying trace and dividing by the unit degree would otherwise make the original class divisible by 3. Averaging over the diamond group likewise identifies the localized trivial-character Hecke algebras. This checks the otherwise potentially nonunit \(\Gamma_0/\Gamma_1\) change.

For completeness, the cohomological period/congruence comparison has a lattice proof. By (3.1), integral cohomology at \(\mathfrak m\) is free of rank two over \(A\). The boundary cohomology is Eisenstein and vanishes after this localization. There is no order-three elliptic-point torsion: \(2\mid N\) excludes elliptic points of order three on \(X_0(N)\). Complex conjugation splits compact cohomology into two free rank-one \(A\)-modules, since 2 is a unit and its residual eigenvalues are \(+1,-1\). The cup product, composed with the integral Atkin–Lehner involution, perfectly pairs these modules and makes Hecke operators self-adjoint (the same adjoint identity as Wiles (2.3)).

Apply the two-module version of the lemma in §3.4: use bases \(e_+,e_-\) and the functional \(t\mapsto b(e_+,te_-)\). Perfection again identifies the preimage of \(\lambda\) with a generator of \(\operatorname{Ann}_A I\); the pairing of primitive eigenvectors therefore generates \(\eta_f(N)\). Removing the Atkin–Lehner twist multiplies it by the newform's eigenvalue \(\pm1\). For \(\omega=f(z)dz=\Omega_0^+c^++\Omega_0^-c^-\), Riemann's bilinear identity gives, up to the orientation sign,

\[
\Omega_0^+\Omega_0^-\,\langle c^+,c^-\rangle
=i\int_{\Gamma_0(N)\backslash\mathfrak H}|f(z)|^2\,dx\,dy.
\tag{3.8a}
\]

The periods \(\Omega_0^\pm\) and SU's \(\Omega_f^\pm\) differ by 3-adic units, by the trace argument above. This computes the relevant congruence/period valuation directly.

The normalization can also be cross-checked in SU Lemma 12.2.2, which states it for ordinary forms of level \(Mp^r\), including \(p\mid N\). At weight two its factor \(2^{-3}(2i)^{k+1}\) is \(-i\); its factor \(S(f)=a_p^{-r}p^{r(k/2-1)}W'(f)^{-1}\) is a 3-unit because \(a_3=-1\), \(k=2\), and \(W'(f)\) is a 3-unit as stated before SU (11.7.3.b). Thus this cross-check does not import a good-at-3 period theorem.

CH §3.3 uses the unnormalized Petersson integral: the inverse compact volume in its definition cancels the compact volume in the adelic integral. In particular its displayed \(\zeta_{\mathbf Q}(2)N\prod_{\ell\mid N}(1+\ell^{-1})\) is not an additional factor multiplying the classical Petersson norm. The archimedean Whittaker vector in CH §1.4 is the usual adelization of the normalized form. Finally \((4\pi)^2/(-2\pi i)^2=-4\), a 3-unit. These observations and (3.8a) check all possible nonunit normalization factors; no \(\Gamma_0/\Gamma_1\) index or factor of 3 is omitted. Together with (3.7) they give

\[
\boxed{
\frac{\Omega_{f,q}}{(-2\pi i)^2\Omega_f^+\Omega_f^-}
\text{ is algebraic and a 3-adic unit}.
}
\tag{3.9}
\]

Only a unit comparison is asserted. No numerical complex or p-adic period approximation is used to prove (3.9).

### 3.6 Application to the exact μ-vanishing step

Choose an imaginary quadratic field \(K\) with \(q\) inert, every prime of (N/q) split, and discriminant prime to \(N\). Such choices exist by the usual prescribed quadratic splitting conditions. Take \(N^-=q\); Chida–Hsieh's Eichler level is \(3N^+=N/q\).

Their Theorem C, equivalently detailed Theorem 5.7, applies at weight two and \(p=3\): \(3>k-2=0\), the ordinary eigenvalue is (-1), the residual representation is absolutely irreducible, and \(r_0=0\) because the discriminant is prime to \(q\). The condition (ST) is vacuous and \(3\nmid2^{r_0}\). These are the hypotheses of the μ theorem, not the stronger hypotheses of their period-comparison Proposition 6.1. The detailed theorem permits the finite tame branch character required by SU as well as the trivial branch. It gives \(\mu(\Theta_\infty)=0\), hence \(\mu(\Theta_\infty^2)=0\).

Equation (3.9) transfers this to canonical normalization. To check the conductor factors, take a sufficiently ramified anticyclotomic character of conductor \(3^n\). Since 3 splits in \(K\), its two local characters are inverses, and the Gauss-sum identity \(\tau(\chi)\tau(\chi^{-1})=\chi(-1)3^n\) changes SU's Gauss factor into CH's \(3^n\), up to a unit. Both ordinary factors are \(a_3^{-2n}\), and CH's ramified interpolation multiplier is 1. The remaining factors from \(D_K\), \(u_K\), signs and powers of 2 are 3-units; \(3\nmid D_K\) and \(u_K=1\). Character evaluations at fixed ideals give group-ring translation units. Thus the interpolation comparison of SU §12.3.5 preserves μ in this setting. The removed Euler factors have μ zero as in that section. Therefore

\[
\mu(L^{\Sigma,-}_{f,K,\xi})=0
\]

in the normalization required by Proposition 12.3.6. Its weight-two specialization now supplies a unit coefficient in the three-variable argument. This is the specialization used for the Hida family through the higher-weight good-at-3 forms in Skinner's proof of Theorem A.

**No unit-factor ambiguity at this step remains from R2.** The rest of Skinner's published argument and the previously checked Selmer and Néron-period identifications are retained inputs; this addendum is not an independent reproof of every theorem in that argument.

## 4. Checks against the prior failure modes

| Potential invalid shortcut | What the proof above does |
|---|---|
| Jones assumes finite primary Sha | Derive finiteness first by (2.1)–(2.4). |
| Differential multiplicity one is not Jacobian multiplicity one | Apply Wiles's actual Jacobian theorem, with all ordinary/distinguished hypotheses checked. |
| A prime-to-p theorem was applied at \(p\mid N\) | Apply Wiles at (3M), with \(3\nmid M\); keep 3 in the quaternionic Eichler level. |
| Freeness at p=3 was assumed from a p≥5 source | Prove (3.3) using the one-dimensional inertia invariants. |
| Rational Jacquet–Langlands correspondence fixes an integral index | Use the integral supersingular lattice and check stabilizer denominators. |
| Γ₁ and Γ₀ periods may differ by p | Check \(3\nmid\varphi(N)\) and use trace. |
| Congruence norm equals the congruence ideal without freeness | Prove freeness and the elementary pairing lemma before (3.7). |
| CH μ=0 automatically means canonical μ=0 | Insert (3.7)–(3.9) explicitly. |
| A congruence produces only a lower-bound Selmer class | No such implication is used: this is an integral-normalization repair inside the already chosen main-conjecture proof. |
| A local upgrade proves full BSD | The conclusion is the existing 3-primary theorem only. |

The targeted successor citations do not themselves close R2: Haining Wang (not Xin Wan), arXiv:2006.11640, assumes \(\ell>k+1\); Kim–Ota assumes \(p\ge5\) and \(p\nmid N\); Chida–Hsieh Proposition 6.1 has the stated incompatible hypotheses. The retrieved Chida–Hsieh erratum concerns their separate 2015 anticyclotomic-main-conjecture paper and is not an erratum to the μ-vanishing theorem used here. None is silently substituted for the proof in §3.

## 5. Exact supersession and unchanged endpoint

The original p=3 computation and its sealed manifest are unchanged. This addendum replaces only:

1. F1 R1's assertion that Jones was inaccessible/unread, and the resulting unverified nonsplit-source status;
2. F1 R2 and the later period-provenance addendum's assertion that the needed seed specialization remained unproved;
3. the later addendum's overbroad statement that the multiplicity-one/character-module methods all require \(p\ge5\) or \(p\nmid N\). Wiles Theorem 2.1(ii) explicitly covers the ordinary distinguished \(p=3\Vert N\) case used here. The cited CH, PW, and Kim–Ota period theorems still do not directly cover this seed.

It preserves their correct cautions about Kato at multiplicative p: both Iwasawa divisibilities in this chain still come from Skinner Theorem A. It does not manufacture an independent Kato upper bound.

The final implication chain is

\[
\begin{gathered}
\text{(3.1)–(3.9) + CH μ=0}
\Longrightarrow \text{the R2 specialization in SU is justified}\\
\Longrightarrow \text{Skinner's integral equality for the retained Selmer module}\\
\Longrightarrow \operatorname{ord}_TF_E=2
\Longrightarrow \Sha[3^\infty]\text{ finite}\\
\Longrightarrow \text{Jones + the retained height certificate gives order }9\\
\Longrightarrow \Sha[3^\infty]\simeq(\mathbf Z/3)^2.
\end{gathered}
\]

The new work consists of source checking, the noncircular finiteness argument, and the written integral comparison; the numerical inputs are the already certified ones. Global FIN, \(\#\Sha=9\), and \(q_\infty=36\) remain open in the [master record](../../MASTER_BSD_DAG.md). The exact superseded inputs are [F1's hostile audit](/Users/bsm/BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F1_P3_HOSTILE_AUDIT.md) and the [period-provenance addendum](/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/addenda/P3_R2_PERIOD_PROVENANCE_AUDIT.md); the retained numerical theorem is [SHA3_THEOREM.md](/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/SHA3_THEOREM.md).
