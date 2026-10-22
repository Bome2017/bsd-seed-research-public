# From the residual Kato criterion to an explicit coordinate equation

Date: 2026-10-07.

**Grade: written deduction under retained project inputs and the published Rubin/Coleman formalism; independent review required. No residual coordinate or BSD bound is computed.**

This is a continuation of the existing BKS/leading-term route, not a new global-object proposal. Its concrete purpose is to express the already-constructed derivative's coordinate pair using height pairings, logarithms, and the Coleman image of the SAME class. It does not identify a p-adic leading term with the complex BSD quotient.

## 1. Retained inputs and conventions

Use the retained seed

\[
 E:y^2=x^3-x^2-66020924x-65074271436,
 \quad P_1=(-3031,327384),\quad P_2=(-2394,281520).
\]

Work on

\[
 D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\},
 \quad N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]

The rank-two saturated basis, residual image, and the integral cohomological/source matching retain their project grades. Put

\[
 R=\mathbf Z_p[[U]],\quad U=\gamma-1,
 \quad M=H^1_{\rm Iw},\quad H=H^1(G_{\mathbf Q,S},T_pE).
\]

The following are RETAINED, not re-proved here:

- The specified integral smoothed Kato class satisfies \(z_\infty=Uy_\infty\), with \(y_\infty\in M\), and \(M/UM\hookrightarrow H\).
- \(\delta_p=\operatorname{aug}(y_\infty)=A_p\kappa(P_1)+B_p\kappa(P_2)\), with \(A_p,B_p\in\mathbf Z_p\).
- \(\delta_p\ne0\) implies that \(\Sha(E/\mathbf Q)[p^\infty]\) is finite, without assuming this finiteness initially.
- \((A_p,B_p)\mathbf Z_p=\mathbf Z_p\) implies \(\Sha(E/\mathbf Q)[p^\infty]=0\) on D.

The class and lattice are transported together. This note does not replace the actual smoothed class by a primitive normalization. In particular it never divides the unknown pair \((A_p,B_p)\) by its common power of p.

Primary project sources:

- Weak order: lab d4d86454eedd7e3be2c0b398f4a8210fa4abc4a3, `WEAK_ORDER_PROOF.md`.
- Source audit: lab 54637ae16c1856d065b8dada5aeab7c7ac33ced6, `FOUNDATION_CHECK.md`.
- Placement: lab f3b3ce88883969e37b48d4db34d5d843a4947283, `PROOF.md`.
- Integral criterion: lab b9c4e1d421b78564904cdd2516ac07f69fcd900e, `INTEGRAL_MATCHING.md` and `ALGEBRA_REVIEW.md`.

## 2. The published formula, and why it must not be imported with its finiteness hypothesis deleted

