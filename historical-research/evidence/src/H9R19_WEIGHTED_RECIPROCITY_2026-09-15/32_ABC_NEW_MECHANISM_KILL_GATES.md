# 32 — NEW-MECHANISM KILL GATES A, B, C (operator, 2026-09-16: "A b c in order as suggested")
Kill-first and source-first, in the order given. Nothing built. No agent launched. No new H9R number. H41 untouched.
No sealed statement changes. Status words and admission gates in force: file 31.

The three questions (operator relay):
 A. Can the Castella–Do relaxed/strict Euler-system machinery be connected by an exact Poitou–Tate/control theorem to the specific
    V_p Sha(E/Q) quotient? Stated kill test: "if its controlled dual Selmer module is a different Selmer structure and there is no exact
    comparison to the Bloch–Kato Sha quotient, stop."
 B. Is there a published or derivable rank-two Kolyvagin/Stark-system construction whose bottom/determinant datum specializes to the
    generalized Kato package and whose primitivity controls this Sha?
 C. With universality relaxed: a mathematically natural infinite family with two independent sections and a uniform p-primary Sha/Selmer
    bound.

## Sources (local line numbers)
[CD]  Castella–Do, "Diagonal cycles and anticyclotomic Iwasawa theory of modular forms", arXiv:2303.06751v2 (v1 12 Mar 2023, v2 30 Sep 2025;
      arXiv lists acceptance in JEMS). PDF sha256 e01027bc2c5cfc9819876da6e6d7ef45ece231f56043fe80cfd2d7a8f6fd95f8; text = lane file 33.
      Thm A l.134 (= Thm 3.4.2); the (ord,ord) and (rel,str) systems l.170-190; Thm B l.198 (= Thm 6.7.1); Thm C l.232 (= Thm 6.5.1);
      Selmer structures l.1958-1971; Thm 6.7.1 and proof l.3115-3134; Remark 6.7.2 l.3135-3160.
[C22] Castella GKC-IMC = lane file 22: Remark 4.2.2 l.784 (Castella–Do used for the main-conjecture divisibility only);
      (5.2) l.810: kappa_p(E) in Sel_{∅,0}(K, T_pE); (5.7) l.1010: kappa_p(E) != 0 iff rank Sel_{∅,0}(K, T_f) = 1.
[RU]  Rubin (joint with Mazur), "Higher rank Kolyvagin systems", lecture slides, Lausanne 11/2012,
      webapps.math.uci.edu/~krubin/lectures/lausanne.pdf. PDF sha256 53ddd75ca89e0ddfc4bb818d69c28fc640d8df933ed9d591eafd87e0fbb7ce74;
      text = lane file 35. Standing hypotheses l.262-263; core rank l.265-279; abelian-variety example l.302-313; Thm 1 l.323;
      Thm 10 and corollary l.555-567; Thm 20 l.580-584; state of examples l.622-633.
[BKS] Burns–Kurihara–Sano, "On derivatives of Kato's Euler system for elliptic curves", arXiv:1910.07404; J. Math. Soc. Japan 76(3)
      (2024) 855-919. Abstract only.
[ZY]  Zywina, "There are infinitely many elliptic curves over the rationals of rank 2", arXiv:2502.01957v1 (4 Feb 2025; no journal
      reference listed). PDF sha256 18400c6915ab3ba8af85cacfaee17bcd0904809148de4965813d7920794df22b; text = lane file 34.
      Thm 1.1 l.31; Thm 1.2 l.35-38; Sha(E/Q)[2] = 0 l.55-56 (the text layer prints Sha as "X"); rank-2 surface and fibres l.58-86;
      "important for the singular fibers of E to occur only at integers and ∞" l.84-86; isogeny Selmer maps are isomorphisms l.103-115.
[JE]  Jeong, "Infinitely many elliptic curves of rank exactly two, II", arXiv:1805.00639: conditional on the parity conjecture (abstract).

## Gate A — Castella–Do machinery versus V_p Sha(E/Q)
A1 The machinery. [CD] Thm A builds an anticyclotomic Euler system for V_{f,chi} (Jetchev–Nekovář–Skinner framework) in two variants,
   with (ord,ord) or (rel,str) local conditions at p. Its theorems bound Bloch–Kato Selmer groups: Thm C, L(f/K,chi,r) != 0 gives
   Sel_BK = 0; Thm B, for j >= r, gives dim Sel_BK >= 1, and dim = 1 when the class z is nonzero; Thm 6.6.1 gives a divisibility in the
   anticyclotomic main conjecture.
A2 The controlled modules. They are the Selmer groups with (ord,ord) or (rel,str) conditions and their duals. (rel,str) coincides with
   Bloch–Kato only for j >= r ([CD] Remark 6.7.2). The H9 case has chi trivial (j = 0 < r = 1), sign +1 and L(f/K,1) = 0: neither Thm B nor
   Thm C applies, and (rel,str) is not the Bloch–Kato structure there. Castella uses [CD] only for the divisibility ([C22] Remark 4.2.2).
