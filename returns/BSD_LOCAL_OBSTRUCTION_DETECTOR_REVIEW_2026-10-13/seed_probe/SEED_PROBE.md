# Sealed bounded seed local-quotient probe

Date: 2026-10-13. This protocol is written before the scan.

Seed model E = [0,-1,0,-66020924,-65074271436].
Retained full Mordell--Weil basis P1=(-3031,327384), P2=(-2394,281520).
Coefficient prime p=5. Retain the previously certified Sha(E/Q)[5]=0; this probe
neither re-proves nor uses numerical L-values to infer it.

Scan rational primes q in ascending order with q<=30000, q not 5 and q of good
reduction. Admit exactly the q with v_5(#E(F_q))=1. Compute [#E(F_q)/5]P_i for
both basis points. Stop at the FIRST admitted q where both are zero. Save all
admitted rows up to that stopping point, including the nonzero-image controls.
If there is no hit, report only NO_HIT_THROUGH_30000.

Independently re-count E(F_q) and implement its finite-field group law in Python
for the first hit. Also find an explicit point R with [#E(F_q)/5]R nonzero.
These checks establish a nonzero local quotient E(Q_q)/5 with zero global
Mordell--Weil image, assuming the retained basis/saturation. They cannot prove
Selmer localization surjective or supply a Sha upper/lower bound.

Expected comparison: the quotient target can be nonzero even when retained
Sha[5]=0. A local target is not automatically the image of global Selmer classes.
No new L-value, height, or Selmer-group calculation is authorized by this probe.
