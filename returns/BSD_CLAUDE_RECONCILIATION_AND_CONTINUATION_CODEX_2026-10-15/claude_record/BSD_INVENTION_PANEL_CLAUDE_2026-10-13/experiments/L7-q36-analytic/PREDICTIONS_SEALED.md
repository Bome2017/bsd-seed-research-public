# Sealed predictions (written 2026-10-13 BEFORE any run on the F/A pair), lens L7-Q36-ANALYTIC

Curves: A = minimal model of elltwist(11a1=[0,-1,1,-10,-20], 43737); F = minimal model of elltwist(11a2=[0,-1,1,-7820,-263580], 43737).
Record inputs (BSD_ODD_EXCESS_CONTROL_EXPERIMENT_2026-10-12/PROOF.md:7-86; BSD_VALUATION_MECHANISM_REVIEW_2026-10-13/CONTROL_GROUPS.md:14-39):
rank 2 both, trivial torsion, Tam A:(1,5,2,2)=20, F:(1,1,2,2)=4, Omega_F/Omega_A=1/5, Sha(F)[5^inf]=(Z/5)^2, Sha(A)[5^inf]=0, 5-isogeny phi:A->F with det M=5.
Points on F (record): Q1=(6288329,-11502941299), Q2=(8502485,21568458354).

Hypothesis under test ("same integer across p" shape of exact MTT / Q.3 common scalar): the p-adic MTT quotient
Lp/Reg_p (PARI ellpadicbsd normalization: Tamagawa, torsion, Euler factor removed) equals #Sha(C) as an INTEGER at every good ordinary p,
including p NOT dividing #Sha.

Predictions at p = 7 (and 11, 13 if run):
P1 (unconditional on #Sha(A)): [Lp(F)/Reg_p(F)] / [Lp(A)/Reg_p(A)] = 25 (mod p^k for every computed k).
P2 (conditional on #Sha(A)=1, to be checked by the real q_A ~ 20): Lp(A)/Reg_p(A) = 1 + O(p^k), Lp(F)/Reg_p(F) = 25 + O(p^k).
P3 (real, BSD-conditional): q_A = L''(A,1)/(2 Omega_A Reg_A) in (19.99, 20.01); q_F in (99.9, 100.1).
FAIL criterion: P1 false at any k >= 2 with 389a1 control giving 1+O(p^3) under the same code path (it did: p=5,7 -> 1+O(p^3)).
Interpretation of PASS: collateral numerical support for the common-scalar shape at a positive-Sha curve at p not dividing #Sha; NOT a theorem, no endpoint effect.

## Addendum (written 2026-10-13 after the p=7 run, BEFORE the p=13 run)
p=7 result: Q_7(F) = 4+3*7+O(7^3) = 25, Q_7(A) = 1+O(7^3): P1, P2 PASS. Real: q_A=20.000..., q_F=100.000... (40 digits): P3 PASS.
p=11 excluded from the test: 11 | N_F = 11*43737^2 with split multiplicative reduction (43737 = 1 mod 11), exceptional zero, MTT has an extra zero.
p=13 (a_13 = -4, ordinary, good): same predictions: Q_13(F) = 25 = 12 + 13 + O(13^k), Q_13(A) = 1 + O(13^k), ratio 25.
