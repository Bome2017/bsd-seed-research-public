# STATUS: PASS_WITH_CORRECTIONS

Lane R25-SR, hostile second reading of R25. Reader B: Claude Opus 5.5, fresh session 48b287, 2026-09-29.
Folder: ~/BSD_R25_SECOND_READER_RETURN_OPUS_B_2026-09-29/. A parallel session [db3ec5] took the OPUS folder; the user chose
"both, separate folders", so the two readings are independent. FABLE_CHECK was opened only after T1-T5 were on disk.

## Result
No step of R25's derivation (D1-D8) is false. No stray power of 3 was found. Every error below leaves #Sha(E/Q)[3^inf] <= 9
unchanged. As in R25, the bound is modulo the declared INPUTS: the height certificate (step 7), (12.5.2) for the seed, B2, and
S.3's a_{4,2}. I did not re-derive those.
Kill tests K-SR1, K-SR2, K-SR3: all PASS (KILL_TESTS.md; exact PARI in checks/ksr12.log).

## Corrections (each with its fix)
C1 (D6(b); also in FABLE's check) Kato 12.5(4) as PRINTED (rendered p.222) reads "length(H^2(V_{F_lambda}(f))_p) <=
   length(H^1(V_{F_lambda}(f))_p/Z(f)_p)". At P = (3) this is vacuous: both sides are 0 once 3 is inverted in the DVR Lambda_(3).
   Fix: cite Kato 13.4(3) (p.226), which bounds H^2(T)_0 = Ker(H^2(T) -> H^2_loc(T)) at every height-one prime. Kato's own
   13.14 ("The inequality in Thm. 12.5 (4) follows from Thm. 13.4 (3)") and 17.13 (p.280) use it this way. At nonsplit 3,
   H^2_loc(T) = 0, and the hypotheses hold (p != 2, unipotent sigma, E[3] irreducible). Then 12.4(3) and 12.6 give
   length H^2(T)_P <= length(H^1(T)/Z(f,T))_P for every P, (3) included. The conclusion char X | L_3 stands (T3).
C2 (D6(b)/O1) "(12.5.1) cannot hold at nonsplit 3" depends on how Kato's sentence is parsed. If the clause "length H^2_loc = 1"
   is not part of (12.5.1), then (12.5.1) HOLDS at P = ker(kappa^{-2} chi). Fix: those P do not contain 3, and 12.5(3), with
   H^2_loc(V)_P = 0, gives the inequality there. (3) is never of (12.5.1)-type (T3).
C3 (D5 Step 2-3; RETURN INPUT 4; D7 item 1) The chi <-> chi^{-1} question is resolved with NO mismatch and NO involution.
   Kato 12.5(1), read literally, gives chi(Col(loc z_gamma)) = alpha^{-(n+1)} tau(chi) L(E,chi^{-1},1)/Omega_+. This equals SW's
   L_alpha(E, chi(gamma)-1) = alpha^{-(n+1)} p^{n+1} G(chi^{-1})^{-1} L(E,chi^{-1},1)/Omega_E for even chi (checked 27 = tau tau-bar).
   Both sides use gamma -> 1+T and sigma -> chi(sigma). Kobayashi's printed l.301-304 and l.320-322 each carry chi in place of
   chi^{-1}, and the two slips cancel. Fix: replace "inherited from Kobayashi's printed split identity" with this literal
   computation (T1). FABLE's involution fallback is true but not needed.
C4 (D5 Step 3) Kato's own L_{p-adic,alpha,omega,gamma} is related by a kappa-shift: Col(loc z_gamma)(psi) = L_Kato(kappa psi), from
   16.2(i) at kappa^r chi^{-1} with r = 1. Fix: state the shift. R25's primary proof already compares SW-normalised values (T1).
C5 (D8 step 7, sharpened) v_3(log_3 kappa(gamma)) = 1, so v_3(Reg_gamma) = v_3(det<,>_p) - 2 exactly. Here Reg_gamma is Jones's
   det<,>_gamma, from p.8: "<,>_p := <,>_gamma log kappa(gamma)". If the certificate's "v_3 = 0" referred to det<,>_p, the chain
   would give only <= 81, and 81 is a square. Fix: the certificate must state det<,>_gamma. FABLE sec. 4.2 reports
   v_3(Reg_PARI) = 2, hence v_3(Reg_gamma) = 0, with a 23/23 rank-1 calibration. That is the needed condition; I have not seen
   it (SECONDARY) (T4).
C6 (D8 step 9) The square fallback (Cassels, finite Sha, B2 gives >= 9) absorbs ANY single stray factor of 3, not only the
   regulator case (K-SR3).
C7 (cosmetic) D2.1 drops the unit H(0) in "p a_n = ..." (T5). D7 item 4: the Manin constant does not enter at all. Both series
   are fixed by interpolation of L-values over periods of omega_E. The Cesnavicius citation is harmless extra safety.

## Steps re-derived by me (DERIVED unless marked)
K-SR1: L_0 = 3/2 and 2 L(E,1)/Omega_+ (Kato 16.2(ii), 12.5(1), 6.2 at source). K-SR2 and T1: Gauss-sum identity for all 10
nontrivial characters of Gamma_1 and Gamma_2 (exact, with a negative control), Kobayashi's rearrangement, Lambda-linearity of
Col, Zariski density. T2: D5 Step 1 (a)-(e): vanishing, ranks, perfect pairing, Kummer onto, Z_3[Gamma_n]-freeness, and log c_0 =
3/2 generating E^(3Z_3) (with a PARI formal-group check). T3: (a2), (a3), the branch, (b) via 13.4(3), (c) the Sigma-imprimitive
sequence, and Kato 6.2, 8.2, 14.9.3, 17.10, 17.13 verbatim. T4: steps 4-6, 8-9 against Jones pp.1-8, 16-18. T5: trace relation,
Dwork's lemma, the D2.3 identity (exact to O(X^32)), integrality of exp(b h) to degree 30 (two negative controls fail as they must).

## Files
KILL_TESTS.md, T1_D5_STEPS2-3_INTERPOLATION.md, T2_D5_STEP1_COL_ISO.md, T3_D6_O2.md, T4_D8_ASSEMBLY_JONES.md, T5_D1_D2_BY_HAND.md,
FABLE_COMPARISON.md, NOTES.md, RESUME.md, STATE.json, checks/ (ksr12, dwork_t5, reg3: .gp + .log), MANIFEST.sha256.
Resources: 1 process at a time, < 1 CPU-min, no web, no subagents, no pushes or messages, no paid compute.

FIN, ORDER9 and Q36 are unchanged.
