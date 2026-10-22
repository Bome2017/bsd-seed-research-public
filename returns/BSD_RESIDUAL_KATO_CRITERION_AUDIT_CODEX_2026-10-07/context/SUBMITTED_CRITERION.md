# Residual nonvanishing of the constructed Kato derivative

Date: 2026-10-07

**Status: CONDITIONAL CRITERION DERIVED; INTEGRAL SOURCE MATCHING STILL REQUIRED.**

This note studies useful nonvanishing of the already constructed first cyclotomic derivative. It does not redo its Mordell–Weil placement. It proves a commutative-algebra implication with explicit hypotheses and explains the stronger arithmetic input needed to apply it. It computes no derivative coefficient, supplies no uniform nonvanishing theorem, and changes none of FIN, ORDER9 or Q36. No novelty or independent certification is claimed.

## 1. The point of the calculation

The retained construction gives an actual smoothed class

\[
z_\infty=U y_\infty,\qquad U=\gamma-1,
\]

and a derivative

\[
\delta_p=\operatorname{aug}(y_\infty)
       =A_p\kappa(P_1)+B_p\kappa(P_2),\qquad A_p,B_p\in\mathbf Z_p.
\]

The letters A_p,B_p here denote point coordinates, not the Frobenius trace. The class and its source lattice are transported together. The retained proof shows that rational nonvanishing of this derivative implies primary finiteness. The question here is different:

> Does nonvanishing of delta_p modulo p imply primary **vanishing**?

The answer is yes under the stronger integral hypotheses below. The earlier inequality at the augmentation prime (U) alone is not enough.

## 2. Explicit hypotheses

Fix p >= 5 and put R=Z_p[[U]], m=(p,U), k=F_p. Let C be a complex representing the full S-cohomology Iwasawa problem for the actual elliptic lattice. Require:

(P1) C is perfect of amplitude [1,2]. Write M=H^1(C), X=H^2(C). M is free of rank one over R, X is finitely generated R-torsion, and Euler rank is one.

(P2) Derived base change identifies C tensor_R^L R/(U) with RΓ(G_{Q,S},T_pE), and C tensor_R^L k with RΓ(G_{Q,S},E[p]). In particular, write H=H^1(C tensor_R^L R/(U)). Retain the Kummer injection of the full rank-two point lattice W into H and its saturation. The classical p-Selmer group embeds in H^1(G_{Q,S},E[p]) and contains E(Q)/p, of dimension two.

(P3) The actual smoothed element z belongs to M, satisfies z=Uy, and its divided augmentation is delta_p in H.

(P4) **Integral Kato bound for this same complex, lattice and class:** for every height-one prime q of R,

\[
\operatorname{length}_{R_q}X_q
\le
\operatorname{length}_{R_q}(M/Rz)_q.
\]

No local correction with nonunit contribution may be silently omitted. In particular, (P4) includes q=(p), unlike the weaker rational inequality used for U-divisibility.

These conditions are hypotheses of the criterion, not assumptions that Sha vanishes. The retained full-S cohomology construction supports much of (P1)-(P3). The complete application of (P4) to the imprimitive elliptic problem is an additional source/lattice/local-factor verification and is not certified by this note.

## 3. Criterion

**Derived proposition.** Under (P1)-(P4),

\[
\delta_p\notin pH
\quad\Longrightarrow\quad
\dim_k H^1(G_{Q,S},E[p])=2
\quad\Longrightarrow\quad
\Sha(E/\mathbf Q)[p^\infty]=0.
\]

By the retained saturation of W and the point-coordinate formula, the premise is equivalent to

\[
(A_p,B_p)\mathbf Z_p=\mathbf Z_p.
\]

The proposition is only sufficient. It does not say that every prime with trivial Sha has a primitive derivative.

## 4. Proof with the H^2/base-change issue retained

### 4.1 Residual nonvanishing makes the divided Iwasawa class a generator

Choose a basis m_0 of the free R-module M and write y=g m_0. If g belongs to m, then g(0) is divisible by p and the augmentation of y belongs to pH. Therefore delta_p not in pH forces g to be an R-unit. Thus y is itself a basis of M and

