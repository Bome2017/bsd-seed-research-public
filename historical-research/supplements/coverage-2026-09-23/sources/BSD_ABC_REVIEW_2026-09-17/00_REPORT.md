# BSD A–B–C review audit and the two-prime Kurihara gate (2026-09-17)

Author-side audit of Pro's review package, run as the handoff `CLAUDE_NEXT_GATE.md` specifies. Kill-first and source-first.
No agent launched. One bounded computation (a 0.59-second primality search). No sealed H41, 62a1/66b1 or H9 statement changed.
No manuscript work. The report is the six required sections, followed by a return block.

## Inputs and sources

Review package (`src/`). Its hashes match its own `SHA256SUMS.txt`:

    ea48cf29827c2ea6ca13645e133742a6710dd2932e06b22d54eeb9c114720d21  BSD_CONTINUITY_AND_ABC_REVIEW.md
    e5d3e4b0bb4b010c9d80459cbd3e6b62d0a57c2ba52aa789975ae67d0ee8fbb9  CLAUDE_NEXT_GATE.md
    b890d69000951d08cf5ff7f25422a18fffe01b1f5cf6bc10b6323ad420e1a008  EXACT_CHECK_RECEIPT.json
    61304380a772595bb479d3c6faf7cf3d9a890fbac537a9e3f4453c089af9542e  verify_compatibility.py
    archive BSD_ABC_REVIEW_2026-09-17.zip = 5c92ddad843e34db23d05c55a3dc70cbc74ee5def444ae5c240531a3364bebb8

The receipt's hash for file 32 (1480451726c3...) equals the lane copy before this audit, so Pro reviewed the current text.
`verify_compatibility.py` was read in full (standard library only) and rerun: PASS, identical output (`runs/verify_compatibility_output.json`).

Primary sources (`sources/`; PDFs fetched 2026-09-17; text by pdftotext -layout; line numbers refer to the .txt):

| key | source | PDF sha256 (prefix) | locators used |
|---|---|---|---|
| MR | Mazur–Rubin, Controlling Selmer groups in the higher core rank case, JTNB 28 (2016) 145–183 | 00725ad7afc9d7f3 | Def 9.4 l.1232; Def 11.3–11.4 l.1348–1358; Rem 11.5 l.1359; Thm 11.7 l.1376; §13 l.1531–1541; Cor 13.1 l.1542–1554; Thm 13.4 l.1584–1601 |
| BKS | Burns–Kurihara–Sano, On derivatives of Kato's Euler system for elliptic curves, JMSJ 76 (2024) 855–919 | bc930bdfc4a979b8 | Hyp 2.2 l.586–592; §3 scope l.1017–1024; §4.3 assumes Hyp 2.2 l.1454; Def 4.10 l.1524; Prop 4.14 l.1554; Conj 4.15 l.1580; Thm 6.2 l.2403 |
| KIM | C.-H. Kim, The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves, arXiv:2203.12159 (version served 2026-09-17) | c1288640f2643cd1 | §1.2.2 l.182–186; Cor 1.6 l.270–284; §1.4.1–1.4.4 l.288–346; Thm 1.8 l.362–400; Thm 1.10 l.446–466 |
| CS | Castella–Sano, On refined nonvanishing conjectures by Kurihara and Kolyvagin, preprint dated 20 Jan 2026 | 9478dc414299a382 | §1.1.1 l.47–72; parity l.120; exact formula l.136; Thm A l.154; Cor A l.158; Thm B l.168–175 |
| TZ | Tao–Ziegler, The primes contain arbitrarily long polynomial progressions, arXiv:math/0610050v2 | 6eb8a5313e6cebb0 | Thm 1.3 l.142–146 |
| ZY | Zywina, arXiv:2502.01957v1 = H9 lane file 34 | 18400c6915ab3ba8 | Thm 1.2 l.35–38; Sha[2] l.55–56; root number l.94–98; Lemma 3.5 l.376–378; E(Q) l.379–381; §4 l.383–398; Lemma 4.1 l.398 |
| CD | Castella–Do, arXiv:2303.06751v2 = H9 lane file 33 | e01027bc2c5cfc98 | Thm 6.5.1; Thm 6.7.1 l.3115; Rem 6.7.2 l.3135 |