Burns--Kurihara--Sano, *On derivatives of Kato's Euler system for elliptic curves*, arXiv:1910.07404v2, Theorem 6.2(i), proves a generalized Rubin formula. Its stated Hypothesis 2.2 includes p-primary Sha finiteness. The source's proof is in Sections 6.3--6.4; the relevant auxiliary statements are Theorem 6.10 (Coleman reciprocity), Theorem 6.11 (Rubin's height identity), Lemma 6.12 (divided Iwasawa class), and Lemma 6.14 (linear Coleman coefficient).

This note uses the v2 numbering actually read. The published JMSJ version should be checked for matching conventions before promotion. The arXiv PDF pages 43--45, including both ordinary and supersingular local-condition diagrams, were visually inspected; page numbers here are the printed v2 numbers.

Choose an allowable root \(\rho\) of

\[
 X^2-a_p(E)X+p=0,
\]

and put \(\sigma=p/\rho\), \(L=\mathbf Q_p(\rho)\). Here \(a_p(E)\) is the Frobenius trace, not the derivative coordinate \(A_p\). Let

\[
 \epsilon_{p,\rho}=(1-\rho^{-1})^{-1}(1-\sigma^{-1}).
\]

These factors are nonzero at a good prime. Take the height pairing and Coleman map with the same root, differential, cyclotomic coordinate, and representation convention.

Define the ACTUAL source distribution

\[
 \mathcal F_{p,\rho}(U)=\operatorname{Col}_{\rho}(\operatorname{loc}_p z_\infty).
\]

This definition fixes the normalization even when the homothety exponent relative to a differently normalized numerical p-adic L-function has not been computed. Its conversion into the project evaluator's particular L-function coefficients remains an explicit normalization task; it is not accomplished by naming the distribution.

The proposed deduction is

\[
 h_{p,\rho}(P,\delta_p)
 =\epsilon_{p,\rho}\log_\omega(P)\,[U^2]\mathcal F_{p,\rho}
 \quad(P\in E(\mathbf Q)),                                      \tag{R}
\]

where \(h_{p,\rho}\) is the scalar coefficient of the height in the U-basis of \(I/I^2\). Equation (R) is about a p-adic L-function/Coleman image, not about \(L''(E,1)\), q, or a cross-prime rational number.

## 3. A finiteness-free local-finiteness lemma

**DERIVED using global and local Tate duality.** Every class of \(H^1(G_{\mathbf Q,S},V_pE)\) localizes into \(H_f^1(\mathbf Q_p,V_pE)\), provided E has a non-torsion rational point.

At a finite place v different from p, the rational local cohomology \(H^1(\mathbf Q_v,V_pE)\) is zero. One way to see this is that the local p-power torsion is finite, so \(H^0(\mathbf Q_v,V_pE)=0\); Weil self-duality gives \(H^2=0\), and the local Euler characteristic at v different from p gives \(H^1=0\). On the retained seed domain the explicit local calculations also supply the necessary vanishings at the bad places. At primes outside S the unramified cup invariant is zero. The odd-p archimedean term causes no issue.

Take a non-torsion rational point P. Its local Kummer class spans the one-dimensional rational Kummer subspace at p: its p-adic logarithm is nonzero, since the kernel of the logarithm on the compact group E(Q_p) is torsion. A rational non-torsion point cannot become torsion in E(Q_p).

Global reciprocity, applied to any global class x and the Kummer class of P, forces their local Tate pairing at p to vanish. The Kummer line is its own annihilator. Therefore loc_p(x) lies in that line.

This argument does not identify the GLOBAL Bloch--Kato Selmer group with the Mordell--Weil group. Unknown rational Tate-module Sha directions remain allowed in the former.

**Consequence.** For every m in M, the augmentation of its Coleman image is zero, by the interpolation formula for the Coleman map and the vanishing of the dual exponential on the local Kummer subspace. Thus

\[
 \operatorname{Col}_{\rho}(M)\subset U\mathcal H_\infty.       \tag{L}
\]

Here the distribution algebra may be larger than R at supersingular primes; vanishing of its constant coefficient still means U-divisibility. No integrality of the distribution coefficients is inferred from (L).

This lemma and its use of rational local duality are independent-review targets, not numerical checks.

## 4. Removing finiteness from (R) for this particular derivative

The existing nonzero-derivative implication allows a case split; no conjectural leading-term formula is used.

### Nonzero derivative

If \(\delta_p\ne0\), the retained weak-order/control argument proves p-primary Sha finiteness. The other parts of BKS Hypothesis 2.2 hold: positive algebraic rank and torsion-free integral global cohomology. The published generalized Rubin formula therefore applies in this branch.

For the source's smoothed class, the formula before cancelling the smoothing factor reads

\[
 \langle P,{}_{c,d}\kappa_\infty\rangle_{p,\rho}
 =\epsilon_{p,\rho}\log_\omega(P)\,
  t_{c,d}(0)\mathcal L^{(2)}_{S,p,\rho}.
\]

Kato/Coleman reciprocity identifies the last product with \([U^2]\operatorname{Col}_{\rho}(z_\infty)\). Taking coefficients in the U-basis gives (R). The formula is linear in the source class, so simultaneous homothety transport scales both sides equally. This is not a p-unit assertion.

### Zero derivative

If \(\delta_p=0\), injectivity of \(M/UM\to H\) gives \(y_\infty\in UM\). Hence \(z_\infty\in U^2M\). By (L),

\[
 \mathcal F_{p,\rho}\in U^3\mathcal H_\infty.
\]

Thus its quadratic coefficient is zero, and both sides of (R) are zero. This branch needs no Sha finiteness.

Together the two branches give (R) under the retained inputs and the stated source/local comparison. In particular the nonzero case is not assumed merely in order to invoke the BKS theorem; it is a branch of a proof covering zero as well.

**Scope.** The argument does not assume height nondegeneracy. BKS's good-prime formula includes supersingular roots through its (phi,Gamma)-module local conditions. Their exact compatibility, the Coleman normalization on the actual transported class, and the zero-branch local argument must be checked in an independent audit. No new rank-one-only source is being substituted for the supersingular case.

## 5. The explicit rank-two coordinate equation

Write

\[
 \mathsf H_{p,\rho}=
 \begin{pmatrix}h_{11}&h_{12}\\h_{12}&h_{22}\end{pmatrix},
 \quad h_{ij}=h_{p,\rho}(P_i,P_j),
 \quad \ell=\binom{\ell_1}{\ell_2}
 =\binom{\log_\omega(P_1)}{\log_\omega(P_2)}.
\]

The notation \(\ell_i\) here means a logarithm, NOT the W3 coefficient called ell_2. Put

\[
 Q_{p,\rho}=\epsilon_{p,\rho}[U^2]\mathcal F_{p,\rho}.
\]

Applying (R) to both points gives the concrete matrix relation

\[
 \boxed{\mathsf H_{p,\rho}\binom{A_p}{B_p}=Q_{p,\rho}\ell.}  \tag{M}
\]

This is the useful source comparison to review: each matrix entry is a height of the known points, the logarithms are local data of those points, and the scalar comes from the actual Coleman image. None is defined by the unknown size of Sha. No new independently computed values of any of these quantities are claimed here.

If \(\det\mathsf H_{p,\rho}\ne0\), elementary algebra yields

\[
 \binom{A_p}{B_p}
 =\frac{Q_{p,\rho}}{h_{11}h_{22}-h_{12}^2}
 \binom{h_{22}\ell_1-h_{12}\ell_2}
       {h_{11}\ell_2-h_{12}\ell_1}.                       \tag{C}
\]

Thus, with \(v_p(p)=1\) also on L and \(Q_{p,\rho}\ne0\),

\[
 \begin{split}
 \min(v_p(A_p),v_p(B_p))
 ={}&v_p(Q_{p,\rho})
 +\min\{v_p(h_{22}\ell_1-h_{12}\ell_2),
          v_p(h_{11}\ell_2-h_{12}\ell_1)\}\\
 &-v_p(h_{11}h_{22}-h_{12}^2).                            \tag{V}
 \end{split}
\]

Primitivity is exactly the assertion that (V) is zero. At supersingular primes individual valuations can be fractional; the completed expression equals the valuation of a pair in Z_p and is therefore a nonnegative integer.

If Q=0 and the matrix is nonsingular, the pair is zero. If the matrix is singular, (M) remains meaningful but division by its determinant is forbidden. This note does not prove nondegeneracy at every prime or outside a finite set.

### A one-sided alternative that does not assume nondegeneracy

For a nonzero row i, put \(m_i=\min_j v_p(h_{ij})\). Equation (M) and integrality of A_p,B_p imply

\[
 \min(v_p(A_p),v_p(B_p))\le v_p(Q_{p,\rho}\ell_i)-m_i.
\]

Therefore proving the right side is less than 1 is sufficient for primitivity. In particular equality \(v_p(Q\ell_i)=m_i\) suffices. This avoids a blanket assumption that the full regulator is nonzero. No such valuation estimate for the actual seed is proved here.

## 6. What source choices can and cannot repair

The source formula already in the foundation audit contains

\[
 t_{c,d}(0)=cd(c-1)(d-1),
 \qquad c_N=\frac{2^5\cdot19\cdot59\cdot487}{2243\cdot5843}.
\]

On D, c_N is a p-unit. For each p in D, the Chinese remainder theorem permits

\[
 c\equiv d\equiv1\pmod{6N},\qquad c\equiv d\equiv2\pmod p,
\]

with distinct positive c,d>1. These satisfy the smoothing coprimality/congruence conditions and give \(t_{c,d}(0)\equiv4\pmod p\). Alternatively, a fixed valid c,d has a fixed finite set of nonunit primes. Consequently smoothing is an avoidable source of additional p-divisibility, not a reason to assume intrinsic primitivity.

For a fixed Betti input, two valid smoothings with unit smoothing factors differ by an R-unit. Their divided augmentations differ by the augmentation of that unit, so their primitivity tests agree. Varying only such smoothings CANNOT turn an intrinsically nonprimitive class into a primitive one.

An unknown integral Betti/image-lattice comparison is a different issue. To identify Q with the record's existing numerical p-adic L-coefficient, the exact source period, image lattice, Euler factors, and smoothing must be matched. An unspecified power of p cannot be absorbed into a unit. This note keeps \(\mathcal F\) tied to the actual source rather than falsely identifying it with a previous W3 output.

## 7. What a nonunit regulator actually means here

The estimate to prove is correlated: (V), or the one-sided row version. Separate unitness of the determinant is not necessary.

For an ABSTRACT example over Z_p, take

\[
 \mathsf H=\operatorname{diag}(1,p),\quad \ell=(1,1)^t,
 \quad Q=p.
\]

Then (M) gives \((A,B)=(p,1)\), which is primitive despite the nonunit determinant and nonunit Q. Conversely, H=I and Q=p give a nonprimitive pair. These are exact algebra controls, NOT values for the seed at p=17 or any other prime.

Another algebra identity is

\[
 \operatorname{adj}(\mathsf H+c\ell\ell^t)\ell
 =\operatorname{adj}(\mathsf H)\ell
\]

for a symmetric 2-by-2 matrix. Its determinant usually changes. Thus where an actual height-splitting comparison has this form, changing splittings does not automatically provide independent cofactor directions. The displayed identity is checked algebraically here; no new arithmetic height-splitting theorem is imported by it.

## 8. Collision with the existing record and the actual delta

A bounded search of the submitted 9,215,156-byte FULL_COMPENDIUM.md found the generalized Rubin formula in the Sept 17 source correction. That entry already identified the p-primary-finiteness hypothesis as the obstacle. The Sept 19/26 leading-term records separately target the conjectural complex-to-p-adic comparison.

The new input now available is the constructed divisible Kato class, its integral placement, and the nonzero-derivative primary-finiteness implication. The case split above is the proposed change to the old failed arrow. The new claim is NOT that BKS or its formula was just discovered, and no exhaustive novelty claim is made.

This is also NOT the analytic Generalized Perrin--Riou conjecture: it does not set Q/det(H) equal to a rational or complex BSD quotient. The latter uniform arithmetic comparison remains unproved.

## 9. What work this identifies, and what it does not accomplish

The precise remaining arithmetic problem is now to control the matched numerator/cofactor/regulator valuation in (V), or an adequate integral row evaluation, outside a fixed finite set of p. Merely recording (V) does not supply that estimate.

Before new large computation, independently review the finiteness-removal argument and bind the actual Coleman output to the record's numerical normalization. Existing point-height and symbol data can then be reused as a bounded nonvacuity/calibration test, without pretending that checking more already-settled primes proves the tail.

A uniform theorem would need a source-level reason why the matched coordinate content is a unit cofinitely. Neither the matrix identity, the positivity of the real L-value quotient, the finite 288 table, nor a generic nonvanishing result supplies that reason. No such theorem is claimed here.

FIN, ORDER9 and Q36 are unchanged. No remote job, prime campaign, repository write, or submission is authorized by this note.

## 10. Primary sources and review priorities

- BKS I, arXiv:1910.07404v2: Hypothesis 2.2; Sections 5.1, 6.1--6.4; Theorems 6.2, 6.10, 6.11 and Lemma 6.14. PDF https://arxiv.org/pdf/1910.07404v2 ; HTML https://arxiv.org/html/1910.07404v2 . The published JMSJ PDF link failed during this pass, so numbering/version claims here are restricted to the version actually read.
- Project foundation proof: https://github.com/Bome2017/bsd-seed-lab/blob/54637ae16c1856d065b8dada5aeab7c7ac33ced6/work/returns/BSD_BKS_FOUNDATION_AUDIT_CODEX_2026-10-07/FOUNDATION_CHECK.md .
- Project placement proof: https://github.com/Bome2017/bsd-seed-lab/blob/f3b3ce88883969e37b48d4db34d5d843a4947283/work/returns/BSD_KATO_DERIVATIVE_MW_PLACEMENT_CODEX_2026-10-07/PROOF.md .
- Integral criterion: https://github.com/Bome2017/bsd-seed-lab/blob/b9c4e1d421b78564904cdd2516ac07f69fcd900e/work/returns/BSD_RESIDUAL_KATO_CRITERION_AUDIT_CODEX_2026-10-07/INTEGRAL_MATCHING.md .

Review the rational local-finiteness/reciprocity lemma, the zero-derivative branch, matching of the smoothed and transported source, and the U-coordinate of the height. At supersingular p, retain the source's exact local (phi,Gamma)-module and root conventions. Do not promote the conditional source adaptation because the separate matrix checks pass.

`check_algebra.py` checks only polynomial identities, the abstract valuation examples and smoothing CRT choices. It does not certify BKS's local comparison, a Kato residue, or cofinite primitivity.