A3 No comparison with Sha or Mordell–Weil exists in [CD]. A full-text search for Tate–Shafarevich, Chow, Mordell–Weil, rational point and
   Kummer finds only bibliography titles and an étale Abel–Jacobi remark about finite-level classes (l.767).
A4 None can exist inside this machinery. V_p Sha = S/W is not cut out by local conditions, so any exact comparison must take W as input.
   At the trivial character the class in this relaxed-strict Selmer group is the generalized Kato class ([C22] (5.2), (5.7)), known only
   to be a Selmer class; its literal identification with [CD]'s bottom class was not checked, and the kill does not need it. In the H9
   regime V_p Sha = 0 is equivalent to kappa in W (terminal equivalence), so an exact comparison proving V_p Sha = 0 would prove the H9 target.
VERDICT A: KILL TEST FIRES. The controlled modules are (rel,str)/(str,rel)-type Selmer structures, and no exact comparison with the
Bloch–Kato Sha quotient exists; inside this machinery it would be the H9 target itself. STOP.

## Gate B — rank-two Kolyvagin/Stark systems
Scope: Mazur–Rubin / Burns–Sano higher-core-rank Kolyvagin and Stark systems with T_pE coefficients over Q or K. Anticyclotomic
(Jetchev–Nekovář–Skinner, bipartite) systems are the Gate A class.
B1 What primitivity controls. [RU] Thm 10: for core rank r >= 1 and kappa in KS_r(T), kappa_n lies in |Sel(T*, n)| · wedge^r Sel(T, n)
   for every n. Corollary: |Sel(T*)| <= p^d, where d is the divisibility of kappa_1. Thm 20: KS_r(T) is free of rank one. The outputs are
   Selmer groups and Selmer classes only, so the file 31 gate on information about W or V_p Sha fails unless an output is proved Kummer.
B2 Available core ranks. [RU] l.302-313: for an abelian variety A over Q, the natural structure relaxed at p has core rank dim A, and the
   unrelaxed one has core rank 0. For E over Q this gives 1, which is Kato's system. Over K with p split, the positive-core-rank
   structures are (rel,rel), (rel,f) and (f,rel). By Shapiro, (rel,rel) corresponds to A = E × E^K over Q, so its core rank is 2 (count
   derived here, not quoted). In every positive case the dual structure is strict at a prime above p.
B3 The bottom datum vanishes in the H9 regime. When kappa != 0, S_0 = Q_p kappa is nonzero. Restricted to K it is strict at both primes
   above p, so every dual Selmer group in B2 contains it and has positive corank. At level p^k its order is at least p^(k - c) for a
   constant c. [RU] Thm 10 at n = 1 then makes kappa_1 divisible by p^(k - c) for every k, so the p-adic bottom datum is zero. This holds
   under the standing hypotheses of [RU] l.262-263; the passage to the p-adic limit is standard and was not re-derived from the memoir.
   Over Q the same argument gives the vanishing of Kato's bottom class whenever the strict Selmer group is nonzero. So no system of this
   kind has a nonzero bottom datum that could specialize to the generalized Kato package, and none is primitive.
B4 Nonzero information lives in derived classes kappa_n with n > 1. By [RU] Thm 10 these are Selmer-valued too. [BKS]'s Generalized
   Perrin-Riou Conjecture relates a Darmon-type derivative of Kato's zeta element to a higher derivative of the L-function, so it reaches
   Mordell–Weil regulators only through the BSD formula. [BKS] prove its order-of-vanishing part in arbitrary rank, and show it specializes
   to Perrin-Riou's conjecture in analytic rank one (abstract). In 2012 no explicit nontrivial Kolyvagin systems of core rank > 1 were
   known ([RU] l.622-633).
B5 An exact identification with the generalized Kato package would not help. The package is Selmer-valued, and the logarithm contraction
   maps wedge^2 S onto the strict line automatically (file 31 closure). Rational content requires a datum from wedge^2 W, that is, two
   rational directions, which is the H9 target.
VERDICT B: KILL TEST FIRES. Primitivity controls Selmer structure only. When kappa != 0 the bottom datum of every relaxed-at-p system of
positive core rank is zero, and derived data reach L-values only through a conjecture. STOP.

## Gate C — families (universality relaxed by the operator)
C1 The p = 2 version is already a theorem in print. [ZY] Thm 1.2: if m, m + 16n^2 and m + 25n^2 are primes congruent to 11 mod 24, then
   E: y^2 = x^3 - 5(m + 16n^2)x^2 + 4(m + 16n^2)(m + 25n^2)x has E(Q) ≅ Z/2 × Z^2. Both 2-isogeny Selmer maps are isomorphisms and
   Sha(E/Q)[2] = 0 (l.55-56, l.103-115). By Tao–Ziegler there are infinitely many such (m, n), giving infinitely many curves up to
   isomorphism over Q-bar (Thm 1.1). So rank exactly 2 and Sha[2^inf] = 0 hold on an infinite family with two independent sections.
   Earlier results of this kind were conditional on the parity conjecture ([JE]; [ZY] l.100-102).
