/* Lane 3 generic SW evaluator (teichp, an2) copied VERBATIM from D_primes/src/weights.gp (sha256 in lane3_weights_gp.sha256), */
/* applied to the certified symbols [b/81]^+ (s81.gp, generated from run/SYMBOLS_m81.txt).  One statement per line. */
teichp(a, p, k) = lift(Mod(truncate(teichmuller(a + O(p^(k+2)))), p^k));
an2(p, n, sn, snm1, al, good, k) = {my(pn = p^n, S = 0); for(a = 1, p-1, my(w = teichp(a, p, n)); for(j = 0, p^(n-1)-1, my(b = lift(Mod(w * (1+p)^j, pn)), mu); mu = al^-n * sn(b) - if(good, al^-(n+1) * snm1(b % p^(n-1)), 0); S += mu * binomial(j, 2))); S + O(p^k);}
read("s81.gp");
sn(b) = S81[b];
z(b) = 0;
r = an2(3, 4, sn, z, -1, 0, 3);
print("LANE3_AN2 a_{4,2} = ", r, "   (3-adic, mod 27; exact value before truncation in p3_downstream.py)");
r5 = an2(3, 4, sn, z, -1, 0, 6);
print("LANE3_AN2 a_{4,2} mod 3^6 = ", r5, "  valuation ", valuation(r5, 3));