## 1. FILE32_CORRECTIONS

**A. Castella–Do.** Withdrawn: "A4 None can exist inside this machinery", together with the use of "it would be the H9 target" as a
reason to stop. What the sources support: [CD] Thm 6.7.1 needs j >= r and Thm 6.5.1 needs L(f/K,chi,r) != 0. The H9 specialization has
j = 0 < r = 1 and L(f/K,1) = 0, so neither applies directly, and [CD] contains no Sha or Mordell–Weil comparison. That does not show a new
exact comparison cannot be derived; proving the target is what a new theorem would do.
Recorded, as verified linear algebra (Pro's Lemma A1): for ell = log_p ∘ loc_p on S and any subspace W of S,
0 -> S_0/(W ∩ S_0) -> S/W -> ell(S)/ell(W) -> 0 is exact. If one nontorsion rational point P exists, then ell(W) = ell(S) = Q_p, so
V_p Sha(E/Q) ≅ S_0/(W ∩ S_0), realized by s |-> s - (ell(s)/ell(delta P)) delta P. This is statement-level linear algebra over Q. It is not a
Castella–Do dual-module theorem, and it does not show the quotient vanishes.

**B. Higher-core-rank systems.** Withdrawn: "and none is primitive" (file 32 B3), and the verdict KILLED for all of gate B.
[MR] §13 defines a stub Kolyvagin system as primitive when it generates KS'_r(T), equivalently when kappa_n generates
m^{lambda(n)}(wedge^r H^1_{F(n)}(K,T)) ⊗ G_n for every n. Corollary 13.1(iii) treats a primitive system with kappa_1 = 0, which then forces
length H^1_{F*}(K,T*) >= k. For R a DVR and nonzero kappa in KS'_r(T), Theorem 13.4 gives: (iv) corank H^1_{F*}(K,T*) = ord(kappa);
(vii) kappa primitive iff dphi_kappa(infinity) = 0; (viii) length H^1_{F*}(K,T*) finite iff kappa_1 != 0.
Retained, now with a published locator: in the kappa != 0 H9 regime the relevant dual Selmer group is strict at a prime above p and
contains the strict line, so it is infinite. Theorem 13.4(viii) therefore gives kappa_1 = 0 for every nonzero stub system of positive
core rank, under hypotheses (H.1)–(H.6). That obstructs only a proposal needing a nonzero underived bottom class.
Also corrected: file 32 B1 cited "KS_r(T) free of rank one" from Rubin's 2012 slides. In the published paper this is Theorem 11.7(i),
for the stub module KS'_r(T). For core rank one, KS'_1 = KS_1 (Remark 11.5).

**BKS.** Corrected: file 32 B4 and the lane ledger said the Generalized Perrin-Riou Conjecture reaches Mordell–Weil regulators "only through
the BSD formula". In fact [BKS] Def 4.10 builds the Bockstein regulator from a basis of E(Q) and log_omega. Prop 4.14 restates Conjecture 4.8
as kappa_inf = (L*_S(E,1)/(Omega_xi R_inf)) · R^omega_Boc, with the Néron–Tate regulator R_inf. Theorem 6.2, the generalized Rubin formula,
is proved. The operative limitation: §4.3 (l.1454) and Theorem 6.2 assume Hypothesis 2.2, and part (iii) of that hypothesis is
"Sha(E/Q)[p^inf] is finite". So using that package to prove the same finiteness is circular. §3 (l.1017–1024) needs neither r_alg > 0
nor finite Sha unless it says so, and the objection does not extend there.

**C. Families.** Withdrawn: file 32 C2's closing sentence and the 2026-09-16 chat claim that Zywina's method "cannot run at a prime p > 3 with
E[p] irreducible", and file 32's "p >= 5 NOT STARTABLE". A rational 2-torsion point is compatible with a surjective mod-5 representation.
2-descent supplies two rational directions but no 5-primary bound. The rational-5-torsion discriminant example concerns only that
family. Replacement status: rank 2 and Sha[2] = 0 are an existing theorem [ZY]; good ordinary reduction and surjective mod-5 image on an
infinite subfamily are verified in §2; the uniform 5-primary bound is open (§4).

## 2. C1_COMPATIBILITY_PROOF_AUDIT — PASS

Family C1: A = m + 16n^2, B = m + 25n^2, E: y^2 = x^3 - 5Ax^2 + 4ABx, with m ≡ 491 (mod 840), n ≡ 0 (mod 420), m, n > 0, and m, A, B prime.

| item | claim | verdict and check |
|---|---|---|
| C1.1 | infinitely many members | PASS. [TZ] Thm 1.3: A ⊂ P of positive relative upper density; P_i in Z[m] with P_i(0) = 0; infinitely many x + P_i(m) in A with m > 0. Primes ≡ 491 mod 840 have relative density 1/phi(840) = 1/192 (Dirichlet). The polynomials 0, 16(420u)^2, 25(420u)^2 vanish at 0 and are ≡ 0 mod 840 (script). |
| C1.2 | Zywina applies | PASS. 840 = 24·35 and 491 ≡ 11 (mod 24), so all three primes are ≡ 11 mod 24. |
| C1.3 | E(Q) ≅ Z/2 × Z^2, P1 and P2 independent, Sha[2^inf] = 0 | PASS. [ZY] Thm 1.2 and Lemma 3.5: E(Q)/2E(Q) ≅ (Z/2)^3 is generated by P0, P1, P2 with P0 the 2-torsion point, so P1 and P2 span the free part mod 2 and are independent. Sha[2] = 0 (l.55–56), hence Sha[2^inf] = 0. |
| C1.4 | pairwise distinct j | PASS. j = 16(13m + 100n^2)^3 / (9 m B^2); reducedness is [ZY] Lemma 4.1 and was rechecked (13m + 100n^2 ≡ 2 mod 3, ≡ 100n^2 mod m, ≡ -225n^2 mod B; m and B do not divide 30n). The denominator recovers m and B, then n. |
| C1.5 | c4 = 16A(13m + 100n^2), Delta = 2^8 3^2 m A^3 B^2, points on the curve | PASS (script, exact polynomial identities). |
| C1.6 | a_5 = -2, a_7 = 0; 5 good ordinary | PASS. m ≡ 1 and n ≡ 0 mod 5 and mod 7 reduce the curve to y^2 = x^3 - 5x^2 + 4x; #E(F_5) = #E(F_7) = 8 (script and hand count). |
| C1.7 | mod-5 representation irreducible | PASS. Frob_7 has X^2 + 7 ≡ X^2 + 2 over F_5, discriminant 2, a nonsquare. |
| C1.8 | transvection at m | PASS. v_m(Delta) = 1; c4 ≡ 25600 n^4 (mod m) is nonzero because m does not divide 10n; the model is minimal with I_1 reduction and 5 does not divide v_m(Delta). |
| C1.9 | image GL_2(F_5) | PASS. If all conjugates of the transvection fixed one line, that line would be stable, contradicting irreducibility. An upper unipotent conjugation moves the second fixed line to <e2>. Upper and lower unipotents generate SL_2(F_5) (script: order 120), and the cyclotomic determinant is onto F_5^×. |
| C1.10 | Tamagawa product prime to 5 | PASS, with added precision. Minimal model everywhere (valuations 8, 2, 1, 3, 2 < 12). Reduction types: 3 multiplicative I_2 (c4 ≡ 1 mod 3); m I_1; B multiplicative I_2 (c4 ≡ 32400 n^4 mod B); A additive type III (v_A(Delta) = 3, v_A(c4) = 1, v_A(j) >= 0); 2 additive (v_2(c4) = 4). So c_3, c_B <= 2, c_m = 1, c_A = 2, c_2 <= 4. |
| C1.11 | E[5] ramified at m, A, B | PASS (used in §5). At m and B, 5 does not divide v(Delta). At A, reduction is potentially good and inertia acts through a group of order 4, prime to 5, which injects into GL_2(F_5). |
| C1.12 | normalization | PASS. Least-degree isogeny to the strong Weil curve has degree prime to 5, since a kernel of order divisible by 5 would contain E[5] by irreducibility. 5-primary Selmer groups, Sha[5^inf] and 5-parts of component groups are preserved. (5 ∤ c_phi) holds because 25 does not divide N ([CS] l.72, citing Mazur Cor 4.1). E(Q_5)[5] = 0 since #E(F_5) = 8. |
| C1.13 | Castella's curve-side hypotheses | PASS. Root number +1 ([ZY] l.94–98); L(E,1) = 0 because rank 2 (Kato–Kolyvagin); q = m exactly divides N, m ≡ 1 mod 5 and E[5] is ramified at m; image contains SL_2(F_5). |

## 3. KIM_CS_HYPOTHESES_AND_NONCIRCULARITY

Hypotheses as printed:
- [KIM] Thm 1.8: p >= 5, rho-bar surjective, Manin constant prime to p, ord(delta~) < inf. Conclusions (1)–(3) need no Sha assumption;
  (4)–(6) add "finiteness of Sha(E/Q)[p^inf]" (l.382).
- [KIM] Cor 1.6: under the same curve hypotheses, good ordinary reduction at p gives delta~ not identically zero, so ord(delta~) < inf.
- [CS] Thm B: p > 3, (sur), (p ∤ c_phi), and p good ordinary give M_inf(delta) = ord_p(Tam_E). [CS] l.120: delta_n = 0 unless
  (-1)^{nu(n)} = epsilon.
- [KIM] Thm 1.10 (mod p) also needs E(Q_p)[p] = 0 and all Tamagawa factors prime to p.
All of these hold at p = 5 for the strong Weil curve in the isogeny class of every C1 member (§2).

Pro's Lemma C2 is VERIFIED, and it sharpens to an equivalence.

**Proposition K (proved here from the printed statements).** Let E be in C1 and p = 5.
- (a) ord(delta~) = corank Sel_{5^inf}(E/Q), and this is an even integer >= 2.
- (b) Sha(E/Q)[5^inf] is finite iff ord(delta~) = 2, iff some n in N_1 with nu(n) = 2 has delta_n != 0.
- (c) When Sha(E/Q)[5^inf] is finite, ord_5 #Sha(E/Q)[5^inf] = M_2(delta) = min{M(n) : nu(n) = 2}.
- (d) Hence, for every C >= 0: some n with nu(n) = 2 has delta_n != 0 and M(n) <= C, iff #Sha(E/Q)[5^inf] <= 5^C.
  In particular, a 5-adic unit two-prime witness exists iff Sha(E/Q)[5^inf] = 0.
- (e) For any auxiliary (K, chi) as in Castella's Choice 5.2.1 with q = m: kappa_5(E) != 0 iff Sha(E/Q)[5^inf] is finite.

Proof.
- (a) Cor 1.6 gives ord < inf, and Thm 1.8(1) gives equality with the corank. The corank is at least rank E(Q) = 2, and it is even by
  [CS] l.120 with epsilon = +1.
- (b) Since rank E(Q) = 2, the Kummer sequence shows Sha[5^inf] is finite exactly when the corank is 2. Combine with (a).
- (c) Thm 1.8(3) and [CS] l.136 give length(Sel/Sel_div) = M_2 - M_inf. [CS] Thm B gives M_inf = ord_5(Tam) = 0. When Sha is finite,
  Sel_div is the image of E(Q) ⊗ Q_5/Z_5, so Sel/Sel_div ≅ Sha(E/Q)[5^inf].
- (d) Follows from (b) and (c): M_2 is a minimum over two-prime n, and M(n) < v_5(I_n) whenever delta_n != 0.
- (e) If kappa != 0, Castella Thm A(1) gives dim Sel(Q, V_5E) = 2, so the corank is 2 and Sha is finite. Conversely, if Sha is
  finite then dim Sel = 2, and loc_5 is nonzero on Sel because log_5(P1) != 0; Thm A(2) then gives kappa != 0. □

Noncircularity. The direction "two-prime witness gives finite Sha" uses only Thm 1.8(1) and the known rank, as Pro says. But (b)–(e)
show the certificate is equivalent to the conclusion on C1. A nonzero two-prime Kurihara number, a nonzero generalized Kato class and
finite 5-primary Sha are one statement for these curves, and a valuation-bounded witness is exactly a Sha order bound. The Kurihara
language gives exact bookkeeping, not leverage: a proof of the witness is a proof of 5-primary Sha finiteness, and nothing less.

## 4. EXACT_NEW_ARITHMETIC_PROPOSITION

(P_fin) There is an explicitly specified infinite subfamily F of C1 such that every E in F has some n = ell_1 ell_2 in N_1 with
delta_n(E) != 0.

(P_C) There are C >= 0 and an explicitly specified infinite subfamily F of C1 such that every E in F has some n = ell_1 ell_2 in N_1
with delta_n(E) != 0 and M(n) <= C.

By Proposition K, (P_fin) is equivalent to "Sha(E/Q)[5^inf] is finite for every E in F", which is also equivalent to kappa_5(E) != 0 on F.
(P_C) is equivalent to "#Sha(E/Q)[5^inf] <= 5^C for every E in F". The subfamily F must be cut out by a condition that is not itself
equivalent to the conclusion.

## 5. PROPOSED_MECHANISM_AND_RESOURCE_ESTIMATE

Candidates, written before any computation:

- **M1, congruence transport.** Implication tested: if two curves share the mod-5 representation, their Kurihara numbers agree mod 5 up to
  a unit and level corrections, since mod-5 modular symbols are determined by the mod-5 eigensystem. One unit witness would then
  transfer across the subfamily.
  **KILLED on C1, by theory with no computation.** By C1.11 the mod-5 representation of each member is ramified at its own primes m, A
  and B, all at least 491. Two members with equal representations have equal ramification sets, so equal ordered triples m < A < B,
  hence the same (m, n). No fixed residual representation, from a member or from an outside reference curve, covers more than one member.
- **M2, rank-two refined Mazur–Tate / Generalized Perrin-Riou identity.** Implication: delta_{ell1 ell2} ≡ unit · (#Sha · Tam / #tors^2)
  · det[reduction of P_j at ell_i] modulo higher terms. A Chebotarev choice of ell_1, ell_2 would then make the determinant a unit.
  **NOT ADMISSIBLE.** In rank 2 this is conjectural. The regulator package in [BKS] §4.3 and Conj 4.15 (l.1580) is stated under
  Hypothesis 2.2(iii), finite Sha, and the formula carries #Sha. Even a proof would bound the witness only given a Sha bound.
- **M3, Kim's mod-5 semi-local description.** [KIM] Thm 1.10 applies to C1: it yields an n with delta_n != 0 mod 5 at nu(n) = ord(delta~^(1))
  and Sel(Q, E[5]) ≅ ⊕_{ell | n} E(F_ell)/5.
  **No leverage.** It does not fix nu(n), and nu(n) = 2 is again Sha[5] = 0.

Resource estimate for any computational test on actual members (`runs/smallest_member.py`; 0.59 s, 49 MB):
- The smallest member is m = 3011, n = 420, A = 2,825,411, B = 4,413,011.
- log10(m A^2 B) = 23.03 and N = 2^{f_2} · 3 · m · A^2 · B with 2 <= f_2 <= 8, so 10^24.1 <= N <= 10^25.9. f_2 was not computed, since PARI
  and Sage are not installed.
- Its first depth-1 admissible primes are 211, 271, 631, 811, 1021 and 1601, each with v_5(I_ell) = 1.
- The smallest two-prime modulus, n = 211 · 271 = 57,181, needs phi(n) = 56,700 modular symbols [a/n]^+.
- A modular-symbol space at level N has dimension about N/12, at least 10^23. Evaluating individual symbols through twisted L-values or
  period integrals needs on the order of sqrt(N) · n, at least 10^16, Fourier coefficients.
- Both exceed the ceiling (one process, 4 GiB, 20 CPU-minutes) by many orders of magnitude. FEASIBILITY FAILED; no implementation launched.

## 6. RESULT_AND_PRECISE_REMAINING_OBLIGATION

Outcome: **UNKNOWN**, with one proved implication and one killed candidate.
- Proved: Proposition K. On C1 at p = 5, a two-prime Kurihara witness, a nonzero generalized Kato class and finite Sha[5^inf] are equivalent.
  A witness of valuation at most C is equivalent to #Sha[5^inf] <= 5^C.
- Killed: M1, congruence transport. The residual representation changes with the ramification set {m, A, B}.
- Not admissible: M2 (circular) and M3 (no control of the index).
- Remaining obligation: an arithmetic mechanism, not equivalent by definition to its conclusion, that proves Sha(E/Q)[5^inf] finite for
  every curve in an explicitly specified infinite subfamily of C1 (P_fin), or with a uniform bound (P_C). Equivalently, one that forces a
  nonzero two-prime Kurihara number, or a nonzero generalized Kato class, uniformly. It has to work while the mod-5 representation changes
  from member to member.
- Nonclaims: no Sha[5^inf] finiteness is proved for any member; no Kurihara number was computed; no H9 or H41 sealed status changed.
  C1 is Pro's compatibility corollary of Zywina and Tao–Ziegler, audited here. Proposition K is an equivalence, not a uniform theorem.

## Return

```
FILE32_CORRECTIONS                 = A impossibility WITHDRAWN (direct application still NOT_APPLICABLE; Lemma A1 recorded);
                                     B "none primitive" WITHDRAWN (MR Cor 13.1(iii), Thm 13.4(vii)); bottom zero RETAINED (Thm 13.4(viii));
                                     BKS description CORRECTED (Def 4.10, Prop 4.14; circular only via Hyp 2.2(iii)); C "not startable" WITHDRAWN
C1_COMPATIBILITY_PROOF_AUDIT       = PASS (C1.1-C1.13; reduction types added: 3 I_2, m I_1, B I_2, A III, 2 additive)
KIM_CS_HYPOTHESES_AND_NONCIRCULARITY = HYPOTHESES MET on C1 at p = 5; C2 VERIFIED; SHARPENED to Proposition K (equivalence)
EXACT_NEW_ARITHMETIC_PROPOSITION   = (P_fin) / (P_C), equivalent to finite / 5^C-bounded Sha[5^inf] on an explicit infinite subfamily
PROPOSED_MECHANISM_AND_RESOURCE_ESTIMATE = M1 KILLED; M2 NOT ADMISSIBLE; M3 NO LEVERAGE; smallest conductor 10^24.1-10^25.9; FEASIBILITY FAILED
RESULT_AND_PRECISE_REMAINING_OBLIGATION = UNKNOWN; missing: a non-tautological mechanism for (P_fin) or (P_C)
```
