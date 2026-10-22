# Bounded Euler-factor reconciliation

**Verdict: IMPORTED_THEOREM_INTERNAL_INTERFACE_OPEN (the third authorized outcome).**

**3-primary theorem retained via Skinner Theorem A as published; internal provenance open at the Euler-removal interface.**

The bounded cleanup is finished. The written integral period comparison and conditional R1 deduction retain their review grades. The rejected primitive-to-imprimitive μ argument in the project's original §3.6 is not repaired. There is no new adverse conclusion about the 3-primary arithmetic, and no further internal R2 reconstruction is selected.

## 1. Exact source custody and scope

The proof read for Skinner's *Multiplicative reduction and the cyclotomic main conjecture for GL2* is the [published MSP PDF](https://msp.org/pjm/2016/283-1/pjm-v283-n1-p10-s.pdf), Pacific Journal of Mathematics 283 (2016), 171–200, DOI 10.2140/pjm.2016.283.171. The preserved local PDF is [Skinner2016_published.pdf](../p3_r1_r2_2026-09-19/sources/Skinner2016_published.pdf), SHA-256 `d270e8311b228e0e97f89a836d0363a58882c0bc2629c159871d2fc37b6b113c`.

For Skinner–Urban, the locally inspected body remains the [author copy](../p3_r1_r2_2026-09-19/sources/SkinnerUrban_MC.pdf), SHA-256 `f9faa40aa5e30eba705da88e3d68c8aa43069b5be01c1cc6ece212dd57879748`, supplied on [Urban's website](https://www.math.columbia.edu/~urban/eurp/MC.pdf). Its §§12.3.5–12.3.6 are on author-copy pages 201–202. This must not be relabeled a byte-verified copy of the journal version. The [publisher record](https://link.springer.com/article/10.1007/s00222-013-0448-1) verifies Inventiones mathematicae 195 (2014), 1–277 and DOI 10.1007/s00222-013-0448-1. The publisher PDF request exposed a subscription preview; the Princeton repository PDF request returned HTTP 401. The locally downloaded publisher HTML is an access-challenge response, not mathematical source text. Those access receipts do not validate the inaccessible journal body.

This operation reread the relevant published Skinner argument and its exact Euler identities. It did not rerun the arithmetic, reprove the integral period comparison, or audit every dependency of the imported main-conjecture theorem.

## 2. What is explicitly reconstructed in the published proof

Put \(\Lambda=\mathcal O[[\Gamma]]\). In Skinner's notation let \(C_f^\Sigma\) denote the characteristic ideal of the imprimitive Selmer dual, \(F_f^\Sigma\) its Fitting ideal, and \(\mathcal L_f^\Sigma\) the imprimitive cyclotomic p-adic L-function. Write

\[
\mathcal E_\Sigma=\prod_{\ell\in\Sigma\setminus\{p\}}
P_\ell(\Psi^{-1}\epsilon^{-1}(\operatorname{frob}_\ell)).
\]

Lemma 2.3.4(i), published page 184, and equation (2-4-2), page 186, give **the same factors on both sides**:

\[
C_f^\Sigma=C_f\,(\mathcal E_\Sigma),\qquad
\mathcal L_f^\Sigma=\mathcal L_f\mathcal E_\Sigma.
\tag{E1}
\]

Thus an already established integral equality
\(C_f^\Sigma=(\mathcal L_f^\Sigma)\) implies
\(C_f=(\mathcal L_f)\) by cancellation of the common nonzero principal ideal in the domain \(\Lambda\). The factor need not be a unit. For example, \((3a)=(3b)\) implies \((a)=(b)\) in this domain; it does not imply \(\mu(3a)=\mu(a)\).

This cancellation is a proved transition **after** integral equality has been established. It is not a repair of an earlier argument that uses primitive μ zero to establish an imprimitive unit coefficient.

For the seed, the cyclotomic factor over \(\mathbf Q\) at the split multiplicative prime \(q=2243\) is, by the formula immediately following (2-4-2),

\[
\mathcal E_q^{\mathbf Q}=1-q^{-1}\Psi^{-1}(\operatorname{frob}_q).
\tag{E2}
\]

Its augmentation is \(1-q^{-1}\not\equiv0\pmod3\), since \(q\equiv-1\pmod3\). Consequently it is even a unit for this seed over the cyclotomic algebra. It is a different factor from the inert base-change factor after anticyclotomic specialization. Confusing these two rings or factors would erase the precise distinction that caused the failed reconstruction.

## 3. How Theorem A actually reaches multiplicative reduction

Theorem A, published page 172, applies at \(p=3\): weight two has the required congruence, \(a_3=-1\) is a unit, the retained residual representation is irreducible, and \(2243\parallel N\) is residually ramified. The last condition is the retained local statement from \(v_{2243}(\Delta_{\min})=1\).

The proof in §3.1, pages 191–192, proceeds through higher-weight, good-ordinary Hida specializations \(f_m\) of tame level \(N/3\). In outline, with each arrow referring to the published result rather than an independent reconstruction of all its dependencies,

\[
\begin{aligned}
&\text{Theorem 2.5.2 for }f_m
&&\Longrightarrow C_{f_m}^\Sigma=(\mathcal L_{f_m}^\Sigma),\\
&\text{Proposition 2.3.3 and Lemma 2.3.4}
&&\Longrightarrow F_{f_m}^\Sigma=C_{f_m}^\Sigma,\\
&\text{Selmer congruence and (2-6-3)}
&&\Longrightarrow(F_f^\Sigma,p^m)=(\mathcal L_f^\Sigma,p^m)\quad\text{for all }m,\\
&\text{nonvanishing, torsion, and completeness}
&&\Longrightarrow C_f^\Sigma=(\mathcal L_f^\Sigma),\\
&\text{(E1)}&&\Longrightarrow C_f=(\mathcal L_f).
\end{aligned}
\tag{E3}
\]

This published route does not require the project to prove primitive-to-imprimitive anticyclotomic μ preservation for the seed as an additional hypothesis. However, Theorem 2.5.2 itself imports the good-ordinary Skinner–Urban/Kato theorem. Thus (E3) is **not** an independent bypass of the unresolved internal SU normalization question. It identifies the published theorem being used and prevents the failed local reconstruction from being mistaken for a failed theorem application.

Skinner's published page 188 expressly augments SU's Vatsal citation in Proposition 12.3.6 with Chida–Hsieh Theorem C to cover a weight-two multiplicative specialization. That addresses the stated reduction-at-p scope issue. This operation has not established that it also supplies the missing inert Euler normalization in the project's CH-to-SU comparison.

## 4. What remains unreconstructed, and the stopping rule

For the audited primitive interpolation, inert \(q\), trivial character on the principal ideal \((q)\), and split multiplicative \(a_q=1\), the removed factor is

\[
\mathcal E_q^{K,-}=1-q^{-2},\qquad
v_3(\mathcal E_q^{K,-})
=v_3((2243-1)(2243+1))=1.
\tag{E4}
\]

The original §3.6's μ-preservation inference is therefore false in that normalization. The author-copy proof of SU Proposition 12.3.6 uses a unit among the specialized coefficients to exclude an extended height-one prime. A merely nonzero specialization does not supply that unit. Nor does a unit ratio of periods remove the positive valuation in (E4).

No exact source identification was obtained that cancels (E4) before that unit argument, absorbs it in a nonunit normalization with a proved integral comparison, or replaces that step in the full SU dependency. The printed author-copy formula's notation is not used as evidence for a repair. The journal body was not independently obtained, so no claim of a newly discovered error in the published theorem follows.

**Stop R2 cleanup here.** Retain the 3-primary theorem through published Skinner Theorem A, Jones with finiteness in the correct order, and the existing arithmetic certificates and other retained qualifications. Preserve the original repair and hostile review unchanged. The remaining provenance limitation is localized at the internal Euler-removal interface, not promoted to a new open arithmetic target.

## 5. Exact effect on the BSD obligations

No numerical result or global endpoint changes:

\[
\Sha(E/\mathbf Q)[3^\infty]\simeq(\mathbf Z/3)^2
\quad\text{at the published-theorem dependency tier};
\qquad \mathrm{FIN},\ \#\Sha=9,\ q=36\text{ remain open}.
\]

The next authorized operation is solely the comparison of the exact M1 weighted period with \(\Omega_E R\), aiming at \(q=36\), without FIN or BSD. It does not reopen any stopped FIN architecture.
