# Light checks (Claude, 2026-10-07; each one gp/sage process, < 1 min)

1. mtt_389a1_p7.sage — 389a1, p=7 (a_7=-5, ordinary, rank 2, Tam 1, tors 1, c_inf 2):
   Sha_an_padic(7) = 1 + O(7^3)  => MTT quotient == 1 (mod 7); record tame K == 1 (mod 7) (DINF3:116-119). CONSISTENT.

2. wieferich_kp.gp — seed, minimal model [0,-1,0,-66020924,-65074271436], Q1=[-3031,327384], Q2=[-2394,281520],
   N = 6503188012738584 = 2^3*3*2243*4547^2*5843. 2257 good primes 5..20000:
   v_p(log_omega Q_i) >= 2 (single-point elliptic Wieferich) only at p=5 (Q1), 73 (Q1), 107 (Q2), 2659 (Q2);
   p=3581: m1=1, m2 unresolved at precision 10 (ellmul returned [0]).  k_p = 0 at EVERY tested prime (no simultaneous event).

3. bockstein_content.gp — 70 ordinary p in 7..400, p notin S_*: v(Reg_p) = 2 (baseline) except p=17 (v=3, the
   record's 17-divisible regulator); k_p = 0 throughout; vB = 1 (baseline, unit Bockstein content) at ALL 70 primes,
   including p=17.  => the 17-divisible regulator does NOT make delta_17 non-primitive.
