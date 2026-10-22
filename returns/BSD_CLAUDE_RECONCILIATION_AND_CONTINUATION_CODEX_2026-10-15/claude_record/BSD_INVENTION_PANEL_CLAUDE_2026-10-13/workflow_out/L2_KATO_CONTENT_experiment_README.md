# L2-KATO-CONTENT inventor pass, 2026-10-13 — experiment notes (replay + pipeline caveat)

Scripts: calib.gp, seed_q.gp, period_check.gp (PARI 2.17.3, nbthreads=1, total CPU < 10 s). Outputs: calib.out, seed_q.out, period_check.out.

1. seed_q.out: seed minimal model [0,-1,0,-66020924,-65074271436], P1=(-3031,327384), P2=(-2394,281520), Tam 16, tors 2, Delta>0.
   R_U := ellpadicregulator(E,p,8,[P1,P2])/log(1+p)^2 is a p-unit with residue 1 at p=5,7,11,13 (Reg_gamma mod p^2 = 21,36,56,144,
   identical to the record's avatar file). With the certified full-real-period cyclotomic coefficients C_p = 1,4,4,1 (p=5,7,11,13):
   Q_p := C_p t^2/(c eps_p R_U) = 4,2,9,9 mod p = 9 mod p at all four primes (prediction of exact MTT p-adic BSD with #Sha=9).
   This REPLAYS record unit E11-080 (BSD_PERIMETER_Q36_2026-09-25/q36/synthesis_checks/avatar_residues_clean.out: q_p = 4 Q_p = 36 mod p). Not new.
2. calib.out / period_check.out: PARI msfromell normalizes by E.omega[1] = identity-component period; for Delta>0 curves
   Omega_full/omega1 = 2 (24a1, 15a1 rank-0 BSD checks), so the lab pipeline one_row.gp / candidate43737_values.gp returns
   Q = 2 + O(p^4) on 389a1 at p=5,7,11 and 1 on 433a1. Valuation law unaffected (2 is a p-unit); the UNIT part of that pipeline
   on a Delta>0 curve is c_inf * (MTT quotient). All lab controls had Delta<0, the seed has Delta>0.
