# 2243: reconciliation of D2 and D5

This is a local, source-based reconciliation at the project's published-theorem import grade. It does not compute C_2243, re-prove Skinner's main conjecture, or upgrade any retained numerical input. Existing folders remain untouched. No paid computation is authorized.

## D2: the factor T, including the Selmer object

Skinner, *Multiplicative reduction and the cyclotomic main conjecture*, published text, §2.3 (equations (2-3-2), (2-3-3), Proposition 2.3.2) and the opening of §3.2, p. 193, supplies

    0 -> S -> Sel_Gr -> H^1(F_p,(M^-)^{I_p}) -> 0.

The right-hand group is Q_p/Z_p with trivial Gamma action in the split case. Its Pontryagin dual is Lambda/(T). Consequently

    char_Lambda(X_Gr) = (T) char_Lambda(S^vee).

This is an integral characteristic-ideal equality. It is not obtained by applying the rank-zero conclusion of Theorem B to this rank-two curve. The opening exact-sequence argument only requires the irreducibility/torsion inputs of Proposition 2.3.2, supplied at the retained Theorem A grade.

To identify S with the classical cyclotomic Selmer group: for every finite local extension F of Q_p, split Tate uniformization gives

    E(F) = F^*/q_E^Z,
    0 -> mu_{p^infty} -> E[p^infty] -> Q_p/Z_p -> 0.

Surjectivity F^* -> E(F), compatibility of Kummer maps, and the cohomology sequence show

    im(E(F) tensor Q_p/Z_p -> H^1(F,E[p^infty]))
       = im H^1(F,mu_{p^infty})
       = ker(H^1(F,E[p^infty]) -> H^1(F,Q_p/Z_p)).

Pass to the direct limit in the cyclotomic tower and use Shapiro's identification with Skinner's M. Away from p the classical local Kummer tensor is zero at each finite local field; Skinner explicitly identifies H^1(Q_l,M) with H^1(I_l,M)^{G_Q_l} for l != p (p.181), so the away-p conditions agree as well. Thus S is the classical Selmer group and D2 is supplied, with these identifications recorded. No independent nonzero height computation is needed to obtain this exact sequence.

## D5: separate hypothesis versus consequence of a successful certificate

Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, §6.1, Theorem 6.1, explicitly states that the classical characteristic series has order at least r, with equality if and only if the p-adic height is nondegenerate and the p-primary Sha group is finite. The theorem includes multiplicative reduction and identifies the height with the corrected height in §4.2.

Accordingly, importing that published theorem as stated gives the conditional chain

    C_{2243,3} != 0 mod 2243
    -> [T^3] L_p is a unit
    -> ord_T L_p = 3                  (the lower bound follows from D2 and rank 2)
    -> ord_T char(X_cl) = 2
    -> height nondegenerate AND Sha[2243^infty] finite.

Thus a separate numerical nonzero-regulator certificate is NOT an additional mathematical prerequisite for this sufficient implication at this dependency grade. This is conditional on the successful cubic certificate, not a present claim that the height is nondegenerate.

S1_RESULTS.md instead elects to use Jones's Theorem 3.1 only in its forward direction. Under that narrower proof-reconstruction policy, a separate nondegeneracy input remains needed. The original Jones theorem's forward statement does not refute the stronger published Stein--Wuthrich statement. Conversely, reading Stein--Wuthrich is not an independent reconstruction of Jones/Schneider/Werner. These grades must not be conflated.

## Leading-term normalization and integrality

Use kappa(gamma)=1+p. The locally checked invariant is

    ell_gamma = log_p(q_E)/(ord_p(q_E) log_p(1+p)) = 1799 mod 2243,

so v_p(log_p(q_E))=1 and ell_gamma is a unit. This is the T-variable normalization, not the unnormalized L-invariant.

SW §4.2 uses the corrected split height

    h_p(P) = 2 log_p(e(P)/sigma_p(P)) - log_p(u(P))^2/log_p(q_E)

on points in the formal group and with good reduction at all finite places. An integer multiple prime to 2243 achieves these conditions: all component orders divide 2 and the split local identity-component quotient has order p-1. For such points log_p(u) lies in p Z_p, while every Q_p logarithm lies in p Z_p. Since v_p(log_p(q_E))=1, both terms of the height lie in p Z_p. Dividing by log_p(1+p) and polarizing introduces only p-units. The normalized height matrix and its determinant are integral. This is an integrality argument, not a computation of the determinant.

The SW Theorem 6.1 valuation formula, together with the retained Tamagawa product 16, torsion order 2 and the unit ell_gamma, therefore gives

    0 = v_p(leading char(X_cl))
      = v_p(#Sha[p^infty]) + v_p(Reg_gamma),

where both terms are nonnegative. A unit cubic coefficient consequently suffices for Sha[p^infty]=0 at the retained import grade.

There is a minor normalization label to correct in S1c: the engine's plus period is the least-positive real period omega_1. For this two-component curve the total real Neron period used in the BSD convention is 2 omega_1. Calling omega_1 the SW/BSD total period is inaccurate. The resulting factor 2 is a unit at 2243 and does not alter this nonvanishing test, but exact coefficient labels must specify the convention.

## Status

D2: supplied by the cited exact sequence plus the explicit Tate/Kummer identification above.
D5: redundant as an independently computed premise IF SW Theorem 6.1 is imported as stated; still required under the pilot's stricter Jones-forward-only policy.
No independent height certificate was generated; no C_2243 value was computed. Period/main-conjecture imports and the 1/1024 symbol lattice retain their earlier qualifications. This removes no Sha prime by itself.

Sources read locally:
- /Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/p3_r1_r2_2026-09-19/sources/Skinner2016_published.txt (lines 412--587 and 1193--1237).
- /Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11/aristotle_handoff/ARISTOTLE_C11_RESULT/sources/SteinWuthrich2013_shark.txt (§§4.2,4.4,6.1).
- /Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S1_RESULTS.md.