\[
M/Rz\simeq R/(U).
\]

This conclusion is about the specified smoothed class. It does not replace that class by an independently normalized generator.

### 4.2 The cycle is primitive in a free representative, not just in abstract H^1

The coefficient triangle for multiplication by p on C tensor_R^L R/(U) gives an injection

\[
H/pH\hookrightarrow H^1(C\otimes_R^{\mathbf L} k).
\]

Thus y has nonzero cohomology class after reduction modulo m. Represent C by finite free modules F^1 -> F^2. A cycle representing y cannot belong to mF^1: such a vector would reduce to zero. It is consequently primitive in F^1 and can be extended to an R-basis.

Split

\[
F^1=Ry\oplus F',\qquad d(y)=0.
\]

The complementary differential D:F' -> F^2 has zero kernel, because H^1(C)=Ry. Euler rank one gives rank(F')=rank(F^2)=n. Therefore

\[
C\simeq R[-1]\oplus[\,R^n\xrightarrow{D}R^n\,],
\]

where the bracket is in degrees one and two, D is injective, and X=coker(D). Here R[-1] denotes R in cohomological degree one.

This split is the important safeguard. It produces an actual square presentation of X and prevents a hidden finite H^2 submodule from being discarded by characteristic-ideal notation.

### 4.3 Integral divisibility makes the determinant a single augmentation factor

The ring R is a regular local unique-factorization domain. The characteristic ideal of coker(D) is generated by det(D). By (P4) and M/Rz=R/(U), its height-one valuations satisfy

\[
v_q(\det D)\le v_q(U)
\]

for every height-one q, including (p). Hence det(D) is either a unit or a unit times U.

The unit case would make the complementary complex acyclic, and H would then have rank one. That contradicts the two independent Kummer point directions from (P2). Thus

\[
\det D=\varepsilon U,\qquad\varepsilon\in R^\times.
\]

### 4.4 A determinant with a nonzero linear term controls the special fibre

Because U is not in m^2, the reduction of D modulo m has rank n-1. Indeed, if its corank were at least two, eliminate all unit pivots. The remaining square block would have size at least two and every entry in m; its determinant would belong to m^2, a contradiction.

After invertible row and column operations, D is a direct sum of n-1 unit blocks and one block epsilon' U, with epsilon' a unit. Consequently

\[
C\simeq R[-1]\oplus[\,R\xrightarrow{U}R\,]
\]

up to contractible summands and a unit change of basis. Reducing the complex modulo m gives two degree-one copies of k and one degree-two copy. In particular,

\[
\dim_k H^1(C\otimes_R^{\mathbf L}k)=2.
\]

No unrestricted commutation of cohomology with base change has been asserted; the complex itself has been reduced.

### 4.5 Kummer finishes the residual statement

By (P2), the classical p-Selmer group is a subspace of this two-dimensional global H^1 and already contains the two-dimensional Kummer space E(Q)/p. They are equal. The Kummer exact sequence therefore gives Sha[p]=0.

A nonzero p-primary torsion group always has a nonzero element killed by p. Hence Sha[p]=0 implies Sha[p^infinity]=0. This proves the criterion without an initial primary-finiteness assumption.

## 5. Why the previous (U)-only estimate is insufficient

Take e >= 1 and the free two-term R-complex

\[
C_e=R[-1]\oplus
[\,R^{e+1}\xrightarrow{\operatorname{diag}(U,p,\ldots,p)}R^{e+1}\,].
\]

Then H^1(C_e)=R, z=U times its basis, and the divided augmentation is primitive. Its degree-two module is

\[
X_e=R/(U)\oplus(R/(p))^e.
\]

At (U), p is invertible, so length(X_e,(U))=1. Thus the old augmentation-prime inequality is satisfied exactly. Nevertheless,

\[
\dim_kH^1(C_e\otimes_R^{\mathbf L}k)=e+2.
\]

The stronger integral inequality fails at (p). This is an abstract algebra countercontrol, not a seed Selmer complex or an arithmetic counterexample. It pinpoints why this new criterion cannot be claimed from the earlier weak-order proof alone.

