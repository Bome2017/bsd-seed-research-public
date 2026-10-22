# 31 — COEFFICIENT-GATE SOURCE CHECK + scope corrections to audit 26 (2026-09-16)
Bounded source check, as the operator relayed it. Read-only. No new H9R number. No agent launched. Nothing built. H41 untouched.
No status of any sealed object changes.

Input: `28_SRC_pro_H9_audit26_response_and_coefficient_gate_2026-09-16.md` (byte copy of the iCloud note;
sha256 b631866c41f8359cb7121767e4da62d19cff6ca50b8cbdb22c439f8c8053b13e), with the operator's framing: send the coefficient-field lemma,
limited to algebraicity over Q, "for a bounded source check. No H41 status, sealed H9 theorem, or build authorization should change."

## Sources
[FP16] Fuchs–Pham, "Some applications of the p-adic analytic subgroup theorem", arXiv:1412.1248v2 (v1 3 Dec 2014, v2 11 Jan 2016; arXiv
       lists "Accepted for publication in Glasnik Matematicki"). PDF sha256 b880eebbda5b94fbb9c96c129ce20c7134d32769326f524623e96965b2aa0053;
       text = lane file 29. The text layer DROPS the overline on Q. Pages 2-3 were rendered and read as images; every field quoted below as
       Q̄ was confirmed on the image. Locators (page / text line): Thm 1.1 p.2 / l.73; A_p and A_Q̄ = {alpha in A_p : exp(alpha) in A(Q̄)}
       p.2; Thm 2.1 p.2 / l.93; End(a) "the ring of endomorphisms of a (defined over Q̄)" p.3; Thm 2.2 p.3 / l.115; Thm 2.3 p.3;
       proof of Thm 2.2 l.196-221.
[FP15] Fuchs–Pham, "The p-adic analytic subgroup theorem revisited", arXiv:1502.00768v1 (3 Feb 2015); p-Adic Numbers, Ultrametric Analysis
       and Applications 7 (2015) 143-156 (per arXiv). PDF sha256 f208a43e4e1c152965453f27a403ff1f45129240ae157c2c4cd2526a6af86f1a; text = lane
       file 30. Thm 2.2 (text l.88-91) is the same theorem as [FP16] Thm 1.1 (text layer only; overlines not re-checked on images here).
       Credits: Matev, arXiv 1010.3156 (preprint), and Bertrand, Astérisque 145-146 (1987), Remarque 2 p.37, "without proof and in
       equivalent form" (text l.34-40, refs l.722, l.728).
[Ho]   Howard arXiv 1202.6358 (lane-3 source copy) l.64-65: F_p = residue field of R_p at an arithmetic prime, "a finite extension of Q_p".
[LV]   Longo–Vigni arXiv 0903.2797 (lane-3 source copy) l.2439-2440: the same convention.
[CH]   Castella–Hsieh arXiv copy (sha256 8302d020...) l.702: "V = T_pE (x)_{Z_p} L with L a finite extension of Q_p".
Not re-read here: the published Castella–Hsieh text (Pro read it; its inequality sum_i r_i d_i <= ord_J Theta matches the arXiv
inequality 2rho >= sum_i i e_i at l.1441 once odd layers vanish); the Glasnik publisher PDF; Matev's preprint.

## 1. The lemma — CONFIRMED
Statement (note sec 4.1). E/Q non-CM; M = E(Q)/E(Q)_tors; F_alg = Q̄ ∩ Q_p for a fixed embedding; log_p normalized by an invariant
differential defined over Q. Then ell_p : M (x)_Z F_alg -> Q_p, sum_i P_i (x) a_i |-> sum_i a_i log_p(P_i), is injective.

Source statement, read on the page image ([FP16] Thm 2.2): A a simple abelian variety (defined over Q̄, per the setup on p.2);
u_1, ..., u_m in A_Q̄ linearly independent over End(A) are linearly independent over End(a). For dim A = 1, End(a) = Q̄. For E non-CM,
End(A) = End_Q̄(E) = Z.

Proof check (note sec 4.3):
 (i)   Choose N with every N P_i in exp(A_p); A_p is open ([FP16] p.2). Then u_i := log(N P_i) lies in A_Q̄.                       OK
 (ii)  The u_i are Z-independent: log has torsion kernel on E(Q_p), so a Z-relation would make a Z-combination of the P_i torsion.  OK
 (iii) [FP16] Thm 2.2 makes the u_i Q̄-independent, hence also log_p(P_i) = u_i / N.                                                OK
 (iv)  Lie(E)(C_p) = C_p is identified through the Q-rational differential, which preserves Q̄-linear relations.                  OK
 (v)   M is free on the P_i and F_alg is contained in Q̄, so ell_p is injective.                                                    OK
