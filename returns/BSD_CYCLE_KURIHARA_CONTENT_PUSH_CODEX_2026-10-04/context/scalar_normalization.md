# Independent source check of the common reciprocity unit

**Verdict: CONFIRMED_IN_THE_PRINTED_SOURCE_CONVENTIONS.**

Primary text: Kim, arXiv:2203.12159v6, §2.2–2.3 and Theorem 3.11 with its proof, printed pp.20–21. The live HTML and the supplied p.21 image agree in the load-bearing display:

https://arxiv.org/html/2203.12159v6#S3.SS4

The theorem statement alone gives an unspecified unit after a chosen lattice coordinate. The proof specifies more: before that coordinate is applied, the exponential image of kappa_n equals E_p delta_n in L_p/I_n L_p, where at good reduction and t=0

    E_p = (p+1-a_p)/p = #E(F_p)/p,
    L_p = E_p Z_p.

This display is independent of n. The earlier E_p(sigma_p) acts on the descended scalar trivially; the source explicitly replaces it by E_p. Section 2.3 fixes a coherent Kato Euler system associated to the real Neron period, and the derivative/edge conventions use the corresponding fixed primitive roots. No independent conductor rescaling is inserted here.

Define xi_p on the fractional lattice by xi_p(E_p*x)=x. The reductions of this single map at all I_n are compatible. Therefore

    (xi_p exp* loc_p^s)(kappa_n)=delta_n

simultaneously. This proves the claimed choice u_n=1 at the source-import grade. It does not infer an exact unit from numerical patterns. Multiplication by p/#E(F_p) is performed on L_p; E_p is not treated as an integral unit or cancelled after an invalid reduction in a different lattice.

The retained E(Q_p)[p]=0 removes H^2(Q_p,T)[p], so the residual singular quotient is the reduction of the integral lattice. No uncontrolled projection onto a local torsion summand is used. This is precisely why the old local-torsion control examples cannot be substituted into the profile.

A different single coherent lattice coordinate introduces one p-dependent unit at every conductor, absorbed into C_p. Separate changes of individual Kato components are not licensed: they may violate the edge relations. A numerical symbol implementation must also document its period and label conversion. This audit does not claim that Opus's saved pair tables already use the source normalization.

The original Kato and KKS reciprocity arguments remain imported. This check independently verifies the exact printed equality and the consequence for a coherent coordinate; it does not reprove those foundational arguments or claim a fresh binary hash match to the live PDF.