## 6. The published input that may supply (P4)

Kato's Theorem 12.5(3), printed p.222, bounds heights-one lengths away from primes containing p. Part (4) is the integral version, under condition (12.5.2): the image on the cyclotomic kernel contains SL_2(Z_p) in a suitable lattice basis. The good-reduction domain avoids the exceptional local correction described there. Theorem 12.6 puts the actual smoothed-source module inside Kato's zeta-image module. A cyclic submodule generated by the specified smoothed source then gives a weaker, still sufficient upper bound.

This makes (P4) a concrete source-matching question, not an assumption of BSD or an Iwasawa-main-conjecture equality. However three details must be supplied before applying the proposition to the seed:

1. Match the integral big-image hypothesis, not just residual irreducibility, with the retained seed image statement and its lifting argument.
2. Transport the actual lattice, zeta-image module, smoothed class and character component together. No division by an unproved p-unit is allowed.
3. Compare Kato's j_* cohomology and the full S-imprimitive complex integrally at all relevant height-one primes. The preceding foundation audit established that comparison at (U). Nonzero augmentation is insufficient at (p) or at the maximal ideal; any needed local acyclicity or correction must now be proved or placed in an explicit finite exception set.

The retained tame domain suggests excluding its known bad-local factors, but this note does not declare an all-good-prime or supersingular theorem without those checks. The commutative-algebra proposition itself uses no ordinary filtration.

## 7. Endpoint and what should not be inferred

If the integral source matching is completed, this turns a specific residual nonvanishing statement about the constructed derivative into primary vanishing:

\[
\delta_p\bmod p\ne0\quad\Longrightarrow\quad\Sha[p^\infty]=0.
\]

It would therefore make the coordinate ideal (A_p,B_p) a one-sided detector. It would not prove that this ideal is the unit ideal at any seed prime, let alone cofinitely. It would not make A_p or B_p rational or independent of p, and it would not identify the derivative with a particular numerical modular-symbol coefficient.

No new primary prime, finite-support bound, FIN, ORDER9 or Q36 is proved here. The tame fixed-scalar comparison is also not supplied. The present result is the conditional implication and the exact stronger integral input it requires; no additional worker run or publication is authorized by it.

## Sources and collision scope

- Kato, *P-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), Theorems 12.4–12.6, printed pp.221–222. The repository's preserved primary-source text was read; the live Numdam PDF fetch failed because of its size. The text's displayed formulas have extraction corruption, so a clean primary-PDF comparison remains desirable before promoting the arithmetic application.
  Primary URL: https://www.numdam.org/article/AST_2004__295__117_0.pdf
  Repository text path: work/state-sync-2026-10-04/dossiers/BSD_WEIGHT3_KATO_INDEX_CHECK_CODEX_2026-10-01/sources/Kato2004_fresh.txt
- Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919, especially Proposition 4.4 and Section 7. The published PDF was opened. Its leading-term equality in Section 7 must not be imported after deleting its finiteness/main-conjecture assumptions.
  https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en
- Retained weak-order deduction: lab d4d86454eedd7e3be2c0b398f4a8210fa4abc4a3, BSD_BKS_COMBINATION_LEDGER_CODEX_2026-10-07/WEAK_ORDER_PROOF.md.
- Retained foundation audit: lab 54637ae16c1856d065b8dada5aeab7c7ac33ced6, BSD_BKS_FOUNDATION_AUDIT_CODEX_2026-10-07/FOUNDATION_CHECK.md.
- Retained placement: lab f3b3ce88883969e37b48d4db34d5d843a4947283, BSD_KATO_DERIVATIVE_MW_PLACEMENT_CODEX_2026-10-07/PROOF.md.
- Current LATEST_RETURN was fetched before starting this calculation and still listed placement as its newest return. A repository search for 'primitive derivative' returned no matches. This is a narrow collision check, not an exhaustive novelty audit.

This note is a model-derived written argument, not a Lean proof, an independently reviewed theorem, or a canonical project-state change.