Second route in the same source: [FP16] Thm 2.1 with k = 1, n_0 = 0, E_1 = E, L_1 = Q gives dim_Q̄ <1, v_1, ..., v_n> = 1 + dim_Q <v_1, ..., v_n>
for p-adic elliptic logarithms of algebraic points. This is the inhomogeneous form: a_0 + sum a_i log_p(P_i) = 0 with all a_i in Q̄ forces
every a_i = 0. Both theorems are deduced from [FP16] Thm 1.1, so they are not independent evidence.
Remark (derived here, unaudited, not needed because Castella's multiplicative prime excludes CM): for E/Q with CM by K, rational points
independent modulo torsion are also O_K-independent. Apply complex conjugation to alpha P + beta Q = 0 and eliminate Q to get
(alpha beta-bar - alpha-bar beta) P = 0, so alpha/beta is rational. The lemma then extends to CM curves over Q through Thm 2.2.

## 2. H9 consequences — CONFIRMED, with their limits
C1 Put W_alg = delta(M (x) F_alg) inside S = Sel(Q,V_pE). Then W_alg ∩ ker(loc_p) = {0}. If b in Q_p is nonzero, v in W_alg and
   b v in ker(loc_p), then v = 0. (delta is injective on M (x) F_alg, and loc_p followed by log is ell_p on Kummer classes.)
C2 For independent P, Q in E(Q), log_p(Q)/log_p(P) is transcendental over Q. This agrees with Castella Remark (2) and CH Cor 5.1: the
   conjectured algebraicity concerns the common scalar in front of log_p(Q)P - log_p(P)Q, not the coordinate ratio.
C3 The test is NOT closed under limits. F_alg contains Q, which is dense in Q_p. Rational c_n -> c = log_p(Q)/log_p(P) give
   c_n P - Q -> cP - Q, which has zero logarithm. The one-direction test (a closed line) survives limits; this test does not.
C4 p-adic coefficient fields are outside the test: a finite extension of Q_p contains elements transcendental over Q.

## 3. What the test reaches inside this record
- 08 terminal block, consequence (a): "a P in E(Q) (x) L with Kum(P) != 0, loc_p Kum(P) = 0 ... exists iff rank >= 2". There L is a
  finite extension of Q_p ([CH] l.702), so the statement stands. ANNOTATION: with L a number field, or any coefficient field algebraic over
  Q, no such P exists at any rank (C1).
- Milestone 05 l.41: the unproved chain ends in E(Q) (x) F_g. F_g is not defined in the local record. In the standard convention it is the
  residue field of the Hida Hecke algebra at the arithmetic prime of g, a finite extension of Q_p ([Ho] l.64-65; [LV] l.2439-2440). The
  chain's target is therefore outside the test (C4), and the chain is limit-type in any case (C3).
- The sealed tower has no defined descended output (26 sec 2), so this test says nothing about it, exactly as G-SUPPORT could not.
- No killed route in 08 is killed again or revived by this test.

## 4. Scope corrections to audit 26 — ACCEPTED (also appended to 26 as a supersession, and to the 08 ledger)
SC1 Status words. In this lane "LANE CLOSED" meant a stopped route, while "H9R16C = CLOSED" meant a proved theorem. From now on:
      CURRENT_H9_CONSTRUCTION      = STOPPED AT ITS RECORDED BOUNDARY
      UNIFORM_H9_ARITHMETIC_TARGET = OPEN
      NEW_ADMITTED_MECHANISM       = NONE IDENTIFIED
SC2 Certificates. 26 N6 R1's "Certificate A never supplies information that Certificate B lacks" holds only for the inspected printed
    criteria, as logical redundancy. It is not a cost comparison. A new geometric proof of kappa != 0 (which yields dim Sel = 2 through
    Castella Thm A(1)) or of kappa in W would be new information. The 2026-09-16 chat sentence "Certificate A is never cheaper than
    Certificate B" is WITHDRAWN.
SC3 26 N6's closing sentence is replaced by: "The inspected instance criteria already contain sufficient arithmetic bounds, so adding kappa
    as an intermediate conclusion is unnecessary for those finiteness deductions. No additional arithmetic contribution of the currently
    sealed tower has been established."
SC4 Wall label. 26's corrected label holds under the full hypotheses of Castella's Theorem A, including the auxiliary choice, with
    kappa_p(E) != 0. Asserted for every curve of Selmer corank 2 it is a strictly stronger target.
SC5 Dating. 26's use of Stein–Wuthrich l.139-140 reports the authors' statement at the time of writing, not a 2026 literature survey.
SC6 Admission gate. G-CYC is REPLACED by G-WSHA: when kappa != 0, dim S = 2 is already a conclusion of Castella's Theorem A, so another
    upper bound on S adds nothing. A proposal must give information about W (a rational lower bound), about V_p Sha, or an argument that
    puts kappa in W. A bound on a different Selmer structure counts only after an exact comparison with V_p Sha.
    NEW G-COEFF: a proposal aimed at the nonzero strict class cannot end in a finite vector whose coordinates in a rational Mordell–Weil
    basis are algebraic over Q, even up to one common p-adic scalar (C1). It must name its genuinely p-adic coefficient or limit
    mechanism, and that mechanism must separately handle descent, control and the live branch.

## Return
```
COEFFICIENT_LEMMA            = CONFIRMED ([FP16] Thm 2.2 on page images, Q̄ verified; also [FP16] Thm 2.1)
UNDERLYING_THEOREM           = p-adic analytic subgroup theorem = [FP16] Thm 1.1 = [FP15] Thm 2.2 (published 2015; Matev; Bertrand)
H9_CONSEQUENCES              = C1-C4 CONFIRMED; the test is not closed under limits and does not cover p-adic coefficient fields
REACH_IN_RECORD              = 08 consequence (a) annotated; 05 l.41 chain outside the test; sealed tower untouched; no route status changes
SCOPE_CORRECTIONS_TO_26      = SC1-SC6 ACCEPTED
ADMISSION_GATE               = G-DATUM, G-MECH, G-REUSE, G-SUPPORT, G-AUX, G-WSHA, G-COEFF, G-TEST
CURRENT_H9_CONSTRUCTION      = STOPPED AT ITS RECORDED BOUNDARY
UNIFORM_H9_ARITHMETIC_TARGET = OPEN
NEW_ADMITTED_MECHANISM       = NONE IDENTIFIED
BUILD                        = NONE
```
