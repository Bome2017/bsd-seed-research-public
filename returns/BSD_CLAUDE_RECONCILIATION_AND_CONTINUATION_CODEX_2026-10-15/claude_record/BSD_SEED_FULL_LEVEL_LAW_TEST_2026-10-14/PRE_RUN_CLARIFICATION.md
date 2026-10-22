# Pre-run clarification (written 2026-10-14 before any table at these ell exists)

PREDICTIONS_SEALED.md says c_k uses "N_a, the record pipeline's plus-symbol numerators (lattice 1/1024, omega_1 convention),
exactly as in the p = 83 certificate and c2_from_symbols.py". The binding part is "exactly as in ... c2_from_symbols.py":
N_a is the integer symbol VALUE [a/l]^+ = cand/1024 from the certified XB line (integral on all historical seed runs and on
p83, e.g. XB 1 plus cand 11264/1024 = 11). It is not the raw candidate 11264. The word "numerators" was imprecise.
No prediction value changes: the predictions are 288*(a_l-2)*R_l and do not depend on this convention.

Full-level evaluation rule (fixed now): with g the least primitive root and j(a) = ind_g(a) in [0, l-2],
c_k = sum_a binom(j(a) mod m, k) * [a/l]^+ reduced mod m (m = odd part of l-1). For odd m, binom(j+m,2) - binom(j,2) = m*j + m(m-1)/2 = 0 mod m,
so reducing j mod m before the binomial is exact; the I^2/I^3 coefficient equals c_2 mod m once c_0 = 0 and c_1 = 0 mod m.
The frozen checker reduces j mod p and requires p >= 5 with v_p(l-1) = 1; it is used here for integrity/binding/symbol
identification only. Acceptance: its only failure reasons may be the p-admissibility ones.
