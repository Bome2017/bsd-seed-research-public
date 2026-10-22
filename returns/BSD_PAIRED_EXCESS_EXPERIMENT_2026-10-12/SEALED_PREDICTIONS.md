# Sealed before new A-side calculation

P=5, d=43737. Exact source A0=[0,-1,1,-10,-20].
Specified A points from prior return. Predictions derived from the isogeny, not fed into producers:
- [U^2] L_A = 4*5 + O(5^2).
- det H_U,A = det H_U,F.
- L_F=5 L_A in matched Neron normalization.
- M^t H_F M = 5 H_A, M=[-1,3;-1,-2].
- corrected Q_A=1+O(5), Q_F/Q_A=25 to available precision.
One numerator run at precision5 with fixed4GB stack; direct series required.
Independent tests mean no F value passed to A producer, not separate modular symbol software.

Next bounded discovery: extend previous classgroup filter from d=43738 to300000, at most12 new surviving S-class candidates,6000 screened fields,or120seconds; at most6 exact-rank-two height cases. Search for nonunit U-regulator. Classgroups only select candidates; final Sha claims require separate isogeny proof. Save all candidates and ambiguous ranks. Do not compute numerator except for a positive excess candidate with nonunit regulator.

## Second geometry screen, sealed after first bounded screen
First screen cost 2.096s, selected12 candidates and3 calculable rank-two pairs; all regulator units. One exact-rank-two curve had only one point and remains unmeasured. Extend from97718 to2000000,200 S-class candidates,100000 fields,24 calculable rank-two pairs,or120 seconds, whichever stops first. Stop at first v5(det H_U)>0 with isogeny point index5; no extrapolation from absence. Numerator only after the candidate has an independent positive-excess proof.

## New combined control d=329233
Selected independently by exact rank2, point-map determinant5, local products20/4, and v5(det H_U)=2. Its height/log lines coincide. Expected corrected excess if the earlier pattern persists: v5(L2)=4, v5(Q)=2. This is a prediction, not a certified Sha order. Attempt numerator at precision7, fixed4GB stack,180second cap. A precision or memory failure is not zero.

## Memory repair
Official whole-sum run overflowed4GB, rejected. Partial-sum patch changes only three b-loop ranges, starts partial accumulator at0, and sums output moments modulo original5^(n+vden). Exact full moments match original on d13,29,-7 and the prior d43737 at precision5. New combined control attempt at same n7,512MB stack,batch2000,180seconds. No prediction changed.

## One-digit continuation
The accepted n7 run returned L2=O(5^4), HU exact valuation2, so corrected Q is only O(5^2). No exact numerator/quotient valuation inferred. n8 attempt raises precision by1 with512MB,batch2000,300second cap; partial moments saved every20chunks. Predictions remain vL2=4,vQ=2, allowed to fail.