C2 The mechanism does not transfer to H9. The Selmer computation is a descent along a rational 2-isogeny, which needs a rational 2-torsion
   point. The infinitude needs every singular fibre of the rank-2 surface over an integer or ∞, so that the bad primes are values of
   prime patterns covered by Tao–Ziegler ([ZY] l.84-86). H9 works at p > 3 with E[p] absolutely irreducible (Castella Thm A (i)), where no
   isogeny descent exists.
C3 p >= 5: no uniform Selmer-control mechanism on an infinite family with two sections is in print or identified. The family-level tool
   at odd p is congruence control of Iwasawa lambda-invariants (Greenberg–Vatsal, not re-read). It needs constant E[p] or rational p-torsion,
   plus local control at every new bad prime, since congruent curves' lambda-invariants differ by local terms there. The natural families
   have singular fibres over irrational points. Example computed here with sympy: the universal curve with a rational 5-torsion point,
   y^2 + (1-t)xy - ty = x^3 - tx^2, has discriminant t^5 (t^2 - 11t - 1), with t^2 - 11t - 1 irreducible over Q (discriminant 125). Its new
   bad primes divide values of an irreducible quadratic, which Tao–Ziegler-type results do not control, and that family has reducible
   E[5], outside Castella's hypotheses anyway.
VERDICT C: p = 2 ALREADY PROVED (Zywina 2025); no new theorem, and the mechanism does not transfer. p >= 5 NOT STARTABLE: no uniform
mechanism, and its first obligation (a constant-E[p] family with two sections and controlled new bad primes) is unidentified.

## Outcome
```
GATE_A                       = KILLED: controlled modules are Selmer structures; no Bloch–Kato Sha comparison; one would be the H9 target
GATE_B                       = KILLED: primitivity controls Selmer only; bottom datum is zero when kappa != 0; derived data tied to L-values only conjecturally
GATE_C                       = p = 2 ALREADY IN PRINT (Zywina 2025: infinitely many curves, rank exactly 2, Sha[2] = 0); p >= 5 NOT STARTABLE
SURVIVING_MECHANISM          = NONE
CURRENT_H9_CONSTRUCTION      = STOPPED AT ITS RECORDED BOUNDARY
UNIFORM_H9_ARITHMETIC_TARGET = OPEN; PARKED until a genuinely new arithmetic idea appears
NEW_ADMITTED_MECHANISM       = NONE IDENTIFIED
WRITE_UP                     = NOT STARTED: the "write up if all die" step needs an operator decision under the standing no-manuscript rule
BUILD                        = NONE
```

## CORRECTION (2026-09-17, after Pro's review BSD_ABC_REVIEW_2026-09-17; audit = ~/BSD_ABC_REVIEW_2026-09-17/00_REPORT.md, sha256 7478087bfaad5624679da399d50c9e5c00c34408d7cc9948f632180e4c2afce5)
The text above is kept unedited. Pro reviewed this file at sha256 1480451726c3... Corrections, all verified against published sources:
- A: WITHDRAWN "A4 None can exist inside this machinery". Supported: Castella–Do Thms 6.5.1/6.7.1 do not apply directly (j = 0 < r = 1;
  L(f/K,1) = 0) and the paper has no Sha comparison. Not supported: that none can be derived. Pro's Lemma A1 (exact sequence
  0 -> S_0/(W∩S_0) -> S/W -> ell(S)/ell(W) -> 0; with one nontorsion point V_p Sha ≅ S_0/(W∩S_0)) is verified linear algebra.
- B: WITHDRAWN "and none is primitive" and the verdict KILLED. Mazur–Rubin JTNB 28 (2016): primitive = generates the stub module KS'_r(T)
  (§13); Cor 13.1(iii) allows primitive with kappa_1 = 0; Thm 13.4(iv) corank = ord(kappa), (vii) primitive iff dphi(inf) = 0,
  (viii) dual Selmer finite iff kappa_1 != 0. RETAINED: bottom kappa_1 = 0 in the kappa != 0 regime (Thm 13.4(viii)). "KS_r free of rank
  one" is Thm 11.7(i) for stub systems.
- BKS: CORRECTED. Def 4.10 and Prop 4.14 contain the Bockstein and Néron–Tate regulators explicitly; Thm 6.2 is proved. The circularity is
  Hypothesis 2.2(iii) (Sha[p^inf] finite) behind §4.3 and Thm 6.2; §3 does not assume it.
- C: WITHDRAWN "p >= 5 NOT STARTABLE" and the claim that Zywina's method cannot run with E[p] irreducible. Rational 2-torsion is compatible
  with surjective mod-5 image; Pro's family C1 (Zywina's curves with m = 491 mod 840, n = 0 mod 420) is audited PASS (good ordinary at 5,
  image GL_2(F_5), Tamagawa prime to 5, infinitely many by Tao–Ziegler Thm 1.3). New gate result: UNKNOWN; on C1 a two-prime Kurihara
  witness, kappa_5 != 0 and finite Sha[5^inf] are EQUIVALENT (Proposition K, report sec 3), so the uniform bound is exactly the open
  5-primary Sha statement.
