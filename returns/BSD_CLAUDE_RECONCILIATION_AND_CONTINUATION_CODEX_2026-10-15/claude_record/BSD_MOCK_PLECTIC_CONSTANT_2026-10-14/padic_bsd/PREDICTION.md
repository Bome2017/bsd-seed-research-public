# p-adic constant check — sealed before running (2026-10-14)
For each curve below (rank 2, Sha_an = 1 by Cremona curvedata) and each good ordinary prime p in {5,7,11,13,17,19,23}:
PARI ellpadicbsd returns analytic p-adic rank r = 2, and Lp / ellpadicregulator(Cremona generators) = 1 (= Sha_an) to the
returned precision. Meaning: the p-adic rank-two class at every tested prime is the SAME rational multiple (#Sha*Tam/tors^2,
built into PARI's normalization, i.e. K_E/(4 c_inf)) of one global class P1^P2. Curves: 389a1 433a1 664a1 655a1 1615a1
1001c1 1309b1 1653a1. Known territory (p-adic BSD numerics); here it is the exact form of the wild-leg (a_p-1)^2 law.
